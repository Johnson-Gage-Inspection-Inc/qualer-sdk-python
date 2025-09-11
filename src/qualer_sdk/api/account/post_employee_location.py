from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_employee_location_response_200 import PostEmployeeLocationResponse200
from ...models.qualer_api_models_employees_from_employee_location_model import (
    QualerApiModelsEmployeesFromEmployeeLocationModel,
)
from ...types import Response


def _get_kwargs(
    *,
    body: QualerApiModelsEmployeesFromEmployeeLocationModel,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/user/location",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostEmployeeLocationResponse200]:
    if response.status_code == 200:
        response_200 = PostEmployeeLocationResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostEmployeeLocationResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsEmployeesFromEmployeeLocationModel,
) -> Response[PostEmployeeLocationResponse200]:
    """Post Employee Location

     Sample request:

    POST api/user/location

    Latitude - The latitude in degrees.<br />
    Longitude - The longitude in degrees.<br />
    Accuracy - The radius of uncertainty for the location, measured in meters.<br />
    Altitude - The altitude in meters above the WGS 84 reference ellipsoid.<br />
    AltitudeAccuracy - The accuracy of the altitude value, in meters.<br />
    Heading - Horizontal direction of travel of this device, measured in degrees starting at due north
    and continuing clockwise around the compass. Thus, north is 0 degrees, east is 90 degrees, south is
    180 degrees, and so on.<br />
    Speed - The instantaneous speed of the device in meters per second.<br />
    Timestamp - The time at which this position information was obtained, in seconds.

    Args:
        body (QualerApiModelsEmployeesFromEmployeeLocationModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostEmployeeLocationResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsEmployeesFromEmployeeLocationModel,
) -> Optional[PostEmployeeLocationResponse200]:
    """Post Employee Location

     Sample request:

    POST api/user/location

    Latitude - The latitude in degrees.<br />
    Longitude - The longitude in degrees.<br />
    Accuracy - The radius of uncertainty for the location, measured in meters.<br />
    Altitude - The altitude in meters above the WGS 84 reference ellipsoid.<br />
    AltitudeAccuracy - The accuracy of the altitude value, in meters.<br />
    Heading - Horizontal direction of travel of this device, measured in degrees starting at due north
    and continuing clockwise around the compass. Thus, north is 0 degrees, east is 90 degrees, south is
    180 degrees, and so on.<br />
    Speed - The instantaneous speed of the device in meters per second.<br />
    Timestamp - The time at which this position information was obtained, in seconds.

    Args:
        body (QualerApiModelsEmployeesFromEmployeeLocationModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostEmployeeLocationResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsEmployeesFromEmployeeLocationModel,
) -> Response[PostEmployeeLocationResponse200]:
    """Post Employee Location

     Sample request:

    POST api/user/location

    Latitude - The latitude in degrees.<br />
    Longitude - The longitude in degrees.<br />
    Accuracy - The radius of uncertainty for the location, measured in meters.<br />
    Altitude - The altitude in meters above the WGS 84 reference ellipsoid.<br />
    AltitudeAccuracy - The accuracy of the altitude value, in meters.<br />
    Heading - Horizontal direction of travel of this device, measured in degrees starting at due north
    and continuing clockwise around the compass. Thus, north is 0 degrees, east is 90 degrees, south is
    180 degrees, and so on.<br />
    Speed - The instantaneous speed of the device in meters per second.<br />
    Timestamp - The time at which this position information was obtained, in seconds.

    Args:
        body (QualerApiModelsEmployeesFromEmployeeLocationModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostEmployeeLocationResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QualerApiModelsEmployeesFromEmployeeLocationModel,
) -> Optional[PostEmployeeLocationResponse200]:
    """Post Employee Location

     Sample request:

    POST api/user/location

    Latitude - The latitude in degrees.<br />
    Longitude - The longitude in degrees.<br />
    Accuracy - The radius of uncertainty for the location, measured in meters.<br />
    Altitude - The altitude in meters above the WGS 84 reference ellipsoid.<br />
    AltitudeAccuracy - The accuracy of the altitude value, in meters.<br />
    Heading - Horizontal direction of travel of this device, measured in degrees starting at due north
    and continuing clockwise around the compass. Thus, north is 0 degrees, east is 90 degrees, south is
    180 degrees, and so on.<br />
    Speed - The instantaneous speed of the device in meters per second.<br />
    Timestamp - The time at which this position information was obtained, in seconds.

    Args:
        body (QualerApiModelsEmployeesFromEmployeeLocationModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostEmployeeLocationResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
