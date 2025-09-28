from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_asset_service_record_response_200 import AddAssetServiceRecordResponse200
from ...models.qualer_api_models_asset_service_records_from_add_asset_service_record_model import (
    AssetServiceRecordsFromAddAssetServiceRecordModel,
)
from ...models.qualer_api_models_asset_service_records_to_add_asset_service_record_response import (
    AssetServiceRecordsToAddAssetServiceRecordResponse,
)
from ...types import Response


def _get_kwargs(
    asset_id: int,
    *,
    body: AssetServiceRecordsFromAddAssetServiceRecordModel,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/assets/{asset_id}/assetservicerecords",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[AddAssetServiceRecordResponse200, AssetServiceRecordsToAddAssetServiceRecordResponse]
]:
    if response.status_code == 200:
        response_200 = AddAssetServiceRecordResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 201:
        response_201 = AssetServiceRecordsToAddAssetServiceRecordResponse.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        response.raise_for_status()
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        AddAssetServiceRecordResponse200,
        AssetServiceRecordsToAddAssetServiceRecordResponse,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AssetServiceRecordsFromAddAssetServiceRecordModel,
) -> Response[
    Union[
        AddAssetServiceRecordResponse200,
        AssetServiceRecordsToAddAssetServiceRecordResponse,
    ]
]:
    """
    Args:
        asset_id (int):
        body (AssetServiceRecordsFromAddAssetServiceRecordModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddAssetServiceRecordResponse200, AssetServiceRecordsToAddAssetServiceRecordResponse]]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AssetServiceRecordsFromAddAssetServiceRecordModel,
) -> Optional[
    Union[AddAssetServiceRecordResponse200, AssetServiceRecordsToAddAssetServiceRecordResponse]
]:
    """
    Args:
        asset_id (int):
        body (AssetServiceRecordsFromAddAssetServiceRecordModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Optional[Union[AddAssetServiceRecordResponse200, AssetServiceRecordsToAddAssetServiceRecordResponse]]
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    asset_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AssetServiceRecordsFromAddAssetServiceRecordModel,
) -> Response[
    Union[
        AddAssetServiceRecordResponse200,
        AssetServiceRecordsToAddAssetServiceRecordResponse,
    ]
]:
    """
    Args:
        asset_id (int):
        body (AssetServiceRecordsFromAddAssetServiceRecordModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddAssetServiceRecordResponse200, AssetServiceRecordsToAddAssetServiceRecordResponse]]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AssetServiceRecordsFromAddAssetServiceRecordModel,
) -> Optional[
    Union[
        AddAssetServiceRecordResponse200,
        AssetServiceRecordsToAddAssetServiceRecordResponse,
    ]
]:
    """
    Args:
        asset_id (int):
        body (AssetServiceRecordsFromAddAssetServiceRecordModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Optional[Union[AddAssetServiceRecordResponse200, AssetServiceRecordsToAddAssetServiceRecordResponse]]
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            body=body,
        )
    ).parsed
