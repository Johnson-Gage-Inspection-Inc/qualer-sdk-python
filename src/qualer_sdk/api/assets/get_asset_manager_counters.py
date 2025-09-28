from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_asset_to_assets_count_response_model import (
    AssetToAssetsCountResponseModel,
)
from ...types import Response


def _get_kwargs(
    *,
    model_search_string: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["model.searchString"] = model_search_string

    params = {k: v for k, v in params.items() if v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/assets/counters",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AssetToAssetsCountResponseModel]:
    if response.status_code == 200:
        response_200 = AssetToAssetsCountResponseModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        response.raise_for_status()
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AssetToAssetsCountResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    model_search_string: Optional[str] = None,
) -> Response[AssetToAssetsCountResponseModel]:
    """GetAssetManagerCounters

    Args:
        model_search_string (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetToAssetsCountResponseModel]
    """

    kwargs = _get_kwargs(
        model_search_string=model_search_string,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    model_search_string: Optional[str] = None,
) -> Optional[AssetToAssetsCountResponseModel]:
    """GetAssetManagerCounters

    Args:
        model_search_string (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetToAssetsCountResponseModel
    """

    return sync_detailed(
        client=client,
        model_search_string=model_search_string,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    model_search_string: Optional[str] = None,
) -> Response[AssetToAssetsCountResponseModel]:
    """GetAssetManagerCounters

    Args:
        model_search_string (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetToAssetsCountResponseModel]
    """

    kwargs = _get_kwargs(
        model_search_string=model_search_string,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    model_search_string: Optional[str] = None,
) -> Optional[AssetToAssetsCountResponseModel]:
    """GetAssetManagerCounters

    Args:
        model_search_string (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetToAssetsCountResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            model_search_string=model_search_string,
        )
    ).parsed
