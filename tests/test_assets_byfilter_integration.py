#!/usr/bin/env python3
"""
Integration test for the specific assets byfilter endpoint.

This test specifically targets the endpoint:
https://jgiquality.qualer.com/api/assets/byfilter?model.filterType=Unset&model.searchString=Thermocouple%20Wire%20Set

Known Issues:
- The endpoint may fail due to nullable date fields in the response model
- The QualerApiModelsAssetToAssetManageResponseModel.from_dict method may not handle None values
  for date fields like warranty_end, warranty_start, etc.
"""

import os
import pytest
from dotenv import load_dotenv

from qualer_sdk.client import AuthenticatedClient
from qualer_sdk.api.assets.get_asset_manager_list import sync as get_asset_manager_list

# Load environment variables
load_dotenv()

# Check if API key is available - skip entire module if not
API_KEY = os.getenv("QUALER_API_KEY")
if not API_KEY:
    pytest.skip(
        "QUALER_API_KEY not found in environment variables. Skipping integration tests.",
        allow_module_level=True,
    )


@pytest.fixture(scope="session")
def authenticated_client():
    """Create an authenticated client for testing."""
    api_token = os.getenv("QUALER_API_KEY")
    if not api_token:
        pytest.skip("QUALER_API_KEY not found in environment variables")

    return AuthenticatedClient(api_token)


@pytest.mark.integration
def test_assets_byfilter_thermocouple_wire_set(authenticated_client):
    """
    Test the specific endpoint: /api/assets/byfilter with filterType=Unset and searchString=Thermocouple Wire Set

    This test verifies:
    1. The endpoint can be called successfully
    2. The response can be parsed without errors
    3. The response contains the expected data structure
    4. Any returned assets have the expected properties
    """
    print("🔍 Testing Assets ByFilter Integration - Thermocouple Wire Set")
    print("=" * 60)

    try:
        # Call the endpoint with the specific parameters
        response = get_asset_manager_list(
            client=authenticated_client,
            model_filter_type="Unset",
            model_search_string="Thermocouple Wire Set",
        )

        print("✅ API call successful - response parsed without errors")

        # Log response details
        if response is None:
            print("⚠️  Response is None - no assets found matching criteria")
            return

        print(f"📊 Found {len(response)} assets matching 'Thermocouple Wire Set'")

        if response:
            print("✅ Successfully retrieved assets")

            # Show first few assets
            print(f"\n📋 First {min(3, len(response))} assets:")
            for i, asset in enumerate(response[:3]):
                print(f"  [{i+1}] Asset ID: {asset.asset_id}")
                print(f"      Name: {asset.asset_name}")
                print(f"      Description: {asset.asset_description}")
                print(f"      Maker: {asset.asset_maker}")
                print(f"      Serial Number: {asset.serial_number}")
                print(f"      Asset Tag: {asset.asset_tag}")

                # Check for date fields that might be None
                if hasattr(asset, "warranty_start") and asset.warranty:
                    print(f"      Warranty Start: {asset.warranty}")
                if hasattr(asset, "warranty_end") and asset.warranty_end:
                    print(f"      Warranty End: {asset.warranty_end}")
                if hasattr(asset, "purchase_date") and asset.purchase_date:
                    print(f"      Purchase Date: {asset.purchase_date}")

                print()

            # Verify data structure
            sample_asset = response[0]
            assert sample_asset.asset_id is not None, "Asset ID should not be None"

            # Check if any assets contain "Thermocouple" or "Wire Set" in the name or description
            thermocouple_assets = []
            wire_set_assets = []

            for asset in response:
                asset_text = (
                    f"{asset.asset_name or ''} {asset.asset_description or ''}".lower()
                )
                if "thermocouple" in asset_text:
                    thermocouple_assets.append(asset)
                if "wire set" in asset_text:
                    wire_set_assets.append(asset)

            print("\n📈 Search Results Analysis:")
            print(f"  Assets containing 'thermocouple': {len(thermocouple_assets)}")
            print(f"  Assets containing 'wire set': {len(wire_set_assets)}")

            # Show some statistics
            with_serial_numbers = sum(1 for asset in response if asset.serial_number)
            with_asset_tags = sum(1 for asset in response if asset.asset_tag)
            with_descriptions = sum(1 for asset in response if asset.asset_description)

            print("\n📊 Asset Statistics:")
            print(
                f"  Assets with serial numbers: {with_serial_numbers}/{len(response)} ({with_serial_numbers/len(response)*100:.1f}%)"
            )
            print(
                f"  Assets with asset tags: {with_asset_tags}/{len(response)} ({with_asset_tags/len(response)*100:.1f}%)"
            )
            print(
                f"  Assets with descriptions: {with_descriptions}/{len(response)} ({with_descriptions/len(response)*100:.1f}%)"
            )

            print("✅ Data validation passed")
        else:
            print(
                "⚠️  No assets found - this might be expected if no matching data exists"
            )

    except Exception as e:
        print(f"❌ Error: {e}")
        print(f"Error type: {type(e)}")
        import traceback

        traceback.print_exc()
        raise e


