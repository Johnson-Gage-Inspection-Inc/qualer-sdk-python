from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_service_orders_to_service_order_task_response import (
    QualerApiModelsServiceOrdersToServiceOrderTaskResponse,
)
from ...types import Response


def _get_kwargs(
    service_order_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/service/workorders/{service_order_id}/tasks",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[Any, list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"]]
]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                QualerApiModelsServiceOrdersToServiceOrderTaskResponse.from_dict(
                    response_200_item_data
                )
            )

            response_200.append(response_200_item)

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
) -> Response[
    Union[Any, list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"]]
]:
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
) -> Response[
    Union[Any, list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"]]
]:
    """TimeSpent
    Integer part (before dot) is hours
    Fractional part (after dot) is minutes
    For example:
        if time spent is 10 minutes -&gt; 10 / 60 = 0.1666666666666667
        if time spent is 65 minutes -&gt; (65 - 60) + (5 / 60) = 1.0833333333333333

    Args:
        service_order_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['QualerApiModelsServiceOrdersToServiceOrderTaskResponse']]]
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
) -> Optional[
    Union[Any, list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"]]
]:
    """TimeSpent
    Integer part (before dot) is hours
    Fractional part (after dot) is minutes
    For example:
        if time spent is 10 minutes -&gt; 10 / 60 = 0.1666666666666667
        if time spent is 65 minutes -&gt; (65 - 60) + (5 / 60) = 1.0833333333333333

    Args:
        service_order_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['QualerApiModelsServiceOrdersToServiceOrderTaskResponse']]
    """

    return sync_detailed(
        service_order_id=service_order_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_order_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[Any, list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"]]
]:
    """TimeSpent
    Integer part (before dot) is hours
    Fractional part (after dot) is minutes
    For example:
        if time spent is 10 minutes -&gt; 10 / 60 = 0.1666666666666667
        if time spent is 65 minutes -&gt; (65 - 60) + (5 / 60) = 1.0833333333333333

    Args:
        service_order_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['QualerApiModelsServiceOrdersToServiceOrderTaskResponse']]]
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
) -> Optional[
    Union[Any, list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"]]
]:
    """TimeSpent
    Integer part (before dot) is hours
    Fractional part (after dot) is minutes
    For example:
        if time spent is 10 minutes -&gt; 10 / 60 = 0.1666666666666667
        if time spent is 65 minutes -&gt; (65 - 60) + (5 / 60) = 1.0833333333333333

    Args:
        service_order_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['QualerApiModelsServiceOrdersToServiceOrderTaskResponse']]
    """

    return (
        await asyncio_detailed(
            service_order_id=service_order_id,
            client=client,
        )
    ).parsed
