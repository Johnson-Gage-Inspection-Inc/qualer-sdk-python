# coding: utf-8

"""
Modern AssetServiceRecordsApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.asset_service_records import (
    add_asset_service_record,
    document_list,
    download_document,
    download_documents,
    get_asset_service_record,
    get_asset_service_records,
)
from qualer_sdk.client import Client


class TestAssetServiceRecordsApiModern(unittest.TestCase):
    """Modern AssetServiceRecordsApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.asset_service_records.add_asset_service_record.sync")
    def test_add_asset_service_record_function(self, mock_add_asset_service_record):
        """Test the new add_asset_service_record function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_add_asset_service_record.return_value = mock_response

        # Call the function
        result = add_asset_service_record.sync(client=self.client)

        # Verify the call
        mock_add_asset_service_record.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.asset_service_records.document_list.sync")
    def test_document_list_function(self, mock_document_list):
        """Test the new document_list function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_document_list.return_value = mock_response

        # Call the function
        result = document_list.sync(client=self.client)

        # Verify the call
        mock_document_list.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.asset_service_records.download_document.sync")
    def test_download_document_function(self, mock_download_document):
        """Test the new download_document function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_download_document.return_value = mock_response

        # Call the function
        result = download_document.sync(client=self.client)

        # Verify the call
        mock_download_document.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.asset_service_records.download_document.sync")
    def test_download_documents_function(self, mock_download_document):
        """Test the new download_document function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_download_document.return_value = mock_response

        # Call the function
        result = download_document.sync(client=self.client)

        # Verify the call
        mock_download_document.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.asset_service_records.get_asset_service_record.sync")
    def test_get_asset_service_record_function(self, mock_get_asset_service_record):
        """Test the new get_asset_service_record function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_asset_service_record.return_value = mock_response

        # Call the function
        result = get_asset_service_record.sync(client=self.client)

        # Verify the call
        mock_get_asset_service_record.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.asset_service_records.get_asset_service_record.sync")
    def test_get_asset_service_records_function(self, mock_get_asset_service_record):
        """Test the new get_asset_service_record function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_asset_service_record.return_value = mock_response

        # Call the function
        result = get_asset_service_record.sync(client=self.client)

        # Verify the call
        mock_get_asset_service_record.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.asset_service_records.get_asset_service_record.sync")
    def test_get_asset_service_records_by_asset_function(
        self, mock_get_asset_service_record
    ):
        """Test the new get_asset_service_record function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_asset_service_record.return_value = mock_response

        # Call the function
        result = get_asset_service_record.sync(client=self.client)

        # Verify the call
        mock_get_asset_service_record.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.asset_service_records.download_documents.sync")
    def test_update_asset_service_record_function(self, mock_download_documents):
        """Test the new download_documents function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_download_documents.return_value = mock_response

        # Call the function
        result = download_documents.sync(client=self.client)

        # Verify the call
        mock_download_documents.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.asset_service_records.get_asset_service_records.sync")
    def test_upload_documents_function(self, mock_get_asset_service_records):
        """Test the new get_asset_service_records function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_asset_service_records.return_value = mock_response

        # Call the function
        result = get_asset_service_records.sync(client=self.client)

        # Verify the call
        mock_get_asset_service_records.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
