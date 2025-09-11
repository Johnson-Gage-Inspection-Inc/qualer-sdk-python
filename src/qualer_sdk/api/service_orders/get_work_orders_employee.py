from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_service_orders_to_provider_service_order_response_model import (
    QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel,
)
from ...types import Response


def _get_kwargs(
    employee_id: int,
    *,
    is_internal: Optional[bool] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["isInternal"] = is_internal

    params = {k: v for k, v in params.items() if v is not None and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/employee/{employee_id}/workorders",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.from_dict(
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
) -> Response[List["QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    employee_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    is_internal: Optional[bool] = None,
) -> Response[List["QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel"]]:
    """
    Args:
        employee_id (int):
        is_internal (Optional[bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel']]
    """

    kwargs = _get_kwargs(
        employee_id=employee_id,
        is_internal=is_internal,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    employee_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    is_internal: Optional[bool] = None,
) -> Optional[List["QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel"]]:
    """
    Args:
        employee_id (int):
        is_internal (Optional[bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel']
    """

    return sync_detailed(
        employee_id=employee_id,
        client=client,
        is_internal=is_internal,
    ).parsed


async def asyncio_detailed(
    employee_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    is_internal: Optional[bool] = None,
) -> Response[List["QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel"]]:
    """
    Args:
        employee_id (int):
        is_internal (Optional[bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel']]
    """

    kwargs = _get_kwargs(
        employee_id=employee_id,
        is_internal=is_internal,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    employee_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    is_internal: Optional[bool] = None,
) -> Optional[List["QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel"]]:
    """
    Args:
        employee_id (int):
        is_internal (Optional[bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel']
    """

    return (
        await asyncio_detailed(
            employee_id=employee_id,
            client=client,
            is_internal=is_internal,
        )
    ).parsed
