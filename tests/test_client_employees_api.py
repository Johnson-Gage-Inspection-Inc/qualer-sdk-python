# coding: utf-8

"""
Modern ClientEmployeesApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.client_employees import (
    create_employee,
    get_employee,
    get_employees,
    send_employee_email,
)
from qualer_sdk.client import Client


class TestClientEmployeesApiModern(unittest.TestCase):
    """Modern ClientEmployeesApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.client_employees.create_employee.sync")
    def test_create_employee_function(self, mock_create_employee):
        """Test the new create_employee function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_create_employee.return_value = mock_response

        # Call the function
        result = create_employee.sync(client=self.client)

        # Verify the call
        mock_create_employee.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.client_employees.get_employee.sync")
    def test_get_employee_function(self, mock_get_employee):
        """Test the new get_employee function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_employee.return_value = mock_response

        # Call the function
        result = get_employee.sync(client=self.client)

        # Verify the call
        mock_get_employee.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.client_employees.get_employee.sync")
    def test_get_employees_function(self, mock_get_employee):
        """Test the new get_employee function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_employee.return_value = mock_response

        # Call the function
        result = get_employee.sync(client=self.client)

        # Verify the call
        mock_get_employee.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.client_employees.send_employee_email.sync")
    def test_send_employee_email_function(self, mock_send_employee_email):
        """Test the new send_employee_email function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_send_employee_email.return_value = mock_response

        # Call the function
        result = send_employee_email.sync(client=self.client)

        # Verify the call
        mock_send_employee_email.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.client_employees.get_employees.sync")
    def test_get_employees_function(self, mock_get_employees):
        """Test the new get_employees function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_employees.return_value = mock_response

        # Call the function
        result = get_employees.sync(client=self.client)

        # Verify the call
        mock_get_employees.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
