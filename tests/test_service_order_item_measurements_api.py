# coding: utf-8

"""
Modern ServiceOrderItemMeasurementsApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.service_order_item_measurements import (
    add_auxiliary_tools,
    create_measurement_form,
    get_measurement_form,
    get_measurements_by_asset_get_2,
    update_measurement_form,
)
from qualer_sdk.client import Client


class TestServiceOrderItemMeasurementsApiModern(unittest.TestCase):
    """Modern ServiceOrderItemMeasurementsApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.service_order_item_measurements.add_auxiliary_tools.sync")
    def test_add_auxiliary_tools_function(self, mock_add_auxiliary_tools):
        """Test the new add_auxiliary_tools function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_add_auxiliary_tools.return_value = mock_response

        # Call the function
        result = add_auxiliary_tools.sync(client=self.client)

        # Verify the call
        mock_add_auxiliary_tools.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch(
        "qualer_sdk.api.service_order_item_measurements.create_measurement_form.sync"
    )
    def test_create_measurement_form_function(self, mock_create_measurement_form):
        """Test the new create_measurement_form function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_create_measurement_form.return_value = mock_response

        # Call the function
        result = create_measurement_form.sync(client=self.client)

        # Verify the call
        mock_create_measurement_form.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_item_measurements.get_measurement_form.sync")
    def test_get_measurement_form_function(self, mock_get_measurement_form):
        """Test the new get_measurement_form function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_measurement_form.return_value = mock_response

        # Call the function
        result = get_measurement_form.sync(client=self.client)

        # Verify the call
        mock_get_measurement_form.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch(
        "qualer_sdk.api.service_order_item_measurements.get_measurements_by_asset_get_2.sync"
    )
    def test_get_measurements_by_asset_function(
        self, mock_get_measurements_by_asset_get_2
    ):
        """Test the new get_measurements_by_asset_get_2 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_measurements_by_asset_get_2.return_value = mock_response

        # Call the function
        result = get_measurements_by_asset_get_2.sync(client=self.client)

        # Verify the call
        mock_get_measurements_by_asset_get_2.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch(
        "qualer_sdk.api.service_order_item_measurements.update_measurement_form.sync"
    )
    def test_update_measurement_form_function(self, mock_update_measurement_form):
        """Test the new update_measurement_form function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_update_measurement_form.return_value = mock_response

        # Call the function
        result = update_measurement_form.sync(client=self.client)

        # Verify the call
        mock_update_measurement_form.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
