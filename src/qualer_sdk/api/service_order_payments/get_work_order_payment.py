from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_service_orders_to_payment_response_model import (
    QualerApiModelsServiceOrdersToPaymentResponseModel,
)
from ...types import Response


def _get_kwargs(
    service_order_payment_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/service/workorders/payments/{service_order_payment_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[QualerApiModelsServiceOrdersToPaymentResponseModel]:
    if response.status_code == 200:
        response_200 = QualerApiModelsServiceOrdersToPaymentResponseModel.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[QualerApiModelsServiceOrdersToPaymentResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_order_payment_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[QualerApiModelsServiceOrdersToPaymentResponseModel]:
    """
    Args:
        service_order_payment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QualerApiModelsServiceOrdersToPaymentResponseModel]
    """

    kwargs = _get_kwargs(
        service_order_payment_id=service_order_payment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_order_payment_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[QualerApiModelsServiceOrdersToPaymentResponseModel]:
    """
    Args:
        service_order_payment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QualerApiModelsServiceOrdersToPaymentResponseModel
    """

    return sync_detailed(
        service_order_payment_id=service_order_payment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_order_payment_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[QualerApiModelsServiceOrdersToPaymentResponseModel]:
    """
    Args:
        service_order_payment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QualerApiModelsServiceOrdersToPaymentResponseModel]
    """

    kwargs = _get_kwargs(
        service_order_payment_id=service_order_payment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_order_payment_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[QualerApiModelsServiceOrdersToPaymentResponseModel]:
    """
    Args:
        service_order_payment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QualerApiModelsServiceOrdersToPaymentResponseModel
    """

    return (
        await asyncio_detailed(
            service_order_payment_id=service_order_payment_id,
            client=client,
        )
    ).parsed
