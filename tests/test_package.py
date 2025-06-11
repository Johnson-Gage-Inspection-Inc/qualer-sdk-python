#!/usr/bin/env python3
"""
Comprehensive test script for the qualer-sdk package - modernized for openapi-python-client.
"""


def test_imports():
    """Test all major imports work correctly."""
    try:
        # Basic package import
        import qualer_sdk

        print("✓ Package imported successfully")
        print(
            f"✓ Version: {qualer_sdk.__version__}"
        )  # Core imports (modern openapi-python-client style)
        from qualer_sdk import Client

        print("✓ Core classes imported")

        # API imports (function-based APIs)
        from qualer_sdk.api.account import login
        from qualer_sdk.api.assets import get_asset

        print("✓ API functions imported")

        # Model imports
        from qualer_sdk import models  # noqa: F401

        print("✓ Models package imported")

        # Test client creation (modern style)
        client = Client(base_url="https://api.example.com")
        print("✓ Client instantiation successful")

        # Use assertion instead of return for pytest
        assert client is not None
        assert login is not None
        assert get_asset is not None

    except Exception as e:
        print(f"✗ Import test failed: {e}")
        assert False, f"Import test failed: {e}"


def test_api_functions():
    """Test that API functions can be imported and are callable."""
    try:
        from qualer_sdk import Client
        from qualer_sdk.api.account import companies, login
        from qualer_sdk.api.assets import get_asset

        # Test client creation
        client = Client(base_url="https://api.example.com")

        # Test that API functions are callable (don't actually call them)
        assert callable(login.sync)
        assert callable(companies.sync)
        assert callable(get_asset.sync)

        print("✓ API functions are callable")

        # Use assertion instead of return for pytest
        assert client is not None

    except Exception as e:
        print(f"✗ API function test failed: {e}")
        assert False, f"API function test failed: {e}"


def main():
    """Run all tests."""
    print("🧪 Testing qualer-sdk package...")
    print("=" * 50)

    tests_passed = 0
    total_tests = 2

    try:
        test_imports()
        tests_passed += 1
    except Exception as e:
        print(f"Import test failed: {e}")

    try:
        test_api_functions()
        tests_passed += 1
    except Exception as e:
        print(f"API function test failed: {e}")

    print("=" * 50)
    if tests_passed == total_tests:
        print("🎉 All tests passed! Package restructuring is successful.")
        print(f"✓ {tests_passed}/{total_tests} tests passed")
    else:
        print(f"❌ Some tests failed: {tests_passed}/{total_tests} tests passed")

    return tests_passed == total_tests


if __name__ == "__main__":
    main()
