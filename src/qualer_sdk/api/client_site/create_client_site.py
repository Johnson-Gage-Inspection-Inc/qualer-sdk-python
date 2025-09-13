from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_client_site_response_200 import CreateClientSiteResponse200
from ...models.qualer_api_models_site_from_site_create_model import (
    SiteFromSiteCreateModel,
)
from ...types import Response


def _get_kwargs(
    client_company_id: int,
    *,
    body: SiteFromSiteCreateModel,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/service/clients/{client_company_id}/sites",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateClientSiteResponse200]]:
    if response.status_code == 200:
        response_200 = CreateClientSiteResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateClientSiteResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    client_company_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SiteFromSiteCreateModel,
) -> Response[Union[Any, CreateClientSiteResponse200]]:
    r"""Create Client Site.

     CultureName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\"

    Args:
        client_company_id (int):
        body (SiteFromSiteCreateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateClientSiteResponse200]]
    """

    kwargs = _get_kwargs(
        client_company_id=client_company_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    client_company_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SiteFromSiteCreateModel,
) -> Optional[Union[Any, CreateClientSiteResponse200]]:
    r"""Create Client Site.

     CultureName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\"

    Args:
        client_company_id (int):
        body (SiteFromSiteCreateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateClientSiteResponse200]
    """

    return sync_detailed(
        client_company_id=client_company_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    client_company_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SiteFromSiteCreateModel,
) -> Response[Union[Any, CreateClientSiteResponse200]]:
    r"""Create Client Site.

     CultureName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\"

    Args:
        client_company_id (int):
        body (SiteFromSiteCreateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateClientSiteResponse200]]
    """

    kwargs = _get_kwargs(
        client_company_id=client_company_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    client_company_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SiteFromSiteCreateModel,
) -> Optional[Union[Any, CreateClientSiteResponse200]]:
    r"""Create Client Site.

     CultureName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\"

    Args:
        client_company_id (int):
        body (SiteFromSiteCreateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateClientSiteResponse200]
    """

    return (
        await asyncio_detailed(
            client_company_id=client_company_id,
            client=client,
            body=body,
        )
    ).parsed
