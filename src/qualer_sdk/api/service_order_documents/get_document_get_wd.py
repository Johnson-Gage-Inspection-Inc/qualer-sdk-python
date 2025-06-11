from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_document_get_wd_response_200 import GetDocumentGetWdResponse200
from ...types import Response


def _get_kwargs(
    guid: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/wd/{guid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetDocumentGetWdResponse200]]:
    if response.status_code == 200:
        response_200 = GetDocumentGetWdResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetDocumentGetWdResponse200]]:
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
) -> Response[Union[Any, GetDocumentGetWdResponse200]]:
    """Retrieve work order document by Unique Id

     Sample request:

    GET api/service/workorders/documents/FE6B21DC-8061-46FF-AAB8-12C2030FE4B9

    GET api/wd/FE6B21DC-8061-46FF-AAB8-12C2030FE4B9

    Args:
        guid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetDocumentGetWdResponse200]]
    """

    kwargs = _get_kwargs(
        guid=guid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    guid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, GetDocumentGetWdResponse200]]:
    """Retrieve work order document by Unique Id

     Sample request:

    GET api/service/workorders/documents/FE6B21DC-8061-46FF-AAB8-12C2030FE4B9

    GET api/wd/FE6B21DC-8061-46FF-AAB8-12C2030FE4B9

    Args:
        guid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetDocumentGetWdResponse200]
    """

    return sync_detailed(
        guid=guid,
        client=client,
    ).parsed


async def asyncio_detailed(
    guid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, GetDocumentGetWdResponse200]]:
    """Retrieve work order document by Unique Id

     Sample request:

    GET api/service/workorders/documents/FE6B21DC-8061-46FF-AAB8-12C2030FE4B9

    GET api/wd/FE6B21DC-8061-46FF-AAB8-12C2030FE4B9

    Args:
        guid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetDocumentGetWdResponse200]]
    """

    kwargs = _get_kwargs(
        guid=guid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    guid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, GetDocumentGetWdResponse200]]:
    """Retrieve work order document by Unique Id

     Sample request:

    GET api/service/workorders/documents/FE6B21DC-8061-46FF-AAB8-12C2030FE4B9

    GET api/wd/FE6B21DC-8061-46FF-AAB8-12C2030FE4B9

    Args:
        guid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetDocumentGetWdResponse200]
    """

    return (
        await asyncio_detailed(
            guid=guid,
            client=client,
        )
    ).parsed
