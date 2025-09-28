from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_asset_to_asset_response_model import (
    AssetToAssetResponseModel,
)
from ...types import Response


def _get_kwargs(
    client_company_id: int,
    *,
    query_equipment_id: Optional[str] = None,
    query_serial_number: Optional[str] = None,
    query_asset_tag: Optional[str] = None,
    query_barcode: Optional[str] = None,
    query_legacy_id: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["query.equipmentId"] = query_equipment_id

    params["query.serialNumber"] = query_serial_number

    params["query.assetTag"] = query_asset_tag

    params["query.barcode"] = query_barcode

    params["query.legacyId"] = query_legacy_id

    params = {k: v for k, v in params.items() if v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/service/clients/{client_company_id}/assets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["AssetToAssetResponseModel"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AssetToAssetResponseModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        response.raise_for_status()
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["AssetToAssetResponseModel"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    client_company_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    query_equipment_id: Optional[str] = None,
    query_serial_number: Optional[str] = None,
    query_asset_tag: Optional[str] = None,
    query_barcode: Optional[str] = None,
    query_legacy_id: Optional[str] = None,
) -> Response[List["AssetToAssetResponseModel"]]:
    """
    Args:
        client_company_id (int):
        query_equipment_id (Optional[str]):
        query_serial_number (Optional[str]):
        query_asset_tag (Optional[str]):
        query_barcode (Optional[str]):
        query_legacy_id (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AssetToAssetResponseModel']]
    """

    kwargs = _get_kwargs(
        client_company_id=client_company_id,
        query_equipment_id=query_equipment_id,
        query_serial_number=query_serial_number,
        query_asset_tag=query_asset_tag,
        query_barcode=query_barcode,
        query_legacy_id=query_legacy_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    client_company_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    query_equipment_id: Optional[str] = None,
    query_serial_number: Optional[str] = None,
    query_asset_tag: Optional[str] = None,
    query_barcode: Optional[str] = None,
    query_legacy_id: Optional[str] = None,
) -> Optional[List["AssetToAssetResponseModel"]]:
    """
    Args:
        client_company_id (int):
        query_equipment_id (Optional[str]):
        query_serial_number (Optional[str]):
        query_asset_tag (Optional[str]):
        query_barcode (Optional[str]):
        query_legacy_id (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['AssetToAssetResponseModel']
    """

    return sync_detailed(
        client_company_id=client_company_id,
        client=client,
        query_equipment_id=query_equipment_id,
        query_serial_number=query_serial_number,
        query_asset_tag=query_asset_tag,
        query_barcode=query_barcode,
        query_legacy_id=query_legacy_id,
    ).parsed


async def asyncio_detailed(
    client_company_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    query_equipment_id: Optional[str] = None,
    query_serial_number: Optional[str] = None,
    query_asset_tag: Optional[str] = None,
    query_barcode: Optional[str] = None,
    query_legacy_id: Optional[str] = None,
) -> Response[List["AssetToAssetResponseModel"]]:
    """
    Args:
        client_company_id (int):
        query_equipment_id (Optional[str]):
        query_serial_number (Optional[str]):
        query_asset_tag (Optional[str]):
        query_barcode (Optional[str]):
        query_legacy_id (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AssetToAssetResponseModel']]
    """

    kwargs = _get_kwargs(
        client_company_id=client_company_id,
        query_equipment_id=query_equipment_id,
        query_serial_number=query_serial_number,
        query_asset_tag=query_asset_tag,
        query_barcode=query_barcode,
        query_legacy_id=query_legacy_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    client_company_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    query_equipment_id: Optional[str] = None,
    query_serial_number: Optional[str] = None,
    query_asset_tag: Optional[str] = None,
    query_barcode: Optional[str] = None,
    query_legacy_id: Optional[str] = None,
) -> Optional[List["AssetToAssetResponseModel"]]:
    """
    Args:
        client_company_id (int):
        query_equipment_id (Optional[str]):
        query_serial_number (Optional[str]):
        query_asset_tag (Optional[str]):
        query_barcode (Optional[str]):
        query_legacy_id (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['AssetToAssetResponseModel']
    """

    return (
        await asyncio_detailed(
            client_company_id=client_company_id,
            client=client,
            query_equipment_id=query_equipment_id,
            query_serial_number=query_serial_number,
            query_asset_tag=query_asset_tag,
            query_barcode=query_barcode,
            query_legacy_id=query_legacy_id,
        )
    ).parsed
