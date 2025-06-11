from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.qualer_api_models_measurements_from_update_measurement_point_model_hysteresis_point import (
    QualerApiModelsMeasurementsFromUpdateMeasurementPointModelHysteresisPoint,
)
from ..models.qualer_api_models_measurements_from_update_measurement_point_model_specification_mode import (
    QualerApiModelsMeasurementsFromUpdateMeasurementPointModelSpecificationMode,
)
from ..models.qualer_api_models_measurements_from_update_measurement_point_model_tolerance_mode import (
    QualerApiModelsMeasurementsFromUpdateMeasurementPointModelToleranceMode,
)
from ..models.qualer_api_models_measurements_from_update_measurement_point_model_tolerance_unit import (
    QualerApiModelsMeasurementsFromUpdateMeasurementPointModelToleranceUnit,
)
from ..models.qualer_api_models_measurements_from_update_measurement_point_model_tool_application_mode import (
    QualerApiModelsMeasurementsFromUpdateMeasurementPointModelToolApplicationMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualer_api_models_measurements_from_update_measurement_condition_factor_model import (
        QualerApiModelsMeasurementsFromUpdateMeasurementConditionFactorModel,
    )
    from ..models.qualer_api_models_measurements_from_update_measurement_model import (
        QualerApiModelsMeasurementsFromUpdateMeasurementModel,
    )
    from ..models.qualer_api_models_measurements_from_update_measurement_tool_model import (
        QualerApiModelsMeasurementsFromUpdateMeasurementToolModel,
    )


T = TypeVar("T", bound="QualerApiModelsMeasurementsFromUpdateMeasurementPointModel")


@_attrs_define
class QualerApiModelsMeasurementsFromUpdateMeasurementPointModel:
    """
    Attributes:
        measurement_point_id (Union[Unset, int]):
        specification_name (Union[Unset, str]):
        unit_of_measure (Union[Unset, str]):
        expected_value (Union[Unset, float]):
        expected_value_raw (Union[Unset, str]):
        base_value (Union[Unset, float]):
        test_value (Union[Unset, float]):
        nominal (Union[Unset, float]):
        range_min (Union[Unset, float]):
        range_max (Union[Unset, float]):
        tolerance_type (Union[Unset, str]):
        precision_type (Union[Unset, str]):
        precision (Union[Unset, float]):
        tolerance_minimum (Union[Unset, float]):
        tolerance_maximum (Union[Unset, float]):
        resolution (Union[Unset, float]):
        resolution_count (Union[Unset, float]):
        is_accredited (Union[Unset, bool]):
        specification_mode (Union[Unset, QualerApiModelsMeasurementsFromUpdateMeasurementPointModelSpecificationMode]):
        tolerance_mode (Union[Unset, QualerApiModelsMeasurementsFromUpdateMeasurementPointModelToleranceMode]):
        tolerance_unit (Union[Unset, QualerApiModelsMeasurementsFromUpdateMeasurementPointModelToleranceUnit]):
        measurements (Union[Unset, list['QualerApiModelsMeasurementsFromUpdateMeasurementModel']]):
        measurement_condition_factors (Union[Unset,
            list['QualerApiModelsMeasurementsFromUpdateMeasurementConditionFactorModel']]):
        tool_application_mode (Union[Unset,
            QualerApiModelsMeasurementsFromUpdateMeasurementPointModelToolApplicationMode]):
        primary_measurement_tool (Union[Unset, QualerApiModelsMeasurementsFromUpdateMeasurementToolModel]):
        secondary_measurement_tool (Union[Unset, QualerApiModelsMeasurementsFromUpdateMeasurementToolModel]):
        linked_measurement_point_id (Union[Unset, int]):
        hysteresis_point (Union[Unset, QualerApiModelsMeasurementsFromUpdateMeasurementPointModelHysteresisPoint]):
        influence_parameter_1_parameter_id (Union[Unset, int]):
        influence_parameter_1_value (Union[Unset, str]):
        influence_parameter_2_parameter_id (Union[Unset, int]):
        influence_parameter_2_value (Union[Unset, str]):
        measurement_not_taken_reason (Union[Unset, str]):
        hide_from_certificate (Union[Unset, bool]):
        measurement_not_taken_result (Union[Unset, str]):
        is_measurement_not_taken (Union[Unset, bool]):
        column_mean (Union[Unset, str]):
        column_mean_result (Union[Unset, str]):
        column_sd (Union[Unset, str]):
        column_sd_result (Union[Unset, str]):
        column_cv (Union[Unset, str]):
        column_cv_result (Union[Unset, str]):
        column_range (Union[Unset, str]):
        column_range_result (Union[Unset, str]):
        column_delta (Union[Unset, str]):
        column_delta_result (Union[Unset, str]):
        column_result (Union[Unset, str]):
    """

    measurement_point_id: Union[Unset, int] = UNSET
    specification_name: Union[Unset, str] = UNSET
    unit_of_measure: Union[Unset, str] = UNSET
    expected_value: Union[Unset, float] = UNSET
    expected_value_raw: Union[Unset, str] = UNSET
    base_value: Union[Unset, float] = UNSET
    test_value: Union[Unset, float] = UNSET
    nominal: Union[Unset, float] = UNSET
    range_min: Union[Unset, float] = UNSET
    range_max: Union[Unset, float] = UNSET
    tolerance_type: Union[Unset, str] = UNSET
    precision_type: Union[Unset, str] = UNSET
    precision: Union[Unset, float] = UNSET
    tolerance_minimum: Union[Unset, float] = UNSET
    tolerance_maximum: Union[Unset, float] = UNSET
    resolution: Union[Unset, float] = UNSET
    resolution_count: Union[Unset, float] = UNSET
    is_accredited: Union[Unset, bool] = UNSET
    specification_mode: Union[
        Unset,
        QualerApiModelsMeasurementsFromUpdateMeasurementPointModelSpecificationMode,
    ] = UNSET
    tolerance_mode: Union[
        Unset, QualerApiModelsMeasurementsFromUpdateMeasurementPointModelToleranceMode
    ] = UNSET
    tolerance_unit: Union[
        Unset, QualerApiModelsMeasurementsFromUpdateMeasurementPointModelToleranceUnit
    ] = UNSET
    measurements: Union[
        Unset, list["QualerApiModelsMeasurementsFromUpdateMeasurementModel"]
    ] = UNSET
    measurement_condition_factors: Union[
        Unset,
        list["QualerApiModelsMeasurementsFromUpdateMeasurementConditionFactorModel"],
    ] = UNSET
    tool_application_mode: Union[
        Unset,
        QualerApiModelsMeasurementsFromUpdateMeasurementPointModelToolApplicationMode,
    ] = UNSET
    primary_measurement_tool: Union[
        Unset, "QualerApiModelsMeasurementsFromUpdateMeasurementToolModel"
    ] = UNSET
    secondary_measurement_tool: Union[
        Unset, "QualerApiModelsMeasurementsFromUpdateMeasurementToolModel"
    ] = UNSET
    linked_measurement_point_id: Union[Unset, int] = UNSET
    hysteresis_point: Union[
        Unset, QualerApiModelsMeasurementsFromUpdateMeasurementPointModelHysteresisPoint
    ] = UNSET
    influence_parameter_1_parameter_id: Union[Unset, int] = UNSET
    influence_parameter_1_value: Union[Unset, str] = UNSET
    influence_parameter_2_parameter_id: Union[Unset, int] = UNSET
    influence_parameter_2_value: Union[Unset, str] = UNSET
    measurement_not_taken_reason: Union[Unset, str] = UNSET
    hide_from_certificate: Union[Unset, bool] = UNSET
    measurement_not_taken_result: Union[Unset, str] = UNSET
    is_measurement_not_taken: Union[Unset, bool] = UNSET
    column_mean: Union[Unset, str] = UNSET
    column_mean_result: Union[Unset, str] = UNSET
    column_sd: Union[Unset, str] = UNSET
    column_sd_result: Union[Unset, str] = UNSET
    column_cv: Union[Unset, str] = UNSET
    column_cv_result: Union[Unset, str] = UNSET
    column_range: Union[Unset, str] = UNSET
    column_range_result: Union[Unset, str] = UNSET
    column_delta: Union[Unset, str] = UNSET
    column_delta_result: Union[Unset, str] = UNSET
    column_result: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        specification_mode: Union[Unset, str] = UNSET
        if not isinstance(self.specification_mode, Unset):
            specification_mode = self.specification_mode.value

        tolerance_mode: Union[Unset, str] = UNSET
        if not isinstance(self.tolerance_mode, Unset):
            tolerance_mode = self.tolerance_mode.value

        tolerance_unit: Union[Unset, str] = UNSET
        if not isinstance(self.tolerance_unit, Unset):
            tolerance_unit = self.tolerance_unit.value

        measurements: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.measurements, Unset):
            measurements = []
            for measurements_item_data in self.measurements:
                measurements_item = measurements_item_data.to_dict()
                measurements.append(measurements_item)

        measurement_condition_factors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.measurement_condition_factors, Unset):
            measurement_condition_factors = []
            for (
                measurement_condition_factors_item_data
            ) in self.measurement_condition_factors:
                measurement_condition_factors_item = (
                    measurement_condition_factors_item_data.to_dict()
                )
                measurement_condition_factors.append(measurement_condition_factors_item)

        tool_application_mode: Union[Unset, str] = UNSET
        if not isinstance(self.tool_application_mode, Unset):
            tool_application_mode = self.tool_application_mode.value

        primary_measurement_tool: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.primary_measurement_tool, Unset):
            primary_measurement_tool = self.primary_measurement_tool.to_dict()

        secondary_measurement_tool: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.secondary_measurement_tool, Unset):
            secondary_measurement_tool = self.secondary_measurement_tool.to_dict()

        linked_measurement_point_id = self.linked_measurement_point_id

        hysteresis_point: Union[Unset, str] = UNSET
        if not isinstance(self.hysteresis_point, Unset):
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measurement_point_id is not UNSET:
            field_dict["MeasurementPointId"] = measurement_point_id
        if specification_name is not UNSET:
            field_dict["SpecificationName"] = specification_name
        if unit_of_measure is not UNSET:
            field_dict["UnitOfMeasure"] = unit_of_measure
        if expected_value is not UNSET:
            field_dict["ExpectedValue"] = expected_value
        if expected_value_raw is not UNSET:
            field_dict["ExpectedValueRaw"] = expected_value_raw
        if base_value is not UNSET:
            field_dict["BaseValue"] = base_value
        if test_value is not UNSET:
            field_dict["TestValue"] = test_value
        if nominal is not UNSET:
            field_dict["Nominal"] = nominal
        if range_min is not UNSET:
            field_dict["RangeMin"] = range_min
        if range_max is not UNSET:
            field_dict["RangeMax"] = range_max
        if tolerance_type is not UNSET:
            field_dict["ToleranceType"] = tolerance_type
        if precision_type is not UNSET:
            field_dict["PrecisionType"] = precision_type
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
        if is_accredited is not UNSET:
            field_dict["IsAccredited"] = is_accredited
        if specification_mode is not UNSET:
            field_dict["SpecificationMode"] = specification_mode
        if tolerance_mode is not UNSET:
            field_dict["ToleranceMode"] = tolerance_mode
        if tolerance_unit is not UNSET:
            field_dict["ToleranceUnit"] = tolerance_unit
        if measurements is not UNSET:
            field_dict["Measurements"] = measurements
        if measurement_condition_factors is not UNSET:
            field_dict["MeasurementConditionFactors"] = measurement_condition_factors
        if tool_application_mode is not UNSET:
            field_dict["ToolApplicationMode"] = tool_application_mode
        if primary_measurement_tool is not UNSET:
            field_dict["PrimaryMeasurementTool"] = primary_measurement_tool
        if secondary_measurement_tool is not UNSET:
            field_dict["SecondaryMeasurementTool"] = secondary_measurement_tool
        if linked_measurement_point_id is not UNSET:
            field_dict["LinkedMeasurementPointId"] = linked_measurement_point_id
        if hysteresis_point is not UNSET:
            field_dict["HysteresisPoint"] = hysteresis_point
        if influence_parameter_1_parameter_id is not UNSET:
            field_dict["InfluenceParameter1ParameterId"] = (
                influence_parameter_1_parameter_id
            )
        if influence_parameter_1_value is not UNSET:
            field_dict["InfluenceParameter1Value"] = influence_parameter_1_value
        if influence_parameter_2_parameter_id is not UNSET:
            field_dict["InfluenceParameter2ParameterId"] = (
                influence_parameter_2_parameter_id
            )
        if influence_parameter_2_value is not UNSET:
            field_dict["InfluenceParameter2Value"] = influence_parameter_2_value
        if measurement_not_taken_reason is not UNSET:
            field_dict["MeasurementNotTakenReason"] = measurement_not_taken_reason
        if hide_from_certificate is not UNSET:
            field_dict["HideFromCertificate"] = hide_from_certificate
        if measurement_not_taken_result is not UNSET:
            field_dict["MeasurementNotTakenResult"] = measurement_not_taken_result
        if is_measurement_not_taken is not UNSET:
            field_dict["IsMeasurementNotTaken"] = is_measurement_not_taken
        if column_mean is not UNSET:
            field_dict["ColumnMean"] = column_mean
        if column_mean_result is not UNSET:
            field_dict["ColumnMeanResult"] = column_mean_result
        if column_sd is not UNSET:
            field_dict["ColumnSD"] = column_sd
        if column_sd_result is not UNSET:
            field_dict["ColumnSDResult"] = column_sd_result
        if column_cv is not UNSET:
            field_dict["ColumnCV"] = column_cv
        if column_cv_result is not UNSET:
            field_dict["ColumnCVResult"] = column_cv_result
        if column_range is not UNSET:
            field_dict["ColumnRange"] = column_range
        if column_range_result is not UNSET:
            field_dict["ColumnRangeResult"] = column_range_result
        if column_delta is not UNSET:
            field_dict["ColumnDelta"] = column_delta
        if column_delta_result is not UNSET:
            field_dict["ColumnDeltaResult"] = column_delta_result
        if column_result is not UNSET:
            field_dict["ColumnResult"] = column_result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_measurements_from_update_measurement_condition_factor_model import (
            QualerApiModelsMeasurementsFromUpdateMeasurementConditionFactorModel,
        )
        from ..models.qualer_api_models_measurements_from_update_measurement_model import (
            QualerApiModelsMeasurementsFromUpdateMeasurementModel,
        )
        from ..models.qualer_api_models_measurements_from_update_measurement_tool_model import (
            QualerApiModelsMeasurementsFromUpdateMeasurementToolModel,
        )

        d = dict(src_dict)
        measurement_point_id = d.pop("MeasurementPointId", UNSET)

        specification_name = d.pop("SpecificationName", UNSET)

        unit_of_measure = d.pop("UnitOfMeasure", UNSET)

        expected_value = d.pop("ExpectedValue", UNSET)

        expected_value_raw = d.pop("ExpectedValueRaw", UNSET)

        base_value = d.pop("BaseValue", UNSET)

        test_value = d.pop("TestValue", UNSET)

        nominal = d.pop("Nominal", UNSET)

        range_min = d.pop("RangeMin", UNSET)

        range_max = d.pop("RangeMax", UNSET)

        tolerance_type = d.pop("ToleranceType", UNSET)

        precision_type = d.pop("PrecisionType", UNSET)

        precision = d.pop("Precision", UNSET)

        tolerance_minimum = d.pop("ToleranceMinimum", UNSET)

        tolerance_maximum = d.pop("ToleranceMaximum", UNSET)

        resolution = d.pop("Resolution", UNSET)

        resolution_count = d.pop("ResolutionCount", UNSET)

        is_accredited = d.pop("IsAccredited", UNSET)

        _specification_mode = d.pop("SpecificationMode", UNSET)
        specification_mode: Union[
            Unset,
            QualerApiModelsMeasurementsFromUpdateMeasurementPointModelSpecificationMode,
        ]
        if isinstance(_specification_mode, Unset):
            specification_mode = UNSET
        else:
            specification_mode = QualerApiModelsMeasurementsFromUpdateMeasurementPointModelSpecificationMode(
                _specification_mode
            )

        _tolerance_mode = d.pop("ToleranceMode", UNSET)
        tolerance_mode: Union[
            Unset,
            QualerApiModelsMeasurementsFromUpdateMeasurementPointModelToleranceMode,
        ]
        if isinstance(_tolerance_mode, Unset):
            tolerance_mode = UNSET
        else:
            tolerance_mode = (
                QualerApiModelsMeasurementsFromUpdateMeasurementPointModelToleranceMode(
                    _tolerance_mode
                )
            )

        _tolerance_unit = d.pop("ToleranceUnit", UNSET)
        tolerance_unit: Union[
            Unset,
            QualerApiModelsMeasurementsFromUpdateMeasurementPointModelToleranceUnit,
        ]
        if isinstance(_tolerance_unit, Unset):
            tolerance_unit = UNSET
        else:
            tolerance_unit = (
                QualerApiModelsMeasurementsFromUpdateMeasurementPointModelToleranceUnit(
                    _tolerance_unit
                )
            )

        measurements = []
        _measurements = d.pop("Measurements", UNSET)
        for measurements_item_data in _measurements or []:
            measurements_item = (
                QualerApiModelsMeasurementsFromUpdateMeasurementModel.from_dict(
                    measurements_item_data
                )
            )

            measurements.append(measurements_item)

        measurement_condition_factors = []
        _measurement_condition_factors = d.pop("MeasurementConditionFactors", UNSET)
        for measurement_condition_factors_item_data in (
            _measurement_condition_factors or []
        ):
            measurement_condition_factors_item = QualerApiModelsMeasurementsFromUpdateMeasurementConditionFactorModel.from_dict(
                measurement_condition_factors_item_data
            )

            measurement_condition_factors.append(measurement_condition_factors_item)

        _tool_application_mode = d.pop("ToolApplicationMode", UNSET)
        tool_application_mode: Union[
            Unset,
            QualerApiModelsMeasurementsFromUpdateMeasurementPointModelToolApplicationMode,
        ]
        if isinstance(_tool_application_mode, Unset):
            tool_application_mode = UNSET
        else:
            tool_application_mode = QualerApiModelsMeasurementsFromUpdateMeasurementPointModelToolApplicationMode(
                _tool_application_mode
            )

        _primary_measurement_tool = d.pop("PrimaryMeasurementTool", UNSET)
        primary_measurement_tool: Union[
            Unset, QualerApiModelsMeasurementsFromUpdateMeasurementToolModel
        ]
        if isinstance(_primary_measurement_tool, Unset):
            primary_measurement_tool = UNSET
        else:
            primary_measurement_tool = (
                QualerApiModelsMeasurementsFromUpdateMeasurementToolModel.from_dict(
                    _primary_measurement_tool
                )
            )

        _secondary_measurement_tool = d.pop("SecondaryMeasurementTool", UNSET)
        secondary_measurement_tool: Union[
            Unset, QualerApiModelsMeasurementsFromUpdateMeasurementToolModel
        ]
        if isinstance(_secondary_measurement_tool, Unset):
            secondary_measurement_tool = UNSET
        else:
            secondary_measurement_tool = (
                QualerApiModelsMeasurementsFromUpdateMeasurementToolModel.from_dict(
                    _secondary_measurement_tool
                )
            )

        linked_measurement_point_id = d.pop("LinkedMeasurementPointId", UNSET)

        _hysteresis_point = d.pop("HysteresisPoint", UNSET)
        hysteresis_point: Union[
            Unset,
            QualerApiModelsMeasurementsFromUpdateMeasurementPointModelHysteresisPoint,
        ]
        if isinstance(_hysteresis_point, Unset):
            hysteresis_point = UNSET
        else:
            hysteresis_point = QualerApiModelsMeasurementsFromUpdateMeasurementPointModelHysteresisPoint(
                _hysteresis_point
            )

        influence_parameter_1_parameter_id = d.pop(
            "InfluenceParameter1ParameterId", UNSET
        )

        influence_parameter_1_value = d.pop("InfluenceParameter1Value", UNSET)

        influence_parameter_2_parameter_id = d.pop(
            "InfluenceParameter2ParameterId", UNSET
        )

        influence_parameter_2_value = d.pop("InfluenceParameter2Value", UNSET)

        measurement_not_taken_reason = d.pop("MeasurementNotTakenReason", UNSET)

        hide_from_certificate = d.pop("HideFromCertificate", UNSET)

        measurement_not_taken_result = d.pop("MeasurementNotTakenResult", UNSET)

        is_measurement_not_taken = d.pop("IsMeasurementNotTaken", UNSET)

        column_mean = d.pop("ColumnMean", UNSET)

        column_mean_result = d.pop("ColumnMeanResult", UNSET)

        column_sd = d.pop("ColumnSD", UNSET)

        column_sd_result = d.pop("ColumnSDResult", UNSET)

        column_cv = d.pop("ColumnCV", UNSET)

        column_cv_result = d.pop("ColumnCVResult", UNSET)

        column_range = d.pop("ColumnRange", UNSET)

        column_range_result = d.pop("ColumnRangeResult", UNSET)

        column_delta = d.pop("ColumnDelta", UNSET)

        column_delta_result = d.pop("ColumnDeltaResult", UNSET)

        column_result = d.pop("ColumnResult", UNSET)

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

        qualer_api_models_measurements_from_update_measurement_point_model.additional_properties = (
            d
        )
        return qualer_api_models_measurements_from_update_measurement_point_model

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
