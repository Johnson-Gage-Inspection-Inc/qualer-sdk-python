from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_clients_to_employee_response_model import (
    QualerApiModelsClientsToEmployeeResponseModel,
)
from ...types import Response


def _get_kwargs(
    employee_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/employees/{employee_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[QualerApiModelsClientsToEmployeeResponseModel]:
    if response.status_code == 200:
        response_200 = QualerApiModelsClientsToEmployeeResponseModel.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[QualerApiModelsClientsToEmployeeResponseModel]:
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
) -> Response[QualerApiModelsClientsToEmployeeResponseModel]:
    """
    Args:
        employee_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QualerApiModelsClientsToEmployeeResponseModel]
    """

    kwargs = _get_kwargs(
        employee_id=employee_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    employee_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[QualerApiModelsClientsToEmployeeResponseModel]:
    """
    Args:
        employee_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QualerApiModelsClientsToEmployeeResponseModel
    """

    return sync_detailed(
        employee_id=employee_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    employee_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[QualerApiModelsClientsToEmployeeResponseModel]:
    """
    Args:
        employee_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QualerApiModelsClientsToEmployeeResponseModel]
    """

    kwargs = _get_kwargs(
        employee_id=employee_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    employee_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[QualerApiModelsClientsToEmployeeResponseModel]:
    """
    Args:
        employee_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QualerApiModelsClientsToEmployeeResponseModel
    """

    return (
        await asyncio_detailed(
            employee_id=employee_id,
            client=client,
        )
    ).parsed
