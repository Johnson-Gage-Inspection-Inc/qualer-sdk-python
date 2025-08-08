#!/usr/bin/env python3
"""
Post-processing script to fix deprecated cgi module imports.

This script replaces uses of the deprecated cgi.parse_header() function
with a manual implementation to ensure compatibility with Python 3.13+.
"""

import os
import re


def fix_cgi_import_file(file_path):
    """Fix cgi imports in a single file."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if this file uses cgi.parse_header
    if "import cgi" not in content or "cgi.parse_header" not in content:
        return False

    print(f"🔧 Fixing cgi import in {file_path}")

    # Replace the cgi import and parse_header usage
    old_pattern = (
        r"(\s+)# Extract filename from Content-Disposition header if present\s*\n"
        r"\s+import cgi\s*\n"
        r"(\s+from io import BytesIO\s*\n)"
        r"(\s+from urllib\.parse import unquote\s*\n)"
        r"\s*\n"
        r"(\s+content_disposition = response\.headers\.get\(['\"]Content-Disposition['\"], ['\"]['\"].*?\)\s*\n)"
        r"(\s+filename = None\s*\n)"
        r"(\s+if content_disposition:\s*\n)"
        r"(\s+value, params = cgi\.parse_header\(content_disposition\))"
    )

    replacement = (
        r"\1# Extract filename from Content-Disposition header if present\n"
        r"\2"  # from io import BytesIO
        r"\3"  # from urllib.parse import unquote
        r"\n"
        r"\4"  # content_disposition = ...
        r"\5"  # filename = None
        r"\6"  # if content_disposition:
        r"\1    # Parse header manually to avoid deprecated cgi module\n"
        r"\1    value = content_disposition.split(';')[0].strip()\n"
        r"\1    params = {}\n"
        r"\1    for part in content_disposition.split(';')[1:]:\n"
        r"\1        if '=' in part:\n"
        r"\1            key, val = part.split('=', 1)\n"
        r"\1            params[key.strip()] = val.strip(' \"\\'')\n"
        r"\1    value, params = value, params"
    )

    # Try the complex pattern first
    new_content = re.sub(
        old_pattern, replacement, content, flags=re.MULTILINE | re.DOTALL
    )

    # If that didn't work, try a simpler pattern
    if new_content == content:
        # Simple pattern just for the cgi.parse_header line
        simple_pattern = (
            r"(\s+)value, params = cgi\.parse_header\(content_disposition\)"
        )
        simple_replacement = (
            r"\1# Parse header manually to avoid deprecated cgi module\n"
            r"\1value = content_disposition.split(';')[0].strip()\n"
            r"\1params = {}\n"
            r"\1for part in content_disposition.split(';')[1:]:\n"
            r"\1    if '=' in part:\n"
            r"\1        key, val = part.split('=', 1)\n"
            r"\1        params[key.strip()] = val.strip(' \"\\'')\n"
            r"\1value, params = value, params"
        )
        new_content = re.sub(
            simple_pattern, simple_replacement, content, flags=re.MULTILINE
        )

        # Remove the cgi import line
        if new_content != content:
            new_content = re.sub(r"\s+import cgi\s*\n", "", new_content)

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"✅ Fixed cgi import in {file_path}")
        return True
    else:
        print(f"⚠️  Could not fix cgi import in {file_path}")
        return False


def fix_cgi_imports():
    """Fix cgi imports in all generated SDK files."""
    print("🔧 Fixing deprecated cgi module imports...")

    src_dir = os.path.join("src", "qualer_sdk")
    if not os.path.exists(src_dir):
        print("⚠️  SDK source directory not found")
        return

    fixed_count = 0

    # Walk through all Python files in the SDK
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                if fix_cgi_import_file(file_path):
                    fixed_count += 1

    if fixed_count > 0:
        print(f"✅ Fixed cgi imports in {fixed_count} files")
    else:
        print("ℹ️  No cgi imports found to fix")


if __name__ == "__main__":
    fix_cgi_imports()
