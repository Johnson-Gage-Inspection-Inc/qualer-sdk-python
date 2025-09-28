#!/usr/bin/env python3
"""
Comprehensive GET Endpoint Integration Test

This module automatically discovers and tests all GET endpoints that don't require
input parameters to ensure they can be called and parsed without errors.
"""

import inspect
import os
from pathlib import Path
from typing import Any, Dict, List, Tuple

import pytest

from qualer_sdk.client import AuthenticatedClient


def discover_get_endpoints() -> List[Tuple[str, Any]]:
    """
    Discover all GET endpoints by scanning the API modules.
    Returns list of (endpoint_name, function) tuples.
    """
    endpoints = []

    # Import the main API package
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
                            function_module = __import__(function_module_name, fromlist=[""])

                            # Look for 'sync' function (the main API function)
                            if hasattr(function_module, "sync"):
                                sync_func = getattr(function_module, "sync")
                                endpoint_name = f"{subdir.name}.{py_file.stem}"
                                endpoints.append((endpoint_name, sync_func))

                        except ImportError as e:
                            print(f"⚠️  Could not import {function_module_name}: {e}")
                            continue

                except ImportError as e:
                    print(f"⚠️  Could not import {module_name}: {e}")
                    continue

    except Exception as e:
        print(f"❌ Error discovering endpoints: {e}")

    return endpoints


def analyze_function_signature(func: Any) -> Dict[str, Any]:
    """
    Analyze function signature to determine if it can be called with just a client.
    Returns info about the function's parameters.
    """
    try:
        sig = inspect.signature(func)
        params = sig.parameters

        # Required parameters (excluding 'client')
        required_params = []
        optional_params = []

        for name, param in params.items():
            if name == "client":
                continue

            if param.default == inspect.Parameter.empty:
                required_params.append(name)
            else:
                optional_params.append(name)

        return {
            "can_call_with_client_only": len(required_params) == 0,
            "required_params": required_params,
            "optional_params": optional_params,
            "total_params": len(params),
        }

    except Exception as e:
        return {
            "can_call_with_client_only": False,
            "required_params": ["unknown"],
            "optional_params": [],
            "total_params": 0,
            "error": str(e),
        }


@pytest.fixture(scope="session")
def authenticated_client():
    """Create an authenticated client for testing."""
    api_token = os.getenv("QUALER_API_KEY")
    if not api_token:
        pytest.skip("QUALER_API_KEY not set in environment")
    return AuthenticatedClient(api_token)


@pytest.mark.vcr()
def test_get_endpoint_without_parameters(authenticated_client, endpoint_name, func, sig_info):
    """Test that GET endpoints that don't require parameters can be called successfully."""

    try:
        print(f"  🔍 Testing {endpoint_name}...")
        response = func(client=authenticated_client)

        # Note: None is a valid response (e.g., no data available)
        # We're just testing that the endpoint can be called without exceptions

        # Log response info for debugging
        response_type = type(response).__name__
        print(f"  ✅ {endpoint_name}: {response_type}", end="")

        if response is None:
            pytest.skip(f"Endpoint {endpoint_name} returned None response")

        try:
            if hasattr(response, "__len__"):
                response_length = len(response)
                print(f" (length: {response_length})")
            else:
                print()
        except Exception:
            print()

    except Exception as e:
        pytest.fail(f"Endpoint {endpoint_name} raised exception: {e}")


def test_endpoint_discovery():
    """Test that we can discover API endpoints."""
    endpoints = discover_get_endpoints()
    assert len(endpoints) > 0, "No API endpoints discovered"

    # Check that we have some expected endpoint patterns
    endpoint_names = [name for name, _ in endpoints]

    # Should have at least some common endpoints
    assert any("assets" in name for name in endpoint_names), "No assets endpoints found"
    assert any("clients" in name for name in endpoint_names), "No clients endpoints found"


def test_client_authentication(authenticated_client):
    """Test that the authenticated client is properly configured."""
    assert authenticated_client is not None
    assert hasattr(authenticated_client, "_client")
    assert hasattr(authenticated_client, "token")


def test_testable_endpoints_exist():
    """Test that there are endpoints that can be tested without parameters."""
    all_endpoints = discover_get_endpoints()

    testable = []
    for endpoint_name, func in all_endpoints:
        sig_info = analyze_function_signature(func)
        if sig_info["can_call_with_client_only"]:
            testable.append((endpoint_name, func, sig_info))

    assert len(testable) > 0, "No testable endpoints found"
    print(f"Found {len(testable)} testable endpoints")

    # Log a few examples
    for i, (endpoint_name, _, sig_info) in enumerate(testable[:5]):
        print(f"  Example {i+1}: {endpoint_name} (optional params: {sig_info['optional_params']})")


# Custom pytest collection to make parametrized tests work with fixtures
def pytest_generate_tests(metafunc):
    """Generate test parameters for parametrized tests."""
    if "endpoint_name" in metafunc.fixturenames and "func" in metafunc.fixturenames:
        # Discover endpoints at collection time
        all_endpoints = discover_get_endpoints()

        testable = []
        ids = []
        for endpoint_name, func in all_endpoints:
            sig_info = analyze_function_signature(func)
            if sig_info["can_call_with_client_only"]:
                testable.append((endpoint_name, func, sig_info))
                ids.append(endpoint_name)

        metafunc.parametrize("endpoint_name,func,sig_info", testable, ids=ids)


if __name__ == "__main__":
    # Allow running as a script for quick testing
    pytest.main([__file__, "-v", "-m", "integration"])
