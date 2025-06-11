"""
Regenerates the Qualer SDK from the patched Swagger spec.

Steps:
1. Downloads the OpenAPI spec from the Qualer server
2. Patches RecordType enum to support integer values
3. Regenerates the SDK using openapi-generator-cli
"""

import json
import os
import re
import shutil
import subprocess
import sys
from collections import defaultdict

from fix_swagger_spec import fix_swagger_spec

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
        print("✅ Patched RecordType enum.")
    else:
        print("⚠️  RecordType not found in expected definition.")
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


def generate_sdk():
    # Create a temporary directory for generation
    temp_dir = "temp_sdk_gen"

    # Remove temporary directory if it exists
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)

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
                shutil.rmtree(path)
            elif os.path.isfile(path):
                os.remove(path)
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
    shutil.rmtree(temp_dir)
    print("✅ SDK regenerated successfully.")


def post_process_generated_files():
    """Fix known issues in generated files."""
    print("🔧 Post-processing generated files...")

    # Fix __init__.py to add version
    init_file = os.path.join(OUTPUT_DIR, "__init__.py")
    if os.path.exists(init_file):
        with open(init_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Add version at the top after the future import
        if "__version__" not in content:
            lines = content.split("\n")
            # Find the line with "from __future__ import absolute_import"
            insert_idx = 0
            for i, line in enumerate(lines):
                if "from __future__ import absolute_import" in line:
                    insert_idx = i + 1
                    break

            lines.insert(insert_idx, "")
            lines.insert(insert_idx + 1, '__version__ = "2.2.1"')

            content = "\n".join(lines)
            with open(init_file, "w", encoding="utf-8") as f:
                f.write(content)
            print("✅ Added __version__ to __init__.py")


def create_exceptions_file():
    """Create the exceptions.py file needed by the generated SDK code."""
    print("🔧 Creating exceptions.py file...")

    # Read the template exceptions file from the project root
    template_file = "exceptions.py"
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

    init_content = '''# coding: utf-8

# flake8: noqa

"""
Qualer SDK

Python SDK for the Qualer API.
Generated by openapi-python-client
"""

__version__ = "2.2.1"

# Import core classes using relative imports
from .client import Client
from .errors import UnexpectedStatus
from .types import Response

# Import API and models modules using relative imports to avoid circular imports
from . import api, models

__all__ = [
    "Client",
    "UnexpectedStatus",
    "Response", 
    "api",
    "models",
]
'''

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

    api_init_content = f'''# coding: utf-8

# flake8: noqa

"""
Qualer SDK API Classes

This module provides access to all API functions.
Generated by openapi-python-client
"""

# Import all API functions
{"\n".join(api_imports)}

# Re-export everything imported
__all__ = []
'''

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
        # Convert filename to class name (e.g., qualer_api_models_account_from_login_response_model.py -> QualerApiModelsAccountFromLoginResponseModel)
        module_name = model_file[
            :-3
        ]  # Remove .py        # Convert snake_case to PascalCase for class name
        class_name = "".join(word.capitalize() for word in module_name.split("_"))

        model_imports.append(f"from .{module_name} import {class_name}")
        model_exports.append(f'    "{class_name}",')

    models_init_content = f'''# coding: utf-8

# flake8: noqa

"""
Qualer SDK Model Classes

This module provides access to all model classes.
Generated by OpenAPI Generator (https://openapi-generator.tech)

The version of the OpenAPI document: v1
"""

# Import all model classes
{"\n".join(model_imports)}

__all__ = [
{"\n".join(model_exports)}
]
'''

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


if __name__ == "__main__":
    patch_spec()
    convert_spec_to_openapi_v3()
    generate_sdk()

    print("🧹 Cleaning up auto-generated files...")
    print("✅ SDK regeneration complete! Clean structure maintained.")
