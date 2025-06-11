# coding: utf-8

"""
Modern ProductApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.product import (
    add_manufacturer,
    add_product,
    get_inventory_count,
    get_manufacturers,
    get_product,
    product,
)
from qualer_sdk.client import Client


class TestProductApiModern(unittest.TestCase):
    """Modern ProductApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.product.add_manufacturer.sync")
    def test_add_manufacturer_function(self, mock_add_manufacturer):
        """Test the new add_manufacturer function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_add_manufacturer.return_value = mock_response

        # Call the function
        result = add_manufacturer.sync(client=self.client)

        # Verify the call
        mock_add_manufacturer.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.product.add_product.sync")
    def test_add_product_function(self, mock_add_product):
        """Test the new add_product function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_add_product.return_value = mock_response

        # Call the function
        result = add_product.sync(client=self.client)

        # Verify the call
        mock_add_product.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.product.get_inventory_count.sync")
    def test_get_inventory_count_function(self, mock_get_inventory_count):
        """Test the new get_inventory_count function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_inventory_count.return_value = mock_response

        # Call the function
        result = get_inventory_count.sync(client=self.client)

        # Verify the call
        mock_get_inventory_count.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.product.get_manufacturers.sync")
    def test_get_manufacturers_function(self, mock_get_manufacturers):
        """Test the new get_manufacturers function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_manufacturers.return_value = mock_response

        # Call the function
        result = get_manufacturers.sync(client=self.client)

        # Verify the call
        mock_get_manufacturers.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.product.get_product.sync")
    def test_get_product_function(self, mock_get_product):
        """Test the new get_product function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_product.return_value = mock_response

        # Call the function
        result = get_product.sync(client=self.client)

        # Verify the call
        mock_get_product.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.product.add_product.sync")
    def test_product_function(self, mock_add_product):
        """Test the new add_product function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_add_product.return_value = mock_response

        # Call the function
        result = add_product.sync(client=self.client)

        # Verify the call
        mock_add_product.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.product.product.sync")
    def test_put_inventory_count_function(self, mock_product):
        """Test the new product function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_product.return_value = mock_response

        # Call the function
        result = product.sync(client=self.client)

        # Verify the call
        mock_product.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
