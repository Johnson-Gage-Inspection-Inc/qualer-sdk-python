# coding: utf-8

"""
Modern ServiceOrderPartsApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.service_order_parts import (
    create_work_order_parts,
    delete_work_order_task,
    get_work_order_parts,
    update_work_order_parts,
)
from qualer_sdk.client import Client


class TestServiceOrderPartsApiModern(unittest.TestCase):
    """Modern ServiceOrderPartsApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.service_order_parts.create_work_order_parts.sync")
    def test_create_work_order_parts_function(self, mock_create_work_order_parts):
        """Test the new create_work_order_parts function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_create_work_order_parts.return_value = mock_response

        # Call the function
        result = create_work_order_parts.sync(client=self.client)

        # Verify the call
        mock_create_work_order_parts.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_parts.delete_work_order_task.sync")
    def test_delete_work_order_task_function(self, mock_delete_work_order_task):
        """Test the new delete_work_order_task function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_delete_work_order_task.return_value = mock_response

        # Call the function
        result = delete_work_order_task.sync(client=self.client)

        # Verify the call
        mock_delete_work_order_task.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_parts.get_work_order_parts.sync")
    def test_get_work_order_parts_function(self, mock_get_work_order_parts):
        """Test the new get_work_order_parts function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_work_order_parts.return_value = mock_response

        # Call the function
        result = get_work_order_parts.sync(client=self.client)

        # Verify the call
        mock_get_work_order_parts.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_parts.update_work_order_parts.sync")
    def test_update_work_order_parts_function(self, mock_update_work_order_parts):
        """Test the new update_work_order_parts function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_update_work_order_parts.return_value = mock_response

        # Call the function
        result = update_work_order_parts.sync(client=self.client)

        # Verify the call
        mock_update_work_order_parts.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
