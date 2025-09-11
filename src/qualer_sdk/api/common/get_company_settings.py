from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_common_to_setting_response_model import (
    QualerApiModelsCommonToSettingResponseModel,
)
from ...types import Response


def _get_kwargs(
    *,
    setting_key: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["settingKey"] = setting_key

    params = {k: v for k, v in params.items() if v is not None and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/common/settings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[QualerApiModelsCommonToSettingResponseModel]:
    if response.status_code == 200:
        response_200 = QualerApiModelsCommonToSettingResponseModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[QualerApiModelsCommonToSettingResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    setting_key: str,
) -> Response[QualerApiModelsCommonToSettingResponseModel]:
    """
    Args:
        setting_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QualerApiModelsCommonToSettingResponseModel]
    """

    kwargs = _get_kwargs(
        setting_key=setting_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    setting_key: str,
) -> Optional[QualerApiModelsCommonToSettingResponseModel]:
    """
    Args:
        setting_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QualerApiModelsCommonToSettingResponseModel
    """

    return sync_detailed(
        client=client,
        setting_key=setting_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    setting_key: str,
) -> Response[QualerApiModelsCommonToSettingResponseModel]:
    """
    Args:
        setting_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QualerApiModelsCommonToSettingResponseModel]
    """

    kwargs = _get_kwargs(
        setting_key=setting_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    setting_key: str,
) -> Optional[QualerApiModelsCommonToSettingResponseModel]:
    """
    Args:
        setting_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QualerApiModelsCommonToSettingResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            setting_key=setting_key,
        )
    ).parsed
