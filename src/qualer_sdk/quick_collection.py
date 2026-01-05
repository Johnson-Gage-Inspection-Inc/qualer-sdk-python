"""Context-managed set of asset IDs that mirrors Qualer QuickCollection.

Usage:
    with QuickCollection(client, [1, 2, 3]) as coll:
        coll.add(4)
        coll.discard(2)
        # Within this block, the server QuickCollection stays in sync.
    # On exit, the server collection is cleared.
"""

from __future__ import annotations

import logging
from typing import Iterable, cast

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

from .api.assets import clear_collected_assets, collect_assets, get_asset_manager_list
from .api.client_assets import get_asset_manager_list_get_2
from .client import AuthenticatedClient
from .models import (
    AssetFilterType,
    AssetToClientAssetManagerResponseModel,
    FilterType,
)

logger = logging.getLogger(__name__)


class QuickCollection(set[int]):
    """A set-like context manager that keeps server QuickCollection in sync.

    Notes:
        - Only specific mutating operations are supported and synchronized:
          add, update, remove, discard, pop (no args), clear.
        - Bulk algebraic updates like intersection_update, difference_update,
          and symmetric_difference_update are intentionally not implemented to
          avoid server/client divergence.

    Example:
        ```python
        with QuickCollection(client, [1235770, 1235660, 1235502]) as coll:
            assets = coll.get_details(search_string=search_string)
            for asset in assets:
                print(f"Asset {asset.asset_id}: {asset.category_name}")
        # Collection is automatically cleared when exiting the context.
        ```
    """

    client: AuthenticatedClient

    def __init__(
        self,
        client: AuthenticatedClient,
        asset_ids: Iterable[int] | None = None,
        *,
        start_clean: bool = True,
    ) -> None:
        super().__init__()
        self.client = client
        if start_clean:
            # Clear server-side collection without syncing through self.clear()
            try:
                clear_collected_assets.sync(client=self.client, body=[])
            except Exception as e:
                logger.warning("Failed to clear server collection during init: %r", e)
        if asset_ids:
            ids = list(asset_ids)
            if ids:
                collect_assets.sync(client=self.client, body=ids)
                super().update(ids)

    # --- Context manager protocol ---
    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc, tb) -> None:  # type: ignore[override]
        try:
            clear_collected_assets.sync(client=self.client, body=[])
        except Exception as cleanup_err:
            logger.error("Failed to clear server collection during cleanup: %r", cleanup_err)
            # If a primary exception exists, attach cleanup failure as a note; otherwise re-raise.
            if exc is not None and hasattr(exc, "add_note"):
                try:
                    exc.add_note(f"Cleanup failed: {cleanup_err!r}")
                except Exception:
                    # If add_note fails for any reason, prefer not to mask the original.
                    pass
            else:
                raise

    # --- Mutating operations (synchronized with server) ---
    def add(self, asset_id: int) -> None:  # type: ignore[override]
        """Add a single asset ID to the collection (server first)."""
        collect_assets.sync(client=self.client, body=[asset_id])
        super().add(asset_id)

    def update(self, *iterables: Iterable[int]) -> None:  # type: ignore[override]
        """Add multiple asset IDs to the collection (server first)."""
        ids: set[int] = set()
        for it in iterables:
            ids.update(it)
        if not ids:
            return
        collect_assets.sync(client=self.client, body=list(ids))
        super().update(ids)

    def remove(self, asset_id: int) -> None:  # type: ignore[override]
        """Remove an asset ID (server first). Raises KeyError if absent."""
        if asset_id not in self:
            raise KeyError(asset_id)
        clear_collected_assets.sync(client=self.client, body=[asset_id])
        super().remove(asset_id)

    def discard(self, asset_id: int) -> None:  # type: ignore[override]
        """Remove an asset ID if present (server first, but only if local contains it)."""
        if asset_id in self:
            clear_collected_assets.sync(client=self.client, body=[asset_id])
            super().discard(asset_id)

    def pop(self) -> int:  # type: ignore[override]
        """Remove and return an arbitrary element (server first)."""
        try:
            asset_id = next(iter(self))
        except StopIteration as e:
            raise KeyError("pop from an empty set") from e
        clear_collected_assets.sync(client=self.client, body=[asset_id])
        super().remove(asset_id)
        return asset_id

    def clear(self) -> None:  # type: ignore[override]
        clear_collected_assets.sync(client=self.client, body=[])
        super().clear()

    def copy(self) -> set[int]:  # type: ignore[override]
        """
        Return a shallow copy of the collection as a standard set.

        Note:
            The returned set is not synchronized with the server; modifications to it
            will not affect the underlying server-side collection.
        """
        import warnings

        warnings.warn(
            (
                "Copies are made to a standard set. The returned set will not be linked "
                "to the underlying collection. Modifications to the returned set will "
                "not affect the underlying collection on the server."
            ),
            stacklevel=2,
        )
        return super().copy()

    # --- Block unsupported bulk-update patterns that could desync server ---
    def intersection_update(self, *s: Iterable[int]) -> None:  # type: ignore[override]
        raise NotImplementedError(
            "intersection_update is not supported; use remove/discard to shrink the set."
        )

    def difference_update(self, *s: Iterable[int]) -> None:  # type: ignore[override]
        raise NotImplementedError(
            "difference_update is not supported; use remove/discard to shrink the set."
        )

    def symmetric_difference_update(self, s: Iterable[int]) -> None:  # type: ignore[override]
        raise NotImplementedError(
            "symmetric_difference_update is not supported; use add/update/remove/discard."
        )

    # Convenience function
    def get_details(
        self,
        *,
        client_company_id: int | None = None,
        search_string: str | None = None,
        page: int | None = None,
        page_size: int | None = None,
    ) -> list[AssetToClientAssetManagerResponseModel]:
        """Retrieve asset details for the collected assets.

        Returns the richer AssetToClientAssetManagerResponseModel which works for both
        standard and client-specific asset queries. Client-specific fields (asset_collection_id,
        in_service, in_last_service, service_tag, service_site_name, service_site_id,
        standard_title, schedules) will be None when querying standard assets via the
        standard endpoint.

        **Note:** The return type was changed from AssetToAssetManageResponseModel to
        AssetToClientAssetManagerResponseModel in order to support both standard and
        client assets through a single unified interface. AssetToClientAssetManagerResponseModel
        is a strict superset of AssetToAssetManageResponseModel (all common fields are
        identical, with 8 additional optional fields). The cast is safe because the API
        response data structure is compatible with the richer model type.
        """
        if not client_company_id:
            # Cast standard assets to client model (superset type). Safe because:
            # 1. AssetToClientAssetManagerResponseModel has all fields from AssetToAssetManageResponseModel
            # 2. Additional client-specific fields are optional and will be None
            # 3. Both models parse the same base asset JSON structure
            result = get_asset_manager_list.sync(
                client=self.client,
                model_filter_type=FilterType.COLLECTED_ASSETS,
                model_search_string=search_string,
                model_page=page,
                model_page_size=page_size,
            )
            return cast(list[AssetToClientAssetManagerResponseModel], result or [])
        else:
            return (
                get_asset_manager_list_get_2.sync(
                    client_company_id=client_company_id,
                    client=self.client,
                    query_filter_type=AssetFilterType.CLIENT_ASSETS_COLLECTED,
                    query_search_string=search_string,
                    query_page=page,
                    query_page_size=page_size,
                )
                or []
            )


