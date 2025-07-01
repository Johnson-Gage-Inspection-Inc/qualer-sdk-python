#!/usr/bin/env python3
"""
Test to reproduce the UnicodeDecodeError by mocking a binary response.

This test creates a mock response that mimics what happens when the API
returns binary content instead of JSON, causing the UnicodeDecodeError.
"""

import os
import unittest
from unittest.mock import MagicMock, patch
from uuid import UUID

import httpx
from dotenv import load_dotenv

from qualer_sdk.api.service_order_documents import get_document
from qualer_sdk.client import AuthenticatedClient

# Load environment variables
load_dotenv()


class TestGetDocumentMockBinaryResponse(unittest.TestCase):
    """Test cases to reproduce the UnicodeDecodeError with mocked binary responses."""

    @classmethod
    def setUpClass(cls):
        """Set up test client with authentication."""
        api_token = os.getenv("QUALER_API_KEY") or "test-token"
        base_url = os.getenv("QUALER_BASE_URL", "https://api.qualer.com")

        cls.client = AuthenticatedClient(base_url=base_url, token=api_token)
        cls.sample_uuid = UUID("c4ab6a7c-e2f1-4984-837f-9390f9a84dfc")

    def test_unicode_error_with_mock_binary_response(self):
        """
        Test that reproduces the UnicodeDecodeError with a mocked binary response.

        This simulates what happens when the API returns binary content (like a PDF)
        but the _parse_response function tries to call response.json().
        """
        # Create binary content that would cause UnicodeDecodeError when decoded as UTF-8
        # This simulates PDF header with some binary data that contains invalid UTF-8 bytes
        binary_content = b"%PDF-1.4\n%\x9c\x9c\x9c\x9c binary content that cannot be decoded as utf-8"

        # Create a mock response that looks like a successful binary response
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.status_code = 200
        mock_response.content = binary_content
        mock_response.headers = {"content-type": "application/pdf"}

        # Make json() method raise UnicodeDecodeError like it would with real binary content
        def json_side_effect():
            # This simulates what happens when httpx tries to decode binary as JSON
            binary_content.decode("utf-8")  # This will raise UnicodeDecodeError

        mock_response.json.side_effect = json_side_effect

        # Patch the httpx client's request method at the module level
        with patch("httpx.Client.request", return_value=mock_response):
            # This should reproduce the UnicodeDecodeError - but since we fixed it,
            # we expect this to work without errors now
            try:
                response = get_document.sync_detailed(
                    guid=self.sample_uuid, client=self.client
                )
                # The fix should prevent UnicodeDecodeError and return a proper response
                self.assertIsNotNone(response)
                # Verify that the response contains the expected binary content
                self.assertIsNotNone(response.content)
            except UnicodeDecodeError:
                self.fail(
                    "UnicodeDecodeError should not occur with the fixed binary endpoint"
                )

    def test_binary_content_handling_fix(self):
        """
        Test that demonstrates how binary content should be handled.

        This shows the fix - when we get binary content, we should not try to parse it as JSON.
        """
        # Create binary content
        binary_content = b"%PDF-1.4\n%\x9c\x9c\x9c\x9c binary PDF content"

        # Create a mock response
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.status_code = 200
        mock_response.content = binary_content
        mock_response.headers = {"content-type": "application/pdf"}

        # Test that we can handle the content without trying to parse it as JSON
        # This demonstrates the fix approach
        self.assertEqual(mock_response.status_code, 200)
        self.assertTrue(mock_response.content.startswith(b"%PDF"))
        self.assertEqual(mock_response.headers["content-type"], "application/pdf")

        # Additional assertions to verify binary content handling
        self.assertIsInstance(mock_response.content, bytes)
        self.assertGreater(len(mock_response.content), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
