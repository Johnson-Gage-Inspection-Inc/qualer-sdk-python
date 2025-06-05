"""
Regenerates the Qualer SDK from the patched Swagger spec.

Steps:
1. Downloads the OpenAPI spec from the Qualer server
2. Patches RecordType enum to support integer values
3. Regenerates the SDK using swagger-codegen-cli
"""

import os
import subprocess
import sys
import json
import shutil

SWAGGER_URL = "https://jgiquality.qualer.com/swagger/docs/v1"
SWAGGER_CODEGEN_JAR = "swagger-codegen-cli-2.4.21.jar"
SPEC_FILE = "spec.json"
OUTPUT_DIR = os.path.join("src", "qualer_sdk")


def patch_spec():
    print("🛠️ Patching RecordType enum and operationIds...")
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

    with open(SPEC_FILE, "w", encoding="utf-8") as f:
        json.dump(spec, f, indent=2)
    print("✅ Cleaned up operationId prefixes.")


def generate_sdk():
    if not os.path.exists(SWAGGER_CODEGEN_JAR):
        sys.exit(f"❌ Swagger Codegen JAR not found: {SWAGGER_CODEGEN_JAR}")

    # Create a temporary directory for generation
    temp_dir = "temp_sdk_gen"

    command = [
        "java",
        "-jar",
        SWAGGER_CODEGEN_JAR,
        "generate",
        "-i",
        SPEC_FILE,
        "-l",
        "python",
        "-o",
        temp_dir,
        "--additional-properties=packageName=qualer_sdk",
    ]

    print("⚙️ Running Swagger Codegen...")
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
                shutil.copy2(src_path, dst_path)

    # Add py.typed marker
    py_typed_path = os.path.join(OUTPUT_DIR, "py.typed")
    with open(py_typed_path, "w") as f:
        f.write("")  # Empty file to mark as typed package

    # Clean up temporary directory
    shutil.rmtree(temp_dir)
    print("✅ SDK regenerated successfully.")


if __name__ == "__main__":
    patch_spec()
    generate_sdk()

    print("🧹 Cleaning up auto-generated files...")
    # No need to remove setup.py from SDK folder since we use a temp directory now
    print("✅ SDK regeneration complete! Clean structure maintained.")
