from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_vendors_from_sponsored_vendor_edit_model import (
    QualerApiModelsVendorsFromSponsoredVendorEditModel,
)
from ...models.update_put_4_response_200 import UpdatePut4Response200
from ...types import Response


def _get_kwargs(
    *,
    body: QualerApiModelsVendorsFromSponsoredVendorEditModel,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/service/vendors",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdatePut4Response200]]:
    if response.status_code == 200:
        response_200 = UpdatePut4Response200.from_dict(response.json())

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
) -> Response[Union[Any, UpdatePut4Response200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsVendorsFromSponsoredVendorEditModel,
) -> Response[Union[Any, UpdatePut4Response200]]:
    """Update Vendor information.

    Args:
        body (QualerApiModelsVendorsFromSponsoredVendorEditModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdatePut4Response200]]
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
    body: QualerApiModelsVendorsFromSponsoredVendorEditModel,
) -> Optional[Union[Any, UpdatePut4Response200]]:
    """Update Vendor information.

    Args:
        body (QualerApiModelsVendorsFromSponsoredVendorEditModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdatePut4Response200]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsVendorsFromSponsoredVendorEditModel,
) -> Response[Union[Any, UpdatePut4Response200]]:
    """Update Vendor information.

    Args:
        body (QualerApiModelsVendorsFromSponsoredVendorEditModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdatePut4Response200]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsVendorsFromSponsoredVendorEditModel,
) -> Optional[Union[Any, UpdatePut4Response200]]:
    """Update Vendor information.

    Args:
        body (QualerApiModelsVendorsFromSponsoredVendorEditModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdatePut4Response200]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
