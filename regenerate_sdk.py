"""
Regenerates the Qualer SDK from the patched Swagger spec.

Steps:
1. Downloads the OpenAPI spec from the Qualer server
2. Patches RecordType enum to support integer values
3. Regenerates the SDK using openapi-generator-cli
4. Applies custom templates for better maintainability (e.g., client.py with Api-Token prefix)
"""

import json
import os
import re
import shutil
import subprocess
import sys
from collections import defaultdict

from fix_binary_endpoints import fix_binary_endpoints
from fix_swagger_spec import fix_swagger_spec
from get_version import get_version_from_git_with_commits

SWAGGER_URL = "https://jgiquality.qualer.com/swagger/docs/v1"
SPEC_FILE = "spec.json"
FIXED_SPEC_FILE = "spec_fixed.json"
OUTPUT_DIR = os.path.join("src", "qualer_sdk")


def uniquify_operation_ids(spec):
    """Rename any operationId collisions by appending _{method}_{count}."""
    seen = defaultdict(int)

    for path, path_item in spec.get("paths", {}).items():
        for method, op in path_item.items():
            opid = op.get("operationId")
            if not opid:
                continue

            key = opid.lower()
            seen[key] += 1
            if seen[key] > 1:
                # e.g. “getAsset” → “getAsset_get_2”
                new_opid = f"{opid}_{method}_{seen[key]}"
                print(f"🔧 Renaming duplicate operationId {opid!r} → {new_opid!r}")
                op["operationId"] = new_opid


def patch_spec():
    print("Patching RecordType enum and operationIds...")
    with open(SPEC_FILE, "r", encoding="utf-8") as f:
        spec = json.load(f)

    # Patch RecordType enum
    target_def = spec["definitions"].get(
        "Qualer.Api.Models.Asset.To.AssetManageResponseModel"
    )
    if target_def and "RecordType" in target_def.get("properties", {}):
        target_def["properties"]["RecordType"] = {
            "type": "integer",
            "format": "int32",
            "enum": [0, 1, 2, 3],
            "x-enumNames": ["WaitingForAgreement", "Equipment", "System", "Agreement"],
        }
        print("Patched RecordType enum.")
    else:
        print("RecordType not found in expected definition.")
        sys.exit(1)

    # Fix nullable enums in spec definitions
    fix_nullable_enums_in_spec(spec)

    # Fix nullable date fields in spec definitions
    fix_nullable_dates_in_spec(spec)

    # Fix date-time parameters to accept string inputs
    fix_datetime_parameters_in_spec(spec)

    # Fix binary endpoints that incorrectly declare JSON responses
    fix_binary_endpoints_in_spec(spec)

    # Fix response format issues
    fix_response_format_issues_in_spec(spec)

    # Clean up redundant prefixes in operationIds
    for path_item in spec.get("paths", {}).values():
        for op in path_item.values():
            tags = op.get("tags", [])
            operation_id = op.get("operationId")
            if operation_id and tags:
                tag_prefix = f"{tags[0]}_"
                if operation_id.startswith(tag_prefix):
                    op["operationId"] = operation_id[len(tag_prefix) :]

    # Inject any path-template parameters that weren't declared
    inject_missing_path_params(spec)
    # Ensure operationIds are unique
    uniquify_operation_ids(spec)

    # Save the original spec with our base patches
    with open(SPEC_FILE, "w", encoding="utf-8") as f:
        json.dump(spec, f, indent=2)
    print("✅ Cleaned up operationId prefixes.")

    # Apply the fix to avoid multiple schema issues
    fix_swagger_spec(SPEC_FILE, FIXED_SPEC_FILE)
    print("✅ Fixed multiple schema issues in specification.")


def inject_missing_path_params(spec):
    """For each path like /foo/{X}/{y}, ensure X and y are declared as path params."""
    for path, path_item in spec.get("paths", {}).items():
        # Extract all parameters from the path template
        path_param_names = re.findall(r"\{([^/}]+)\}", path)

        # For each operation in this path
        for method, op in path_item.items():
            # Initialize parameters list if it doesn't exist
            op.setdefault("parameters", [])

            # Get the set of path parameter names already declared for this operation
            declared_for_op = {
                p["name"] for p in op.get("parameters", []) if p.get("in") == "path"
            }

            # Add any missing path parameters for this specific operation
            for name in path_param_names:
                if name not in declared_for_op:
                    param_obj = {
                        "name": name,
                        "in": "path",
                        "required": True,
                        "type": "string",
                    }
                    print(f"🔧 Injecting path-param {name!r} into {path!r} {method}")
                    op["parameters"].append(param_obj.copy())


