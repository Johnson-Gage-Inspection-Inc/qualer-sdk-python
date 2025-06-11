# coding: utf-8

"""
Tests for regenerate_sdk.py

Tests the modern openapi-python-client based SDK generation.
"""

import json
import subprocess
from unittest.mock import MagicMock, mock_open, patch

import pytest

from regenerate_sdk import (
    FIXED_SPEC_FILE,
    OUTPUT_DIR,
    SPEC_FILE,
    create_api_init_file,
    create_custom_init_file,
    create_models_init_file,
    format_files_with_autoflake,
    format_generated_files,
    format_generated_files_with_black,
    generate_sdk,
    inject_missing_path_params,
    patch_spec,
    post_process_generated_files,
    sort_imports_with_isort,
    uniquify_operation_ids,
)


class TestUniqueOperationIds:
    def test_uniquify_operation_ids(self):
        """Test that duplicate operation IDs are properly renamed."""
        # Create mock spec with duplicate operation IDs
        mock_spec = {
            "paths": {
                "/api/resource1": {"get": {"operationId": "getDuplicateOp"}},
                "/api/resource2": {"get": {"operationId": "getDuplicateOp"}},
                "/api/resource3": {"post": {"operationId": "uniqueOp"}},
            }
        }

        # Call the function
        uniquify_operation_ids(mock_spec)

        # Check that the first operationId is unchanged and the duplicate is renamed
        assert (
            mock_spec["paths"]["/api/resource1"]["get"]["operationId"]
            == "getDuplicateOp"
        )
        assert (
            mock_spec["paths"]["/api/resource2"]["get"]["operationId"]
            == "getDuplicateOp_get_2"
        )
        assert mock_spec["paths"]["/api/resource3"]["post"]["operationId"] == "uniqueOp"


class TestInjectMissingPathParams:
    def test_inject_missing_path_params(self):
        """Test that missing path parameters are properly injected."""
        # Create mock spec with a path template missing parameter declarations
        mock_spec = {
            "paths": {
                "/api/{resourceId}/items/{itemId}": {
                    "get": {
                        "operationId": "getItem",
                        "parameters": [
                            # Only resourceId is declared, itemId is missing
                            {
                                "name": "resourceId",
                                "in": "path",
                                "required": True,
                                "type": "string",
                            }
                        ],
                    },
                    "put": {"operationId": "updateItem", "parameters": []},
                }
            }
        }

        # Call the function
        inject_missing_path_params(mock_spec)

        # Check that the missing path parameter was added to both operations
        get_params = mock_spec["paths"]["/api/{resourceId}/items/{itemId}"]["get"][
            "parameters"
        ]
        put_params = mock_spec["paths"]["/api/{resourceId}/items/{itemId}"]["put"][
            "parameters"
        ]

        # Check that itemId was added to get operation
        itemId_param = next((p for p in get_params if p["name"] == "itemId"), None)
        assert itemId_param is not None
        assert itemId_param["in"] == "path"
        assert itemId_param["required"] is True

        # Check that both parameters were added to put operation
        resourceId_param = next(
            (p for p in put_params if p["name"] == "resourceId"), None
        )
        itemId_param = next((p for p in put_params if p["name"] == "itemId"), None)
        assert resourceId_param is not None
        assert itemId_param is not None


