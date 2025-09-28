import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_clients_to_client_company_response_model import (
    ClientsToClientCompanyResponseModel,
)
from ...types import Response


def _get_kwargs(
    *,
    model_legacy_id: Optional[str] = None,
    model_account_number_text: Optional[str] = None,
    model_company_name: Optional[str] = None,
    model_take: Optional[int] = None,
    model_modified_after: Optional[datetime.datetime] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["model.legacyId"] = model_legacy_id

    params["model.accountNumberText"] = model_account_number_text

    params["model.companyName"] = model_company_name

    params["model.take"] = model_take

    json_model_modified_after: Optional[str] = None
    if model_modified_after:
        json_model_modified_after = model_modified_after.isoformat()
    params["model.modifiedAfter"] = json_model_modified_after

    params = {k: v for k, v in params.items() if v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/service/clients",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["ClientsToClientCompanyResponseModel"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ClientsToClientCompanyResponseModel.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        response.raise_for_status()
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["ClientsToClientCompanyResponseModel"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    model_legacy_id: Optional[str] = None,
    model_account_number_text: Optional[str] = None,
    model_company_name: Optional[str] = None,
    model_take: Optional[int] = None,
    model_modified_after: Optional[datetime.datetime] = None,
) -> Response[List["ClientsToClientCompanyResponseModel"]]:
    """
    Args:
        model_legacy_id (Optional[str]):
        model_account_number_text (Optional[str]):
        model_company_name (Optional[str]):
        model_take (Optional[int]):
        model_modified_after (Optional[datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ClientsToClientCompanyResponseModel']]
    """

    kwargs = _get_kwargs(
        model_legacy_id=model_legacy_id,
        model_account_number_text=model_account_number_text,
        model_company_name=model_company_name,
        model_take=model_take,
        model_modified_after=model_modified_after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    model_legacy_id: Optional[str] = None,
    model_account_number_text: Optional[str] = None,
    model_company_name: Optional[str] = None,
    model_take: Optional[int] = None,
    model_modified_after: Optional[datetime.datetime] = None,
) -> Optional[List["ClientsToClientCompanyResponseModel"]]:
    """
    Args:
        model_legacy_id (Optional[str]):
        model_account_number_text (Optional[str]):
        model_company_name (Optional[str]):
        model_take (Optional[int]):
        model_modified_after (Optional[datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ClientsToClientCompanyResponseModel']
    """

    return sync_detailed(
        client=client,
        model_legacy_id=model_legacy_id,
        model_account_number_text=model_account_number_text,
        model_company_name=model_company_name,
        model_take=model_take,
        model_modified_after=model_modified_after,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    model_legacy_id: Optional[str] = None,
    model_account_number_text: Optional[str] = None,
    model_company_name: Optional[str] = None,
    model_take: Optional[int] = None,
    model_modified_after: Optional[datetime.datetime] = None,
) -> Response[List["ClientsToClientCompanyResponseModel"]]:
    """
    Args:
        model_legacy_id (Optional[str]):
        model_account_number_text (Optional[str]):
        model_company_name (Optional[str]):
        model_take (Optional[int]):
        model_modified_after (Optional[datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ClientsToClientCompanyResponseModel']]
    """

    kwargs = _get_kwargs(
        model_legacy_id=model_legacy_id,
        model_account_number_text=model_account_number_text,
        model_company_name=model_company_name,
        model_take=model_take,
        model_modified_after=model_modified_after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    model_legacy_id: Optional[str] = None,
    model_account_number_text: Optional[str] = None,
    model_company_name: Optional[str] = None,
    model_take: Optional[int] = None,
    model_modified_after: Optional[datetime.datetime] = None,
) -> Optional[List["ClientsToClientCompanyResponseModel"]]:
    """
    Args:
        model_legacy_id (Optional[str]):
        model_account_number_text (Optional[str]):
        model_company_name (Optional[str]):
        model_take (Optional[int]):
        model_modified_after (Optional[datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ClientsToClientCompanyResponseModel']
    """

    return (
        await asyncio_detailed(
            client=client,
            model_legacy_id=model_legacy_id,
            model_account_number_text=model_account_number_text,
            model_company_name=model_company_name,
            model_take=model_take,
            model_modified_after=model_modified_after,
        )
    ).parsed
