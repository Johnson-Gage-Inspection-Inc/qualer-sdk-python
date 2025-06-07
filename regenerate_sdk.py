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
OPENAPI_GENERATOR_JAR = "openapi-generator-cli.jar"
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

    # Apply the fix to avoid multiple schema issues
    fix_swagger_spec(SPEC_FILE, FIXED_SPEC_FILE)
    print("✅ Fixed multiple schema issues in specification.")

    # Save the original spec with our base patches
    with open(SPEC_FILE, "w", encoding="utf-8") as f:
        json.dump(spec, f, indent=2)
    print("✅ Cleaned up operationId prefixes.")


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
    if not os.path.exists(OPENAPI_GENERATOR_JAR):
        sys.exit(
            f"❌ OpenAPI Generator JAR not found: {OPENAPI_GENERATOR_JAR}"
        )  # Create a temporary directory for generation
    temp_dir = "temp_sdk_gen"  # Use OpenAPI Generator (typed output)
    command = [
        "java",
        "-jar",
        OPENAPI_GENERATOR_JAR,
        "generate",
        "-i",
        FIXED_SPEC_FILE,  # Use the fixed specification
        "-g",
        "python-nextgen",
        "-o",
        temp_dir,
        "--additional-properties=packageName=qualer_sdk,legacyDiscriminatorBehavior=true",
        "--skip-validate-spec",
    ]

    print("⚙️ Running OpenAPI Generator...")
    subprocess.run(command, check=True)

    # Clean previous SDK core files in the proper location
    if os.path.exists(OUTPUT_DIR):
        print(f"🧹 Cleaning previous SDK subfolders in {OUTPUT_DIR}")
        for sub in [
            "api",
            "models",
            "rest.py",
            "api_client.py",
            "configuration.py",
            "__init__.py",
        ]:
            path = os.path.join(OUTPUT_DIR, sub)
            if os.path.isdir(path):
                shutil.rmtree(path)
            elif os.path.isfile(path):
                os.remove(path)
    else:
        os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Copy the generated package contents to our clean structure
    temp_package_dir = os.path.join(temp_dir, "qualer_sdk")
    for item in [
        "api",
        "models",
        "rest.py",
        "api_client.py",
        "configuration.py",
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


if __name__ == "__main__":
    patch_spec()
    generate_sdk()

    print("🧹 Cleaning up auto-generated files...")
    # No need to remove setup.py from SDK folder since we use a temp directory now
    print("✅ SDK regeneration complete! Clean structure maintained.")
    print("✅ SDK regeneration complete! Clean structure maintained.")
