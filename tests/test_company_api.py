# coding: utf-8

"""
Modern CompanyApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.company import (
    add_department,
    delete_department,
    departments,
    lookups,
    site_rooms,
    sites,
)
from qualer_sdk.client import Client


class TestCompanyApiModern(unittest.TestCase):
    """Modern CompanyApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.company.add_department.sync")
    def test_add_department_function(self, mock_add_department):
        """Test the new add_department function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_add_department.return_value = mock_response

        # Call the function
        result = add_department.sync(client=self.client)

        # Verify the call
        mock_add_department.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.company.delete_department.sync")
    def test_delete_department_function(self, mock_delete_department):
        """Test the new delete_department function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_delete_department.return_value = mock_response

        # Call the function
        result = delete_department.sync(client=self.client)

        # Verify the call
        mock_delete_department.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.company.departments.sync")
    def test_departments_function(self, mock_departments):
        """Test the new departments function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_departments.return_value = mock_response

        # Call the function
        result = departments.sync(client=self.client)

        # Verify the call
        mock_departments.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.company.lookups.sync")
    def test_lookups_function(self, mock_lookups):
        """Test the new lookups function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_lookups.return_value = mock_response

        # Call the function
        result = lookups.sync(client=self.client)

        # Verify the call
        mock_lookups.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.company.site_rooms.sync")
    def test_site_rooms_function(self, mock_site_rooms):
        """Test the new site_rooms function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_site_rooms.return_value = mock_response

        # Call the function
        result = site_rooms.sync(client=self.client)

        # Verify the call
        mock_site_rooms.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.company.sites.sync")
    def test_sites_function(self, mock_sites):
        """Test the new sites function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_sites.return_value = mock_response

        # Call the function
        result = sites.sync(client=self.client)

        # Verify the call
        mock_sites.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
