from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_report_datasets_to_client_attribute_response import (
    ReportDatasetsToClientAttributeResponse,
)
from ...types import Response


def _get_kwargs(
    service_order_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/data/ClientAttributes/{service_order_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ReportDatasetsToClientAttributeResponse]:
    if response.status_code == 200:
        response_200 = ReportDatasetsToClientAttributeResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        response.raise_for_status()
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ReportDatasetsToClientAttributeResponse]:
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
) -> Response[ReportDatasetsToClientAttributeResponse]:
    """
    Args:
        service_order_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReportDatasetsToClientAttributeResponse]
    """

    kwargs = _get_kwargs(
        service_order_id=service_order_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_order_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ReportDatasetsToClientAttributeResponse]:
    """
    Args:
        service_order_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReportDatasetsToClientAttributeResponse
    """

    return sync_detailed(
        service_order_id=service_order_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_order_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ReportDatasetsToClientAttributeResponse]:
    """
    Args:
        service_order_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReportDatasetsToClientAttributeResponse]
    """

    kwargs = _get_kwargs(
        service_order_id=service_order_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_order_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ReportDatasetsToClientAttributeResponse]:
    """
    Args:
        service_order_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReportDatasetsToClientAttributeResponse
    """

    return (
        await asyncio_detailed(
            service_order_id=service_order_id,
            client=client,
        )
    ).parsed
