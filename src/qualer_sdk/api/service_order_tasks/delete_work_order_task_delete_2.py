from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_work_order_task_delete_2_response_204 import (
    DeleteWorkOrderTaskDelete2Response204,
)
from ...types import Response


def _get_kwargs(
    service_order_id: int,
    service_order_task_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/api/service/workorders/{service_order_id}/Tasks/{service_order_task_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DeleteWorkOrderTaskDelete2Response204]]:
    if response.status_code == 204:
        response_204 = DeleteWorkOrderTaskDelete2Response204.from_dict(response.json())

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
) -> Response[Union[Any, DeleteWorkOrderTaskDelete2Response204]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_order_id: int,
    service_order_task_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, DeleteWorkOrderTaskDelete2Response204]]:
    """
    Args:
        service_order_id (int):
        service_order_task_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeleteWorkOrderTaskDelete2Response204]]
    """

    kwargs = _get_kwargs(
        service_order_id=service_order_id,
        service_order_task_id=service_order_task_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_order_id: int,
    service_order_task_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, DeleteWorkOrderTaskDelete2Response204]]:
    """
    Args:
        service_order_id (int):
        service_order_task_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeleteWorkOrderTaskDelete2Response204]
    """

    return sync_detailed(
        service_order_id=service_order_id,
        service_order_task_id=service_order_task_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_order_id: int,
    service_order_task_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, DeleteWorkOrderTaskDelete2Response204]]:
    """
    Args:
        service_order_id (int):
        service_order_task_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeleteWorkOrderTaskDelete2Response204]]
    """

    kwargs = _get_kwargs(
        service_order_id=service_order_id,
        service_order_task_id=service_order_task_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_order_id: int,
    service_order_task_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, DeleteWorkOrderTaskDelete2Response204]]:
    """
    Args:
        service_order_id (int):
        service_order_task_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeleteWorkOrderTaskDelete2Response204]
    """

    return (
        await asyncio_detailed(
            service_order_id=service_order_id,
            service_order_task_id=service_order_task_id,
            client=client,
        )
    ).parsed
