from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_asset_from_update_filter_preference_model import (
    QualerApiModelsAssetFromUpdateFilterPreferenceModel,
)
from ...models.update_employee_filter_preference_response_200 import (
    UpdateEmployeeFilterPreferenceResponse200,
)
from ...types import Response


def _get_kwargs(
    *,
    body: QualerApiModelsAssetFromUpdateFilterPreferenceModel,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/user/filters",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UpdateEmployeeFilterPreferenceResponse200]:
    if response.status_code == 200:
        response_200 = UpdateEmployeeFilterPreferenceResponse200.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UpdateEmployeeFilterPreferenceResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsAssetFromUpdateFilterPreferenceModel,
) -> Response[UpdateEmployeeFilterPreferenceResponse200]:
    """UpdateEmployeeFilterPreference

    Args:
        body (QualerApiModelsAssetFromUpdateFilterPreferenceModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateEmployeeFilterPreferenceResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsAssetFromUpdateFilterPreferenceModel,
) -> Optional[UpdateEmployeeFilterPreferenceResponse200]:
    """UpdateEmployeeFilterPreference

    Args:
        body (QualerApiModelsAssetFromUpdateFilterPreferenceModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateEmployeeFilterPreferenceResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsAssetFromUpdateFilterPreferenceModel,
) -> Response[UpdateEmployeeFilterPreferenceResponse200]:
    """UpdateEmployeeFilterPreference

    Args:
        body (QualerApiModelsAssetFromUpdateFilterPreferenceModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateEmployeeFilterPreferenceResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsAssetFromUpdateFilterPreferenceModel,
) -> Optional[UpdateEmployeeFilterPreferenceResponse200]:
    """UpdateEmployeeFilterPreference

    Args:
        body (QualerApiModelsAssetFromUpdateFilterPreferenceModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateEmployeeFilterPreferenceResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
