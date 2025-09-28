import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_asset_reservation_to_asset_reservation_response import (
    AssetReservationToAssetReservationResponse,
)
from ...types import Response


def _get_kwargs(
    *,
    model_from: Optional[datetime.datetime] = None,
    model_to: Optional[datetime.datetime] = None,
    model_asset_id: Optional[int] = None,
    model_area_id: Optional[int] = None,
    model_product_id: Optional[int] = None,
    model_serial_number: Optional[str] = None,
    model_asset_tag: Optional[str] = None,
    model_reservation_id: Optional[int] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_model_from: Optional[str] = None
    if model_from:
        json_model_from = model_from.isoformat()
    params["model.from"] = json_model_from

    json_model_to: Optional[str] = None
    if model_to:
        json_model_to = model_to.isoformat()
    params["model.to"] = json_model_to

    params["model.assetId"] = model_asset_id

    params["model.areaId"] = model_area_id

    params["model.productId"] = model_product_id

    params["model.serialNumber"] = model_serial_number

    params["model.assetTag"] = model_asset_tag

    params["model.reservationId"] = model_reservation_id

    params = {k: v for k, v in params.items() if v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/assetsreservations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["AssetReservationToAssetReservationResponse"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AssetReservationToAssetReservationResponse.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        response.raise_for_status()
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["AssetReservationToAssetReservationResponse"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    model_from: Optional[datetime.datetime] = None,
    model_to: Optional[datetime.datetime] = None,
    model_asset_id: Optional[int] = None,
    model_area_id: Optional[int] = None,
    model_product_id: Optional[int] = None,
    model_serial_number: Optional[str] = None,
    model_asset_tag: Optional[str] = None,
    model_reservation_id: Optional[int] = None,
) -> Response[List["AssetReservationToAssetReservationResponse"]]:
    """
    Args:
        model_from (Optional[datetime.datetime]):
        model_to (Optional[datetime.datetime]):
        model_asset_id (Optional[int]):
        model_area_id (Optional[int]):
        model_product_id (Optional[int]):
        model_serial_number (Optional[str]):
        model_asset_tag (Optional[str]):
        model_reservation_id (Optional[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AssetReservationToAssetReservationResponse']]
    """

    kwargs = _get_kwargs(
        model_from=model_from,
        model_to=model_to,
        model_asset_id=model_asset_id,
        model_area_id=model_area_id,
        model_product_id=model_product_id,
        model_serial_number=model_serial_number,
        model_asset_tag=model_asset_tag,
        model_reservation_id=model_reservation_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    model_from: Optional[datetime.datetime] = None,
    model_to: Optional[datetime.datetime] = None,
    model_asset_id: Optional[int] = None,
    model_area_id: Optional[int] = None,
    model_product_id: Optional[int] = None,
    model_serial_number: Optional[str] = None,
    model_asset_tag: Optional[str] = None,
    model_reservation_id: Optional[int] = None,
) -> Optional[List["AssetReservationToAssetReservationResponse"]]:
    """
    Args:
        model_from (Optional[datetime.datetime]):
        model_to (Optional[datetime.datetime]):
        model_asset_id (Optional[int]):
        model_area_id (Optional[int]):
        model_product_id (Optional[int]):
        model_serial_number (Optional[str]):
        model_asset_tag (Optional[str]):
        model_reservation_id (Optional[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['AssetReservationToAssetReservationResponse']
    """

    return sync_detailed(
        client=client,
        model_from=model_from,
        model_to=model_to,
        model_asset_id=model_asset_id,
        model_area_id=model_area_id,
        model_product_id=model_product_id,
        model_serial_number=model_serial_number,
        model_asset_tag=model_asset_tag,
        model_reservation_id=model_reservation_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    model_from: Optional[datetime.datetime] = None,
    model_to: Optional[datetime.datetime] = None,
    model_asset_id: Optional[int] = None,
    model_area_id: Optional[int] = None,
    model_product_id: Optional[int] = None,
    model_serial_number: Optional[str] = None,
    model_asset_tag: Optional[str] = None,
    model_reservation_id: Optional[int] = None,
) -> Response[List["AssetReservationToAssetReservationResponse"]]:
    """
    Args:
        model_from (Optional[datetime.datetime]):
        model_to (Optional[datetime.datetime]):
        model_asset_id (Optional[int]):
        model_area_id (Optional[int]):
        model_product_id (Optional[int]):
        model_serial_number (Optional[str]):
        model_asset_tag (Optional[str]):
        model_reservation_id (Optional[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AssetReservationToAssetReservationResponse']]
    """

    kwargs = _get_kwargs(
        model_from=model_from,
        model_to=model_to,
        model_asset_id=model_asset_id,
        model_area_id=model_area_id,
        model_product_id=model_product_id,
        model_serial_number=model_serial_number,
        model_asset_tag=model_asset_tag,
        model_reservation_id=model_reservation_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    model_from: Optional[datetime.datetime] = None,
    model_to: Optional[datetime.datetime] = None,
    model_asset_id: Optional[int] = None,
    model_area_id: Optional[int] = None,
    model_product_id: Optional[int] = None,
    model_serial_number: Optional[str] = None,
    model_asset_tag: Optional[str] = None,
    model_reservation_id: Optional[int] = None,
) -> Optional[List["AssetReservationToAssetReservationResponse"]]:
    """
    Args:
        model_from (Optional[datetime.datetime]):
        model_to (Optional[datetime.datetime]):
        model_asset_id (Optional[int]):
        model_area_id (Optional[int]):
        model_product_id (Optional[int]):
        model_serial_number (Optional[str]):
        model_asset_tag (Optional[str]):
        model_reservation_id (Optional[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['AssetReservationToAssetReservationResponse']
    """

    return (
        await asyncio_detailed(
            client=client,
            model_from=model_from,
            model_to=model_to,
            model_asset_id=model_asset_id,
            model_area_id=model_area_id,
            model_product_id=model_product_id,
            model_serial_number=model_serial_number,
            model_asset_tag=model_asset_tag,
            model_reservation_id=model_reservation_id,
        )
    ).parsed
