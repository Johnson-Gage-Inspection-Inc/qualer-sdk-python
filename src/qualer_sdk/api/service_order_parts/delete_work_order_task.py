from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_work_order_task_response_204 import DeleteWorkOrderTaskResponse204
from ...types import Response


def _get_kwargs(
    service_order_id: int,
    service_order_item_part_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/api/service/workorders/{service_order_id}/parts/{service_order_item_part_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DeleteWorkOrderTaskResponse204]:
    if response.status_code == 204:
        response_204 = DeleteWorkOrderTaskResponse204.from_dict(response.json())

        return response_204
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DeleteWorkOrderTaskResponse204]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_order_id: int,
    service_order_item_part_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DeleteWorkOrderTaskResponse204]:
    """
    Args:
        service_order_id (int):
        service_order_item_part_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteWorkOrderTaskResponse204]
    """

    kwargs = _get_kwargs(
        service_order_id=service_order_id,
        service_order_item_part_id=service_order_item_part_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_order_id: int,
    service_order_item_part_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[DeleteWorkOrderTaskResponse204]:
    """
    Args:
        service_order_id (int):
        service_order_item_part_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteWorkOrderTaskResponse204
    """

    return sync_detailed(
        service_order_id=service_order_id,
        service_order_item_part_id=service_order_item_part_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_order_id: int,
    service_order_item_part_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DeleteWorkOrderTaskResponse204]:
    """
    Args:
        service_order_id (int):
        service_order_item_part_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteWorkOrderTaskResponse204]
    """

    kwargs = _get_kwargs(
        service_order_id=service_order_id,
        service_order_item_part_id=service_order_item_part_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_order_id: int,
    service_order_item_part_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[DeleteWorkOrderTaskResponse204]:
    """
    Args:
        service_order_id (int):
        service_order_item_part_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteWorkOrderTaskResponse204
    """

    return (
        await asyncio_detailed(
            service_order_id=service_order_id,
            service_order_item_part_id=service_order_item_part_id,
            client=client,
        )
    ).parsed
