from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.logout_response_200 import LogoutResponse200
from ...models.qualer_api_models_account_to_logout_model import (
    QualerApiModelsAccountToLogoutModel,
)
from ...types import Response


def _get_kwargs(
    *,
    body: QualerApiModelsAccountToLogoutModel,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/logout",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, LogoutResponse200]]:
    if response.status_code == 200:
        response_200 = LogoutResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, LogoutResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsAccountToLogoutModel,
) -> Response[Union[Any, LogoutResponse200]]:
    """Logout

     LogoutAction:<br />
    Logout - remove the passed token from the list of active sessions (default value)<br />
    LogoutAll - remove this token and all other tokens created for the same user from the list of active
    sessions<br />
    LogoutAllOther - remove all tokens created for the same user from the list of session except for the
    one that is passed in<br />
    Rotate - change the current token to a different GUID and return the new GUID

    Args:
        body (QualerApiModelsAccountToLogoutModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LogoutResponse200]]
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
    body: QualerApiModelsAccountToLogoutModel,
) -> Optional[Union[Any, LogoutResponse200]]:
    """Logout

     LogoutAction:<br />
    Logout - remove the passed token from the list of active sessions (default value)<br />
    LogoutAll - remove this token and all other tokens created for the same user from the list of active
    sessions<br />
    LogoutAllOther - remove all tokens created for the same user from the list of session except for the
    one that is passed in<br />
    Rotate - change the current token to a different GUID and return the new GUID

    Args:
        body (QualerApiModelsAccountToLogoutModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LogoutResponse200]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsAccountToLogoutModel,
) -> Response[Union[Any, LogoutResponse200]]:
    """Logout

     LogoutAction:<br />
    Logout - remove the passed token from the list of active sessions (default value)<br />
    LogoutAll - remove this token and all other tokens created for the same user from the list of active
    sessions<br />
    LogoutAllOther - remove all tokens created for the same user from the list of session except for the
    one that is passed in<br />
    Rotate - change the current token to a different GUID and return the new GUID

    Args:
        body (QualerApiModelsAccountToLogoutModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LogoutResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsAccountToLogoutModel,
) -> Optional[Union[Any, LogoutResponse200]]:
    """Logout

     LogoutAction:<br />
    Logout - remove the passed token from the list of active sessions (default value)<br />
    LogoutAll - remove this token and all other tokens created for the same user from the list of active
    sessions<br />
    LogoutAllOther - remove all tokens created for the same user from the list of session except for the
    one that is passed in<br />
    Rotate - change the current token to a different GUID and return the new GUID

    Args:
        body (QualerApiModelsAccountToLogoutModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LogoutResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
