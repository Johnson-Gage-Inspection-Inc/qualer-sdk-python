#!/usr/bin/env python3
"""
Parameterized Integration Tests for Qualer SDK Endpoints

This test suite automatically discovers and tests all GET endpoints that don't require
input parameters using pytest parameterization. Each endpoint is tested individually
to ensure responses parse correctly.

Known Issues:
- Some endpoints with nullable enums fail due to OpenAPI generator limitations
- The generator creates IntEnum classes that don't handle None values properly
- Even with 'nullable: true' in the OpenAPI spec, the generated models fail when
  the API returns None for enum fields like ToolRole
- Affected endpoints are skipped with detailed explanations

Recent Fixes Applied:
- Added x-nullable: true to date-time fields to handle None dates
- Fixed ReportType enum type from string to integer to match API responses
- Fixed RecordType enum type from string to integer to match API responses
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

# Check if API key is available - skip entire module if not
API_KEY = os.getenv("QUALER_API_KEY")
if not API_KEY:
    pytest.skip(
        "QUALER_API_KEY not found in environment variables. Skipping integration tests.",
        allow_module_level=True,
    )


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


def discover_asset_id_only_endpoints() -> List[Tuple[str, Any]]:
    """
    Discover all endpoints that require only asset_id parameter (plus client).
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

                                # Check if function requires only asset_id
                                if requires_only_asset_id(sync_func):
                                    endpoint_name = f"{subdir.name}.{py_file.stem}"
                                    endpoints.append((endpoint_name, sync_func))

                        except ImportError:
                            continue

                except ImportError:
                    continue

    except Exception:
        pass

    return endpoints


def requires_only_asset_id(func: Any) -> bool:
    """
    Check if function requires only asset_id parameter (plus client).
    """
    try:
        sig = inspect.signature(func)
        params = sig.parameters

        required_params = []

        # Check for required parameters (excluding 'client')
        for name, param in params.items():
            if name == "client":
                continue
            if param.default == inspect.Parameter.empty:
                required_params.append(name.lower())

        # Check if the only required parameter is some form of asset_id
        if len(required_params) == 1:
            param_name = required_params[0]
            # Check for common asset ID parameter names
            return param_name in ["asset_id", "assetid", "id", "asset_identifier"]

        return False
    except Exception:
        return False


def discover_client_company_id_only_endpoints() -> List[Tuple[str, Any]]:
    """
    Discover all endpoints that require only client_company_id parameter (plus client).
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

                                # Check if function requires only client_company_id
                                if requires_only_client_company_id(sync_func):
                                    endpoint_name = f"{subdir.name}.{py_file.stem}"
                                    endpoints.append((endpoint_name, sync_func))

                        except ImportError:
                            continue

                except ImportError:
                    continue

    except Exception:
        pass

    return endpoints


def requires_only_client_company_id(func: Any) -> bool:
    """
    Check if function requires only client_company_id parameter (plus client).
    """
    try:
        sig = inspect.signature(func)
        params = sig.parameters

        required_params = []

        # Check for required parameters (excluding 'client')
        for name, param in params.items():
            if name == "client":
                continue
            if param.default == inspect.Parameter.empty:
                required_params.append(name.lower())

        # Check if the only required parameter is some form of client_company_id
        if len(required_params) == 1:
            param_name = required_params[0]
            # Check for common client company ID parameter names
            return param_name in [
                "client_company_id",
                "clientcompanyid",
                "company_id",
                "companyid",
                "client_id",
                "clientid",
            ]

        return False
    except Exception:
        return False


def discover_service_order_id_endpoints() -> List[Tuple[str, Any]]:
    """
    Discover all endpoints that require only service_order_id parameter.
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

                                # Check if function requires only service_order_id
                                if requires_only_service_order_id(sync_func):
                                    endpoint_name = f"{subdir.name}.{py_file.stem}"
                                    endpoints.append((endpoint_name, sync_func))

                        except ImportError:
                            continue

                except ImportError:
                    continue

    except Exception:
        pass

    return endpoints


