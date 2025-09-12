from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_asset_to_client_asset_manager_response_model import (
    QualerApiModelsAssetToClientAssetManagerResponseModel,
)
from ...types import Response


def _get_kwargs(
    client_company_id: int,
    *,
    query_filter_type: Optional[str] = None,
    query_search_string: Optional[str] = None,
    query_page: Optional[int] = None,
    query_page_size: Optional[int] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["query.filterType"] = query_filter_type

    params["query.searchString"] = query_search_string

    params["query.page"] = query_page

    params["query.pageSize"] = query_page_size

    params = {k: v for k, v in params.items() if v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/service/clients/{client_company_id}/assets/byfilter",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["QualerApiModelsAssetToClientAssetManagerResponseModel"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = QualerApiModelsAssetToClientAssetManagerResponseModel.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["QualerApiModelsAssetToClientAssetManagerResponseModel"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    client_company_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    query_filter_type: Optional[str] = None,
    query_search_string: Optional[str] = None,
    query_page: Optional[int] = None,
    query_page_size: Optional[int] = None,
) -> Response[List["QualerApiModelsAssetToClientAssetManagerResponseModel"]]:
    """GetAssetManagerList

     assetFilterType: ClientUnset, ClientAssetsCollected, ClientPastDue, ClientDueForService,
    ClientOutOfService, ClientWithoutSchedule

    ClientDueForService - depends on Employee Filter Preference
    POST api/user/filters

    Args:
        client_company_id (int):
        query_filter_type (Optional[str]):
        query_search_string (Optional[str]):
        query_page (Optional[int]):
        query_page_size (Optional[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['QualerApiModelsAssetToClientAssetManagerResponseModel']]
    """

    kwargs = _get_kwargs(
        client_company_id=client_company_id,
        query_filter_type=query_filter_type,
        query_search_string=query_search_string,
        query_page=query_page,
        query_page_size=query_page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    client_company_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    query_filter_type: Optional[str] = None,
    query_search_string: Optional[str] = None,
    query_page: Optional[int] = None,
    query_page_size: Optional[int] = None,
) -> Optional[List["QualerApiModelsAssetToClientAssetManagerResponseModel"]]:
    """GetAssetManagerList

     assetFilterType: ClientUnset, ClientAssetsCollected, ClientPastDue, ClientDueForService,
    ClientOutOfService, ClientWithoutSchedule

    ClientDueForService - depends on Employee Filter Preference
    POST api/user/filters

    Args:
        client_company_id (int):
        query_filter_type (Optional[str]):
        query_search_string (Optional[str]):
        query_page (Optional[int]):
        query_page_size (Optional[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['QualerApiModelsAssetToClientAssetManagerResponseModel']
    """

    return sync_detailed(
        client_company_id=client_company_id,
        client=client,
        query_filter_type=query_filter_type,
        query_search_string=query_search_string,
        query_page=query_page,
        query_page_size=query_page_size,
    ).parsed


async def asyncio_detailed(
    client_company_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    query_filter_type: Optional[str] = None,
    query_search_string: Optional[str] = None,
    query_page: Optional[int] = None,
    query_page_size: Optional[int] = None,
) -> Response[List["QualerApiModelsAssetToClientAssetManagerResponseModel"]]:
    """GetAssetManagerList

     assetFilterType: ClientUnset, ClientAssetsCollected, ClientPastDue, ClientDueForService,
    ClientOutOfService, ClientWithoutSchedule

    ClientDueForService - depends on Employee Filter Preference
    POST api/user/filters

    Args:
        client_company_id (int):
        query_filter_type (Optional[str]):
        query_search_string (Optional[str]):
        query_page (Optional[int]):
        query_page_size (Optional[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['QualerApiModelsAssetToClientAssetManagerResponseModel']]
    """

    kwargs = _get_kwargs(
        client_company_id=client_company_id,
        query_filter_type=query_filter_type,
        query_search_string=query_search_string,
        query_page=query_page,
        query_page_size=query_page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    client_company_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    query_filter_type: Optional[str] = None,
    query_search_string: Optional[str] = None,
    query_page: Optional[int] = None,
    query_page_size: Optional[int] = None,
) -> Optional[List["QualerApiModelsAssetToClientAssetManagerResponseModel"]]:
    """GetAssetManagerList

     assetFilterType: ClientUnset, ClientAssetsCollected, ClientPastDue, ClientDueForService,
    ClientOutOfService, ClientWithoutSchedule

    ClientDueForService - depends on Employee Filter Preference
    POST api/user/filters

    Args:
        client_company_id (int):
        query_filter_type (Optional[str]):
        query_search_string (Optional[str]):
        query_page (Optional[int]):
        query_page_size (Optional[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['QualerApiModelsAssetToClientAssetManagerResponseModel']
    """

    return (
        await asyncio_detailed(
            client_company_id=client_company_id,
            client=client,
            query_filter_type=query_filter_type,
            query_search_string=query_search_string,
            query_page=query_page,
            query_page_size=query_page_size,
        )
    ).parsed
