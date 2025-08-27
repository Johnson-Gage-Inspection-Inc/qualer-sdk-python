import datetime
import importlib
import os

import pytest

from qualer_sdk.client import AuthenticatedClient

ASSET_ID = 1235564  # valid asset ID for testing
ASSET_POOL_ID = 620646  # valid asset pool ID for testing
CLIENT_COMPANY_ID = 57613  # valid client company id
SERVICE_ORDER_ID = 1235369  # valid service order ID
SERVICE_ORDER_ITEM_ID = 3662396  # valid work item ID
ASSET_SERVICE_RECORD_ID = 2325444  # valid record ID
PDF_DOCUMENT_UUID = "c4ab6a7c-e2f1-4984-837f-9390f9a84dfc"  # known PDF
VENDOR_COMPANY_ID = 78095  # valid vendor id
EMPLOYEE_ID = 149992  # valid employee id
SITE_ID = 81690  # valid site id

# Mapping of endpoint to required params (from discovery log)
ENDPOINT_REQUIRED_PARAMS = {
    "asset_attributes.get_asset_attributes": {"asset_id": ASSET_ID},
    "asset_maintenance_plans.get_maintenance_plan": {
        "asset_id": ASSET_ID,
        "maintenance_plan_id": "MAINTENANCE_PLAN_ID",
    },
    "asset_maintenance_plans.get_maintenance_plans": {"asset_id": ASSET_ID},
    "asset_measurements.get_measurements_by_asset": {"asset_id": ASSET_ID},
    "asset_pools.get": {"id": ASSET_POOL_ID},
    "asset_pools.get_all": {},
    "asset_reservation.get_get_2": {},
    "asset_service_forecast.get_asset_forecast_list": {},
    "asset_service_forecast.get_client_asset_forecast_list": {
        "client_company_id": CLIENT_COMPANY_ID
    },
    "asset_service_records.document_list": {
        "asset_service_record_id_path": ASSET_SERVICE_RECORD_ID
    },
    "asset_service_records.download_document": {
        "asset_service_record_id_path": ASSET_SERVICE_RECORD_ID,
        "file_name_path": '"test.pdf"',
    },
    "asset_service_records.download_documents": {
        "asset_service_record_id": ASSET_SERVICE_RECORD_ID
    },
    "asset_service_records.get_asset_service_record": {
        "asset_service_record_id": ASSET_SERVICE_RECORD_ID
    },
    "asset_service_records.get_asset_service_records": {"model_asset_id": ASSET_ID},
    "asset_service_records.get_asset_service_records_by_asset": {"asset_id": ASSET_ID},
    # "assets.clear_collected_assets": {"body": '"BODY_PLACEHOLDER"'},
    # "assets.collect_assets": {"body": '"BODY_PLACEHOLDER"'},
    "assets.get_all_assets": {},
    "assets.get_asset": {"id": ASSET_ID},
    "assets.get_asset_by_asset_pool": {"asset_pool_id": "ASSET_POOL_ID"},
    "assets.get_asset_by_asset_tag": {"asset_tag": "ASSET_TAG"},
    "assets.get_asset_by_attribute": {},
    "assets.get_asset_by_barcode": {"barcode": ""},
    "assets.get_asset_by_serial_number": {"serial_number": "ASSET_SN"},
    "assets.get_asset_images": {"id": ""},
    "assets.get_asset_manager_counters": {},
    "assets.get_asset_manager_list": {},
    "assets.get_assets_by_equipment_id": {"equipment_id": "EQUIPMENT_ID"},
    "client_asset_attributes.get_asset_attributes_get_2": {"asset_id": ASSET_ID},
    "client_asset_service_records.get_asset_service_records_by_asset_get_2": {
        "asset_id": ASSET_ID
    },
    "client_assets.get_all_assets_get_2": {},
    "client_assets.get_asset_counters": {"client_company_id": CLIENT_COMPANY_ID},
    "client_assets.get_asset_get_2": {"asset_id_path": ASSET_ID},
    "client_assets.get_asset_manager_list_get_2": {
        "client_company_id": CLIENT_COMPANY_ID
    },
    "client_assets.get_assets": {"client_company_id": CLIENT_COMPANY_ID},
    "client_attribute.get_client_attributes": {"client_company_id": CLIENT_COMPANY_ID},
    "client_employees.get_employee": {"employee_id_path": EMPLOYEE_ID},
    "client_employees.get_employees": {"client_company_id": CLIENT_COMPANY_ID},
    "client_maintenance_plans.get_maintenance_plan_assets": {
        "maintenance_plan_id": "MAINTENANCE_PLAN_ID"
    },
    "client_maintenance_plans.get_maintenance_plans_get_2": {
        "client_company_id": CLIENT_COMPANY_ID
    },
    "client_site.get_client_sites": {"client_company_id": CLIENT_COMPANY_ID},
    "clients.get_all_get_2": {},
    "clients.get_get_3": {"client_company_id": CLIENT_COMPANY_ID},
    "common.culture_list": {},
    "common.culture_ui_list": {},
    # "common.get_company_settings": {"setting_key": ""},
    "company.departments": {},
    # "company.site_rooms": {"id": ""},
    "company.sites": {},
    "employee_filter_preference.get_employee_filter_preferences": {},
    "employee_preference.get_get_4": {"element_page": '"AssetManager"'},
    "employees.get_employee_get_2": {"employee_id": EMPLOYEE_ID},
    "employees.get_employees_get_2": {},
    "environments.get_get_5": {"id": ""},
    "maintenance_plans.get_maintenance_plan_assets_get_2": {
        "maintenance_plan_id": "MAINTENANCE_PLAN_ID"
    },
    "maintenance_plans.get_maintenance_plans_get_3": {},
    "product.get_inventory_count": {},
    "product.get_manufacturers": {},
    "product.get_product": {"product_id": "PRODUCT_ID"},
    "reference.get_measurement_quantities": {},
    "reference.get_units_of_measure": {},
    "report_datasets.get_all_measurements": {
        "service_order_item_id": SERVICE_ORDER_ITEM_ID
    },
    "report_datasets.get_all_measurements_by_order": {
        "service_order_id": SERVICE_ORDER_ID
    },
    "report_datasets.get_as_found_measurements": {
        "service_order_item_id": SERVICE_ORDER_ITEM_ID
    },
    "report_datasets.get_as_found_measurements_by_order": {
        "service_order_id": SERVICE_ORDER_ID
    },
    "report_datasets.get_as_left_measurements": {
        "service_order_item_id": SERVICE_ORDER_ITEM_ID
    },
    "report_datasets.get_as_left_measurements_by_order": {
        "service_order_id": SERVICE_ORDER_ID
    },
    "report_datasets.get_asset_attributes_get_3": {
        "service_order_item_id": SERVICE_ORDER_ITEM_ID
    },
    "report_datasets.get_asset_service_records_get_2": {
        "service_order_item_id": SERVICE_ORDER_ITEM_ID
    },
    "report_datasets.get_channel_results": {
        "service_order_item_id": SERVICE_ORDER_ITEM_ID
    },
    "report_datasets.get_channel_results_by_order": {
        "service_order_id": SERVICE_ORDER_ID
    },
    "report_datasets.get_channel_uniformity": {
        "service_order_item_id": SERVICE_ORDER_ITEM_ID
    },
    "report_datasets.get_client_attributes_get_2": {
        "service_order_id": SERVICE_ORDER_ID
    },
    "report_datasets.get_company_certifications": {},
    "report_datasets.get_external_data_reports": {
        "service_order_id": SERVICE_ORDER_ID,
        "service_order_item_ids": "[SERVICE_ORDER_ITEM_ID]",
    },
    "report_datasets.get_measurement_charts": {
        "service_order_item_id": SERVICE_ORDER_ITEM_ID
    },
    "report_datasets.get_measurement_fields": {
        "service_order_item_id": SERVICE_ORDER_ITEM_ID
    },
    "report_datasets.get_measurement_fields_by_order": {
        "service_order_id": SERVICE_ORDER_ID
    },
    "report_datasets.get_order_item_documents": {
        "service_order_item_id": SERVICE_ORDER_ITEM_ID
    },
    "report_datasets.get_order_item_images": {
        "service_order_item_id": SERVICE_ORDER_ITEM_ID
    },
    "report_datasets.get_reference_standards": {
        "service_order_item_id": SERVICE_ORDER_ITEM_ID
    },
    "report_datasets.get_reference_standards_by_order": {
        "service_order_id": SERVICE_ORDER_ID
    },
    "report_datasets.get_service_order_assignees": {
        "service_order_id": SERVICE_ORDER_ID
    },
    "report_datasets.get_service_order_charges": {"service_order_id": SERVICE_ORDER_ID},
    "report_datasets.get_service_order_item_components": {
        "service_order_item_id": SERVICE_ORDER_ITEM_ID
    },
    "report_datasets.get_service_order_item_components_by_order": {
        "service_order_id": SERVICE_ORDER_ID
    },
    "report_datasets.get_service_order_item_fields_by_order": {
        "service_order_id": SERVICE_ORDER_ID
    },
    "report_datasets.get_service_order_item_options": {
        "service_order_item_id": SERVICE_ORDER_ITEM_ID
    },
    "report_datasets.get_service_order_item_status_history_async": {
        "service_order_item_id": SERVICE_ORDER_ITEM_ID
    },
    "report_datasets.get_service_order_item_tasks_by_order": {
        "service_order_id": SERVICE_ORDER_ID
    },
    "report_datasets.get_service_order_item_tasks_by_order_items": {
        "service_order_item_id": SERVICE_ORDER_ITEM_ID
    },
    "report_datasets.get_service_order_items": {
        "service_order_item_id": SERVICE_ORDER_ITEM_ID
    },
    "report_datasets.get_service_order_items_by_order": {
        "service_order_id": SERVICE_ORDER_ID
    },
    "report_datasets.get_service_order_tasks": {"service_order_id": SERVICE_ORDER_ID},
    "report_datasets.get_service_orders": {"service_order_id": SERVICE_ORDER_ID},
    "report_datasets.get_tool_attributes": {
        "service_order_item_id": SERVICE_ORDER_ITEM_ID
    },
    "report_datasets.get_tool_range_attributes": {
        "service_order_item_id": SERVICE_ORDER_ITEM_ID
    },
    "service_order_documents.get_document": {
        "guid": PDF_DOCUMENT_UUID,
    },
    "service_order_documents.get_document_list": {
        "from_": datetime.datetime(2024, 1, 1),
        "to": datetime.datetime(2024, 12, 31),
    },
    "service_order_documents.get_documents": {"service_order_id": SERVICE_ORDER_ID},
    "service_order_documents.get_documents_list": {
        "service_order_id": SERVICE_ORDER_ID
    },
    "service_order_item_documents.get_document_list_get_2": {
        "from_": datetime.datetime(2024, 1, 1),
        "to": datetime.datetime(2024, 12, 31),
    },
    "service_order_item_documents.get_documents_get_2": {
        "service_order_item_id": SERVICE_ORDER_ITEM_ID
    },
    "service_order_item_documents.get_documents_list_get_2": {
        "service_order_item_id": SERVICE_ORDER_ITEM_ID
    },
    # "service_order_item_measurements.get_measurement_form": {
    #     "work_item_id": SERVICE_ORDER_ITEM_ID
    # },  # TODO: fix this endpoint
    "service_order_item_measurements.get_measurements_by_asset_get_2": {
        "asset_id": ASSET_ID
    },
    "service_order_item_parts.get_work_item_parts": {
        "work_item_id": SERVICE_ORDER_ITEM_ID
    },
    "service_order_item_tasks.get_work_item_task": {
        "task_id": "",
        "work_item_id": SERVICE_ORDER_ITEM_ID,
    },
    "service_order_item_tasks.get_work_item_tasks": {
        "work_item_id": SERVICE_ORDER_ITEM_ID
    },
    "service_order_items.get_work_item": {"work_item_id": SERVICE_ORDER_ITEM_ID},
    "service_order_items.get_work_item_charges": {
        "work_item_id": SERVICE_ORDER_ITEM_ID
    },
    "service_order_items.get_work_item_images": {"work_item_id": SERVICE_ORDER_ITEM_ID},
    "service_order_items.get_work_items": {"service_order_id": SERVICE_ORDER_ID},
    "service_order_items.get_work_items_workitems": {},
    "service_order_metadata.get_get_6": {"service_order_id": SERVICE_ORDER_ID},
    "service_order_parts.get_work_order_parts": {"service_order_id": SERVICE_ORDER_ID},
    "service_order_payments.get_all_work_order_payments": {
        "service_order_id": SERVICE_ORDER_ID
    },
    "service_order_payments.get_work_order_payment": {"service_order_payment_id": "1"},
    "service_order_tasks.get_work_order_tasks": {"service_order_id": SERVICE_ORDER_ID},
    "service_orders.get_assignments": {"service_order_id": SERVICE_ORDER_ID},
    "service_orders.get_charges": {"service_order_id": SERVICE_ORDER_ID},
    "service_orders.get_order_status": {"service_order_id": SERVICE_ORDER_ID},
    "service_orders.get_work_order": {"service_order_id": SERVICE_ORDER_ID},
    "service_orders.get_work_orders": {},
    "service_orders.get_work_orders_employee": {"employee_id": EMPLOYEE_ID},
    # "service_pricing.get_get_7": {"service_pricing_id": "1"},
    "vendors.get_all_get_3": {},
    "vendors.get_get_8": {"vendor_company_id": VENDOR_COMPANY_ID},
}


