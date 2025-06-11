# coding: utf-8

"""
Modern ClientAssetServiceRecordsApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.client_asset_service_records import (
    get_asset_service_records_by_asset_get_2,
)
from qualer_sdk.client import Client


class TestClientAssetServiceRecordsApiModern(unittest.TestCase):
    """Modern ClientAssetServiceRecordsApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch(
        "qualer_sdk.api.client_asset_service_records.get_asset_service_records_by_asset_get_2.sync"
    )
    def test_get_asset_service_records_by_asset_function(
        self, mock_get_asset_service_records_by_asset_get_2
    ):
        """Test the new get_asset_service_records_by_asset_get_2 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_asset_service_records_by_asset_get_2.return_value = mock_response

        # Call the function
        result = get_asset_service_records_by_asset_get_2.sync(client=self.client)

        # Verify the call
        mock_get_asset_service_records_by_asset_get_2.assert_called_once_with(
            client=self.client
        )
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
