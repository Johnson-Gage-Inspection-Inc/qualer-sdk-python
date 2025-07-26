from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_service_orders_to_client_order_response_model import (
    QualerApiModelsServiceOrdersToClientOrderResponseModel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: Union[Unset, str] = UNSET,
    company_id: Union[Unset, int] = UNSET,
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
    modified_after: Union[Unset, str] = UNSET,
    work_order_number: Union[Unset, str] = UNSET,
    assigned_employees: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["status"] = status

    params["companyId"] = company_id

    params["from"] = from_

    params["to"] = to

    params["modifiedAfter"] = modified_after

    params["workOrderNumber"] = work_order_number

    params["assignedEmployees"] = assigned_employees

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/service/workorders",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[Any, list["QualerApiModelsServiceOrdersToClientOrderResponseModel"]]
]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                QualerApiModelsServiceOrdersToClientOrderResponseModel.from_dict(
                    response_200_item_data
                )
            )

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[Any, list["QualerApiModelsServiceOrdersToClientOrderResponseModel"]]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, str] = UNSET,
    company_id: Union[Unset, int] = UNSET,
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
    modified_after: Union[Unset, str] = UNSET,
    work_order_number: Union[Unset, str] = UNSET,
    assigned_employees: Union[Unset, str] = UNSET,
) -> Response[
    Union[Any, list["QualerApiModelsServiceOrdersToClientOrderResponseModel"]]
]:
    """Retrieve work orders by filters

     Sample request:

    GET /api/service/workorders

    GET /api/service/workorders?status=submitted

    GET /api/service/workorders?&amp;status=onsite,submitted&amp;companyId=10&amp;from=2010-11-
    15T10:11:12&amp;to=2011-11-15T10:11:12&amp;modifiedAfter=2010-12-
    15T10:11:12&amp;workOrderNumber=00567

    Args:
        status (Union[Unset, str]):
        company_id (Union[Unset, int]):
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):
        modified_after (Union[Unset, str]):
        work_order_number (Union[Unset, str]):
        assigned_employees (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['QualerApiModelsServiceOrdersToClientOrderResponseModel']]]
    """

    kwargs = _get_kwargs(
        status=status,
        company_id=company_id,
        from_=from_,
        to=to,
        modified_after=modified_after,
        work_order_number=work_order_number,
        assigned_employees=assigned_employees,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, str] = UNSET,
    company_id: Union[Unset, int] = UNSET,
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
    modified_after: Union[Unset, str] = UNSET,
    work_order_number: Union[Unset, str] = UNSET,
    assigned_employees: Union[Unset, str] = UNSET,
) -> Optional[
    Union[Any, list["QualerApiModelsServiceOrdersToClientOrderResponseModel"]]
]:
    """Retrieve work orders by filters

     Sample request:

    GET /api/service/workorders

    GET /api/service/workorders?status=submitted

    GET /api/service/workorders?&amp;status=onsite,submitted&amp;companyId=10&amp;from=2010-11-
    15T10:11:12&amp;to=2011-11-15T10:11:12&amp;modifiedAfter=2010-12-
    15T10:11:12&amp;workOrderNumber=00567

    Args:
        status (Union[Unset, str]):
        company_id (Union[Unset, int]):
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):
        modified_after (Union[Unset, str]):
        work_order_number (Union[Unset, str]):
        assigned_employees (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['QualerApiModelsServiceOrdersToClientOrderResponseModel']]
    """

    return sync_detailed(
        client=client,
        status=status,
        company_id=company_id,
        from_=from_,
        to=to,
        modified_after=modified_after,
        work_order_number=work_order_number,
        assigned_employees=assigned_employees,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, str] = UNSET,
    company_id: Union[Unset, int] = UNSET,
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
    modified_after: Union[Unset, str] = UNSET,
    work_order_number: Union[Unset, str] = UNSET,
    assigned_employees: Union[Unset, str] = UNSET,
) -> Response[
    Union[Any, list["QualerApiModelsServiceOrdersToClientOrderResponseModel"]]
]:
    """Retrieve work orders by filters

     Sample request:

    GET /api/service/workorders

    GET /api/service/workorders?status=submitted

    GET /api/service/workorders?&amp;status=onsite,submitted&amp;companyId=10&amp;from=2010-11-
    15T10:11:12&amp;to=2011-11-15T10:11:12&amp;modifiedAfter=2010-12-
    15T10:11:12&amp;workOrderNumber=00567

    Args:
        status (Union[Unset, str]):
        company_id (Union[Unset, int]):
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):
        modified_after (Union[Unset, str]):
        work_order_number (Union[Unset, str]):
        assigned_employees (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['QualerApiModelsServiceOrdersToClientOrderResponseModel']]]
    """

    kwargs = _get_kwargs(
        status=status,
        company_id=company_id,
        from_=from_,
        to=to,
        modified_after=modified_after,
        work_order_number=work_order_number,
        assigned_employees=assigned_employees,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, str] = UNSET,
    company_id: Union[Unset, int] = UNSET,
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
    modified_after: Union[Unset, str] = UNSET,
    work_order_number: Union[Unset, str] = UNSET,
    assigned_employees: Union[Unset, str] = UNSET,
) -> Optional[
    Union[Any, list["QualerApiModelsServiceOrdersToClientOrderResponseModel"]]
]:
    """Retrieve work orders by filters

     Sample request:

    GET /api/service/workorders

    GET /api/service/workorders?status=submitted

    GET /api/service/workorders?&amp;status=onsite,submitted&amp;companyId=10&amp;from=2010-11-
    15T10:11:12&amp;to=2011-11-15T10:11:12&amp;modifiedAfter=2010-12-
    15T10:11:12&amp;workOrderNumber=00567

    Args:
        status (Union[Unset, str]):
        company_id (Union[Unset, int]):
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):
        modified_after (Union[Unset, str]):
        work_order_number (Union[Unset, str]):
        assigned_employees (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['QualerApiModelsServiceOrdersToClientOrderResponseModel']]
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            company_id=company_id,
            from_=from_,
            to=to,
            modified_after=modified_after,
            work_order_number=work_order_number,
            assigned_employees=assigned_employees,
        )
    ).parsed
