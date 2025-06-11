# coding: utf-8

"""
Modern ServiceOrderItemTasksApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.service_order_item_tasks import (
    create_work_item_task,
    delete_work_item_task,
    get_work_item_task,
    get_work_item_tasks,
)
from qualer_sdk.client import Client


class TestServiceOrderItemTasksApiModern(unittest.TestCase):
    """Modern ServiceOrderItemTasksApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.service_order_item_tasks.create_work_item_task.sync")
    def test_create_work_item_task_function(self, mock_create_work_item_task):
        """Test the new create_work_item_task function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_create_work_item_task.return_value = mock_response

        # Call the function
        result = create_work_item_task.sync(client=self.client)

        # Verify the call
        mock_create_work_item_task.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_item_tasks.delete_work_item_task.sync")
    def test_delete_work_item_task_function(self, mock_delete_work_item_task):
        """Test the new delete_work_item_task function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_delete_work_item_task.return_value = mock_response

        # Call the function
        result = delete_work_item_task.sync(client=self.client)

        # Verify the call
        mock_delete_work_item_task.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_item_tasks.get_work_item_task.sync")
    def test_get_work_item_task_function(self, mock_get_work_item_task):
        """Test the new get_work_item_task function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_work_item_task.return_value = mock_response

        # Call the function
        result = get_work_item_task.sync(client=self.client)

        # Verify the call
        mock_get_work_item_task.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_item_tasks.get_work_item_task.sync")
    def test_get_work_item_tasks_function(self, mock_get_work_item_task):
        """Test the new get_work_item_task function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_work_item_task.return_value = mock_response

        # Call the function
        result = get_work_item_task.sync(client=self.client)

        # Verify the call
        mock_get_work_item_task.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_item_tasks.get_work_item_tasks.sync")
    def test_get_work_item_tasks_function(self, mock_get_work_item_tasks):
        """Test the new get_work_item_tasks function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_work_item_tasks.return_value = mock_response

        # Call the function
        result = get_work_item_tasks.sync(client=self.client)

        # Verify the call
        mock_get_work_item_tasks.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
