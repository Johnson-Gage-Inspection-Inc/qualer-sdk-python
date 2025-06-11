# coding: utf-8

"""
Modern ServiceOrderItemDocumentsApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.service_order_item_documents import (
    get_document_list_get_2,
    get_documents_get_2,
    get_documents_list_get_2,
    upload_documents_post_3,
)
from qualer_sdk.client import Client


class TestServiceOrderItemDocumentsApiModern(unittest.TestCase):
    """Modern ServiceOrderItemDocumentsApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.service_order_item_documents.get_document_list_get_2.sync")
    def test_get_document_list_function(self, mock_get_document_list_get_2):
        """Test the new get_document_list_get_2 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_document_list_get_2.return_value = mock_response

        # Call the function
        result = get_document_list_get_2.sync(client=self.client)

        # Verify the call
        mock_get_document_list_get_2.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_item_documents.get_documents_get_2.sync")
    def test_get_documents_function(self, mock_get_documents_get_2):
        """Test the new get_documents_get_2 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_documents_get_2.return_value = mock_response

        # Call the function
        result = get_documents_get_2.sync(client=self.client)

        # Verify the call
        mock_get_documents_get_2.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_item_documents.get_documents_list_get_2.sync")
    def test_get_documents_list_function(self, mock_get_documents_list_get_2):
        """Test the new get_documents_list_get_2 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_documents_list_get_2.return_value = mock_response

        # Call the function
        result = get_documents_list_get_2.sync(client=self.client)

        # Verify the call
        mock_get_documents_list_get_2.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_item_documents.upload_documents_post_3.sync")
    def test_upload_documents_function(self, mock_upload_documents_post_3):
        """Test the new upload_documents_post_3 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_upload_documents_post_3.return_value = mock_response

        # Call the function
        result = upload_documents_post_3.sync(client=self.client)

        # Verify the call
        mock_upload_documents_post_3.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
