from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_order_by_schedule_response_200 import CreateOrderByScheduleResponse200
from ...types import Response


def _get_kwargs(
    service_schedule_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/service/workorders/byplan/{service_schedule_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CreateOrderByScheduleResponse200]:
    if response.status_code == 200:
        response_200 = CreateOrderByScheduleResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CreateOrderByScheduleResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_schedule_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[CreateOrderByScheduleResponse200]:
    """
    Args:
        service_schedule_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOrderByScheduleResponse200]
    """

    kwargs = _get_kwargs(
        service_schedule_id=service_schedule_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_schedule_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[CreateOrderByScheduleResponse200]:
    """
    Args:
        service_schedule_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOrderByScheduleResponse200
    """

    return sync_detailed(
        service_schedule_id=service_schedule_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_schedule_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[CreateOrderByScheduleResponse200]:
    """
    Args:
        service_schedule_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOrderByScheduleResponse200]
    """

    kwargs = _get_kwargs(
        service_schedule_id=service_schedule_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_schedule_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[CreateOrderByScheduleResponse200]:
    """
    Args:
        service_schedule_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOrderByScheduleResponse200
    """

    return (
        await asyncio_detailed(
            service_schedule_id=service_schedule_id,
            client=client,
        )
    ).parsed
