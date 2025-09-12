from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_employee_response_200 import CreateEmployeeResponse200
from ...models.qualer_api_models_clients_from_sponsored_employee_model import (
    QualerApiModelsClientsFromSponsoredEmployeeModel,
)
from ...models.qualer_api_models_clients_to_created_client_employee_response import (
    QualerApiModelsClientsToCreatedClientEmployeeResponse,
)
from ...types import Response


def _get_kwargs(
    *,
    body: QualerApiModelsClientsFromSponsoredEmployeeModel,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/service/clients/employees",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[CreateEmployeeResponse200, QualerApiModelsClientsToCreatedClientEmployeeResponse]
]:
    if response.status_code == 200:
        response_200 = CreateEmployeeResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 201:
        response_201 = QualerApiModelsClientsToCreatedClientEmployeeResponse.from_dict(
            response.json()
        )

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[CreateEmployeeResponse200, QualerApiModelsClientsToCreatedClientEmployeeResponse]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsClientsFromSponsoredEmployeeModel,
) -> Response[
    Union[CreateEmployeeResponse200, QualerApiModelsClientsToCreatedClientEmployeeResponse]
]:
    """
    Args:
        body (QualerApiModelsClientsFromSponsoredEmployeeModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateEmployeeResponse200, QualerApiModelsClientsToCreatedClientEmployeeResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsClientsFromSponsoredEmployeeModel,
) -> Optional[
    Union[CreateEmployeeResponse200, QualerApiModelsClientsToCreatedClientEmployeeResponse]
]:
    """
    Args:
        body (QualerApiModelsClientsFromSponsoredEmployeeModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateEmployeeResponse200, QualerApiModelsClientsToCreatedClientEmployeeResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsClientsFromSponsoredEmployeeModel,
) -> Response[
    Union[CreateEmployeeResponse200, QualerApiModelsClientsToCreatedClientEmployeeResponse]
]:
    """
    Args:
        body (QualerApiModelsClientsFromSponsoredEmployeeModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateEmployeeResponse200, QualerApiModelsClientsToCreatedClientEmployeeResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsClientsFromSponsoredEmployeeModel,
) -> Optional[
    Union[CreateEmployeeResponse200, QualerApiModelsClientsToCreatedClientEmployeeResponse]
]:
    """
    Args:
        body (QualerApiModelsClientsFromSponsoredEmployeeModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateEmployeeResponse200, QualerApiModelsClientsToCreatedClientEmployeeResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
