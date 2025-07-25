from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_asset_service_record_response_200 import (
    AddAssetServiceRecordResponse200,
)
from ...models.qualer_api_models_asset_service_records_from_add_asset_service_record_model import (
    QualerApiModelsAssetServiceRecordsFromAddAssetServiceRecordModel,
)
from ...models.qualer_api_models_asset_service_records_to_add_asset_service_record_response import (
    QualerApiModelsAssetServiceRecordsToAddAssetServiceRecordResponse,
)
from ...types import Response


def _get_kwargs(
    asset_id: int,
    *,
    body: QualerApiModelsAssetServiceRecordsFromAddAssetServiceRecordModel,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
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
    Union[
        AddAssetServiceRecordResponse200,
        QualerApiModelsAssetServiceRecordsToAddAssetServiceRecordResponse,
    ]
]:
    if response.status_code == 200:
        response_200 = AddAssetServiceRecordResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 201:
        response_201 = (
            QualerApiModelsAssetServiceRecordsToAddAssetServiceRecordResponse.from_dict(
                response.json()
            )
        )

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        AddAssetServiceRecordResponse200,
        QualerApiModelsAssetServiceRecordsToAddAssetServiceRecordResponse,
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
    body: QualerApiModelsAssetServiceRecordsFromAddAssetServiceRecordModel,
) -> Response[
    Union[
        AddAssetServiceRecordResponse200,
        QualerApiModelsAssetServiceRecordsToAddAssetServiceRecordResponse,
    ]
]:
    """
    Args:
        asset_id (int):
        body (QualerApiModelsAssetServiceRecordsFromAddAssetServiceRecordModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddAssetServiceRecordResponse200, QualerApiModelsAssetServiceRecordsToAddAssetServiceRecordResponse]]
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
    body: QualerApiModelsAssetServiceRecordsFromAddAssetServiceRecordModel,
) -> Optional[
    Union[
        AddAssetServiceRecordResponse200,
        QualerApiModelsAssetServiceRecordsToAddAssetServiceRecordResponse,
    ]
]:
    """
    Args:
        asset_id (int):
        body (QualerApiModelsAssetServiceRecordsFromAddAssetServiceRecordModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddAssetServiceRecordResponse200, QualerApiModelsAssetServiceRecordsToAddAssetServiceRecordResponse]
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
    body: QualerApiModelsAssetServiceRecordsFromAddAssetServiceRecordModel,
) -> Response[
    Union[
        AddAssetServiceRecordResponse200,
        QualerApiModelsAssetServiceRecordsToAddAssetServiceRecordResponse,
    ]
]:
    """
    Args:
        asset_id (int):
        body (QualerApiModelsAssetServiceRecordsFromAddAssetServiceRecordModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddAssetServiceRecordResponse200, QualerApiModelsAssetServiceRecordsToAddAssetServiceRecordResponse]]
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
    body: QualerApiModelsAssetServiceRecordsFromAddAssetServiceRecordModel,
) -> Optional[
    Union[
        AddAssetServiceRecordResponse200,
        QualerApiModelsAssetServiceRecordsToAddAssetServiceRecordResponse,
    ]
]:
    """
    Args:
        asset_id (int):
        body (QualerApiModelsAssetServiceRecordsFromAddAssetServiceRecordModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddAssetServiceRecordResponse200, QualerApiModelsAssetServiceRecordsToAddAssetServiceRecordResponse]
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            body=body,
        )
    ).parsed