class TestPatchSpec:
    @patch("regenerate_sdk.fix_swagger_spec")
    def test_patch_spec_success(self, mock_fix_swagger):
        """Test successful spec patching."""
        mock_spec = {
            "definitions": {
                "Qualer.Api.Models.Asset.To.AssetManageResponseModel": {
                    "properties": {"RecordType": {"type": "string"}}
                }
            },
            "paths": {
                "/api/test": {
                    "get": {"tags": ["Asset"], "operationId": "Asset_GetAsset"}
                }
            },
        }

        expected_record_type = {
            "type": "integer",
            "format": "int32",
            "enum": [0, 1, 2, 3],
            "x-enumNames": ["WaitingForAgreement", "Equipment", "System", "Agreement"],
        }

        with patch(
            "builtins.open", mock_open(read_data=json.dumps(mock_spec))
        ) as mock_file:
            patch_spec()

            # Verify the spec was patched correctly
            write_calls = mock_file().write.call_args_list
            written_content = "".join(call[0][0] for call in write_calls)
            patched_spec = json.loads(written_content)

            assert (
                patched_spec["definitions"][
                    "Qualer.Api.Models.Asset.To.AssetManageResponseModel"
                ]["properties"]["RecordType"]
                == expected_record_type
            )
            assert (
                patched_spec["paths"]["/api/test"]["get"]["operationId"] == "GetAsset"
            )

            # Verify fix_swagger_spec was called
            mock_fix_swagger.assert_called_once_with(SPEC_FILE, FIXED_SPEC_FILE)

    def test_patch_spec_missing_record_type(self):
        """Test patch_spec when RecordType is missing."""
        mock_spec = {
            "definitions": {
                "Qualer.Api.Models.Asset.To.AssetManageResponseModel": {
                    "properties": {}
                }
            }
        }

        with patch("builtins.open", mock_open(read_data=json.dumps(mock_spec))):
            with pytest.raises(SystemExit) as excinfo:
                patch_spec()
            assert excinfo.value.code == 1

    def test_patch_spec_missing_definition(self):
        """Test patch_spec when the target definition is missing."""
        mock_spec = {"definitions": {}}

        with patch("builtins.open", mock_open(read_data=json.dumps(mock_spec))):
            with pytest.raises(SystemExit) as excinfo:
                patch_spec()
            assert excinfo.value.code == 1


class TestGenerateSDK:
    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.isdir")
    @patch("os.path.isfile")
    @patch("os.remove")
    @patch("os.path.exists")
    @patch("subprocess.run")
    @patch("os.makedirs")
    @patch("shutil.rmtree")
    @patch("shutil.copytree")
    @patch("shutil.copy2")
    @patch("os.listdir")
    @patch("regenerate_sdk.post_process_generated_files")
    @patch("regenerate_sdk.format_generated_files")
    @patch("regenerate_sdk.create_custom_init_file")
    @patch("regenerate_sdk.create_api_init_file")
    @patch("regenerate_sdk.create_models_init_file")
    def test_generate_sdk_success(
        self,
        mock_create_models,
        mock_create_api,
        mock_create_custom,
        mock_format,
        mock_post_process,
        mock_listdir,
        mock_copy2,
        mock_copytree,
        mock_rmtree,
        mock_makedirs,
        mock_subprocess,
        mock_exists,
        mock_remove,
        mock_isfile,
        mock_isdir,
        mock_file,
    ):
        """Test successful SDK generation."""  # Setup mocks

        def exists_side_effect(path):
            if "temp_sdk_gen" in path and "qualer_sdk" in path:
                return True
            if path == OUTPUT_DIR:
                return True
            if any(
                item in path
                for item in [
                    "api",
                    "models",
                    "client.py",
                    "errors.py",
                    "types.py",
                    "__init__.py",
                ]
            ):
                return True
            return False

        def isdir_side_effect(path):
            # For cleanup, return False (treat as files)
            if OUTPUT_DIR in path and any(item in path for item in ["api", "models"]):
                return True if "api" in path or "models" in path else False
            # For the temp directory check, return True for the generated package
            if "temp_sdk_gen" in path and "qualer_sdk" in path:
                return True
            return False

        mock_exists.side_effect = exists_side_effect
        mock_isdir.side_effect = isdir_side_effect
        mock_isfile.return_value = True  # Files exist for cleanup
        mock_subprocess.return_value = MagicMock()

        # Mock directory listing to return the generated package
        def listdir_side_effect(path):
            if path == "temp_sdk_gen":
                return ["qualer_sdk"]
            return []

        mock_listdir.side_effect = listdir_side_effect

        generate_sdk()

        # Verify subprocess was called with correct command
        expected_command = [
            "openapi-python-client",
            "generate",
            "--path",
            "spec_openapi3.json",
            "--output-path",
            "temp_sdk_gen",
            "--overwrite",
        ]
        mock_subprocess.assert_called_once_with(expected_command, check=True)
        mock_post_process.assert_called_once()
        mock_format.assert_called_once()
        mock_create_custom.assert_called_once()
        mock_create_api.assert_called_once()
        mock_create_models.assert_called_once()

    @patch("subprocess.run")
    def test_generate_sdk_failure(self, mock_subprocess):
        """Test SDK generation failure handling."""
        mock_subprocess.side_effect = subprocess.CalledProcessError(
            1, "openapi-python-client"
        )

        with pytest.raises(SystemExit) as excinfo:
            generate_sdk()
        assert excinfo.value.code == 1


