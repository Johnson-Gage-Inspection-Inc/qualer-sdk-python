from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_element_page import DeleteElementPage
from ...models.delete_response_200 import DeleteResponse200
from ...types import Response


def _get_kwargs(
    element_page: DeleteElementPage,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/api/user/preferences/{element_page}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DeleteResponse200]:
    if response.status_code == 200:
        response_200 = DeleteResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DeleteResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    element_page: DeleteElementPage,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DeleteResponse200]:
    """
    Args:
        element_page (DeleteElementPage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteResponse200]
    """

    kwargs = _get_kwargs(
        element_page=element_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    element_page: DeleteElementPage,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[DeleteResponse200]:
    """
    Args:
        element_page (DeleteElementPage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteResponse200
    """

    return sync_detailed(
        element_page=element_page,
        client=client,
    ).parsed


async def asyncio_detailed(
    element_page: DeleteElementPage,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DeleteResponse200]:
    """
    Args:
        element_page (DeleteElementPage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteResponse200]
    """

    kwargs = _get_kwargs(
        element_page=element_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    element_page: DeleteElementPage,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[DeleteResponse200]:
    """
    Args:
        element_page (DeleteElementPage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteResponse200
    """

    return (
        await asyncio_detailed(
            element_page=element_page,
            client=client,
        )
    ).parsed
