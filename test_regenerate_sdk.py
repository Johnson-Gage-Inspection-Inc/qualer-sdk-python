#!/usr/bin/env python3
"""
Test that verifies the SDK regeneration process works correctly.

This test:
1. Runs the regenerate_sdk.py script
2. Verifies all Python files can be compiled (syntax check)
3. Verifies the SDK can be imported without errors
4. Checks that no Pydantic V1 deprecation warnings remain
"""

import ast
import subprocess
import sys
import warnings
from pathlib import Path

import pytest


class TestSDKRegeneration:
    """Test suite for SDK regeneration and Pydantic V2 compatibility."""

    @pytest.fixture(scope="class")
    def regenerated_sdk(self):
        """Regenerate the SDK before running tests."""
        print("\n🔄 Regenerating SDK...")

        # Run the regenerate script
        result = subprocess.run(
            [sys.executable, "regenerate_sdk.py"],
            capture_output=True,
            text=True,
            cwd=Path.cwd(),
        )

        if result.returncode != 0:
            pytest.fail(
                f"SDK regeneration failed:\nSTDOUT: {result.stdout}\nSTDERR: {result.stderr}"
            )

        print("✅ SDK regeneration completed successfully")
        return result

    def test_regenerate_sdk_success(self, regenerated_sdk):
        """Test that the regenerate_sdk.py script runs successfully."""
        assert (
            regenerated_sdk.returncode == 0
        ), f"regenerate_sdk.py failed: {regenerated_sdk.stderr}"

    def test_all_python_files_syntax_valid(self, regenerated_sdk):
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

    def test_sdk_imports_successfully(self, regenerated_sdk):
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

        # Test importing a specific API class
        try:
            from qualer_sdk.api.assets_api import AssetsApi  # noqa: F401

            print("✅ Specific API class import successful")
        except Exception as e:
            pytest.fail(f"Failed to import specific API class: {e}")

        # Test importing a specific model
        try:
            from qualer_sdk.models.qualer_api_models_asset_to_asset_response_model import (  # noqa: F401
                QualerApiModelsAssetToAssetResponseModel,
            )

            print("✅ Specific model import successful")
        except Exception as e:
            pytest.fail(f"Failed to import specific model: {e}")

    def test_no_pydantic_v1_deprecation_warnings(self, regenerated_sdk):
        """Test that no Pydantic V1 deprecation warnings are raised."""
        print("\n⚠️  Checking for Pydantic V1 deprecation warnings...")

        # Capture warnings during import
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")

            try:
                # Import the SDK which should trigger any deprecation warnings
                import qualer_sdk  # noqa: F401
                from qualer_sdk import api, models  # noqa: F401

                # Try to create a simple model instance to trigger any validation warnings
                from qualer_sdk.models.qualer_api_models_asset_to_asset_response_model import (
                    QualerApiModelsAssetToAssetResponseModel,
                )

                # Create an instance with some data
                model = QualerApiModelsAssetToAssetResponseModel()  # noqa: F841

            except Exception as e:
                pytest.fail(f"Error during warning check: {e}")

        # Check for Pydantic V1 deprecation warnings
        pydantic_warnings = []
        for warning in w:
            warning_msg = str(warning.message).lower()
            if any(
                keyword in warning_msg
                for keyword in [
                    "allow_population_by_field_name",
                    "validator",
                    "validate_arguments",
                    "parse_obj",
                    ".dict(",
                    "pydantic v1",
                ]
            ):
                pydantic_warnings.append(
                    f"{warning.category.__name__}: {warning.message}"
                )

        if pydantic_warnings:
            error_msg = "Pydantic V1 deprecation warnings found:\n"
            for warning in pydantic_warnings:
                error_msg += f"  - {warning}\n"
            pytest.fail(error_msg)

        print("✅ No Pydantic V1 deprecation warnings found")

    def test_pydantic_v2_syntax_used(self, regenerated_sdk):
        """Test that Pydantic V2 syntax is used throughout the codebase."""
        print("\n🔧 Verifying Pydantic V2 syntax usage...")

        src_dir = Path("src")
        python_files = list(src_dir.rglob("*.py"))

        v1_issues = []

        for file_path in python_files:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Check for V1 syntax that should have been converted
                if "allow_population_by_field_name" in content:
                    v1_issues.append(
                        f"{file_path}: contains 'allow_population_by_field_name'"
                    )

                if "@validator(" in content and "@field_validator(" not in content:
                    v1_issues.append(
                        f"{file_path}: contains '@validator' without '@field_validator'"
                    )

                if "validate_arguments" in content:
                    v1_issues.append(f"{file_path}: contains 'validate_arguments'")

                if ".parse_obj(" in content:
                    v1_issues.append(f"{file_path}: contains '.parse_obj('")

                # Check for .dict() calls that aren't in comments
                lines = content.split("\n")
                for i, line in enumerate(lines, 1):
                    if ".dict(" in line and not line.strip().startswith("#"):
                        v1_issues.append(f"{file_path}:{i}: contains '.dict(' call")

            except Exception as e:
                pytest.fail(f"Error checking {file_path}: {e}")

        if v1_issues:
            error_msg = "Pydantic V1 syntax found in generated files:\n"
            for issue in v1_issues:
                error_msg += f"  - {issue}\n"
            pytest.fail(error_msg)

        print("✅ All files use Pydantic V2 syntax")

    def test_api_methods_work(self, regenerated_sdk):
        """Test that API methods can be called (basic smoke test)."""
        print("\n🚀 Testing API method instantiation...")

        try:
            # Test that we can create API instances
            from qualer_sdk.api.assets_api import AssetsApi
            from qualer_sdk.api_client import ApiClient

            # Create API client and API instance
            api_client = ApiClient()
            assets_api = AssetsApi(api_client)

            # Verify the API has the expected methods
            assert hasattr(
                assets_api, "get_assets"
            ), "AssetsApi should have get_assets method"

            print("✅ API methods can be instantiated")

        except Exception as e:
            pytest.fail(f"Error testing API methods: {e}")

    def test_model_validation_works(self, regenerated_sdk):
        """Test that model validation works with Pydantic V2."""
        print("\n✅ Testing model validation...")

        try:
            from qualer_sdk.models.qualer_api_models_asset_to_asset_response_model import (
                QualerApiModelsAssetToAssetResponseModel,
            )

            # Test model creation with valid data
            model_data = {"AssetId": 123, "AssetName": "Test Asset"}

            # Use Pydantic V2 syntax
            model = QualerApiModelsAssetToAssetResponseModel.model_validate(model_data)

            # Test model serialization with V2 syntax
            model_dict = model.model_dump()
            assert isinstance(model_dict, dict)

            print("✅ Model validation and serialization work correctly")

        except Exception as e:
            pytest.fail(f"Error testing model validation: {e}")


def main():
    """Run the tests directly."""
    print("🧪 Running SDK regeneration tests...")

    # Run pytest on this file
    exit_code = pytest.main([__file__, "-v", "--tb=short"])
    return exit_code


if __name__ == "__main__":
    exit(main())
