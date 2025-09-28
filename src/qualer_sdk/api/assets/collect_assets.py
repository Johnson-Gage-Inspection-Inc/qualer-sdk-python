from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.collect_assets_response_200 import CollectAssetsResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: List[int],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/api/assets/collection/add",
    }

    _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CollectAssetsResponse200]:
    if response.status_code == 200:
        response_200 = CollectAssetsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 204:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        response.raise_for_status()
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CollectAssetsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: List[int],
) -> Response[CollectAssetsResponse200]:
    """CollectAssets(int[] assetIds)

     [123,234,567]

    Args:
        body (List[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CollectAssetsResponse200]
        Note: If the server responds with 204 No Content, `parsed` will be None.
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
    body: List[int],
) -> Optional[CollectAssetsResponse200]:
    """CollectAssets(int[] assetIds)

     [123,234,567]

    Args:
        body (List[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Optional[CollectAssetsResponse200]
        Note: None when the server returns 204 No Content.
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: List[int],
) -> Response[CollectAssetsResponse200]:
    """CollectAssets(int[] assetIds)

     [123,234,567]

    Args:
        body (List[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CollectAssetsResponse200]
        Note: If the server responds with 204 No Content, `parsed` will be None.
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: List[int],
) -> Optional[CollectAssetsResponse200]:
    """CollectAssets(int[] assetIds)

     [123,234,567]

    Args:
        body (List[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Optional[CollectAssetsResponse200]
        Note: None when the server returns 204 No Content.
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
