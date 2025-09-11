from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_account_from_login_response_model import (
    QualerApiModelsAccountFromLoginResponseModel,
)
from ...models.qualer_web_mvc_areas_api_models_account_to_login_model import (
    QualerWebMvcAreasApiModelsAccountToLoginModel,
)
from ...types import Response


def _get_kwargs(
    *,
    body: QualerWebMvcAreasApiModelsAccountToLoginModel,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/login",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, QualerApiModelsAccountFromLoginResponseModel]]:
    if response.status_code == 200:
        response_200 = QualerApiModelsAccountFromLoginResponseModel.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, QualerApiModelsAccountFromLoginResponseModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerWebMvcAreasApiModelsAccountToLoginModel,
) -> Response[Union[Any, QualerApiModelsAccountFromLoginResponseModel]]:
    """Login

    Args:
        body (QualerWebMvcAreasApiModelsAccountToLoginModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, QualerApiModelsAccountFromLoginResponseModel]]
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
    body: QualerWebMvcAreasApiModelsAccountToLoginModel,
) -> Optional[Union[Any, QualerApiModelsAccountFromLoginResponseModel]]:
    """Login

    Args:
        body (QualerWebMvcAreasApiModelsAccountToLoginModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, QualerApiModelsAccountFromLoginResponseModel]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerWebMvcAreasApiModelsAccountToLoginModel,
) -> Response[Union[Any, QualerApiModelsAccountFromLoginResponseModel]]:
    """Login

    Args:
        body (QualerWebMvcAreasApiModelsAccountToLoginModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, QualerApiModelsAccountFromLoginResponseModel]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerWebMvcAreasApiModelsAccountToLoginModel,
) -> Optional[Union[Any, QualerApiModelsAccountFromLoginResponseModel]]:
    """Login

    Args:
        body (QualerWebMvcAreasApiModelsAccountToLoginModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, QualerApiModelsAccountFromLoginResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
