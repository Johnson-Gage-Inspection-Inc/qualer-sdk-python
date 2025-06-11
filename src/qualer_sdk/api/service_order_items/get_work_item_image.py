from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_work_item_image_response_200 import GetWorkItemImageResponse200
from ...types import Response


def _get_kwargs(
    work_item_id: int,
    image_name: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/service/workitems/{work_item_id}/images/{image_name}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetWorkItemImageResponse200]:
    if response.status_code == 200:
        response_200 = GetWorkItemImageResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetWorkItemImageResponse200]:
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
) -> Response[GetWorkItemImageResponse200]:
    """
    Args:
        work_item_id (int):
        image_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWorkItemImageResponse200]
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
) -> Optional[GetWorkItemImageResponse200]:
    """
    Args:
        work_item_id (int):
        image_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWorkItemImageResponse200
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
) -> Response[GetWorkItemImageResponse200]:
    """
    Args:
        work_item_id (int):
        image_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWorkItemImageResponse200]
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
) -> Optional[GetWorkItemImageResponse200]:
    """
    Args:
        work_item_id (int):
        image_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWorkItemImageResponse200
    """

    return (
        await asyncio_detailed(
            work_item_id=work_item_id,
            image_name=image_name,
            client=client,
        )
    ).parsed
