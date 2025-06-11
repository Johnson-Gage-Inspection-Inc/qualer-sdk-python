from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_asset_to_asset_manage_response_model import (
    QualerApiModelsAssetToAssetManageResponseModel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    model_filter_type: Union[Unset, str] = UNSET,
    model_search_string: Union[Unset, str] = UNSET,
    model_page: Union[Unset, int] = UNSET,
    model_page_size: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["model.filterType"] = model_filter_type

    params["model.searchString"] = model_search_string

    params["model.page"] = model_page

    params["model.pageSize"] = model_page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/assets/byfilter",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["QualerApiModelsAssetToAssetManageResponseModel"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                QualerApiModelsAssetToAssetManageResponseModel.from_dict(
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
) -> Response[list["QualerApiModelsAssetToAssetManageResponseModel"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    model_filter_type: Union[Unset, str] = UNSET,
    model_search_string: Union[Unset, str] = UNSET,
    model_page: Union[Unset, int] = UNSET,
    model_page_size: Union[Unset, int] = UNSET,
) -> Response[list["QualerApiModelsAssetToAssetManageResponseModel"]]:
    """GetAssetManagerList

     filterType: Unset, DueForService, RecentlyServiced, NotServiced, RecentlyPurchased,
        WarrantyExpiring, DueForReplacement, OutOfService,
        PastDue, ServicePending, CollectedAssets,  WithoutSchedule, WithoutVendor,
        WithoutProduct, Added, Modified, Deleted,
        NoAgreement, ExpiredAgreement, AgreementUpForRenewal

    Args:
        model_filter_type (Union[Unset, str]):
        model_search_string (Union[Unset, str]):
        model_page (Union[Unset, int]):
        model_page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsAssetToAssetManageResponseModel']]
    """

    kwargs = _get_kwargs(
        model_filter_type=model_filter_type,
        model_search_string=model_search_string,
        model_page=model_page,
        model_page_size=model_page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    model_filter_type: Union[Unset, str] = UNSET,
    model_search_string: Union[Unset, str] = UNSET,
    model_page: Union[Unset, int] = UNSET,
    model_page_size: Union[Unset, int] = UNSET,
) -> Optional[list["QualerApiModelsAssetToAssetManageResponseModel"]]:
    """GetAssetManagerList

     filterType: Unset, DueForService, RecentlyServiced, NotServiced, RecentlyPurchased,
        WarrantyExpiring, DueForReplacement, OutOfService,
        PastDue, ServicePending, CollectedAssets,  WithoutSchedule, WithoutVendor,
        WithoutProduct, Added, Modified, Deleted,
        NoAgreement, ExpiredAgreement, AgreementUpForRenewal

    Args:
        model_filter_type (Union[Unset, str]):
        model_search_string (Union[Unset, str]):
        model_page (Union[Unset, int]):
        model_page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsAssetToAssetManageResponseModel']
    """

    return sync_detailed(
        client=client,
        model_filter_type=model_filter_type,
        model_search_string=model_search_string,
        model_page=model_page,
        model_page_size=model_page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    model_filter_type: Union[Unset, str] = UNSET,
    model_search_string: Union[Unset, str] = UNSET,
    model_page: Union[Unset, int] = UNSET,
    model_page_size: Union[Unset, int] = UNSET,
) -> Response[list["QualerApiModelsAssetToAssetManageResponseModel"]]:
    """GetAssetManagerList

     filterType: Unset, DueForService, RecentlyServiced, NotServiced, RecentlyPurchased,
        WarrantyExpiring, DueForReplacement, OutOfService,
        PastDue, ServicePending, CollectedAssets,  WithoutSchedule, WithoutVendor,
        WithoutProduct, Added, Modified, Deleted,
        NoAgreement, ExpiredAgreement, AgreementUpForRenewal

    Args:
        model_filter_type (Union[Unset, str]):
        model_search_string (Union[Unset, str]):
        model_page (Union[Unset, int]):
        model_page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsAssetToAssetManageResponseModel']]
    """

    kwargs = _get_kwargs(
        model_filter_type=model_filter_type,
        model_search_string=model_search_string,
        model_page=model_page,
        model_page_size=model_page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    model_filter_type: Union[Unset, str] = UNSET,
    model_search_string: Union[Unset, str] = UNSET,
    model_page: Union[Unset, int] = UNSET,
    model_page_size: Union[Unset, int] = UNSET,
) -> Optional[list["QualerApiModelsAssetToAssetManageResponseModel"]]:
    """GetAssetManagerList

     filterType: Unset, DueForService, RecentlyServiced, NotServiced, RecentlyPurchased,
        WarrantyExpiring, DueForReplacement, OutOfService,
        PastDue, ServicePending, CollectedAssets,  WithoutSchedule, WithoutVendor,
        WithoutProduct, Added, Modified, Deleted,
        NoAgreement, ExpiredAgreement, AgreementUpForRenewal

    Args:
        model_filter_type (Union[Unset, str]):
        model_search_string (Union[Unset, str]):
        model_page (Union[Unset, int]):
        model_page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsAssetToAssetManageResponseModel']
    """

    return (
        await asyncio_detailed(
            client=client,
            model_filter_type=model_filter_type,
            model_search_string=model_search_string,
            model_page=model_page,
            model_page_size=model_page_size,
        )
    ).parsed
