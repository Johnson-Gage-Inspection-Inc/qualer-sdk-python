from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.download_documents_response_200 import DownloadDocumentsResponse200
from ...types import Response


def _get_kwargs(
    asset_service_record_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/assetservicerecords/{asset_service_record_id}/documents",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DownloadDocumentsResponse200]:
    if response.status_code == 200:
        response_200 = DownloadDocumentsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DownloadDocumentsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_service_record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DownloadDocumentsResponse200]:
    """
    Args:
        asset_service_record_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DownloadDocumentsResponse200]
    """

    kwargs = _get_kwargs(
        asset_service_record_id=asset_service_record_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_service_record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[DownloadDocumentsResponse200]:
    """
    Args:
        asset_service_record_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DownloadDocumentsResponse200
    """

    return sync_detailed(
        asset_service_record_id=asset_service_record_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    asset_service_record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DownloadDocumentsResponse200]:
    """
    Args:
        asset_service_record_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DownloadDocumentsResponse200]
    """

    kwargs = _get_kwargs(
        asset_service_record_id=asset_service_record_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_service_record_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[DownloadDocumentsResponse200]:
    """
    Args:
        asset_service_record_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DownloadDocumentsResponse200
    """

    return (
        await asyncio_detailed(
            asset_service_record_id=asset_service_record_id,
            client=client,
        )
    ).parsed
