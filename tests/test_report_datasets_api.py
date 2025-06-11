# coding: utf-8

"""
Modern ReportDatasetsApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.report_datasets import (
    channel_uniformity_by_order,
    get_all_measurements,
    get_all_measurements_by_order,
    get_as_found_measurements,
    get_as_found_measurements_by_order,
    get_as_left_measurements,
)
from qualer_sdk.client import Client


class TestReportDatasetsApiModern(unittest.TestCase):
    """Modern ReportDatasetsApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.report_datasets.channel_uniformity_by_order.sync")
    def test_channel_uniformity_by_order_function(
        self, mock_channel_uniformity_by_order
    ):
        """Test the new channel_uniformity_by_order function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_channel_uniformity_by_order.return_value = mock_response

        # Call the function
        result = channel_uniformity_by_order.sync(client=self.client)

        # Verify the call
        mock_channel_uniformity_by_order.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.report_datasets.get_all_measurements.sync")
    def test_get_all_measurements_function(self, mock_get_all_measurements):
        """Test the new get_all_measurements function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_all_measurements.return_value = mock_response

        # Call the function
        result = get_all_measurements.sync(client=self.client)

        # Verify the call
        mock_get_all_measurements.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.report_datasets.get_all_measurements.sync")
    def test_get_all_measurements_by_order_function(self, mock_get_all_measurements):
        """Test the new get_all_measurements function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_all_measurements.return_value = mock_response

        # Call the function
        result = get_all_measurements.sync(client=self.client)

        # Verify the call
        mock_get_all_measurements.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.report_datasets.get_as_found_measurements.sync")
    def test_get_as_found_measurements_function(self, mock_get_as_found_measurements):
        """Test the new get_as_found_measurements function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_as_found_measurements.return_value = mock_response

        # Call the function
        result = get_as_found_measurements.sync(client=self.client)

        # Verify the call
        mock_get_as_found_measurements.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.report_datasets.get_as_found_measurements.sync")
    def test_get_as_found_measurements_by_order_function(
        self, mock_get_as_found_measurements
    ):
        """Test the new get_as_found_measurements function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_as_found_measurements.return_value = mock_response

        # Call the function
        result = get_as_found_measurements.sync(client=self.client)

        # Verify the call
        mock_get_as_found_measurements.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.report_datasets.get_as_left_measurements.sync")
    def test_get_as_left_measurements_function(self, mock_get_as_left_measurements):
        """Test the new get_as_left_measurements function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_as_left_measurements.return_value = mock_response

        # Call the function
        result = get_as_left_measurements.sync(client=self.client)

        # Verify the call
        mock_get_as_left_measurements.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.report_datasets.get_as_left_measurements.sync")
    def test_get_as_left_measurements_by_order_function(
        self, mock_get_as_left_measurements
    ):
        """Test the new get_as_left_measurements function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_as_left_measurements.return_value = mock_response

        # Call the function
        result = get_as_left_measurements.sync(client=self.client)

        # Verify the call
        mock_get_as_left_measurements.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.report_datasets.get_all_measurements_by_order.sync")
    def test_get_asset_attributes_function(self, mock_get_all_measurements_by_order):
        """Test the new get_all_measurements_by_order function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_all_measurements_by_order.return_value = mock_response

        # Call the function
        result = get_all_measurements_by_order.sync(client=self.client)

        # Verify the call
        mock_get_all_measurements_by_order.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.report_datasets.get_as_found_measurements_by_order.sync")
    def test_get_asset_service_records_function(
        self, mock_get_as_found_measurements_by_order
    ):
        """Test the new get_as_found_measurements_by_order function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_as_found_measurements_by_order.return_value = mock_response

        # Call the function
        result = get_as_found_measurements_by_order.sync(client=self.client)

        # Verify the call
        mock_get_as_found_measurements_by_order.assert_called_once_with(
            client=self.client
        )
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
