import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_service_order_documents_to_company_order_controlled_document_response import (
    ServiceOrderDocumentsToCompanyOrderControlledDocumentResponse,
)
from ...types import Response


def _get_kwargs(
    *,
    from_: datetime.datetime,
    to: datetime.datetime,
    report_type: Optional[str] = None,
    service_order_id: Optional[int] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to = to.isoformat()
    params["to"] = json_to

    params["reportType"] = report_type

    params["serviceOrderId"] = service_order_id

    params = {k: v for k, v in params.items() if v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/service/workorders/documents/list",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        Any,
        List["ServiceOrderDocumentsToCompanyOrderControlledDocumentResponse"],
    ]
]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                ServiceOrderDocumentsToCompanyOrderControlledDocumentResponse.from_dict(
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
    Union[
        Any,
        List["ServiceOrderDocumentsToCompanyOrderControlledDocumentResponse"],
    ]
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
    from_: datetime.datetime,
    to: datetime.datetime,
    report_type: Optional[str] = None,
    service_order_id: Optional[int] = None,
) -> Response[
    Union[
        Any,
        List["ServiceOrderDocumentsToCompanyOrderControlledDocumentResponse"],
    ]
]:
    """Retrieve work order documents

     Sample request:

    GET /api/service/workorders/documents/list

    GET /api/service/workorders/documents/list?status=reportType

    GET /api/service/workorders/documents/list?from=2020-12-01T10:11:12&amp;to=2021-01-
    01T10:11:12&amp;reportType=OrderInvoice&amp;ServiceOrderId=1

    reportType:<br />
    None = 0,<br />
    AssetSummary = 1,<br />
    AssetLabel = 11,<br />
    AssetDetail = 2,<br />
    AssetCertificate = 21,<br />
    OrderSummary / ServiceOrderSummary = 3,<br />
    OrderInvoice / ServiceOrderInvoice = 31,<br />
    OrderEstimate / ServiceOrderEstimate = 32,<br />
    Dashboard = 4,<br />
    OrderDetail / ServiceOrderDetail = 5,<br />
    OrderCertificate / ServiceOrderCertificate = 5<br />

    Args:
        from_ (datetime.datetime):
        to (datetime.datetime):
        report_type (Optional[str]):
        service_order_id (Optional[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ServiceOrderDocumentsToCompanyOrderControlledDocumentResponse']]]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        report_type=report_type,
        service_order_id=service_order_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    from_: datetime.datetime,
    to: datetime.datetime,
    report_type: Optional[str] = None,
    service_order_id: Optional[int] = None,
) -> Optional[
    Union[
        Any,
        List["ServiceOrderDocumentsToCompanyOrderControlledDocumentResponse"],
    ]
]:
    """Retrieve work order documents

     Sample request:

    GET /api/service/workorders/documents/list

    GET /api/service/workorders/documents/list?status=reportType

    GET /api/service/workorders/documents/list?from=2020-12-01T10:11:12&amp;to=2021-01-
    01T10:11:12&amp;reportType=OrderInvoice&amp;ServiceOrderId=1

    reportType:<br />
    None = 0,<br />
    AssetSummary = 1,<br />
    AssetLabel = 11,<br />
    AssetDetail = 2,<br />
    AssetCertificate = 21,<br />
    OrderSummary / ServiceOrderSummary = 3,<br />
    OrderInvoice / ServiceOrderInvoice = 31,<br />
    OrderEstimate / ServiceOrderEstimate = 32,<br />
    Dashboard = 4,<br />
    OrderDetail / ServiceOrderDetail = 5,<br />
    OrderCertificate / ServiceOrderCertificate = 5<br />

    Args:
        from_ (datetime.datetime):
        to (datetime.datetime):
        report_type (Optional[str]):
        service_order_id (Optional[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['ServiceOrderDocumentsToCompanyOrderControlledDocumentResponse']]
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
        report_type=report_type,
        service_order_id=service_order_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    from_: datetime.datetime,
    to: datetime.datetime,
    report_type: Optional[str] = None,
    service_order_id: Optional[int] = None,
) -> Response[
    Union[
        Any,
        List["ServiceOrderDocumentsToCompanyOrderControlledDocumentResponse"],
    ]
]:
    """Retrieve work order documents

     Sample request:

    GET /api/service/workorders/documents/list

    GET /api/service/workorders/documents/list?status=reportType

    GET /api/service/workorders/documents/list?from=2020-12-01T10:11:12&amp;to=2021-01-
    01T10:11:12&amp;reportType=OrderInvoice&amp;ServiceOrderId=1

    reportType:<br />
    None = 0,<br />
    AssetSummary = 1,<br />
    AssetLabel = 11,<br />
    AssetDetail = 2,<br />
    AssetCertificate = 21,<br />
    OrderSummary / ServiceOrderSummary = 3,<br />
    OrderInvoice / ServiceOrderInvoice = 31,<br />
    OrderEstimate / ServiceOrderEstimate = 32,<br />
    Dashboard = 4,<br />
    OrderDetail / ServiceOrderDetail = 5,<br />
    OrderCertificate / ServiceOrderCertificate = 5<br />

    Args:
        from_ (datetime.datetime):
        to (datetime.datetime):
        report_type (Optional[str]):
        service_order_id (Optional[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ServiceOrderDocumentsToCompanyOrderControlledDocumentResponse']]]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        report_type=report_type,
        service_order_id=service_order_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    from_: datetime.datetime,
    to: datetime.datetime,
    report_type: Optional[str] = None,
    service_order_id: Optional[int] = None,
) -> Optional[
    Union[
        Any,
        List["ServiceOrderDocumentsToCompanyOrderControlledDocumentResponse"],
    ]
]:
    """Retrieve work order documents

     Sample request:

    GET /api/service/workorders/documents/list

    GET /api/service/workorders/documents/list?status=reportType

    GET /api/service/workorders/documents/list?from=2020-12-01T10:11:12&amp;to=2021-01-
    01T10:11:12&amp;reportType=OrderInvoice&amp;ServiceOrderId=1

    reportType:<br />
    None = 0,<br />
    AssetSummary = 1,<br />
    AssetLabel = 11,<br />
    AssetDetail = 2,<br />
    AssetCertificate = 21,<br />
    OrderSummary / ServiceOrderSummary = 3,<br />
    OrderInvoice / ServiceOrderInvoice = 31,<br />
    OrderEstimate / ServiceOrderEstimate = 32,<br />
    Dashboard = 4,<br />
    OrderDetail / ServiceOrderDetail = 5,<br />
    OrderCertificate / ServiceOrderCertificate = 5<br />

    Args:
        from_ (datetime.datetime):
        to (datetime.datetime):
        report_type (Optional[str]):
        service_order_id (Optional[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['ServiceOrderDocumentsToCompanyOrderControlledDocumentResponse']]
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
            report_type=report_type,
            service_order_id=service_order_id,
        )
    ).parsed
