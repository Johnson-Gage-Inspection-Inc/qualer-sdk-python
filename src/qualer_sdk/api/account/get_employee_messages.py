from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_account_to_employee_event_response_model import (
    QualerApiModelsAccountToEmployeeEventResponseModel,
)
from ...types import Response


def _get_kwargs(
    *,
    model_period: Optional[int] = None,
    model_site_id: Optional[int] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["model.period"] = model_period

    params["model.siteId"] = model_site_id

    params = {k: v for k, v in params.items() if v is not None and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/user/messages",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["QualerApiModelsAccountToEmployeeEventResponseModel"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = QualerApiModelsAccountToEmployeeEventResponseModel.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["QualerApiModelsAccountToEmployeeEventResponseModel"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    model_period: Optional[int] = None,
    model_site_id: Optional[int] = None,
) -> Response[List["QualerApiModelsAccountToEmployeeEventResponseModel"]]:
    """
    Args:
        model_period (Optional[int]):
        model_site_id (Optional[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['QualerApiModelsAccountToEmployeeEventResponseModel']]
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
    model_period: Optional[int] = None,
    model_site_id: Optional[int] = None,
) -> Optional[List["QualerApiModelsAccountToEmployeeEventResponseModel"]]:
    """
    Args:
        model_period (Optional[int]):
        model_site_id (Optional[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['QualerApiModelsAccountToEmployeeEventResponseModel']
    """

    return sync_detailed(
        client=client,
        model_period=model_period,
        model_site_id=model_site_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    model_period: Optional[int] = None,
    model_site_id: Optional[int] = None,
) -> Response[List["QualerApiModelsAccountToEmployeeEventResponseModel"]]:
    """
    Args:
        model_period (Optional[int]):
        model_site_id (Optional[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['QualerApiModelsAccountToEmployeeEventResponseModel']]
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
    model_period: Optional[int] = None,
    model_site_id: Optional[int] = None,
) -> Optional[List["QualerApiModelsAccountToEmployeeEventResponseModel"]]:
    """
    Args:
        model_period (Optional[int]):
        model_site_id (Optional[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['QualerApiModelsAccountToEmployeeEventResponseModel']
    """

    return (
        await asyncio_detailed(
            client=client,
            model_period=model_period,
            model_site_id=model_site_id,
        )
    ).parsed
