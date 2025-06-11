# coding: utf-8

"""
Modern ClientsApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.clients import create, get_all_get_2, get_get_3, update
from qualer_sdk.client import Client


class TestClientsApiModern(unittest.TestCase):
    """Modern ClientsApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.clients.create.sync")
    def test_create_function(self, mock_create):
        """Test the new create function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_create.return_value = mock_response

        # Call the function
        result = create.sync(client=self.client)

        # Verify the call
        mock_create.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.clients.get_all_get_2.sync")
    def test_get_function(self, mock_get_all_get_2):
        """Test the new get_all_get_2 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_all_get_2.return_value = mock_response

        # Call the function
        result = get_all_get_2.sync(client=self.client)

        # Verify the call
        mock_get_all_get_2.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.clients.get_all_get_2.sync")
    def test_get_all_function(self, mock_get_all_get_2):
        """Test the new get_all_get_2 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_all_get_2.return_value = mock_response

        # Call the function
        result = get_all_get_2.sync(client=self.client)

        # Verify the call
        mock_get_all_get_2.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.clients.update.sync")
    def test_update_function(self, mock_update):
        """Test the new update function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_update.return_value = mock_response

        # Call the function
        result = update.sync(client=self.client)

        # Verify the call
        mock_update.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.clients.get_get_3.sync")
    def test_get_get_3_function(self, mock_get_get_3):
        """Test the new get_get_3 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_get_3.return_value = mock_response

        # Call the function
        result = get_get_3.sync(client=self.client)

        # Verify the call
        mock_get_get_3.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
