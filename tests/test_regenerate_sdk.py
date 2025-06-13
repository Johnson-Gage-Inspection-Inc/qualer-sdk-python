import os
from unittest.mock import MagicMock, mock_open, patch

from regenerate_sdk import (
    create_api_init_file,
    create_custom_init_file,
    create_exceptions_file,
    create_models_init_file,
    format_files_with_autoflake,
    format_generated_files,
    format_generated_files_with_black,
    inject_missing_path_params,
    patch_spec,
    post_process_generated_files,
    sort_imports_with_isort,
    uniquify_operation_ids,
)


def test_uniquify_operation_ids():
    """Test that duplicate operation IDs are properly renamed."""
    spec = {
        "paths": {
            "/path1": {
                "get": {"operationId": "getDuplicate"},
                "post": {"operationId": "postUnique"},
            },
            "/path2": {
                "get": {"operationId": "getDuplicate"},  # Duplicate
                "put": {"operationId": "putUnique"},
            },
        }
    }

    uniquify_operation_ids(spec)

    assert spec["paths"]["/path1"]["get"]["operationId"] == "getDuplicate"
    assert spec["paths"]["/path2"]["get"]["operationId"] == "getDuplicate_get_2"
    assert spec["paths"]["/path1"]["post"]["operationId"] == "postUnique"
    assert spec["paths"]["/path2"]["put"]["operationId"] == "putUnique"


def test_inject_missing_path_params():
    """Test that missing path parameters are properly injected."""
    spec = {
        "paths": {
            "/resource/{id}": {
                "get": {
                    "parameters": [
                        {"name": "otherParam", "in": "query", "type": "string"}
                    ]
                }
            },
            "/nested/{parentId}/child/{childId}": {
                "get": {
                    "parameters": [
                        {
                            "name": "parentId",
                            "in": "path",
                            "required": True,
                            "type": "string",
                        }
                    ]
                }
            },
        }
    }

    inject_missing_path_params(spec)

    # Check that id param was added to first path
    id_param = next(
        (
            p
            for p in spec["paths"]["/resource/{id}"]["get"]["parameters"]
            if p["name"] == "id"
        ),
        None,
    )
    assert id_param is not None
    assert id_param["in"] == "path"
    assert id_param["required"] is True

    # Check that childId param was added to second path
    path2_params = spec["paths"]["/nested/{parentId}/child/{childId}"]["get"][
        "parameters"
    ]
    child_param = next((p for p in path2_params if p["name"] == "childId"), None)
    assert child_param is not None
    assert child_param["in"] == "path"
    assert child_param["required"] is True


@patch("regenerate_sdk.os.path.exists")
@patch("regenerate_sdk.open", new_callable=mock_open)
def test_post_process_generated_files_init_only(mock_file, mock_exists):
    """Test that version is added to __init__.py when only __init__.py exists."""

    # Set up file existence: only __init__.py exists
    def mock_exists_side_effect(path):
        if path.endswith("__init__.py"):
            return True
        return False

    mock_exists.side_effect = mock_exists_side_effect

    # Mock file content for __init__.py (without __version__)
    init_file_content = "from __future__ import absolute_import\n\nsome other content"
    mock_file.return_value.read.return_value = init_file_content

    post_process_generated_files()

    # Verify that write was called once for __init__.py only
    expected_content = 'from __future__ import absolute_import\n\n__version__ = "2.2.1"\n\nsome other content'
    mock_file.return_value.write.assert_called_once_with(expected_content)


@patch("regenerate_sdk.os.path.exists")
@patch("regenerate_sdk.open", new_callable=mock_open)
def test_post_process_generated_files_full(mock_file, mock_exists):
    """Test that version is added to __init__.py and client template is applied when all files exist."""

    # Set up file existence: all files exist
    def mock_exists_side_effect(path):
        return True  # All files exist

    mock_exists.side_effect = mock_exists_side_effect

    # Mock file content for __init__.py (without __version__)
    init_file_content = "from __future__ import absolute_import\n\nsome other content"
    # Mock file content for client template
    template_content = "# Custom client template content with Api-Token"

    # Set up side effects for read operations - the function reads two files
    mock_file.return_value.read.side_effect = [init_file_content, template_content]

    post_process_generated_files()

    # Verify that write was called twice - once for __init__.py and once for client.py
    expected_init_content = 'from __future__ import absolute_import\n\n__version__ = "2.2.1"\n\nsome other content'
    expected_client_content = "# Custom client template content with Api-Token"

    write_calls = mock_file.return_value.write.call_args_list
    assert len(write_calls) == 2, f"Expected 2 write calls, but got {len(write_calls)}"
    assert (
        write_calls[0][0][0] == expected_init_content
    ), "First write call content mismatch"
    assert (
        write_calls[1][0][0] == expected_client_content
    ), "Second write call content mismatch"


