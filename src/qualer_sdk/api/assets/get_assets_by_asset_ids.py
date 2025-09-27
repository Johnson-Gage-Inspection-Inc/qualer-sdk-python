"""Retrieve assets by IDs using the collected assets workflow.

This module provides convenience functions that:
- temporarily collect a set of asset IDs using the QuickCollection mechanism,
- fetch the collected assets via the asset manager list endpoint, and
- automatically clear the collection afterwards.
"""

from typing import List, Optional

from ...client import AuthenticatedClient
from ...context_managers import collected_assets, collected_assets_async
from ...models.filter_type import FilterType
from ...models.qualer_api_models_asset_to_asset_manage_response_model import (
    AssetToAssetManageResponseModel,
)
from . import get_asset_manager_list


def sync(
    client: AuthenticatedClient,
    asset_ids: List[int],
    *,
    search_string: Optional[str] = None,
    page: Optional[int] = None,
    page_size: Optional[int] = None,
) -> Optional[List[AssetToAssetManageResponseModel]]:
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
        List of collected AssetToAssetManageResponseModel objects
    """
    with collected_assets(client, asset_ids):
        return get_asset_manager_list.sync(
            client=client,
            model_filter_type=FilterType.COLLECTED_ASSETS,
            model_search_string=search_string,
            model_page=page,
            model_page_size=page_size,
        )


async def asyncio(
    client: AuthenticatedClient,
    asset_ids: List[int],
    *,
    search_string: Optional[str] = None,
    page: Optional[int] = None,
    page_size: Optional[int] = None,
) -> Optional[List[AssetToAssetManageResponseModel]]:
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
    async with collected_assets_async(client, asset_ids):
        return await get_asset_manager_list.asyncio(
            client=client,
            model_filter_type=FilterType.COLLECTED_ASSETS,
            model_search_string=search_string,
            model_page=page,
            model_page_size=page_size,
        )
