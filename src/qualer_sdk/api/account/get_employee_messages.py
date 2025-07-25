from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_account_to_employee_event_response_model import (
    QualerApiModelsAccountToEmployeeEventResponseModel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    model_period: Union[Unset, int] = UNSET,
    model_site_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["model.period"] = model_period

    params["model.siteId"] = model_site_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/user/messages",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["QualerApiModelsAccountToEmployeeEventResponseModel"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                QualerApiModelsAccountToEmployeeEventResponseModel.from_dict(
                    response_200_item_data
                )
            )

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["QualerApiModelsAccountToEmployeeEventResponseModel"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    model_period: Union[Unset, int] = UNSET,
    model_site_id: Union[Unset, int] = UNSET,
) -> Response[list["QualerApiModelsAccountToEmployeeEventResponseModel"]]:
    """
    Args:
        model_period (Union[Unset, int]):
        model_site_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsAccountToEmployeeEventResponseModel']]
    """

    kwargs = _get_kwargs(
        model_period=model_period,
        model_site_id=model_site_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    model_period: Union[Unset, int] = UNSET,
    model_site_id: Union[Unset, int] = UNSET,
) -> Optional[list["QualerApiModelsAccountToEmployeeEventResponseModel"]]:
    """
    Args:
        model_period (Union[Unset, int]):
        model_site_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsAccountToEmployeeEventResponseModel']
    """

    return sync_detailed(
        client=client,
        model_period=model_period,
        model_site_id=model_site_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    model_period: Union[Unset, int] = UNSET,
    model_site_id: Union[Unset, int] = UNSET,
) -> Response[list["QualerApiModelsAccountToEmployeeEventResponseModel"]]:
    """
    Args:
        model_period (Union[Unset, int]):
        model_site_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsAccountToEmployeeEventResponseModel']]
    """

    kwargs = _get_kwargs(
        model_period=model_period,
        model_site_id=model_site_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    model_period: Union[Unset, int] = UNSET,
    model_site_id: Union[Unset, int] = UNSET,
) -> Optional[list["QualerApiModelsAccountToEmployeeEventResponseModel"]]:
    """
    Args:
        model_period (Union[Unset, int]):
        model_site_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsAccountToEmployeeEventResponseModel']
    """

    return (
        await asyncio_detailed(
            client=client,
            model_period=model_period,
            model_site_id=model_site_id,
        )
    ).parsed
