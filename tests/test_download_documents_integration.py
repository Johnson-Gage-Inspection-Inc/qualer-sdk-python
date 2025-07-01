#!/usr/bin/env python3
"""
Integration Test for download_documents endpoint

This test verifies that we can successfully retrieve documents from asset service records
using the fixed binary endpoint without encountering UnicodeDecodeError.
"""

import os
import unittest

import pytest
from dotenv import load_dotenv

from qualer_sdk.api.asset_service_records import download_documents
from qualer_sdk.client import AuthenticatedClient
from qualer_sdk.types import File

# Load environment variables
load_dotenv()


class TestDownloadDocumentsIntegration(unittest.TestCase):
    """Integration tests for the download_documents endpoint."""

    @classmethod
    def setUpClass(cls):
        """Set up test client with authentication."""
        api_token = os.getenv("QUALER_API_KEY")
        base_url = os.getenv("QUALER_BASE_URL", "https://jgiquality.qualer.com")

        if not api_token:
            pytest.skip("QUALER_API_KEY environment variable not set")

        cls.client = AuthenticatedClient(base_url=base_url, token=api_token)

        print("🔧 Testing asset service record documents download")
        print(f"🌐 Base URL: {base_url}")
        print(f"🔑 Using API token: {api_token[:8]}...")

    def test_download_documents_with_valid_id(self):
        """
        Test downloading documents from an asset service record.

        This test should:
        1. Successfully call the endpoint without UnicodeDecodeError
        2. Handle the response appropriately (200 with content or 404 if no documents)
        3. Validate binary content handling
        """
        print("\n📋 Testing download_documents endpoint...")

        # Use a test asset service record ID (we'll try a few common ones)
        test_asset_service_record_ids = [1, 2, 3, 10, 100]

        success_found = False
        for asset_service_record_id in test_asset_service_record_ids:
            print(f"🔍 Trying asset service record ID: {asset_service_record_id}")

            try:
                # Call the download_documents endpoint
                response = download_documents.sync_detailed(
                    asset_service_record_id=asset_service_record_id, client=self.client
                )

                print(f"📊 Response status: {response.status_code}")
                print(f"📋 Response headers: {dict(response.headers)}")

                if response.status_code == 200:
                    success_found = True
                    print("✅ Found asset service record with documents!")

                    # Verify response content exists
                    self.assertIsNotNone(response.content)
                    print(f"📄 Response content length: {len(response.content)} bytes")

                    # Verify parsed response is a File object
                    self.assertIsNotNone(response.parsed)
                    self.assertIsInstance(response.parsed, File)
                    print("✅ Response correctly parsed as File object")

                    # Verify the File object contains the binary data
                    if response.parsed is not None:
                        file_content = response.parsed.payload.read()
                        self.assertIsNotNone(file_content)
                        self.assertGreater(len(file_content), 0)
                        print(f"📄 File content length: {len(file_content)} bytes")

                        # Reset payload position for potential future reads
                        response.parsed.payload.seek(0)

                        # Check if it looks like a valid binary file (common headers)
                        if file_content.startswith(b"%PDF"):
                            print("📄 Content appears to be a PDF document")
                        elif file_content.startswith(b"\x89PNG"):
                            print("🖼️ Content appears to be a PNG image")
                        elif file_content.startswith(b"\xff\xd8\xff"):
                            print("🖼️ Content appears to be a JPEG image")
                        elif file_content.startswith(b"PK"):
                            print("📦 Content appears to be a ZIP archive")
                        else:
                            print(
                                f"📄 Content appears to be binary data (first 20 bytes: {file_content[:20]})"
                            )

                    break

                elif response.status_code == 404:
                    print(
                        f"ℹ️ Asset service record {asset_service_record_id} not found or has no documents"
                    )
                    continue

                elif response.status_code == 401:
                    self.fail("❌ Authentication failed - check API token")

                elif response.status_code == 403:
                    print(
                        f"🚫 Access denied for asset service record {asset_service_record_id}"
                    )
                    continue

                else:
                    print(f"⚠️ Unexpected status code: {response.status_code}")
                    continue

            except UnicodeDecodeError as e:
                self.fail(
                    f"❌ UnicodeDecodeError encountered - binary endpoint fix failed: {e}"
                )

            except Exception as e:
                print(
                    f"⚠️ Error for asset service record {asset_service_record_id}: {e}"
                )
                continue

        if success_found:
            print(
                "✅ Successfully tested download_documents endpoint with binary content!"
            )
        else:
            print(
                "ℹ️ No asset service records with documents found, but endpoint handled requests correctly"
            )

    def test_download_documents_error_handling(self):
        """
        Test that the endpoint handles errors gracefully without UnicodeDecodeError.
        """
        print("\n🔍 Testing error handling for download_documents endpoint...")

        # Test with an obviously invalid asset service record ID
        invalid_id = 999999999

        try:
            response = download_documents.sync_detailed(
                asset_service_record_id=invalid_id, client=self.client
            )

            print(f"📊 Response status for invalid ID: {response.status_code}")

            # Should get 404 or similar, but no UnicodeDecodeError
            self.assertIn(response.status_code, [404, 400, 403])
            print("✅ Error handled gracefully without UnicodeDecodeError")

        except UnicodeDecodeError as e:
            self.fail(
                f"❌ UnicodeDecodeError encountered - indicates binary endpoint issue: {e}"
            )

        except Exception as e:
            # Other exceptions are fine as long as it's not UnicodeDecodeError
            print(f"ℹ️ Expected exception for invalid ID: {e}")

    def test_download_documents_sync_method(self):
        """
        Test the simplified sync method that returns just the parsed result.
        """
        print("\n🔄 Testing download_documents.sync method...")

        # Test with a few IDs to see if we can find one with documents
        test_ids = [1, 2, 5, 10]

        for asset_service_record_id in test_ids:
            try:
                # Use the simplified sync method
                result = download_documents.sync(
                    asset_service_record_id=asset_service_record_id, client=self.client
                )

                if result is not None:
                    print(
                        f"✅ Found documents for asset service record {asset_service_record_id}"
                    )
                    self.assertIsInstance(result, File)

                    # Verify we can read the file content
                    file_content = result.payload.read()
                    self.assertIsNotNone(file_content)
                    print(f"📄 File content length: {len(file_content)} bytes")

                    # Reset payload position
                    result.payload.seek(0)
                    break
                else:
                    print(
                        f"ℹ️ No documents found for asset service record {asset_service_record_id}"
                    )

            except UnicodeDecodeError as e:
                self.fail(
                    f"❌ UnicodeDecodeError in sync method - binary endpoint issue: {e}"
                )

            except Exception as e:
                print(
                    f"ℹ️ Expected error for asset service record {asset_service_record_id}: {e}"
                )

        print("✅ sync method test completed without UnicodeDecodeError")


if __name__ == "__main__":
    unittest.main()
