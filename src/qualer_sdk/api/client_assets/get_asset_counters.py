from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_asset_to_client_asset_counters_response_model import (
    AssetToClientAssetCountersResponseModel,
)
from ...types import Response


def _get_kwargs(
    client_company_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/service/clients/{client_company_id}/counters",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AssetToClientAssetCountersResponseModel]:
    if response.status_code == 200:
        response_200 = AssetToClientAssetCountersResponseModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AssetToClientAssetCountersResponseModel]:
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
) -> Response[AssetToClientAssetCountersResponseModel]:
    """
    Args:
        client_company_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetToClientAssetCountersResponseModel]
    """

    kwargs = _get_kwargs(
        client_company_id=client_company_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    client_company_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AssetToClientAssetCountersResponseModel]:
    """
    Args:
        client_company_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetToClientAssetCountersResponseModel
    """

    return sync_detailed(
        client_company_id=client_company_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    client_company_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AssetToClientAssetCountersResponseModel]:
    """
    Args:
        client_company_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetToClientAssetCountersResponseModel]
    """

    kwargs = _get_kwargs(
        client_company_id=client_company_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    client_company_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AssetToClientAssetCountersResponseModel]:
    """
    Args:
        client_company_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetToClientAssetCountersResponseModel
    """

    return (
        await asyncio_detailed(
            client_company_id=client_company_id,
            client=client,
        )
    ).parsed
