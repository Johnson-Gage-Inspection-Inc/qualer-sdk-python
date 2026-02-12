from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_employee_department_response_204 import DeleteEmployeeDepartmentResponse204
from ...types import Response


def _get_kwargs(
    employee_id: int,
    department_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/api/employees/{employee_id}/department/{department_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DeleteEmployeeDepartmentResponse204]:
    if response.status_code == 204:
        response_204 = DeleteEmployeeDepartmentResponse204.from_dict(response.json())

        return response_204
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DeleteEmployeeDepartmentResponse204]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    employee_id: int,
    department_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DeleteEmployeeDepartmentResponse204]:
    """
    Args:
        employee_id (int):
        department_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteEmployeeDepartmentResponse204]
    """

    kwargs = _get_kwargs(
        employee_id=employee_id,
        department_id=department_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    employee_id: int,
    department_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[DeleteEmployeeDepartmentResponse204]:
    """
    Args:
        employee_id (int):
        department_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteEmployeeDepartmentResponse204
    """

    return sync_detailed(
        employee_id=employee_id,
        department_id=department_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    employee_id: int,
    department_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DeleteEmployeeDepartmentResponse204]:
    """
    Args:
        employee_id (int):
        department_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteEmployeeDepartmentResponse204]
    """

    kwargs = _get_kwargs(
        employee_id=employee_id,
        department_id=department_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    employee_id: int,
    department_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[DeleteEmployeeDepartmentResponse204]:
    """
    Args:
        employee_id (int):
        department_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteEmployeeDepartmentResponse204
    """

    return (
        await asyncio_detailed(
            employee_id=employee_id,
            department_id=department_id,
            client=client,
        )
    ).parsed
