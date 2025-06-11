from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_asset_reservation_from_upsert_asset_reservation_model import (
    QualerApiModelsAssetReservationFromUpsertAssetReservationModel,
)
from ...models.qualer_api_models_asset_reservation_to_upsert_asset_reservation_response import (
    QualerApiModelsAssetReservationToUpsertAssetReservationResponse,
)
from ...types import Response


def _get_kwargs(
    *,
    body: QualerApiModelsAssetReservationFromUpsertAssetReservationModel,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/assetsreservations",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[QualerApiModelsAssetReservationToUpsertAssetReservationResponse]:
    if response.status_code == 200:
        response_200 = (
            QualerApiModelsAssetReservationToUpsertAssetReservationResponse.from_dict(
                response.json()
            )
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[QualerApiModelsAssetReservationToUpsertAssetReservationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsAssetReservationFromUpsertAssetReservationModel,
) -> Response[QualerApiModelsAssetReservationToUpsertAssetReservationResponse]:
    """
    Args:
        body (QualerApiModelsAssetReservationFromUpsertAssetReservationModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QualerApiModelsAssetReservationToUpsertAssetReservationResponse]
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
    body: QualerApiModelsAssetReservationFromUpsertAssetReservationModel,
) -> Optional[QualerApiModelsAssetReservationToUpsertAssetReservationResponse]:
    """
    Args:
        body (QualerApiModelsAssetReservationFromUpsertAssetReservationModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QualerApiModelsAssetReservationToUpsertAssetReservationResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsAssetReservationFromUpsertAssetReservationModel,
) -> Response[QualerApiModelsAssetReservationToUpsertAssetReservationResponse]:
    """
    Args:
        body (QualerApiModelsAssetReservationFromUpsertAssetReservationModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QualerApiModelsAssetReservationToUpsertAssetReservationResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsAssetReservationFromUpsertAssetReservationModel,
) -> Optional[QualerApiModelsAssetReservationToUpsertAssetReservationResponse]:
    """
    Args:
        body (QualerApiModelsAssetReservationFromUpsertAssetReservationModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QualerApiModelsAssetReservationToUpsertAssetReservationResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
