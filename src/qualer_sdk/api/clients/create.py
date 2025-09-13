from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_clients_from_sponsored_client_create_model import (
    ClientsFromSponsoredClientCreateModel,
)
from ...models.qualer_api_models_clients_to_created_client_company_response import (
    ClientsToCreatedClientCompanyResponse,
)
from ...types import Response


def _get_kwargs(
    *,
    body: ClientsFromSponsoredClientCreateModel,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/service/clients",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ClientsToCreatedClientCompanyResponse]]:
    if response.status_code == 201:
        response_201 = ClientsToCreatedClientCompanyResponse.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ClientsToCreatedClientCompanyResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ClientsFromSponsoredClientCreateModel,
) -> Response[Union[Any, ClientsToCreatedClientCompanyResponse]]:
    """Create Client information.

     ClientStatus: Prospect = 0, Approved = 1, NotApproved = 2, Hidden = 3

    Args:
        body (ClientsFromSponsoredClientCreateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ClientsToCreatedClientCompanyResponse]]
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
    body: ClientsFromSponsoredClientCreateModel,
) -> Optional[Union[Any, ClientsToCreatedClientCompanyResponse]]:
    """Create Client information.

     ClientStatus: Prospect = 0, Approved = 1, NotApproved = 2, Hidden = 3

    Args:
        body (ClientsFromSponsoredClientCreateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ClientsToCreatedClientCompanyResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ClientsFromSponsoredClientCreateModel,
) -> Response[Union[Any, ClientsToCreatedClientCompanyResponse]]:
    """Create Client information.

     ClientStatus: Prospect = 0, Approved = 1, NotApproved = 2, Hidden = 3

    Args:
        body (ClientsFromSponsoredClientCreateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ClientsToCreatedClientCompanyResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ClientsFromSponsoredClientCreateModel,
) -> Optional[Union[Any, ClientsToCreatedClientCompanyResponse]]:
    """Create Client information.

     ClientStatus: Prospect = 0, Approved = 1, NotApproved = 2, Hidden = 3

    Args:
        body (ClientsFromSponsoredClientCreateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ClientsToCreatedClientCompanyResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
