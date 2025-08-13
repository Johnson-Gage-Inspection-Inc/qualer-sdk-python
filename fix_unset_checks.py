"""
Fix Unset checks to include truthiness validation.

This script replaces patterns like:
    if not isinstance(x, Unset):
with:
    if x and not isinstance(x, Unset):

This prevents operations on falsy values (None, empty strings, etc.) that aren't Unset.
"""

import os
import re


def fix_unset_checks_in_file(filepath):
    """Fix Unset checks in a single file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # Pattern to match: if not isinstance({variable}, Unset):
        # Capture the variable name and any whitespace/indentation
        pattern = r"(\s*)if not isinstance\(([^,\s]+), Unset\):"

        def replacement(match):
            indent = match.group(1)
            variable = match.group(2)
            return f"{indent}if {variable} and not isinstance({variable}, Unset):"

        content = re.sub(pattern, replacement, content)

        # Also update type hints: Union[Unset, T] -> Union[None, Unset, T]
        # Avoid adding None twice if it's already present as the first member
        content = re.sub(
            r"Union\s*\[(?!\s*None\s*,\s*Unset)\s*Unset",
            "Union[None, Unset",
            content,
        )

        # Only write if there were changes
        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            return True

        return False

    except Exception as e:
        print(f"⚠️  Error processing {filepath}: {e}")
        return False


def fix_unset_checks_in_directory(directory):
    """Fix Unset checks in all Python files in a directory."""
    fixed_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                if fix_unset_checks_in_file(filepath):
                    fixed_files.append(filepath)

    return fixed_files


def fix_unset_checks():
    """Fix Unset checks and Union types in the generated SDK."""
    print("🔧 Fixing Unset checks and Union[Unset,...] type hints (adding None)...")

    # Target directory for generated SDK
    sdk_dir = os.path.join("src", "qualer_sdk")

    if not os.path.exists(sdk_dir):
        print(f"⚠️  SDK directory {sdk_dir} not found, skipping fixes")
        return

    fixed_files = fix_unset_checks_in_directory(sdk_dir)

    if fixed_files:
        print(f"✅ Applied fixes in {len(fixed_files)} files")
    else:
        print("ℹ️  No fixes needed")


if __name__ == "__main__":
    fix_unset_checks()
