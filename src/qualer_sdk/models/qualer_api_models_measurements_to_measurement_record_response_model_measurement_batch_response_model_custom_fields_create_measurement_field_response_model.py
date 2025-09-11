from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T",
    bound="QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFieldsCreateMeasurementFieldResponseModel",
)


@_attrs_define
class QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFieldsCreateMeasurementFieldResponseModel:
    """
    Attributes:
        name (Optional[str]):
        type_ (Optional[str]):
        value (Optional[str]):
        field_id (Optional[str]):
        valid_values (Optional[str]):
    """

    name: Optional[str] = None
    type_: Optional[str] = None
    value: Optional[str] = None
    field_id: Optional[str] = None
    valid_values: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        type_ = self.type_

        value = self.value

        field_id = self.field_id

        valid_values = self.valid_values

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not None:
            field_dict["Name"] = name
        if type_ is not None:
            field_dict["Type"] = type_
        if value is not None:
            field_dict["Value"] = value
        if field_id is not None:
            field_dict["FieldId"] = field_id
        if valid_values is not None:
            field_dict["ValidValues"] = valid_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("Name", None)

        type_ = d.pop("Type", None)

        value = d.pop("Value", None)

        field_id = d.pop("FieldId", None)

        valid_values = d.pop("ValidValues", None)

        qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_custom_fields_create_measurement_field_response_model = cls(
            name=name,
            type_=type_,
            value=value,
            field_id=field_id,
            valid_values=valid_values,
        )

        qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_custom_fields_create_measurement_field_response_model.additional_properties = (
            d
        )
        return qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_custom_fields_create_measurement_field_response_model

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
