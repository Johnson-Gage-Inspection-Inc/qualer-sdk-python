from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.qualer_api_models_measurements_from_update_measurement_point_model_hysteresis_point import (
    MeasurementsFromUpdateMeasurementPointModelHysteresisPoint,
)
from ..models.qualer_api_models_measurements_from_update_measurement_point_model_specification_mode import (
    MeasurementsFromUpdateMeasurementPointModelSpecificationMode,
)
from ..models.qualer_api_models_measurements_from_update_measurement_point_model_tolerance_mode import (
    MeasurementsFromUpdateMeasurementPointModelToleranceMode,
)
from ..models.qualer_api_models_measurements_from_update_measurement_point_model_tolerance_unit import (
    MeasurementsFromUpdateMeasurementPointModelToleranceUnit,
)
from ..models.qualer_api_models_measurements_from_update_measurement_point_model_tool_application_mode import (
    MeasurementsFromUpdateMeasurementPointModelToolApplicationMode,
)

if TYPE_CHECKING:
    from ..models.qualer_api_models_measurements_from_update_measurement_condition_factor_model import (
        MeasurementsFromUpdateMeasurementConditionFactorModel,
    )
    from ..models.qualer_api_models_measurements_from_update_measurement_model import (
        MeasurementsFromUpdateMeasurementModel,
    )
    from ..models.qualer_api_models_measurements_from_update_measurement_tool_model import (
        MeasurementsFromUpdateMeasurementToolModel,
    )


T = TypeVar("T", bound="MeasurementsFromUpdateMeasurementPointModel")


