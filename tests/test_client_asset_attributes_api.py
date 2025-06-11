# coding: utf-8

"""
Modern ClientAssetAttributesApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.client_asset_attributes import (
    get_asset_attributes_get_2,
    upsert_asset_attributes_put_2,
)
from qualer_sdk.client import Client


class TestClientAssetAttributesApiModern(unittest.TestCase):
    """Modern ClientAssetAttributesApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.client_asset_attributes.get_asset_attributes_get_2.sync")
    def test_get_asset_attributes_function(self, mock_get_asset_attributes_get_2):
        """Test the new get_asset_attributes_get_2 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_asset_attributes_get_2.return_value = mock_response

        # Call the function
        result = get_asset_attributes_get_2.sync(client=self.client)

        # Verify the call
        mock_get_asset_attributes_get_2.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.client_asset_attributes.upsert_asset_attributes_put_2.sync")
    def test_upsert_asset_attributes_function(self, mock_upsert_asset_attributes_put_2):
        """Test the new upsert_asset_attributes_put_2 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_upsert_asset_attributes_put_2.return_value = mock_response

        # Call the function
        result = upsert_asset_attributes_put_2.sync(client=self.client)

        # Verify the call
        mock_upsert_asset_attributes_put_2.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
