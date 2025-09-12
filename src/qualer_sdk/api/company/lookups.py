from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lookups_lookup_type import LookupsLookupType
from ...types import Response


def _get_kwargs(
    *,
    lookup_type: LookupsLookupType,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_lookup_type = lookup_type.value
    params["lookupType"] = json_lookup_type

    params = {k: v for k, v in params.items() if v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/company/lookups",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List[str]]:
    if response.status_code == 200:
        response_200 = cast(List[str], response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List[str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    lookup_type: LookupsLookupType,
) -> Response[List[str]]:
    """lookupName:
    AssetClass = 1
    AssetCriticality = 2
    AssetCondition = 3
    InventoryCategory = 4
    InventoryUnit = 5
    OrderItemInProgressWorkStatus = 6
    OrderItemDelayWorkStatus = 7
    OrderItemWithdrawnWorkStatus = 8
    OrderItemCompletedWorkStatus = 9
    OrderDelayedStatus = 10
    ClientInvoicing = 11
    ClientStanding = 12
    ClientCategory = 13
    CancelOrderReasons = 14
    OrderItemLockedWorkStatus = 15

    Args:
        lookup_type (LookupsLookupType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[str]]
    """

    kwargs = _get_kwargs(
        lookup_type=lookup_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    lookup_type: LookupsLookupType,
) -> Optional[List[str]]:
    """lookupName:
    AssetClass = 1
    AssetCriticality = 2
    AssetCondition = 3
    InventoryCategory = 4
    InventoryUnit = 5
    OrderItemInProgressWorkStatus = 6
    OrderItemDelayWorkStatus = 7
    OrderItemWithdrawnWorkStatus = 8
    OrderItemCompletedWorkStatus = 9
    OrderDelayedStatus = 10
    ClientInvoicing = 11
    ClientStanding = 12
    ClientCategory = 13
    CancelOrderReasons = 14
    OrderItemLockedWorkStatus = 15

    Args:
        lookup_type (LookupsLookupType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List[str]
    """

    return sync_detailed(
        client=client,
        lookup_type=lookup_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    lookup_type: LookupsLookupType,
) -> Response[List[str]]:
    """lookupName:
    AssetClass = 1
    AssetCriticality = 2
    AssetCondition = 3
    InventoryCategory = 4
    InventoryUnit = 5
    OrderItemInProgressWorkStatus = 6
    OrderItemDelayWorkStatus = 7
    OrderItemWithdrawnWorkStatus = 8
    OrderItemCompletedWorkStatus = 9
    OrderDelayedStatus = 10
    ClientInvoicing = 11
    ClientStanding = 12
    ClientCategory = 13
    CancelOrderReasons = 14
    OrderItemLockedWorkStatus = 15

    Args:
        lookup_type (LookupsLookupType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[str]]
    """

    kwargs = _get_kwargs(
        lookup_type=lookup_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    lookup_type: LookupsLookupType,
) -> Optional[List[str]]:
    """lookupName:
    AssetClass = 1
    AssetCriticality = 2
    AssetCondition = 3
    InventoryCategory = 4
    InventoryUnit = 5
    OrderItemInProgressWorkStatus = 6
    OrderItemDelayWorkStatus = 7
    OrderItemWithdrawnWorkStatus = 8
    OrderItemCompletedWorkStatus = 9
    OrderDelayedStatus = 10
    ClientInvoicing = 11
    ClientStanding = 12
    ClientCategory = 13
    CancelOrderReasons = 14
    OrderItemLockedWorkStatus = 15

    Args:
        lookup_type (LookupsLookupType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List[str]
    """

    return (
        await asyncio_detailed(
            client=client,
            lookup_type=lookup_type,
        )
    ).parsed