@_attrs_define
class MeasurementsFromUpdateMeasurementPointModel:
    """
    Attributes:
        measurement_point_id (Optional[int]):
        specification_name (Optional[str]):
        unit_of_measure (Optional[str]):
        expected_value (Optional[float]):
        expected_value_raw (Optional[str]):
        base_value (Optional[float]):
        test_value (Optional[float]):
        nominal (Optional[float]):
        range_min (Optional[float]):
        range_max (Optional[float]):
        tolerance_type (Optional[str]):
        precision_type (Optional[str]):
        precision (Optional[float]):
        tolerance_minimum (Optional[float]):
        tolerance_maximum (Optional[float]):
        resolution (Optional[float]):
        resolution_count (Optional[float]):
        is_accredited (Optional[bool]):
        specification_mode (Optional[MeasurementsFromUpdateMeasurementPointModelSpecificationMode]):
        tolerance_mode (Optional[MeasurementsFromUpdateMeasurementPointModelToleranceMode]):
        tolerance_unit (Optional[MeasurementsFromUpdateMeasurementPointModelToleranceUnit]):
        measurements (Optional[List['MeasurementsFromUpdateMeasurementModel']]):
        measurement_condition_factors (Union[None,
            List['MeasurementsFromUpdateMeasurementConditionFactorModel']]):
        tool_application_mode (Union[None,
            MeasurementsFromUpdateMeasurementPointModelToolApplicationMode]):
        primary_measurement_tool (Optional[MeasurementsFromUpdateMeasurementToolModel]):
        secondary_measurement_tool (Optional[MeasurementsFromUpdateMeasurementToolModel]):
        linked_measurement_point_id (Optional[int]):
        hysteresis_point (Optional[MeasurementsFromUpdateMeasurementPointModelHysteresisPoint]):
        influence_parameter_1_parameter_id (Optional[int]):
        influence_parameter_1_value (Optional[str]):
        influence_parameter_2_parameter_id (Optional[int]):
        influence_parameter_2_value (Optional[str]):
        measurement_not_taken_reason (Optional[str]):
        hide_from_certificate (Optional[bool]):
        measurement_not_taken_result (Optional[str]):
        is_measurement_not_taken (Optional[bool]):
        column_mean (Optional[str]):
        column_mean_result (Optional[str]):
        column_sd (Optional[str]):
        column_sd_result (Optional[str]):
        column_cv (Optional[str]):
        column_cv_result (Optional[str]):
        column_range (Optional[str]):
        column_range_result (Optional[str]):
        column_delta (Optional[str]):
        column_delta_result (Optional[str]):
        column_result (Optional[str]):
    """

    measurement_point_id: Optional[int] = None
    specification_name: Optional[str] = None
    unit_of_measure: Optional[str] = None
    expected_value: Optional[float] = None
    expected_value_raw: Optional[str] = None
    base_value: Optional[float] = None
    test_value: Optional[float] = None
    nominal: Optional[float] = None
    range_min: Optional[float] = None
    range_max: Optional[float] = None
    tolerance_type: Optional[str] = None
    precision_type: Optional[str] = None
    precision: Optional[float] = None
    tolerance_minimum: Optional[float] = None
    tolerance_maximum: Optional[float] = None
    resolution: Optional[float] = None
    resolution_count: Optional[float] = None
    is_accredited: Optional[bool] = None
    specification_mode: Union[
        None,
        None,
        MeasurementsFromUpdateMeasurementPointModelSpecificationMode,
    ] = None
    tolerance_mode: Union[
        None,
        None,
        MeasurementsFromUpdateMeasurementPointModelToleranceMode,
    ] = None
    tolerance_unit: Union[
        None,
        None,
        MeasurementsFromUpdateMeasurementPointModelToleranceUnit,
    ] = None
    measurements: Union[None, List["MeasurementsFromUpdateMeasurementModel"]] = None
    measurement_condition_factors: Union[
        None,
        None,
        List["MeasurementsFromUpdateMeasurementConditionFactorModel"],
    ] = None
    tool_application_mode: Union[
        None,
        None,
        MeasurementsFromUpdateMeasurementPointModelToolApplicationMode,
    ] = None
    primary_measurement_tool: Union[None, "MeasurementsFromUpdateMeasurementToolModel"] = None
    secondary_measurement_tool: Union[None, "MeasurementsFromUpdateMeasurementToolModel"] = None
    linked_measurement_point_id: Optional[int] = None
    hysteresis_point: Union[
        None,
        None,
        MeasurementsFromUpdateMeasurementPointModelHysteresisPoint,
    ] = None
    influence_parameter_1_parameter_id: Optional[int] = None
    influence_parameter_1_value: Optional[str] = None
    influence_parameter_2_parameter_id: Optional[int] = None
    influence_parameter_2_value: Optional[str] = None
    measurement_not_taken_reason: Optional[str] = None
    hide_from_certificate: Optional[bool] = None
    measurement_not_taken_result: Optional[str] = None
    is_measurement_not_taken: Optional[bool] = None
    column_mean: Optional[str] = None
    column_mean_result: Optional[str] = None
    column_sd: Optional[str] = None
    column_sd_result: Optional[str] = None
    column_cv: Optional[str] = None
    column_cv_result: Optional[str] = None
    column_range: Optional[str] = None
    column_range_result: Optional[str] = None
    column_delta: Optional[str] = None
    column_delta_result: Optional[str] = None
    column_result: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        measurement_point_id = self.measurement_point_id

        specification_name = self.specification_name

        unit_of_measure = self.unit_of_measure

        expected_value = self.expected_value

        expected_value_raw = self.expected_value_raw

        base_value = self.base_value

        test_value = self.test_value

        nominal = self.nominal

        range_min = self.range_min

        range_max = self.range_max

        tolerance_type = self.tolerance_type

        precision_type = self.precision_type

        precision = self.precision

        tolerance_minimum = self.tolerance_minimum

        tolerance_maximum = self.tolerance_maximum

        resolution = self.resolution

        resolution_count = self.resolution_count

        is_accredited = self.is_accredited

        specification_mode: Optional[int] = None
        if self.specification_mode:
            specification_mode = self.specification_mode.value

        tolerance_mode: Optional[int] = None
        if self.tolerance_mode:
            tolerance_mode = self.tolerance_mode.value

        tolerance_unit: Optional[int] = None
        if self.tolerance_unit:
            tolerance_unit = self.tolerance_unit.value

        measurements: Optional[List[Dict[str, Any]]] = None
        if self.measurements:
            measurements = []
            for measurements_item_data in self.measurements:
                measurements_item = measurements_item_data.to_dict()
                measurements.append(measurements_item)

        measurement_condition_factors: Optional[List[Dict[str, Any]]] = None
        if self.measurement_condition_factors and not isinstance(
            self.measurement_condition_factors, None
        ):
            measurement_condition_factors = []
            for measurement_condition_factors_item_data in self.measurement_condition_factors:
                measurement_condition_factors_item = (
                    measurement_condition_factors_item_data.to_dict()
                )
                measurement_condition_factors.append(measurement_condition_factors_item)

        tool_application_mode: Optional[str] = None
        if self.tool_application_mode and not isinstance(self.tool_application_mode, None):
            tool_application_mode = self.tool_application_mode.value

        primary_measurement_tool: Optional[Dict[str, Any]] = None
        if self.primary_measurement_tool and not isinstance(self.primary_measurement_tool, None):
            primary_measurement_tool = self.primary_measurement_tool.to_dict()

        secondary_measurement_tool: Optional[Dict[str, Any]] = None
        if self.secondary_measurement_tool and not isinstance(
            self.secondary_measurement_tool, None
        ):
            secondary_measurement_tool = self.secondary_measurement_tool.to_dict()

        linked_measurement_point_id = self.linked_measurement_point_id

        hysteresis_point: Optional[str] = None
        if self.hysteresis_point:
            hysteresis_point = self.hysteresis_point.value

        influence_parameter_1_parameter_id = self.influence_parameter_1_parameter_id

        influence_parameter_1_value = self.influence_parameter_1_value

        influence_parameter_2_parameter_id = self.influence_parameter_2_parameter_id

        influence_parameter_2_value = self.influence_parameter_2_value

        measurement_not_taken_reason = self.measurement_not_taken_reason

        hide_from_certificate = self.hide_from_certificate

        measurement_not_taken_result = self.measurement_not_taken_result

        is_measurement_not_taken = self.is_measurement_not_taken

        column_mean = self.column_mean

        column_mean_result = self.column_mean_result

        column_sd = self.column_sd

        column_sd_result = self.column_sd_result

        column_cv = self.column_cv

        column_cv_result = self.column_cv_result

        column_range = self.column_range

        column_range_result = self.column_range_result

        column_delta = self.column_delta

        column_delta_result = self.column_delta_result

        column_result = self.column_result

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
        if expected_value_raw is not None:
            field_dict["ExpectedValueRaw"] = expected_value_raw
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
        if specification_mode is not None:
            field_dict["SpecificationMode"] = specification_mode
        if tolerance_mode is not None:
            field_dict["ToleranceMode"] = tolerance_mode
        if tolerance_unit is not None:
            field_dict["ToleranceUnit"] = tolerance_unit
        if measurements is not None:
            field_dict["Measurements"] = measurements
        if measurement_condition_factors is not None:
            field_dict["MeasurementConditionFactors"] = measurement_condition_factors
        if tool_application_mode is not None:
            field_dict["ToolApplicationMode"] = tool_application_mode
        if primary_measurement_tool is not None:
            field_dict["PrimaryMeasurementTool"] = primary_measurement_tool
        if secondary_measurement_tool is not None:
            field_dict["SecondaryMeasurementTool"] = secondary_measurement_tool
        if linked_measurement_point_id is not None:
            field_dict["LinkedMeasurementPointId"] = linked_measurement_point_id
        if hysteresis_point is not None:
            field_dict["HysteresisPoint"] = hysteresis_point
        if influence_parameter_1_parameter_id is not None:
            field_dict["InfluenceParameter1ParameterId"] = influence_parameter_1_parameter_id
        if influence_parameter_1_value is not None:
            field_dict["InfluenceParameter1Value"] = influence_parameter_1_value
        if influence_parameter_2_parameter_id is not None:
            field_dict["InfluenceParameter2ParameterId"] = influence_parameter_2_parameter_id
        if influence_parameter_2_value is not None:
            field_dict["InfluenceParameter2Value"] = influence_parameter_2_value
        if measurement_not_taken_reason is not None:
            field_dict["MeasurementNotTakenReason"] = measurement_not_taken_reason
        if hide_from_certificate is not None:
            field_dict["HideFromCertificate"] = hide_from_certificate
        if measurement_not_taken_result is not None:
            field_dict["MeasurementNotTakenResult"] = measurement_not_taken_result
        if is_measurement_not_taken is not None:
            field_dict["IsMeasurementNotTaken"] = is_measurement_not_taken
        if column_mean is not None:
            field_dict["ColumnMean"] = column_mean
        if column_mean_result is not None:
            field_dict["ColumnMeanResult"] = column_mean_result
        if column_sd is not None:
            field_dict["ColumnSD"] = column_sd
        if column_sd_result is not None:
            field_dict["ColumnSDResult"] = column_sd_result
        if column_cv is not None:
            field_dict["ColumnCV"] = column_cv
        if column_cv_result is not None:
            field_dict["ColumnCVResult"] = column_cv_result
        if column_range is not None:
            field_dict["ColumnRange"] = column_range
        if column_range_result is not None:
            field_dict["ColumnRangeResult"] = column_range_result
        if column_delta is not None:
            field_dict["ColumnDelta"] = column_delta
        if column_delta_result is not None:
            field_dict["ColumnDeltaResult"] = column_delta_result
        if column_result is not None:
            field_dict["ColumnResult"] = column_result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_measurements_from_update_measurement_condition_factor_model import (
            MeasurementsFromUpdateMeasurementConditionFactorModel,
        )
        from ..models.qualer_api_models_measurements_from_update_measurement_model import (
            MeasurementsFromUpdateMeasurementModel,
        )
        from ..models.qualer_api_models_measurements_from_update_measurement_tool_model import (
            MeasurementsFromUpdateMeasurementToolModel,
        )

        d = dict(src_dict)
        measurement_point_id = d.pop("MeasurementPointId", None)

        specification_name = d.pop("SpecificationName", None)

        unit_of_measure = d.pop("UnitOfMeasure", None)

        expected_value = d.pop("ExpectedValue", None)

        expected_value_raw = d.pop("ExpectedValueRaw", None)

        base_value = d.pop("BaseValue", None)

        test_value = d.pop("TestValue", None)

        nominal = d.pop("Nominal", None)

        range_min = d.pop("RangeMin", None)

        range_max = d.pop("RangeMax", None)

        tolerance_type = d.pop("ToleranceType", None)

        precision_type = d.pop("PrecisionType", None)

        precision = d.pop("Precision", None)

        tolerance_minimum = d.pop("ToleranceMinimum", None)

        tolerance_maximum = d.pop("ToleranceMaximum", None)

        resolution = d.pop("Resolution", None)

        resolution_count = d.pop("ResolutionCount", None)

        is_accredited = d.pop("IsAccredited", None)

        _specification_mode = d.pop("SpecificationMode", None)
        specification_mode: Union[
            None,
            None,
            MeasurementsFromUpdateMeasurementPointModelSpecificationMode,
        ]
        if not _specification_mode:
            specification_mode = None
        else:
            specification_mode = MeasurementsFromUpdateMeasurementPointModelSpecificationMode(
                _specification_mode
            )

        _tolerance_mode = d.pop("ToleranceMode", None)
        tolerance_mode: Union[
            None,
            None,
            MeasurementsFromUpdateMeasurementPointModelToleranceMode,
        ]
        if not _tolerance_mode:
            tolerance_mode = None
        else:
            tolerance_mode = MeasurementsFromUpdateMeasurementPointModelToleranceMode(
                _tolerance_mode
            )

        _tolerance_unit = d.pop("ToleranceUnit", None)
        tolerance_unit: Union[
            None,
            None,
            MeasurementsFromUpdateMeasurementPointModelToleranceUnit,
        ]
        if not _tolerance_unit:
            tolerance_unit = None
        else:
            tolerance_unit = MeasurementsFromUpdateMeasurementPointModelToleranceUnit(
                _tolerance_unit
            )

        measurements = []
        _measurements = d.pop("Measurements", None)
        for measurements_item_data in _measurements or []:
            measurements_item = MeasurementsFromUpdateMeasurementModel.from_dict(
                measurements_item_data
            )

            measurements.append(measurements_item)

        measurement_condition_factors = []
        _measurement_condition_factors = d.pop("MeasurementConditionFactors", None)
        for measurement_condition_factors_item_data in _measurement_condition_factors or []:
            measurement_condition_factors_item = (
                MeasurementsFromUpdateMeasurementConditionFactorModel.from_dict(
                    measurement_condition_factors_item_data
                )
            )

            measurement_condition_factors.append(measurement_condition_factors_item)

        _tool_application_mode = d.pop("ToolApplicationMode", None)
        tool_application_mode: Union[
            None,
            None,
            MeasurementsFromUpdateMeasurementPointModelToolApplicationMode,
        ]
        if not _tool_application_mode:
            tool_application_mode = None
        else:
            tool_application_mode = MeasurementsFromUpdateMeasurementPointModelToolApplicationMode(
                _tool_application_mode
            )

        _primary_measurement_tool = d.pop("PrimaryMeasurementTool", None)
        primary_measurement_tool: Union[None, MeasurementsFromUpdateMeasurementToolModel]
        if not _primary_measurement_tool:
            primary_measurement_tool = None
        else:
            primary_measurement_tool = MeasurementsFromUpdateMeasurementToolModel.from_dict(
                _primary_measurement_tool
            )

        _secondary_measurement_tool = d.pop("SecondaryMeasurementTool", None)
        secondary_measurement_tool: Union[None, MeasurementsFromUpdateMeasurementToolModel]
        if not _secondary_measurement_tool:
            secondary_measurement_tool = None
        else:
            secondary_measurement_tool = MeasurementsFromUpdateMeasurementToolModel.from_dict(
                _secondary_measurement_tool
            )

        linked_measurement_point_id = d.pop("LinkedMeasurementPointId", None)

        _hysteresis_point = d.pop("HysteresisPoint", None)
        hysteresis_point: Union[
            None,
            None,
            MeasurementsFromUpdateMeasurementPointModelHysteresisPoint,
        ]
        if not _hysteresis_point:
            hysteresis_point = None
        else:
            hysteresis_point = MeasurementsFromUpdateMeasurementPointModelHysteresisPoint(
                _hysteresis_point
            )

        influence_parameter_1_parameter_id = d.pop("InfluenceParameter1ParameterId", None)

        influence_parameter_1_value = d.pop("InfluenceParameter1Value", None)

        influence_parameter_2_parameter_id = d.pop("InfluenceParameter2ParameterId", None)

        influence_parameter_2_value = d.pop("InfluenceParameter2Value", None)

        measurement_not_taken_reason = d.pop("MeasurementNotTakenReason", None)

        hide_from_certificate = d.pop("HideFromCertificate", None)

        measurement_not_taken_result = d.pop("MeasurementNotTakenResult", None)

        is_measurement_not_taken = d.pop("IsMeasurementNotTaken", None)

        column_mean = d.pop("ColumnMean", None)

        column_mean_result = d.pop("ColumnMeanResult", None)

        column_sd = d.pop("ColumnSD", None)

        column_sd_result = d.pop("ColumnSDResult", None)

        column_cv = d.pop("ColumnCV", None)

        column_cv_result = d.pop("ColumnCVResult", None)

        column_range = d.pop("ColumnRange", None)

        column_range_result = d.pop("ColumnRangeResult", None)

        column_delta = d.pop("ColumnDelta", None)

        column_delta_result = d.pop("ColumnDeltaResult", None)

        column_result = d.pop("ColumnResult", None)

        qualer_api_models_measurements_from_update_measurement_point_model = cls(
            measurement_point_id=measurement_point_id,
            specification_name=specification_name,
            unit_of_measure=unit_of_measure,
            expected_value=expected_value,
            expected_value_raw=expected_value_raw,
            base_value=base_value,
            test_value=test_value,
            nominal=nominal,
            range_min=range_min,
            range_max=range_max,
            tolerance_type=tolerance_type,
            precision_type=precision_type,
            precision=precision,
            tolerance_minimum=tolerance_minimum,
            tolerance_maximum=tolerance_maximum,
            resolution=resolution,
            resolution_count=resolution_count,
            is_accredited=is_accredited,
            specification_mode=specification_mode,
            tolerance_mode=tolerance_mode,
            tolerance_unit=tolerance_unit,
            measurements=measurements,
            measurement_condition_factors=measurement_condition_factors,
            tool_application_mode=tool_application_mode,
            primary_measurement_tool=primary_measurement_tool,
            secondary_measurement_tool=secondary_measurement_tool,
            linked_measurement_point_id=linked_measurement_point_id,
            hysteresis_point=hysteresis_point,
            influence_parameter_1_parameter_id=influence_parameter_1_parameter_id,
            influence_parameter_1_value=influence_parameter_1_value,
            influence_parameter_2_parameter_id=influence_parameter_2_parameter_id,
            influence_parameter_2_value=influence_parameter_2_value,
            measurement_not_taken_reason=measurement_not_taken_reason,
            hide_from_certificate=hide_from_certificate,
            measurement_not_taken_result=measurement_not_taken_result,
            is_measurement_not_taken=is_measurement_not_taken,
            column_mean=column_mean,
            column_mean_result=column_mean_result,
            column_sd=column_sd,
            column_sd_result=column_sd_result,
            column_cv=column_cv,
            column_cv_result=column_cv_result,
            column_range=column_range,
            column_range_result=column_range_result,
            column_delta=column_delta,
            column_delta_result=column_delta_result,
            column_result=column_result,
        )

        qualer_api_models_measurements_from_update_measurement_point_model.additional_properties = d
        return qualer_api_models_measurements_from_update_measurement_point_model

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
