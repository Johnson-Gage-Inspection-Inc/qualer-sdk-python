from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_clients_from_sponsored_client_edit_model import (
    QualerApiModelsClientsFromSponsoredClientEditModel,
)
from ...models.update_response_200 import UpdateResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: QualerApiModelsClientsFromSponsoredClientEditModel,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/service/clients",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, UpdateResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsClientsFromSponsoredClientEditModel,
) -> Response[Union[Any, UpdateResponse200]]:
    """Update Client information.

     ClientStatus: Prospect = 0, Approved = 1, NotApproved = 2, Hidden = 3

    Args:
        body (QualerApiModelsClientsFromSponsoredClientEditModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateResponse200]]
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
    body: QualerApiModelsClientsFromSponsoredClientEditModel,
) -> Optional[Union[Any, UpdateResponse200]]:
    """Update Client information.

     ClientStatus: Prospect = 0, Approved = 1, NotApproved = 2, Hidden = 3

    Args:
        body (QualerApiModelsClientsFromSponsoredClientEditModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateResponse200]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsClientsFromSponsoredClientEditModel,
) -> Response[Union[Any, UpdateResponse200]]:
    """Update Client information.

     ClientStatus: Prospect = 0, Approved = 1, NotApproved = 2, Hidden = 3

    Args:
        body (QualerApiModelsClientsFromSponsoredClientEditModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsClientsFromSponsoredClientEditModel,
) -> Optional[Union[Any, UpdateResponse200]]:
    """Update Client information.

     ClientStatus: Prospect = 0, Approved = 1, NotApproved = 2, Hidden = 3

    Args:
        body (QualerApiModelsClientsFromSponsoredClientEditModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
