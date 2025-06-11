# coding: utf-8

"""
Modern ServiceOrderPaymentsApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.service_order_payments import (
    change_work_order_payment_status,
    create_work_order_payment,
    get_all_work_order_payments,
    get_work_order_payment,
)
from qualer_sdk.client import Client


class TestServiceOrderPaymentsApiModern(unittest.TestCase):
    """Modern ServiceOrderPaymentsApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch(
        "qualer_sdk.api.service_order_payments.change_work_order_payment_status.sync"
    )
    def test_change_work_order_payment_status_function(
        self, mock_change_work_order_payment_status
    ):
        """Test the new change_work_order_payment_status function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_change_work_order_payment_status.return_value = mock_response

        # Call the function
        result = change_work_order_payment_status.sync(client=self.client)

        # Verify the call
        mock_change_work_order_payment_status.assert_called_once_with(
            client=self.client
        )
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_payments.create_work_order_payment.sync")
    def test_create_work_order_payment_function(self, mock_create_work_order_payment):
        """Test the new create_work_order_payment function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_create_work_order_payment.return_value = mock_response

        # Call the function
        result = create_work_order_payment.sync(client=self.client)

        # Verify the call
        mock_create_work_order_payment.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_payments.get_all_work_order_payments.sync")
    def test_get_all_work_order_payments_function(
        self, mock_get_all_work_order_payments
    ):
        """Test the new get_all_work_order_payments function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_all_work_order_payments.return_value = mock_response

        # Call the function
        result = get_all_work_order_payments.sync(client=self.client)

        # Verify the call
        mock_get_all_work_order_payments.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_payments.get_work_order_payment.sync")
    def test_get_work_order_payment_function(self, mock_get_work_order_payment):
        """Test the new get_work_order_payment function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_work_order_payment.return_value = mock_response

        # Call the function
        result = get_work_order_payment.sync(client=self.client)

        # Verify the call
        mock_get_work_order_payment.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
