from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_clients_to_employee_response_model import (
    QualerApiModelsClientsToEmployeeResponseModel,
)
from ...types import Response


def _get_kwargs(
    *,
    model_search_string: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["model.searchString"] = model_search_string

    params = {k: v for k, v in params.items() if v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/employees",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["QualerApiModelsClientsToEmployeeResponseModel"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = QualerApiModelsClientsToEmployeeResponseModel.from_dict(
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
) -> Response[List["QualerApiModelsClientsToEmployeeResponseModel"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    model_search_string: Optional[str] = None,
) -> Response[List["QualerApiModelsClientsToEmployeeResponseModel"]]:
    """
    Args:
        model_search_string (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['QualerApiModelsClientsToEmployeeResponseModel']]
    """

    kwargs = _get_kwargs(
        model_search_string=model_search_string,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    model_search_string: Optional[str] = None,
) -> Optional[List["QualerApiModelsClientsToEmployeeResponseModel"]]:
    """
    Args:
        model_search_string (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['QualerApiModelsClientsToEmployeeResponseModel']
    """

    return sync_detailed(
        client=client,
        model_search_string=model_search_string,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    model_search_string: Optional[str] = None,
) -> Response[List["QualerApiModelsClientsToEmployeeResponseModel"]]:
    """
    Args:
        model_search_string (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['QualerApiModelsClientsToEmployeeResponseModel']]
    """

    kwargs = _get_kwargs(
        model_search_string=model_search_string,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    model_search_string: Optional[str] = None,
) -> Optional[List["QualerApiModelsClientsToEmployeeResponseModel"]]:
    """
    Args:
        model_search_string (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['QualerApiModelsClientsToEmployeeResponseModel']
    """

    return (
        await asyncio_detailed(
            client=client,
            model_search_string=model_search_string,
        )
    ).parsed
