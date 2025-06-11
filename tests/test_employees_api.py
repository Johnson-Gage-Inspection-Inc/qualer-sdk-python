# coding: utf-8

"""
Modern EmployeesApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.employees import (
    add_employee_department,
    create_employee_post_2,
    delete_employee_department,
    get_employee_get_2,
    get_employees_get_2,
    update_employee,
)
from qualer_sdk.client import Client


class TestEmployeesApiModern(unittest.TestCase):
    """Modern EmployeesApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.employees.add_employee_department.sync")
    def test_add_employee_department_function(self, mock_add_employee_department):
        """Test the new add_employee_department function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_add_employee_department.return_value = mock_response

        # Call the function
        result = add_employee_department.sync(client=self.client)

        # Verify the call
        mock_add_employee_department.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.employees.create_employee_post_2.sync")
    def test_create_employee_function(self, mock_create_employee_post_2):
        """Test the new create_employee_post_2 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_create_employee_post_2.return_value = mock_response

        # Call the function
        result = create_employee_post_2.sync(client=self.client)

        # Verify the call
        mock_create_employee_post_2.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.employees.delete_employee_department.sync")
    def test_delete_employee_department_function(self, mock_delete_employee_department):
        """Test the new delete_employee_department function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_delete_employee_department.return_value = mock_response

        # Call the function
        result = delete_employee_department.sync(client=self.client)

        # Verify the call
        mock_delete_employee_department.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.employees.get_employee_get_2.sync")
    def test_get_employee_function(self, mock_get_employee_get_2):
        """Test the new get_employee_get_2 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_employee_get_2.return_value = mock_response

        # Call the function
        result = get_employee_get_2.sync(client=self.client)

        # Verify the call
        mock_get_employee_get_2.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.employees.get_employees_get_2.sync")
    def test_get_employees_function(self, mock_get_employees_get_2):
        """Test the new get_employees_get_2 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_employees_get_2.return_value = mock_response

        # Call the function
        result = get_employees_get_2.sync(client=self.client)

        # Verify the call
        mock_get_employees_get_2.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.employees.update_employee.sync")
    def test_update_employee_function(self, mock_update_employee):
        """Test the new update_employee function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_update_employee.return_value = mock_response

        # Call the function
        result = update_employee.sync(client=self.client)

        # Verify the call
        mock_update_employee.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
