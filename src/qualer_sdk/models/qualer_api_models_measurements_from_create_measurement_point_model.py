from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualer_api_models_measurements_from_create_measurement_condition_factor_model import (
        QualerApiModelsMeasurementsFromCreateMeasurementConditionFactorModel,
    )
    from ..models.qualer_api_models_measurements_from_create_measurement_model import (
        QualerApiModelsMeasurementsFromCreateMeasurementModel,
    )
    from ..models.qualer_api_models_measurements_from_create_measurement_tool_model import (
        QualerApiModelsMeasurementsFromCreateMeasurementToolModel,
    )


T = TypeVar("T", bound="QualerApiModelsMeasurementsFromCreateMeasurementPointModel")


@_attrs_define
class QualerApiModelsMeasurementsFromCreateMeasurementPointModel:
    """
    Attributes:
        specification_name (Union[Unset, str]):
        measurement_quantity (Union[Unset, str]):
        unit_of_measure_id (Union[Unset, int]):
        unit_of_measure (Union[Unset, str]):
        range_min (Union[Unset, float]):
        range_max (Union[Unset, float]):
        specification_mode (Union[Unset, str]):
        tolerance_type (Union[Unset, str]):
        tolerance_mode (Union[Unset, str]):
        tolerance_unit (Union[Unset, str]):
        precision_type (Union[Unset, str]):
        readings (Union[Unset, int]):
        channels_type (Union[Unset, str]):
        channel_count (Union[Unset, int]):
        precision (Union[Unset, float]):
        tolerance_minimum (Union[Unset, float]):
        tolerance_maximum (Union[Unset, float]):
        resolution (Union[Unset, float]):
        resolution_count (Union[Unset, float]):
        nominal (Union[Unset, float]):
        expected_value (Union[Unset, float]):
        base_value (Union[Unset, float]):
        test_value (Union[Unset, float]):
        is_accredited (Union[Unset, bool]):
        measurements (Union[Unset, list['QualerApiModelsMeasurementsFromCreateMeasurementModel']]):
        condition_factors (Union[Unset, list['QualerApiModelsMeasurementsFromCreateMeasurementConditionFactorModel']]):
        primary_measurement_tool (Union[Unset, QualerApiModelsMeasurementsFromCreateMeasurementToolModel]):
        secondary_measurement_tool (Union[Unset, QualerApiModelsMeasurementsFromCreateMeasurementToolModel]):
    """

    specification_name: Union[Unset, str] = UNSET
    measurement_quantity: Union[Unset, str] = UNSET
    unit_of_measure_id: Union[Unset, int] = UNSET
    unit_of_measure: Union[Unset, str] = UNSET
    range_min: Union[Unset, float] = UNSET
    range_max: Union[Unset, float] = UNSET
    specification_mode: Union[Unset, str] = UNSET
    tolerance_type: Union[Unset, str] = UNSET
    tolerance_mode: Union[Unset, str] = UNSET
    tolerance_unit: Union[Unset, str] = UNSET
    precision_type: Union[Unset, str] = UNSET
    readings: Union[Unset, int] = UNSET
    channels_type: Union[Unset, str] = UNSET
    channel_count: Union[Unset, int] = UNSET
    precision: Union[Unset, float] = UNSET
    tolerance_minimum: Union[Unset, float] = UNSET
    tolerance_maximum: Union[Unset, float] = UNSET
    resolution: Union[Unset, float] = UNSET
    resolution_count: Union[Unset, float] = UNSET
    nominal: Union[Unset, float] = UNSET
    expected_value: Union[Unset, float] = UNSET
    base_value: Union[Unset, float] = UNSET
    test_value: Union[Unset, float] = UNSET
    is_accredited: Union[Unset, bool] = UNSET
    measurements: Union[
        Unset, list["QualerApiModelsMeasurementsFromCreateMeasurementModel"]
    ] = UNSET
    condition_factors: Union[
        Unset,
        list["QualerApiModelsMeasurementsFromCreateMeasurementConditionFactorModel"],
    ] = UNSET
    primary_measurement_tool: Union[
        Unset, "QualerApiModelsMeasurementsFromCreateMeasurementToolModel"
    ] = UNSET
    secondary_measurement_tool: Union[
        Unset, "QualerApiModelsMeasurementsFromCreateMeasurementToolModel"
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        specification_name = self.specification_name

        measurement_quantity = self.measurement_quantity

        unit_of_measure_id = self.unit_of_measure_id

        unit_of_measure = self.unit_of_measure

        range_min = self.range_min

        range_max = self.range_max

        specification_mode = self.specification_mode

        tolerance_type = self.tolerance_type

        tolerance_mode = self.tolerance_mode

        tolerance_unit = self.tolerance_unit

        precision_type = self.precision_type

        readings = self.readings

        channels_type = self.channels_type

        channel_count = self.channel_count

        precision = self.precision

        tolerance_minimum = self.tolerance_minimum

        tolerance_maximum = self.tolerance_maximum

        resolution = self.resolution

        resolution_count = self.resolution_count

        nominal = self.nominal

        expected_value = self.expected_value

        base_value = self.base_value

        test_value = self.test_value

        is_accredited = self.is_accredited

        measurements: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.measurements, Unset):
            measurements = []
            for measurements_item_data in self.measurements:
                measurements_item = measurements_item_data.to_dict()
                measurements.append(measurements_item)

        condition_factors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.condition_factors, Unset):
            condition_factors = []
            for condition_factors_item_data in self.condition_factors:
                condition_factors_item = condition_factors_item_data.to_dict()
                condition_factors.append(condition_factors_item)

        primary_measurement_tool: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.primary_measurement_tool, Unset):
            primary_measurement_tool = self.primary_measurement_tool.to_dict()

        secondary_measurement_tool: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.secondary_measurement_tool, Unset):
            secondary_measurement_tool = self.secondary_measurement_tool.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if specification_name is not UNSET:
            field_dict["SpecificationName"] = specification_name
        if measurement_quantity is not UNSET:
            field_dict["MeasurementQuantity"] = measurement_quantity
        if unit_of_measure_id is not UNSET:
            field_dict["UnitOfMeasureId"] = unit_of_measure_id
        if unit_of_measure is not UNSET:
            field_dict["UnitOfMeasure"] = unit_of_measure
        if range_min is not UNSET:
            field_dict["RangeMin"] = range_min
        if range_max is not UNSET:
            field_dict["RangeMax"] = range_max
        if specification_mode is not UNSET:
            field_dict["SpecificationMode"] = specification_mode
        if tolerance_type is not UNSET:
            field_dict["ToleranceType"] = tolerance_type
        if tolerance_mode is not UNSET:
            field_dict["ToleranceMode"] = tolerance_mode
        if tolerance_unit is not UNSET:
            field_dict["ToleranceUnit"] = tolerance_unit
        if precision_type is not UNSET:
            field_dict["PrecisionType"] = precision_type
        if readings is not UNSET:
            field_dict["Readings"] = readings
        if channels_type is not UNSET:
            field_dict["ChannelsType"] = channels_type
        if channel_count is not UNSET:
            field_dict["ChannelCount"] = channel_count
        if precision is not UNSET:
            field_dict["Precision"] = precision
        if tolerance_minimum is not UNSET:
            field_dict["ToleranceMinimum"] = tolerance_minimum
        if tolerance_maximum is not UNSET:
            field_dict["ToleranceMaximum"] = tolerance_maximum
        if resolution is not UNSET:
            field_dict["Resolution"] = resolution
        if resolution_count is not UNSET:
            field_dict["ResolutionCount"] = resolution_count
        if nominal is not UNSET:
            field_dict["Nominal"] = nominal
        if expected_value is not UNSET:
            field_dict["ExpectedValue"] = expected_value
        if base_value is not UNSET:
            field_dict["BaseValue"] = base_value
        if test_value is not UNSET:
            field_dict["TestValue"] = test_value
        if is_accredited is not UNSET:
            field_dict["IsAccredited"] = is_accredited
        if measurements is not UNSET:
            field_dict["Measurements"] = measurements
        if condition_factors is not UNSET:
            field_dict["ConditionFactors"] = condition_factors
        if primary_measurement_tool is not UNSET:
            field_dict["PrimaryMeasurementTool"] = primary_measurement_tool
        if secondary_measurement_tool is not UNSET:
            field_dict["SecondaryMeasurementTool"] = secondary_measurement_tool

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_measurements_from_create_measurement_condition_factor_model import (
            QualerApiModelsMeasurementsFromCreateMeasurementConditionFactorModel,
        )
        from ..models.qualer_api_models_measurements_from_create_measurement_model import (
            QualerApiModelsMeasurementsFromCreateMeasurementModel,
        )
        from ..models.qualer_api_models_measurements_from_create_measurement_tool_model import (
            QualerApiModelsMeasurementsFromCreateMeasurementToolModel,
        )

        d = dict(src_dict)
        specification_name = d.pop("SpecificationName", UNSET)

        measurement_quantity = d.pop("MeasurementQuantity", UNSET)

        unit_of_measure_id = d.pop("UnitOfMeasureId", UNSET)

        unit_of_measure = d.pop("UnitOfMeasure", UNSET)

        range_min = d.pop("RangeMin", UNSET)

        range_max = d.pop("RangeMax", UNSET)

        specification_mode = d.pop("SpecificationMode", UNSET)

        tolerance_type = d.pop("ToleranceType", UNSET)

        tolerance_mode = d.pop("ToleranceMode", UNSET)

        tolerance_unit = d.pop("ToleranceUnit", UNSET)

        precision_type = d.pop("PrecisionType", UNSET)

        readings = d.pop("Readings", UNSET)

        channels_type = d.pop("ChannelsType", UNSET)

        channel_count = d.pop("ChannelCount", UNSET)

        precision = d.pop("Precision", UNSET)

        tolerance_minimum = d.pop("ToleranceMinimum", UNSET)

        tolerance_maximum = d.pop("ToleranceMaximum", UNSET)

        resolution = d.pop("Resolution", UNSET)

        resolution_count = d.pop("ResolutionCount", UNSET)

        nominal = d.pop("Nominal", UNSET)

        expected_value = d.pop("ExpectedValue", UNSET)

        base_value = d.pop("BaseValue", UNSET)

        test_value = d.pop("TestValue", UNSET)

        is_accredited = d.pop("IsAccredited", UNSET)

        measurements = []
        _measurements = d.pop("Measurements", UNSET)
        for measurements_item_data in _measurements or []:
            measurements_item = (
                QualerApiModelsMeasurementsFromCreateMeasurementModel.from_dict(
                    measurements_item_data
                )
            )

            measurements.append(measurements_item)

        condition_factors = []
        _condition_factors = d.pop("ConditionFactors", UNSET)
        for condition_factors_item_data in _condition_factors or []:
            condition_factors_item = QualerApiModelsMeasurementsFromCreateMeasurementConditionFactorModel.from_dict(
                condition_factors_item_data
            )

            condition_factors.append(condition_factors_item)

        _primary_measurement_tool = d.pop("PrimaryMeasurementTool", UNSET)
        primary_measurement_tool: Union[
            Unset, QualerApiModelsMeasurementsFromCreateMeasurementToolModel
        ]
        if isinstance(_primary_measurement_tool, Unset):
            primary_measurement_tool = UNSET
        else:
            primary_measurement_tool = (
                QualerApiModelsMeasurementsFromCreateMeasurementToolModel.from_dict(
                    _primary_measurement_tool
                )
            )

        _secondary_measurement_tool = d.pop("SecondaryMeasurementTool", UNSET)
        secondary_measurement_tool: Union[
            Unset, QualerApiModelsMeasurementsFromCreateMeasurementToolModel
        ]
        if isinstance(_secondary_measurement_tool, Unset):
            secondary_measurement_tool = UNSET
        else:
            secondary_measurement_tool = (
                QualerApiModelsMeasurementsFromCreateMeasurementToolModel.from_dict(
                    _secondary_measurement_tool
                )
            )

        qualer_api_models_measurements_from_create_measurement_point_model = cls(
            specification_name=specification_name,
            measurement_quantity=measurement_quantity,
            unit_of_measure_id=unit_of_measure_id,
            unit_of_measure=unit_of_measure,
            range_min=range_min,
            range_max=range_max,
            specification_mode=specification_mode,
            tolerance_type=tolerance_type,
            tolerance_mode=tolerance_mode,
            tolerance_unit=tolerance_unit,
            precision_type=precision_type,
            readings=readings,
            channels_type=channels_type,
            channel_count=channel_count,
            precision=precision,
            tolerance_minimum=tolerance_minimum,
            tolerance_maximum=tolerance_maximum,
            resolution=resolution,
            resolution_count=resolution_count,
            nominal=nominal,
            expected_value=expected_value,
            base_value=base_value,
            test_value=test_value,
            is_accredited=is_accredited,
            measurements=measurements,
            condition_factors=condition_factors,
            primary_measurement_tool=primary_measurement_tool,
            secondary_measurement_tool=secondary_measurement_tool,
        )

        qualer_api_models_measurements_from_create_measurement_point_model.additional_properties = (
            d
        )
        return qualer_api_models_measurements_from_create_measurement_point_model

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
