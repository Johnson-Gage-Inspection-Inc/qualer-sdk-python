from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.close_response_200 import CloseResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    model_asset_id: Union[None, Unset, int] = UNSET,
    model_area_id: Union[None, Unset, int] = UNSET,
    model_product_id: Union[None, Unset, int] = UNSET,
    model_serial_number: Union[None, Unset, str] = UNSET,
    model_asset_tag: Union[None, Unset, str] = UNSET,
    model_reservation_id: Union[None, Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["model.assetId"] = model_asset_id

    params["model.areaId"] = model_area_id

    params["model.productId"] = model_product_id

    params["model.serialNumber"] = model_serial_number

    params["model.assetTag"] = model_asset_tag

    params["model.reservationId"] = model_reservation_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/assetsreservations/close",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CloseResponse200]:
    if response.status_code == 200:
        response_200 = CloseResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CloseResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    model_asset_id: Union[None, Unset, int] = UNSET,
    model_area_id: Union[None, Unset, int] = UNSET,
    model_product_id: Union[None, Unset, int] = UNSET,
    model_serial_number: Union[None, Unset, str] = UNSET,
    model_asset_tag: Union[None, Unset, str] = UNSET,
    model_reservation_id: Union[None, Unset, int] = UNSET,
) -> Response[CloseResponse200]:
    """
    Args:
        model_asset_id (Union[None, Unset, int]):
        model_area_id (Union[None, Unset, int]):
        model_product_id (Union[None, Unset, int]):
        model_serial_number (Union[None, Unset, str]):
        model_asset_tag (Union[None, Unset, str]):
        model_reservation_id (Union[None, Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloseResponse200]
    """

    kwargs = _get_kwargs(
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
    model_asset_id: Union[None, Unset, int] = UNSET,
    model_area_id: Union[None, Unset, int] = UNSET,
    model_product_id: Union[None, Unset, int] = UNSET,
    model_serial_number: Union[None, Unset, str] = UNSET,
    model_asset_tag: Union[None, Unset, str] = UNSET,
    model_reservation_id: Union[None, Unset, int] = UNSET,
) -> Optional[CloseResponse200]:
    """
    Args:
        model_asset_id (Union[None, Unset, int]):
        model_area_id (Union[None, Unset, int]):
        model_product_id (Union[None, Unset, int]):
        model_serial_number (Union[None, Unset, str]):
        model_asset_tag (Union[None, Unset, str]):
        model_reservation_id (Union[None, Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloseResponse200
    """

    return sync_detailed(
        client=client,
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
    model_asset_id: Union[None, Unset, int] = UNSET,
    model_area_id: Union[None, Unset, int] = UNSET,
    model_product_id: Union[None, Unset, int] = UNSET,
    model_serial_number: Union[None, Unset, str] = UNSET,
    model_asset_tag: Union[None, Unset, str] = UNSET,
    model_reservation_id: Union[None, Unset, int] = UNSET,
) -> Response[CloseResponse200]:
    """
    Args:
        model_asset_id (Union[None, Unset, int]):
        model_area_id (Union[None, Unset, int]):
        model_product_id (Union[None, Unset, int]):
        model_serial_number (Union[None, Unset, str]):
        model_asset_tag (Union[None, Unset, str]):
        model_reservation_id (Union[None, Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloseResponse200]
    """

    kwargs = _get_kwargs(
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
    model_asset_id: Union[None, Unset, int] = UNSET,
    model_area_id: Union[None, Unset, int] = UNSET,
    model_product_id: Union[None, Unset, int] = UNSET,
    model_serial_number: Union[None, Unset, str] = UNSET,
    model_asset_tag: Union[None, Unset, str] = UNSET,
    model_reservation_id: Union[None, Unset, int] = UNSET,
) -> Optional[CloseResponse200]:
    """
    Args:
        model_asset_id (Union[None, Unset, int]):
        model_area_id (Union[None, Unset, int]):
        model_product_id (Union[None, Unset, int]):
        model_serial_number (Union[None, Unset, str]):
        model_asset_tag (Union[None, Unset, str]):
        model_reservation_id (Union[None, Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloseResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            model_asset_id=model_asset_id,
            model_area_id=model_area_id,
            model_product_id=model_product_id,
            model_serial_number=model_serial_number,
            model_asset_tag=model_asset_tag,
            model_reservation_id=model_reservation_id,
        )
    ).parsed
