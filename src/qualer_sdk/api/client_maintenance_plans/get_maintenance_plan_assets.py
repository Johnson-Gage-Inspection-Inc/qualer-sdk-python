from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_asset_to_asset_forecast_api_response_model import (
    QualerApiModelsAssetToAssetForecastApiResponseModel,
)
from ...types import Response


def _get_kwargs(
    maintenance_plan_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/service/clients/plans/{maintenance_plan_id}/assets",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["QualerApiModelsAssetToAssetForecastApiResponseModel"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                QualerApiModelsAssetToAssetForecastApiResponseModel.from_dict(
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
) -> Response[list["QualerApiModelsAssetToAssetForecastApiResponseModel"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    maintenance_plan_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[list["QualerApiModelsAssetToAssetForecastApiResponseModel"]]:
    """
    Args:
        maintenance_plan_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsAssetToAssetForecastApiResponseModel']]
    """

    kwargs = _get_kwargs(
        maintenance_plan_id=maintenance_plan_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    maintenance_plan_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[list["QualerApiModelsAssetToAssetForecastApiResponseModel"]]:
    """
    Args:
        maintenance_plan_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsAssetToAssetForecastApiResponseModel']
    """

    return sync_detailed(
        maintenance_plan_id=maintenance_plan_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    maintenance_plan_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[list["QualerApiModelsAssetToAssetForecastApiResponseModel"]]:
    """
    Args:
        maintenance_plan_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsAssetToAssetForecastApiResponseModel']]
    """

    kwargs = _get_kwargs(
        maintenance_plan_id=maintenance_plan_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    maintenance_plan_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[list["QualerApiModelsAssetToAssetForecastApiResponseModel"]]:
    """
    Args:
        maintenance_plan_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsAssetToAssetForecastApiResponseModel']
    """

    return (
        await asyncio_detailed(
            maintenance_plan_id=maintenance_plan_id,
            client=client,
        )
    ).parsed
