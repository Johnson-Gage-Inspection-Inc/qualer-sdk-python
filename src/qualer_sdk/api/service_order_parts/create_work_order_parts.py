from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_work_order_parts_response_204 import CreateWorkOrderPartsResponse204
from ...models.qualer_web_mvc_areas_api_models_service_orders_from_service_order_part_repair_create_model import (
    QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel,
)
from ...types import Response


def _get_kwargs(
    service_order_id: int,
    *,
    body: QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/service/workorders/{service_order_id}/parts",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateWorkOrderPartsResponse204]]:
    if response.status_code == 204:
        response_204 = CreateWorkOrderPartsResponse204.from_dict(response.json())

        return response_204
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        response.raise_for_status()
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, CreateWorkOrderPartsResponse204]]:
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
    body: QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel,
) -> Response[Union[Any, CreateWorkOrderPartsResponse204]]:
    """ServiceOrderChargeType: Part, Labor, Charge

    Args:
        service_order_id (int):
        body (QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateWorkOrderPartsResponse204]]
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
    body: QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel,
) -> Optional[Union[Any, CreateWorkOrderPartsResponse204]]:
    """ServiceOrderChargeType: Part, Labor, Charge

    Args:
        service_order_id (int):
        body (QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateWorkOrderPartsResponse204]
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
    body: QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel,
) -> Response[Union[Any, CreateWorkOrderPartsResponse204]]:
    """ServiceOrderChargeType: Part, Labor, Charge

    Args:
        service_order_id (int):
        body (QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateWorkOrderPartsResponse204]]
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
    body: QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel,
) -> Optional[Union[Any, CreateWorkOrderPartsResponse204]]:
    """ServiceOrderChargeType: Part, Labor, Charge

    Args:
        service_order_id (int):
        body (QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateWorkOrderPartsResponse204]
    """

    return (
        await asyncio_detailed(
            service_order_id=service_order_id,
            client=client,
            body=body,
        )
    ).parsed
