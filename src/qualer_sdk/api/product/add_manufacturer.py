from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_manufacturer_response_200 import AddManufacturerResponse200
from ...types import Response


def _get_kwargs(
    *,
    manufacturer_name: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["manufacturerName"] = manufacturer_name

    params = {k: v for k, v in params.items() if v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/manufacturers/add",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AddManufacturerResponse200]:
    if response.status_code == 200:
        response_200 = AddManufacturerResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        response.raise_for_status()
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AddManufacturerResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    manufacturer_name: str,
) -> Response[AddManufacturerResponse200]:
    """
    Args:
        manufacturer_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddManufacturerResponse200]
    """

    kwargs = _get_kwargs(
        manufacturer_name=manufacturer_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    manufacturer_name: str,
) -> Optional[AddManufacturerResponse200]:
    """
    Args:
        manufacturer_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddManufacturerResponse200
    """

    return sync_detailed(
        client=client,
        manufacturer_name=manufacturer_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    manufacturer_name: str,
) -> Response[AddManufacturerResponse200]:
    """
    Args:
        manufacturer_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddManufacturerResponse200]
    """

    kwargs = _get_kwargs(
        manufacturer_name=manufacturer_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    manufacturer_name: str,
) -> Optional[AddManufacturerResponse200]:
    """
    Args:
        manufacturer_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddManufacturerResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            manufacturer_name=manufacturer_name,
        )
    ).parsed
