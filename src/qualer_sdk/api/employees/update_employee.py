from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_employees_from_update_employee_model import (
    EmployeesFromUpdateEmployeeModel,
)
from ...models.update_employee_response_201 import UpdateEmployeeResponse201
from ...types import Response


def _get_kwargs(
    employee_id: int,
    *,
    body: EmployeesFromUpdateEmployeeModel,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/api/employees/{employee_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateEmployeeResponse201]]:
    if response.status_code == 201:
        response_201 = UpdateEmployeeResponse201.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        response.raise_for_status()
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, UpdateEmployeeResponse201]]:
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
    body: EmployeesFromUpdateEmployeeModel,
) -> Response[Union[Any, UpdateEmployeeResponse201]]:
    r"""Update Employee

     CultureName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\".<br />
    CultureUiName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\"<br />
    List of culture codes: GET /api/common/culturelist\"
    List of UI culture codes: GET /api/common/cultureuilist\"

    Args:
        employee_id (int):
        body (EmployeesFromUpdateEmployeeModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateEmployeeResponse201]]
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
    body: EmployeesFromUpdateEmployeeModel,
) -> Optional[Union[Any, UpdateEmployeeResponse201]]:
    r"""Update Employee

     CultureName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\".<br />
    CultureUiName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\"<br />
    List of culture codes: GET /api/common/culturelist\"
    List of UI culture codes: GET /api/common/cultureuilist\"

    Args:
        employee_id (int):
        body (EmployeesFromUpdateEmployeeModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateEmployeeResponse201]
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
    body: EmployeesFromUpdateEmployeeModel,
) -> Response[Union[Any, UpdateEmployeeResponse201]]:
    r"""Update Employee

     CultureName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\".<br />
    CultureUiName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\"<br />
    List of culture codes: GET /api/common/culturelist\"
    List of UI culture codes: GET /api/common/cultureuilist\"

    Args:
        employee_id (int):
        body (EmployeesFromUpdateEmployeeModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateEmployeeResponse201]]
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
    body: EmployeesFromUpdateEmployeeModel,
) -> Optional[Union[Any, UpdateEmployeeResponse201]]:
    r"""Update Employee

     CultureName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\".<br />
    CultureUiName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\"<br />
    List of culture codes: GET /api/common/culturelist\"
    List of UI culture codes: GET /api/common/cultureuilist\"

    Args:
        employee_id (int):
        body (EmployeesFromUpdateEmployeeModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateEmployeeResponse201]
    """

    return (
        await asyncio_detailed(
            employee_id=employee_id,
            client=client,
            body=body,
        )
    ).parsed
