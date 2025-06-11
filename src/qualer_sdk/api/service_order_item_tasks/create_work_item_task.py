from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_work_item_task_response_200 import CreateWorkItemTaskResponse200
from ...models.qualer_api_models_service_order_item_tasks_from_service_order_item_task_create_model import (
    QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel,
)
from ...types import Response


def _get_kwargs(
    work_item_id: int,
    *,
    body: QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/service/workitems/{work_item_id}/tasks",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CreateWorkItemTaskResponse200]:
    if response.status_code == 200:
        response_200 = CreateWorkItemTaskResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CreateWorkItemTaskResponse200]:
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
    body: QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel,
) -> Response[CreateWorkItemTaskResponse200]:
    """
    Args:
        work_item_id (int):
        body (QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWorkItemTaskResponse200]
    """

    kwargs = _get_kwargs(
        work_item_id=work_item_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    work_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel,
) -> Optional[CreateWorkItemTaskResponse200]:
    """
    Args:
        work_item_id (int):
        body (QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWorkItemTaskResponse200
    """

    return sync_detailed(
        work_item_id=work_item_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    work_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel,
) -> Response[CreateWorkItemTaskResponse200]:
    """
    Args:
        work_item_id (int):
        body (QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWorkItemTaskResponse200]
    """

    kwargs = _get_kwargs(
        work_item_id=work_item_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    work_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel,
) -> Optional[CreateWorkItemTaskResponse200]:
    """
    Args:
        work_item_id (int):
        body (QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWorkItemTaskResponse200
    """

    return (
        await asyncio_detailed(
            work_item_id=work_item_id,
            client=client,
            body=body,
        )
    ).parsed
