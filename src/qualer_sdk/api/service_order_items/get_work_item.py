from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_service_orders_to_client_order_item_response_model import (
    QualerApiModelsServiceOrdersToClientOrderItemResponseModel,
)
from ...types import Response


def _get_kwargs(
    work_item_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/service/workitems/{work_item_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[QualerApiModelsServiceOrdersToClientOrderItemResponseModel]:
    if response.status_code == 200:
        response_200 = (
            QualerApiModelsServiceOrdersToClientOrderItemResponseModel.from_dict(
                response.json()
            )
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[QualerApiModelsServiceOrdersToClientOrderItemResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    work_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[QualerApiModelsServiceOrdersToClientOrderItemResponseModel]:
    """
    Args:
        work_item_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QualerApiModelsServiceOrdersToClientOrderItemResponseModel]
    """

    kwargs = _get_kwargs(
        work_item_id=work_item_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    work_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[QualerApiModelsServiceOrdersToClientOrderItemResponseModel]:
    """
    Args:
        work_item_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QualerApiModelsServiceOrdersToClientOrderItemResponseModel
    """

    return sync_detailed(
        work_item_id=work_item_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    work_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[QualerApiModelsServiceOrdersToClientOrderItemResponseModel]:
    """
    Args:
        work_item_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QualerApiModelsServiceOrdersToClientOrderItemResponseModel]
    """

    kwargs = _get_kwargs(
        work_item_id=work_item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    work_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[QualerApiModelsServiceOrdersToClientOrderItemResponseModel]:
    """
    Args:
        work_item_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QualerApiModelsServiceOrdersToClientOrderItemResponseModel
    """

    return (
        await asyncio_detailed(
            work_item_id=work_item_id,
            client=client,
        )
    ).parsed
