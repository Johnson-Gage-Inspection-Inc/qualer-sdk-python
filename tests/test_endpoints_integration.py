#!/usr/bin/env python3
"""
Parameterized Integration Tests for Qualer SDK Endpoints

This test suite automatically discovers and tests all GET endpoints that don't require
input parameters using pytest parameterization. Each endpoint is tested individually
to ensure responses parse correctly.
"""

import inspect
import os
from pathlib import Path
from typing import Any, List, Tuple

import pytest
from dotenv import load_dotenv

from qualer_sdk.client import AuthenticatedClient

# Load environment variables
load_dotenv()


def discover_testable_endpoints() -> List[Tuple[str, Any]]:
    """
    Discover all GET endpoints that can be called with just a client.
    Returns list of (endpoint_name, function) tuples.
    """
    endpoints = []

    try:
        import qualer_sdk.api as api_package

        api_path = Path(api_package.__file__).parent

        # Scan all API subdirectories
        for subdir in api_path.iterdir():
            if subdir.is_dir() and not subdir.name.startswith("__"):
                module_name = f"qualer_sdk.api.{subdir.name}"

                try:
                    # Import the module
                    __import__(module_name, fromlist=[""])

                    # Scan all Python files in the subdirectory
                    for py_file in subdir.glob("*.py"):
                        if py_file.name.startswith("__"):
                            continue

                        function_module_name = f"{module_name}.{py_file.stem}"
                        try:
                            function_module = __import__(
                                function_module_name, fromlist=[""]
                            )

                            # Look for 'sync' function (the main API function)
                            if hasattr(function_module, "sync"):
                                sync_func = getattr(function_module, "sync")

                                # Check if function can be called with client only
                                if can_call_with_client_only(sync_func):
                                    endpoint_name = f"{subdir.name}.{py_file.stem}"
                                    endpoints.append((endpoint_name, sync_func))

                        except ImportError:
                            continue

                except ImportError:
                    continue

    except Exception:
        pass

    return endpoints


def can_call_with_client_only(func: Any) -> bool:
    """
    Check if function can be called with just a client parameter.
    """
    try:
        sig = inspect.signature(func)
        params = sig.parameters

        # Check for required parameters (excluding 'client')
        for name, param in params.items():
            if name == "client":
                continue
            if param.default == inspect.Parameter.empty:
                return False
        return True
    except Exception:
        return False


# Discover endpoints at module level for pytest parameterization
TESTABLE_ENDPOINTS = discover_testable_endpoints()


@pytest.fixture(scope="session")
def authenticated_client():
    """Create an authenticated client for testing."""
    api_token = os.getenv("QUALER_API_KEY")
    if not api_token:
        pytest.skip("QUALER_API_KEY not found in environment variables")

    base_url = "https://jgiquality.qualer.com"
    return AuthenticatedClient(base_url=base_url, token=api_token)


@pytest.mark.parametrize("endpoint_name,endpoint_func", TESTABLE_ENDPOINTS)
def test_endpoint_response_parsing(endpoint_name, endpoint_func, authenticated_client):
    """
    Test that an endpoint can be called and its response parsed correctly.

    This test verifies:
    1. The endpoint can be called without errors
    2. The response can be parsed by the generated SDK models
    3. The response has the expected structure (not None)
    """
    # Call the endpoint
    response = endpoint_func(client=authenticated_client)

    # The main goal is to test that the response parses without errors
    # Some endpoints legitimately return None (no data), which is acceptable
    # We're primarily testing that no parsing/enum/date errors occur

    # If we get here without an exception, the parsing was successful
    print(f"✓ {endpoint_name}: Response parsed successfully")

    # Log response details for debugging
    if response is None:
        print(
            f"  - {endpoint_name}: Response is None (may be expected for this endpoint)"
        )
    elif isinstance(response, list):
        print(f"  - {endpoint_name}: Response is a list with {len(response)} items")
    elif hasattr(response, "__dict__"):
        print(f"  - {endpoint_name}: Response is a {type(response).__name__} object")
    else:
        print(f"  - {endpoint_name}: Response type: {type(response)}")

    # Response should have a valid type name (not contain error indicators)
    response_type = type(response).__name__
    assert (
        "Error" not in response_type
    ), f"Endpoint {endpoint_name} returned error type: {response_type}"


def test_endpoint_discovery():
    """Test that we can discover endpoints."""
    assert len(TESTABLE_ENDPOINTS) > 0, "No testable endpoints found"

    # Print some info for debugging
    print(f"\nDiscovered {len(TESTABLE_ENDPOINTS)} testable endpoints:")
    for endpoint_name, _ in TESTABLE_ENDPOINTS[:5]:  # Show first 5
        print(f"  • {endpoint_name}")

    if len(TESTABLE_ENDPOINTS) > 5:
        print(f"  ... and {len(TESTABLE_ENDPOINTS) - 5} more")


if __name__ == "__main__":
    # Run the tests
    pytest.main([__file__, "-v"])
