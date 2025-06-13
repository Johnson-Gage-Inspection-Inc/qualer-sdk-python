#!/usr/bin/env python3
"""
Test that verifies the current SDK structure and functionality.

This test:
1. Verifies all Python files can be compiled (syntax check)
2. Verifies the SDK can be imported without errors
3. Checks that attrs-based models work correctly
4. Tests that basic API functionality works
"""

import ast
import warnings
from pathlib import Path

import pytest


class TestSDKStructure:
    """Test suite for SDK structure and functionality."""

    def test_all_python_files_syntax_valid(self):
        """Test that all generated Python files have valid syntax."""
        src_dir = Path("src")
        python_files = list(src_dir.rglob("*.py"))

        print(f"\n🔍 Checking syntax of {len(python_files)} Python files...")

        syntax_errors = []

        for file_path in python_files:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Try to parse the file
                ast.parse(content, filename=str(file_path))

            except SyntaxError as e:
                syntax_errors.append((file_path, str(e)))
            except Exception as e:
                syntax_errors.append((file_path, f"Unexpected error: {e}"))

        if syntax_errors:
            error_msg = "Syntax errors found in generated files:\n"
            for file_path, error in syntax_errors:
                error_msg += f"  - {file_path}: {error}\n"
            pytest.fail(error_msg)

        print("✅ All Python files have valid syntax")

    def test_sdk_imports_successfully(self):
        """Test that the SDK can be imported without errors."""
        print("\n📦 Testing SDK import...")

        # Test importing the main SDK
        try:
            import qualer_sdk  # noqa: F401

            print("✅ Main SDK import successful")
        except Exception as e:
            pytest.fail(f"Failed to import qualer_sdk: {e}")

        # Test importing specific modules
        try:
            from qualer_sdk import api, models  # noqa: F401

            print("✅ API and models import successful")
        except Exception as e:
            pytest.fail(f"Failed to import qualer_sdk.api or qualer_sdk.models: {e}")

        # Test importing a specific API function
        try:
            from qualer_sdk.api.assets.get_all_assets import sync  # noqa: F401

            print("✅ Specific API function import successful")
        except Exception as e:
            pytest.fail(f"Failed to import specific API function: {e}")

        # Test importing a specific model
        try:
            from qualer_sdk.models.qualer_api_models_asset_to_asset_response_model import (  # noqa: F401
                QualerApiModelsAssetToAssetResponseModel,
            )

            print("✅ Specific model import successful")
        except Exception as e:
            pytest.fail(f"Failed to import specific model: {e}")

    def test_no_deprecated_syntax_warnings(self):
        """Test that no deprecated syntax warnings are raised."""
        print("\n⚠️  Checking for deprecated syntax warnings...")

        # Capture warnings during import
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")

            try:
                # Import the SDK which should trigger any deprecation warnings
                import qualer_sdk  # noqa: F401
                from qualer_sdk import api, models  # noqa: F401

                # Try to create a simple model instance
                from qualer_sdk.models.qualer_api_models_asset_to_asset_response_model import (
                    QualerApiModelsAssetToAssetResponseModel,
                )

                # Create an instance
                model = QualerApiModelsAssetToAssetResponseModel()  # noqa: F841

            except Exception as e:
                pytest.fail(f"Error during warning check: {e}")

        # Check for any concerning warnings
        concerning_warnings = []
        for warning in w:
            warning_msg = str(warning.message).lower()
            if any(
                keyword in warning_msg
                for keyword in [
                    "deprecated",
                    "outdated",
                    "legacy",
                ]
            ):
                concerning_warnings.append(
                    f"{warning.category.__name__}: {warning.message}"
                )

        if concerning_warnings:
            error_msg = "Deprecated syntax warnings found:\n"
            for warning in concerning_warnings:
                error_msg += f"  - {warning}\n"
            pytest.fail(error_msg)

        print("✅ No deprecated syntax warnings found")

    def test_attrs_syntax_used(self):
        """Test that attrs syntax is used throughout the codebase."""
        print("\n🔧 Verifying attrs syntax usage...")

        src_dir = Path("src")
        python_files = list(src_dir.rglob("*.py"))

        attrs_usage_count = 0
        pydantic_issues = []

        for file_path in python_files:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Check for attrs usage
                if "@_attrs_define" in content or "from attrs import" in content:
                    attrs_usage_count += 1

                # Check for old Pydantic syntax that shouldn't be there
                if "from pydantic import" in content:
                    pydantic_issues.append(f"{file_path}: contains pydantic imports")

                if "BaseModel" in content and "pydantic" in content:
                    pydantic_issues.append(f"{file_path}: contains BaseModel usage")

            except Exception as e:
                pytest.fail(f"Error checking {file_path}: {e}")

        if pydantic_issues:
            error_msg = "Pydantic usage found in files (should use attrs):\n"
            for issue in pydantic_issues:
                error_msg += f"  - {issue}\n"
            pytest.fail(error_msg)

        print(f"✅ Found {attrs_usage_count} files using attrs, no pydantic usage")

    def test_api_methods_work(self):
        """Test that API methods can be called (basic smoke test)."""
        print("\n🚀 Testing API method instantiation...")

        try:
            # Test that we can create API client and call functions
            from qualer_sdk.client import Client

            # Create API client
            client = Client(base_url="https://test.qualer.com")

            # Test that we can import and call an API function
            from qualer_sdk.api.assets.get_all_assets import sync

            # Verify the function exists and is callable
            assert callable(sync), "get_all_assets sync function should be callable"

            print("✅ API methods can be instantiated")

        except Exception as e:
            pytest.fail(f"Error testing API methods: {e}")

    def test_model_validation_works(self):
        """Test that model validation works with attrs-based models."""
        print("\n✅ Testing model validation...")

        try:
            from qualer_sdk.models.qualer_api_models_asset_to_asset_response_model import (
                QualerApiModelsAssetToAssetResponseModel,
            )

            # Test model creation with valid data
            model_data = {"asset_id": 123, "asset_name": "Test Asset"}

            # Use attrs-based model methods (from_dict/to_dict)
            model = QualerApiModelsAssetToAssetResponseModel.from_dict(model_data)

            # Test model serialization
            model_dict = model.to_dict()
            assert isinstance(model_dict, dict)

            print("✅ Model validation and serialization work correctly")

        except Exception as e:
            pytest.fail(f"Error testing model validation: {e}")


def main():
    """Run the tests directly."""
    print("🧪 Running SDK structure tests...")

    # Run pytest on this file
    exit_code = pytest.main([__file__, "-v", "--tb=short"])
    return exit_code


if __name__ == "__main__":
    exit(main())
