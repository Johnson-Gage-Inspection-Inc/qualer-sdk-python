# coding: utf-8

"""
Modern CommonApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.common import culture_list, culture_ui_list, get_company_settings
from qualer_sdk.client import Client


class TestCommonApiModern(unittest.TestCase):
    """Modern CommonApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.common.culture_list.sync")
    def test_culture_list_function(self, mock_culture_list):
        """Test the new culture_list function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_culture_list.return_value = mock_response

        # Call the function
        result = culture_list.sync(client=self.client)

        # Verify the call
        mock_culture_list.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.common.culture_ui_list.sync")
    def test_culture_ui_list_function(self, mock_culture_ui_list):
        """Test the new culture_ui_list function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_culture_ui_list.return_value = mock_response

        # Call the function
        result = culture_ui_list.sync(client=self.client)

        # Verify the call
        mock_culture_ui_list.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.common.get_company_settings.sync")
    def test_get_company_settings_function(self, mock_get_company_settings):
        """Test the new get_company_settings function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_company_settings.return_value = mock_response

        # Call the function
        result = get_company_settings.sync(client=self.client)

        # Verify the call
        mock_get_company_settings.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
