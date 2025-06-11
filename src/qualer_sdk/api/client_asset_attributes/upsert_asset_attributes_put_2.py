from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_common_from_attribute_model import (
    QualerApiModelsCommonFromAttributeModel,
)
from ...models.upsert_asset_attributes_put_2_response_200 import (
    UpsertAssetAttributesPut2Response200,
)
from ...types import Response


def _get_kwargs(
    asset_id: int,
    *,
    body: list["QualerApiModelsCommonFromAttributeModel"],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/service/clients/assets/{asset_id}/attributes",
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UpsertAssetAttributesPut2Response200]:
    if response.status_code == 200:
        response_200 = UpsertAssetAttributesPut2Response200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UpsertAssetAttributesPut2Response200]:
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
    body: list["QualerApiModelsCommonFromAttributeModel"],
) -> Response[UpsertAssetAttributesPut2Response200]:
    """
    Args:
        asset_id (int):
        body (list['QualerApiModelsCommonFromAttributeModel']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpsertAssetAttributesPut2Response200]
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
    body: list["QualerApiModelsCommonFromAttributeModel"],
) -> Optional[UpsertAssetAttributesPut2Response200]:
    """
    Args:
        asset_id (int):
        body (list['QualerApiModelsCommonFromAttributeModel']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpsertAssetAttributesPut2Response200
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
    body: list["QualerApiModelsCommonFromAttributeModel"],
) -> Response[UpsertAssetAttributesPut2Response200]:
    """
    Args:
        asset_id (int):
        body (list['QualerApiModelsCommonFromAttributeModel']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpsertAssetAttributesPut2Response200]
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
    body: list["QualerApiModelsCommonFromAttributeModel"],
) -> Optional[UpsertAssetAttributesPut2Response200]:
    """
    Args:
        asset_id (int):
        body (list['QualerApiModelsCommonFromAttributeModel']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpsertAssetAttributesPut2Response200
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            body=body,
        )
    ).parsed
