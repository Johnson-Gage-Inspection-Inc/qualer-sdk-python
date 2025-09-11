from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_asset_to_asset_response_model import (
    QualerApiModelsAssetToAssetResponseModel,
)
from ...types import Response


def _get_kwargs(
    serial_number: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/assets/byserialnumber/{serial_number}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["QualerApiModelsAssetToAssetResponseModel"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = QualerApiModelsAssetToAssetResponseModel.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["QualerApiModelsAssetToAssetResponseModel"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    serial_number: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[List["QualerApiModelsAssetToAssetResponseModel"]]:
    """
    Args:
        serial_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['QualerApiModelsAssetToAssetResponseModel']]
    """

    kwargs = _get_kwargs(
        serial_number=serial_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    serial_number: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[List["QualerApiModelsAssetToAssetResponseModel"]]:
    """
    Args:
        serial_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['QualerApiModelsAssetToAssetResponseModel']
    """

    return sync_detailed(
        serial_number=serial_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    serial_number: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[List["QualerApiModelsAssetToAssetResponseModel"]]:
    """
    Args:
        serial_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['QualerApiModelsAssetToAssetResponseModel']]
    """

    kwargs = _get_kwargs(
        serial_number=serial_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    serial_number: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[List["QualerApiModelsAssetToAssetResponseModel"]]:
    """
    Args:
        serial_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['QualerApiModelsAssetToAssetResponseModel']
    """

    return (
        await asyncio_detailed(
            serial_number=serial_number,
            client=client,
        )
    ).parsed
