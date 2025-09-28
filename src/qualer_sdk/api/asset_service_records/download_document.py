from http import HTTPStatus
from io import BytesIO
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import File, Response


def _get_kwargs(
    asset_service_record_id_path: str,
    file_name_path: str,
    *,
    asset_service_record_id_query: Optional[str] = None,
    file_name_query: Optional[str] = None,
    model_asset_service_record_id: Optional[int] = None,
    model_file_name: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["assetServiceRecordId"] = asset_service_record_id_query

    params["fileName"] = file_name_query

    params["model.assetServiceRecordId"] = model_asset_service_record_id

    params["model.fileName"] = model_file_name

    params = {k: v for k, v in params.items() if v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/assetservicerecords/{asset_service_record_id_path}/documents/{file_name_path}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[File]:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        response.raise_for_status()
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_service_record_id_path: str,
    file_name_path: str,
    *,
    client: Union[AuthenticatedClient, Client],
    asset_service_record_id_query: Optional[str] = None,
    file_name_query: Optional[str] = None,
    model_asset_service_record_id: Optional[int] = None,
    model_file_name: Optional[str] = None,
) -> Response[File]:
    """
    Args:
        asset_service_record_id_path (str):
        file_name_path (str):
        asset_service_record_id_query (Optional[str]):
        file_name_query (Optional[str]):
        model_asset_service_record_id (Optional[int]):
        model_file_name (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        asset_service_record_id_path=asset_service_record_id_path,
        file_name_path=file_name_path,
        asset_service_record_id_query=asset_service_record_id_query,
        file_name_query=file_name_query,
        model_asset_service_record_id=model_asset_service_record_id,
        model_file_name=model_file_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_service_record_id_path: str,
    file_name_path: str,
    *,
    client: Union[AuthenticatedClient, Client],
    asset_service_record_id_query: Optional[str] = None,
    file_name_query: Optional[str] = None,
    model_asset_service_record_id: Optional[int] = None,
    model_file_name: Optional[str] = None,
) -> Optional[File]:
    """
    Args:
        asset_service_record_id_path (str):
        file_name_path (str):
        asset_service_record_id_query (Optional[str]):
        file_name_query (Optional[str]):
        model_asset_service_record_id (Optional[int]):
        model_file_name (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return sync_detailed(
        asset_service_record_id_path=asset_service_record_id_path,
        file_name_path=file_name_path,
        client=client,
        asset_service_record_id_query=asset_service_record_id_query,
        file_name_query=file_name_query,
        model_asset_service_record_id=model_asset_service_record_id,
        model_file_name=model_file_name,
    ).parsed


async def asyncio_detailed(
    asset_service_record_id_path: str,
    file_name_path: str,
    *,
    client: Union[AuthenticatedClient, Client],
    asset_service_record_id_query: Optional[str] = None,
    file_name_query: Optional[str] = None,
    model_asset_service_record_id: Optional[int] = None,
    model_file_name: Optional[str] = None,
) -> Response[File]:
    """
    Args:
        asset_service_record_id_path (str):
        file_name_path (str):
        asset_service_record_id_query (Optional[str]):
        file_name_query (Optional[str]):
        model_asset_service_record_id (Optional[int]):
        model_file_name (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        asset_service_record_id_path=asset_service_record_id_path,
        file_name_path=file_name_path,
        asset_service_record_id_query=asset_service_record_id_query,
        file_name_query=file_name_query,
        model_asset_service_record_id=model_asset_service_record_id,
        model_file_name=model_file_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_service_record_id_path: str,
    file_name_path: str,
    *,
    client: Union[AuthenticatedClient, Client],
    asset_service_record_id_query: Optional[str] = None,
    file_name_query: Optional[str] = None,
    model_asset_service_record_id: Optional[int] = None,
    model_file_name: Optional[str] = None,
) -> Optional[File]:
    """
    Args:
        asset_service_record_id_path (str):
        file_name_path (str):
        asset_service_record_id_query (Optional[str]):
        file_name_query (Optional[str]):
        model_asset_service_record_id (Optional[int]):
        model_file_name (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return (
        await asyncio_detailed(
            asset_service_record_id_path=asset_service_record_id_path,
            file_name_path=file_name_path,
            client=client,
            asset_service_record_id_query=asset_service_record_id_query,
            file_name_query=file_name_query,
            model_asset_service_record_id=model_asset_service_record_id,
            model_file_name=model_file_name,
        )
    ).parsed
