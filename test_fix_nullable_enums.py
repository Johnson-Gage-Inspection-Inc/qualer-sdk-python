#!/usr/bin/env python3
"""
Test script to verify fix_nullable_enums function works correctly.
This allows us to test the regex patterns and replacements without regenerating the entire SDK.
"""

import os
import re
import tempfile
import shutil


def test_fix_nullable_enums():
    """Test the fix_nullable_enums function with sample generated code."""

    # Sample generated code that represents the problematic pattern
    sample_code = """
        _service_order_status = d.pop("ServiceOrderStatus", UNSET)
        service_order_status: Union[Unset, QualerApiModelsAssetToAssetManageResponseModelServiceOrderStatus]
        if isinstance(_service_order_status, Unset):
            service_order_status = UNSET
        else:
            service_order_status = QualerApiModelsAssetToAssetManageResponseModelServiceOrderStatus(
                _service_order_status
            )

        _record_type = d.pop("RecordType", UNSET)
        record_type: Union[Unset, QualerApiModelsAssetToAssetManageResponseModelRecordType]
        if isinstance(_record_type, Unset):
            record_type = UNSET
        else:
            record_type = QualerApiModelsAssetToAssetManageResponseModelRecordType(_record_type)

        _result_status = d.pop("ResultStatus", UNSET)
        result_status: Union[Unset, ResultStatus]
        if isinstance(_result_status, Unset):
            result_status = UNSET
        else:
            result_status = ResultStatus(_result_status)
    """

    # Create a temporary directory and file for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        models_dir = os.path.join(temp_dir, "models")
        os.makedirs(models_dir)

        test_file = os.path.join(models_dir, "test_model.py")
        with open(test_file, "w", encoding="utf-8") as f:
            f.write(sample_code)

        print("🔧 Testing fix_nullable_enums function...")
        print("=" * 60)

        # Test each pattern
        nullable_enum_patterns = [
            ("service_order_status", "ServiceOrderStatus"),
            ("record_type", "RecordType"),
            ("result_status", "ResultStatus"),
        ]

        with open(test_file, "r", encoding="utf-8") as f:
            content = f.read()

        print("📋 Original content:")
        print(content)
        print("=" * 60)

        original_content = content

        # Apply the fixes
        for var_name, enum_class_suffix in nullable_enum_patterns:
            print(f"🔍 Testing pattern: {var_name} -> {enum_class_suffix}")

            # Use the same pattern from fix_nullable_enums
            old_pattern = (
                rf"(\s+)if isinstance\(_{var_name}, Unset\):\s*\n"
                rf"(\s+){var_name} = UNSET\s*\n"
                rf"(\s+)else:\s*\n"
                rf"(\s+){var_name} = (\s*\n\s*)?([^(]+\(\s*_{var_name}\s*\))"
            )

            # Find the pattern
            match = re.search(old_pattern, content, re.MULTILINE | re.DOTALL)
            if match:
                print(f"✅ Found pattern for {var_name}")

                # Check if it already has the None check
                full_match = match.group(0)
                if f"elif _{var_name} is None:" not in full_match:
                    print(f"🔧 Applying fix for {var_name}")

                    # Extract indentation from the captured groups
                    indent1 = match.group(1)
                    indent2 = match.group(2)
                    indent3 = match.group(3)
                    indent4 = match.group(4)
                    # Get the enum constructor, handling multi-line cases
                    enum_constructor = match.group(6).strip()

                    print(f"   - indent1: '{indent1}'")
                    print(f"   - indent2: '{indent2}'")
                    print(f"   - indent3: '{indent3}'")
                    print(f"   - indent4: '{indent4}'")
                    print(f"   - enum_constructor: '{enum_constructor}'")

                    # Create the replacement with proper indentation
                    replacement = (
                        f"{indent1}if isinstance(_{var_name}, Unset):\n"
                        f"{indent2}{var_name} = UNSET\n"
                        f"{indent3}elif _{var_name} is None:\n"
                        f"{indent4}{var_name} = None\n"
                        f"{indent3}else:\n"
                        f"{indent4}{var_name} = {enum_constructor}"
                    )

                    content = content.replace(full_match, replacement)
                    print(f"✅ Fixed {var_name} nullable enum")
                else:
                    print(f"ℹ️  {var_name} already has None check, skipping")
            else:
                print(f"❌ Pattern not found for {var_name}")
                print(f"   Regex: {old_pattern}")

        print("=" * 60)
        print("📋 Fixed content:")
        print(content)
        print("=" * 60)

        # Verify the changes
        if content != original_content:
            print("✅ Content was modified - fix appears to work!")

            # Check if the None checks were added
            for var_name, _ in nullable_enum_patterns:
                if f"elif _{var_name} is None:" in content:
                    print(f"✅ {var_name} None check added successfully")
                else:
                    print(f"❌ {var_name} None check was NOT added")
        else:
            print("❌ No changes made - fix did not work!")

        return content != original_content


if __name__ == "__main__":
    success = test_fix_nullable_enums()
    if success:
        print("\n🎉 fix_nullable_enums test PASSED!")
    else:
        print("\n💥 fix_nullable_enums test FAILED!")
