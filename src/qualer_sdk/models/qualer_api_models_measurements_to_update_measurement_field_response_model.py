from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QualerApiModelsMeasurementsToUpdateMeasurementFieldResponseModel")


@_attrs_define
class QualerApiModelsMeasurementsToUpdateMeasurementFieldResponseModel:
    """
    Attributes:
        field_id (Optional[str]):
        name (Optional[str]):
        type_ (Optional[str]):
        value (Optional[str]):
    """

    field_id: Optional[str] = None
    name: Optional[str] = None
    type_: Optional[str] = None
    value: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_id = self.field_id

        name = self.name

        type_ = self.type_

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_id is not None:
            field_dict["FieldId"] = field_id
        if name is not None:
            field_dict["Name"] = name
        if type_ is not None:
            field_dict["Type"] = type_
        if value is not None:
            field_dict["Value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_id = d.pop("FieldId", None)

        name = d.pop("Name", None)

        type_ = d.pop("Type", None)

        value = d.pop("Value", None)

        qualer_api_models_measurements_to_update_measurement_field_response_model = cls(
            field_id=field_id,
            name=name,
            type_=type_,
            value=value,
        )

        qualer_api_models_measurements_to_update_measurement_field_response_model.additional_properties = (
            d
        )
        return qualer_api_models_measurements_to_update_measurement_field_response_model

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
