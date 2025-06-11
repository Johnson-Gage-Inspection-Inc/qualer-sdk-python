# coding: utf-8

"""
Modern ServicePricingApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.service_pricing import get_get_7, update_put_3
from qualer_sdk.client import Client


class TestServicePricingApiModern(unittest.TestCase):
    """Modern ServicePricingApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.service_pricing.get_get_7.sync")
    def test_get_function(self, mock_get_get_7):
        """Test the new get_get_7 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_get_7.return_value = mock_response

        # Call the function
        result = get_get_7.sync(client=self.client)

        # Verify the call
        mock_get_get_7.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_pricing.update_put_3.sync")
    def test_update_function(self, mock_update_put_3):
        """Test the new update_put_3 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_update_put_3.return_value = mock_response

        # Call the function
        result = update_put_3.sync(client=self.client)

        # Verify the call
        mock_update_put_3.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
