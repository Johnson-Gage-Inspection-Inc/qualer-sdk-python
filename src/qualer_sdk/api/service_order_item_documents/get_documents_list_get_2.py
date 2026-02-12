from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models import ServiceOrderDocumentResponse
from ...types import Response


def _get_kwargs(
    service_order_item_id: int,
    *,
    model_report_type: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["model.reportType"] = model_report_type

    params = {k: v for k, v in params.items() if v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/service/workitems/{service_order_item_id}/documents/list",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["ServiceOrderDocumentResponse"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ServiceOrderDocumentResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["ServiceOrderDocumentResponse"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_order_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    model_report_type: Optional[str] = None,
) -> Response[List["ServiceOrderDocumentResponse"]]:
    """
    Args:
        service_order_item_id (int):
        model_report_type (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ServiceOrderDocumentResponse']]
    """

    kwargs = _get_kwargs(
        service_order_item_id=service_order_item_id,
        model_report_type=model_report_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_order_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    model_report_type: Optional[str] = None,
) -> Optional[List["ServiceOrderDocumentResponse"]]:
    """
    Args:
        service_order_item_id (int):
        model_report_type (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ServiceOrderDocumentResponse']
    """

    return sync_detailed(
        service_order_item_id=service_order_item_id,
        client=client,
        model_report_type=model_report_type,
    ).parsed


async def asyncio_detailed(
    service_order_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    model_report_type: Optional[str] = None,
) -> Response[List["ServiceOrderDocumentResponse"]]:
    """
    Args:
        service_order_item_id (int):
        model_report_type (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ServiceOrderDocumentResponse']]
    """

    kwargs = _get_kwargs(
        service_order_item_id=service_order_item_id,
        model_report_type=model_report_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_order_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    model_report_type: Optional[str] = None,
) -> Optional[List["ServiceOrderDocumentResponse"]]:
    """
    Args:
        service_order_item_id (int):
        model_report_type (Optional[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ServiceOrderDocumentResponse']
    """

    return (
        await asyncio_detailed(
            service_order_item_id=service_order_item_id,
            client=client,
            model_report_type=model_report_type,
        )
    ).parsed
