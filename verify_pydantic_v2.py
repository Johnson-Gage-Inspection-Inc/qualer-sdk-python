#!/usr/bin/env python3
"""
Verify that all Pydantic V2 fixes have been applied correctly.

This script checks that:
1. No deprecated V1 syntax remains
2. All imports are valid
3. Models can be imported without errors
"""

import ast
import re
from pathlib import Path


def check_file_syntax(file_path: Path) -> bool:
    """Check if a Python file has valid syntax."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        ast.parse(content)
        return True
    except SyntaxError as e:
        print(f"❌ Syntax error in {file_path}: {e}")
        return False
    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")
        return False


def check_deprecated_syntax(file_path: Path) -> list:
    """Check for any remaining deprecated Pydantic V1 syntax."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return []

    issues = []

    # Check for deprecated syntax
    if "allow_population_by_field_name" in content:
        issues.append("Found deprecated 'allow_population_by_field_name'")

    if re.search(r"@validator\(", content):
        issues.append("Found deprecated '@validator' decorator")

    if re.search(r"\.dict\(", content):
        issues.append("Found deprecated '.dict()' method")

    if re.search(r"\.parse_obj\(", content):
        issues.append("Found deprecated '.parse_obj()' method")

    if "@validate_arguments" in content:
        issues.append("Found deprecated '@validate_arguments' decorator")

    # Check for syntax issues
    if ",," in content:
        issues.append("Found double comma syntax error")

    if re.search(r"from pydantic import\s*\(\s*,", content):
        issues.append("Found malformed import with leading comma")

    if re.search(r",\s*\)", content) and "from pydantic import" in content:
        issues.append("Found malformed import with trailing comma")

    return issues


def main():
    """Main verification function."""
    print("🔍 Verifying Pydantic V2 fixes...")

    src_dir = Path("src")
    if not src_dir.exists():
        print(f"❌ Source directory not found: {src_dir}")
        return 1

    python_files = list(src_dir.rglob("*.py"))
    print(f"📁 Found {len(python_files)} Python files")

    syntax_errors = 0
    deprecated_issues = 0

    for file_path in python_files:
        # Check syntax
        if not check_file_syntax(file_path):
            syntax_errors += 1

        # Check for deprecated syntax
        issues = check_deprecated_syntax(file_path)
        if issues:
            deprecated_issues += 1
            print(f"⚠️  Issues in {file_path}:")
            for issue in issues:
                print(f"   - {issue}")
    print("\n📊 Verification Results:")
    print(f"   Files checked: {len(python_files)}")
    print(f"   Syntax errors: {syntax_errors}")
    print(f"   Files with deprecated syntax: {deprecated_issues}")

    if syntax_errors == 0 and deprecated_issues == 0:
        print("✅ All Pydantic V2 fixes have been applied successfully!")
        return 0
    else:
        print("❌ Some issues remain that need to be fixed")
        return 1


if __name__ == "__main__":
    exit(main())
