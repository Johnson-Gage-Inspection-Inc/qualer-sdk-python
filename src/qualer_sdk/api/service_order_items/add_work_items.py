from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_service_orders_from_add_work_items_model import (
    QualerApiModelsServiceOrdersFromAddWorkItemsModel,
)
from ...models.qualer_api_models_service_orders_to_asset_add_result_response_model import (
    QualerApiModelsServiceOrdersToAssetAddResultResponseModel,
)
from ...types import Response


def _get_kwargs(
    service_order_id: int,
    *,
    body: QualerApiModelsServiceOrdersFromAddWorkItemsModel,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/service/workorders/{service_order_id}/workitems",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, QualerApiModelsServiceOrdersToAssetAddResultResponseModel]]:
    if response.status_code == 200:
        response_200 = (
            QualerApiModelsServiceOrdersToAssetAddResultResponseModel.from_dict(
                response.json()
            )
        )

        return response_200
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, QualerApiModelsServiceOrdersToAssetAddResultResponseModel]]:
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
    body: QualerApiModelsServiceOrdersFromAddWorkItemsModel,
) -> Response[Union[Any, QualerApiModelsServiceOrdersToAssetAddResultResponseModel]]:
    """Add work items

    Args:
        service_order_id (int):
        body (QualerApiModelsServiceOrdersFromAddWorkItemsModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, QualerApiModelsServiceOrdersToAssetAddResultResponseModel]]
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
    body: QualerApiModelsServiceOrdersFromAddWorkItemsModel,
) -> Optional[Union[Any, QualerApiModelsServiceOrdersToAssetAddResultResponseModel]]:
    """Add work items

    Args:
        service_order_id (int):
        body (QualerApiModelsServiceOrdersFromAddWorkItemsModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, QualerApiModelsServiceOrdersToAssetAddResultResponseModel]
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
    body: QualerApiModelsServiceOrdersFromAddWorkItemsModel,
) -> Response[Union[Any, QualerApiModelsServiceOrdersToAssetAddResultResponseModel]]:
    """Add work items

    Args:
        service_order_id (int):
        body (QualerApiModelsServiceOrdersFromAddWorkItemsModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, QualerApiModelsServiceOrdersToAssetAddResultResponseModel]]
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
    body: QualerApiModelsServiceOrdersFromAddWorkItemsModel,
) -> Optional[Union[Any, QualerApiModelsServiceOrdersToAssetAddResultResponseModel]]:
    """Add work items

    Args:
        service_order_id (int):
        body (QualerApiModelsServiceOrdersFromAddWorkItemsModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, QualerApiModelsServiceOrdersToAssetAddResultResponseModel]
    """

    return (
        await asyncio_detailed(
            service_order_id=service_order_id,
            client=client,
            body=body,
        )
    ).parsed
