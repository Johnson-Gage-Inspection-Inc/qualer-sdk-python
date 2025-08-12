from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_service_record_id_path: str,
    *,
    asset_service_record_id_query: Union[None, Unset, str] = UNSET,
    model_asset_service_record_id: Union[None, Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["assetServiceRecordId"] = asset_service_record_id_query

    params["model.assetServiceRecordId"] = model_asset_service_record_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/assetservicerecords/{asset_service_record_id_path}/documents/files",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list[str]]:
    if response.status_code == 200:
        response_200 = cast(list[str], response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list[str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_service_record_id_path: str,
    *,
    client: Union[AuthenticatedClient, Client],
    asset_service_record_id_query: Union[None, Unset, str] = UNSET,
    model_asset_service_record_id: Union[None, Unset, int] = UNSET,
) -> Response[list[str]]:
    """
    Args:
        asset_service_record_id_path (str):
        asset_service_record_id_query (Union[None, Unset, str]):
        model_asset_service_record_id (Union[None, Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[str]]
    """

    kwargs = _get_kwargs(
        asset_service_record_id_path=asset_service_record_id_path,
        asset_service_record_id_query=asset_service_record_id_query,
        model_asset_service_record_id=model_asset_service_record_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_service_record_id_path: str,
    *,
    client: Union[AuthenticatedClient, Client],
    asset_service_record_id_query: Union[None, Unset, str] = UNSET,
    model_asset_service_record_id: Union[None, Unset, int] = UNSET,
) -> Optional[list[str]]:
    """
    Args:
        asset_service_record_id_path (str):
        asset_service_record_id_query (Union[None, Unset, str]):
        model_asset_service_record_id (Union[None, Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[str]
    """

    return sync_detailed(
        asset_service_record_id_path=asset_service_record_id_path,
        client=client,
        asset_service_record_id_query=asset_service_record_id_query,
        model_asset_service_record_id=model_asset_service_record_id,
    ).parsed


async def asyncio_detailed(
    asset_service_record_id_path: str,
    *,
    client: Union[AuthenticatedClient, Client],
    asset_service_record_id_query: Union[None, Unset, str] = UNSET,
    model_asset_service_record_id: Union[None, Unset, int] = UNSET,
) -> Response[list[str]]:
    """
    Args:
        asset_service_record_id_path (str):
        asset_service_record_id_query (Union[None, Unset, str]):
        model_asset_service_record_id (Union[None, Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[str]]
    """

    kwargs = _get_kwargs(
        asset_service_record_id_path=asset_service_record_id_path,
        asset_service_record_id_query=asset_service_record_id_query,
        model_asset_service_record_id=model_asset_service_record_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_service_record_id_path: str,
    *,
    client: Union[AuthenticatedClient, Client],
    asset_service_record_id_query: Union[None, Unset, str] = UNSET,
    model_asset_service_record_id: Union[None, Unset, int] = UNSET,
) -> Optional[list[str]]:
    """
    Args:
        asset_service_record_id_path (str):
        asset_service_record_id_query (Union[None, Unset, str]):
        model_asset_service_record_id (Union[None, Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[str]
    """

    return (
        await asyncio_detailed(
            asset_service_record_id_path=asset_service_record_id_path,
            client=client,
            asset_service_record_id_query=asset_service_record_id_query,
            model_asset_service_record_id=model_asset_service_record_id,
        )
    ).parsed
