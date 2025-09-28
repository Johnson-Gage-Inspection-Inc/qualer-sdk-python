from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_employee_department_response_204 import AddEmployeeDepartmentResponse204
from ...models.qualer_api_models_employees_from_employee_department_model import (
    EmployeesFromEmployeeDepartmentModel,
)
from ...types import Response


def _get_kwargs(
    employee_id: int,
    *,
    body: EmployeesFromEmployeeDepartmentModel,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/employees/{employee_id}/department",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AddEmployeeDepartmentResponse204, Any]]:
    if response.status_code == 204:
        response_204 = AddEmployeeDepartmentResponse204.from_dict(response.json())

        return response_204
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        response.raise_for_status()
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AddEmployeeDepartmentResponse204, Any]]:
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
    body: EmployeesFromEmployeeDepartmentModel,
) -> Response[Union[AddEmployeeDepartmentResponse204, Any]]:
    """
    Args:
        employee_id (int):
        body (EmployeesFromEmployeeDepartmentModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddEmployeeDepartmentResponse204, Any]]
    """

    kwargs = _get_kwargs(
        employee_id=employee_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    employee_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: EmployeesFromEmployeeDepartmentModel,
) -> Optional[Union[AddEmployeeDepartmentResponse204, Any]]:
    """
    Args:
        employee_id (int):
        body (EmployeesFromEmployeeDepartmentModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddEmployeeDepartmentResponse204, Any]
    """

    return sync_detailed(
        employee_id=employee_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    employee_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: EmployeesFromEmployeeDepartmentModel,
) -> Response[Union[AddEmployeeDepartmentResponse204, Any]]:
    """
    Args:
        employee_id (int):
        body (EmployeesFromEmployeeDepartmentModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddEmployeeDepartmentResponse204, Any]]
    """

    kwargs = _get_kwargs(
        employee_id=employee_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    employee_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: EmployeesFromEmployeeDepartmentModel,
) -> Optional[Union[AddEmployeeDepartmentResponse204, Any]]:
    """
    Args:
        employee_id (int):
        body (EmployeesFromEmployeeDepartmentModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddEmployeeDepartmentResponse204, Any]
    """

    return (
        await asyncio_detailed(
            employee_id=employee_id,
            client=client,
            body=body,
        )
    ).parsed
