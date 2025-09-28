from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_post_2_response_200 import CreatePost2Response200
from ...models.qualer_api_models_service_orders_from_service_order_metadata_create_model import (
    ServiceOrdersFromServiceOrderMetadataCreateModel,
)
from ...types import Response


def _get_kwargs(
    service_order_id: int,
    *,
    body: ServiceOrdersFromServiceOrderMetadataCreateModel,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/service/workorders/{service_order_id}/metadata",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CreatePost2Response200]:
    if response.status_code == 200:
        response_200 = CreatePost2Response200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        response.raise_for_status()
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CreatePost2Response200]:
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
    body: ServiceOrdersFromServiceOrderMetadataCreateModel,
) -> Response[CreatePost2Response200]:
    """Create metadata

    Args:
        service_order_id (int):
        body (ServiceOrdersFromServiceOrderMetadataCreateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatePost2Response200]
    """

    kwargs = _get_kwargs(
        service_order_id=service_order_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_order_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ServiceOrdersFromServiceOrderMetadataCreateModel,
) -> Optional[CreatePost2Response200]:
    """Create metadata

    Args:
        service_order_id (int):
        body (ServiceOrdersFromServiceOrderMetadataCreateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatePost2Response200
    """

    return sync_detailed(
        service_order_id=service_order_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    service_order_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ServiceOrdersFromServiceOrderMetadataCreateModel,
) -> Response[CreatePost2Response200]:
    """Create metadata

    Args:
        service_order_id (int):
        body (ServiceOrdersFromServiceOrderMetadataCreateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatePost2Response200]
    """

    kwargs = _get_kwargs(
        service_order_id=service_order_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_order_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ServiceOrdersFromServiceOrderMetadataCreateModel,
) -> Optional[CreatePost2Response200]:
    """Create metadata

    Args:
        service_order_id (int):
        body (ServiceOrdersFromServiceOrderMetadataCreateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatePost2Response200
    """

    return (
        await asyncio_detailed(
            service_order_id=service_order_id,
            client=client,
            body=body,
        )
    ).parsed
