from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_web_mvc_areas_api_models_company_from_update_department_model import (
    QualerWebMvcAreasApiModelsCompanyFromUpdateDepartmentModel,
)
from ...models.update_department_response_204 import UpdateDepartmentResponse204
from ...types import Response


def _get_kwargs(
    department_id: int,
    *,
    body: QualerWebMvcAreasApiModelsCompanyFromUpdateDepartmentModel,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/api/company/departments/{department_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UpdateDepartmentResponse204]:
    if response.status_code == 204:
        response_204 = UpdateDepartmentResponse204.from_dict(response.json())

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
) -> Response[UpdateDepartmentResponse204]:
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
    body: QualerWebMvcAreasApiModelsCompanyFromUpdateDepartmentModel,
) -> Response[UpdateDepartmentResponse204]:
    """
    Args:
        department_id (int):
        body (QualerWebMvcAreasApiModelsCompanyFromUpdateDepartmentModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateDepartmentResponse204]
    """

    kwargs = _get_kwargs(
        department_id=department_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    department_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerWebMvcAreasApiModelsCompanyFromUpdateDepartmentModel,
) -> Optional[UpdateDepartmentResponse204]:
    """
    Args:
        department_id (int):
        body (QualerWebMvcAreasApiModelsCompanyFromUpdateDepartmentModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateDepartmentResponse204
    """

    return sync_detailed(
        department_id=department_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    department_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerWebMvcAreasApiModelsCompanyFromUpdateDepartmentModel,
) -> Response[UpdateDepartmentResponse204]:
    """
    Args:
        department_id (int):
        body (QualerWebMvcAreasApiModelsCompanyFromUpdateDepartmentModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateDepartmentResponse204]
    """

    kwargs = _get_kwargs(
        department_id=department_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    department_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerWebMvcAreasApiModelsCompanyFromUpdateDepartmentModel,
) -> Optional[UpdateDepartmentResponse204]:
    """
    Args:
        department_id (int):
        body (QualerWebMvcAreasApiModelsCompanyFromUpdateDepartmentModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateDepartmentResponse204
    """

    return (
        await asyncio_detailed(
            department_id=department_id,
            client=client,
            body=body,
        )
    ).parsed
