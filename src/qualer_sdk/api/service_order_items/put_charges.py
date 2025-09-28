from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_charges_response_200 import PutChargesResponse200
from ...models.qualer_api_models_service_orders_from_item_charge_update_model import (
    ServiceOrdersFromItemChargeUpdateModel,
)
from ...types import Response


def _get_kwargs(
    work_item_id: int,
    *,
    body: ServiceOrdersFromItemChargeUpdateModel,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/api/service/workitems/{work_item_id}/charges",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PutChargesResponse200]:
    if response.status_code == 200:
        response_200 = PutChargesResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        response.raise_for_status()
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PutChargesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    work_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ServiceOrdersFromItemChargeUpdateModel,
) -> Response[PutChargesResponse200]:
    """Apply Service Order Item Charges

     Allowed Names:
        OverrideServiceTotal,
        OverridePartsTotal,
        OverrideRepairsTotal

    Args:
        work_item_id (int):
        body (ServiceOrdersFromItemChargeUpdateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutChargesResponse200]
    """

    kwargs = _get_kwargs(
        work_item_id=work_item_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    work_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ServiceOrdersFromItemChargeUpdateModel,
) -> Optional[PutChargesResponse200]:
    """Apply Service Order Item Charges

     Allowed Names:
        OverrideServiceTotal,
        OverridePartsTotal,
        OverrideRepairsTotal

    Args:
        work_item_id (int):
        body (ServiceOrdersFromItemChargeUpdateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutChargesResponse200
    """

    return sync_detailed(
        work_item_id=work_item_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    work_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ServiceOrdersFromItemChargeUpdateModel,
) -> Response[PutChargesResponse200]:
    """Apply Service Order Item Charges

     Allowed Names:
        OverrideServiceTotal,
        OverridePartsTotal,
        OverrideRepairsTotal

    Args:
        work_item_id (int):
        body (ServiceOrdersFromItemChargeUpdateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutChargesResponse200]
    """

    kwargs = _get_kwargs(
        work_item_id=work_item_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    work_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ServiceOrdersFromItemChargeUpdateModel,
) -> Optional[PutChargesResponse200]:
    """Apply Service Order Item Charges

     Allowed Names:
        OverrideServiceTotal,
        OverridePartsTotal,
        OverrideRepairsTotal

    Args:
        work_item_id (int):
        body (ServiceOrdersFromItemChargeUpdateModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutChargesResponse200
    """

    return (
        await asyncio_detailed(
            work_item_id=work_item_id,
            client=client,
            body=body,
        )
    ).parsed
