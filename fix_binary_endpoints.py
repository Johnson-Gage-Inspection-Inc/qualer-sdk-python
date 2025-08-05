#!/usr/bin/env python3
"""
Post-processing script to fix binary endpoint response parsing.

This script fixes the _parse_response functions in binary endpoints to properly
handle HTTP 200 responses by returning response.content instead of None.

This is needed because openapi-python-client doesn't properly handle binary
responses with "type": "string", "format": "binary" in the OpenAPI spec.
"""

import os
import re


def fix_binary_endpoint_file(file_path):
    """Fix a single binary endpoint file."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if this file needs fixing (has _parse_response)
    if "_parse_response" not in content:
        return False

    # Check if it already has correct 200 handling (return response.content)
    if (
        "response.status_code == 200" in content
        and "return response.content" in content
    ):
        return False

    # Pattern 1: Missing 200 handling entirely
    pattern1 = (
        r"(def _parse_response\(\s*\*,\s*client:\s*Union\[AuthenticatedClient,\s*Client\],\s*"
        r"response:\s*httpx\.Response\s*\)\s*->\s*Optional\[Any\]:\s*\n)"
    )
    replacement1 = (
        r"\1    if response.status_code == 200:\n        return response.content\n"
    )

    # Pattern 2: Wrong 200 handling with File(payload=BytesIO(response.json()))
    pattern2 = (
        r"(\s+if response\.status_code == 200:\s*\n)"
        r"(\s+response_200 = File\(payload=BytesIO\(response\.json\(\)\)\)\s*\n\s*\n)"
        r"(\s+return response_200\s*\n)"
    )
    replacement2 = r"\1        return response.content\n"

    # Try pattern 1 first (missing 200 handling)
    new_content = re.sub(pattern1, replacement1, content)

    # If that didn't change anything, try pattern 2 (wrong 200 handling)
    if new_content == content:
        new_content = re.sub(pattern2, replacement2, content, flags=re.MULTILINE)

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True

    return False


def fix_binary_endpoints():
    """Fix all binary endpoint files in the SDK."""
    # List of known binary endpoints that need fixing
    binary_endpoints = [
        "src/qualer_sdk/api/service_order_documents/get_document.py",
        "src/qualer_sdk/api/service_order_documents/get_document_get_wd.py",
        "src/qualer_sdk/api/service_order_items/get_work_item_image.py",
        "src/qualer_sdk/api/service_order_documents/get_documents.py",
        "src/qualer_sdk/api/service_order_item_documents/get_documents_get_2.py",
    ]

    fixed_count = 0

    for endpoint_file in binary_endpoints:
        if os.path.exists(endpoint_file):
            if fix_binary_endpoint_file(endpoint_file):
                print(f"✅ Fixed binary response handling in {endpoint_file}")
                fixed_count += 1
            else:
                print(f"⚪ No changes needed for {endpoint_file}")
        else:
            print(f"⚠️  File not found: {endpoint_file}")

    if fixed_count > 0:
        print(f"\n🎉 Fixed {fixed_count} binary endpoint files!")
    else:
        print("\n✨ All binary endpoints are already properly configured!")


if __name__ == "__main__":
    raise RuntimeError(
        "This script is not meant to be run directly. Please use the appropriate entry point."
    )
