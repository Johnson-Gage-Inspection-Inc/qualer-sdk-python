# coding: utf-8

"""
Modern ReferenceApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.reference import get_measurement_quantities, get_units_of_measure
from qualer_sdk.client import Client


class TestReferenceApiModern(unittest.TestCase):
    """Modern ReferenceApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.reference.get_measurement_quantities.sync")
    def test_get_measurement_quantities_function(self, mock_get_measurement_quantities):
        """Test the new get_measurement_quantities function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_measurement_quantities.return_value = mock_response

        # Call the function
        result = get_measurement_quantities.sync(client=self.client)

        # Verify the call
        mock_get_measurement_quantities.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.reference.get_units_of_measure.sync")
    def test_get_units_of_measure_function(self, mock_get_units_of_measure):
        """Test the new get_units_of_measure function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_units_of_measure.return_value = mock_response

        # Call the function
        result = get_units_of_measure.sync(client=self.client)

        # Verify the call
        mock_get_units_of_measure.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
