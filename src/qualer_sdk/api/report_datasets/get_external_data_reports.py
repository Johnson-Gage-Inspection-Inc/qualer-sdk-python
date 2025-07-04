from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_report_datasets_to_external_data_report_response import (
    QualerApiModelsReportDatasetsToExternalDataReportResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    service_order_id: int,
    *,
    service_order_item_ids: list[int],
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_service_order_item_ids = service_order_item_ids

    params["serviceOrderItemIds"] = json_service_order_item_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/data/{service_order_id}/ExternalDataReports",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["QualerApiModelsReportDatasetsToExternalDataReportResponse"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                QualerApiModelsReportDatasetsToExternalDataReportResponse.from_dict(
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
) -> Response[list["QualerApiModelsReportDatasetsToExternalDataReportResponse"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_order_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    service_order_item_ids: list[int],
) -> Response[list["QualerApiModelsReportDatasetsToExternalDataReportResponse"]]:
    """
    Args:
        service_order_id (int):
        service_order_item_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsReportDatasetsToExternalDataReportResponse']]
    """

    kwargs = _get_kwargs(
        service_order_id=service_order_id,
        service_order_item_ids=service_order_item_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_order_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    service_order_item_ids: list[int],
) -> Optional[list["QualerApiModelsReportDatasetsToExternalDataReportResponse"]]:
    """
    Args:
        service_order_id (int):
        service_order_item_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsReportDatasetsToExternalDataReportResponse']
    """

    return sync_detailed(
        service_order_id=service_order_id,
        client=client,
        service_order_item_ids=service_order_item_ids,
    ).parsed


async def asyncio_detailed(
    service_order_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    service_order_item_ids: list[int],
) -> Response[list["QualerApiModelsReportDatasetsToExternalDataReportResponse"]]:
    """
    Args:
        service_order_id (int):
        service_order_item_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsReportDatasetsToExternalDataReportResponse']]
    """

    kwargs = _get_kwargs(
        service_order_id=service_order_id,
        service_order_item_ids=service_order_item_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_order_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    service_order_item_ids: list[int],
) -> Optional[list["QualerApiModelsReportDatasetsToExternalDataReportResponse"]]:
    """
    Args:
        service_order_id (int):
        service_order_item_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsReportDatasetsToExternalDataReportResponse']
    """

    return (
        await asyncio_detailed(
            service_order_id=service_order_id,
            client=client,
            service_order_item_ids=service_order_item_ids,
        )
    ).parsed
