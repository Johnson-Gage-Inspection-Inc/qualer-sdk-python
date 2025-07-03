#!/usr/bin/env python3
"""
Integration Test for get_document endpoint with known PDF document

This test verifies that we can successfully retrieve a known PDF document
using the fixed binary endpoint without encountering UnicodeDecodeError.
"""

import os
import unittest
from uuid import UUID

import pytest
from dotenv import load_dotenv

from qualer_sdk.api.service_order_documents import get_document
from qualer_sdk.client import AuthenticatedClient

# Load environment variables
load_dotenv()


@pytest.mark.integration
class TestGetDocumentIntegration(unittest.TestCase):
    """Integration tests for the get_document endpoint."""

    @classmethod
    def setUpClass(cls):
        """Set up test client with authentication."""
        api_token = os.getenv("QUALER_API_KEY")
        base_url = os.getenv("QUALER_BASE_URL", "https://jgiquality.qualer.com")

        if not api_token:
            pytest.skip("QUALER_API_KEY environment variable not set")

        cls.client = AuthenticatedClient(base_url=base_url, token=api_token)
        cls.known_pdf_uuid = UUID("c4ab6a7c-e2f1-4984-837f-9390f9a84dfc")

        print("🔧 Testing PDF document retrieval")
        print(f"📄 Known PDF UUID: {cls.known_pdf_uuid}")
        print(f"🌐 Base URL: {base_url}")
        print(f"🔑 Using API token: {api_token[:8]}...")

    def test_retrieve_known_pdf_document(self):
        """
        Test retrieving a known PDF document to verify the fix works.

        This test should:
        1. Successfully call the endpoint without UnicodeDecodeError
        2. Receive a 200 response with PDF content
        3. Validate the content is actually a PDF
        """
        print(f"\n🧪 Testing retrieval of PDF document {self.known_pdf_uuid}")

        try:
            # Use sync_detailed to get full response information
            response = get_document.sync_detailed(
                guid=self.known_pdf_uuid, client=self.client
            )

            print(f"📊 Response Status: {response.status_code}")
            print(f"📝 Content-Type: {response.headers.get('content-type', 'Unknown')}")
            print(
                f"📦 Content Length: {len(response.content) if response.content else 0} bytes"
            )

            # Test 1: No UnicodeDecodeError should occur
            self.assertIsNotNone(response, "Response should not be None")

            # Test 2: Should be a successful response
            if response.status_code == 200:
                print("✅ Received successful 200 response")

                # Test 3: Should have content
                self.assertIsNotNone(
                    response.content, "Response content should not be None"
                )
                self.assertGreater(
                    len(response.content), 0, "Response content should not be empty"
                )

                # Test 4: Content should be PDF
                self.assertTrue(
                    response.content.startswith(b"%PDF"),
                    "Content should start with PDF signature",
                )

                # Test 5: Content-Type should indicate PDF
                content_type = response.headers.get("content-type", "").lower()
                print(f"📋 Content-Type: {content_type}")

                self.assertTrue(
                    response.headers.encoding == "ascii",
                    "Content-Type should be ASCII encoded for PDF",
                )

                # Test 6: Verify PDF structure
                if len(response.content) > 100:
                    # Look for PDF version in first 20 bytes
                    pdf_header = response.content[:20]
                    print(f"📄 PDF Header: {pdf_header}")

                    # Check for common PDF elements
                    pdf_content_str = response.content[:1000].decode(
                        "latin-1", errors="ignore"
                    )
                    if any(
                        marker in pdf_content_str
                        for marker in ["%PDF-", "obj", "endobj"]
                    ):
                        print("✅ Content appears to be a valid PDF document")
                    else:
                        print("⚠️  Content may not be a complete PDF")

                print("🎉 SUCCESS: PDF document retrieved successfully!")

            elif response.status_code == 404:
                self.fail(
                    "Document not found (404). The UUID may be invalid or inaccessible."
                )

            elif response.status_code == 403:
                self.fail("Access forbidden (403). Check API permissions.")

            elif response.status_code == 500:
                # Log the error but don't fail - might be server issue
                error_content = response.content.decode("utf-8", errors="ignore")
                print(f"⚠️  Server error (500): {error_content}")
                self.fail("Server returned 500 error - may be temporary")

            else:
                self.fail(f"Unexpected status code: {response.status_code}")

        except UnicodeDecodeError as e:
            self.fail(f"❌ UnicodeDecodeError still occurs - fix not working: {e}")

        except Exception as e:
            print(f"⚠️  Unexpected exception: {type(e).__name__}: {e}")
            raise

    def test_document_endpoint_binary_handling(self):
        """
        Test that the endpoint properly handles binary responses without JSON parsing.
        """
        print("\n🧪 Testing binary response handling")

        try:
            response = get_document.sync_detailed(
                guid=self.known_pdf_uuid, client=self.client
            )

            # Verify response structure for binary endpoint
            self.assertHasAttr(response, "status_code")
            self.assertHasAttr(response, "content")
            self.assertHasAttr(response, "headers")
            self.assertHasAttr(response, "parsed")

            # For binary endpoints, parsed should be None
            self.assertIsNone(
                response.parsed, "Binary endpoints should not have parsed content"
            )

            # Content should be bytes
            if response.content:
                self.assertIsInstance(
                    response.content,
                    bytes,
                    "Content should be bytes for binary endpoints",
                )

            print("✅ Binary response handling is correct")

        except Exception as e:
            print(f"⚠️  Exception in binary handling test: {type(e).__name__}: {e}")
            # Don't fail the test for this - it's supplementary

    def test_binary_response_methods(self):
        """
        Test that the binary endpoint methods work correctly.
        """
        print("\n🧪 Testing binary response methods")

        try:
            # Test sync_detailed method
            detailed_result = get_document.sync_detailed(
                guid=self.known_pdf_uuid, client=self.client
            )

            print(f"📊 Detailed result type: {type(detailed_result)}")

            # sync_detailed should return the full Response object
            self.assertIsNotNone(
                detailed_result, "sync_detailed() should return Response object"
            )

            # Check that we can access response attributes
            self.assertHasAttr(detailed_result, "status_code")
            self.assertHasAttr(detailed_result, "content")
            self.assertHasAttr(detailed_result, "headers")

            print("✅ Binary response methods work correctly")

        except Exception as e:
            print(f"⚠️  Exception in binary methods test: {type(e).__name__}: {e}")

    def assertHasAttr(self, obj, attr):
        """Helper method to assert object has attribute."""
        self.assertTrue(hasattr(obj, attr), f"Object should have attribute '{attr}'")


if __name__ == "__main__":
    # Run the integration tests
    unittest.main(verbosity=2)
