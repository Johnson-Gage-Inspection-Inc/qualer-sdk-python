from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_service_orders_from_add_payment_model import (
    QualerApiModelsServiceOrdersFromAddPaymentModel,
)
from ...models.qualer_api_models_service_orders_to_created_work_order_payment_response import (
    QualerApiModelsServiceOrdersToCreatedWorkOrderPaymentResponse,
)
from ...types import Response


def _get_kwargs(
    service_order_id: int,
    *,
    body: QualerApiModelsServiceOrdersFromAddPaymentModel,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/service/workorders/{service_order_id}/payments",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[QualerApiModelsServiceOrdersToCreatedWorkOrderPaymentResponse]:
    if response.status_code == 200:
        response_200 = QualerApiModelsServiceOrdersToCreatedWorkOrderPaymentResponse.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[QualerApiModelsServiceOrdersToCreatedWorkOrderPaymentResponse]:
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
    body: QualerApiModelsServiceOrdersFromAddPaymentModel,
) -> Response[QualerApiModelsServiceOrdersToCreatedWorkOrderPaymentResponse]:
    """
    Args:
        service_order_id (int):
        body (QualerApiModelsServiceOrdersFromAddPaymentModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QualerApiModelsServiceOrdersToCreatedWorkOrderPaymentResponse]
    """

    kwargs = _get_kwargs(
        service_order_id=service_order_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_order_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsServiceOrdersFromAddPaymentModel,
) -> Optional[QualerApiModelsServiceOrdersToCreatedWorkOrderPaymentResponse]:
    """
    Args:
        service_order_id (int):
        body (QualerApiModelsServiceOrdersFromAddPaymentModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QualerApiModelsServiceOrdersToCreatedWorkOrderPaymentResponse
    """

    return sync_detailed(
        service_order_id=service_order_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    service_order_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsServiceOrdersFromAddPaymentModel,
) -> Response[QualerApiModelsServiceOrdersToCreatedWorkOrderPaymentResponse]:
    """
    Args:
        service_order_id (int):
        body (QualerApiModelsServiceOrdersFromAddPaymentModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QualerApiModelsServiceOrdersToCreatedWorkOrderPaymentResponse]
    """

    kwargs = _get_kwargs(
        service_order_id=service_order_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_order_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsServiceOrdersFromAddPaymentModel,
) -> Optional[QualerApiModelsServiceOrdersToCreatedWorkOrderPaymentResponse]:
    """
    Args:
        service_order_id (int):
        body (QualerApiModelsServiceOrdersFromAddPaymentModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QualerApiModelsServiceOrdersToCreatedWorkOrderPaymentResponse
    """

    return (
        await asyncio_detailed(
            service_order_id=service_order_id,
            client=client,
            body=body,
        )
    ).parsed
