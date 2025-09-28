from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.order_cancel_response_200 import OrderCancelResponse200
from ...types import Response


def _get_kwargs(
    service_order_id: int,
    *,
    reason_text: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["reasonText"] = reason_text

    params = {k: v for k, v in params.items() if v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/api/service/workorders/{service_order_id}/cancel",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OrderCancelResponse200]:
    if response.status_code == 200:
        response_200 = OrderCancelResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        response.raise_for_status()
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OrderCancelResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_order_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    reason_text: Optional[str] = None,
) -> Response[OrderCancelResponse200]:
    """Cancel work order

    Args:
        service_order_id (int):
        reason_text (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderCancelResponse200]
    """

    kwargs = _get_kwargs(
        service_order_id=service_order_id,
        reason_text=reason_text,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_order_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    reason_text: Optional[str] = None,
) -> Optional[OrderCancelResponse200]:
    """Cancel work order

    Args:
        service_order_id (int):
        reason_text (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrderCancelResponse200
    """

    return sync_detailed(
        service_order_id=service_order_id,
        client=client,
        reason_text=reason_text,
    ).parsed


async def asyncio_detailed(
    service_order_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    reason_text: Optional[str] = None,
) -> Response[OrderCancelResponse200]:
    """Cancel work order

    Args:
        service_order_id (int):
        reason_text (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderCancelResponse200]
    """

    kwargs = _get_kwargs(
        service_order_id=service_order_id,
        reason_text=reason_text,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_order_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    reason_text: Optional[str] = None,
) -> Optional[OrderCancelResponse200]:
    """Cancel work order

    Args:
        service_order_id (int):
        reason_text (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrderCancelResponse200
    """

    return (
        await asyncio_detailed(
            service_order_id=service_order_id,
            client=client,
            reason_text=reason_text,
        )
    ).parsed
