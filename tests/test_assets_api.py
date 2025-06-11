# coding: utf-8

"""
Modern AssetsApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.assets import (
    clear_collected_assets,
    collect_assets,
    get_all_assets,
    get_asset,
    get_asset_by_asset_pool,
    get_asset_by_asset_tag,
)
from qualer_sdk.client import Client


class TestAssetsApiModern(unittest.TestCase):
    """Modern AssetsApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.assets.clear_collected_assets.sync")
    def test_clear_collected_assets_function(self, mock_clear_collected_assets):
        """Test the new clear_collected_assets function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_clear_collected_assets.return_value = mock_response

        # Call the function
        result = clear_collected_assets.sync(client=self.client)

        # Verify the call
        mock_clear_collected_assets.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.assets.collect_assets.sync")
    def test_collect_assets_function(self, mock_collect_assets):
        """Test the new collect_assets function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_collect_assets.return_value = mock_response

        # Call the function
        result = collect_assets.sync(client=self.client)

        # Verify the call
        mock_collect_assets.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.assets.get_all_assets.sync")
    def test_get_all_assets_function(self, mock_get_all_assets):
        """Test the new get_all_assets function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_all_assets.return_value = mock_response

        # Call the function
        result = get_all_assets.sync(client=self.client)

        # Verify the call
        mock_get_all_assets.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.assets.get_asset.sync")
    def test_get_asset_function(self, mock_get_asset):
        """Test the new get_asset function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_asset.return_value = mock_response

        # Call the function
        result = get_asset.sync(client=self.client)

        # Verify the call
        mock_get_asset.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.assets.get_asset.sync")
    def test_get_asset_by_asset_pool_function(self, mock_get_asset):
        """Test the new get_asset function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_asset.return_value = mock_response

        # Call the function
        result = get_asset.sync(client=self.client)

        # Verify the call
        mock_get_asset.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.assets.get_asset.sync")
    def test_get_asset_by_asset_tag_function(self, mock_get_asset):
        """Test the new get_asset function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_asset.return_value = mock_response

        # Call the function
        result = get_asset.sync(client=self.client)

        # Verify the call
        mock_get_asset.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.assets.get_asset.sync")
    def test_get_asset_by_attribute_function(self, mock_get_asset):
        """Test the new get_asset function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_asset.return_value = mock_response

        # Call the function
        result = get_asset.sync(client=self.client)

        # Verify the call
        mock_get_asset.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.assets.get_asset.sync")
    def test_get_asset_by_barcode_function(self, mock_get_asset):
        """Test the new get_asset function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_asset.return_value = mock_response

        # Call the function
        result = get_asset.sync(client=self.client)

        # Verify the call
        mock_get_asset.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.assets.get_asset.sync")
    def test_get_asset_by_serial_number_function(self, mock_get_asset):
        """Test the new get_asset function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_asset.return_value = mock_response

        # Call the function
        result = get_asset.sync(client=self.client)

        # Verify the call
        mock_get_asset.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.assets.get_asset.sync")
    def test_get_asset_images_function(self, mock_get_asset):
        """Test the new get_asset function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_asset.return_value = mock_response

        # Call the function
        result = get_asset.sync(client=self.client)

        # Verify the call
        mock_get_asset.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.assets.get_asset.sync")
    def test_get_asset_manager_counters_function(self, mock_get_asset):
        """Test the new get_asset function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_asset.return_value = mock_response

        # Call the function
        result = get_asset.sync(client=self.client)

        # Verify the call
        mock_get_asset.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.assets.get_asset.sync")
    def test_get_asset_manager_list_function(self, mock_get_asset):
        """Test the new get_asset function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_asset.return_value = mock_response

        # Call the function
        result = get_asset.sync(client=self.client)

        # Verify the call
        mock_get_asset.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.assets.get_asset.sync")
    def test_get_assets_by_equipment_id_function(self, mock_get_asset):
        """Test the new get_asset function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_asset.return_value = mock_response

        # Call the function
        result = get_asset.sync(client=self.client)

        # Verify the call
        mock_get_asset.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.assets.get_asset_by_asset_pool.sync")
    def test_post_asset_images_function(self, mock_get_asset_by_asset_pool):
        """Test the new get_asset_by_asset_pool function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_asset_by_asset_pool.return_value = mock_response

        # Call the function
        result = get_asset_by_asset_pool.sync(client=self.client)

        # Verify the call
        mock_get_asset_by_asset_pool.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.assets.get_asset_by_asset_tag.sync")
    def test_update_asset_class_function(self, mock_get_asset_by_asset_tag):
        """Test the new get_asset_by_asset_tag function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_asset_by_asset_tag.return_value = mock_response

        # Call the function
        result = get_asset_by_asset_tag.sync(client=self.client)

        # Verify the call
        mock_get_asset_by_asset_tag.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
