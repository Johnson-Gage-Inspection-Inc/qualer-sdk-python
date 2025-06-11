from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsMeasurementsFromUpdateMeasurementFieldModel")


@_attrs_define
class QualerApiModelsMeasurementsFromUpdateMeasurementFieldModel:
    """
    Attributes:
        field_id (Union[Unset, str]):
        name (Union[Unset, str]):
        type_ (Union[Unset, str]):
        value (Union[Unset, str]):
    """

    field_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        name = self.name

        type_ = self.type_

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_id is not UNSET:
            field_dict["FieldId"] = field_id
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

        name = d.pop("Name", UNSET)

        type_ = d.pop("Type", UNSET)

        value = d.pop("Value", UNSET)

        qualer_api_models_measurements_from_update_measurement_field_model = cls(
            field_id=field_id,
            name=name,
            type_=type_,
            value=value,
        )

        qualer_api_models_measurements_from_update_measurement_field_model.additional_properties = (
            d
        )
        return qualer_api_models_measurements_from_update_measurement_field_model

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
