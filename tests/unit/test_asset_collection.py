import asyncio

import pytest


def _setup_stubs(monkeypatch):
    """Prepare stubs for API modules used by QuickCollection."""
    import qualer_sdk.quick_collection as ac

    calls = {
        "collect_sync": [],
        "collect_async": [],
        "clear_sync": [],
        "clear_async": [],
        "get_sync": [],
        "get_async": [],
        "get_client_sync": [],
        "get_client_async": [],
    }

    def collect_sync(*, client, body):
        calls["collect_sync"].append((client, tuple(body)))

    async def collect_async(*, client, body):
        calls["collect_async"].append((client, tuple(body)))

    def clear_sync(*, client, body):
        calls["clear_sync"].append((client, tuple(body)))

    async def clear_async(*, client, body):
        calls["clear_async"].append((client, tuple(body)))

    def get_sync(*, client, model_filter_type, model_search_string, model_page, model_page_size):
        calls["get_sync"].append(
            (client, model_filter_type, model_search_string, model_page, model_page_size)
        )
        # Return a simple structure we can assert on
        return [{"id": 1}, {"id": 2}]

    async def get_async(
        *, client, model_filter_type, model_search_string, model_page, model_page_size
    ):
        calls["get_async"].append(
            (client, model_filter_type, model_search_string, model_page, model_page_size)
        )
        return [{"id": 1}, {"id": 2}]

    def get_client_sync(
        *,
        client_company_id,
        client,
        query_filter_type,
        query_search_string,
        query_page,
        query_page_size,
    ):
        calls["get_client_sync"].append(
            (
                client_company_id,
                client,
                query_filter_type,
                query_search_string,
                query_page,
                query_page_size,
            )
        )
        return [{"id": 10}, {"id": 20}]

    async def get_client_async(
        *,
        client_company_id,
        client,
        query_filter_type,
        query_search_string,
        query_page,
        query_page_size,
    ):
        calls["get_client_async"].append(
            (
                client_company_id,
                client,
                query_filter_type,
                query_search_string,
                query_page,
                query_page_size,
            )
        )
        return [{"id": 10}, {"id": 20}]

    # Patch the module objects and their sync/asyncio attributes
    monkeypatch.setattr(ac.collect_assets, "sync", collect_sync, raising=True)
    monkeypatch.setattr(ac.collect_assets, "asyncio", collect_async, raising=True)
    monkeypatch.setattr(ac.clear_collected_assets, "sync", clear_sync, raising=True)
    monkeypatch.setattr(ac.clear_collected_assets, "asyncio", clear_async, raising=True)
    monkeypatch.setattr(ac.get_asset_manager_list, "sync", get_sync, raising=True)
    monkeypatch.setattr(ac.get_asset_manager_list, "asyncio", get_async, raising=True)
    monkeypatch.setattr(ac.get_asset_manager_list_get_2, "sync", get_client_sync, raising=True)
    monkeypatch.setattr(ac.get_asset_manager_list_get_2, "asyncio", get_client_async, raising=True)

    return ac, calls


def test_asset_collection_add_and_details(monkeypatch):
    ac, calls = _setup_stubs(monkeypatch)

    client = object()
    # Disable start_clean to avoid an initial clear-all call
    with ac.QuickCollection(client, [1, 2], start_clean=False) as coll:
        coll.add(3)
        # get details should call the list endpoint with collected filter
        details = coll.get_details(page=1, page_size=50)

        assert isinstance(details, list)
        assert calls["collect_sync"] == [(client, (1, 2)), (client, (3,))]
        # clear is called on exit only (after context)
        assert calls["clear_sync"] == []
        # get manager list called once with our pagination
        assert len(calls["get_sync"]) == 1
        _, filter_type, _, page, page_size = calls["get_sync"][0]
        assert page == 1 and page_size == 50
        # Filter type is an enum; just ensure we passed some value
        assert filter_type is not None

    # After context exit, clear_sync should be called with []
    assert calls["clear_sync"] == [(client, ())]


def test_asset_collection_remove_discard_pop_clear(monkeypatch):
    ac, calls = _setup_stubs(monkeypatch)

    client = object()
    with ac.QuickCollection(client, [1, 2, 3]) as coll:
        # remove should clear that specific id on server
        coll.remove(2)
        assert (client, (2,)) in calls["clear_sync"]

        # discard a missing id should be a no-op on server
        before = list(calls["clear_sync"])
        coll.discard(99)
        assert list(calls["clear_sync"]) == before

        # pop from a singleton set is deterministic
        coll.clear()  # clear everything, then add a single id for deterministic pop
        coll.add(42)
        popped = coll.pop()
        assert popped == 42
        # pop should clear that single id on server
        assert (client, (42,)) in calls["clear_sync"]

        # clear should clear all on server with []
        coll.clear()
        assert (client, ()) in calls["clear_sync"]


