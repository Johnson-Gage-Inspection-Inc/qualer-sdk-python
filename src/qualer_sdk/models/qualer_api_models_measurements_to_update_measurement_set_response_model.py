from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.qualer_api_models_measurements_to_update_measurement_set_response_model_influence_parameter_1_type import (
    QualerApiModelsMeasurementsToUpdateMeasurementSetResponseModelInfluenceParameter1Type,
)
from ..models.qualer_api_models_measurements_to_update_measurement_set_response_model_influence_parameter_2_type import (
    QualerApiModelsMeasurementsToUpdateMeasurementSetResponseModelInfluenceParameter2Type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualer_api_models_measurements_to_update_measurement_field_response_model import (
        QualerApiModelsMeasurementsToUpdateMeasurementFieldResponseModel,
    )
    from ..models.qualer_api_models_measurements_to_update_measurement_point_response_model import (
        QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel,
    )


T = TypeVar("T", bound="QualerApiModelsMeasurementsToUpdateMeasurementSetResponseModel")


@_attrs_define
class QualerApiModelsMeasurementsToUpdateMeasurementSetResponseModel:
    """
    Attributes:
        measurement_set_id (Union[None, Unset, int]):
        measurement_name (Union[None, Unset, str]):
        is_accredited (Union[None, Unset, bool]):
        use_expected_value (Union[None, Unset, bool]):
        decimal_places (Union[None, Unset, int]):
        significant_figures (Union[None, Unset, int]):
        influence_parameter_1_type (Union[None, Unset,
            QualerApiModelsMeasurementsToUpdateMeasurementSetResponseModelInfluenceParameter1Type]):
        influence_parameter_1_tool_type_id (Union[None, Unset, int]):
        influence_parameter_1_parameter_id (Union[None, Unset, int]):
        influence_parameter_1_source (Union[None, Unset, str]):
        influence_parameter_1_value (Union[None, Unset, str]):
        influence_parameter_2_type (Union[None, Unset,
            QualerApiModelsMeasurementsToUpdateMeasurementSetResponseModelInfluenceParameter2Type]):
        influence_parameter_2_tool_type_id (Union[None, Unset, int]):
        influence_parameter_2_parameter_id (Union[None, Unset, int]):
        influence_parameter_2_source (Union[None, Unset, str]):
        influence_parameter_2_value (Union[None, Unset, str]):
        measurement_points (Union[None, Unset, list['QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel']]):
        measurement_fields (Union[None, Unset, list['QualerApiModelsMeasurementsToUpdateMeasurementFieldResponseModel']]):
    """

    measurement_set_id: Union[None, Unset, int] = UNSET
    measurement_name: Union[None, Unset, str] = UNSET
    is_accredited: Union[None, Unset, bool] = UNSET
    use_expected_value: Union[None, Unset, bool] = UNSET
    decimal_places: Union[None, Unset, int] = UNSET
    significant_figures: Union[None, Unset, int] = UNSET
    influence_parameter_1_type: Union[None, Unset,
        QualerApiModelsMeasurementsToUpdateMeasurementSetResponseModelInfluenceParameter1Type,
    ] = UNSET
    influence_parameter_1_tool_type_id: Union[None, Unset, int] = UNSET
    influence_parameter_1_parameter_id: Union[None, Unset, int] = UNSET
    influence_parameter_1_source: Union[None, Unset, str] = UNSET
    influence_parameter_1_value: Union[None, Unset, str] = UNSET
    influence_parameter_2_type: Union[None, Unset,
        QualerApiModelsMeasurementsToUpdateMeasurementSetResponseModelInfluenceParameter2Type,
    ] = UNSET
    influence_parameter_2_tool_type_id: Union[None, Unset, int] = UNSET
    influence_parameter_2_parameter_id: Union[None, Unset, int] = UNSET
    influence_parameter_2_source: Union[None, Unset, str] = UNSET
    influence_parameter_2_value: Union[None, Unset, str] = UNSET
    measurement_points: Union[None, Unset, list["QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel"]
    ] = UNSET
    measurement_fields: Union[None, Unset, list["QualerApiModelsMeasurementsToUpdateMeasurementFieldResponseModel"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measurement_set_id = self.measurement_set_id

        measurement_name = self.measurement_name

        is_accredited = self.is_accredited

        use_expected_value = self.use_expected_value

        decimal_places = self.decimal_places

        significant_figures = self.significant_figures

        influence_parameter_1_type: Union[None, Unset, str] = UNSET
        if self.influence_parameter_1_type and not isinstance(
            self.influence_parameter_1_type, Unset
        ):
            influence_parameter_1_type = self.influence_parameter_1_type.value

        influence_parameter_1_tool_type_id = self.influence_parameter_1_tool_type_id

        influence_parameter_1_parameter_id = self.influence_parameter_1_parameter_id

        influence_parameter_1_source = self.influence_parameter_1_source

        influence_parameter_1_value = self.influence_parameter_1_value

        influence_parameter_2_type: Union[None, Unset, str] = UNSET
        if self.influence_parameter_2_type and not isinstance(
            self.influence_parameter_2_type, Unset
        ):
            influence_parameter_2_type = self.influence_parameter_2_type.value

        influence_parameter_2_tool_type_id = self.influence_parameter_2_tool_type_id

        influence_parameter_2_parameter_id = self.influence_parameter_2_parameter_id

        influence_parameter_2_source = self.influence_parameter_2_source

        influence_parameter_2_value = self.influence_parameter_2_value

        measurement_points: Union[None, Unset, list[dict[str, Any]]] = UNSET
        if self.measurement_points and not isinstance(self.measurement_points, Unset):
            measurement_points = []
            for measurement_points_item_data in self.measurement_points:
                measurement_points_item = measurement_points_item_data.to_dict()
                measurement_points.append(measurement_points_item)

        measurement_fields: Union[None, Unset, list[dict[str, Any]]] = UNSET
        if self.measurement_fields and not isinstance(self.measurement_fields, Unset):
            measurement_fields = []
            for measurement_fields_item_data in self.measurement_fields:
                measurement_fields_item = measurement_fields_item_data.to_dict()
                measurement_fields.append(measurement_fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measurement_set_id is not UNSET:
            field_dict["MeasurementSetId"] = measurement_set_id
        if measurement_name is not UNSET:
            field_dict["MeasurementName"] = measurement_name
        if is_accredited is not UNSET:
            field_dict["IsAccredited"] = is_accredited
        if use_expected_value is not UNSET:
            field_dict["UseExpectedValue"] = use_expected_value
        if decimal_places is not UNSET:
            field_dict["DecimalPlaces"] = decimal_places
        if significant_figures is not UNSET:
            field_dict["SignificantFigures"] = significant_figures
        if influence_parameter_1_type is not UNSET:
            field_dict["InfluenceParameter1Type"] = influence_parameter_1_type
        if influence_parameter_1_tool_type_id is not UNSET:
            field_dict["InfluenceParameter1ToolTypeId"] = (
                influence_parameter_1_tool_type_id
            )
        if influence_parameter_1_parameter_id is not UNSET:
            field_dict["InfluenceParameter1ParameterId"] = (
                influence_parameter_1_parameter_id
            )
        if influence_parameter_1_source is not UNSET:
            field_dict["InfluenceParameter1Source"] = influence_parameter_1_source
        if influence_parameter_1_value is not UNSET:
            field_dict["InfluenceParameter1Value"] = influence_parameter_1_value
        if influence_parameter_2_type is not UNSET:
            field_dict["InfluenceParameter2Type"] = influence_parameter_2_type
        if influence_parameter_2_tool_type_id is not UNSET:
            field_dict["InfluenceParameter2ToolTypeId"] = (
                influence_parameter_2_tool_type_id
            )
        if influence_parameter_2_parameter_id is not UNSET:
            field_dict["InfluenceParameter2ParameterId"] = (
                influence_parameter_2_parameter_id
            )
        if influence_parameter_2_source is not UNSET:
            field_dict["InfluenceParameter2Source"] = influence_parameter_2_source
        if influence_parameter_2_value is not UNSET:
            field_dict["InfluenceParameter2Value"] = influence_parameter_2_value
        if measurement_points is not UNSET:
            field_dict["MeasurementPoints"] = measurement_points
        if measurement_fields is not UNSET:
            field_dict["MeasurementFields"] = measurement_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_measurements_to_update_measurement_field_response_model import (
            QualerApiModelsMeasurementsToUpdateMeasurementFieldResponseModel,
        )
        from ..models.qualer_api_models_measurements_to_update_measurement_point_response_model import (
            QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel,
        )

        d = dict(src_dict)
        measurement_set_id = d.pop("MeasurementSetId", UNSET)

        measurement_name = d.pop("MeasurementName", UNSET)

        is_accredited = d.pop("IsAccredited", UNSET)

        use_expected_value = d.pop("UseExpectedValue", UNSET)

        decimal_places = d.pop("DecimalPlaces", UNSET)

        significant_figures = d.pop("SignificantFigures", UNSET)

        _influence_parameter_1_type = d.pop("InfluenceParameter1Type", UNSET)
        influence_parameter_1_type: Union[None, Unset,
            QualerApiModelsMeasurementsToUpdateMeasurementSetResponseModelInfluenceParameter1Type,
        ]
        if isinstance(_influence_parameter_1_type, Unset):
            influence_parameter_1_type = UNSET
        else:
            influence_parameter_1_type = QualerApiModelsMeasurementsToUpdateMeasurementSetResponseModelInfluenceParameter1Type(
                _influence_parameter_1_type
            )

        influence_parameter_1_tool_type_id = d.pop(
            "InfluenceParameter1ToolTypeId", UNSET
        )

        influence_parameter_1_parameter_id = d.pop(
            "InfluenceParameter1ParameterId", UNSET
        )

        influence_parameter_1_source = d.pop("InfluenceParameter1Source", UNSET)

        influence_parameter_1_value = d.pop("InfluenceParameter1Value", UNSET)

        _influence_parameter_2_type = d.pop("InfluenceParameter2Type", UNSET)
        influence_parameter_2_type: Union[None, Unset,
            QualerApiModelsMeasurementsToUpdateMeasurementSetResponseModelInfluenceParameter2Type,
        ]
        if isinstance(_influence_parameter_2_type, Unset):
            influence_parameter_2_type = UNSET
        else:
            influence_parameter_2_type = QualerApiModelsMeasurementsToUpdateMeasurementSetResponseModelInfluenceParameter2Type(
                _influence_parameter_2_type
            )

        influence_parameter_2_tool_type_id = d.pop(
            "InfluenceParameter2ToolTypeId", UNSET
        )

        influence_parameter_2_parameter_id = d.pop(
            "InfluenceParameter2ParameterId", UNSET
        )

        influence_parameter_2_source = d.pop("InfluenceParameter2Source", UNSET)

        influence_parameter_2_value = d.pop("InfluenceParameter2Value", UNSET)

        measurement_points = []
        _measurement_points = d.pop("MeasurementPoints", UNSET)
        for measurement_points_item_data in _measurement_points or []:
            measurement_points_item = QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.from_dict(
                measurement_points_item_data
            )

            measurement_points.append(measurement_points_item)

        measurement_fields = []
        _measurement_fields = d.pop("MeasurementFields", UNSET)
        for measurement_fields_item_data in _measurement_fields or []:
            measurement_fields_item = QualerApiModelsMeasurementsToUpdateMeasurementFieldResponseModel.from_dict(
                measurement_fields_item_data
            )

            measurement_fields.append(measurement_fields_item)

        qualer_api_models_measurements_to_update_measurement_set_response_model = cls(
            measurement_set_id=measurement_set_id,
            measurement_name=measurement_name,
            is_accredited=is_accredited,
            use_expected_value=use_expected_value,
            decimal_places=decimal_places,
            significant_figures=significant_figures,
            influence_parameter_1_type=influence_parameter_1_type,
            influence_parameter_1_tool_type_id=influence_parameter_1_tool_type_id,
            influence_parameter_1_parameter_id=influence_parameter_1_parameter_id,
            influence_parameter_1_source=influence_parameter_1_source,
            influence_parameter_1_value=influence_parameter_1_value,
            influence_parameter_2_type=influence_parameter_2_type,
            influence_parameter_2_tool_type_id=influence_parameter_2_tool_type_id,
            influence_parameter_2_parameter_id=influence_parameter_2_parameter_id,
            influence_parameter_2_source=influence_parameter_2_source,
            influence_parameter_2_value=influence_parameter_2_value,
            measurement_points=measurement_points,
            measurement_fields=measurement_fields,
        )

        qualer_api_models_measurements_to_update_measurement_set_response_model.additional_properties = (
            d
        )
        return qualer_api_models_measurements_to_update_measurement_set_response_model

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
