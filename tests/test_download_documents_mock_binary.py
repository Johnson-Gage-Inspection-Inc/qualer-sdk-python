#!/usr/bin/env python3
"""
Mock Test for download_documents endpoint with binary content

This test verifies that the download_documents endpoint correctly handles binary content
when mocked with actual binary data, ensuring no UnicodeDecodeError occurs.
"""

import unittest
from unittest.mock import MagicMock, patch

import httpx

from qualer_sdk.api.asset_service_records import download_documents
from qualer_sdk.client import AuthenticatedClient
from qualer_sdk.types import File


class TestDownloadDocumentsMockBinary(unittest.TestCase):
    """Mock tests for the download_documents endpoint with binary content."""

    def setUp(self):
        """Set up test client."""
        self.client = AuthenticatedClient(
            base_url="https://test.qualer.com", token="test-token"
        )

    @patch("httpx.Client.request")
    def test_download_documents_with_mock_pdf(self, mock_request):
        """
        Test download_documents endpoint with mocked PDF binary content.

        This test should:
        1. Mock a successful 200 response with PDF binary content
        2. Verify the response is correctly parsed as a File object
        3. Ensure no UnicodeDecodeError occurs
        """
        print("\n📄 Testing download_documents with mock PDF content...")

        # Create mock PDF binary content
        pdf_content = (
            b"%PDF-1.4\n"
            b"1 0 obj\n"
            b"<<\n"
            b"/Type /Catalog\n"
            b"/Pages 2 0 R\n"
            b">>\n"
            b"endobj\n"
            b"2 0 obj\n"
            b"<<\n"
            b"/Type /Pages\n"
            b"/Kids [3 0 R]\n"
            b"/Count 1\n"
            b">>\n"
            b"endobj\n"
            b"3 0 obj\n"
            b"<<\n"
            b"/Type /Page\n"
            b"/Parent 2 0 R\n"
            b"/MediaBox [0 0 612 792]\n"
            b">>\n"
            b"endobj\n"
            b"xref\n"
            b"0 4\n"
            b"0000000000 65535 f \n"
            b"0000000009 00000 n \n"
            b"0000000074 00000 n \n"
            b"0000000120 00000 n \n"
            b"trailer\n"
            b"<<\n"
            b"/Size 4\n"
            b"/Root 1 0 R\n"
            b">>\n"
            b"startxref\n"
            b"207\n"
            b"%%EOF\n"
        )

        # Mock the HTTP response
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.status_code = 200
        mock_response.content = pdf_content
        mock_response.headers = {
            "content-type": "application/pdf",
            "content-length": str(len(pdf_content)),
        }

        mock_request.return_value = mock_response

        # Call the download_documents endpoint
        result = download_documents.sync_detailed(
            asset_service_record_id=123, client=self.client
        )

        print(f"📊 Response status: {result.status_code}")
        print(f"📄 Content length: {len(result.content)} bytes")

        # Verify the response
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.content, pdf_content)
        self.assertIsNotNone(result.parsed)
        self.assertIsInstance(result.parsed, File)

        # Verify the File object contains the PDF content
        if result.parsed is not None:
            file_content = result.parsed.payload.read()
            self.assertEqual(file_content, pdf_content)
            self.assertTrue(file_content.startswith(b"%PDF"))
            print("✅ PDF content correctly handled as binary data")

            # Reset payload position
            result.parsed.payload.seek(0)

        print("✅ No UnicodeDecodeError occurred with binary PDF content")

    @patch("httpx.Client.request")
    def test_download_documents_with_mock_zip(self, mock_request):
        """
        Test download_documents endpoint with mocked ZIP binary content.
        """
        print("\n📦 Testing download_documents with mock ZIP content...")

        # Create mock ZIP binary content (ZIP file signature)
        zip_content = (
            b"PK\x03\x04\x14\x00\x00\x00\x08\x00"
            b"\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            b"\x08\x00\x00\x00test.txt"
            b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            b"PK\x01\x02\x14\x00\x14\x00\x00\x00\x08\x00"
            b"\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            b"\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x01\x00\x00\x00\x00"
            b"test.txt"
            b"PK\x05\x06\x00\x00\x00\x00\x01\x00\x01\x006\x00\x00\x00\x1a\x00\x00\x00\x00\x00"
        )

        # Mock the HTTP response
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.status_code = 200
        mock_response.content = zip_content
        mock_response.headers = {
            "content-type": "application/zip",
            "content-length": str(len(zip_content)),
        }

        mock_request.return_value = mock_response

        # Call the download_documents endpoint
        result = download_documents.sync(
            asset_service_record_id=456, client=self.client
        )

        # Verify the response
        self.assertIsNotNone(result)
        self.assertIsInstance(result, File)

        # Verify the File object contains the ZIP content
        if result is not None:
            file_content = result.payload.read()
            self.assertEqual(file_content, zip_content)
            self.assertTrue(file_content.startswith(b"PK"))
            print("✅ ZIP content correctly handled as binary data")

        print("✅ No UnicodeDecodeError occurred with binary ZIP content")

    @patch("httpx.Client.request")
    def test_download_documents_with_mock_image(self, mock_request):
        """
        Test download_documents endpoint with mocked PNG image binary content.
        """
        print("\n🖼️ Testing download_documents with mock PNG content...")

        # Create mock PNG binary content
        png_content = (
            b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01"
            b"\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\tpHYs\x00\x00\x0b\x13"
            b"\x00\x00\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\x00\x0cIDATx\x9cc```"
            b"\x00\x00\x00\x04\x00\x01\xdd\xac\xb8\x18\x00\x00\x00\x00IEND\xaeB`\x82"
        )

        # Mock the HTTP response
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.status_code = 200
        mock_response.content = png_content
        mock_response.headers = {
            "content-type": "image/png",
            "content-length": str(len(png_content)),
        }

        mock_request.return_value = mock_response

        # Call the download_documents endpoint
        result = download_documents.sync_detailed(
            asset_service_record_id=789, client=self.client
        )

        # Verify the response
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.content, png_content)
        self.assertIsNotNone(result.parsed)

        # Verify the File object contains the PNG content
        if result.parsed is not None:
            file_content = result.parsed.payload.read()
            self.assertEqual(file_content, png_content)
            self.assertTrue(file_content.startswith(b"\x89PNG"))
            print("✅ PNG content correctly handled as binary data")

        print("✅ No UnicodeDecodeError occurred with binary PNG content")

    @patch("httpx.Client.request")
    def test_download_documents_mock_error_response(self, mock_request):
        """
        Test that error responses don't cause UnicodeDecodeError.
        """
        print("\n❌ Testing download_documents error response handling...")

        # Mock a 404 error response
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.status_code = 404
        mock_response.content = b""
        mock_response.headers = {"content-type": "text/plain"}

        mock_request.return_value = mock_response

        # Call the download_documents endpoint
        result = download_documents.sync_detailed(
            asset_service_record_id=999, client=self.client
        )

        # Verify the error response is handled correctly
        self.assertEqual(result.status_code, 404)
        self.assertIsNone(result.parsed)  # Should be None for 404
        print("✅ Error response handled gracefully without UnicodeDecodeError")

    def test_download_documents_api_structure(self):
        """
        Test that the download_documents API has the expected structure.
        """
        print("\n🔍 Verifying download_documents API structure...")

        # Verify the module has the expected functions
        self.assertTrue(hasattr(download_documents, "sync"))
        self.assertTrue(hasattr(download_documents, "sync_detailed"))
        self.assertTrue(hasattr(download_documents, "asyncio"))
        self.assertTrue(hasattr(download_documents, "asyncio_detailed"))

        print("✅ download_documents API has all expected functions")

        # Verify the functions are callable
        self.assertTrue(callable(download_documents.sync))
        self.assertTrue(callable(download_documents.sync_detailed))

        print("✅ download_documents API functions are callable")


if __name__ == "__main__":
    unittest.main()
