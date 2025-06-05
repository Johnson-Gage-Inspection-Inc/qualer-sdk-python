#!/usr/bin/env python3
"""
Comprehensive test script for the qualer-sdk package restructuring.
"""


def test_imports():
    """Test all major imports work correctly."""
    try:
        # Basic package import
        import qualer_sdk

        print("✓ Package imported successfully")
        print(f"✓ Version: {qualer_sdk.__version__}")

        # Core imports
        from qualer_sdk import ApiClient, Configuration

        print("✓ Core classes imported")

        # API imports
        from qualer_sdk.api import AccountApi, AssetsApi, CommonApi, ServiceOrdersApi

        print("✓ API classes imported")

        # Model imports
        from qualer_sdk import models

        print("✓ Models package imported")
        # Test client creation
        config = Configuration()
        client = ApiClient(config)
        print("✓ Client instantiation successful")

        # Use assertion instead of return for pytest
        assert client is not None
        assert config is not None

    except Exception as e:
        print(f"✗ Import test failed: {e}")
        assert False, f"Import test failed: {e}"


def test_api_classes():
    """Test that API classes can be instantiated."""
    try:
        from qualer_sdk import ApiClient, Configuration
        from qualer_sdk.api import AccountApi, AssetsApi

        config = Configuration()
        client = ApiClient(config)
        # Test API instantiation
        account_api = AccountApi(client)
        assets_api = AssetsApi(client)

        print("✓ API classes instantiated successfully")
        # Use assertion instead of return for pytest
        assert account_api is not None
        assert assets_api is not None

    except Exception as e:
        print(f"✗ API class test failed: {e}")
        assert False, f"API class test failed: {e}"


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
        test_api_classes()
        tests_passed += 1
    except Exception as e:
        print(f"API class test failed: {e}")

    print("=" * 50)
    if tests_passed == total_tests:
        print("🎉 All tests passed! Package restructuring is successful.")
        print(f"✓ {tests_passed}/{total_tests} tests passed")
    else:
        print(f"❌ Some tests failed: {tests_passed}/{total_tests} tests passed")

    return tests_passed == total_tests


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
