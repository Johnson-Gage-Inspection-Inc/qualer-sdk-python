from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_vendors_to_vendor_company_response_model import (
    QualerApiModelsVendorsToVendorCompanyResponseModel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    model_account_number_text: Union[Unset, str] = UNSET,
    model_company_name: Union[Unset, str] = UNSET,
    model_take: Union[Unset, int] = UNSET,
    model_modified_after: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["model.accountNumberText"] = model_account_number_text

    params["model.companyName"] = model_company_name

    params["model.take"] = model_take

    params["model.modifiedAfter"] = model_modified_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/service/vendors",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["QualerApiModelsVendorsToVendorCompanyResponseModel"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                QualerApiModelsVendorsToVendorCompanyResponseModel.from_dict(
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
) -> Response[list["QualerApiModelsVendorsToVendorCompanyResponseModel"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    model_account_number_text: Union[Unset, str] = UNSET,
    model_company_name: Union[Unset, str] = UNSET,
    model_take: Union[Unset, int] = UNSET,
    model_modified_after: Union[Unset, str] = UNSET,
) -> Response[list["QualerApiModelsVendorsToVendorCompanyResponseModel"]]:
    """
    Args:
        model_account_number_text (Union[Unset, str]):
        model_company_name (Union[Unset, str]):
        model_take (Union[Unset, int]):
        model_modified_after (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsVendorsToVendorCompanyResponseModel']]
    """

    kwargs = _get_kwargs(
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
    model_account_number_text: Union[Unset, str] = UNSET,
    model_company_name: Union[Unset, str] = UNSET,
    model_take: Union[Unset, int] = UNSET,
    model_modified_after: Union[Unset, str] = UNSET,
) -> Optional[list["QualerApiModelsVendorsToVendorCompanyResponseModel"]]:
    """
    Args:
        model_account_number_text (Union[Unset, str]):
        model_company_name (Union[Unset, str]):
        model_take (Union[Unset, int]):
        model_modified_after (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsVendorsToVendorCompanyResponseModel']
    """

    return sync_detailed(
        client=client,
        model_account_number_text=model_account_number_text,
        model_company_name=model_company_name,
        model_take=model_take,
        model_modified_after=model_modified_after,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    model_account_number_text: Union[Unset, str] = UNSET,
    model_company_name: Union[Unset, str] = UNSET,
    model_take: Union[Unset, int] = UNSET,
    model_modified_after: Union[Unset, str] = UNSET,
) -> Response[list["QualerApiModelsVendorsToVendorCompanyResponseModel"]]:
    """
    Args:
        model_account_number_text (Union[Unset, str]):
        model_company_name (Union[Unset, str]):
        model_take (Union[Unset, int]):
        model_modified_after (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsVendorsToVendorCompanyResponseModel']]
    """

    kwargs = _get_kwargs(
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
    model_account_number_text: Union[Unset, str] = UNSET,
    model_company_name: Union[Unset, str] = UNSET,
    model_take: Union[Unset, int] = UNSET,
    model_modified_after: Union[Unset, str] = UNSET,
) -> Optional[list["QualerApiModelsVendorsToVendorCompanyResponseModel"]]:
    """
    Args:
        model_account_number_text (Union[Unset, str]):
        model_company_name (Union[Unset, str]):
        model_take (Union[Unset, int]):
        model_modified_after (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsVendorsToVendorCompanyResponseModel']
    """

    return (
        await asyncio_detailed(
            client=client,
            model_account_number_text=model_account_number_text,
            model_company_name=model_company_name,
            model_take=model_take,
            model_modified_after=model_modified_after,
        )
    ).parsed
