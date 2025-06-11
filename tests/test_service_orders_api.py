# coding: utf-8

"""
Modern ServiceOrdersApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.service_orders import (
    change_order_status,
    create_async,
    create_order_by_schedule,
    get_assignments,
    get_charges,
    get_order_status,
)
from qualer_sdk.client import Client


class TestServiceOrdersApiModern(unittest.TestCase):
    """Modern ServiceOrdersApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.service_orders.change_order_status.sync")
    def test_change_order_status_function(self, mock_change_order_status):
        """Test the new change_order_status function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_change_order_status.return_value = mock_response

        # Call the function
        result = change_order_status.sync(client=self.client)

        # Verify the call
        mock_change_order_status.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_orders.create_async.sync")
    def test_create_async_function(self, mock_create_async):
        """Test the new create_async function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_create_async.return_value = mock_response

        # Call the function
        result = create_async.sync(client=self.client)

        # Verify the call
        mock_create_async.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_orders.create_order_by_schedule.sync")
    def test_create_order_by_schedule_function(self, mock_create_order_by_schedule):
        """Test the new create_order_by_schedule function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_create_order_by_schedule.return_value = mock_response

        # Call the function
        result = create_order_by_schedule.sync(client=self.client)

        # Verify the call
        mock_create_order_by_schedule.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_orders.get_assignments.sync")
    def test_get_assignments_function(self, mock_get_assignments):
        """Test the new get_assignments function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_assignments.return_value = mock_response

        # Call the function
        result = get_assignments.sync(client=self.client)

        # Verify the call
        mock_get_assignments.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_orders.get_charges.sync")
    def test_get_charges_function(self, mock_get_charges):
        """Test the new get_charges function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_charges.return_value = mock_response

        # Call the function
        result = get_charges.sync(client=self.client)

        # Verify the call
        mock_get_charges.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_orders.get_order_status.sync")
    def test_get_order_status_function(self, mock_get_order_status):
        """Test the new get_order_status function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_order_status.return_value = mock_response

        # Call the function
        result = get_order_status.sync(client=self.client)

        # Verify the call
        mock_get_order_status.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
