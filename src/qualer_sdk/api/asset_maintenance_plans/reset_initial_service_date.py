from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_asset_from_update_asset_maintenance_service_dat import (
    QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat,
)
from ...models.reset_initial_service_date_response_200 import (
    ResetInitialServiceDateResponse200,
)
from ...types import Response


def _get_kwargs(
    asset_id: int,
    maintenance_plan_id: int,
    *,
    body: QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/assets/{asset_id}/plans/{maintenance_plan_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ResetInitialServiceDateResponse200]:
    if response.status_code == 200:
        response_200 = ResetInitialServiceDateResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ResetInitialServiceDateResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: int,
    maintenance_plan_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat,
) -> Response[ResetInitialServiceDateResponse200]:
    """
    Args:
        asset_id (int):
        maintenance_plan_id (int):
        body (QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResetInitialServiceDateResponse200]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        maintenance_plan_id=maintenance_plan_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: int,
    maintenance_plan_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat,
) -> Optional[ResetInitialServiceDateResponse200]:
    """
    Args:
        asset_id (int):
        maintenance_plan_id (int):
        body (QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResetInitialServiceDateResponse200
    """

    return sync_detailed(
        asset_id=asset_id,
        maintenance_plan_id=maintenance_plan_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    asset_id: int,
    maintenance_plan_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat,
) -> Response[ResetInitialServiceDateResponse200]:
    """
    Args:
        asset_id (int):
        maintenance_plan_id (int):
        body (QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResetInitialServiceDateResponse200]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        maintenance_plan_id=maintenance_plan_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: int,
    maintenance_plan_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat,
) -> Optional[ResetInitialServiceDateResponse200]:
    """
    Args:
        asset_id (int):
        maintenance_plan_id (int):
        body (QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResetInitialServiceDateResponse200
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            maintenance_plan_id=maintenance_plan_id,
            client=client,
            body=body,
        )
    ).parsed
