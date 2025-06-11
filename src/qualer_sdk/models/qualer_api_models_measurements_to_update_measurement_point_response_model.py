from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualer_api_models_measurements_to_update_measurement_condition_factor_response import (
        QualerApiModelsMeasurementsToUpdateMeasurementConditionFactorResponse,
    )
    from ..models.qualer_api_models_measurements_to_update_measurement_response_model import (
        QualerApiModelsMeasurementsToUpdateMeasurementResponseModel,
    )
    from ..models.qualer_api_models_measurements_to_update_measurement_tool_response_model import (
        QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel,
    )


T = TypeVar(
    "T", bound="QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel"
)


@_attrs_define
class QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel:
    """
    Attributes:
        measurement_point_id (Union[Unset, int]):
        specification_name (Union[Unset, str]):
        unit_of_measure (Union[Unset, str]):
        expected_value (Union[Unset, float]):
        base_value (Union[Unset, float]):
        test_value (Union[Unset, float]):
        nominal (Union[Unset, float]):
        range_min (Union[Unset, float]):
        range_max (Union[Unset, float]):
        tolerance_type (Union[Unset, str]):
        tolerance_mode (Union[Unset, str]):
        tolerance_unit (Union[Unset, str]):
        precision_type (Union[Unset, str]):
        precision (Union[Unset, float]):
        tolerance_minimum (Union[Unset, float]):
        tolerance_maximum (Union[Unset, float]):
        resolution (Union[Unset, float]):
        resolution_count (Union[Unset, float]):
        is_accredited (Union[Unset, bool]):
        linked_measurement_point_id (Union[Unset, int]):
        hysteresis_point (Union[Unset, str]):
        hide_from_certificate (Union[Unset, bool]):
        is_measurement_not_taken (Union[Unset, bool]):
        measurement_not_taken_result (Union[Unset, str]):
        measurement_not_taken_reason (Union[Unset, str]):
        influence_parameter_1_parameter_id (Union[Unset, int]):
        influence_parameter_1_value (Union[Unset, str]):
        influence_parameter_2_parameter_id (Union[Unset, int]):
        influence_parameter_2_value (Union[Unset, str]):
        measurements (Union[Unset, list['QualerApiModelsMeasurementsToUpdateMeasurementResponseModel']]):
        measurement_condition_factors (Union[Unset,
            list['QualerApiModelsMeasurementsToUpdateMeasurementConditionFactorResponse']]):
        primary_measurement_tool (Union[Unset, QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel]):
        secondary_measurement_tool (Union[Unset, QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel]):
    """

    measurement_point_id: Union[Unset, int] = UNSET
    specification_name: Union[Unset, str] = UNSET
    unit_of_measure: Union[Unset, str] = UNSET
    expected_value: Union[Unset, float] = UNSET
    base_value: Union[Unset, float] = UNSET
    test_value: Union[Unset, float] = UNSET
    nominal: Union[Unset, float] = UNSET
    range_min: Union[Unset, float] = UNSET
    range_max: Union[Unset, float] = UNSET
    tolerance_type: Union[Unset, str] = UNSET
    tolerance_mode: Union[Unset, str] = UNSET
    tolerance_unit: Union[Unset, str] = UNSET
    precision_type: Union[Unset, str] = UNSET
    precision: Union[Unset, float] = UNSET
    tolerance_minimum: Union[Unset, float] = UNSET
    tolerance_maximum: Union[Unset, float] = UNSET
    resolution: Union[Unset, float] = UNSET
    resolution_count: Union[Unset, float] = UNSET
    is_accredited: Union[Unset, bool] = UNSET
    linked_measurement_point_id: Union[Unset, int] = UNSET
    hysteresis_point: Union[Unset, str] = UNSET
    hide_from_certificate: Union[Unset, bool] = UNSET
    is_measurement_not_taken: Union[Unset, bool] = UNSET
    measurement_not_taken_result: Union[Unset, str] = UNSET
    measurement_not_taken_reason: Union[Unset, str] = UNSET
    influence_parameter_1_parameter_id: Union[Unset, int] = UNSET
    influence_parameter_1_value: Union[Unset, str] = UNSET
    influence_parameter_2_parameter_id: Union[Unset, int] = UNSET
    influence_parameter_2_value: Union[Unset, str] = UNSET
    measurements: Union[
        Unset, list["QualerApiModelsMeasurementsToUpdateMeasurementResponseModel"]
    ] = UNSET
    measurement_condition_factors: Union[
        Unset,
        list["QualerApiModelsMeasurementsToUpdateMeasurementConditionFactorResponse"],
    ] = UNSET
    primary_measurement_tool: Union[
        Unset, "QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel"
    ] = UNSET
    secondary_measurement_tool: Union[
        Unset, "QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel"
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        tolerance_mode = self.tolerance_mode

        tolerance_unit = self.tolerance_unit

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

        primary_measurement_tool: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.primary_measurement_tool, Unset):
            primary_measurement_tool = self.primary_measurement_tool.to_dict()

        secondary_measurement_tool: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.secondary_measurement_tool, Unset):
            secondary_measurement_tool = self.secondary_measurement_tool.to_dict()

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
        if tolerance_mode is not UNSET:
            field_dict["ToleranceMode"] = tolerance_mode
        if tolerance_unit is not UNSET:
            field_dict["ToleranceUnit"] = tolerance_unit
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
        if linked_measurement_point_id is not UNSET:
            field_dict["LinkedMeasurementPointId"] = linked_measurement_point_id
        if hysteresis_point is not UNSET:
            field_dict["HysteresisPoint"] = hysteresis_point
        if hide_from_certificate is not UNSET:
            field_dict["HideFromCertificate"] = hide_from_certificate
        if is_measurement_not_taken is not UNSET:
            field_dict["IsMeasurementNotTaken"] = is_measurement_not_taken
        if measurement_not_taken_result is not UNSET:
            field_dict["MeasurementNotTakenResult"] = measurement_not_taken_result
        if measurement_not_taken_reason is not UNSET:
            field_dict["MeasurementNotTakenReason"] = measurement_not_taken_reason
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
        if measurements is not UNSET:
            field_dict["Measurements"] = measurements
        if measurement_condition_factors is not UNSET:
            field_dict["MeasurementConditionFactors"] = measurement_condition_factors
        if primary_measurement_tool is not UNSET:
            field_dict["PrimaryMeasurementTool"] = primary_measurement_tool
        if secondary_measurement_tool is not UNSET:
            field_dict["SecondaryMeasurementTool"] = secondary_measurement_tool

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_measurements_to_update_measurement_condition_factor_response import (
            QualerApiModelsMeasurementsToUpdateMeasurementConditionFactorResponse,
        )
        from ..models.qualer_api_models_measurements_to_update_measurement_response_model import (
            QualerApiModelsMeasurementsToUpdateMeasurementResponseModel,
        )
        from ..models.qualer_api_models_measurements_to_update_measurement_tool_response_model import (
            QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel,
        )

        d = dict(src_dict)
        measurement_point_id = d.pop("MeasurementPointId", UNSET)

        specification_name = d.pop("SpecificationName", UNSET)

        unit_of_measure = d.pop("UnitOfMeasure", UNSET)

        expected_value = d.pop("ExpectedValue", UNSET)

        base_value = d.pop("BaseValue", UNSET)

        test_value = d.pop("TestValue", UNSET)

        nominal = d.pop("Nominal", UNSET)

        range_min = d.pop("RangeMin", UNSET)

        range_max = d.pop("RangeMax", UNSET)

        tolerance_type = d.pop("ToleranceType", UNSET)

        tolerance_mode = d.pop("ToleranceMode", UNSET)

        tolerance_unit = d.pop("ToleranceUnit", UNSET)

        precision_type = d.pop("PrecisionType", UNSET)

        precision = d.pop("Precision", UNSET)

        tolerance_minimum = d.pop("ToleranceMinimum", UNSET)

        tolerance_maximum = d.pop("ToleranceMaximum", UNSET)

        resolution = d.pop("Resolution", UNSET)

        resolution_count = d.pop("ResolutionCount", UNSET)

        is_accredited = d.pop("IsAccredited", UNSET)

        linked_measurement_point_id = d.pop("LinkedMeasurementPointId", UNSET)

        hysteresis_point = d.pop("HysteresisPoint", UNSET)

        hide_from_certificate = d.pop("HideFromCertificate", UNSET)

        is_measurement_not_taken = d.pop("IsMeasurementNotTaken", UNSET)

        measurement_not_taken_result = d.pop("MeasurementNotTakenResult", UNSET)

        measurement_not_taken_reason = d.pop("MeasurementNotTakenReason", UNSET)

        influence_parameter_1_parameter_id = d.pop(
            "InfluenceParameter1ParameterId", UNSET
        )

        influence_parameter_1_value = d.pop("InfluenceParameter1Value", UNSET)

        influence_parameter_2_parameter_id = d.pop(
            "InfluenceParameter2ParameterId", UNSET
        )

        influence_parameter_2_value = d.pop("InfluenceParameter2Value", UNSET)

        measurements = []
        _measurements = d.pop("Measurements", UNSET)
        for measurements_item_data in _measurements or []:
            measurements_item = (
                QualerApiModelsMeasurementsToUpdateMeasurementResponseModel.from_dict(
                    measurements_item_data
                )
            )

            measurements.append(measurements_item)

        measurement_condition_factors = []
        _measurement_condition_factors = d.pop("MeasurementConditionFactors", UNSET)
        for measurement_condition_factors_item_data in (
            _measurement_condition_factors or []
        ):
            measurement_condition_factors_item = QualerApiModelsMeasurementsToUpdateMeasurementConditionFactorResponse.from_dict(
                measurement_condition_factors_item_data
            )

            measurement_condition_factors.append(measurement_condition_factors_item)

        _primary_measurement_tool = d.pop("PrimaryMeasurementTool", UNSET)
        primary_measurement_tool: Union[
            Unset, QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel
        ]
        if isinstance(_primary_measurement_tool, Unset):
            primary_measurement_tool = UNSET
        else:
            primary_measurement_tool = QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.from_dict(
                _primary_measurement_tool
            )

        _secondary_measurement_tool = d.pop("SecondaryMeasurementTool", UNSET)
        secondary_measurement_tool: Union[
            Unset, QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel
        ]
        if isinstance(_secondary_measurement_tool, Unset):
            secondary_measurement_tool = UNSET
        else:
            secondary_measurement_tool = QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.from_dict(
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
