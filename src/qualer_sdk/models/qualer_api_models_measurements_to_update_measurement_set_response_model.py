from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.qualer_api_models_measurements_to_update_measurement_set_response_model_influence_parameter_1_type import (
    MeasurementsToUpdateMeasurementSetResponseModelInfluenceParameter1Type,
)
from ..models.qualer_api_models_measurements_to_update_measurement_set_response_model_influence_parameter_2_type import (
    MeasurementsToUpdateMeasurementSetResponseModelInfluenceParameter2Type,
)

if TYPE_CHECKING:
    from ..models.qualer_api_models_measurements_to_update_measurement_field_response_model import (
        MeasurementsToUpdateMeasurementFieldResponseModel,
    )
    from ..models.qualer_api_models_measurements_to_update_measurement_point_response_model import (
        MeasurementsToUpdateMeasurementPointResponseModel,
    )


T = TypeVar("T", bound="MeasurementsToUpdateMeasurementSetResponseModel")


@_attrs_define
class MeasurementsToUpdateMeasurementSetResponseModel:
    """
    Attributes:
        measurement_set_id (Optional[int]):
        measurement_name (Optional[str]):
        is_accredited (Optional[bool]):
        use_expected_value (Optional[bool]):
        decimal_places (Optional[int]):
        significant_figures (Optional[int]):
        influence_parameter_1_type (Optional[MeasurementsToUpdateMeasurementSetResponseModelInfluenceParameter1Type]):
        influence_parameter_1_tool_type_id (Optional[int]):
        influence_parameter_1_parameter_id (Optional[int]):
        influence_parameter_1_source (Optional[str]):
        influence_parameter_1_value (Optional[str]):
        influence_parameter_2_type (Optional[MeasurementsToUpdateMeasurementSetResponseModelInfluenceParameter2Type]):
        influence_parameter_2_tool_type_id (Optional[int]):
        influence_parameter_2_parameter_id (Optional[int]):
        influence_parameter_2_source (Optional[str]):
        influence_parameter_2_value (Optional[str]):
        measurement_points (Optional[List['MeasurementsToUpdateMeasurementPointResponseModel']]):
        measurement_fields (Optional[List['MeasurementsToUpdateMeasurementFieldResponseModel']]):
    """

    measurement_set_id: Optional[int] = None
    measurement_name: Optional[str] = None
    is_accredited: Optional[bool] = None
    use_expected_value: Optional[bool] = None
    decimal_places: Optional[int] = None
    significant_figures: Optional[int] = None
    influence_parameter_1_type: Optional[
        MeasurementsToUpdateMeasurementSetResponseModelInfluenceParameter1Type
    ] = None
    influence_parameter_1_tool_type_id: Optional[int] = None
    influence_parameter_1_parameter_id: Optional[int] = None
    influence_parameter_1_source: Optional[str] = None
    influence_parameter_1_value: Optional[str] = None
    influence_parameter_2_type: Optional[
        MeasurementsToUpdateMeasurementSetResponseModelInfluenceParameter2Type
    ] = None
    influence_parameter_2_tool_type_id: Optional[int] = None
    influence_parameter_2_parameter_id: Optional[int] = None
    influence_parameter_2_source: Optional[str] = None
    influence_parameter_2_value: Optional[str] = None
    measurement_points: Optional[List["MeasurementsToUpdateMeasurementPointResponseModel"]] = None
    measurement_fields: Optional[List["MeasurementsToUpdateMeasurementFieldResponseModel"]] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        measurement_set_id = self.measurement_set_id
        measurement_name = self.measurement_name
        is_accredited = self.is_accredited
        use_expected_value = self.use_expected_value
        decimal_places = self.decimal_places
        significant_figures = self.significant_figures
        influence_parameter_1_type = self.influence_parameter_1_type.value if self.influence_parameter_1_type else None
        influence_parameter_1_tool_type_id = self.influence_parameter_1_tool_type_id
        influence_parameter_1_parameter_id = self.influence_parameter_1_parameter_id
        influence_parameter_1_source = self.influence_parameter_1_source
        influence_parameter_1_value = self.influence_parameter_1_value
        influence_parameter_2_type = self.influence_parameter_2_type.value if self.influence_parameter_2_type else None
        influence_parameter_2_tool_type_id = self.influence_parameter_2_tool_type_id
        influence_parameter_2_parameter_id = self.influence_parameter_2_parameter_id
        influence_parameter_2_source = self.influence_parameter_2_source
        influence_parameter_2_value = self.influence_parameter_2_value
        measurement_points: Optional[List[Dict[str, Any]]] = None
        if self.measurement_points:
            measurement_points = []
            for measurement_points_item_data in self.measurement_points:
                measurement_points_item = measurement_points_item_data.to_dict()
                measurement_points.append(measurement_points_item)
        measurement_fields: Optional[List[Dict[str, Any]]] = None
        if self.measurement_fields:
            measurement_fields = []
            for measurement_fields_item_data in self.measurement_fields:
                measurement_fields_item = measurement_fields_item_data.to_dict()
                measurement_fields.append(measurement_fields_item)
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measurement_set_id is not None:
            field_dict["MeasurementSetId"] = measurement_set_id
        if measurement_name is not None:
            field_dict["MeasurementName"] = measurement_name
        if is_accredited is not None:
            field_dict["IsAccredited"] = is_accredited
        if use_expected_value is not None:
            field_dict["UseExpectedValue"] = use_expected_value
        if decimal_places is not None:
            field_dict["DecimalPlaces"] = decimal_places
        if significant_figures is not None:
            field_dict["SignificantFigures"] = significant_figures
        if influence_parameter_1_type is not None:
            field_dict["InfluenceParameter1Type"] = influence_parameter_1_type
        if influence_parameter_1_tool_type_id is not None:
            field_dict["InfluenceParameter1ToolTypeId"] = influence_parameter_1_tool_type_id
        if influence_parameter_1_parameter_id is not None:
            field_dict["InfluenceParameter1ParameterId"] = influence_parameter_1_parameter_id
        if influence_parameter_1_source is not None:
            field_dict["InfluenceParameter1Source"] = influence_parameter_1_source
        if influence_parameter_1_value is not None:
            field_dict["InfluenceParameter1Value"] = influence_parameter_1_value
        if influence_parameter_2_type is not None:
            field_dict["InfluenceParameter2Type"] = influence_parameter_2_type
        if influence_parameter_2_tool_type_id is not None:
            field_dict["InfluenceParameter2ToolTypeId"] = influence_parameter_2_tool_type_id
        if influence_parameter_2_parameter_id is not None:
            field_dict["InfluenceParameter2ParameterId"] = influence_parameter_2_parameter_id
        if influence_parameter_2_source is not None:
            field_dict["InfluenceParameter2Source"] = influence_parameter_2_source
        if influence_parameter_2_value is not None:
            field_dict["InfluenceParameter2Value"] = influence_parameter_2_value
        if measurement_points is not None:
            field_dict["MeasurementPoints"] = measurement_points
        if measurement_fields is not None:
            field_dict["MeasurementFields"] = measurement_fields
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_measurements_to_update_measurement_field_response_model import (
            MeasurementsToUpdateMeasurementFieldResponseModel,
        )
        from ..models.qualer_api_models_measurements_to_update_measurement_point_response_model import (
            MeasurementsToUpdateMeasurementPointResponseModel,
        )
        d = dict(src_dict)
        measurement_set_id = d.pop("MeasurementSetId", None)
        measurement_name = d.pop("MeasurementName", None)
        is_accredited = d.pop("IsAccredited", None)
        use_expected_value = d.pop("UseExpectedValue", None)
        decimal_places = d.pop("DecimalPlaces", None)
        significant_figures = d.pop("SignificantFigures", None)
        _influence_parameter_1_type = d.pop("InfluenceParameter1Type", None)
        influence_parameter_1_type: Optional[
            MeasurementsToUpdateMeasurementSetResponseModelInfluenceParameter1Type
        ]
        if not _influence_parameter_1_type:
            influence_parameter_1_type = None
        elif _influence_parameter_1_type is None:
            influence_parameter_1_type = None
        else:
            influence_parameter_1_type = (
                MeasurementsToUpdateMeasurementSetResponseModelInfluenceParameter1Type(
                    _influence_parameter_1_type
                )
            )
        influence_parameter_1_tool_type_id = d.pop("InfluenceParameter1ToolTypeId", None)
        influence_parameter_1_parameter_id = d.pop("InfluenceParameter1ParameterId", None)
        influence_parameter_1_source = d.pop("InfluenceParameter1Source", None)
        influence_parameter_1_value = d.pop("InfluenceParameter1Value", None)
        _influence_parameter_2_type = d.pop("InfluenceParameter2Type", None)
        influence_parameter_2_type: Optional[
            MeasurementsToUpdateMeasurementSetResponseModelInfluenceParameter2Type
        ]
        if not _influence_parameter_2_type:
            influence_parameter_2_type = None
        elif _influence_parameter_2_type is None:
            influence_parameter_2_type = None
        else:
            influence_parameter_2_type = (
                MeasurementsToUpdateMeasurementSetResponseModelInfluenceParameter2Type(
                    _influence_parameter_2_type
                )
            )
        influence_parameter_2_tool_type_id = d.pop("InfluenceParameter2ToolTypeId", None)
        influence_parameter_2_parameter_id = d.pop("InfluenceParameter2ParameterId", None)
        influence_parameter_2_source = d.pop("InfluenceParameter2Source", None)
        influence_parameter_2_value = d.pop("InfluenceParameter2Value", None)
        measurement_points = []
        _measurement_points = d.pop("MeasurementPoints", None)
        for measurement_points_item_data in _measurement_points or []:
            measurement_points_item = MeasurementsToUpdateMeasurementPointResponseModel.from_dict(
                measurement_points_item_data
            )
            measurement_points.append(measurement_points_item)
        measurement_fields = []
        _measurement_fields = d.pop("MeasurementFields", None)
        for measurement_fields_item_data in _measurement_fields or []:
            measurement_fields_item = MeasurementsToUpdateMeasurementFieldResponseModel.from_dict(
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