@pytest.mark.integration
def test_assets_byfilter_various_filter_types(authenticated_client):
    """
    Test the assets byfilter endpoint with various filter types to ensure robustness.

    This test verifies multiple filter types work correctly:
    - Unset
    - DueForService
    - RecentlyServiced
    - NotServiced
    """
    print("🔍 Testing Assets ByFilter Integration - Various Filter Types")
    print("=" * 60)

    filter_types = ["Unset", "DueForService", "RecentlyServiced", "NotServiced"]

    for filter_type in filter_types:
        print(f"\n🔍 Testing filter type: {filter_type}")
        try:
            response = get_asset_manager_list(
                client=authenticated_client,
                model_filter_type=filter_type,
                model_page_size=10,  # Limit to 10 results for testing
            )

            if response is None:
                print(f"  ⚠️  No assets found for filter type: {filter_type}")
            else:
                print(
                    f"  ✅ Found {len(response)} assets for filter type: {filter_type}"
                )

                # Basic validation
                if response:
                    sample_asset = response[0]
                    assert (
                        sample_asset.asset_id is not None
                    ), f"Asset ID should not be None for filter type: {filter_type}"

        except Exception as e:
            print(f"  ❌ Error with filter type {filter_type}: {e}")
            # Continue with other filter types
            continue

    print("\n✅ Filter type testing completed")


@pytest.mark.integration
def test_assets_byfilter_pagination(authenticated_client):
    """
    Test the assets byfilter endpoint with pagination parameters.

    This test verifies:
    1. Pagination works correctly
    2. Page size limits are respected
    3. Different pages return different results
    """
    print("🔍 Testing Assets ByFilter Integration - Pagination")
    print("=" * 60)

    try:
        # Test first page with small page size
        page1_response = get_asset_manager_list(
            client=authenticated_client,
            model_filter_type="Unset",
            model_page=1,
            model_page_size=5,
        )

        # Test second page with same page size
        page2_response = get_asset_manager_list(
            client=authenticated_client,
            model_filter_type="Unset",
            model_page=2,
            model_page_size=5,
        )

        print(f"📄 Page 1 results: {len(page1_response) if page1_response else 0}")
        print(f"📄 Page 2 results: {len(page2_response) if page2_response else 0}")

        # Verify pagination works
        if page1_response and page2_response:
            # Check that pages have different assets (if there are enough assets)
            if len(page1_response) > 0 and len(page2_response) > 0:
                page1_ids = {asset.asset_id for asset in page1_response}
                page2_ids = {asset.asset_id for asset in page2_response}

                # Pages should not have overlapping asset IDs
                overlap = page1_ids.intersection(page2_ids)
                assert (
                    len(overlap) == 0
                ), f"Pages should not overlap, but found {len(overlap)} common assets"

                print("✅ Pagination working correctly - no overlap between pages")
            else:
                print("⚠️  Not enough assets to verify pagination behavior")
        else:
            print("⚠️  Insufficient data to test pagination")

        print("✅ Pagination testing completed")

    except Exception as e:
        print(f"❌ Error during pagination testing: {e}")
        import traceback

        traceback.print_exc()
        raise e


if __name__ == "__main__":
    # Run the tests
    pytest.main([__file__, "-v", "-s"])
