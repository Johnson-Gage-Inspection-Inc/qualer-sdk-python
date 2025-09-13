from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.qualer_api_models_measurements_from_create_measurement_point_model_tolerance_mode import (
    MeasurementsFromCreateMeasurementPointModelToleranceMode,
)
from ..models.qualer_api_models_measurements_from_create_measurement_point_model_tolerance_unit import (
    MeasurementsFromCreateMeasurementPointModelToleranceUnit,
)

if TYPE_CHECKING:
    from ..models.qualer_api_models_measurements_from_create_measurement_condition_factor_model import (
        MeasurementsFromCreateMeasurementConditionFactorModel,
    )
    from ..models.qualer_api_models_measurements_from_create_measurement_model import (
        MeasurementsFromCreateMeasurementModel,
    )
    from ..models.qualer_api_models_measurements_from_create_measurement_tool_model import (
        MeasurementsFromCreateMeasurementToolModel,
    )


T = TypeVar("T", bound="MeasurementsFromCreateMeasurementPointModel")


@_attrs_define
class MeasurementsFromCreateMeasurementPointModel:
    """
    Attributes:
        specification_name (Optional[str]):
        measurement_quantity (Optional[str]):
        unit_of_measure_id (Optional[int]):
        unit_of_measure (Optional[str]):
        range_min (Optional[float]):
        range_max (Optional[float]):
        specification_mode (Optional[int]):
        tolerance_type (Optional[str]):
        tolerance_mode (Optional[MeasurementsFromCreateMeasurementPointModelToleranceMode]):
        tolerance_unit (Optional[MeasurementsFromCreateMeasurementPointModelToleranceUnit]):
        precision_type (Optional[str]):
        readings (Optional[int]):
        channels_type (Optional[str]):
        channel_count (Optional[int]):
        precision (Optional[float]):
        tolerance_minimum (Optional[float]):
        tolerance_maximum (Optional[float]):
        resolution (Optional[float]):
        resolution_count (Optional[float]):
        nominal (Optional[float]):
        expected_value (Optional[float]):
        base_value (Optional[float]):
        test_value (Optional[float]):
        is_accredited (Optional[bool]):
        measurements (Optional[List['MeasurementsFromCreateMeasurementModel']]):
        condition_factors (Optional[List['MeasurementsFromCreateMeasurementConditionFactorModel']]):
        primary_measurement_tool (Optional[MeasurementsFromCreateMeasurementToolModel]):
        secondary_measurement_tool (Optional[MeasurementsFromCreateMeasurementToolModel]):
    """

    specification_name: Optional[str] = None
    measurement_quantity: Optional[str] = None
    unit_of_measure_id: Optional[int] = None
    unit_of_measure: Optional[str] = None
    range_min: Optional[float] = None
    range_max: Optional[float] = None
    specification_mode: Optional[int] = None
    tolerance_type: Optional[str] = None
    tolerance_mode: Union[
        None,
        None,
        MeasurementsFromCreateMeasurementPointModelToleranceMode,
    ] = None
    tolerance_unit: Union[
        None,
        None,
        MeasurementsFromCreateMeasurementPointModelToleranceUnit,
    ] = None
    precision_type: Optional[str] = None
    readings: Optional[int] = None
    channels_type: Optional[str] = None
    channel_count: Optional[int] = None
    precision: Optional[float] = None
    tolerance_minimum: Optional[float] = None
    tolerance_maximum: Optional[float] = None
    resolution: Optional[float] = None
    resolution_count: Optional[float] = None
    nominal: Optional[float] = None
    expected_value: Optional[float] = None
    base_value: Optional[float] = None
    test_value: Optional[float] = None
    is_accredited: Optional[bool] = None
    measurements: Union[None, List["MeasurementsFromCreateMeasurementModel"]] = None
    condition_factors: Union[
        None,
        None,
        List["MeasurementsFromCreateMeasurementConditionFactorModel"],
    ] = None
    primary_measurement_tool: Union[None, "MeasurementsFromCreateMeasurementToolModel"] = None
    secondary_measurement_tool: Union[None, "MeasurementsFromCreateMeasurementToolModel"] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        specification_name = self.specification_name

        measurement_quantity = self.measurement_quantity

        unit_of_measure_id = self.unit_of_measure_id

        unit_of_measure = self.unit_of_measure

        range_min = self.range_min

        range_max = self.range_max

        specification_mode = self.specification_mode

        tolerance_type = self.tolerance_type

        tolerance_mode: Optional[int] = None
        if self.tolerance_mode:
            tolerance_mode = self.tolerance_mode.value

        tolerance_unit: Optional[int] = None
        if self.tolerance_unit:
            tolerance_unit = self.tolerance_unit.value

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

        measurements: Optional[List[Dict[str, Any]]] = None
        if self.measurements:
            measurements = []
            for measurements_item_data in self.measurements:
                measurements_item = measurements_item_data.to_dict()
                measurements.append(measurements_item)

        condition_factors: Optional[List[Dict[str, Any]]] = None
        if self.condition_factors:
            condition_factors = []
            for condition_factors_item_data in self.condition_factors:
                condition_factors_item = condition_factors_item_data.to_dict()
                condition_factors.append(condition_factors_item)

        primary_measurement_tool: Optional[Dict[str, Any]] = None
        if self.primary_measurement_tool and not isinstance(self.primary_measurement_tool, None):
            primary_measurement_tool = self.primary_measurement_tool.to_dict()

        secondary_measurement_tool: Optional[Dict[str, Any]] = None
        if self.secondary_measurement_tool and not isinstance(
            self.secondary_measurement_tool, None
        ):
            secondary_measurement_tool = self.secondary_measurement_tool.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if specification_name is not None:
            field_dict["SpecificationName"] = specification_name
        if measurement_quantity is not None:
            field_dict["MeasurementQuantity"] = measurement_quantity
        if unit_of_measure_id is not None:
            field_dict["UnitOfMeasureId"] = unit_of_measure_id
        if unit_of_measure is not None:
            field_dict["UnitOfMeasure"] = unit_of_measure
        if range_min is not None:
            field_dict["RangeMin"] = range_min
        if range_max is not None:
            field_dict["RangeMax"] = range_max
        if specification_mode is not None:
            field_dict["SpecificationMode"] = specification_mode
        if tolerance_type is not None:
            field_dict["ToleranceType"] = tolerance_type
        if tolerance_mode is not None:
            field_dict["ToleranceMode"] = tolerance_mode
        if tolerance_unit is not None:
            field_dict["ToleranceUnit"] = tolerance_unit
        if precision_type is not None:
            field_dict["PrecisionType"] = precision_type
        if readings is not None:
            field_dict["Readings"] = readings
        if channels_type is not None:
            field_dict["ChannelsType"] = channels_type
        if channel_count is not None:
            field_dict["ChannelCount"] = channel_count
        if precision is not None:
            field_dict["Precision"] = precision
        if tolerance_minimum is not None:
            field_dict["ToleranceMinimum"] = tolerance_minimum
        if tolerance_maximum is not None:
            field_dict["ToleranceMaximum"] = tolerance_maximum
        if resolution is not None:
            field_dict["Resolution"] = resolution
        if resolution_count is not None:
            field_dict["ResolutionCount"] = resolution_count
        if nominal is not None:
            field_dict["Nominal"] = nominal
        if expected_value is not None:
            field_dict["ExpectedValue"] = expected_value
        if base_value is not None:
            field_dict["BaseValue"] = base_value
        if test_value is not None:
            field_dict["TestValue"] = test_value
        if is_accredited is not None:
            field_dict["IsAccredited"] = is_accredited
        if measurements is not None:
            field_dict["Measurements"] = measurements
        if condition_factors is not None:
            field_dict["ConditionFactors"] = condition_factors
        if primary_measurement_tool is not None:
            field_dict["PrimaryMeasurementTool"] = primary_measurement_tool
        if secondary_measurement_tool is not None:
            field_dict["SecondaryMeasurementTool"] = secondary_measurement_tool

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_measurements_from_create_measurement_condition_factor_model import (
            MeasurementsFromCreateMeasurementConditionFactorModel,
        )
        from ..models.qualer_api_models_measurements_from_create_measurement_model import (
            MeasurementsFromCreateMeasurementModel,
        )
        from ..models.qualer_api_models_measurements_from_create_measurement_tool_model import (
            MeasurementsFromCreateMeasurementToolModel,
        )

        d = dict(src_dict)
        specification_name = d.pop("SpecificationName", None)

        measurement_quantity = d.pop("MeasurementQuantity", None)

        unit_of_measure_id = d.pop("UnitOfMeasureId", None)

        unit_of_measure = d.pop("UnitOfMeasure", None)

        range_min = d.pop("RangeMin", None)

        range_max = d.pop("RangeMax", None)

        specification_mode = d.pop("SpecificationMode", None)

        tolerance_type = d.pop("ToleranceType", None)

        _tolerance_mode = d.pop("ToleranceMode", None)
        tolerance_mode: Union[
            None,
            None,
            MeasurementsFromCreateMeasurementPointModelToleranceMode,
        ]
        if not _tolerance_mode:
            tolerance_mode = None
        else:
            tolerance_mode = MeasurementsFromCreateMeasurementPointModelToleranceMode(
                _tolerance_mode
            )

        _tolerance_unit = d.pop("ToleranceUnit", None)
        tolerance_unit: Union[
            None,
            None,
            MeasurementsFromCreateMeasurementPointModelToleranceUnit,
        ]
        if not _tolerance_unit:
            tolerance_unit = None
        else:
            tolerance_unit = MeasurementsFromCreateMeasurementPointModelToleranceUnit(
                _tolerance_unit
            )

        precision_type = d.pop("PrecisionType", None)

        readings = d.pop("Readings", None)

        channels_type = d.pop("ChannelsType", None)

        channel_count = d.pop("ChannelCount", None)

        precision = d.pop("Precision", None)

        tolerance_minimum = d.pop("ToleranceMinimum", None)

        tolerance_maximum = d.pop("ToleranceMaximum", None)

        resolution = d.pop("Resolution", None)

        resolution_count = d.pop("ResolutionCount", None)

        nominal = d.pop("Nominal", None)

        expected_value = d.pop("ExpectedValue", None)

        base_value = d.pop("BaseValue", None)

        test_value = d.pop("TestValue", None)

        is_accredited = d.pop("IsAccredited", None)

        measurements = []
        _measurements = d.pop("Measurements", None)
        for measurements_item_data in _measurements or []:
            measurements_item = MeasurementsFromCreateMeasurementModel.from_dict(
                measurements_item_data
            )

            measurements.append(measurements_item)

        condition_factors = []
        _condition_factors = d.pop("ConditionFactors", None)
        for condition_factors_item_data in _condition_factors or []:
            condition_factors_item = (
                MeasurementsFromCreateMeasurementConditionFactorModel.from_dict(
                    condition_factors_item_data
                )
            )

            condition_factors.append(condition_factors_item)

        _primary_measurement_tool = d.pop("PrimaryMeasurementTool", None)
        primary_measurement_tool: Union[None, MeasurementsFromCreateMeasurementToolModel]
        if not _primary_measurement_tool:
            primary_measurement_tool = None
        else:
            primary_measurement_tool = MeasurementsFromCreateMeasurementToolModel.from_dict(
                _primary_measurement_tool
            )

        _secondary_measurement_tool = d.pop("SecondaryMeasurementTool", None)
        secondary_measurement_tool: Union[None, MeasurementsFromCreateMeasurementToolModel]
        if not _secondary_measurement_tool:
            secondary_measurement_tool = None
        else:
            secondary_measurement_tool = MeasurementsFromCreateMeasurementToolModel.from_dict(
                _secondary_measurement_tool
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

        qualer_api_models_measurements_from_create_measurement_point_model.additional_properties = d
        return qualer_api_models_measurements_from_create_measurement_point_model

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