class AsyncQuickCollection:
    """Async context-managed set that mirrors Qualer QuickCollection.

    This class provides an async API for keeping the server QuickCollection in sync
    with a local set of asset IDs. It does not subclass ``set`` to avoid overriding
    synchronous methods with async ones; instead it exposes a set-like surface via
    iteration, membership, and length, along with async mutators.

    Usage:
    ```python
    async with AsyncQuickCollection(client, [1, 2, 3]) as coll:
        await coll.add(4)
        await coll.discard(2)
        assets = await coll.get_details()
    ```
    """

    client: AuthenticatedClient

    def __init__(
        self,
        client: AuthenticatedClient,
        asset_ids: Iterable[int] | None = None,
        *,
        start_clean: bool = True,
    ) -> None:
        self.client = client
        self._ids: set[int] = set()
        self._initial_ids: set[int] = set(asset_ids or [])
        self._start_clean = start_clean

    # --- Async context manager protocol ---
    async def __aenter__(self) -> AsyncQuickCollection:
        if self._start_clean:
            await clear_collected_assets.asyncio(client=self.client, body=[])
            self._ids.clear()
        if self._initial_ids:
            await collect_assets.asyncio(client=self.client, body=list(self._initial_ids))
            self._ids.update(self._initial_ids)
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:  # type: ignore[override]
        try:
            await clear_collected_assets.asyncio(client=self.client, body=[])
        except Exception as cleanup_err:
            logger.error("Failed to clear server collection during cleanup: %r", cleanup_err)
            if exc is not None and hasattr(exc, "add_note"):
                try:
                    exc.add_note(f"Cleanup failed: {cleanup_err!r}")
                except Exception as add_note_err:
                    # Failed to add note to exception during cleanup; log the error.
                    logger.warning(
                        "Failed to add cleanup failure note in AsyncQuickCollection.__aexit__: %r. "
                        "Original cleanup error: %r",
                        add_note_err,
                        cleanup_err,
                    )
            else:
                raise

    # --- Read-only set-like surface ---
    def __iter__(self):
        return iter(self._ids)

    def __contains__(self, item: object) -> bool:
        """Return True if item is in the local set of asset IDs."""
        return item in self._ids

    def __len__(self) -> int:
        """Return the number of asset IDs in the local collection."""
        return len(self._ids)

    def copy(self) -> set[int]:
        """Return a shallow copy of the local IDs as a standard set."""
        import warnings

        warnings.warn(
            (
                "Copies are made to a standard set. The returned set will not be linked "
                "to the underlying collection. Modifications to the returned set will "
                "not affect the underlying collection on the server."
            ),
            stacklevel=2,
        )
        return set(self._ids)

    # --- Async mutating operations (server first) ---
    async def add(self, asset_id: int) -> None:
        await collect_assets.asyncio(client=self.client, body=[asset_id])
        self._ids.add(asset_id)

    async def update(self, *iterables: Iterable[int]) -> None:
        ids: set[int] = set()
        for it in iterables:
            ids.update(it)
        if not ids:
            return
        await collect_assets.asyncio(client=self.client, body=list(ids))
        self._ids.update(ids)

    async def remove(self, asset_id: int) -> None:
        if asset_id not in self._ids:
            raise KeyError(asset_id)
        await clear_collected_assets.asyncio(client=self.client, body=[asset_id])
        self._ids.remove(asset_id)

    async def discard(self, asset_id: int) -> None:
        if asset_id in self._ids:
            await clear_collected_assets.asyncio(client=self.client, body=[asset_id])
            self._ids.discard(asset_id)

    async def pop(self) -> int:
        try:
            asset_id = next(iter(self._ids))
        except StopIteration as e:
            raise KeyError("pop from an empty set") from e
        await clear_collected_assets.asyncio(client=self.client, body=[asset_id])
        self._ids.remove(asset_id)
        return asset_id

    async def clear(self) -> None:
        await clear_collected_assets.asyncio(client=self.client, body=[])
        self._ids.clear()

    async def get_details(
        self,
        *,
        client_company_id: int | None = None,
        search_string: str | None = None,
        page: int | None = None,
        page_size: int | None = None,
    ) -> list[AssetToClientAssetManagerResponseModel]:
        """Retrieve asset details for the collected assets (async version).

        Returns the richer AssetToClientAssetManagerResponseModel which works for both
        standard and client-specific asset queries. Client-specific fields (asset_collection_id,
        in_service, in_last_service, service_tag, service_site_name, service_site_id,
        standard_title, schedules) will be None when querying standard assets via the
        standard endpoint.

        **Note:** The return type was changed from AssetToAssetManageResponseModel to
        AssetToClientAssetManagerResponseModel in order to support both standard and
        client assets through a single unified interface. AssetToClientAssetManagerResponseModel
        is a strict superset of AssetToAssetManageResponseModel (all common fields are
        identical, with 8 additional optional fields). The cast is safe because the API
        response data structure is compatible with the richer model type.
        """
        if not client_company_id:
            # Cast standard assets to client model (superset type). Safe because:
            # 1. AssetToClientAssetManagerResponseModel has all fields from AssetToAssetManageResponseModel
            # 2. Additional client-specific fields are optional and will be None
            # 3. Both models parse the same base asset JSON structure
            result = await get_asset_manager_list.asyncio(
                client=self.client,
                model_filter_type=FilterType.COLLECTED_ASSETS,
                model_search_string=search_string,
                model_page=page,
                model_page_size=page_size,
            )
            return cast(list[AssetToClientAssetManagerResponseModel], result or [])
        else:
            return (
                await get_asset_manager_list_get_2.asyncio(
                    client_company_id=client_company_id,
                    client=self.client,
                    query_filter_type=AssetFilterType.CLIENT_ASSETS_COLLECTED,
                    query_search_string=search_string,
                    query_page=page,
                    query_page_size=page_size,
                )
                or []
            )