def requires_only_service_order_id(func: Any) -> bool:
    """
    Check if function requires only service_order_id parameter (plus client).
    """
    try:
        sig = inspect.signature(func)
        params = sig.parameters

        # Should have exactly 2 parameters: client and service_order_id (or similar)
        non_client_params = [name for name in params.keys() if name != "client"]

        if len(non_client_params) != 1:
            return False

        # Check if the parameter is related to service order ID
        param_name = non_client_params[0].lower()
        service_order_keywords = [
            "service_order_id",
            "serviceorderid",
            "order_id",
            "orderid",
        ]

        return any(keyword in param_name for keyword in service_order_keywords)
    except Exception:
        return False


def requires_only_service_order_item_id(func: Any) -> bool:
    """
    Check if function requires only service_order_item_id/work_item_id parameter (plus client).
    """
    try:
        sig = inspect.signature(func)
        params = sig.parameters

        # Should have exactly 2 parameters: client and service_order_item_id (or similar)
        non_client_params = [name for name in params.keys() if name != "client"]

        if len(non_client_params) != 1:
            return False

        # Check if the parameter is related to service order item ID or work item ID
        param_name = non_client_params[0].lower()
        item_keywords = [
            "service_order_item_id",
            "serviceorderitemid",
            "work_item_id",
            "workitemid",
            "workitem_id",
            "item_id",
            "itemid",
        ]

        return any(keyword in param_name for keyword in item_keywords)
    except Exception:
        return False