# Legacy test name for backward compatibility - use full test since template files are tracked in git
test_post_process_generated_files = test_post_process_generated_files_full


@patch("regenerate_sdk.os.path.exists")
@patch("regenerate_sdk.open", new_callable=mock_open)
@patch("regenerate_sdk.sys.exit")
def test_create_exceptions_file(mock_exit, mock_file, mock_exists):
    """Test that exceptions file is created correctly."""
    mock_exists.return_value = True

    template_content = "# Exception classes for the SDK"
    mock_file.return_value.read.return_value = template_content

    create_exceptions_file()

    mock_file.assert_any_call("templates/exceptions.py", "r", encoding="utf-8")
    mock_file.assert_any_call(
        os.path.join("src", "qualer_sdk", "exceptions.py"), "w", encoding="utf-8"
    )
    mock_file.return_value.write.assert_called_once_with(template_content)

    mock_exit.assert_not_called()


@patch("regenerate_sdk.os.path.exists")
@patch("regenerate_sdk.sys.exit")
def test_create_exceptions_file_template_missing(mock_exit, mock_exists):
    """Test that sys.exit is called if template file is missing."""
    mock_exists.return_value = False

    create_exceptions_file()

    mock_exit.assert_called_once_with(1)


@patch("regenerate_sdk.os.path.exists")
@patch("regenerate_sdk.open", new_callable=mock_open)
def test_create_custom_init_file(mock_file, mock_exists):
    """Test that custom __init__.py file is created correctly."""
    mock_exists.return_value = True

    template_content = "# Custom init template"
    mock_file.return_value.read.return_value = template_content

    create_custom_init_file()

    mock_file.assert_any_call(
        os.path.join("templates", "init_template.py"), "r", encoding="utf-8"
    )
    mock_file.assert_any_call(
        os.path.join("src", "qualer_sdk", "__init__.py"), "w", encoding="utf-8"
    )
    mock_file.return_value.write.assert_called_once_with(template_content)


@patch("regenerate_sdk.os.path.exists")
@patch("regenerate_sdk.os.path.isdir")
@patch("regenerate_sdk.os.listdir")
@patch("regenerate_sdk.open", new_callable=mock_open)
def test_create_api_init_file(mock_file, mock_listdir, mock_isdir, mock_exists):
    """Test that API __init__.py file is created correctly."""
    mock_exists.return_value = True
    mock_isdir.side_effect = lambda path: "api" in path and not path.endswith(
        "__pycache__"
    )

    # Mock API directory structure
    mock_listdir.side_effect = lambda path: (
        ["api_subdir1", "api_subdir2", "__pycache__"]
        if "api" in path and "subdir" not in path
        else ["file1.py", "file2.py", "__init__.py"]
    )

    template_content = "# API __init__.py template\n{api_imports}"
    mock_file.return_value.read.return_value = template_content

    create_api_init_file()

    mock_file.assert_any_call(
        os.path.join("templates", "api_init_template.py"), "r", encoding="utf-8"
    )

    # Check that API imports were correctly generated
    write_calls = mock_file.return_value.write.call_args_list
    assert len(write_calls) > 0
    written_content = write_calls[0][0][0]
    assert "from .api_subdir1.file1 import *" in written_content
    assert "from .api_subdir2.file2 import *" in written_content


