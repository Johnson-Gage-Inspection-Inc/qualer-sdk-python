from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_report_datasets_to_service_order_item_task_response import (
    QualerApiModelsReportDatasetsToServiceOrderItemTaskResponse,
)
from ...types import Response


def _get_kwargs(
    service_order_item_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/data/ServiceOrderItemTasksByOrderItem/{service_order_item_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["QualerApiModelsReportDatasetsToServiceOrderItemTaskResponse"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                QualerApiModelsReportDatasetsToServiceOrderItemTaskResponse.from_dict(
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
) -> Response[list["QualerApiModelsReportDatasetsToServiceOrderItemTaskResponse"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_order_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[list["QualerApiModelsReportDatasetsToServiceOrderItemTaskResponse"]]:
    """
    Args:
        service_order_item_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsReportDatasetsToServiceOrderItemTaskResponse']]
    """

    kwargs = _get_kwargs(
        service_order_item_id=service_order_item_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_order_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[list["QualerApiModelsReportDatasetsToServiceOrderItemTaskResponse"]]:
    """
    Args:
        service_order_item_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsReportDatasetsToServiceOrderItemTaskResponse']
    """

    return sync_detailed(
        service_order_item_id=service_order_item_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_order_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[list["QualerApiModelsReportDatasetsToServiceOrderItemTaskResponse"]]:
    """
    Args:
        service_order_item_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsReportDatasetsToServiceOrderItemTaskResponse']]
    """

    kwargs = _get_kwargs(
        service_order_item_id=service_order_item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_order_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[list["QualerApiModelsReportDatasetsToServiceOrderItemTaskResponse"]]:
    """
    Args:
        service_order_item_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsReportDatasetsToServiceOrderItemTaskResponse']
    """

    return (
        await asyncio_detailed(
            service_order_item_id=service_order_item_id,
            client=client,
        )
    ).parsed
