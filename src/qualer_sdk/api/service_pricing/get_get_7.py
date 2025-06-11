from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_service_orders_to_service_order_task_response import (
    QualerApiModelsServiceOrdersToServiceOrderTaskResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    service_pricing_id: int,
    service_group_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["servicePricingId"] = service_pricing_id

    params["serviceGroupId"] = service_group_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/service/pricing",
        "params": params,
    }

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
    service_pricing_id: int,
    service_group_id: Union[Unset, int] = UNSET,
) -> Response[list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"]]:
    """
    Args:
        service_pricing_id (int):
        service_group_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsServiceOrdersToServiceOrderTaskResponse']]
    """

    kwargs = _get_kwargs(
        service_pricing_id=service_pricing_id,
        service_group_id=service_group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    service_pricing_id: int,
    service_group_id: Union[Unset, int] = UNSET,
) -> Optional[list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"]]:
    """
    Args:
        service_pricing_id (int):
        service_group_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsServiceOrdersToServiceOrderTaskResponse']
    """

    return sync_detailed(
        client=client,
        service_pricing_id=service_pricing_id,
        service_group_id=service_group_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    service_pricing_id: int,
    service_group_id: Union[Unset, int] = UNSET,
) -> Response[list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"]]:
    """
    Args:
        service_pricing_id (int):
        service_group_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsServiceOrdersToServiceOrderTaskResponse']]
    """

    kwargs = _get_kwargs(
        service_pricing_id=service_pricing_id,
        service_group_id=service_group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    service_pricing_id: int,
    service_group_id: Union[Unset, int] = UNSET,
) -> Optional[list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"]]:
    """
    Args:
        service_pricing_id (int):
        service_group_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsServiceOrdersToServiceOrderTaskResponse']
    """

    return (
        await asyncio_detailed(
            client=client,
            service_pricing_id=service_pricing_id,
            service_group_id=service_group_id,
        )
    ).parsed
