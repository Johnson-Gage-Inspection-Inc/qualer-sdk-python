from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_maintenance_plans_to_maintenance_plan_response import (
    QualerApiModelsMaintenancePlansToMaintenancePlanResponse,
)
from ...types import Response


def _get_kwargs(
    client_company_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/service/clients/{client_company_id}/plans",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["QualerApiModelsMaintenancePlansToMaintenancePlanResponse"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                QualerApiModelsMaintenancePlansToMaintenancePlanResponse.from_dict(
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
) -> Response[list["QualerApiModelsMaintenancePlansToMaintenancePlanResponse"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    client_company_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[list["QualerApiModelsMaintenancePlansToMaintenancePlanResponse"]]:
    """
    Args:
        client_company_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsMaintenancePlansToMaintenancePlanResponse']]
    """

    kwargs = _get_kwargs(
        client_company_id=client_company_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    client_company_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[list["QualerApiModelsMaintenancePlansToMaintenancePlanResponse"]]:
    """
    Args:
        client_company_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsMaintenancePlansToMaintenancePlanResponse']
    """

    return sync_detailed(
        client_company_id=client_company_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    client_company_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[list["QualerApiModelsMaintenancePlansToMaintenancePlanResponse"]]:
    """
    Args:
        client_company_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsMaintenancePlansToMaintenancePlanResponse']]
    """

    kwargs = _get_kwargs(
        client_company_id=client_company_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    client_company_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[list["QualerApiModelsMaintenancePlansToMaintenancePlanResponse"]]:
    """
    Args:
        client_company_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsMaintenancePlansToMaintenancePlanResponse']
    """

    return (
        await asyncio_detailed(
            client_company_id=client_company_id,
            client=client,
        )
    ).parsed
