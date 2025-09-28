import httpx
import pytest

from qualer_sdk import errors
from qualer_sdk.api.service_order_items import get_work_items_workitems as workitems
from qualer_sdk.client import Client


class _FakeHTTPXClient(httpx.Client):
    def __init__(self, response: httpx.Response):
        super().__init__(base_url="https://jgiquality.qualer.com")
        self._response = response
        self.last_request_kwargs = None

    def request(self, *args, **kwargs):
        # capture for assertions if needed
        self.last_request_kwargs = kwargs
        return self._response


def _server_500_response():
    # Simulate Qualer returning a 500 with a simple JSON error body
    return httpx.Response(
        status_code=500,
        content=b'{"Message": "Something went wrong."}',
        headers={"content-type": "application/json; charset=utf-8"},
        request=httpx.Request("GET", "https://jgiquality.qualer.com/api/service/workitems"),
    )


def test_workitems_500_returns_none_by_default():
    client = Client()  # raise_on_unexpected_status defaults to False
    fake_httpx = _FakeHTTPXClient(_server_500_response())
    client.set_httpx_client(fake_httpx)

    # Using the convenience sync() which returns parsed or None
    result = workitems.sync(client=client, work_item_number="56561-072770")
    assert result is None

    # And the detailed variant exposes the raw status code but still parsed is None
    detailed = workitems.sync_detailed(client=client, work_item_number="56561-072770")
    assert int(detailed.status_code) == 500
    assert detailed.parsed is None


def test_workitems_500_raises_when_configured():
    client = Client(raise_on_unexpected_status=True)
    fake_httpx = _FakeHTTPXClient(_server_500_response())
    client.set_httpx_client(fake_httpx)

    with pytest.raises(errors.UnexpectedStatus) as ei:
        workitems.sync(client=client, work_item_number="56561-072770")

    exc = ei.value
    assert exc.status_code == 500
    assert b"Something went wrong" in exc.content
