from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.product_response_200 import ProductResponse200
from ...models.qualer_web_mvc_areas_api_models_product_from_product_api_edit_model import (
    QualerWebMvcAreasApiModelsProductFromProductApiEditModel,
)
from ...types import Response


def _get_kwargs(
    product_id: int,
    *,
    body: QualerWebMvcAreasApiModelsProductFromProductApiEditModel,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/products/{product_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ProductResponse200]:
    if response.status_code == 200:
        response_200 = ProductResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ProductResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    product_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerWebMvcAreasApiModelsProductFromProductApiEditModel,
) -> Response[ProductResponse200]:
    """
    Args:
        product_id (int):
        body (QualerWebMvcAreasApiModelsProductFromProductApiEditModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProductResponse200]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    product_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerWebMvcAreasApiModelsProductFromProductApiEditModel,
) -> Optional[ProductResponse200]:
    """
    Args:
        product_id (int):
        body (QualerWebMvcAreasApiModelsProductFromProductApiEditModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProductResponse200
    """

    return sync_detailed(
        product_id=product_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    product_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerWebMvcAreasApiModelsProductFromProductApiEditModel,
) -> Response[ProductResponse200]:
    """
    Args:
        product_id (int):
        body (QualerWebMvcAreasApiModelsProductFromProductApiEditModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProductResponse200]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerWebMvcAreasApiModelsProductFromProductApiEditModel,
) -> Optional[ProductResponse200]:
    """
    Args:
        product_id (int):
        body (QualerWebMvcAreasApiModelsProductFromProductApiEditModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProductResponse200
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            client=client,
            body=body,
        )
    ).parsed