def on_rm_error(func, path, exc_info):
    """Error handler for shutil.rmtree to handle Windows file locks."""
    import stat

    try:
        # Remove read-only flag and try again
        os.chmod(path, stat.S_IWRITE)
        func(path)
    except Exception:
        # If it still fails, just continue
        pass


def generate_sdk():
    # Create a temporary directory for generation
    temp_dir = "temp_sdk_gen"

    # Remove temporary directory if it exists
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir, onerror=on_rm_error)

    # Use openapi-python-client to generate the SDK
    command = [
        "openapi-python-client",
        "generate",
        "--path",
        "spec_openapi3.json",
        "--output-path",
        temp_dir,
        "--overwrite",
    ]

    print("⚙️ Running openapi-python-client...")
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ SDK generation failed: {e}")
        sys.exit(1)

    # Clean previous SDK core files in the proper location
    if os.path.exists(OUTPUT_DIR):
        print(f"🧹 Cleaning previous SDK subfolders in {OUTPUT_DIR}")
        for sub in [
            "api",
            "models",
            "client.py",
            "errors.py",
            "types.py",
            "__init__.py",
        ]:
            path = os.path.join(OUTPUT_DIR, sub)
            if os.path.isdir(path):
                shutil.rmtree(path, onerror=on_rm_error)
            elif os.path.isfile(path):
                try:
                    os.remove(path)
                except OSError:
                    pass  # Ignore if file is locked
    else:
        os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Find the generated package directory (openapi-python-client creates a package based on the spec title)
    generated_dirs = [
        d
        for d in os.listdir(temp_dir)
        if os.path.isdir(os.path.join(temp_dir, d)) and not d.startswith(".")
    ]
    if not generated_dirs:
        print("❌ No generated package directory found")
        sys.exit(1)

    temp_package_dir = os.path.join(temp_dir, generated_dirs[0])
    print(f"📦 Found generated package: {generated_dirs[0]}")

    # Copy the generated package contents to our clean structure
    for item in [
        "api",
        "models",
        "client.py",
        "errors.py",
        "types.py",
        "__init__.py",
    ]:
        src_path = os.path.join(temp_package_dir, item)
        dst_path = os.path.join(OUTPUT_DIR, item)
        if os.path.exists(src_path):
            if os.path.isdir(src_path):
                shutil.copytree(src_path, dst_path)
            else:
                shutil.copy2(src_path, dst_path)  # Add py.typed marker
    py_typed_path = os.path.join(OUTPUT_DIR, "py.typed")
    with open(py_typed_path, "w") as f:
        f.write("")  # Empty file to mark as typed package

    # Create custom exceptions file
    create_exceptions_file()

    # Create custom __init__.py file with proper imports
    create_custom_init_file()

    # Create API __init__.py file with all API imports
    create_api_init_file()

    # Create models __init__.py file with all model imports
    create_models_init_file()

    # Post-process generated files to fix known issues
    post_process_generated_files()

    # Format all generated files with black
    format_generated_files()

    # Clean up temporary directory
    shutil.rmtree(temp_dir, onerror=on_rm_error)
    print("✅ SDK regenerated successfully.")