class TestPostProcessGeneratedFiles:
    @patch("os.path.exists")
    def test_post_process_init_file_adds_version(self, mock_exists):
        """Test that version is added to __init__.py when missing."""
        mock_exists.return_value = True
        init_content = "from __future__ import absolute_import\nother content"
        expected_content = 'from __future__ import absolute_import\n\n__version__ = "2.2.1"\nother content'

        with patch("builtins.open", mock_open(read_data=init_content)) as mock_file:
            post_process_generated_files()

            mock_file().write.assert_called_with(expected_content)

    @patch("os.path.exists")
    def test_post_process_init_file_version_exists(self, mock_exists):
        """Test that version is not added when already present."""
        mock_exists.return_value = True
        init_content = 'from __future__ import absolute_import\n__version__ = "1.0.0"'

        with patch("builtins.open", mock_open(read_data=init_content)) as mock_file:
            post_process_generated_files()

            # Should not modify content if version already exists
            mock_file().write.assert_not_called()


class TestFormatGeneratedFiles:
    @patch("regenerate_sdk.format_files_with_autoflake")
    @patch("regenerate_sdk.sort_imports_with_isort")
    @patch("regenerate_sdk.format_generated_files_with_black")
    def test_format_generated_files_calls_all_formatters(
        self, mock_black, mock_isort, mock_autoflake
    ):
        """Test that all formatters are called."""
        format_generated_files()

        mock_autoflake.assert_called_once()
        mock_isort.assert_called_once()
        mock_black.assert_called_once()

    @patch("subprocess.run")
    def test_format_files_with_autoflake(self, mock_subprocess):
        """Test autoflake formatting."""
        mock_subprocess.return_value = MagicMock()

        format_files_with_autoflake()

        mock_subprocess.assert_called_once_with(
            [
                "autoflake",
                "--in-place",
                "--remove-all-unused-imports",
                "--remove-unused-variables",
                "--recursive",
                OUTPUT_DIR,
            ],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )

    @patch("subprocess.run")
    def test_format_files_with_autoflake_not_found(self, mock_subprocess):
        """Test autoflake when not installed."""
        mock_subprocess.side_effect = FileNotFoundError()

        # Should not raise exception
        format_files_with_autoflake()

    @patch("subprocess.run")
    def test_sort_imports_with_isort(self, mock_subprocess):
        """Test isort import sorting."""
        mock_subprocess.return_value = MagicMock()

        sort_imports_with_isort()

        mock_subprocess.assert_called_once_with(
            ["isort", OUTPUT_DIR],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )

    @patch("subprocess.run")
    def test_sort_imports_with_isort_not_found(self, mock_subprocess):
        """Test isort when not installed."""
        mock_subprocess.side_effect = FileNotFoundError()

        # Should not raise exception
        sort_imports_with_isort()

    @patch("subprocess.run")
    def test_format_generated_files_with_black_success(self, mock_subprocess):
        """Test black formatting success."""
        mock_subprocess.return_value = MagicMock(returncode=0)

        format_generated_files_with_black()

        mock_subprocess.assert_called_once_with(
            ["black", OUTPUT_DIR],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )

    @patch("subprocess.run")
    def test_format_generated_files_with_black_failure(self, mock_subprocess):
        """Test black formatting failure."""
        mock_subprocess.return_value = MagicMock(returncode=1, stderr="Error message")

        # Should not raise exception
        format_generated_files_with_black()

    @patch("subprocess.run")
    def test_format_generated_files_with_black_not_found(self, mock_subprocess):
        """Test black when not installed."""
        mock_subprocess.side_effect = FileNotFoundError()

        # Should not raise exception
        format_generated_files_with_black()

    @patch("subprocess.run")
    def test_format_generated_files_with_black_exception(self, mock_subprocess):
        """Test black unexpected exception."""
        mock_subprocess.side_effect = Exception("Unexpected error")

        # Should not raise exception
        format_generated_files_with_black()


