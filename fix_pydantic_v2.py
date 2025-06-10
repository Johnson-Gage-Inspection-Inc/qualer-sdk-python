#!/usr/bin/env python3
"""
Fix Pydantic V2 deprecation warnings in the Qualer SDK.

This script updates the generated SDK code to use Pydantic V2 syntax:
- allow_population_by_field_name → populate_by_name
- @validator → @field_validator
- validate_arguments → validate_call
- parse_obj → model_validate
- .dict() → .model_dump()

Run this after regenerating the SDK to ensure Pydantic V2 compatibility.
"""

import ast
import os
import re
from pathlib import Path
from typing import List


class PydanticV2Fixer:
    """Fix Pydantic V1 to V2 deprecation warnings in Python files."""

    def __init__(self, src_dir: str = "src"):
        self.src_dir = Path(src_dir)
        self.fixes_applied = 0

    def fix_file(self, file_path: Path) -> bool:
        """Fix a single Python file. Returns True if changes were made."""
        if not file_path.suffix == ".py":
            return False

        print(f"Processing {file_path}")

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return False

        original_content = content

        # Fix imports
        content = self._fix_imports(content)

        # Fix Config class
        content = self._fix_config_class(content)

        # Fix validators
        content = self._fix_validators(content)

        # Fix method calls
        content = self._fix_method_calls(content)

        # Write back if changed
        if content != original_content:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                self.fixes_applied += 1
                print(f"  ✅ Fixed {file_path}")
                return True
            except Exception as e:
                print(f"Error writing {file_path}: {e}")
                return False
        else:
            print(f"  ⏭️  No changes needed for {file_path}")
            return False

    def _fix_imports(self, content: str) -> str:
        """Fix import statements."""
        # Replace validate_arguments with validate_call
        content = re.sub(
            r"from pydantic import ([^,\n]*,?\s*)?validate_arguments([,\s][^,\n]*)?",
            lambda m: f'from pydantic import {m.group(1) or ""}validate_call{m.group(2) or ""}',
            content,
        )

        # Add field_validator import when @validator is used
        if "@validator(" in content:
            # Check if field_validator is already imported
            if "field_validator" not in content:
                # Add field_validator to existing pydantic import
                content = re.sub(
                    r"from pydantic import ([^\n]+)",
                    r"from pydantic import \1, field_validator",
                    content,
                    count=1,
                )

        return content

    def _fix_config_class(self, content: str) -> str:
        """Fix Pydantic Config class settings."""
        # Replace allow_population_by_field_name with populate_by_name
        content = re.sub(
            r"allow_population_by_field_name\s*=\s*True",
            "populate_by_name = True",
            content,
        )

        return content

    def _fix_validators(self, content: str) -> str:
        """Fix @validator decorators to @field_validator."""
        # Pattern to match @validator("field_name") decorator
        validator_pattern = r"@validator\(([^)]+)\)"

        def replace_validator(match):
            field_spec = match.group(1)
            # For field validators, we need to add mode parameter
            return f'@field_validator({field_spec}, mode="before")'

        content = re.sub(validator_pattern, replace_validator, content)

        return content

    def _fix_method_calls(self, content: str) -> str:
        """Fix deprecated method calls."""
        # Replace validate_arguments decorator with validate_call
        content = re.sub(r"@validate_arguments", "@validate_call", content)

        # Replace parse_obj with model_validate
        content = re.sub(r"\.parse_obj\(", ".model_validate(", content)

        # Replace .dict( with .model_dump(
        content = re.sub(r"\.dict\(", ".model_dump(", content)

        # Fix self.dict() calls in to_str and to_dict methods
        content = re.sub(
            r"return pprint\.pformat\(self\.dict\(",
            "return pprint.pformat(self.model_dump(",
            content,
        )

        content = re.sub(r"_dict = self\.dict\(", "_dict = self.model_dump(", content)

        return content

    def fix_all_files(self) -> int:
        """Fix all Python files in the source directory."""
        print(f"🔧 Starting Pydantic V2 fixes in {self.src_dir}")

        python_files = list(self.src_dir.rglob("*.py"))
        print(f"Found {len(python_files)} Python files")

        for file_path in python_files:
            self.fix_file(file_path)

        print(f"\n✅ Applied fixes to {self.fixes_applied} files")
        return self.fixes_applied


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Fix Pydantic V2 deprecation warnings")
    parser.add_argument(
        "--src-dir", default="src", help="Source directory to process (default: src)"
    )
    parser.add_argument("--file", help="Fix a specific file instead of all files")

    args = parser.parse_args()

    fixer = PydanticV2Fixer(args.src_dir)

    if args.file:
        # Fix single file
        file_path = Path(args.file)
        if file_path.exists():
            fixer.fix_file(file_path)
        else:
            print(f"❌ File not found: {args.file}")
            return 1
    else:
        # Fix all files
        fixer.fix_all_files()

    return 0


if __name__ == "__main__":
    exit(main())
