# coding: utf-8

"""
Modern EnvironmentsApi Test

This demonstrates the new function-based API approach using openapi-python-client.
Migrated from the old class-based approach using actual discovered function names.
"""

import unittest
from unittest.mock import MagicMock, patch

from qualer_sdk.api.environments import get_get_5, post
from qualer_sdk.client import Client


class TestEnvironmentsApiModern(unittest.TestCase):
    """Modern EnvironmentsApi test examples using function-based approach."""

    def setUp(self):
        self.client = Client(base_url="https://test.qualer.com")

    def tearDown(self):
        pass

    @patch("qualer_sdk.api.environments.get_get_5.sync")
    def test_get_function(self, mock_get_get_5):
        """Test the new get_get_5 function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_get_get_5.return_value = mock_response

        # Call the function
        result = get_get_5.sync(client=self.client)

        # Verify the call
        mock_get_get_5.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)

    @patch("qualer_sdk.api.environments.post.sync")
    def test_post_function(self, mock_post):
        """Test the new post function approach."""
        # Mock the response
        mock_response = MagicMock()
        mock_post.return_value = mock_response

        # Call the function
        result = post.sync(client=self.client)

        # Verify the call
        mock_post.assert_called_once_with(client=self.client)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
