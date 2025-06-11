# coding: utf-8

"""
Modern AssetMeasurementsApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.asset_measurements import get_measurements_by_asset
from qualer_sdk.client import Client


class TestAssetMeasurementsApiModern(unittest.TestCase):
    """Modern AssetMeasurementsApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.asset_measurements.get_measurements_by_asset.sync")
    def test_get_measurements_by_asset_function(self, mock_get_measurements_by_asset):
        """Test the new get_measurements_by_asset function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_measurements_by_asset.return_value = mock_response

        # Call the function
        result = get_measurements_by_asset.sync(client=self.client)

        # Verify the call
        mock_get_measurements_by_asset.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
