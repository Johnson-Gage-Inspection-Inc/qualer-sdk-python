from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_service_orders_from_service_order_task_update_model import (
    ServiceOrdersFromServiceOrderTaskUpdateModel,
)
from ...models.update_work_order_task_response_204 import UpdateWorkOrderTaskResponse204
from ...types import Response


def _get_kwargs(
    service_order_id: int,
    *,
    body: ServiceOrdersFromServiceOrderTaskUpdateModel,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/api/service/workorders/{service_order_id}/tasks",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UpdateWorkOrderTaskResponse204]:
    if response.status_code == 204:
        response_204 = UpdateWorkOrderTaskResponse204.from_dict(response.json())

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
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UpdateWorkOrderTaskResponse204]:
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
    body: ServiceOrdersFromServiceOrderTaskUpdateModel,
) -> Response[UpdateWorkOrderTaskResponse204]:
    """- If StartTime and FinishTime are defined TimeSpent will be ignored and recalculated based on their
    difference
    - If StartTime and FinishTime are not defined they will be recalculated
        - if StartTime - in will be recalculated FinishTime - TimeSpent
        - if FinishTime - in will be recalculated StartTime + TimeSpent

    Args:
        service_order_id (int):
        body (ServiceOrdersFromServiceOrderTaskUpdateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateWorkOrderTaskResponse204]
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
    body: ServiceOrdersFromServiceOrderTaskUpdateModel,
) -> Optional[UpdateWorkOrderTaskResponse204]:
    """- If StartTime and FinishTime are defined TimeSpent will be ignored and recalculated based on their
    difference
    - If StartTime and FinishTime are not defined they will be recalculated
        - if StartTime - in will be recalculated FinishTime - TimeSpent
        - if FinishTime - in will be recalculated StartTime + TimeSpent

    Args:
        service_order_id (int):
        body (ServiceOrdersFromServiceOrderTaskUpdateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateWorkOrderTaskResponse204
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
    body: ServiceOrdersFromServiceOrderTaskUpdateModel,
) -> Response[UpdateWorkOrderTaskResponse204]:
    """- If StartTime and FinishTime are defined TimeSpent will be ignored and recalculated based on their
    difference
    - If StartTime and FinishTime are not defined they will be recalculated
        - if StartTime - in will be recalculated FinishTime - TimeSpent
        - if FinishTime - in will be recalculated StartTime + TimeSpent

    Args:
        service_order_id (int):
        body (ServiceOrdersFromServiceOrderTaskUpdateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateWorkOrderTaskResponse204]
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
    body: ServiceOrdersFromServiceOrderTaskUpdateModel,
) -> Optional[UpdateWorkOrderTaskResponse204]:
    """- If StartTime and FinishTime are defined TimeSpent will be ignored and recalculated based on their
    difference
    - If StartTime and FinishTime are not defined they will be recalculated
        - if StartTime - in will be recalculated FinishTime - TimeSpent
        - if FinishTime - in will be recalculated StartTime + TimeSpent

    Args:
        service_order_id (int):
        body (ServiceOrdersFromServiceOrderTaskUpdateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateWorkOrderTaskResponse204
    """

    return (
        await asyncio_detailed(
            service_order_id=service_order_id,
            client=client,
            body=body,
        )
    ).parsed
