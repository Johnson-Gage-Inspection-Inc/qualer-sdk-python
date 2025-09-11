from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_asset_to_asset_response_model import (
    QualerApiModelsAssetToAssetResponseModel,
)
from ...types import Response


def _get_kwargs(
    asset_id_path: str,
    *,
    asset_id_query: Optional[str] = None,
    model_asset_id: Optional[int] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["assetId"] = asset_id_query

    params["model.assetId"] = model_asset_id

    params = {k: v for k, v in params.items() if v is not None and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/service/clients/assets/{asset_id_path}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[QualerApiModelsAssetToAssetResponseModel]:
    if response.status_code == 200:
        response_200 = QualerApiModelsAssetToAssetResponseModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[QualerApiModelsAssetToAssetResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id_path: str,
    *,
    client: Union[AuthenticatedClient, Client],
    asset_id_query: Optional[str] = None,
    model_asset_id: Optional[int] = None,
) -> Response[QualerApiModelsAssetToAssetResponseModel]:
    """
    Args:
        asset_id_path (str):
        asset_id_query (Optional[str]):
        model_asset_id (Optional[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QualerApiModelsAssetToAssetResponseModel]
    """

    kwargs = _get_kwargs(
        asset_id_path=asset_id_path,
        asset_id_query=asset_id_query,
        model_asset_id=model_asset_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id_path: str,
    *,
    client: Union[AuthenticatedClient, Client],
    asset_id_query: Optional[str] = None,
    model_asset_id: Optional[int] = None,
) -> Optional[QualerApiModelsAssetToAssetResponseModel]:
    """
    Args:
        asset_id_path (str):
        asset_id_query (Optional[str]):
        model_asset_id (Optional[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QualerApiModelsAssetToAssetResponseModel
    """

    return sync_detailed(
        asset_id_path=asset_id_path,
        client=client,
        asset_id_query=asset_id_query,
        model_asset_id=model_asset_id,
    ).parsed


async def asyncio_detailed(
    asset_id_path: str,
    *,
    client: Union[AuthenticatedClient, Client],
    asset_id_query: Optional[str] = None,
    model_asset_id: Optional[int] = None,
) -> Response[QualerApiModelsAssetToAssetResponseModel]:
    """
    Args:
        asset_id_path (str):
        asset_id_query (Optional[str]):
        model_asset_id (Optional[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QualerApiModelsAssetToAssetResponseModel]
    """

    kwargs = _get_kwargs(
        asset_id_path=asset_id_path,
        asset_id_query=asset_id_query,
        model_asset_id=model_asset_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id_path: str,
    *,
    client: Union[AuthenticatedClient, Client],
    asset_id_query: Optional[str] = None,
    model_asset_id: Optional[int] = None,
) -> Optional[QualerApiModelsAssetToAssetResponseModel]:
    """
    Args:
        asset_id_path (str):
        asset_id_query (Optional[str]):
        model_asset_id (Optional[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QualerApiModelsAssetToAssetResponseModel
    """

    return (
        await asyncio_detailed(
            asset_id_path=asset_id_path,
            client=client,
            asset_id_query=asset_id_query,
            model_asset_id=model_asset_id,
        )
    ).parsed