class TestCreateFiles:
    @patch("os.path.exists")
    @patch("os.listdir")
    def test_create_custom_init_file(self, mock_listdir, mock_exists):
        """Test custom __init__.py file creation."""
        mock_exists.return_value = True

        with patch("builtins.open", mock_open()) as mock_file:
            create_custom_init_file()

            # Verify file was written
            mock_file.assert_called_once()
            written_content = mock_file().write.call_args[0][0]
            assert '__version__ = "2.2.1"' in written_content
            assert "from .client import Client" in written_content

    @patch("os.path.exists")
    @patch("os.listdir")
    def test_create_api_init_file(self, mock_listdir, mock_exists):
        """Test API __init__.py file creation."""
        mock_exists.return_value = True
        mock_listdir.side_effect = [
            ["account", "assets"],  # API subdirectories (sorted)
            ["get_asset.py", "get_all_assets.py"],  # Files in account
            ["login.py", "logout.py"],  # Files in assets
        ]

        with patch("builtins.open", mock_open()) as mock_file:
            create_api_init_file()

            # Verify file was written
            mock_file.assert_called_once()
            written_content = mock_file().write.call_args[0][0]
            assert "from .account.get_asset import *" in written_content
            assert "from .assets.login import *" in written_content

    @patch("os.path.exists")
    @patch("os.listdir")
    def test_create_models_init_file(self, mock_listdir, mock_exists):
        """Test models __init__.py file creation."""
        mock_exists.return_value = True
        mock_listdir.return_value = [
            "test_model.py",
            "another_model.py",
            "__init__.py",  # Should be excluded
        ]

        with patch("builtins.open", mock_open()) as mock_file:
            create_models_init_file()

            # Verify file was written
            mock_file.assert_called_once()
            written_content = mock_file().write.call_args[0][0]
            assert "from .test_model import TestModel" in written_content
            assert "from .another_model import AnotherModel" in written_content
            assert '"TestModel",' in written_content


class TestMainExecution:
    @patch("regenerate_sdk.patch_spec")
    @patch("regenerate_sdk.generate_sdk")
    @patch("regenerate_sdk.convert_spec_to_openapi_v3")
    def test_main_execution(self, mock_convert, mock_generate, mock_patch):
        """Test main execution flow."""
        # Create a mock globals dict that includes our mocked functions
        mock_globals = {
            "patch_spec": mock_patch,
            "convert_spec_to_openapi_v3": mock_convert,
            "generate_sdk": mock_generate,
            "__name__": "__main__",
            "print": print,  # Keep print for any output
        }

        # Read and execute just the main block
        main_code = """
if __name__ == "__main__":
    patch_spec()
    convert_spec_to_openapi_v3()
    generate_sdk()
"""

        exec(compile(main_code, "regenerate_sdk.py", "exec"), mock_globals)

        mock_patch.assert_called_once()
        mock_convert.assert_called_once()
        mock_generate.assert_called_once()
