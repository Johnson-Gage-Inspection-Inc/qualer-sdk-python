from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.upload_documents_post_2_response_200 import UploadDocumentsPost2Response200
from ...types import Response


def _get_kwargs(
    service_order_id: int,
    *,
    model_report_type: Optional[str] = None,
    model_is_private: Optional[bool] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["model.reportType"] = model_report_type

    params["model.isPrivate"] = model_is_private

    params = {k: v for k, v in params.items() if v is not None and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/service/workorders/{service_order_id}/documents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UploadDocumentsPost2Response200]:
    if response.status_code == 200:
        response_200 = UploadDocumentsPost2Response200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UploadDocumentsPost2Response200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_order_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    model_report_type: Optional[str] = None,
    model_is_private: Optional[bool] = None,
) -> Response[UploadDocumentsPost2Response200]:
    """reportType:<br />
    assetsummary, assetlabel, assetdetail, assetcertificate,<br />
    ordersummary / serviceordersummary,<br />
    orderinvoice / serviceorderinvoice,<br />
    orderestimate / serviceorderestimate,<br />
    orderdetail / serviceorderdetail,<br />
    ordercertificate / serviceordercertificate,<br />
    general

    Args:
        service_order_id (int):
        model_report_type (Optional[str]):
        model_is_private (Optional[bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadDocumentsPost2Response200]
    """

    kwargs = _get_kwargs(
        service_order_id=service_order_id,
        model_report_type=model_report_type,
        model_is_private=model_is_private,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_order_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    model_report_type: Optional[str] = None,
    model_is_private: Optional[bool] = None,
) -> Optional[UploadDocumentsPost2Response200]:
    """reportType:<br />
    assetsummary, assetlabel, assetdetail, assetcertificate,<br />
    ordersummary / serviceordersummary,<br />
    orderinvoice / serviceorderinvoice,<br />
    orderestimate / serviceorderestimate,<br />
    orderdetail / serviceorderdetail,<br />
    ordercertificate / serviceordercertificate,<br />
    general

    Args:
        service_order_id (int):
        model_report_type (Optional[str]):
        model_is_private (Optional[bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadDocumentsPost2Response200
    """

    return sync_detailed(
        service_order_id=service_order_id,
        client=client,
        model_report_type=model_report_type,
        model_is_private=model_is_private,
    ).parsed


async def asyncio_detailed(
    service_order_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    model_report_type: Optional[str] = None,
    model_is_private: Optional[bool] = None,
) -> Response[UploadDocumentsPost2Response200]:
    """reportType:<br />
    assetsummary, assetlabel, assetdetail, assetcertificate,<br />
    ordersummary / serviceordersummary,<br />
    orderinvoice / serviceorderinvoice,<br />
    orderestimate / serviceorderestimate,<br />
    orderdetail / serviceorderdetail,<br />
    ordercertificate / serviceordercertificate,<br />
    general

    Args:
        service_order_id (int):
        model_report_type (Optional[str]):
        model_is_private (Optional[bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadDocumentsPost2Response200]
    """

    kwargs = _get_kwargs(
        service_order_id=service_order_id,
        model_report_type=model_report_type,
        model_is_private=model_is_private,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_order_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    model_report_type: Optional[str] = None,
    model_is_private: Optional[bool] = None,
) -> Optional[UploadDocumentsPost2Response200]:
    """reportType:<br />
    assetsummary, assetlabel, assetdetail, assetcertificate,<br />
    ordersummary / serviceordersummary,<br />
    orderinvoice / serviceorderinvoice,<br />
    orderestimate / serviceorderestimate,<br />
    orderdetail / serviceorderdetail,<br />
    ordercertificate / serviceordercertificate,<br />
    general

    Args:
        service_order_id (int):
        model_report_type (Optional[str]):
        model_is_private (Optional[bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadDocumentsPost2Response200
    """

    return (
        await asyncio_detailed(
            service_order_id=service_order_id,
            client=client,
            model_report_type=model_report_type,
            model_is_private=model_is_private,
        )
    ).parsed
