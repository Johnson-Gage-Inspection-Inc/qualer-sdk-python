from http import HTTPStatus
from io import BytesIO
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    service_order_item_id: int,
    *,
    model_report_type: Union[Unset, str] = UNSET,
    model_is_private: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["model.reportType"] = model_report_type

    params["model.isPrivate"] = model_is_private

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/service/workitems/{service_order_item_id}/documents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[File]:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[File]:
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
    model_report_type: Union[Unset, str] = UNSET,
    model_is_private: Union[Unset, bool] = UNSET,
) -> Response[File]:
    """
    Args:
        service_order_item_id (int):
        model_report_type (Union[Unset, str]):
        model_is_private (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        service_order_item_id=service_order_item_id,
        model_report_type=model_report_type,
        model_is_private=model_is_private,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_order_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    model_report_type: Union[Unset, str] = UNSET,
    model_is_private: Union[Unset, bool] = UNSET,
) -> Optional[File]:
    """
    Args:
        service_order_item_id (int):
        model_report_type (Union[Unset, str]):
        model_is_private (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return sync_detailed(
        service_order_item_id=service_order_item_id,
        client=client,
        model_report_type=model_report_type,
        model_is_private=model_is_private,
    ).parsed


async def asyncio_detailed(
    service_order_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    model_report_type: Union[Unset, str] = UNSET,
    model_is_private: Union[Unset, bool] = UNSET,
) -> Response[File]:
    """
    Args:
        service_order_item_id (int):
        model_report_type (Union[Unset, str]):
        model_is_private (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        service_order_item_id=service_order_item_id,
        model_report_type=model_report_type,
        model_is_private=model_is_private,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_order_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    model_report_type: Union[Unset, str] = UNSET,
    model_is_private: Union[Unset, bool] = UNSET,
) -> Optional[File]:
    """
    Args:
        service_order_item_id (int):
        model_report_type (Union[Unset, str]):
        model_is_private (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return (
        await asyncio_detailed(
            service_order_item_id=service_order_item_id,
            client=client,
            model_report_type=model_report_type,
            model_is_private=model_is_private,
        )
    ).parsed
