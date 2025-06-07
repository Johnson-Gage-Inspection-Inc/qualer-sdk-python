import json
from unittest.mock import MagicMock, mock_open, patch

import pytest

from regenerate_sdk import (
    OPENAPI_GENERATOR_JAR,
    OUTPUT_DIR,
    SPEC_FILE,
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
    def test_patch_spec_success(self):
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

    def test_patch_spec_missing_record_type(self):
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
        mock_spec = {"definitions": {}}

        with patch("builtins.open", mock_open(read_data=json.dumps(mock_spec))):
            with pytest.raises(SystemExit) as excinfo:
                patch_spec()
            assert excinfo.value.code == 1


class TestGenerateSDK:
    @patch("os.path.exists")
    @patch("subprocess.run")
    @patch("os.makedirs")
    @patch("shutil.rmtree")
    @patch("shutil.copytree")
    @patch("shutil.copy2")
    @patch("regenerate_sdk.post_process_generated_files")
    @patch("regenerate_sdk.format_generated_files")
    def test_generate_sdk_success(
        self,
        mock_format,
        mock_post_process,
        mock_copy2,
        mock_copytree,
        mock_rmtree,
        mock_makedirs,
        mock_subprocess,
        mock_exists,
    ):
        # Setup mocks
        mock_exists.side_effect = (
            lambda path: path == OPENAPI_GENERATOR_JAR
            or path.startswith("temp_sdk_gen")
        )
        mock_subprocess.return_value = MagicMock()

        generate_sdk()  # Verify subprocess was called with correct command
        expected_command = [
            "java",
            "-jar",
            OPENAPI_GENERATOR_JAR,
            "generate",
            "-i",
            SPEC_FILE,
            "-g",
            "python-nextgen",
            "-o",
            "temp_sdk_gen",
            "--additional-properties=packageName=qualer_sdk",
        ]
        mock_subprocess.assert_called_once_with(expected_command, check=True)
        mock_post_process.assert_called_once()
        mock_format.assert_called_once()

    @patch("os.path.exists")
    def test_generate_sdk_missing_jar(self, mock_exists):
        mock_exists.return_value = False

        with pytest.raises(SystemExit) as excinfo:
            generate_sdk()
        assert f"❌ OpenAPI Generator JAR not found: {OPENAPI_GENERATOR_JAR}" in str(
            excinfo.value
        )


class TestPostProcessGeneratedFiles:
    @patch("os.path.exists")
    def test_post_process_init_file_adds_version(self, mock_exists):
        mock_exists.return_value = True
        init_content = "from __future__ import absolute_import\nother content"
        expected_content = 'from __future__ import absolute_import\n\n__version__ = "2.2.1"\nother content'

        with patch("builtins.open", mock_open(read_data=init_content)) as mock_file:
            post_process_generated_files()

            mock_file().write.assert_called_with(expected_content)

    @patch("os.path.exists")
    def test_post_process_init_file_version_exists(self, mock_exists):
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

        format_generated_files()

        mock_autoflake.assert_called_once()
        mock_isort.assert_called_once()
        mock_black.assert_called_once()

    @patch("subprocess.run")
    def test_format_files_with_autoflake(self, mock_subprocess):

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

        mock_subprocess.side_effect = FileNotFoundError()

        # Should not raise exception
        format_files_with_autoflake()

    @patch("subprocess.run")
    def test_sort_imports_with_isort(self, mock_subprocess):

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

        mock_subprocess.side_effect = FileNotFoundError()

        # Should not raise exception
        sort_imports_with_isort()

    @patch("subprocess.run")
    def test_format_generated_files_with_black_success(self, mock_subprocess):

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

        mock_subprocess.return_value = MagicMock(returncode=1, stderr="Error message")

        # Should not raise exception
        format_generated_files_with_black()

    @patch("subprocess.run")
    def test_format_generated_files_with_black_not_found(self, mock_subprocess):

        mock_subprocess.side_effect = FileNotFoundError()

        # Should not raise exception
        format_generated_files_with_black()

    @patch("subprocess.run")
    def test_format_generated_files_with_black_exception(self, mock_subprocess):

        mock_subprocess.side_effect = Exception("Unexpected error")

        # Should not raise exception
        format_generated_files_with_black()


class TestMainExecution:
    @patch("regenerate_sdk.patch_spec")
    @patch("regenerate_sdk.generate_sdk")
    def test_main_execution(self, mock_generate, mock_patch):
        # Create a mock globals dict that includes our mocked functions
        mock_globals = {
            "patch_spec": mock_patch,
            "generate_sdk": mock_generate,
            "__name__": "__main__",
            "print": print,  # Keep print for any output
        }

        # Read and execute just the main block
        main_code = """
if __name__ == "__main__":
    patch_spec()
    generate_sdk()
"""

        exec(compile(main_code, "regenerate_sdk.py", "exec"), mock_globals)

        mock_patch.assert_called_once()
        mock_generate.assert_called_once()
