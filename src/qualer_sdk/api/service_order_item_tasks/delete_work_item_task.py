from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_work_item_task_response_200 import DeleteWorkItemTaskResponse200
from ...types import Response


def _get_kwargs(
    work_item_id: int,
    task_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/api/service/workitems/{work_item_id}/tasks/{task_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DeleteWorkItemTaskResponse200]:
    if response.status_code == 200:
        response_200 = DeleteWorkItemTaskResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        response.raise_for_status()
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DeleteWorkItemTaskResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    work_item_id: int,
    task_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DeleteWorkItemTaskResponse200]:
    """
    Args:
        work_item_id (int):
        task_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteWorkItemTaskResponse200]
    """

    kwargs = _get_kwargs(
        work_item_id=work_item_id,
        task_id=task_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    work_item_id: int,
    task_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[DeleteWorkItemTaskResponse200]:
    """
    Args:
        work_item_id (int):
        task_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteWorkItemTaskResponse200
    """

    return sync_detailed(
        work_item_id=work_item_id,
        task_id=task_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    work_item_id: int,
    task_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DeleteWorkItemTaskResponse200]:
    """
    Args:
        work_item_id (int):
        task_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteWorkItemTaskResponse200]
    """

    kwargs = _get_kwargs(
        work_item_id=work_item_id,
        task_id=task_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    work_item_id: int,
    task_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[DeleteWorkItemTaskResponse200]:
    """
    Args:
        work_item_id (int):
        task_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteWorkItemTaskResponse200
    """

    return (
        await asyncio_detailed(
            work_item_id=work_item_id,
            task_id=task_id,
            client=client,
        )
    ).parsed
