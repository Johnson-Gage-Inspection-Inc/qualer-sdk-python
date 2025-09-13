from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_measurement_form_response_200 import CreateMeasurementFormResponse200
from ...models.qualer_api_models_measurements_from_create_measurement_form_model import (
    MeasurementsFromCreateMeasurementFormModel,
)
from ...types import Response


def _get_kwargs(
    work_item_id: int,
    *,
    body: MeasurementsFromCreateMeasurementFormModel,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/service/workitems/{work_item_id}/measurements",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateMeasurementFormResponse200]]:
    if response.status_code == 200:
        response_200 = CreateMeasurementFormResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, CreateMeasurementFormResponse200]]:
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
    body: MeasurementsFromCreateMeasurementFormModel,
) -> Response[Union[Any, CreateMeasurementFormResponse200]]:
    """Create Measurement Form.

     BatchType: AsLeft, AsFound.

    BatchResult: NotServiced, Fail, FailAmbiguous, FailSignificant, Pass, PassAmbiguous, PassAdjustment,
    Done, Pending.

    CustomFields.Result: NotServiced, Fail, Pass.

    ToleranceType: Percentage, Range, Offset, PercentagePlus, Ppm, PpmPlus, Function.

    ToleranceMode: Symmetric, Asymmetric, Range.

    ToleranceUnit: Percentage, UnitOfMeasure, Ppm.

    PrecisionType: Percentage, UnitOfMeasure.

    ChannelsType: Combined, IndividualAcross, IndividualDown, OneOf.

    Measurement.Result: NotServiced, Fail, FailAmbiguous, FailSignificant, Pass, PassAmbiguous,
    PassAdjustment, Done, Pending.

    FactorId: AmbientTemperature, AirHumidity, BarometricPressure, EvaporationRate, AirBuoyancy,
    ZFactor, Altitude, WindSpeed, SolarRadiation, LightIntensity, NoiseLevel, PhLevel,
    WaterConductivity3, WaterTemperature.

    Args:
        work_item_id (int):
        body (MeasurementsFromCreateMeasurementFormModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateMeasurementFormResponse200]]
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
    body: MeasurementsFromCreateMeasurementFormModel,
) -> Optional[Union[Any, CreateMeasurementFormResponse200]]:
    """Create Measurement Form.

     BatchType: AsLeft, AsFound.

    BatchResult: NotServiced, Fail, FailAmbiguous, FailSignificant, Pass, PassAmbiguous, PassAdjustment,
    Done, Pending.

    CustomFields.Result: NotServiced, Fail, Pass.

    ToleranceType: Percentage, Range, Offset, PercentagePlus, Ppm, PpmPlus, Function.

    ToleranceMode: Symmetric, Asymmetric, Range.

    ToleranceUnit: Percentage, UnitOfMeasure, Ppm.

    PrecisionType: Percentage, UnitOfMeasure.

    ChannelsType: Combined, IndividualAcross, IndividualDown, OneOf.

    Measurement.Result: NotServiced, Fail, FailAmbiguous, FailSignificant, Pass, PassAmbiguous,
    PassAdjustment, Done, Pending.

    FactorId: AmbientTemperature, AirHumidity, BarometricPressure, EvaporationRate, AirBuoyancy,
    ZFactor, Altitude, WindSpeed, SolarRadiation, LightIntensity, NoiseLevel, PhLevel,
    WaterConductivity3, WaterTemperature.

    Args:
        work_item_id (int):
        body (MeasurementsFromCreateMeasurementFormModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateMeasurementFormResponse200]
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
    body: MeasurementsFromCreateMeasurementFormModel,
) -> Response[Union[Any, CreateMeasurementFormResponse200]]:
    """Create Measurement Form.

     BatchType: AsLeft, AsFound.

    BatchResult: NotServiced, Fail, FailAmbiguous, FailSignificant, Pass, PassAmbiguous, PassAdjustment,
    Done, Pending.

    CustomFields.Result: NotServiced, Fail, Pass.

    ToleranceType: Percentage, Range, Offset, PercentagePlus, Ppm, PpmPlus, Function.

    ToleranceMode: Symmetric, Asymmetric, Range.

    ToleranceUnit: Percentage, UnitOfMeasure, Ppm.

    PrecisionType: Percentage, UnitOfMeasure.

    ChannelsType: Combined, IndividualAcross, IndividualDown, OneOf.

    Measurement.Result: NotServiced, Fail, FailAmbiguous, FailSignificant, Pass, PassAmbiguous,
    PassAdjustment, Done, Pending.

    FactorId: AmbientTemperature, AirHumidity, BarometricPressure, EvaporationRate, AirBuoyancy,
    ZFactor, Altitude, WindSpeed, SolarRadiation, LightIntensity, NoiseLevel, PhLevel,
    WaterConductivity3, WaterTemperature.

    Args:
        work_item_id (int):
        body (MeasurementsFromCreateMeasurementFormModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateMeasurementFormResponse200]]
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
    body: MeasurementsFromCreateMeasurementFormModel,
) -> Optional[Union[Any, CreateMeasurementFormResponse200]]:
    """Create Measurement Form.

     BatchType: AsLeft, AsFound.

    BatchResult: NotServiced, Fail, FailAmbiguous, FailSignificant, Pass, PassAmbiguous, PassAdjustment,
    Done, Pending.

    CustomFields.Result: NotServiced, Fail, Pass.

    ToleranceType: Percentage, Range, Offset, PercentagePlus, Ppm, PpmPlus, Function.

    ToleranceMode: Symmetric, Asymmetric, Range.

    ToleranceUnit: Percentage, UnitOfMeasure, Ppm.

    PrecisionType: Percentage, UnitOfMeasure.

    ChannelsType: Combined, IndividualAcross, IndividualDown, OneOf.

    Measurement.Result: NotServiced, Fail, FailAmbiguous, FailSignificant, Pass, PassAmbiguous,
    PassAdjustment, Done, Pending.

    FactorId: AmbientTemperature, AirHumidity, BarometricPressure, EvaporationRate, AirBuoyancy,
    ZFactor, Altitude, WindSpeed, SolarRadiation, LightIntensity, NoiseLevel, PhLevel,
    WaterConductivity3, WaterTemperature.

    Args:
        work_item_id (int):
        body (MeasurementsFromCreateMeasurementFormModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateMeasurementFormResponse200]
    """

    return (
        await asyncio_detailed(
            work_item_id=work_item_id,
            client=client,
            body=body,
        )
    ).parsed
