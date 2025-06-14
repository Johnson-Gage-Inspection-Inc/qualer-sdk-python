from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_service_orders_to_service_order_task_response import (
    QualerApiModelsServiceOrdersToServiceOrderTaskResponse,
)
from ...models.qualer_web_mvc_areas_api_models_service_prices_from_service_price_bulk_edit_model import (
    QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel,
)
from ...types import Response


def _get_kwargs(
    *,
    body: list["QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel"],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/service/pricing",
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                QualerApiModelsServiceOrdersToServiceOrderTaskResponse.from_dict(
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
) -> Response[list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel"],
) -> Response[list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"]]:
    """
    Args:
        body (list['QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsServiceOrdersToServiceOrderTaskResponse']]
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
    body: list["QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel"],
) -> Optional[list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"]]:
    """
    Args:
        body (list['QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsServiceOrdersToServiceOrderTaskResponse']
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel"],
) -> Response[list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"]]:
    """
    Args:
        body (list['QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsServiceOrdersToServiceOrderTaskResponse']]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel"],
) -> Optional[list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"]]:
    """
    Args:
        body (list['QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsServiceOrdersToServiceOrderTaskResponse']
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
