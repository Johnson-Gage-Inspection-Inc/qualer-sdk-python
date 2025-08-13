import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_measurements_to_measurement_record_response_model import (
    QualerApiModelsMeasurementsToMeasurementRecordResponseModel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: int,
    *,
    from_: Union[None, Unset, datetime.datetime] = UNSET,
    to: Union[None, Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_from_: Union[None, Unset, str] = UNSET
    if from_ and not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: Union[None, Unset, str] = UNSET
    if to and not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/assets/{asset_id}/measurements",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["QualerApiModelsMeasurementsToMeasurementRecordResponseModel"]]:
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
) -> Response[list["QualerApiModelsMeasurementsToMeasurementRecordResponseModel"]]:
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
    from_: Union[None, Unset, datetime.datetime] = UNSET,
    to: Union[None, Unset, datetime.datetime] = UNSET,
) -> Response[list["QualerApiModelsMeasurementsToMeasurementRecordResponseModel"]]:
    """
    Args:
        asset_id (int):
        from_ (Union[None, Unset, datetime.datetime]):
        to (Union[None, Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsMeasurementsToMeasurementRecordResponseModel']]
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
    from_: Union[None, Unset, datetime.datetime] = UNSET,
    to: Union[None, Unset, datetime.datetime] = UNSET,
) -> Optional[list["QualerApiModelsMeasurementsToMeasurementRecordResponseModel"]]:
    """
    Args:
        asset_id (int):
        from_ (Union[None, Unset, datetime.datetime]):
        to (Union[None, Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsMeasurementsToMeasurementRecordResponseModel']
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
    from_: Union[None, Unset, datetime.datetime] = UNSET,
    to: Union[None, Unset, datetime.datetime] = UNSET,
) -> Response[list["QualerApiModelsMeasurementsToMeasurementRecordResponseModel"]]:
    """
    Args:
        asset_id (int):
        from_ (Union[None, Unset, datetime.datetime]):
        to (Union[None, Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QualerApiModelsMeasurementsToMeasurementRecordResponseModel']]
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
    from_: Union[None, Unset, datetime.datetime] = UNSET,
    to: Union[None, Unset, datetime.datetime] = UNSET,
) -> Optional[list["QualerApiModelsMeasurementsToMeasurementRecordResponseModel"]]:
    """
    Args:
        asset_id (int):
        from_ (Union[None, Unset, datetime.datetime]):
        to (Union[None, Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QualerApiModelsMeasurementsToMeasurementRecordResponseModel']
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            from_=from_,
            to=to,
        )
    ).parsed
