import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_measurements_to_measurement_record_response_model import (
    QualerApiModelsMeasurementsToMeasurementRecordResponseModel,
)
from ...types import Response


def _get_kwargs(
    asset_id: int,
    *,
    from_: Optional[datetime.datetime] = None,
    to: Optional[datetime.datetime] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_from_: Optional[str] = None
    if from_:
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: Optional[str] = None
    if to:
        json_to = to.isoformat()
    params["to"] = json_to

    params = {k: v for k, v in params.items() if v is not None and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/service/assets/{asset_id}/measurements",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["QualerApiModelsMeasurementsToMeasurementRecordResponseModel"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                QualerApiModelsMeasurementsToMeasurementRecordResponseModel.from_dict(
                    response_200_item_data
                )
            )

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["QualerApiModelsMeasurementsToMeasurementRecordResponseModel"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    from_: Optional[datetime.datetime] = None,
    to: Optional[datetime.datetime] = None,
) -> Response[List["QualerApiModelsMeasurementsToMeasurementRecordResponseModel"]]:
    """
    Args:
        asset_id (int):
        from_ (Optional[datetime.datetime]):
        to (Optional[datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['QualerApiModelsMeasurementsToMeasurementRecordResponseModel']]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        from_=from_,
        to=to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    from_: Optional[datetime.datetime] = None,
    to: Optional[datetime.datetime] = None,
) -> Optional[List["QualerApiModelsMeasurementsToMeasurementRecordResponseModel"]]:
    """
    Args:
        asset_id (int):
        from_ (Optional[datetime.datetime]):
        to (Optional[datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['QualerApiModelsMeasurementsToMeasurementRecordResponseModel']
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    asset_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    from_: Optional[datetime.datetime] = None,
    to: Optional[datetime.datetime] = None,
) -> Response[List["QualerApiModelsMeasurementsToMeasurementRecordResponseModel"]]:
    """
    Args:
        asset_id (int):
        from_ (Optional[datetime.datetime]):
        to (Optional[datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['QualerApiModelsMeasurementsToMeasurementRecordResponseModel']]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        from_=from_,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    from_: Optional[datetime.datetime] = None,
    to: Optional[datetime.datetime] = None,
) -> Optional[List["QualerApiModelsMeasurementsToMeasurementRecordResponseModel"]]:
    """
    Args:
        asset_id (int):
        from_ (Optional[datetime.datetime]):
        to (Optional[datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['QualerApiModelsMeasurementsToMeasurementRecordResponseModel']
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            from_=from_,
            to=to,
        )
    ).parsed
