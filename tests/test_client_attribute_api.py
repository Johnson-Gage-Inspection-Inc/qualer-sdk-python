# coding: utf-8

"""
Modern ClientAttributeApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.client_attribute import (
    get_client_attributes,
    upsert_client_attribute,
)
from qualer_sdk.client import Client


class TestClientAttributeApiModern(unittest.TestCase):
    """Modern ClientAttributeApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.client_attribute.get_client_attributes.sync")
    def test_get_client_attributes_function(self, mock_get_client_attributes):
        """Test the new get_client_attributes function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_client_attributes.return_value = mock_response

        # Call the function
        result = get_client_attributes.sync(client=self.client)

        # Verify the call
        mock_get_client_attributes.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.client_attribute.upsert_client_attribute.sync")
    def test_upsert_client_attribute_function(self, mock_upsert_client_attribute):
        """Test the new upsert_client_attribute function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_upsert_client_attribute.return_value = mock_response

        # Call the function
        result = upsert_client_attribute.sync(client=self.client)

        # Verify the call
        mock_upsert_client_attribute.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
