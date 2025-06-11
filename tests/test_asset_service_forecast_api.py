# coding: utf-8

"""
Modern AssetServiceForecastApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.asset_service_forecast import (
    get_asset_forecast_list,
    get_client_asset_forecast_list,
)
from qualer_sdk.client import Client


class TestAssetServiceForecastApiModern(unittest.TestCase):
    """Modern AssetServiceForecastApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.asset_service_forecast.get_asset_forecast_list.sync")
    def test_get_asset_forecast_list_function(self, mock_get_asset_forecast_list):
        """Test the new get_asset_forecast_list function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_asset_forecast_list.return_value = mock_response

        # Call the function
        result = get_asset_forecast_list.sync(client=self.client)

        # Verify the call
        mock_get_asset_forecast_list.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.asset_service_forecast.get_client_asset_forecast_list.sync")
    def test_get_client_asset_forecast_list_function(
        self, mock_get_client_asset_forecast_list
    ):
        """Test the new get_client_asset_forecast_list function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_client_asset_forecast_list.return_value = mock_response

        # Call the function
        result = get_client_asset_forecast_list.sync(client=self.client)

        # Verify the call
        mock_get_client_asset_forecast_list.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
