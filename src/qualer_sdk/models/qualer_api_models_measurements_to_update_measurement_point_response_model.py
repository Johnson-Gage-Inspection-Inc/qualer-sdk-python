from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.qualer_api_models_measurements_to_update_measurement_point_response_model_tolerance_mode import (
    MeasurementsToUpdateMeasurementPointResponseModelToleranceMode,
)
from ..models.qualer_api_models_measurements_to_update_measurement_point_response_model_tolerance_unit import (
    MeasurementsToUpdateMeasurementPointResponseModelToleranceUnit,
)

if TYPE_CHECKING:
    from ..models.qualer_api_models_measurements_to_update_measurement_condition_factor_response import (
        MeasurementsToUpdateMeasurementConditionFactorResponse,
    )
    from ..models.qualer_api_models_measurements_to_update_measurement_response_model import (
        MeasurementsToUpdateMeasurementResponseModel,
    )
    from ..models.qualer_api_models_measurements_to_update_measurement_tool_response_model import (
        MeasurementsToUpdateMeasurementToolResponseModel,
    )


T = TypeVar("T", bound="MeasurementsToUpdateMeasurementPointResponseModel")


@_attrs_define
class MeasurementsToUpdateMeasurementPointResponseModel:
    """
    Attributes:
        measurement_point_id (Optional[int]):
        specification_name (Optional[str]):
        unit_of_measure (Optional[str]):
        expected_value (Optional[float]):
        base_value (Optional[float]):
        test_value (Optional[float]):
        nominal (Optional[float]):
        range_min (Optional[float]):
        range_max (Optional[float]):
        tolerance_type (Optional[str]):
        tolerance_mode (Optional[MeasurementsToUpdateMeasurementPointResponseModelToleranceMode]):
        tolerance_unit (Optional[MeasurementsToUpdateMeasurementPointResponseModelToleranceUnit]):
        precision_type (Optional[str]):
        precision (Optional[float]):
        tolerance_minimum (Optional[float]):
        tolerance_maximum (Optional[float]):
        resolution (Optional[float]):
        resolution_count (Optional[float]):
        is_accredited (Optional[bool]):
        linked_measurement_point_id (Optional[int]):
        hysteresis_point (Optional[str]):
        hide_from_certificate (Optional[bool]):
        is_measurement_not_taken (Optional[bool]):
        measurement_not_taken_result (Optional[str]):
        measurement_not_taken_reason (Optional[str]):
        influence_parameter_1_parameter_id (Optional[int]):
        influence_parameter_1_value (Optional[str]):
        influence_parameter_2_parameter_id (Optional[int]):
        influence_parameter_2_value (Optional[str]):
        measurements (Optional[List['MeasurementsToUpdateMeasurementResponseModel']]):
        measurement_condition_factors (Optional[List['MeasurementsToUpdateMeasurementConditionFactorResponse']]):
        primary_measurement_tool (Optional[MeasurementsToUpdateMeasurementToolResponseModel]):
        secondary_measurement_tool (Optional[MeasurementsToUpdateMeasurementToolResponseModel]):
    """

    measurement_point_id: Optional[int] = None
    specification_name: Optional[str] = None
    unit_of_measure: Optional[str] = None
    expected_value: Optional[float] = None
    base_value: Optional[float] = None
    test_value: Optional[float] = None
    nominal: Optional[float] = None
    range_min: Optional[float] = None
    range_max: Optional[float] = None
    tolerance_type: Optional[str] = None
    tolerance_mode: Optional[MeasurementsToUpdateMeasurementPointResponseModelToleranceMode] = None
    tolerance_unit: Optional[MeasurementsToUpdateMeasurementPointResponseModelToleranceUnit] = None
    precision_type: Optional[str] = None
    precision: Optional[float] = None
    tolerance_minimum: Optional[float] = None
    tolerance_maximum: Optional[float] = None
    resolution: Optional[float] = None
    resolution_count: Optional[float] = None
    is_accredited: Optional[bool] = None
    linked_measurement_point_id: Optional[int] = None
    hysteresis_point: Optional[str] = None
    hide_from_certificate: Optional[bool] = None
    is_measurement_not_taken: Optional[bool] = None
    measurement_not_taken_result: Optional[str] = None
    measurement_not_taken_reason: Optional[str] = None
    influence_parameter_1_parameter_id: Optional[int] = None
    influence_parameter_1_value: Optional[str] = None
    influence_parameter_2_parameter_id: Optional[int] = None
    influence_parameter_2_value: Optional[str] = None
    measurements: Optional[List["MeasurementsToUpdateMeasurementResponseModel"]] = None
    measurement_condition_factors: Optional[
        List["MeasurementsToUpdateMeasurementConditionFactorResponse"]
    ] = None
    primary_measurement_tool: Optional["MeasurementsToUpdateMeasurementToolResponseModel"] = None
    secondary_measurement_tool: Optional["MeasurementsToUpdateMeasurementToolResponseModel"] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        measurement_point_id = self.measurement_point_id

        specification_name = self.specification_name

        unit_of_measure = self.unit_of_measure

        expected_value = self.expected_value

        base_value = self.base_value

        test_value = self.test_value

        nominal = self.nominal

        range_min = self.range_min

        range_max = self.range_max

        tolerance_type = self.tolerance_type

        tolerance_mode: Optional[int] = None
        if self.tolerance_mode:
            tolerance_mode = self.tolerance_mode.value

        tolerance_unit: Optional[int] = None
        if self.tolerance_unit:
            tolerance_unit = self.tolerance_unit.value

        precision_type = self.precision_type

        precision = self.precision

        tolerance_minimum = self.tolerance_minimum

        tolerance_maximum = self.tolerance_maximum

        resolution = self.resolution

        resolution_count = self.resolution_count

        is_accredited = self.is_accredited

        linked_measurement_point_id = self.linked_measurement_point_id

        hysteresis_point = self.hysteresis_point

        hide_from_certificate = self.hide_from_certificate

        is_measurement_not_taken = self.is_measurement_not_taken

        measurement_not_taken_result = self.measurement_not_taken_result

        measurement_not_taken_reason = self.measurement_not_taken_reason

        influence_parameter_1_parameter_id = self.influence_parameter_1_parameter_id

        influence_parameter_1_value = self.influence_parameter_1_value

        influence_parameter_2_parameter_id = self.influence_parameter_2_parameter_id

        influence_parameter_2_value = self.influence_parameter_2_value

        measurements: Optional[List[Dict[str, Any]]] = None
        if self.measurements:
            measurements = []
            for measurements_item_data in self.measurements:
                measurements_item = measurements_item_data.to_dict()
                measurements.append(measurements_item)

        measurement_condition_factors: Optional[List[Dict[str, Any]]] = None
        if self.measurement_condition_factors:
            measurement_condition_factors = []
            for measurement_condition_factors_item_data in self.measurement_condition_factors:
                measurement_condition_factors_item = (
                    measurement_condition_factors_item_data.to_dict()
                )
                measurement_condition_factors.append(measurement_condition_factors_item)

        primary_measurement_tool: Optional[Dict[str, Any]] = None
        if self.primary_measurement_tool:
            primary_measurement_tool = self.primary_measurement_tool.to_dict()

        secondary_measurement_tool: Optional[Dict[str, Any]] = None
        if self.secondary_measurement_tool:
            secondary_measurement_tool = self.secondary_measurement_tool.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measurement_point_id is not None:
            field_dict["MeasurementPointId"] = measurement_point_id
        if specification_name is not None:
            field_dict["SpecificationName"] = specification_name
        if unit_of_measure is not None:
            field_dict["UnitOfMeasure"] = unit_of_measure
        if expected_value is not None:
            field_dict["ExpectedValue"] = expected_value
        if base_value is not None:
            field_dict["BaseValue"] = base_value
        if test_value is not None:
            field_dict["TestValue"] = test_value
        if nominal is not None:
            field_dict["Nominal"] = nominal
        if range_min is not None:
            field_dict["RangeMin"] = range_min
        if range_max is not None:
            field_dict["RangeMax"] = range_max
        if tolerance_type is not None:
            field_dict["ToleranceType"] = tolerance_type
        if tolerance_mode is not None:
            field_dict["ToleranceMode"] = tolerance_mode
        if tolerance_unit is not None:
            field_dict["ToleranceUnit"] = tolerance_unit
        if precision_type is not None:
            field_dict["PrecisionType"] = precision_type
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
        if is_accredited is not None:
            field_dict["IsAccredited"] = is_accredited
        if linked_measurement_point_id is not None:
            field_dict["LinkedMeasurementPointId"] = linked_measurement_point_id
        if hysteresis_point is not None:
            field_dict["HysteresisPoint"] = hysteresis_point
        if hide_from_certificate is not None:
            field_dict["HideFromCertificate"] = hide_from_certificate
        if is_measurement_not_taken is not None:
            field_dict["IsMeasurementNotTaken"] = is_measurement_not_taken
        if measurement_not_taken_result is not None:
            field_dict["MeasurementNotTakenResult"] = measurement_not_taken_result
        if measurement_not_taken_reason is not None:
            field_dict["MeasurementNotTakenReason"] = measurement_not_taken_reason
        if influence_parameter_1_parameter_id is not None:
            field_dict["InfluenceParameter1ParameterId"] = influence_parameter_1_parameter_id
        if influence_parameter_1_value is not None:
            field_dict["InfluenceParameter1Value"] = influence_parameter_1_value
        if influence_parameter_2_parameter_id is not None:
            field_dict["InfluenceParameter2ParameterId"] = influence_parameter_2_parameter_id
        if influence_parameter_2_value is not None:
            field_dict["InfluenceParameter2Value"] = influence_parameter_2_value
        if measurements is not None:
            field_dict["Measurements"] = measurements
        if measurement_condition_factors is not None:
            field_dict["MeasurementConditionFactors"] = measurement_condition_factors
        if primary_measurement_tool is not None:
            field_dict["PrimaryMeasurementTool"] = primary_measurement_tool
        if secondary_measurement_tool is not None:
            field_dict["SecondaryMeasurementTool"] = secondary_measurement_tool

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_measurements_to_update_measurement_condition_factor_response import (
            MeasurementsToUpdateMeasurementConditionFactorResponse,
        )
        from ..models.qualer_api_models_measurements_to_update_measurement_response_model import (
            MeasurementsToUpdateMeasurementResponseModel,
        )
        from ..models.qualer_api_models_measurements_to_update_measurement_tool_response_model import (
            MeasurementsToUpdateMeasurementToolResponseModel,
        )

        d = dict(src_dict)
        measurement_point_id = d.pop("MeasurementPointId", None)

        specification_name = d.pop("SpecificationName", None)

        unit_of_measure = d.pop("UnitOfMeasure", None)

        expected_value = d.pop("ExpectedValue", None)

        base_value = d.pop("BaseValue", None)

        test_value = d.pop("TestValue", None)

        nominal = d.pop("Nominal", None)

        range_min = d.pop("RangeMin", None)

        range_max = d.pop("RangeMax", None)

        tolerance_type = d.pop("ToleranceType", None)

        _tolerance_mode = d.pop("ToleranceMode", None)
        tolerance_mode: Optional[MeasurementsToUpdateMeasurementPointResponseModelToleranceMode]
        if not _tolerance_mode:
            tolerance_mode = None
        elif _tolerance_mode is None:
            tolerance_mode = None
        else:
            # Handle string to integer mapping for IntEnum
            if isinstance(_tolerance_mode, str):
                tolerance_mode_map = {"Symmetric": 0, "Asymmetric": 1, "Range": 2}
                _tolerance_mode = tolerance_mode_map.get(_tolerance_mode, _tolerance_mode)
            tolerance_mode = MeasurementsToUpdateMeasurementPointResponseModelToleranceMode(
                _tolerance_mode
            )

        _tolerance_unit = d.pop("ToleranceUnit", None)
        tolerance_unit: Optional[MeasurementsToUpdateMeasurementPointResponseModelToleranceUnit]
        if not _tolerance_unit:
            tolerance_unit = None
        elif _tolerance_unit is None:
            tolerance_unit = None
        else:
            # Handle string to integer mapping for IntEnum
            if isinstance(_tolerance_unit, str):
                tolerance_unit_map = {
                    "Percentage": 0,
                    "UnitOfMeasure": 1,
                    "Readability": 2,
                }
                _tolerance_unit = tolerance_unit_map.get(_tolerance_unit, _tolerance_unit)
            tolerance_unit = MeasurementsToUpdateMeasurementPointResponseModelToleranceUnit(
                _tolerance_unit
            )

        precision_type = d.pop("PrecisionType", None)

        precision = d.pop("Precision", None)

        tolerance_minimum = d.pop("ToleranceMinimum", None)

        tolerance_maximum = d.pop("ToleranceMaximum", None)

        resolution = d.pop("Resolution", None)

        resolution_count = d.pop("ResolutionCount", None)

        is_accredited = d.pop("IsAccredited", None)

        linked_measurement_point_id = d.pop("LinkedMeasurementPointId", None)

        hysteresis_point = d.pop("HysteresisPoint", None)

        hide_from_certificate = d.pop("HideFromCertificate", None)

        is_measurement_not_taken = d.pop("IsMeasurementNotTaken", None)

        measurement_not_taken_result = d.pop("MeasurementNotTakenResult", None)

        measurement_not_taken_reason = d.pop("MeasurementNotTakenReason", None)

        influence_parameter_1_parameter_id = d.pop("InfluenceParameter1ParameterId", None)

        influence_parameter_1_value = d.pop("InfluenceParameter1Value", None)

        influence_parameter_2_parameter_id = d.pop("InfluenceParameter2ParameterId", None)

        influence_parameter_2_value = d.pop("InfluenceParameter2Value", None)

        measurements = []
        _measurements = d.pop("Measurements", None)
        for measurements_item_data in _measurements or []:
            measurements_item = MeasurementsToUpdateMeasurementResponseModel.from_dict(
                measurements_item_data
            )

            measurements.append(measurements_item)

        measurement_condition_factors = []
        _measurement_condition_factors = d.pop("MeasurementConditionFactors", None)
        for measurement_condition_factors_item_data in _measurement_condition_factors or []:
            measurement_condition_factors_item = (
                MeasurementsToUpdateMeasurementConditionFactorResponse.from_dict(
                    measurement_condition_factors_item_data
                )
            )

            measurement_condition_factors.append(measurement_condition_factors_item)

        _primary_measurement_tool = d.pop("PrimaryMeasurementTool", None)
        primary_measurement_tool: Optional[MeasurementsToUpdateMeasurementToolResponseModel]
        if not _primary_measurement_tool:
            primary_measurement_tool = None
        else:
            primary_measurement_tool = MeasurementsToUpdateMeasurementToolResponseModel.from_dict(
                _primary_measurement_tool
            )

        _secondary_measurement_tool = d.pop("SecondaryMeasurementTool", None)
        secondary_measurement_tool: Optional[MeasurementsToUpdateMeasurementToolResponseModel]
        if not _secondary_measurement_tool:
            secondary_measurement_tool = None
        else:
            secondary_measurement_tool = MeasurementsToUpdateMeasurementToolResponseModel.from_dict(
                _secondary_measurement_tool
            )

        qualer_api_models_measurements_to_update_measurement_point_response_model = cls(
            measurement_point_id=measurement_point_id,
            specification_name=specification_name,
            unit_of_measure=unit_of_measure,
            expected_value=expected_value,
            base_value=base_value,
            test_value=test_value,
            nominal=nominal,
            range_min=range_min,
            range_max=range_max,
            tolerance_type=tolerance_type,
            tolerance_mode=tolerance_mode,
            tolerance_unit=tolerance_unit,
            precision_type=precision_type,
            precision=precision,
            tolerance_minimum=tolerance_minimum,
            tolerance_maximum=tolerance_maximum,
            resolution=resolution,
            resolution_count=resolution_count,
            is_accredited=is_accredited,
            linked_measurement_point_id=linked_measurement_point_id,
            hysteresis_point=hysteresis_point,
            hide_from_certificate=hide_from_certificate,
            is_measurement_not_taken=is_measurement_not_taken,
            measurement_not_taken_result=measurement_not_taken_result,
            measurement_not_taken_reason=measurement_not_taken_reason,
            influence_parameter_1_parameter_id=influence_parameter_1_parameter_id,
            influence_parameter_1_value=influence_parameter_1_value,
            influence_parameter_2_parameter_id=influence_parameter_2_parameter_id,
            influence_parameter_2_value=influence_parameter_2_value,
            measurements=measurements,
            measurement_condition_factors=measurement_condition_factors,
            primary_measurement_tool=primary_measurement_tool,
            secondary_measurement_tool=secondary_measurement_tool,
        )

        qualer_api_models_measurements_to_update_measurement_point_response_model.additional_properties = (
            d
        )
        return qualer_api_models_measurements_to_update_measurement_point_response_model

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
