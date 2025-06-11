from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_get_4_element_page import GetGet4ElementPage
from ...models.qualer_api_models_asset_to_employee_preference_response_model import (
    QualerApiModelsAssetToEmployeePreferenceResponseModel,
)
from ...types import Response


def _get_kwargs(
    element_page: GetGet4ElementPage,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/user/preferences/{element_page}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["QualerApiModelsAssetToEmployeePreferenceResponseModel"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                QualerApiModelsAssetToEmployeePreferenceResponseModel.from_dict(
                    response_200_item_data
                )
            )

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["QualerApiModelsAssetToEmployeePreferenceResponseModel"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    element_page: GetGet4ElementPage,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[list["QualerApiModelsAssetToEmployeePreferenceResponseModel"]]:
    """elementPage:
    AssetManager = 1,
    WorkOrders = 2,
    ServiceOrderItems = 3,
    ServiceSchedules = 4,
    ServiceRequests = 5,
    Vendors = 6,
    VendorAgreements = 7,
    ClientAgreements = 8,
    WorkCalendar = 9,
    Clients = 10,
    GlobalAssetManager = 11,
    InvoicesManager = 12,
    ProductManager = 13,
    ProductSpecifications = 14,
    DocumentManager = 15

    Args:
        element_page (GetGet4ElementPage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsAssetToEmployeePreferenceResponseModel']]
    """

    kwargs = _get_kwargs(
        element_page=element_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    element_page: GetGet4ElementPage,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[list["QualerApiModelsAssetToEmployeePreferenceResponseModel"]]:
    """elementPage:
    AssetManager = 1,
    WorkOrders = 2,
    ServiceOrderItems = 3,
    ServiceSchedules = 4,
    ServiceRequests = 5,
    Vendors = 6,
    VendorAgreements = 7,
    ClientAgreements = 8,
    WorkCalendar = 9,
    Clients = 10,
    GlobalAssetManager = 11,
    InvoicesManager = 12,
    ProductManager = 13,
    ProductSpecifications = 14,
    DocumentManager = 15

    Args:
        element_page (GetGet4ElementPage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsAssetToEmployeePreferenceResponseModel']
    """

    return sync_detailed(
        element_page=element_page,
        client=client,
    ).parsed


async def asyncio_detailed(
    element_page: GetGet4ElementPage,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[list["QualerApiModelsAssetToEmployeePreferenceResponseModel"]]:
    """elementPage:
    AssetManager = 1,
    WorkOrders = 2,
    ServiceOrderItems = 3,
    ServiceSchedules = 4,
    ServiceRequests = 5,
    Vendors = 6,
    VendorAgreements = 7,
    ClientAgreements = 8,
    WorkCalendar = 9,
    Clients = 10,
    GlobalAssetManager = 11,
    InvoicesManager = 12,
    ProductManager = 13,
    ProductSpecifications = 14,
    DocumentManager = 15

    Args:
        element_page (GetGet4ElementPage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsAssetToEmployeePreferenceResponseModel']]
    """

    kwargs = _get_kwargs(
        element_page=element_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    element_page: GetGet4ElementPage,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[list["QualerApiModelsAssetToEmployeePreferenceResponseModel"]]:
    """elementPage:
    AssetManager = 1,
    WorkOrders = 2,
    ServiceOrderItems = 3,
    ServiceSchedules = 4,
    ServiceRequests = 5,
    Vendors = 6,
    VendorAgreements = 7,
    ClientAgreements = 8,
    WorkCalendar = 9,
    Clients = 10,
    GlobalAssetManager = 11,
    InvoicesManager = 12,
    ProductManager = 13,
    ProductSpecifications = 14,
    DocumentManager = 15

    Args:
        element_page (GetGet4ElementPage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsAssetToEmployeePreferenceResponseModel']
    """

    return (
        await asyncio_detailed(
            element_page=element_page,
            client=client,
        )
    ).parsed
