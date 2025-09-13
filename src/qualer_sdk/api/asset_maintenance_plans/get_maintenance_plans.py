from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_asset_to_asset_maintenance_plan_model import (
    AssetToAssetMaintenancePlanModel,
)
from ...types import Response


def _get_kwargs(
    asset_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/assets/{asset_id}/plans",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AssetToAssetMaintenancePlanModel]:
    if response.status_code == 200:
        response_200 = AssetToAssetMaintenancePlanModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AssetToAssetMaintenancePlanModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AssetToAssetMaintenancePlanModel]:
    """
    Args:
        asset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetToAssetMaintenancePlanModel]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AssetToAssetMaintenancePlanModel]:
    """
    Args:
        asset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetToAssetMaintenancePlanModel
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    asset_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AssetToAssetMaintenancePlanModel]:
    """
    Args:
        asset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetToAssetMaintenancePlanModel]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AssetToAssetMaintenancePlanModel]:
    """
    Args:
        asset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetToAssetMaintenancePlanModel
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
        )
    ).parsed
