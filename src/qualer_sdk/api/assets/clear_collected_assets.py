from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.clear_collected_assets_response_200 import (
    ClearCollectedAssetsResponse200,
)
from ...types import Response


def _get_kwargs(
    *,
    body: list[int],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/assets/collection/remove",
    }

    _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ClearCollectedAssetsResponse200]:
    if response.status_code == 200:
        response_200 = ClearCollectedAssetsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ClearCollectedAssetsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[int],
) -> Response[ClearCollectedAssetsResponse200]:
    """ClearCollectedAssets(int[] assetIds)

     [123,234,567] removes assets with selected Ids

    [] removes all assets from QuickCollection

    Args:
        body (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClearCollectedAssetsResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[int],
) -> Optional[ClearCollectedAssetsResponse200]:
    """ClearCollectedAssets(int[] assetIds)

     [123,234,567] removes assets with selected Ids

    [] removes all assets from QuickCollection

    Args:
        body (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClearCollectedAssetsResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[int],
) -> Response[ClearCollectedAssetsResponse200]:
    """ClearCollectedAssets(int[] assetIds)

     [123,234,567] removes assets with selected Ids

    [] removes all assets from QuickCollection

    Args:
        body (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClearCollectedAssetsResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[int],
) -> Optional[ClearCollectedAssetsResponse200]:
    """ClearCollectedAssets(int[] assetIds)

     [123,234,567] removes assets with selected Ids

    [] removes all assets from QuickCollection

    Args:
        body (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClearCollectedAssetsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
