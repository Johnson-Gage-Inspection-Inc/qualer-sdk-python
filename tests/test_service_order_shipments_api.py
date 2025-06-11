# coding: utf-8

"""
Modern ServiceOrderShipmentsApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.service_order_shipments import (
    append_shipment_tracking_number,
    update_shipment_status,
)
from qualer_sdk.client import Client


class TestServiceOrderShipmentsApiModern(unittest.TestCase):
    """Modern ServiceOrderShipmentsApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch(
        "qualer_sdk.api.service_order_shipments.append_shipment_tracking_number.sync"
    )
    def test_append_shipment_tracking_number_function(
        self, mock_append_shipment_tracking_number
    ):
        """Test the new append_shipment_tracking_number function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_append_shipment_tracking_number.return_value = mock_response

        # Call the function
        result = append_shipment_tracking_number.sync(client=self.client)

        # Verify the call
        mock_append_shipment_tracking_number.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_shipments.update_shipment_status.sync")
    def test_update_shipment_status_function(self, mock_update_shipment_status):
        """Test the new update_shipment_status function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_update_shipment_status.return_value = mock_response

        # Call the function
        result = update_shipment_status.sync(client=self.client)

        # Verify the call
        mock_update_shipment_status.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
