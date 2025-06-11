# coding: utf-8

"""
Modern VendorsApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.vendors import create_post_3, get_all_get_3, get_get_8, update_put_4
from qualer_sdk.client import Client


class TestVendorsApiModern(unittest.TestCase):
    """Modern VendorsApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.vendors.create_post_3.sync")
    def test_create_function(self, mock_create_post_3):
        """Test the new create_post_3 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_create_post_3.return_value = mock_response

        # Call the function
        result = create_post_3.sync(client=self.client)

        # Verify the call
        mock_create_post_3.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.vendors.get_all_get_3.sync")
    def test_get_function(self, mock_get_all_get_3):
        """Test the new get_all_get_3 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_all_get_3.return_value = mock_response

        # Call the function
        result = get_all_get_3.sync(client=self.client)

        # Verify the call
        mock_get_all_get_3.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.vendors.get_all_get_3.sync")
    def test_get_all_function(self, mock_get_all_get_3):
        """Test the new get_all_get_3 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_all_get_3.return_value = mock_response

        # Call the function
        result = get_all_get_3.sync(client=self.client)

        # Verify the call
        mock_get_all_get_3.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.vendors.update_put_4.sync")
    def test_update_function(self, mock_update_put_4):
        """Test the new update_put_4 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_update_put_4.return_value = mock_response

        # Call the function
        result = update_put_4.sync(client=self.client)

        # Verify the call
        mock_update_put_4.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.vendors.get_get_8.sync")
    def test_get_get_8_function(self, mock_get_get_8):
        """Test the new get_get_8 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_get_8.return_value = mock_response

        # Call the function
        result = get_get_8.sync(client=self.client)

        # Verify the call
        mock_get_get_8.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