def post_process_generated_files():
    """Fix known issues in generated files."""
    print("🔧 Post-processing generated files...")

    # Fix __init__.py to add version
    init_file = os.path.join(OUTPUT_DIR, "__init__.py")
    if os.path.exists(init_file):
        with open(init_file, "r", encoding="utf-8") as f:
            content = f.read()  # Add version at the top after the future import
        if "__version__" not in content:
            current_version = get_version_from_git_with_commits()
            lines = content.split("\n")
            # Find the line with "from __future__ import absolute_import"
            insert_idx = 0
            for i, line in enumerate(lines):
                if "from __future__ import absolute_import" in line:
                    insert_idx = i + 1
                    break

            lines.insert(insert_idx, "")
            lines.insert(insert_idx + 1, f'__version__ = "{current_version}"')

            content = "\n".join(lines)
            with open(init_file, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✅ Added __version__ = '{current_version}' to __init__.py")
    # Use custom client template with Api-Token as default prefix
    client_template_file = os.path.join("templates", "client_template.py")
    client_file = os.path.join(OUTPUT_DIR, "client.py")

    if os.path.exists(client_template_file) and os.path.exists(client_file):
        # Replace the generated client.py with our custom template
        with open(client_template_file, "r", encoding="utf-8") as f:
            template_content = f.read()

        with open(client_file, "w", encoding="utf-8") as f:
            f.write(template_content)
        print("✅ Applied custom client template with 'Api-Token' as default prefix")

    # Fix binary endpoints to properly handle HTTP 200 responses
    fix_binary_endpoints()

    # Fix nullable enums to properly handle None values
    fix_nullable_enums()

    # Fix nullable date parsing to handle None values
    fix_nullable_date_parsing()


def create_exceptions_file():
    """Create the exceptions.py file needed by the generated SDK code."""
    print("🔧 Creating exceptions.py file...")

    # Read the template exceptions file from the project root
    template_file = "templates/exceptions.py"
    if not os.path.exists(template_file):
        print(f"❌ Template file {template_file} not found")
        sys.exit(1)

    with open(template_file, "r", encoding="utf-8") as f:
        exceptions_content = f.read()

    exceptions_file = os.path.join(OUTPUT_DIR, "exceptions.py")
    with open(exceptions_file, "w", encoding="utf-8") as f:
        f.write(exceptions_content)

    print("✅ Created exceptions.py file")


def create_custom_init_file():
    """Create a custom __init__.py file with proper imports."""
    print("🔧 Creating custom __init__.py file...")

    # Read the template init file from the templates directory
    template_file = os.path.join("templates", "init_template.py")
    if not os.path.exists(template_file):
        print(f"❌ Template file {template_file} not found")
        sys.exit(1)

    with open(template_file, "r", encoding="utf-8") as f:
        init_content = f.read()

    init_file = os.path.join(OUTPUT_DIR, "__init__.py")
    with open(init_file, "w", encoding="utf-8") as f:
        f.write(init_content)

    print("✅ Created custom __init__.py file")


def create_api_init_file():
    """Create a proper __init__.py file for the API package with all API imports."""
    print("🔧 Creating API __init__.py file...")

    api_dir = os.path.join(OUTPUT_DIR, "api")
    if not os.path.exists(api_dir):
        print("⚠️  API directory not found, skipping API __init__.py creation")
        return

    # Get all API subdirectories
    api_subdirs = [
        f
        for f in os.listdir(api_dir)
        if os.path.isdir(os.path.join(api_dir, f)) and not f.startswith("__")
    ]

    api_imports = []

    for subdir in sorted(api_subdirs):
        subdir_path = os.path.join(
            api_dir, subdir
        )  # Get all Python files in this subdirectory (excluding __init__.py)
        api_files = [
            f
            for f in os.listdir(subdir_path)
            if f.endswith(".py") and f != "__init__.py"
        ]

        for api_file in api_files:
            # Create import for each function in the API file
            module_name = api_file[:-3]  # Remove .py
            api_imports.append(f"from .{subdir}.{module_name} import *")

    # Read the template API init file from the templates directory
    template_file = os.path.join("templates", "api_init_template.py")
    if not os.path.exists(template_file):
        print(f"❌ Template file {template_file} not found")
        sys.exit(1)

    with open(template_file, "r", encoding="utf-8") as f:
        api_init_content = f.read()

    # Replace the placeholder with actual imports
    api_init_content = api_init_content.format(api_imports="\n".join(api_imports))

    api_init_file = os.path.join(api_dir, "__init__.py")
    with open(api_init_file, "w", encoding="utf-8") as f:
        f.write(api_init_content)

    print(f"✅ Created API __init__.py with {len(api_subdirs)} API groups")


def create_models_init_file():
    """Create a proper __init__.py file for the models package with all model imports."""
    print("🔧 Creating models __init__.py file...")

    models_dir = os.path.join(OUTPUT_DIR, "models")
    if not os.path.exists(models_dir):
        print("⚠️  Models directory not found, skipping models __init__.py creation")
        return

    # Get all model files
    model_files = [
        f for f in os.listdir(models_dir) if f.endswith(".py") and f != "__init__.py"
    ]

    model_imports = []
    model_exports = []

    for model_file in sorted(model_files):
        # Convert filename to class name
        # (e.g., qualer_api_models_account_from_login_response_model.py -> QualerApiModelsAccountFromLoginResponseModel)
        module_name = model_file[
            :-3
        ]  # Remove .py        # Convert snake_case to PascalCase for class name
        class_name = "".join(word.capitalize() for word in module_name.split("_"))

        model_imports.append(f"from .{module_name} import {class_name}")
        model_exports.append(f'    "{class_name}",')

    # Read the template file
    template_file = os.path.join("templates", "models_init_template.py")
    if not os.path.exists(template_file):
        print(f"❌ Template file {template_file} not found")
        sys.exit(1)

    with open(template_file, "r", encoding="utf-8") as f:
        template_content = f.read()

    # Replace placeholders in template
    models_init_content = template_content.format(
        model_imports="\n".join(model_imports), model_exports="\n".join(model_exports)
    )

    models_init_file = os.path.join(models_dir, "__init__.py")
    with open(models_init_file, "w", encoding="utf-8") as f:
        f.write(models_init_content)

    print(f"✅ Created models __init__.py with {len(model_files)} model classes")


def format_generated_files():
    """Format all generated files using black."""

    format_files_with_autoflake()
    sort_imports_with_isort()
    format_generated_files_with_black()


def sort_imports_with_isort():
    print("🎨 Sorting imports with isort...")
    try:
        subprocess.run(
            ["isort", OUTPUT_DIR],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except FileNotFoundError:
        print("⚠️  isort not found. Install with: pip install isort")
        print("   Skipping import sorting...")


def format_files_with_autoflake():
    print("🎨 Formatting generated files with autoflake...")
    try:
        subprocess.run(
            [
                "autoflake",
                "--in-place",
                "--remove-all-unused-imports",
                "--remove-unused-variables",
                "--recursive",
                OUTPUT_DIR,
            ],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except FileNotFoundError:
        print("⚠️  Autoflake not found. Install with: pip install autoflake")
        print("   Skipping autoflake formatting...")


def format_generated_files_with_black():
    print("🎨 Formatting generated files with black...")

    try:
        # Run black on the entire SDK directory
        result = subprocess.run(
            ["black", OUTPUT_DIR],
            capture_output=True,
            text=True,
            encoding="utf-8",  # Explicitly specify UTF-8 encoding
            errors="replace",  # Replace problematic characters instead of failing
            check=False,  # Don't raise exception on non-zero exit code
        )

        if result.returncode == 0:
            print("✅ Code formatting completed successfully")
        else:
            print(f"⚠️  Black formatting had some issues: {result.stderr}")
            # Don't fail the entire process if black has issues

    except FileNotFoundError:
        print("⚠️  Black not found. Install with: pip install black")
        print("   Skipping code formatting...")
    except Exception as e:
        print(f"⚠️  Error running black: {e}")
        print("   Skipping code formatting...")


def convert_spec_to_openapi_v3():
    """Convert the fixed spec to OpenAPI v3 format."""
    print("🔄 Converting spec to OpenAPI v3 format...")

    try:
        subprocess.run(["prance", "convert", "spec_fixed.json", "spec_openapi3.json"])
        print("✅ Spec converted to OpenAPI v3 format.")
    except Exception as e:
        print(f"❌ Failed to convert spec to OpenAPI v3: {e}")
        sys.exit(1)


def fix_nullable_enums():
    """Fix nullable enum fields to properly handle None values in generated models."""
    print("🔧 Fixing nullable enum fields...")

    models_dir = os.path.join(OUTPUT_DIR, "models")
    if not os.path.exists(models_dir):
        print("⚠️  Models directory not found, skipping nullable enum fixes")
        return

    # List of known nullable enum fields that need fixing
    nullable_enum_patterns = [
        # Pattern: (enum_var_name, enum_class_pattern)
        ("service_order_status", "ServiceOrderStatus"),
        ("as_found_result", "AsFoundResult"),
        ("as_left_result", "AsLeftResult"),
        ("result_status", "ResultStatus"),
        ("due_status", "DueStatus"),
        ("work_status", "WorkStatus"),
        ("tool_role", "ToolRole"),
        ("record_type", "RecordType"),
        ("as_found_measurement_not_taken_result", "AsFoundMeasurementNotTakenResult"),
        ("guard_band_logic", "GuardBandLogic"),
        ("influence_parameter_1_type", "InfluenceParameter1Type"),
        ("process_date_option", "ProcessDateOption"),
        ("reading_entry_logic", "ReadingEntryLogic"),
    ]

    fixed_files = []

    for filename in os.listdir(models_dir):
        if not filename.endswith(".py"):
            continue

        filepath = os.path.join(models_dir, filename)

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            original_content = content

            # Fix each nullable enum pattern
            for var_name, enum_class_suffix in nullable_enum_patterns:
                # Fix 1: Update type annotations to include None
                # Look for: var_name: Union[Unset, EnumClass]
                # Replace with: var_name: Union[None, Unset, EnumClass]
                type_annotation_pattern = rf"(\s+){var_name}: Union\[Unset, ([^\]]+)\]"
                type_match = re.search(type_annotation_pattern, content)
                if type_match and "None" not in type_match.group(0):
                    old_annotation = type_match.group(0)
                    new_annotation = f"{type_match.group(1)}{var_name}: Union[None, Unset, {type_match.group(2)}]"
                    content = content.replace(old_annotation, new_annotation)
                    print(f"✅ Fixed {var_name} type annotation in {filename}")

                # Fix 2: Update constructor parameters to include None
                # Look for: var_name: Union[Unset, EnumClass] = UNSET,
                # Replace with: var_name: Union[None, Unset, EnumClass] = UNSET,
                constructor_param_pattern = (
                    rf"(\s+){var_name}: Union\[Unset, ([^\]]+)\](\s*=\s*UNSET,?)"
                )
                constructor_match = re.search(constructor_param_pattern, content)
                if constructor_match and "None" not in constructor_match.group(0):
                    old_param = constructor_match.group(0)
                    new_param = (
                        f"{constructor_match.group(1)}{var_name}: Union[None, Unset, "
                        f"{constructor_match.group(2)}]{constructor_match.group(3)}"
                    )
                    content = content.replace(old_param, new_param)
                    print(f"✅ Fixed {var_name} constructor parameter in {filename}")

                # Fix 3: Update from_dict parsing logic
                # Look for the specific pattern that needs fixing:
                # if isinstance(_var_name, Unset):
                #     var_name = UNSET
                # else:
                #     var_name = EnumClass(_var_name)
                old_pattern = (
                    rf"(\s+)if isinstance\(_{var_name}, Unset\):\s*\n"
                    rf"(\s+){var_name} = UNSET\s*\n"
                    rf"(\s+)else:\s*\n"
                    rf"(\s+){var_name} = (\s*\n\s*)?([^(]+\(\s*_{var_name}\s*\))"
                )

                # Find the pattern
                match = re.search(old_pattern, content, re.MULTILINE | re.DOTALL)
                if match:
                    # Check if it already has the None check
                    full_match = match.group(0)
                    if f"elif _{var_name} is None:" not in full_match:
                        # Extract indentation from the captured groups
                        indent1 = match.group(1)
                        indent2 = match.group(2)
                        indent3 = match.group(3)
                        indent4 = match.group(4)
                        # Get the enum constructor, handling multi-line cases
                        enum_constructor = match.group(6).strip()

                        # Create the replacement with proper indentation
                        replacement = (
                            f"{indent1}if isinstance(_{var_name}, Unset):\n"
                            f"{indent2}{var_name} = UNSET\n"
                            f"{indent3}elif _{var_name} is None:\n"
                            f"{indent4}{var_name} = None\n"
                            f"{indent3}else:\n"
                            f"{indent4}{var_name} = {enum_constructor}"
                        )

                        content = content.replace(full_match, replacement)
                        print(f"✅ Fixed {var_name} from_dict parsing in {filename}")

                # Fix 4: Update to_dict serialization logic
                # Look for: var_name = self.var_name
                # Replace with proper None handling
                to_dict_pattern = rf"(\s+){var_name} = self\.{var_name}\s*\n"
                to_dict_match = re.search(to_dict_pattern, content)
                if to_dict_match:
                    old_to_dict = to_dict_match.group(0)
                    indent = to_dict_match.group(1)
                    new_to_dict = (
                        f"{indent}{var_name}: Union[None, Unset, str]\n"
                        f"{indent}if isinstance(self.{var_name}, Unset):\n"
                        f"{indent}    {var_name} = UNSET\n"
                        f"{indent}else:\n"
                        f"{indent}    {var_name} = self.{var_name}\n"
                    )
                    content = content.replace(old_to_dict, new_to_dict)
                    print(f"✅ Fixed {var_name} to_dict serialization in {filename}")

            # Save the file if it was modified
            if content != original_content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                fixed_files.append(filename)

        except Exception as e:
            print(f"⚠️  Error processing {filename}: {e}")
            continue

    if fixed_files:
        print(
            f"✅ Fixed nullable enums in {len(fixed_files)} files: {', '.join(fixed_files)}"
        )
    else:
        print("ℹ️  No nullable enum fixes needed")


def fix_nullable_enums_in_spec(spec):
    """Fix enum definitions to allow None values where appropriate."""
    print("🔧 Fixing nullable enum definitions in spec...")

    # Known enum fields that can be None and the values that should be allowed
    nullable_enum_fixes = {
        # WorkStatus enum - add None as valid value
        "WorkStatus": {
            "nullable": True,
            "additional_values": [
                None,
                0,
                1,
                2,
                3,
                4,
                5,
            ],  # Pending=0, InProgress=1, Completed=2, etc.
        },
        # ServiceOrderStatus enum
        "ServiceOrderStatus": {
            "nullable": True,
            "additional_values": [None, 0, 1, 2, 3, 4, 5],
        },
        # ResultStatus enum
        "ResultStatus": {
            "nullable": True,
            "additional_values": [
                None,
                0,
                1,
                2,
                10,
                11,
                20,
                21,
                22,
            ],  # NotAvailable=0, Fail=1, Pass=2, etc.
        },
        # ProcessDateOption enum
        "ProcessDateOption": {
            "nullable": True,
            "additional_values": [None, 0, 1, 2, 3],
        },
        # MeasurementType enum
        "MeasurementType": {
            "nullable": True,
            "additional_values": [None, 0, 1, 2, 3, 4, 5],
        },
        # InfluenceParameter1Type enum
        "InfluenceParameter1Type": {
            "nullable": True,
            "additional_values": [None, 0, 1, 2, 3],
        },
        # AsFoundMeasurementNotTakenResult enum
        "AsFoundMeasurementNotTakenResult": {
            "nullable": True,
            "additional_values": [None, 0, 1, 2, 3],
        },
        # GuardBandLogic enum
        "GuardBandLogic": {
            "nullable": True,
            "additional_values": [None, 0, 1, 2, 3],
        },
        # ReadingEntryLogic enum
        "ReadingEntryLogic": {
            "nullable": True,
            "additional_values": [None, 0, 1, 2, 3],
        },
    }

    fixed_enums = []

    # Traverse all definitions to find and fix enum fields
    for def_name, definition in spec.get("definitions", {}).items():
        if isinstance(definition, dict) and "properties" in definition:
            for prop_name, prop_def in definition["properties"].items():
                if isinstance(prop_def, dict):
                    # Check if this property has an enum that we need to fix
                    enum_values = prop_def.get("enum")

                    # Look for enum properties that match our patterns
                    for enum_pattern, fix_info in nullable_enum_fixes.items():
                        if enum_pattern.lower() in prop_name.lower() or (
                            enum_values
                            and any(enum_pattern in str(val) for val in enum_values)
                        ):

                            # Make the enum nullable and add missing values
                            if enum_values:
                                # Convert enum to integer type with nullable
                                prop_def["type"] = "integer"
                                prop_def["format"] = "int32"
                                prop_def["nullable"] = True

                                # Add the additional enum values if not present
                                current_values = set(enum_values)
                                for new_val in fix_info["additional_values"]:
                                    if new_val not in current_values:
                                        current_values.add(new_val)

                                # Sort values, handling mixed types safely
                                non_none_values = [
                                    v for v in current_values if v is not None
                                ]
                                # Separate integers and strings for sorting
                                int_values = sorted(
                                    [v for v in non_none_values if isinstance(v, int)]
                                )
                                str_values = sorted(
                                    [v for v in non_none_values if isinstance(v, str)]
                                )
                                prop_def["enum"] = int_values + str_values + [None]
                                fixed_enums.append(f"{def_name}.{prop_name}")
                                break

    if fixed_enums:
        print(
            f"✅ Fixed nullable enums: {', '.join(fixed_enums[:5])}{'...' if len(fixed_enums) > 5 else ''}"
        )
    else:
        print("ℹ️  No nullable enum fixes needed")


def fix_datetime_parameters_in_spec(spec):
    """Fix date-time parameters to properly handle string inputs."""
    print("🔧 Fixing date-time parameters in spec...")

    fixed_params = []

    for path, path_item in spec.get("paths", {}).items():
        for method, operation in path_item.items():
            if isinstance(operation, dict) and "parameters" in operation:
                for param in operation["parameters"]:
                    if (
                        isinstance(param, dict)
                        and param.get("type") == "string"
                        and param.get("format") == "date-time"
                    ):

                        # Keep as string but remove the strict date-time format requirement
                        # This allows the generated code to accept string inputs
                        param["type"] = "string"
                        # Remove format to be less strict about the exact format
                        if "format" in param:
                            del param["format"]

                        # Add pattern to indicate expected format
                        param["pattern"] = r"^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2})?$"
                        param["x-python-type"] = "Union[str, datetime.datetime]"

                        fixed_params.append(
                            f"{path}:{method}:{param.get('name', 'unknown')}"
                        )

    if fixed_params:
        print(f"✅ Fixed {len(fixed_params)} date-time parameters")
    else:
        print("ℹ️  No date-time parameter fixes needed")


def fix_binary_endpoints_in_spec(spec):
    """Fix endpoints that return binary data but are marked as JSON."""
    print("🔧 Fixing binary endpoints in spec...")

    # Known endpoints that return binary data but are incorrectly marked as JSON
    binary_endpoints = [
        "/api/service/workorders/{serviceOrderId}/documents",
        "/api/service/workitems/{serviceOrderItemId}/documents",
        "/api/assetservicerecords/{AssetServiceRecordId}/documents/files",
    ]

    fixed_endpoints = []

    for path, path_item in spec.get("paths", {}).items():
        # Check if this path might return binary data
        is_binary_path = any(
            binary_pattern in path for binary_pattern in binary_endpoints
        )

        if is_binary_path:
            for method, operation in path_item.items():
                if isinstance(operation, dict) and "responses" in operation:
                    for status_code, response_def in operation["responses"].items():
                        if (
                            isinstance(response_def, dict)
                            and "schema" in response_def
                            and status_code == "200"
                        ):

                            # Check if this claims to return JSON but should be binary
                            produces = operation.get("produces", [])
                            if any("json" in prod for prod in produces):
                                # This is likely a binary endpoint mismarked as JSON
                                # Update the response schema to indicate binary
                                response_def["schema"] = {
                                    "type": "string",
                                    "format": "binary",
                                }

                                # Update produces to indicate binary content
                                operation["produces"] = [
                                    "application/octet-stream",
                                    "application/pdf",
                                    "application/zip",
                                ]

                                fixed_endpoints.append(f"{path}:{method}")

    if fixed_endpoints:
        print(f"✅ Fixed {len(fixed_endpoints)} binary endpoints")
    else:
        print("ℹ️  No binary endpoint fixes needed")


def fix_nullable_dates_in_spec(spec):
    """Fix date fields that can be None but are being parsed as required."""
    print("🔧 Fixing nullable date fields in spec...")

    fixed_dates = []

    # Traverse all definitions to find and fix date fields
    for def_name, definition in spec.get("definitions", {}).items():
        if isinstance(definition, dict) and "properties" in definition:
            for prop_name, prop_def in definition["properties"].items():
                if isinstance(prop_def, dict):
                    # Look for date fields that should be nullable
                    prop_type = prop_def.get("type")
                    prop_format = prop_def.get("format")

                    # Check if this is a date/datetime field
                    if (
                        prop_type == "string"
                        and prop_format in ["date", "date-time"]
                        and ("date" in prop_name.lower() or "time" in prop_name.lower())
                    ):

                        # Make the field nullable
                        prop_def["nullable"] = True
                        prop_def["x-nullable"] = True
                        fixed_dates.append(f"{def_name}.{prop_name}")

    if fixed_dates:
        print(f"✅ Fixed {len(fixed_dates)} nullable date fields")
    else:
        print("ℹ️  No nullable date field fixes needed")


def fix_nullable_date_parsing():
    """Fix date parsing to handle None values properly in generated models."""
    print("🔧 Fixing nullable date parsing in models...")

    models_dir = os.path.join(OUTPUT_DIR, "models")
    if not os.path.exists(models_dir):
        print("⚠️  Models directory not found, skipping date parsing fixes")
        return

    fixed_files = []

    for filename in os.listdir(models_dir):
        if not filename.endswith(".py"):
            continue

        filepath = os.path.join(models_dir, filename)

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            original_content = content

            # Look for patterns like: var_name = isoparse(_var_name)
            # Replace with proper None handling
            isoparse_pattern = r"(\s+)(\w+) = isoparse\((_\w+)\)"

            def replace_isoparse(match):
                indent = match.group(1)
                var_name = match.group(2)
                source_var = match.group(3)

                return (
                    f"{indent}if {source_var} is None:\n"
                    f"{indent}    {var_name} = None\n"
                    f"{indent}else:\n"
                    f"{indent}    {var_name} = isoparse({source_var})"
                )

            new_content = re.sub(isoparse_pattern, replace_isoparse, content)

            if new_content != content:
                content = new_content
                fixed_files.append(filename)

            # Save the file if it was modified
            if content != original_content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)

        except Exception as e:
            print(f"⚠️  Error processing {filename}: {e}")
            continue

    if fixed_files:
        ellipsis = "..." if len(fixed_files) > 5 else ""
        print(
            f"✅ Fixed date parsing in {len(fixed_files)} files: {', '.join(fixed_files[:5])}{ellipsis}"
        )
    else:
        print("ℹ️  No date parsing fixes needed")


def fix_response_format_issues_in_spec(spec):
    """Fix endpoints that have incorrect response format definitions."""
    print("🔧 Fixing response format issues in spec...")

    fixed_responses = []

    # Known endpoints with response format issues
    problem_endpoints = {
        "/api/service/workitems/{workItemId}/tasks": {
            "expected_format": "array_of_objects",
            "current_issue": "incorrect_schema",
        }
    }

    for path, path_item in spec.get("paths", {}).items():
        if path in problem_endpoints:
            for method, operation in path_item.items():
                if isinstance(operation, dict) and "responses" in operation:
                    response_200 = operation["responses"].get("200")
                    if response_200 and "schema" in response_200:
                        # For the work item tasks endpoint, ensure it returns an array
                        if "tasks" in path:
                            response_200["schema"] = {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "additionalProperties": True,
                                },
                            }
                            fixed_responses.append(f"{path}:{method}")

    if fixed_responses:
        print(f"✅ Fixed {len(fixed_responses)} response format issues")
    else:
        print("ℹ️  No response format fixes needed")


if __name__ == "__main__":
    patch_spec()
    convert_spec_to_openapi_v3()
    generate_sdk()

    print("🧹 Cleaning up auto-generated files...")
    # Delete spec_fixed.json and spec_openapi3.json
    if os.path.exists(FIXED_SPEC_FILE):
        os.remove(FIXED_SPEC_FILE)
    OPENAPI_V3_SPEC_FILE = "spec_openapi3.json"
    if os.path.exists(OPENAPI_V3_SPEC_FILE):
        os.remove(OPENAPI_V3_SPEC_FILE)
    print("✅ SDK regeneration complete! Clean structure maintained.")
