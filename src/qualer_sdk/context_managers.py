"""Context managers for Qualer SDK operations."""

from contextlib import asynccontextmanager, contextmanager
from typing import AsyncIterator, Iterator, List

from .api.assets import clear_collected_assets, collect_assets
from .client import AuthenticatedClient


@contextmanager
def collected_assets(
    client: AuthenticatedClient,
    asset_ids: List[int],
) -> Iterator[None]:
    """Context manager for working with collected assets.

    This context manager simplifies the workflow of:
    1. Collecting assets by their IDs
    2. Retrieving the collected assets
    3. Automatically clearing the collection on exit

    Args:
        client: The authenticated client to use for API calls
        asset_ids: List of asset IDs to collect

    Yields:
        List of collected AssetToAssetManageResponseModel objects

    Example:
        ```python
        with collected_assets(client, [123, 456, 789]) as assets:
            assets = get_asset_manager_list.sync(
                client=client,
                model_filter_type=FilterType.COLLECTED_ASSETS,
                model_search_string=search_string,
                model_page=page,
                model_page_size=page_size,
            )
        # Assets are automatically cleared when exiting the context
        ```

    Raises:
        Any exceptions raised by the underlying API calls will propagate.
        The cleanup (clear_collected_assets) will still be attempted even if
        an exception occurs during the context block execution.
    """
    try:
        # Step 1: Collect the assets
        collect_assets.sync(client=client, body=asset_ids)

        # Yield. (No reason to actually return anything though)
        yield None

    finally:
        try:
            clear_collected_assets.sync(client=client, body=[])
        except Exception:
            # Don't let cleanup errors mask the original exception
            # You might want to log this in a real application
            pass


@asynccontextmanager
async def collected_assets_async(
    client: AuthenticatedClient,
    asset_ids: List[int],
) -> AsyncIterator[None]:
    """Async context manager for working with collected assets.

    This is the async version of the collected_assets context manager.
    All the same functionality as the sync version, but uses async/await.

    Args:
        client: The authenticated client to use for API calls
        asset_ids: List of asset IDs to collect

    Yields:
        None

    Example:
        ```python
        from qualer_sdk.models.filter_type import FilterType
        async with collected_assets_async(client, [123, 456, 789]):
            # Now get the assets that were just collected
            assets = await get_asset_manager_list.asyncio(
                client=client,
                model_filter_type=FilterType.COLLECTED_ASSETS,
            )
            for asset in assets:
                print(f"Asset: {asset.asset_name} (ID: {asset.asset_id})")
        # Assets are automatically cleared when exiting the context
        ```

    Raises:
        Any exceptions raised by the underlying API calls will propagate.
        The cleanup (clear_collected_assets) will still be attempted even if
        an exception occurs during the context block execution.
    """
    try:
        # Step 1: Collect the assets
        await collect_assets.asyncio(client=client, body=asset_ids)

        # Yield. (No reason to actually return anything though)
        yield None

    finally:
        try:
            await clear_collected_assets.asyncio(client=client, body=[])
        except Exception:
            # Don't let cleanup errors mask the original exception
            # You might want to log this in a real application
            pass


# Convenience function to clear all collected assets
def clear_all_collected_assets(client: AuthenticatedClient) -> None:
    """Clear all collected assets.

    This is a convenience function that calls clear_collected_assets with an empty list,
    which clears all assets from the QuickCollection according to the API documentation.

    Args:
        client: The authenticated client to use for API calls
    """
    clear_collected_assets.sync(client=client, body=[])


async def clear_all_collected_assets_async(client: AuthenticatedClient) -> None:
    """Async version of clear_all_collected_assets.

    Args:
        client: The authenticated client to use for API calls
    """
    await clear_collected_assets.asyncio(client=client, body=[])
