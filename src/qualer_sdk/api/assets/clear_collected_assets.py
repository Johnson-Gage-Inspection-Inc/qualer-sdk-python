from typing import Any, Dict, List, Union

from ...client import AuthenticatedClient, Client


def _get_kwargs(
    *,
    body: List[int],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/api/assets/collection/remove",
    }
    _kwargs["json"] = body
    headers["Content-Type"] = "application/json"
    _kwargs["headers"] = headers
    return _kwargs


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: List[int],
) -> None:
    """ClearCollectedAssets(int[] assetIds)

     [123,234,567] removes assets with selected Ids

    [] removes all assets from QuickCollection

    Args:
        body (List[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    client.get_httpx_client().request(
        **kwargs,
    )


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: List[int],
) -> None:
    """ClearCollectedAssets(int[] assetIds)

     [123,234,567] removes assets with selected Ids

    [] removes all assets from QuickCollection

    Args:
        body (List[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:

    """

    sync_detailed(
        client=client,
        body=body,
    )


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: List[int],
) -> None:
    """ClearCollectedAssets(int[] assetIds)

     [123,234,567] removes assets with selected Ids

    [] removes all assets from QuickCollection

    Args:
        body (List[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    await client.get_async_httpx_client().request(**kwargs)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: List[int],
) -> None:
    """ClearCollectedAssets(int[] assetIds)

    Args:
        body (List[int]): [123,234,567] removes assets with selected Ids. [] removes all assets from QuickCollection.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:

    """

    await asyncio_detailed(
        client=client,
        body=body,
    )
