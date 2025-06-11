# coding: utf-8

"""
Tests for AuthenticatedClient with Api-Token prefix

This test module validates that the AuthenticatedClient correctly uses
"Api-Token" as the default authorization prefix instead of "Bearer".
"""

import unittest

from qualer_sdk.client import AuthenticatedClient


class TestAuthenticatedClient(unittest.TestCase):
    """Test AuthenticatedClient authorization functionality."""

    def test_default_prefix_is_api_token(self):
        """Test that the default prefix is 'Api-Token'."""
        client = AuthenticatedClient(
            base_url="https://test.qualer.com", token="test-token-123"
        )
        self.assertEqual(client.prefix, "Api-Token")

    def test_custom_prefix_can_be_set(self):
        """Test that a custom prefix can be set."""
        client = AuthenticatedClient(
            base_url="https://test.qualer.com", token="test-token-123", prefix="Bearer"
        )
        self.assertEqual(client.prefix, "Bearer")

    def test_authorization_header_with_default_prefix(self):
        """Test that the Authorization header is set with Api-Token prefix."""
        client = AuthenticatedClient(
            base_url="https://test.qualer.com", token="test-token-123"
        )

        # Get the httpx client to trigger header setup
        httpx_client = client.get_httpx_client()

        # Check that the Authorization header is set correctly
        self.assertIn("Authorization", httpx_client.headers)
        self.assertEqual(
            httpx_client.headers["Authorization"], "Api-Token test-token-123"
        )

    def test_authorization_header_with_custom_prefix(self):
        """Test that the Authorization header works with custom prefix."""
        client = AuthenticatedClient(
            base_url="https://test.qualer.com", token="test-token-123", prefix="Bearer"
        )

        # Get the httpx client to trigger header setup
        httpx_client = client.get_httpx_client()

        # Check that the Authorization header is set correctly
        self.assertIn("Authorization", httpx_client.headers)
        self.assertEqual(httpx_client.headers["Authorization"], "Bearer test-token-123")

    def test_authorization_header_with_empty_prefix(self):
        """Test that the Authorization header works with empty prefix."""
        client = AuthenticatedClient(
            base_url="https://test.qualer.com", token="test-token-123", prefix=""
        )

        # Get the httpx client to trigger header setup
        httpx_client = client.get_httpx_client()

        # Check that the Authorization header is set correctly (token only)
        self.assertIn("Authorization", httpx_client.headers)
        self.assertEqual(httpx_client.headers["Authorization"], "test-token-123")

    def test_authorization_header_with_none_prefix(self):
        """Test that the Authorization header works with None prefix."""
        client = AuthenticatedClient(
            base_url="https://test.qualer.com", token="test-token-123", prefix=None
        )

        # Get the httpx client to trigger header setup
        httpx_client = client.get_httpx_client()

        # Check that the Authorization header is set correctly (token only)
        self.assertIn("Authorization", httpx_client.headers)
        self.assertEqual(httpx_client.headers["Authorization"], "test-token-123")

    def test_async_client_authorization_header(self):
        """Test that the async client also sets the Authorization header correctly."""
        client = AuthenticatedClient(
            base_url="https://test.qualer.com", token="test-token-123"
        )

        # Get the async httpx client to trigger header setup
        async_client = client.get_async_httpx_client()

        # Check that the Authorization header is set correctly
        self.assertIn("Authorization", async_client.headers)
        self.assertEqual(
            async_client.headers["Authorization"], "Api-Token test-token-123"
        )

    def test_custom_auth_header_name(self):
        """Test that a custom auth header name can be used."""
        client = AuthenticatedClient(
            base_url="https://test.qualer.com",
            token="test-token-123",
            auth_header_name="X-API-Key",
        )

        # Get the httpx client to trigger header setup
        httpx_client = client.get_httpx_client()

        # Check that the custom auth header is set correctly
        self.assertIn("X-API-Key", httpx_client.headers)
        self.assertEqual(httpx_client.headers["X-API-Key"], "Api-Token test-token-123")
        # Authorization header should not be set
        self.assertNotIn("Authorization", httpx_client.headers)

    def test_with_headers_preserves_auth(self):
        """Test that with_headers preserves the authorization header."""
        client = AuthenticatedClient(
            base_url="https://test.qualer.com", token="test-token-123"
        )

        # Add additional headers
        new_client = client.with_headers({"X-Custom": "value"})

        # Get the httpx client to trigger header setup
        httpx_client = new_client.get_httpx_client()

        # Check that both custom and auth headers are present
        self.assertIn("Authorization", httpx_client.headers)
        self.assertIn("X-Custom", httpx_client.headers)
        self.assertEqual(
            httpx_client.headers["Authorization"], "Api-Token test-token-123"
        )
        self.assertEqual(httpx_client.headers["X-Custom"], "value")

    def test_backward_compatibility_with_bearer(self):
        """Test that existing code using Bearer prefix still works."""
        client = AuthenticatedClient(
            base_url="https://test.qualer.com", token="test-token-123", prefix="Bearer"
        )

        # Get the httpx client to trigger header setup
        httpx_client = client.get_httpx_client()

        # Check that Bearer still works for backward compatibility
        self.assertIn("Authorization", httpx_client.headers)
        self.assertEqual(httpx_client.headers["Authorization"], "Bearer test-token-123")

    def test_token_only_without_prefix(self):
        """Test various scenarios where prefix might be falsy."""
        test_cases = [
            ("", "test-token"),  # empty string
            (None, "test-token"),  # None
            (False, "test-token"),  # False
        ]

        for prefix, expected_header in test_cases:
            with self.subTest(prefix=prefix):
                client = AuthenticatedClient(
                    base_url="https://test.qualer.com",
                    token="test-token",
                    prefix=prefix,
                )

                httpx_client = client.get_httpx_client()
                self.assertEqual(httpx_client.headers["Authorization"], expected_header)


if __name__ == "__main__":
    unittest.main()
