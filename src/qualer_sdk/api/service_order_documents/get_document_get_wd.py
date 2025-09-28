from http import HTTPStatus
from typing import Any, Dict, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    guid: UUID,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/wd/{guid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[bytes]:
    if response.status_code == 200:
        return response.content
    if response.status_code == 400:
        return None
    if response.status_code == 404:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        response.raise_for_status()
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[bytes]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    guid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[bytes]:
    """Retrieve work order document by Unique Id

     Sample request:

    GET api/service/workorders/documents/FE6B21DC-8061-46FF-AAB8-12C2030FE4B9

    GET api/wd/FE6B21DC-8061-46FF-AAB8-12C2030FE4B9

    Args:
        guid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[bytes]
    """

    kwargs = _get_kwargs(
        guid=guid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    guid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[bytes]:
    """Retrieve work order document by Unique Id

     Sample request:

    GET api/service/workorders/documents/FE6B21DC-8061-46FF-AAB8-12C2030FE4B9

    GET api/wd/FE6B21DC-8061-46FF-AAB8-12C2030FE4B9

    Args:
        guid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[bytes]
    """

    kwargs = _get_kwargs(
        guid=guid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
