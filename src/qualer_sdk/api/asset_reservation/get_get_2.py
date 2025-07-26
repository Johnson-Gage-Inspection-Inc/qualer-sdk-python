from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_asset_reservation_to_asset_reservation_response import (
    QualerApiModelsAssetReservationToAssetReservationResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    model_from: Union[Unset, str] = UNSET,
    model_to: Union[Unset, str] = UNSET,
    model_asset_id: Union[Unset, int] = UNSET,
    model_area_id: Union[Unset, int] = UNSET,
    model_product_id: Union[Unset, int] = UNSET,
    model_serial_number: Union[Unset, str] = UNSET,
    model_asset_tag: Union[Unset, str] = UNSET,
    model_reservation_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["model.from"] = model_from

    params["model.to"] = model_to

    params["model.assetId"] = model_asset_id

    params["model.areaId"] = model_area_id

    params["model.productId"] = model_product_id

    params["model.serialNumber"] = model_serial_number

    params["model.assetTag"] = model_asset_tag

    params["model.reservationId"] = model_reservation_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/assetsreservations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["QualerApiModelsAssetReservationToAssetReservationResponse"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                QualerApiModelsAssetReservationToAssetReservationResponse.from_dict(
                    response_200_item_data
                )
            )

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["QualerApiModelsAssetReservationToAssetReservationResponse"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    model_from: Union[Unset, str] = UNSET,
    model_to: Union[Unset, str] = UNSET,
    model_asset_id: Union[Unset, int] = UNSET,
    model_area_id: Union[Unset, int] = UNSET,
    model_product_id: Union[Unset, int] = UNSET,
    model_serial_number: Union[Unset, str] = UNSET,
    model_asset_tag: Union[Unset, str] = UNSET,
    model_reservation_id: Union[Unset, int] = UNSET,
) -> Response[list["QualerApiModelsAssetReservationToAssetReservationResponse"]]:
    """
    Args:
        model_from (Union[Unset, str]):
        model_to (Union[Unset, str]):
        model_asset_id (Union[Unset, int]):
        model_area_id (Union[Unset, int]):
        model_product_id (Union[Unset, int]):
        model_serial_number (Union[Unset, str]):
        model_asset_tag (Union[Unset, str]):
        model_reservation_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsAssetReservationToAssetReservationResponse']]
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
    model_from: Union[Unset, str] = UNSET,
    model_to: Union[Unset, str] = UNSET,
    model_asset_id: Union[Unset, int] = UNSET,
    model_area_id: Union[Unset, int] = UNSET,
    model_product_id: Union[Unset, int] = UNSET,
    model_serial_number: Union[Unset, str] = UNSET,
    model_asset_tag: Union[Unset, str] = UNSET,
    model_reservation_id: Union[Unset, int] = UNSET,
) -> Optional[list["QualerApiModelsAssetReservationToAssetReservationResponse"]]:
    """
    Args:
        model_from (Union[Unset, str]):
        model_to (Union[Unset, str]):
        model_asset_id (Union[Unset, int]):
        model_area_id (Union[Unset, int]):
        model_product_id (Union[Unset, int]):
        model_serial_number (Union[Unset, str]):
        model_asset_tag (Union[Unset, str]):
        model_reservation_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsAssetReservationToAssetReservationResponse']
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
    model_from: Union[Unset, str] = UNSET,
    model_to: Union[Unset, str] = UNSET,
    model_asset_id: Union[Unset, int] = UNSET,
    model_area_id: Union[Unset, int] = UNSET,
    model_product_id: Union[Unset, int] = UNSET,
    model_serial_number: Union[Unset, str] = UNSET,
    model_asset_tag: Union[Unset, str] = UNSET,
    model_reservation_id: Union[Unset, int] = UNSET,
) -> Response[list["QualerApiModelsAssetReservationToAssetReservationResponse"]]:
    """
    Args:
        model_from (Union[Unset, str]):
        model_to (Union[Unset, str]):
        model_asset_id (Union[Unset, int]):
        model_area_id (Union[Unset, int]):
        model_product_id (Union[Unset, int]):
        model_serial_number (Union[Unset, str]):
        model_asset_tag (Union[Unset, str]):
        model_reservation_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsAssetReservationToAssetReservationResponse']]
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
    model_from: Union[Unset, str] = UNSET,
    model_to: Union[Unset, str] = UNSET,
    model_asset_id: Union[Unset, int] = UNSET,
    model_area_id: Union[Unset, int] = UNSET,
    model_product_id: Union[Unset, int] = UNSET,
    model_serial_number: Union[Unset, str] = UNSET,
    model_asset_tag: Union[Unset, str] = UNSET,
    model_reservation_id: Union[Unset, int] = UNSET,
) -> Optional[list["QualerApiModelsAssetReservationToAssetReservationResponse"]]:
    """
    Args:
        model_from (Union[Unset, str]):
        model_to (Union[Unset, str]):
        model_asset_id (Union[Unset, int]):
        model_area_id (Union[Unset, int]):
        model_product_id (Union[Unset, int]):
        model_serial_number (Union[Unset, str]):
        model_asset_tag (Union[Unset, str]):
        model_reservation_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsAssetReservationToAssetReservationResponse']
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
