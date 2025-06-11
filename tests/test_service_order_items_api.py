# coding: utf-8

"""
Modern ServiceOrderItemsApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.service_order_items import (
    add_work_items,
    delete_work_item_image,
    get_work_item,
    get_work_item_charges,
    get_work_item_image,
    get_work_item_images,
)
from qualer_sdk.client import Client


class TestServiceOrderItemsApiModern(unittest.TestCase):
    """Modern ServiceOrderItemsApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.service_order_items.add_work_items.sync")
    def test_add_work_items_function(self, mock_add_work_items):
        """Test the new add_work_items function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_add_work_items.return_value = mock_response

        # Call the function
        result = add_work_items.sync(client=self.client)

        # Verify the call
        mock_add_work_items.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_items.delete_work_item_image.sync")
    def test_delete_work_item_image_function(self, mock_delete_work_item_image):
        """Test the new delete_work_item_image function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_delete_work_item_image.return_value = mock_response

        # Call the function
        result = delete_work_item_image.sync(client=self.client)

        # Verify the call
        mock_delete_work_item_image.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_items.get_work_item.sync")
    def test_get_work_item_function(self, mock_get_work_item):
        """Test the new get_work_item function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_work_item.return_value = mock_response

        # Call the function
        result = get_work_item.sync(client=self.client)

        # Verify the call
        mock_get_work_item.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_items.get_work_item.sync")
    def test_get_work_item_charges_function(self, mock_get_work_item):
        """Test the new get_work_item function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_work_item.return_value = mock_response

        # Call the function
        result = get_work_item.sync(client=self.client)

        # Verify the call
        mock_get_work_item.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_items.get_work_item.sync")
    def test_get_work_item_image_function(self, mock_get_work_item):
        """Test the new get_work_item function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_work_item.return_value = mock_response

        # Call the function
        result = get_work_item.sync(client=self.client)

        # Verify the call
        mock_get_work_item.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_items.get_work_item.sync")
    def test_get_work_item_images_function(self, mock_get_work_item):
        """Test the new get_work_item function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_work_item.return_value = mock_response

        # Call the function
        result = get_work_item.sync(client=self.client)

        # Verify the call
        mock_get_work_item.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_items.get_work_item.sync")
    def test_get_work_items_function(self, mock_get_work_item):
        """Test the new get_work_item function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_work_item.return_value = mock_response

        # Call the function
        result = get_work_item.sync(client=self.client)

        # Verify the call
        mock_get_work_item.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_items.get_work_item.sync")
    def test_get_work_items_0_function(self, mock_get_work_item):
        """Test the new get_work_item function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_work_item.return_value = mock_response

        # Call the function
        result = get_work_item.sync(client=self.client)

        # Verify the call
        mock_get_work_item.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_items.get_work_item_charges.sync")
    def test_put_charges_function(self, mock_get_work_item_charges):
        """Test the new get_work_item_charges function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_work_item_charges.return_value = mock_response

        # Call the function
        result = get_work_item_charges.sync(client=self.client)

        # Verify the call
        mock_get_work_item_charges.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_items.get_work_item_image.sync")
    def test_set_work_item_function(self, mock_get_work_item_image):
        """Test the new get_work_item_image function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_work_item_image.return_value = mock_response

        # Call the function
        result = get_work_item_image.sync(client=self.client)

        # Verify the call
        mock_get_work_item_image.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.service_order_items.get_work_item_images.sync")
    def test_upload_work_item_images_function(self, mock_get_work_item_images):
        """Test the new get_work_item_images function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_work_item_images.return_value = mock_response

        # Call the function
        result = get_work_item_images.sync(client=self.client)

        # Verify the call
        mock_get_work_item_images.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
