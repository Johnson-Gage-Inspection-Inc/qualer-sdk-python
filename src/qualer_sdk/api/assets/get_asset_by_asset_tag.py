from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_asset_to_asset_response_model import (
    QualerApiModelsAssetToAssetResponseModel,
)
from ...types import Response


def _get_kwargs(
    asset_tag: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/assets/byassettag/{asset_tag}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["QualerApiModelsAssetToAssetResponseModel"]]:
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
) -> Response[list["QualerApiModelsAssetToAssetResponseModel"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_tag: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[list["QualerApiModelsAssetToAssetResponseModel"]]:
    """
    Args:
        asset_tag (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsAssetToAssetResponseModel']]
    """

    kwargs = _get_kwargs(
        asset_tag=asset_tag,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_tag: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[list["QualerApiModelsAssetToAssetResponseModel"]]:
    """
    Args:
        asset_tag (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsAssetToAssetResponseModel']
    """

    return sync_detailed(
        asset_tag=asset_tag,
        client=client,
    ).parsed


async def asyncio_detailed(
    asset_tag: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[list["QualerApiModelsAssetToAssetResponseModel"]]:
    """
    Args:
        asset_tag (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsAssetToAssetResponseModel']]
    """

    kwargs = _get_kwargs(
        asset_tag=asset_tag,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_tag: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[list["QualerApiModelsAssetToAssetResponseModel"]]:
    """
    Args:
        asset_tag (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsAssetToAssetResponseModel']
    """

    return (
        await asyncio_detailed(
            asset_tag=asset_tag,
            client=client,
        )
    ).parsed
