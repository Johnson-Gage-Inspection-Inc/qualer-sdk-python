# coding: utf-8

"""
Modern AssetReservationApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.asset_reservation import close, get_get_2, upsert
from qualer_sdk.client import Client


class TestAssetReservationApiModern(unittest.TestCase):
    """Modern AssetReservationApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.asset_reservation.close.sync")
    def test_close_function(self, mock_close):
        """Test the new close function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_close.return_value = mock_response

        # Call the function
        result = close.sync(client=self.client)

        # Verify the call
        mock_close.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.asset_reservation.get_get_2.sync")
    def test_get_function(self, mock_get_get_2):
        """Test the new get_get_2 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_get_2.return_value = mock_response

        # Call the function
        result = get_get_2.sync(client=self.client)

        # Verify the call
        mock_get_get_2.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.asset_reservation.upsert.sync")
    def test_upsert_function(self, mock_upsert):
        """Test the new upsert function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_upsert.return_value = mock_response

        # Call the function
        result = upsert.sync(client=self.client)

        # Verify the call
        mock_upsert.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
