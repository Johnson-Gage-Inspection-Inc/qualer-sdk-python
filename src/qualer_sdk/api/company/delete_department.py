from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_department_response_204 import DeleteDepartmentResponse204
from ...types import Response


def _get_kwargs(
    department_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/api/company/departments/{department_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DeleteDepartmentResponse204]:
    if response.status_code == 204:
        response_204 = DeleteDepartmentResponse204.from_dict(response.json())

        return response_204
    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DeleteDepartmentResponse204]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    department_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DeleteDepartmentResponse204]:
    """
    Args:
        department_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteDepartmentResponse204]
    """

    kwargs = _get_kwargs(
        department_id=department_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    department_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[DeleteDepartmentResponse204]:
    """
    Args:
        department_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteDepartmentResponse204
    """

    return sync_detailed(
        department_id=department_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    department_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DeleteDepartmentResponse204]:
    """
    Args:
        department_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteDepartmentResponse204]
    """

    kwargs = _get_kwargs(
        department_id=department_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    department_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[DeleteDepartmentResponse204]:
    """
    Args:
        department_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteDepartmentResponse204
    """

    return (
        await asyncio_detailed(
            department_id=department_id,
            client=client,
        )
    ).parsed
