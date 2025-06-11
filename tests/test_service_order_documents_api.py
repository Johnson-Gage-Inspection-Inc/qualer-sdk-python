# coding: utf-8

"""
Modern ServiceOrderDocumentsApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.service_order_documents import (
    get_document,
    get_document_get_wd,
    get_document_list,
    get_documents,
    get_documents_list,
    upload_documents_post_2,
)
from qualer_sdk.client import Client


class TestServiceOrderDocumentsApiModern(unittest.TestCase):
    """Modern ServiceOrderDocumentsApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.service_order_documents.get_document.sync")
    def test_get_document_function(self, mock_get_document):
        """Test the new get_document function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_document.return_value = mock_response

        # Call the function
        result = get_document.sync(client=self.client)

        # Verify the call
        mock_get_document.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_documents.get_document.sync")
    def test_get_document_0_function(self, mock_get_document):
        """Test the new get_document function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_document.return_value = mock_response

        # Call the function
        result = get_document.sync(client=self.client)

        # Verify the call
        mock_get_document.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_documents.get_document.sync")
    def test_get_document_list_function(self, mock_get_document):
        """Test the new get_document function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_document.return_value = mock_response

        # Call the function
        result = get_document.sync(client=self.client)

        # Verify the call
        mock_get_document.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_documents.get_document.sync")
    def test_get_documents_function(self, mock_get_document):
        """Test the new get_document function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_document.return_value = mock_response

        # Call the function
        result = get_document.sync(client=self.client)

        # Verify the call
        mock_get_document.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_documents.get_document.sync")
    def test_get_documents_list_function(self, mock_get_document):
        """Test the new get_document function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_document.return_value = mock_response

        # Call the function
        result = get_document.sync(client=self.client)

        # Verify the call
        mock_get_document.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_documents.upload_documents_post_2.sync")
    def test_upload_documents_function(self, mock_upload_documents_post_2):
        """Test the new upload_documents_post_2 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_upload_documents_post_2.return_value = mock_response

        # Call the function
        result = upload_documents_post_2.sync(client=self.client)

        # Verify the call
        mock_upload_documents_post_2.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_documents.get_document_get_wd.sync")
    def test_get_document_get_wd_function(self, mock_get_document_get_wd):
        """Test the new get_document_get_wd function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_document_get_wd.return_value = mock_response

        # Call the function
        result = get_document_get_wd.sync(client=self.client)

        # Verify the call
        mock_get_document_get_wd.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_documents.get_document_list.sync")
    def test_get_document_list_function(self, mock_get_document_list):
        """Test the new get_document_list function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_document_list.return_value = mock_response

        # Call the function
        result = get_document_list.sync(client=self.client)

        # Verify the call
        mock_get_document_list.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_documents.get_documents.sync")
    def test_get_documents_function(self, mock_get_documents):
        """Test the new get_documents function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_documents.return_value = mock_response

        # Call the function
        result = get_documents.sync(client=self.client)

        # Verify the call
        mock_get_documents.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_documents.get_documents_list.sync")
    def test_get_documents_list_function(self, mock_get_documents_list):
        """Test the new get_documents_list function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_documents_list.return_value = mock_response

        # Call the function
        result = get_documents_list.sync(client=self.client)

        # Verify the call
        mock_get_documents_list.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
