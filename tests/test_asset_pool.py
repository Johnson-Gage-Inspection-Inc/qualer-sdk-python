#!/usr/bin/env python3
"""
Test script to get assets from asset pool 620646 using the Qualer SDK.
"""

import os
import sys
import traceback
from pathlib import Path

# Add the src directory to the Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

# Load environment variables
from dotenv import load_dotenv

load_dotenv()

from typing import List

from qualer_sdk.api.assets.get_asset_by_asset_pool import sync as get_assets_by_pool
from qualer_sdk.client import AuthenticatedClient
from qualer_sdk.models import QualerApiModelsAssetToAssetResponseModel


def main():
    print(
        "If there are errors, update spec.json and regenerate the SDK and re-test using:"
    )
    print("python regenerate_sdk.py && test_asset_pool.py")
    # Get API token from environment
    api_token = os.getenv("QUALER_API_KEY")
    if not api_token:
        print("❌ QUALER_API_KEY not found in environment variables")
        return 1

    # Create authenticated client
    base_url = "https://jgiquality.qualer.com"
    client = AuthenticatedClient(base_url=base_url, token=api_token)

    print(f"🔧 Connecting to Qualer API at {base_url}")
    print(
        f"🔑 Using API token: {api_token[:8]}..."
    )  # Test getting assets from asset pool 620646
    asset_pool_id = 620646
    print(f"📦 Getting assets from asset pool {asset_pool_id}...")

    try:
        # Use detailed response to get more error information
        assets: List[QualerApiModelsAssetToAssetResponseModel] = get_assets_by_pool(
            asset_pool_id=asset_pool_id, client=client
        )

        # Try to access parsed response with more debugging
        print("🔍 Attempting to parse response...")
        try:
            print(f"🔍 Parsed response type: {type(assets)}")
            print(f"🔍 Parsed response value: {assets}")
        except Exception as parse_error:
            traceback.print_exc()
            print(f"❌ Error parsing response: {parse_error}")
            return 1

        if assets is None:
            print("❌ No assets returned (parsed response is None)")
            return 1

        if not isinstance(assets, list):
            print(f"❌ Unexpected response type: {type(assets)}")
            print(f"📄 Raw response: {assets}")
            return 1

        print(
            f"✅ Successfully retrieved {len(assets)} assets from asset pool {asset_pool_id}"
        )  # Display asset details with date fields
        for i, asset in enumerate(assets[:5]):  # Show first 5 assets
            print(f"\n📋 Asset {i+1}:")
            print(f"   ID: {asset.asset_id}")
            print(f"   Name: {asset.asset_name}")
            print(f"   Serial Number: {asset.serial_number}")
            print(f"   Asset Tag: {asset.asset_tag}")
            print(f"   Status: {asset.asset_status}")
            print(f"   Location: {asset.location}")

            # Test the nullable date fields that were causing issues
            print(f"   Purchase Date: {asset.purchase_date}")
            print(f"   Activation Date: {asset.activation_date}")
            print(f"   Retirement Date: {asset.retirement_date}")

            # Test asset user and equipment ID
            print(f"   Asset User: {asset.asset_user}")
            print(f"   Equipment ID: {asset.equipment_id}")

        if len(assets) > 5:
            print(f"\n... and {len(assets) - 5} more assets")

    except Exception as e:
        traceback.print_exc()
        print(f"❌ Error getting assets from asset pool {asset_pool_id}: {e}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
