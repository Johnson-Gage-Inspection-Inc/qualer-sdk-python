from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsMeasurementsFromCreateMeasurementFieldModel")


@_attrs_define
class QualerApiModelsMeasurementsFromCreateMeasurementFieldModel:
    """
    Attributes:
        field_id (Union[None, Unset, str]):
        valid_values (Union[None, Unset, str]):
        name (Union[None, Unset, str]):
        type_ (Union[None, Unset, str]):
        value (Union[None, Unset, str]):
    """

    field_id: Union[None, Unset, str] = UNSET
    valid_values: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    type_: Union[None, Unset, str] = UNSET
    value: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        valid_values = self.valid_values

        name = self.name

        type_ = self.type_

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_id is not UNSET:
            field_dict["FieldId"] = field_id
        if valid_values is not UNSET:
            field_dict["ValidValues"] = valid_values
        if name is not UNSET:
            field_dict["Name"] = name
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if value is not UNSET:
            field_dict["Value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_id = d.pop("FieldId", UNSET)

        valid_values = d.pop("ValidValues", UNSET)

        name = d.pop("Name", UNSET)

        type_ = d.pop("Type", UNSET)

        value = d.pop("Value", UNSET)

        qualer_api_models_measurements_from_create_measurement_field_model = cls(
            field_id=field_id,
            valid_values=valid_values,
            name=name,
            type_=type_,
            value=value,
        )

        qualer_api_models_measurements_from_create_measurement_field_model.additional_properties = (
            d
        )
        return qualer_api_models_measurements_from_create_measurement_field_model

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
