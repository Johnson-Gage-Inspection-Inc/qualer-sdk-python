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
                # Look for the specific pattern that needs fixing:
                # if isinstance(_var_name, Unset):
                #     var_name = UNSET
                # else:
                #     var_name = EnumClass(_var_name)

                # This pattern should be replaced with:
                # if isinstance(_var_name, Unset):
                #     var_name = UNSET
                # elif _var_name is None:
                #     var_name = None
                # else:
                #     var_name = EnumClass(_var_name)

                # Use a more flexible pattern that handles multi-line enum constructors
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
                        print(f"✅ Fixed {var_name} nullable enum in {filename}")

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
