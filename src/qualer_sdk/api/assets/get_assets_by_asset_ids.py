"""Retrieve assets by IDs using the collected assets workflow.

This module provides convenience functions that:
- temporarily collect a set of asset IDs using the QuickCollection mechanism,
- fetch the collected assets via the asset manager list endpoint, and
- automatically clear the collection afterwards.
"""

from typing import List, Optional

from ...client import AuthenticatedClient
from ...models.qualer_api_models_asset_to_client_asset_manager_response_model import (
    AssetToClientAssetManagerResponseModel,
)
from ...quick_collection import AsyncQuickCollection, QuickCollection


def sync(
    client: AuthenticatedClient,
    asset_ids: List[int],
    *,
    search_string: Optional[str] = None,
    page: Optional[int] = None,
    page_size: Optional[int] = None,
) -> Optional[List[AssetToClientAssetManagerResponseModel]]:
    """Get assets by their IDs using the collected assets workflow.

    This is a convenience function that uses the collected_assets context manager
    to collect, retrieve, and clear assets in one call.

    Args:
        client: The authenticated client to use for API calls
        asset_ids: List of asset IDs to collect
        search_string: Optional search string to filter the collected assets
        page: Optional page number for pagination
        page_size: Optional page size for pagination

    Returns:
        List of collected AssetToClientAssetManagerResponseModel objects
    """
    with QuickCollection(client, asset_ids) as collection:
        return collection.get_details(
            search_string=search_string,
            page=page,
            page_size=page_size,
        )


async def asyncio(
    client: AuthenticatedClient,
    asset_ids: List[int],
    *,
    search_string: Optional[str] = None,
    page: Optional[int] = None,
    page_size: Optional[int] = None,
) -> Optional[List[AssetToClientAssetManagerResponseModel]]:
    """Async version of get_assets_by_asset_ids.

    Args:
        client: The authenticated client to use for API calls
        asset_ids: List of asset IDs to collect
        search_string: Optional search string to filter the collected assets
        page: Optional page number for pagination
        page_size: Optional page size for pagination

    Returns:
        List of collected AssetToAssetManageResponseModel objects
    """
    async with AsyncQuickCollection(client, asset_ids) as collection:
        return await collection.get_details(
            search_string=search_string,
            page=page,
            page_size=page_size,
        )
