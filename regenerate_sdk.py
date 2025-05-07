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
import urllib.request
import shutil

SWAGGER_URL = "https://jgiquality.qualer.com/swagger/docs/v1"
SWAGGER_CODEGEN_JAR = "swagger-codegen-cli-2.4.21.jar"
SPEC_FILE = "spec.json"
OUTPUT_DIR = "qualer_sdk"


def download_spec():
    print(f"📥 Downloading spec from {SWAGGER_URL}")
    urllib.request.urlretrieve(SWAGGER_URL, SPEC_FILE)
    print("✅ Downloaded spec.json")


def patch_spec():
    print("🛠️ Patching RecordType enum...")
    with open(SPEC_FILE, "r", encoding="utf-8") as f:
        spec = json.load(f)

    target_def = spec["definitions"][
        "Qualer.Api.Models.Asset.To.AssetManageResponseModel"
        ]
    if "RecordType" in target_def["properties"]:
        target_def["properties"]["RecordType"] = {
            "type": "integer",
            "format": "int32",
            "enum": [0, 1, 2, 3],
            "x-enumNames": [
                "WaitingForAgreement",
                "Equipment",
                "System",
                "Agreement"
            ]
        }
        with open(SPEC_FILE, "w", encoding="utf-8") as f:
            json.dump(spec, f, indent=2)
        print("✅ Patched RecordType enum.")
    else:
        print("⚠️  RecordType not found in expected definition.")
        sys.exit(1)


def generate_sdk():
    if not os.path.exists(SWAGGER_CODEGEN_JAR):
        sys.exit(f"❌ Swagger Codegen JAR not found: {SWAGGER_CODEGEN_JAR}")

    if os.path.exists(OUTPUT_DIR):
        print(f"🧹 Cleaning previous SDK at {OUTPUT_DIR}")
        shutil.rmtree(OUTPUT_DIR)

    command = [
        "java", "-jar", SWAGGER_CODEGEN_JAR,
        "generate",
        "-i", SPEC_FILE,
        "-l", "python",
        "-o", OUTPUT_DIR
    ]

    print("⚙️ Running Swagger Codegen...")
    subprocess.run(command, check=True)
    print("✅ SDK regenerated successfully.")


if __name__ == "__main__":
    download_spec()
    patch_spec()
    generate_sdk()
