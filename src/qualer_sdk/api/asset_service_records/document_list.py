from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    asset_service_record_id_path: str,
    *,
    asset_service_record_id_query: Optional[str] = None,
    model_asset_service_record_id: Optional[int] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["assetServiceRecordId"] = asset_service_record_id_query

    params["model.assetServiceRecordId"] = model_asset_service_record_id

    params = {k: v for k, v in params.items() if v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/assetservicerecords/{asset_service_record_id_path}/documents/files",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List[str]]:
    if response.status_code == 200:
        response_200 = cast(List[str], response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        response.raise_for_status()
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List[str]]:
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
    asset_service_record_id_query: Optional[str] = None,
    model_asset_service_record_id: Optional[int] = None,
) -> Response[List[str]]:
    """
    Args:
        asset_service_record_id_path (str):
        asset_service_record_id_query (Optional[str]):
        model_asset_service_record_id (Optional[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[str]]
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
    asset_service_record_id_query: Optional[str] = None,
    model_asset_service_record_id: Optional[int] = None,
) -> Optional[List[str]]:
    """
    Args:
        asset_service_record_id_path (str):
        asset_service_record_id_query (Optional[str]):
        model_asset_service_record_id (Optional[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List[str]
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
    asset_service_record_id_query: Optional[str] = None,
    model_asset_service_record_id: Optional[int] = None,
) -> Response[List[str]]:
    """
    Args:
        asset_service_record_id_path (str):
        asset_service_record_id_query (Optional[str]):
        model_asset_service_record_id (Optional[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[str]]
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
    asset_service_record_id_query: Optional[str] = None,
    model_asset_service_record_id: Optional[int] = None,
) -> Optional[List[str]]:
    """
    Args:
        asset_service_record_id_path (str):
        asset_service_record_id_query (Optional[str]):
        model_asset_service_record_id (Optional[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List[str]
    """

    return (
        await asyncio_detailed(
            asset_service_record_id_path=asset_service_record_id_path,
            client=client,
            asset_service_record_id_query=asset_service_record_id_query,
            model_asset_service_record_id=model_asset_service_record_id,
        )
    ).parsed
