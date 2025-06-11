from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_asset_from_update_asset_class_model import (
    QualerApiModelsAssetFromUpdateAssetClassModel,
)
from ...models.update_asset_class_response_200 import UpdateAssetClassResponse200
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: QualerApiModelsAssetFromUpdateAssetClassModel,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/assets/{id}/class",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UpdateAssetClassResponse200]:
    if response.status_code == 200:
        response_200 = UpdateAssetClassResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UpdateAssetClassResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsAssetFromUpdateAssetClassModel,
) -> Response[UpdateAssetClassResponse200]:
    """
    Args:
        id (int):
        body (QualerApiModelsAssetFromUpdateAssetClassModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateAssetClassResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsAssetFromUpdateAssetClassModel,
) -> Optional[UpdateAssetClassResponse200]:
    """
    Args:
        id (int):
        body (QualerApiModelsAssetFromUpdateAssetClassModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateAssetClassResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsAssetFromUpdateAssetClassModel,
) -> Response[UpdateAssetClassResponse200]:
    """
    Args:
        id (int):
        body (QualerApiModelsAssetFromUpdateAssetClassModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateAssetClassResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsAssetFromUpdateAssetClassModel,
) -> Optional[UpdateAssetClassResponse200]:
    """
    Args:
        id (int):
        body (QualerApiModelsAssetFromUpdateAssetClassModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateAssetClassResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
