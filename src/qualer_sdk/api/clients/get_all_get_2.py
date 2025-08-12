import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_clients_to_client_company_response_model import (
    QualerApiModelsClientsToClientCompanyResponseModel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    model_legacy_id: Union[Unset, str] = UNSET,
    model_account_number_text: Union[Unset, str] = UNSET,
    model_company_name: Union[Unset, str] = UNSET,
    model_take: Union[Unset, int] = UNSET,
    model_modified_after: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["model.legacyId"] = model_legacy_id

    params["model.accountNumberText"] = model_account_number_text

    params["model.companyName"] = model_company_name

    params["model.take"] = model_take

    json_model_modified_after: Union[Unset, str] = UNSET
    if model_modified_after and not isinstance(model_modified_after, Unset):
        json_model_modified_after = model_modified_after.isoformat()
    params["model.modifiedAfter"] = json_model_modified_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/service/clients",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["QualerApiModelsClientsToClientCompanyResponseModel"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                QualerApiModelsClientsToClientCompanyResponseModel.from_dict(
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
) -> Response[list["QualerApiModelsClientsToClientCompanyResponseModel"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    model_legacy_id: Union[Unset, str] = UNSET,
    model_account_number_text: Union[Unset, str] = UNSET,
    model_company_name: Union[Unset, str] = UNSET,
    model_take: Union[Unset, int] = UNSET,
    model_modified_after: Union[Unset, datetime.datetime] = UNSET,
) -> Response[list["QualerApiModelsClientsToClientCompanyResponseModel"]]:
    """
    Args:
        model_legacy_id (Union[Unset, str]):
        model_account_number_text (Union[Unset, str]):
        model_company_name (Union[Unset, str]):
        model_take (Union[Unset, int]):
        model_modified_after (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsClientsToClientCompanyResponseModel']]
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
    model_legacy_id: Union[Unset, str] = UNSET,
    model_account_number_text: Union[Unset, str] = UNSET,
    model_company_name: Union[Unset, str] = UNSET,
    model_take: Union[Unset, int] = UNSET,
    model_modified_after: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[list["QualerApiModelsClientsToClientCompanyResponseModel"]]:
    """
    Args:
        model_legacy_id (Union[Unset, str]):
        model_account_number_text (Union[Unset, str]):
        model_company_name (Union[Unset, str]):
        model_take (Union[Unset, int]):
        model_modified_after (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsClientsToClientCompanyResponseModel']
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
    model_legacy_id: Union[Unset, str] = UNSET,
    model_account_number_text: Union[Unset, str] = UNSET,
    model_company_name: Union[Unset, str] = UNSET,
    model_take: Union[Unset, int] = UNSET,
    model_modified_after: Union[Unset, datetime.datetime] = UNSET,
) -> Response[list["QualerApiModelsClientsToClientCompanyResponseModel"]]:
    """
    Args:
        model_legacy_id (Union[Unset, str]):
        model_account_number_text (Union[Unset, str]):
        model_company_name (Union[Unset, str]):
        model_take (Union[Unset, int]):
        model_modified_after (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsClientsToClientCompanyResponseModel']]
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
    model_legacy_id: Union[Unset, str] = UNSET,
    model_account_number_text: Union[Unset, str] = UNSET,
    model_company_name: Union[Unset, str] = UNSET,
    model_take: Union[Unset, int] = UNSET,
    model_modified_after: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[list["QualerApiModelsClientsToClientCompanyResponseModel"]]:
    """
    Args:
        model_legacy_id (Union[Unset, str]):
        model_account_number_text (Union[Unset, str]):
        model_company_name (Union[Unset, str]):
        model_take (Union[Unset, int]):
        model_modified_after (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsClientsToClientCompanyResponseModel']
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
