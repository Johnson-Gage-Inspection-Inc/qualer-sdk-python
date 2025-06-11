from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_account_to_employee_event_message_response_model import (
    QualerApiModelsAccountToEmployeeEventMessageResponseModel,
)
from ...types import Response


def _get_kwargs(
    message_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/user/messages/{message_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[QualerApiModelsAccountToEmployeeEventMessageResponseModel]:
    if response.status_code == 200:
        response_200 = (
            QualerApiModelsAccountToEmployeeEventMessageResponseModel.from_dict(
                response.json()
            )
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[QualerApiModelsAccountToEmployeeEventMessageResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    message_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[QualerApiModelsAccountToEmployeeEventMessageResponseModel]:
    """
    Args:
        message_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QualerApiModelsAccountToEmployeeEventMessageResponseModel]
    """

    kwargs = _get_kwargs(
        message_id=message_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    message_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[QualerApiModelsAccountToEmployeeEventMessageResponseModel]:
    """
    Args:
        message_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QualerApiModelsAccountToEmployeeEventMessageResponseModel
    """

    return sync_detailed(
        message_id=message_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    message_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[QualerApiModelsAccountToEmployeeEventMessageResponseModel]:
    """
    Args:
        message_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QualerApiModelsAccountToEmployeeEventMessageResponseModel]
    """

    kwargs = _get_kwargs(
        message_id=message_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    message_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[QualerApiModelsAccountToEmployeeEventMessageResponseModel]:
    """
    Args:
        message_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QualerApiModelsAccountToEmployeeEventMessageResponseModel
    """

    return (
        await asyncio_detailed(
            message_id=message_id,
            client=client,
        )
    ).parsed