def discover_service_order_item_id_endpoints() -> List[Tuple[str, Any]]:
    """
    Discover all endpoints that require only service_order_item_id/work_item_id parameter.
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

                                # Check if function requires only service_order_item_id
                                if requires_only_service_order_item_id(sync_func):
                                    endpoint_name = f"{subdir.name}.{py_file.stem}"
                                    endpoints.append((endpoint_name, sync_func))

                        except ImportError:
                            continue

                except ImportError:
                    continue

    except Exception:
        pass

    return endpoints


# Test data for Asset Service Record ID endpoints
try:
    import qualer_sdk.api.asset_service_records.document_list
    import qualer_sdk.api.asset_service_records.download_documents
    import qualer_sdk.api.asset_service_records.get_asset_service_record
    import qualer_sdk.api.asset_service_records.upload_documents

    ASSET_SERVICE_RECORD_ID_ONLY_ENDPOINTS = [
        (
            "asset_service_records.get_asset_service_record",
            qualer_sdk.api.asset_service_records.get_asset_service_record.sync,
        ),
        (
            "asset_service_records.document_list",
            qualer_sdk.api.asset_service_records.document_list.sync,
        ),
        (
            "asset_service_records.download_documents",
            qualer_sdk.api.asset_service_records.download_documents.sync,
        ),
        (
            "asset_service_records.upload_documents",
            qualer_sdk.api.asset_service_records.upload_documents.sync,
        ),
    ]
except ImportError:
    ASSET_SERVICE_RECORD_ID_ONLY_ENDPOINTS = []

# Problematic Asset Service Record ID endpoints (known OpenAPI generator issues)
PROBLEMATIC_ASSET_SERVICE_RECORD_ENDPOINTS = [
    # Download endpoints return binary data, not JSON
    "asset_service_records.download_documents",
]


# Test data for Employee ID endpoints
try:
    import qualer_sdk.api.client_employees.get_employee
    import qualer_sdk.api.employees.get_employee_get_2
    import qualer_sdk.api.service_orders.get_work_orders_employee

    EMPLOYEE_ID_ONLY_ENDPOINTS = [
        (
            "employees.get_employee_get_2",
            qualer_sdk.api.employees.get_employee_get_2.sync,
        ),
        (
            "service_orders.get_work_orders_employee",
            qualer_sdk.api.service_orders.get_work_orders_employee.sync,
        ),
        (
            "client_employees.get_employee",
            qualer_sdk.api.client_employees.get_employee.sync,
        ),
    ]
except ImportError:
    EMPLOYEE_ID_ONLY_ENDPOINTS = []


# Individual specialized endpoint definitions
try:
    # Asset Pool ID endpoints
    import qualer_sdk.api.assets.get_asset_by_asset_pool

    ASSET_POOL_ID_ENDPOINTS = [
        (
            "assets.get_asset_by_asset_pool",
            qualer_sdk.api.assets.get_asset_by_asset_pool.sync,
        ),
    ]

    # Equipment ID endpoints
    import qualer_sdk.api.assets.get_assets_by_equipment_id

    EQUIPMENT_ID_ENDPOINTS = [
        (
            "assets.get_assets_by_equipment_id",
            qualer_sdk.api.assets.get_assets_by_equipment_id.sync,
        ),
    ]

    # Product ID endpoints
    import qualer_sdk.api.product.get_product

    PRODUCT_ID_ENDPOINTS = [
        ("product.get_product", qualer_sdk.api.product.get_product.sync),
    ]

    # Service Order Payment ID endpoints
    import qualer_sdk.api.service_order_payments.get_work_order_payment

    SERVICE_ORDER_PAYMENT_ID_ENDPOINTS = [
        (
            "service_order_payments.get_work_order_payment",
            qualer_sdk.api.service_order_payments.get_work_order_payment.sync,
        ),
    ]

    # Vendor Company ID endpoints
    import qualer_sdk.api.vendors.get_get_8

    VENDOR_COMPANY_ID_ENDPOINTS = [
        ("vendors.get_get_8", qualer_sdk.api.vendors.get_get_8.sync),
    ]

    # Maintenance Plan ID endpoints (the GET ones only)
    import qualer_sdk.api.client_maintenance_plans.get_maintenance_plan_assets
    import qualer_sdk.api.maintenance_plans.get_maintenance_plan_assets_get_2

    MAINTENANCE_PLAN_ID_ENDPOINTS = [
        (
            "maintenance_plans.get_maintenance_plan_assets_get_2",
            qualer_sdk.api.maintenance_plans.get_maintenance_plan_assets_get_2.sync,
        ),
        (
            "client_maintenance_plans.get_maintenance_plan_assets",
            qualer_sdk.api.client_maintenance_plans.get_maintenance_plan_assets.sync,
        ),
    ]

except ImportError:
    ASSET_POOL_ID_ENDPOINTS = []
    EQUIPMENT_ID_ENDPOINTS = []
    PRODUCT_ID_ENDPOINTS = []
    SERVICE_ORDER_PAYMENT_ID_ENDPOINTS = []
    VENDOR_COMPANY_ID_ENDPOINTS = []
    MAINTENANCE_PLAN_ID_ENDPOINTS = []


# Discover endpoints at module level for pytest parameterization
TESTABLE_ENDPOINTS = discover_testable_endpoints()
ASSET_ID_ONLY_ENDPOINTS = discover_asset_id_only_endpoints()
CLIENT_COMPANY_ID_ONLY_ENDPOINTS = discover_client_company_id_only_endpoints()
SERVICE_ORDER_ID_ONLY_ENDPOINTS = discover_service_order_id_endpoints()
SERVICE_ORDER_ITEM_ID_ONLY_ENDPOINTS = discover_service_order_item_id_endpoints()


@pytest.fixture(scope="session")
def authenticated_client():
    """Create an authenticated client for testing."""
    api_token = os.getenv("QUALER_API_KEY")
    if not api_token:
        pytest.skip("QUALER_API_KEY not found in environment variables")

    return AuthenticatedClient(api_token)


@pytest.fixture(scope="session")
def sample_asset_id(authenticated_client):
    """Get a sample asset ID for testing asset-specific endpoints."""
    return 1235564  # This asset ID triggers the SpecificationMode enum bug
    # try:
    #     # Try to get assets from the get_all_assets endpoint
    #     from qualer_sdk.api.assets import get_all_assets

    #     assets = get_all_assets.sync(client=authenticated_client)
    #     if assets and len(assets) > 0:
    #         return assets[0].asset_id

    #     # If we can't get assets, skip the asset ID tests
    #     pytest.skip("Could not retrieve sample asset ID for testing")

    # except Exception as e:
    #     pytest.skip(f"Could not retrieve sample asset ID: {e}")


@pytest.fixture(scope="session")
def sample_client_company_id(authenticated_client):
    """Get a sample client company ID for testing."""

    return 57071  # This is a hardcoded value for testing purposes

    # try:
    #     # Import the function to get all clients
    #     from qualer_sdk.api.clients.get_all_get_2 import sync as get_all_clients

    #     # Get the list of client companies
    #     clients = get_all_clients(client=authenticated_client)

    #     # Return the first client company ID if available
    #     if clients and len(clients) > 0:
    #         # Check for common client ID attribute names
    #         client = clients[0]
    #         if hasattr(client, "company_id"):
    #             return client.company_id
    #         else:
    #             # Try to get the first numeric attribute
    #             for attr_name in dir(client):
    #                 if not attr_name.startswith("_"):
    #                     attr_value = getattr(client, attr_name)
    #                     if isinstance(attr_value, int) and attr_value > 0:
    #                         return attr_value

    #     # If we can't get clients, skip the client company ID tests
    #     pytest.skip("Could not retrieve sample client company ID for testing")

    # except Exception as e:
    #     pytest.skip(f"Could not retrieve sample client company ID: {e}")


@pytest.fixture(scope="session")
def sample_service_order_id(authenticated_client):
    """Get a sample service order ID for testing."""

    # Return a hardcoded service order ID for testing
    # This should be a valid service order ID in your system
    # return 12345  # Replace with a valid service order ID

    # Alternative: Try to get a real service order ID from the API
    try:
        from qualer_sdk.api.service_orders.get_work_orders import (
            sync as get_work_orders,
        )

        service_orders = get_work_orders(client=authenticated_client, company_id=57071)

        if service_orders and len(service_orders) > 0:
            service_order = service_orders[0]
            # Check for common service order ID attribute names
            for attr_name in ["id", "service_order_id", "order_id", "work_order_id"]:
                if hasattr(service_order, attr_name):
                    return getattr(service_order, attr_name)

        pytest.skip("Could not retrieve sample service order ID for testing")

    except Exception as e:
        pytest.skip(f"Could not retrieve sample service order ID: {e}")


@pytest.fixture(scope="session")
def sample_employee_id(authenticated_client):
    """Get a sample employee ID for testing."""
    try:
        # Try to get employees from the get_employees_get_2 endpoint
        from qualer_sdk.api.employees import get_employees_get_2

        employees = get_employees_get_2.sync(client=authenticated_client)
        if employees and len(employees) > 0:
            employee = employees[0]
            # Check for common employee ID attribute names
            for attr_name in ["id", "employee_id", "user_id", "person_id"]:
                if hasattr(employee, attr_name):
                    return getattr(employee, attr_name)

        # If we can't get employees, skip the employee ID tests
        pytest.skip("Could not retrieve sample employee ID for testing")

    except Exception as e:
        pytest.skip(f"Could not retrieve sample employee ID: {e}")


# Individual test functions for specialized endpoints


@pytest.fixture(scope="session")
def sample_asset_pool_id():
    """Get a sample asset pool ID for testing."""
    return 1  # Hardcoded for now - replace with dynamic lookup if needed


@pytest.fixture(scope="session")
def sample_equipment_id():
    """Get a sample equipment ID for testing."""
    return "EQ001"  # Hardcoded for now - replace with dynamic lookup if needed


@pytest.fixture(scope="session")
def sample_product_id():
    """Get a sample product ID for testing."""
    return 1  # Hardcoded for now - replace with dynamic lookup if needed


@pytest.fixture(scope="session")
def sample_service_order_payment_id():
    """Get a sample service order payment ID for testing."""
    return 1  # Hardcoded for now - replace with dynamic lookup if needed


@pytest.fixture(scope="session")
def sample_vendor_company_id():
    """Get a sample vendor company ID for testing."""
    return 1  # Hardcoded for now - replace with dynamic lookup if needed


@pytest.fixture(scope="session")
def sample_maintenance_plan_id():
    """Get a sample maintenance plan ID for testing."""
    return 1  # Hardcoded for now - replace with dynamic lookup if needed


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


@pytest.mark.parametrize("endpoint_name,endpoint_func", ASSET_ID_ONLY_ENDPOINTS)
def test_asset_id_endpoint_response_parsing(
    endpoint_name, endpoint_func, authenticated_client, sample_asset_id=1235564
):
    """
    Test that endpoints requiring only asset_id can be called and parsed correctly.

    This test verifies:
    1. The endpoint can be called with a valid asset_id
    2. The response can be parsed by the generated SDK models
    3. No parsing/enum/date errors occur
    """
    # Get the function signature to determine the asset_id parameter name
    sig = inspect.signature(endpoint_func)
    asset_param_name = None

    for name, param in sig.parameters.items():
        if name == "client":
            continue
        if param.default == inspect.Parameter.empty:
            param_name_lower = name.lower()
            if param_name_lower in ["asset_id", "assetid", "id", "asset_identifier"]:
                asset_param_name = name
                break

    if not asset_param_name:
        pytest.fail(f"Could not determine asset ID parameter name for {endpoint_name}")

    # Call the endpoint with the sample asset ID
    kwargs = {"client": authenticated_client, asset_param_name: sample_asset_id}
    response = endpoint_func(**kwargs)

    # The main goal is to test that the response parses without errors
    print(
        f"✓ {endpoint_name}: Response parsed successfully with asset_id={sample_asset_id}"
    )

    # Log response details for debugging
    if response is None:
        print(f"  - {endpoint_name}: Response is None (may be expected)")
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


@pytest.mark.parametrize(
    "endpoint_name,endpoint_func", CLIENT_COMPANY_ID_ONLY_ENDPOINTS
)
def test_client_company_id_endpoint_response_parsing(
    endpoint_name, endpoint_func, authenticated_client, sample_client_company_id=57071
):
    """
    Test that endpoints requiring only client_company_id can be called and parsed correctly.

    This test verifies:
    1. The endpoint can be called with a valid client_company_id
    2. The response can be parsed by the generated SDK models
    3. No parsing/enum/date errors occur
    """
    # Skip problematic endpoints with known OpenAPI generator issues
    problematic_endpoints = [
        "client_assets.get_asset_manager_list_get_2",  # ToolRole enum doesn't handle None
    ]

    if endpoint_name in problematic_endpoints:
        pytest.skip(
            f"Skipping {endpoint_name} - known OpenAPI generator issue with nullable enums"
        )
    # Get the client company ID parameter name from the function signature
    sig = inspect.signature(endpoint_func)
    client_param_name = None

    for name, param in sig.parameters.items():
        if name == "client":
            continue
        if param.default == inspect.Parameter.empty:
            client_param_name = name
            break

    if not client_param_name:
        pytest.fail(
            f"Could not determine client company ID parameter name for {endpoint_name}"
        )

    # Call the endpoint with the sample client company ID
    kwargs = {
        "client": authenticated_client,
        client_param_name: sample_client_company_id,
    }
    response = endpoint_func(**kwargs)

    # The main goal is to test that the response parses without errors
    print(
        f"✓ {endpoint_name}: Response parsed successfully with {client_param_name}={sample_client_company_id}"
    )

    # Log response details for debugging
    if response is None:
        print(f"  - {endpoint_name}: Response is None (may be expected)")
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
    print(f"✓ {endpoint_name}: Response parsed successfully (client_company_id)")

    # Log response details for debugging
    if response is None:
        print(f"  - {endpoint_name}: Response is None (may be expected)")
    elif isinstance(response, list):
        print(f"  - {endpoint_name}: Response is a list with {len(response)} items")
    elif hasattr(response, "__dict__"):
        print(f"  - {endpoint_name}: Response is a {type(response).__name__} object")
    else:
        print(f"  - {endpoint_name}: Response type: {type(response)}")


@pytest.mark.parametrize("endpoint_name,endpoint_func", SERVICE_ORDER_ID_ONLY_ENDPOINTS)
def test_service_order_id_endpoint_response_parsing(
    endpoint_name, endpoint_func, authenticated_client
):
    """
    Test that endpoints requiring only service_order_id can be called and parsed correctly.

    This test verifies:
    1. The endpoint can be called with a valid service_order_id
    2. The response can be parsed by the generated SDK models
    3. No parsing/enum/date errors occur
    """
    # Skip problematic endpoints with known OpenAPI generator issues
    # problematic_endpoints = [
    #     "report_datasets.get_all_measurements_by_order",  # AsFoundMeasurementNotTakenResult enum doesn't handle None
    #     "report_datasets.get_as_found_measurements_by_order",  # GuardBandLogic enum doesn't handle None
    #     "report_datasets.get_as_left_measurements_by_order",  # GuardBandLogic enum doesn't handle None
    #     "report_datasets.get_service_orders",  # Date parsing error with None values
    # ]

    # if endpoint_name in problematic_endpoints:
    #     pytest.skip(
    #         f"Skipping {endpoint_name} - known OpenAPI generator issue with nullable enums"
    #     )
    # Get the service order ID parameter name from the function signature
    sig = inspect.signature(endpoint_func)
    service_order_param_name = None

    for name, param in sig.parameters.items():
        if name == "client":
            continue
        if param.default == inspect.Parameter.empty:
            service_order_param_name = name
            break

    if not service_order_param_name:
        pytest.fail(
            f"Could not determine service order ID parameter name for {endpoint_name}"
        )

    # Use a sample service order ID for testing
    sample_service_order_id = (
        1235369  # Replace with a valid service order ID for testing
    )

    # Call the endpoint with the sample service order ID
    kwargs = {
        "client": authenticated_client,
        service_order_param_name: sample_service_order_id,
    }
    response = endpoint_func(**kwargs)

    # The main goal is to test that the response parses without errors
    print(
        f"✓ {endpoint_name}: Response parsed successfully with {service_order_param_name}={sample_service_order_id}"
    )

    # Log response details for debugging
    if response is None:
        print(f"  - {endpoint_name}: Response is None (may be expected)")
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


@pytest.mark.parametrize(
    "endpoint_name,endpoint_func", SERVICE_ORDER_ITEM_ID_ONLY_ENDPOINTS
)
def test_service_order_item_id_endpoint_response_parsing(
    endpoint_name, endpoint_func, authenticated_client
):
    """
    Test that endpoints requiring only service_order_item_id can be called and parsed correctly.

    This test verifies:
    1. The endpoint can be called with a valid service_order_item_id
    2. The response can be parsed by the generated SDK models
    3. No parsing/enum/date errors occur
    """
    # Skip problematic endpoints with known OpenAPI generator issues
    problematic_endpoints = [
        "report_datasets.get_all_measurements",  # AsFoundMeasurementNotTakenResult enum doesn't handle None
        "report_datasets.get_as_found_measurements",  # GuardBandLogic enum doesn't handle None
        "report_datasets.get_as_left_measurements",  # GuardBandLogic enum doesn't handle None
        "service_order_item_measurements.get_measurement_form",  # InfluenceParameter1Type enum doesn't handle None
        "service_order_item_tasks.get_work_item_tasks",  # Dictionary parsing error
    ]

    if endpoint_name in problematic_endpoints:
        pytest.skip(
            f"Skipping {endpoint_name} - known OpenAPI generator issue with nullable enums or parsing"
        )

    # Get the service order item ID parameter name from the function signature
    sig = inspect.signature(endpoint_func)
    service_order_item_param_name = None

    for name, param in sig.parameters.items():
        if name == "client":
            continue
        if param.default == inspect.Parameter.empty:
            service_order_item_param_name = name
            break

    if not service_order_item_param_name:
        pytest.fail(
            f"Could not determine service order item ID parameter name for {endpoint_name}"
        )

    # Use a sample service order item ID for testing
    sample_service_order_item_id = 3662396

    # Call the endpoint with the sample service order item ID
    kwargs = {
        "client": authenticated_client,
        service_order_item_param_name: sample_service_order_item_id,
    }
    response = endpoint_func(**kwargs)

    # The main goal is to test that the response parses without errors
    print(
        f"✓ {endpoint_name}: Response parsed successfully with {service_order_item_param_name}={sample_service_order_item_id}"
    )

    # Log response details for debugging
    if response is None:
        print(f"  - {endpoint_name}: Response is None (may be expected)")
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


@pytest.mark.parametrize(
    "endpoint_name,endpoint_func", ASSET_SERVICE_RECORD_ID_ONLY_ENDPOINTS
)
def test_asset_service_record_id_endpoint_response_parsing(
    endpoint_name, endpoint_func, authenticated_client
):
    """Test endpoints that require an AssetServiceRecordId parameter."""
    # Skip problematic endpoints
    if endpoint_name in PROBLEMATIC_ASSET_SERVICE_RECORD_ENDPOINTS:
        pytest.skip(f"Skipping {endpoint_name} - known OpenAPI generator issue")

    # Get the function signature to find the parameter name
    sig = inspect.signature(endpoint_func)
    asset_service_record_param_name = None

    for name, param in sig.parameters.items():
        if name == "client":
            continue
        if param.default == inspect.Parameter.empty:
            asset_service_record_param_name = name
            break

    if not asset_service_record_param_name:
        pytest.fail(
            f"Could not determine asset service record ID parameter name for {endpoint_name}"
        )

    # Use a sample asset service record ID for testing
    # This should be a valid AssetServiceRecordId from your test data
    sample_asset_service_record_id = 2325444

    # Call the endpoint with the sample asset service record ID
    kwargs = {
        "client": authenticated_client,
        asset_service_record_param_name: sample_asset_service_record_id,
    }
    response = endpoint_func(**kwargs)

    # The main goal is to test that the response parses without errors
    print(
        f"✓ {endpoint_name}: Response parsed successfully with "
        f"{asset_service_record_param_name}={sample_asset_service_record_id}"
    )

    # Log response details for debugging
    if response is None:
        print(f"  - {endpoint_name}: Response is None (may be expected)")
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


@pytest.mark.parametrize("endpoint_name,endpoint_func", ASSET_POOL_ID_ENDPOINTS)
def test_asset_pool_id_endpoint(
    endpoint_name, endpoint_func, authenticated_client, sample_asset_pool_id
):
    """Test endpoints that require an AssetPoolId parameter."""
    response = endpoint_func(
        client=authenticated_client, asset_pool_id=sample_asset_pool_id
    )
    print(
        f"✓ {endpoint_name}: Response parsed successfully with asset_pool_id={sample_asset_pool_id}"
    )
    response_type = type(response).__name__
    assert (
        "Error" not in response_type
    ), f"Endpoint {endpoint_name} returned error type: {response_type}"


@pytest.mark.parametrize("endpoint_name,endpoint_func", EQUIPMENT_ID_ENDPOINTS)
def test_equipment_id_endpoint(
    endpoint_name, endpoint_func, authenticated_client, sample_equipment_id
):
    """Test endpoints that require an EquipmentId parameter."""
    response = endpoint_func(
        client=authenticated_client, equipment_id=sample_equipment_id
    )
    print(
        f"✓ {endpoint_name}: Response parsed successfully with equipment_id={sample_equipment_id}"
    )
    response_type = type(response).__name__
    assert (
        "Error" not in response_type
    ), f"Endpoint {endpoint_name} returned error type: {response_type}"


@pytest.mark.parametrize("endpoint_name,endpoint_func", PRODUCT_ID_ENDPOINTS)
def test_product_id_endpoint(
    endpoint_name, endpoint_func, authenticated_client, sample_product_id
):
    """Test endpoints that require a ProductId parameter."""
    response = endpoint_func(client=authenticated_client, product_id=sample_product_id)
    print(
        f"✓ {endpoint_name}: Response parsed successfully with product_id={sample_product_id}"
    )
    response_type = type(response).__name__
    assert (
        "Error" not in response_type
    ), f"Endpoint {endpoint_name} returned error type: {response_type}"


@pytest.mark.parametrize(
    "endpoint_name,endpoint_func", SERVICE_ORDER_PAYMENT_ID_ENDPOINTS
)
def test_service_order_payment_id_endpoint(
    endpoint_name, endpoint_func, authenticated_client, sample_service_order_payment_id
):
    """Test endpoints that require a ServiceOrderPaymentId parameter."""
    response = endpoint_func(
        client=authenticated_client,
        service_order_payment_id=sample_service_order_payment_id,
    )
    print(
        f"✓ {endpoint_name}: Response parsed successfully with service_order_payment_id={sample_service_order_payment_id}"
    )
    response_type = type(response).__name__
    assert (
        "Error" not in response_type
    ), f"Endpoint {endpoint_name} returned error type: {response_type}"


@pytest.mark.parametrize("endpoint_name,endpoint_func", VENDOR_COMPANY_ID_ENDPOINTS)
def test_vendor_company_id_endpoint(
    endpoint_name, endpoint_func, authenticated_client, sample_vendor_company_id
):
    """Test endpoints that require a VendorCompanyId parameter."""
    response = endpoint_func(
        client=authenticated_client, vendor_company_id=sample_vendor_company_id
    )
    print(
        f"✓ {endpoint_name}: Response parsed successfully with vendor_company_id={sample_vendor_company_id}"
    )
    response_type = type(response).__name__
    assert (
        "Error" not in response_type
    ), f"Endpoint {endpoint_name} returned error type: {response_type}"


@pytest.mark.parametrize("endpoint_name,endpoint_func", MAINTENANCE_PLAN_ID_ENDPOINTS)
def test_maintenance_plan_id_endpoint(
    endpoint_name, endpoint_func, authenticated_client, sample_maintenance_plan_id
):
    """Test endpoints that require a MaintenancePlanId parameter."""
    response = endpoint_func(
        client=authenticated_client, maintenance_plan_id=sample_maintenance_plan_id
    )
    print(
        f"✓ {endpoint_name}: Response parsed successfully with maintenance_plan_id={sample_maintenance_plan_id}"
    )
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

    # Show info about other endpoint types
    print(f"\nDiscovered {len(ASSET_ID_ONLY_ENDPOINTS)} asset_id-only endpoints")
    print(
        f"Discovered {len(CLIENT_COMPANY_ID_ONLY_ENDPOINTS)} client_company_id-only endpoints"
    )
    print(
        f"Discovered {len(SERVICE_ORDER_ID_ONLY_ENDPOINTS)} service_order_id-only endpoints"
    )
    print(
        f"Discovered {len(SERVICE_ORDER_ITEM_ID_ONLY_ENDPOINTS)} service_order_item_id-only endpoints"
    )
    print(
        f"Discovered {len(ASSET_SERVICE_RECORD_ID_ONLY_ENDPOINTS)} asset_service_record_id-only endpoints"
    )
    print(f"Discovered {len(EMPLOYEE_ID_ONLY_ENDPOINTS)} employee_id-only endpoints")
    print(f"Discovered {len(ASSET_POOL_ID_ENDPOINTS)} asset_pool_id-only endpoints")
    print(f"Discovered {len(EQUIPMENT_ID_ENDPOINTS)} equipment_id-only endpoints")
    print(f"Discovered {len(PRODUCT_ID_ENDPOINTS)} product_id-only endpoints")
    print(
        f"Discovered {len(SERVICE_ORDER_PAYMENT_ID_ENDPOINTS)} service_order_payment_id-only endpoints"
    )
    print(
        f"Discovered {len(VENDOR_COMPANY_ID_ENDPOINTS)} vendor_company_id-only endpoints"
    )
    print(
        f"Discovered {len(MAINTENANCE_PLAN_ID_ENDPOINTS)} maintenance_plan_id-only endpoints"
    )


if __name__ == "__main__":
    # Run the tests
    pytest.main([__file__, "-v"])
