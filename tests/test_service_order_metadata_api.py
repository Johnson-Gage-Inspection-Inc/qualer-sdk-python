# coding: utf-8

"""
Modern ServiceOrderMetadataApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.service_order_metadata import (
    create_post_2,
    delete_delete_2,
    get_get_6,
    update_put_2,
)
from qualer_sdk.client import Client


class TestServiceOrderMetadataApiModern(unittest.TestCase):
    """Modern ServiceOrderMetadataApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.service_order_metadata.create_post_2.sync")
    def test_create_function(self, mock_create_post_2):
        """Test the new create_post_2 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_create_post_2.return_value = mock_response

        # Call the function
        result = create_post_2.sync(client=self.client)

        # Verify the call
        mock_create_post_2.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_metadata.delete_delete_2.sync")
    def test_delete_function(self, mock_delete_delete_2):
        """Test the new delete_delete_2 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_delete_delete_2.return_value = mock_response

        # Call the function
        result = delete_delete_2.sync(client=self.client)

        # Verify the call
        mock_delete_delete_2.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_metadata.get_get_6.sync")
    def test_get_function(self, mock_get_get_6):
        """Test the new get_get_6 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_get_6.return_value = mock_response

        # Call the function
        result = get_get_6.sync(client=self.client)

        # Verify the call
        mock_get_get_6.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_metadata.update_put_2.sync")
    def test_update_function(self, mock_update_put_2):
        """Test the new update_put_2 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_update_put_2.return_value = mock_response

        # Call the function
        result = update_put_2.sync(client=self.client)

        # Verify the call
        mock_update_put_2.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
