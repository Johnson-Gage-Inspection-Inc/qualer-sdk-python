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

    # Check if this file needs fixing (has _parse_response but no 200 handling)
    if "_parse_response" not in content:
        return False

    # Check if it already has 200 handling
    if "response.status_code == 200" in content:
        return False

    # Pattern to match the _parse_response function
    pattern = (
        r"(def _parse_response\(\s*\*,\s*client:\s*Union\[AuthenticatedClient,\s*Client\],\s*"
        r"response:\s*httpx\.Response\s*\)\s*->\s*Optional\[Any\]:\s*\n)"
    )

    # Replacement that adds 200 handling
    replacement = (
        r"\1    if response.status_code == 200:\n        return response.content\n"
    )

    new_content = re.sub(pattern, replacement, content)

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
    fix_binary_endpoints()
