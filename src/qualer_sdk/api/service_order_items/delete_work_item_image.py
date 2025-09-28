from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_work_item_image_response_200 import DeleteWorkItemImageResponse200
from ...types import Response


def _get_kwargs(
    work_item_id: int,
    image_name: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/api/service/workitems/{work_item_id}/images/{image_name}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DeleteWorkItemImageResponse200]:
    if response.status_code == 200:
        response_200 = DeleteWorkItemImageResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        response.raise_for_status()
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DeleteWorkItemImageResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    work_item_id: int,
    image_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DeleteWorkItemImageResponse200]:
    """
    Args:
        work_item_id (int):
        image_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteWorkItemImageResponse200]
    """

    kwargs = _get_kwargs(
        work_item_id=work_item_id,
        image_name=image_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    work_item_id: int,
    image_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[DeleteWorkItemImageResponse200]:
    """
    Args:
        work_item_id (int):
        image_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteWorkItemImageResponse200
    """

    return sync_detailed(
        work_item_id=work_item_id,
        image_name=image_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    work_item_id: int,
    image_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DeleteWorkItemImageResponse200]:
    """
    Args:
        work_item_id (int):
        image_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteWorkItemImageResponse200]
    """

    kwargs = _get_kwargs(
        work_item_id=work_item_id,
        image_name=image_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    work_item_id: int,
    image_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[DeleteWorkItemImageResponse200]:
    """
    Args:
        work_item_id (int):
        image_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteWorkItemImageResponse200
    """

    return (
        await asyncio_detailed(
            work_item_id=work_item_id,
            image_name=image_name,
            client=client,
        )
    ).parsed
