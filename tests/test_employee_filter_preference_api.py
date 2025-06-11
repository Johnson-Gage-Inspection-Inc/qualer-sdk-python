# coding: utf-8

"""
Modern EmployeeFilterPreferenceApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.employee_filter_preference import (
    get_employee_filter_preferences,
    update_employee_filter_preference,
)
from qualer_sdk.client import Client


class TestEmployeeFilterPreferenceApiModern(unittest.TestCase):
    """Modern EmployeeFilterPreferenceApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch(
        "qualer_sdk.api.employee_filter_preference.get_employee_filter_preferences.sync"
    )
    def test_get_employee_filter_preferences_function(
        self, mock_get_employee_filter_preferences
    ):
        """Test the new get_employee_filter_preferences function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_employee_filter_preferences.return_value = mock_response

        # Call the function
        result = get_employee_filter_preferences.sync(client=self.client)

        # Verify the call
        mock_get_employee_filter_preferences.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch(
        "qualer_sdk.api.employee_filter_preference.update_employee_filter_preference.sync"
    )
    def test_update_employee_filter_preference_function(
        self, mock_update_employee_filter_preference
    ):
        """Test the new update_employee_filter_preference function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_update_employee_filter_preference.return_value = mock_response

        # Call the function
        result = update_employee_filter_preference.sync(client=self.client)

        # Verify the call
        mock_update_employee_filter_preference.assert_called_once_with(
            client=self.client
        )
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
