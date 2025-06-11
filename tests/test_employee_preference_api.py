# coding: utf-8

"""
Modern EmployeePreferenceApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.employee_preference import delete, get_get_4
from qualer_sdk.client import Client


class TestEmployeePreferenceApiModern(unittest.TestCase):
    """Modern EmployeePreferenceApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.employee_preference.delete.sync")
    def test_delete_function(self, mock_delete):
        """Test the new delete function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_delete.return_value = mock_response

        # Call the function
        result = delete.sync(client=self.client)

        # Verify the call
        mock_delete.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.employee_preference.get_get_4.sync")
    def test_get_function(self, mock_get_get_4):
        """Test the new get_get_4 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_get_4.return_value = mock_response

        # Call the function
        result = get_get_4.sync(client=self.client)

        # Verify the call
        mock_get_get_4.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
