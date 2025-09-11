from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_asset_from_update_asset_room_model import (
    QualerApiModelsAssetFromUpdateAssetRoomModel,
)
from ...models.update_asset_room_response_200 import UpdateAssetRoomResponse200
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: QualerApiModelsAssetFromUpdateAssetRoomModel,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/api/assets/{id}/room",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UpdateAssetRoomResponse200]:
    if response.status_code == 200:
        response_200 = UpdateAssetRoomResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UpdateAssetRoomResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsAssetFromUpdateAssetRoomModel,
) -> Response[UpdateAssetRoomResponse200]:
    """
    Args:
        id (int):
        body (QualerApiModelsAssetFromUpdateAssetRoomModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateAssetRoomResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsAssetFromUpdateAssetRoomModel,
) -> Optional[UpdateAssetRoomResponse200]:
    """
    Args:
        id (int):
        body (QualerApiModelsAssetFromUpdateAssetRoomModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateAssetRoomResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsAssetFromUpdateAssetRoomModel,
) -> Response[UpdateAssetRoomResponse200]:
    """
    Args:
        id (int):
        body (QualerApiModelsAssetFromUpdateAssetRoomModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateAssetRoomResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsAssetFromUpdateAssetRoomModel,
) -> Optional[UpdateAssetRoomResponse200]:
    """
    Args:
        id (int):
        body (QualerApiModelsAssetFromUpdateAssetRoomModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateAssetRoomResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
