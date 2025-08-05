from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    service_order_id: int,
    *,
    model_file_name: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["model.fileName"] = model_file_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/service/workorders/{service_order_id}/documents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, File]]:
    if response.status_code == 200:
        return response.content
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, File]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_order_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    model_file_name: Union[Unset, str] = UNSET,
) -> Response[Union[Any, File]]:
    """Retrieve work order documents

     Sample request:

    GET api/service/workorders/1000/documents

    Args:
        service_order_id (int):
        model_file_name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, File]]
    """

    kwargs = _get_kwargs(
        service_order_id=service_order_id,
        model_file_name=model_file_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_order_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    model_file_name: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, File]]:
    """Retrieve work order documents

     Sample request:

    GET api/service/workorders/1000/documents

    Args:
        service_order_id (int):
        model_file_name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, File]
    """

    return sync_detailed(
        service_order_id=service_order_id,
        client=client,
        model_file_name=model_file_name,
    ).parsed


async def asyncio_detailed(
    service_order_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    model_file_name: Union[Unset, str] = UNSET,
) -> Response[Union[Any, File]]:
    """Retrieve work order documents

     Sample request:

    GET api/service/workorders/1000/documents

    Args:
        service_order_id (int):
        model_file_name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, File]]
    """

    kwargs = _get_kwargs(
        service_order_id=service_order_id,
        model_file_name=model_file_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_order_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    model_file_name: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, File]]:
    """Retrieve work order documents

     Sample request:

    GET api/service/workorders/1000/documents

    Args:
        service_order_id (int):
        model_file_name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, File]
    """

    return (
        await asyncio_detailed(
            service_order_id=service_order_id,
            client=client,
            model_file_name=model_file_name,
        )
    ).parsed
