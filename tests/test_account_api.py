# coding: utf-8

"""
Modern AccountApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.account import (
    companies,
    get_employee_message,
    get_employee_messages,
    login,
    logout,
    post_employee_location,
)
from qualer_sdk.client import Client


class TestAccountApiModern(unittest.TestCase):
    """Modern AccountApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.account.companies.sync")
    def test_companies_function(self, mock_companies):
        """Test the new companies function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_companies.return_value = mock_response

        # Call the function
        result = companies.sync(client=self.client)

        # Verify the call
        mock_companies.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.account.get_employee_messages.sync")
    def test_get_employee_messages_function(self, mock_get_employee_messages):
        """Test the new get_employee_messages function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_employee_messages.return_value = mock_response

        # Call the function
        result = get_employee_messages.sync(client=self.client)

        # Verify the call
        mock_get_employee_messages.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.account.get_employee_message.sync")
    def test_get_employee_message_function(self, mock_get_employee_message):
        """Test the new get_employee_message function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_employee_message.return_value = mock_response

        # Call the function
        result = get_employee_message.sync(client=self.client)

        # Verify the call
        mock_get_employee_message.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.account.login.sync")
    def test_login_function(self, mock_login):
        """Test the new login function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_login.return_value = mock_response

        # Call the function
        result = login.sync(client=self.client)

        # Verify the call
        mock_login.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.account.logout.sync")
    def test_logout_function(self, mock_logout):
        """Test the new logout function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_logout.return_value = mock_response

        # Call the function
        result = logout.sync(client=self.client)

        # Verify the call
        mock_logout.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.account.post_employee_location.sync")
    def test_post_employee_location_function(self, mock_post_employee_location):
        """Test the new post_employee_location function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_post_employee_location.return_value = mock_response

        # Call the function
        result = post_employee_location.sync(client=self.client)

        # Verify the call
        mock_post_employee_location.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