@pytest.mark.integration
@pytest.mark.parametrize(
    "endpoint_name",
    ENDPOINT_REQUIRED_PARAMS.keys(),
)
def test_the_other_get_endpoints(endpoint_name):
    """Test various GET endpoints in the Qualer API."""
    params = ENDPOINT_REQUIRED_PARAMS.get(endpoint_name, {})
    # Remove params with value '' (user must fill these in for a real test)
    missing = [k for k, v in params.items() if v == ""]
    if missing:
        pytest.skip(f"Missing required test values for: {missing}")

    # Import the sync function for the endpoint
    try:
        module_path, func_name = endpoint_name.split(".")
        api_module = importlib.import_module(
            f"qualer_sdk.api.{module_path}.{func_name}"
        )
        sync_func = getattr(api_module, "sync", None) or getattr(
            api_module, "sync_detailed"
        )
    except Exception as e:
        pytest.skip(f"Could not import endpoint {endpoint_name}: {e}")

    # Get API token from environment
    api_token = os.getenv("QUALER_API_KEY")
    if not api_token:
        pytest.skip("QUALER_API_KEY not set in environment")
    client = AuthenticatedClient(api_token)

    # Prepare call arguments
    call_args = dict(params)
    call_args["client"] = client

    # Call the endpoint and assert no exception
    try:
        sync_func(**call_args)
    except Exception as e:
        pytest.fail(f"Endpoint {endpoint_name} raised exception: {e}")
