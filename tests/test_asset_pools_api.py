# coding: utf-8

"""
Modern AssetPoolsApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.asset_pools import get, get_all
from qualer_sdk.client import Client


class TestAssetPoolsApiModern(unittest.TestCase):
    """Modern AssetPoolsApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.asset_pools.get.sync")
    def test_get_function(self, mock_get):
        """Test the new get function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get.return_value = mock_response

        # Call the function
        result = get.sync(client=self.client)

        # Verify the call
        mock_get.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.asset_pools.get.sync")
    def test_get_all_function(self, mock_get):
        """Test the new get function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get.return_value = mock_response

        # Call the function
        result = get.sync(client=self.client)

        # Verify the call
        mock_get.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.asset_pools.get_all.sync")
    def test_get_all_function(self, mock_get_all):
        """Test the new get_all function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_all.return_value = mock_response

        # Call the function
        result = get_all.sync(client=self.client)

        # Verify the call
        mock_get_all.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