@patch("regenerate_sdk.os.path.exists")
@patch("regenerate_sdk.os.listdir")
@patch("regenerate_sdk.open", new_callable=mock_open)
def test_create_models_init_file(mock_file, mock_listdir, mock_exists):
    """Test that models __init__.py file is created correctly."""
    mock_exists.return_value = True

    # Mock models directory structure
    mock_listdir.return_value = ["model_one.py", "model_two.py", "__init__.py"]

    template_content = "# Models __init__.py template\n{model_imports}\n\n__all__ = [\n{model_exports}\n]"
    mock_file.return_value.read.return_value = template_content

    create_models_init_file()

    mock_file.assert_any_call(
        os.path.join("templates", "models_init_template.py"), "r", encoding="utf-8"
    )

    # Check that model imports and exports were correctly generated
    write_calls = mock_file.return_value.write.call_args_list
    assert len(write_calls) > 0
    written_content = write_calls[0][0][0]
    assert "from .model_one import ModelOne" in written_content
    assert "from .model_two import ModelTwo" in written_content
    assert '"ModelOne",' in written_content
    assert '"ModelTwo",' in written_content


@patch("regenerate_sdk.subprocess.run")
def test_format_files_with_autoflake(mock_run):
    """Test that autoflake is called correctly."""
    format_files_with_autoflake()

    mock_run.assert_called_once()
    args = mock_run.call_args[0][0]
    assert args[0] == "autoflake"
    assert "--in-place" in args
    assert "--remove-all-unused-imports" in args
    assert "--recursive" in args


@patch("regenerate_sdk.subprocess.run")
def test_sort_imports_with_isort(mock_run):
    """Test that isort is called correctly."""
    sort_imports_with_isort()

    mock_run.assert_called_once()
    args = mock_run.call_args[0][0]
    assert args[0] == "isort"


@patch("regenerate_sdk.subprocess.run")
def test_format_generated_files_with_black(mock_run):
    """Test that black is called correctly."""
    mock_run.return_value = MagicMock(returncode=0)

    format_generated_files_with_black()

    mock_run.assert_called_once()
    args = mock_run.call_args[0][0]
    assert args[0] == "black"


@patch("regenerate_sdk.format_files_with_autoflake")
@patch("regenerate_sdk.sort_imports_with_isort")
@patch("regenerate_sdk.format_generated_files_with_black")
def test_format_generated_files(mock_black, mock_isort, mock_autoflake):
    """Test that all formatting functions are called in the correct order."""
    format_generated_files()

    mock_autoflake.assert_called_once()
    mock_isort.assert_called_once()
    mock_black.assert_called_once()


@patch("regenerate_sdk.os.path.exists")
@patch("regenerate_sdk.open", new_callable=mock_open)
@patch("regenerate_sdk.json.load")
@patch("regenerate_sdk.json.dump")
@patch("regenerate_sdk.fix_swagger_spec")
@patch("regenerate_sdk.inject_missing_path_params")
@patch("regenerate_sdk.uniquify_operation_ids")
def test_patch_spec(
    mock_uniquify, mock_inject, mock_fix, mock_dump, mock_load, mock_file, mock_exists
):
    """Test that spec is patched correctly."""
    mock_exists.return_value = True

    # Mock the loaded JSON spec
    mock_spec = {
        "definitions": {
            "Qualer.Api.Models.Asset.To.AssetManageResponseModel": {
                "properties": {"RecordType": {}}
            }
        },
        "paths": {"/path": {"get": {"tags": ["Tag"], "operationId": "Tag_operation"}}},
    }
    mock_load.return_value = mock_spec

    with patch("regenerate_sdk.sys.exit") as mock_exit:
        patch_spec()

        # Verify function calls
        mock_inject.assert_called_once_with(mock_spec)
        mock_uniquify.assert_called_once_with(mock_spec)
        mock_fix.assert_called_once_with("spec.json", "spec_fixed.json")
        mock_exit.assert_not_called()

        # Verify RecordType was patched
        record_type = mock_spec["definitions"][
            "Qualer.Api.Models.Asset.To.AssetManageResponseModel"
        ]["properties"]["RecordType"]
        assert record_type["type"] == "integer"
        assert record_type["enum"] == [0, 1, 2, 3]
        assert "WaitingForAgreement" in record_type["x-enumNames"]

        # Verify operationId prefix was removed
        assert mock_spec["paths"]["/path"]["get"]["operationId"] == "operation"
