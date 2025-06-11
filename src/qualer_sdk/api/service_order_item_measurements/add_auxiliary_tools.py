from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_auxiliary_tools_response_200 import AddAuxiliaryToolsResponse200
from ...models.qualer_api_models_measurements_from_create_measurement_tool_model import (
    QualerApiModelsMeasurementsFromCreateMeasurementToolModel,
)
from ...types import Response


def _get_kwargs(
    work_item_id: int,
    *,
    body: list["QualerApiModelsMeasurementsFromCreateMeasurementToolModel"],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/service/workitems/{work_item_id}/AuxiliaryTools",
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AddAuxiliaryToolsResponse200]:
    if response.status_code == 200:
        response_200 = AddAuxiliaryToolsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AddAuxiliaryToolsResponse200]:
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
    body: list["QualerApiModelsMeasurementsFromCreateMeasurementToolModel"],
) -> Response[AddAuxiliaryToolsResponse200]:
    """
    Args:
        work_item_id (int):
        body (list['QualerApiModelsMeasurementsFromCreateMeasurementToolModel']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddAuxiliaryToolsResponse200]
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
    body: list["QualerApiModelsMeasurementsFromCreateMeasurementToolModel"],
) -> Optional[AddAuxiliaryToolsResponse200]:
    """
    Args:
        work_item_id (int):
        body (list['QualerApiModelsMeasurementsFromCreateMeasurementToolModel']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddAuxiliaryToolsResponse200
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
    body: list["QualerApiModelsMeasurementsFromCreateMeasurementToolModel"],
) -> Response[AddAuxiliaryToolsResponse200]:
    """
    Args:
        work_item_id (int):
        body (list['QualerApiModelsMeasurementsFromCreateMeasurementToolModel']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddAuxiliaryToolsResponse200]
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
    body: list["QualerApiModelsMeasurementsFromCreateMeasurementToolModel"],
) -> Optional[AddAuxiliaryToolsResponse200]:
    """
    Args:
        work_item_id (int):
        body (list['QualerApiModelsMeasurementsFromCreateMeasurementToolModel']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddAuxiliaryToolsResponse200
    """

    return (
        await asyncio_detailed(
            work_item_id=work_item_id,
            client=client,
            body=body,
        )
    ).parsed
