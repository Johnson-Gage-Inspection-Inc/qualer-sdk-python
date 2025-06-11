from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_asset_service_records_to_asset_service_record_response_model import (
    QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_service_record_id: str,
    *,
    model_asset_service_record_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["model.assetServiceRecordId"] = model_asset_service_record_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/assetservicerecords/{asset_service_record_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel]:
    if response.status_code == 200:
        response_200 = QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_service_record_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    model_asset_service_record_id: Union[Unset, int] = UNSET,
) -> Response[QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel]:
    """
    Args:
        asset_service_record_id (str):
        model_asset_service_record_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel]
    """

    kwargs = _get_kwargs(
        asset_service_record_id=asset_service_record_id,
        model_asset_service_record_id=model_asset_service_record_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_service_record_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    model_asset_service_record_id: Union[Unset, int] = UNSET,
) -> Optional[QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel]:
    """
    Args:
        asset_service_record_id (str):
        model_asset_service_record_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel
    """

    return sync_detailed(
        asset_service_record_id=asset_service_record_id,
        client=client,
        model_asset_service_record_id=model_asset_service_record_id,
    ).parsed


async def asyncio_detailed(
    asset_service_record_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    model_asset_service_record_id: Union[Unset, int] = UNSET,
) -> Response[QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel]:
    """
    Args:
        asset_service_record_id (str):
        model_asset_service_record_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel]
    """

    kwargs = _get_kwargs(
        asset_service_record_id=asset_service_record_id,
        model_asset_service_record_id=model_asset_service_record_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_service_record_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    model_asset_service_record_id: Union[Unset, int] = UNSET,
) -> Optional[QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel]:
    """
    Args:
        asset_service_record_id (str):
        model_asset_service_record_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel
    """

    return (
        await asyncio_detailed(
            asset_service_record_id=asset_service_record_id,
            client=client,
            model_asset_service_record_id=model_asset_service_record_id,
        )
    ).parsed
