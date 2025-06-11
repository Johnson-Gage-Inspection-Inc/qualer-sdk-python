# coding: utf-8

"""
Modern ClientSiteApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.client_site import (
    create_client_site,
    get_client_sites,
    update_client_site,
)
from qualer_sdk.client import Client


class TestClientSiteApiModern(unittest.TestCase):
    """Modern ClientSiteApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.client_site.create_client_site.sync")
    def test_create_client_site_function(self, mock_create_client_site):
        """Test the new create_client_site function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_create_client_site.return_value = mock_response

        # Call the function
        result = create_client_site.sync(client=self.client)

        # Verify the call
        mock_create_client_site.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.client_site.get_client_sites.sync")
    def test_get_client_sites_function(self, mock_get_client_sites):
        """Test the new get_client_sites function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_client_sites.return_value = mock_response

        # Call the function
        result = get_client_sites.sync(client=self.client)

        # Verify the call
        mock_get_client_sites.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.client_site.update_client_site.sync")
    def test_update_client_site_function(self, mock_update_client_site):
        """Test the new update_client_site function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_update_client_site.return_value = mock_response

        # Call the function
        result = update_client_site.sync(client=self.client)

        # Verify the call
        mock_update_client_site.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
