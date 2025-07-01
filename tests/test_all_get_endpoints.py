#!/usr/bin/env python3
"""
Comprehensive GET Endpoint Test

This script automatically discovers and tests all GET endpoints that don't require
input parameters to ensure they can be called and parsed without errors.
"""

import inspect
import os
import sys
import traceback
from pathlib import Path
from typing import Any, Dict, List, Tuple

from qualer_sdk.client import AuthenticatedClient

from dotenv import load_dotenv

# Add the src directory to the Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

# Load environment variables

load_dotenv()


def discover_get_endpoints() -> List[Tuple[str, Any]]:
    """
    Discover all GET endpoints by scanning the API modules.
    Returns list of (endpoint_name, function) tuples.
    """
    print(
        "If there are errors, update spec.json and regenerate the SDK and re-test using:"
    )
    print("python regenerate_sdk.py && test_asset_pool.py")
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
                            function_module = __import__(
                                function_module_name, fromlist=[""]
                            )

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


def check_endpoint(
    endpoint_name: str, func: Any, client: AuthenticatedClient
) -> Dict[str, Any]:
    """
    Test a single endpoint and return results.
    """
    result = {
        "endpoint": endpoint_name,
        "success": False,
        "error": None,
        "response_type": None,
        "response_length": None,
        "signature_info": None,
    }

    try:
        # Analyze the function signature
        sig_info = analyze_function_signature(func)
        result["signature_info"] = sig_info  # Only test if we can call with client only
        if not sig_info["can_call_with_client_only"]:
            result["error"] = f"Requires parameters: {sig_info['required_params']}"
            return result

        # Call the endpoint
        print(f"  🔍 Testing {endpoint_name}...")
        response = func(client=client)

        result["success"] = True
        result["response_type"] = type(
            response
        ).__name__  # Try to get length if it's a list/dict
        try:
            if response is not None and hasattr(response, "__len__"):
                result["response_length"] = len(response)
        except Exception as e:
            result["length_error"] = f"Length check failed: {str(e)}"

    except Exception as e:
        result["error"] = str(e)
        result["traceback"] = traceback.format_exc()

    return result


def main():
    print("🚀 Starting comprehensive GET endpoint test...")

    # Get API token from environment
    api_token = os.getenv("QUALER_API_KEY")
    if not api_token:
        print("❌ QUALER_API_KEY not found in environment variables")
        return 1

    # Create authenticated client
    client = AuthenticatedClient(api_token)

    print("🔧 Connected to Qualer API")
    print(f"🔑 Using API token: {api_token[:8]}...")

    # Discover all endpoints
    print("\n📡 Discovering API endpoints...")
    endpoints = discover_get_endpoints()
    print(f"✅ Found {len(endpoints)} potential endpoints")

    # Test each endpoint
    results = []
    testable_count = 0
    success_count = 0

    print("\n🧪 Testing endpoints...")

    for endpoint_name, func in endpoints:
        result = check_endpoint(endpoint_name, func, client)
        results.append(result)

        if (
            result["signature_info"]
            and result["signature_info"]["can_call_with_client_only"]
        ):
            testable_count += 1
            if result["success"]:
                success_count += 1
                print(f"  ✅ {endpoint_name}: {result['response_type']}", end="")
                if result["response_length"] is not None:
                    print(f" (length: {result['response_length']})")
                else:
                    print()
            else:
                print(f"  ❌ {endpoint_name}: {result['error']}")
        else:
            print(f"  ⏭️  {endpoint_name}: Skipped (requires parameters)")

    # Summary
    print("\n📊 Test Summary:")
    print(f"  Total endpoints discovered: {len(endpoints)}")
    print(f"  Testable endpoints (no required params): {testable_count}")
    print(f"  Successful tests: {success_count}")
    print(f"  Failed tests: {testable_count - success_count}")
    print(
        f"  Success rate: {(success_count/testable_count)*100:.1f}%"
        if testable_count > 0
        else "  Success rate: N/A"
    )

    # Detailed results for failures
    failed_tests = [
        r
        for r in results
        if r["signature_info"]
        and r["signature_info"]["can_call_with_client_only"]
        and not r["success"]
    ]

    if failed_tests:
        print(f"\n❌ Failed Tests ({len(failed_tests)}):")
        for result in failed_tests:
            print(f"  • {result['endpoint']}: {result['error']}")
            if "traceback" in result and os.getenv("VERBOSE_ERRORS"):
                print(f"    {result['traceback']}")

    # Show some successful examples
    successful_tests = [r for r in results if r["success"]][:5]
    if successful_tests:
        print("\n✅ Sample Successful Tests:")
        for result in successful_tests:
            print(f"  • {result['endpoint']}: {result['response_type']}", end="")
            if result["response_length"] is not None:
                print(f" (length: {result['response_length']})")
            else:
                print()

    # Show endpoints that require parameters
    param_required = [
        r
        for r in results
        if r["signature_info"] and not r["signature_info"]["can_call_with_client_only"]
    ][:5]
    if param_required:
        print("\n📝 Sample Endpoints Requiring Parameters:")
        for result in param_required:
            req_params = result["signature_info"]["required_params"]
            print(f"  • {result['endpoint']}: requires {req_params}")

    return 0 if testable_count == 0 or success_count == testable_count else 1


if __name__ == "__main__":
    sys.exit(main())
