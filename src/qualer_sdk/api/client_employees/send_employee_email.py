from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_clients_from_send_employee_email_model import (
    QualerApiModelsClientsFromSendEmployeeEmailModel,
)
from ...models.send_employee_email_response_200 import SendEmployeeEmailResponse200
from ...types import Response


def _get_kwargs(
    employee_id: int,
    *,
    body: QualerApiModelsClientsFromSendEmployeeEmailModel,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/service/clients/employees/{employee_id}/sendemail",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SendEmployeeEmailResponse200]:
    if response.status_code == 200:
        response_200 = SendEmployeeEmailResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SendEmployeeEmailResponse200]:
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
    body: QualerApiModelsClientsFromSendEmployeeEmailModel,
) -> Response[SendEmployeeEmailResponse200]:
    """
    Args:
        employee_id (int):
        body (QualerApiModelsClientsFromSendEmployeeEmailModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SendEmployeeEmailResponse200]
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
    body: QualerApiModelsClientsFromSendEmployeeEmailModel,
) -> Optional[SendEmployeeEmailResponse200]:
    """
    Args:
        employee_id (int):
        body (QualerApiModelsClientsFromSendEmployeeEmailModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SendEmployeeEmailResponse200
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
    body: QualerApiModelsClientsFromSendEmployeeEmailModel,
) -> Response[SendEmployeeEmailResponse200]:
    """
    Args:
        employee_id (int):
        body (QualerApiModelsClientsFromSendEmployeeEmailModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SendEmployeeEmailResponse200]
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
    body: QualerApiModelsClientsFromSendEmployeeEmailModel,
) -> Optional[SendEmployeeEmailResponse200]:
    """
    Args:
        employee_id (int):
        body (QualerApiModelsClientsFromSendEmployeeEmailModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SendEmployeeEmailResponse200
    """

    return (
        await asyncio_detailed(
            employee_id=employee_id,
            client=client,
            body=body,
        )
    ).parsed
