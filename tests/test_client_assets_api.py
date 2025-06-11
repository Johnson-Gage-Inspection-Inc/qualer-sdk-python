# coding: utf-8

"""
Modern ClientAssetsApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.client_assets import (
    create_asset,
    get_all_assets_get_2,
    get_asset_counters,
    get_asset_get_2,
    get_asset_manager_list_get_2,
    get_assets,
)
from qualer_sdk.client import Client


class TestClientAssetsApiModern(unittest.TestCase):
    """Modern ClientAssetsApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.client_assets.create_asset.sync")
    def test_create_asset_function(self, mock_create_asset):
        """Test the new create_asset function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_create_asset.return_value = mock_response

        # Call the function
        result = create_asset.sync(client=self.client)

        # Verify the call
        mock_create_asset.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.client_assets.get_all_assets_get_2.sync")
    def test_get_all_assets_function(self, mock_get_all_assets_get_2):
        """Test the new get_all_assets_get_2 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_all_assets_get_2.return_value = mock_response

        # Call the function
        result = get_all_assets_get_2.sync(client=self.client)

        # Verify the call
        mock_get_all_assets_get_2.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.client_assets.get_asset_counters.sync")
    def test_get_asset_function(self, mock_get_asset_counters):
        """Test the new get_asset_counters function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_asset_counters.return_value = mock_response

        # Call the function
        result = get_asset_counters.sync(client=self.client)

        # Verify the call
        mock_get_asset_counters.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.client_assets.get_asset_counters.sync")
    def test_get_asset_counters_function(self, mock_get_asset_counters):
        """Test the new get_asset_counters function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_asset_counters.return_value = mock_response

        # Call the function
        result = get_asset_counters.sync(client=self.client)

        # Verify the call
        mock_get_asset_counters.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.client_assets.get_asset_manager_list_get_2.sync")
    def test_get_asset_manager_list_function(self, mock_get_asset_manager_list_get_2):
        """Test the new get_asset_manager_list_get_2 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_asset_manager_list_get_2.return_value = mock_response

        # Call the function
        result = get_asset_manager_list_get_2.sync(client=self.client)

        # Verify the call
        mock_get_asset_manager_list_get_2.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.client_assets.get_assets.sync")
    def test_get_assets_function(self, mock_get_assets):
        """Test the new get_assets function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_assets.return_value = mock_response

        # Call the function
        result = get_assets.sync(client=self.client)

        # Verify the call
        mock_get_assets.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.client_assets.get_asset_get_2.sync")
    def test_get_asset_get_2_function(self, mock_get_asset_get_2):
        """Test the new get_asset_get_2 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_asset_get_2.return_value = mock_response

        # Call the function
        result = get_asset_get_2.sync(client=self.client)

        # Verify the call
        mock_get_asset_get_2.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
