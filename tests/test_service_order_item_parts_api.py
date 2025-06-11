# coding: utf-8

"""
Modern ServiceOrderItemPartsApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.service_order_item_parts import get_work_item_parts
from qualer_sdk.client import Client


class TestServiceOrderItemPartsApiModern(unittest.TestCase):
    """Modern ServiceOrderItemPartsApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.service_order_item_parts.get_work_item_parts.sync")
    def test_get_work_item_parts_function(self, mock_get_work_item_parts):
        """Test the new get_work_item_parts function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_work_item_parts.return_value = mock_response

        # Call the function
        result = get_work_item_parts.sync(client=self.client)

        # Verify the call
        mock_get_work_item_parts.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