def test_asset_collection_cleanup_on_exception(monkeypatch):
    ac, calls = _setup_stubs(monkeypatch)
    client = object()

    class Boom(RuntimeError):
        pass

    with pytest.raises(Boom):
        with ac.QuickCollection(client, [5]):
            raise Boom("boom")

    # Even with an exception, cleanup should have attempted a clear-all
    assert calls["clear_sync"][-1] == (client, ())


def test_async_asset_collection_add_and_details(monkeypatch):
    ac, calls = _setup_stubs(monkeypatch)
    client = object()

    async def _main():
        async with ac.AsyncQuickCollection(client, [10, 20]) as coll:
            await coll.add(30)
            details = await coll.get_details(search_string="x")
            assert isinstance(details, list)

    asyncio.run(_main())

    # initial collect and add(30)
    assert calls["collect_async"] == [(client, (10, 20)), (client, (30,))]
    # clear-all on exit
    assert calls["clear_async"][-1] == (client, ())


def test_async_asset_collection_cleanup_on_exception(monkeypatch):
    ac, calls = _setup_stubs(monkeypatch)
    client = object()

    class Oops(RuntimeError):
        pass

    async def _boom():
        async with ac.AsyncQuickCollection(client, [7]):
            raise Oops("oops")

    with pytest.raises(Oops):
        asyncio.run(_boom())

    # ensure clear-all attempted
    assert calls["clear_async"][-1] == (client, ())


def test_asset_collection_get_details_with_client_company_id(monkeypatch):
    """Test that get_details uses client API when client_company_id is provided."""
    ac, calls = _setup_stubs(monkeypatch)

    client = object()
    with ac.QuickCollection(client, [1, 2], start_clean=False) as coll:
        # Query with client_company_id should use get_asset_manager_list_get_2
        details = coll.get_details(client_company_id=123, search_string="test")

        assert isinstance(details, list)
        assert len(calls["get_client_sync"]) == 1
        # Verify client_company_id was passed to the client API
        company_id, _, filter_type, search_str, page, page_size = calls["get_client_sync"][0]
        assert company_id == 123
        assert search_str == "test"
        # Standard API should not have been called
        assert len(calls["get_sync"]) == 0


def test_asset_collection_get_details_without_client_company_id(monkeypatch):
    """Test that get_details uses standard API when client_company_id is not provided."""
    ac, calls = _setup_stubs(monkeypatch)

    client = object()
    with ac.QuickCollection(client, [1, 2], start_clean=False) as coll:
        # Query without client_company_id should use standard get_asset_manager_list
        details = coll.get_details(page=2, page_size=25)

        assert isinstance(details, list)
        assert len(calls["get_sync"]) == 1
        # Client API should not have been called
        assert len(calls["get_client_sync"]) == 0


def test_async_asset_collection_get_details_with_client_company_id(monkeypatch):
    """Test that async get_details uses client API when client_company_id is provided."""
    ac, calls = _setup_stubs(monkeypatch)
    client = object()

    async def _main():
        async with ac.AsyncQuickCollection(client, [10, 20], start_clean=False) as coll:
            # Query with client_company_id should use get_asset_manager_list_get_2
            details = await coll.get_details(client_company_id=456, search_string="async_test")
            assert isinstance(details, list)

    asyncio.run(_main())

    assert len(calls["get_client_async"]) == 1
    company_id, _, filter_type, search_str, page, page_size = calls["get_client_async"][0]
    assert company_id == 456
    assert search_str == "async_test"
    # Standard API should not have been called
    assert len(calls["get_async"]) == 0


def test_async_asset_collection_get_details_without_client_company_id(monkeypatch):
    """Test that async get_details uses standard API when client_company_id is not provided."""
    ac, calls = _setup_stubs(monkeypatch)
    client = object()

    async def _main():
        async with ac.AsyncQuickCollection(client, [10, 20], start_clean=False) as coll:
            # Query without client_company_id should use standard get_asset_manager_list
            details = await coll.get_details(page=3, page_size=100)
            assert isinstance(details, list)

    asyncio.run(_main())

    assert len(calls["get_async"]) == 1
    # Client API should not have been called
    assert len(calls["get_client_async"]) == 0
