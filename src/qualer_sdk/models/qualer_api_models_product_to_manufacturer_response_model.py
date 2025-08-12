from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsProductToManufacturerResponseModel")


@_attrs_define
class QualerApiModelsProductToManufacturerResponseModel:
    """
    Attributes:
        manufacturer_id (Union[None, Unset, int]):
        manufacturer_name (Union[None, Unset, str]):
    """

    manufacturer_id: Union[None, Unset, int] = UNSET
    manufacturer_name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        manufacturer_id = self.manufacturer_id

        manufacturer_name = self.manufacturer_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if manufacturer_id is not UNSET:
            field_dict["ManufacturerId"] = manufacturer_id
        if manufacturer_name is not UNSET:
            field_dict["ManufacturerName"] = manufacturer_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        manufacturer_id = d.pop("ManufacturerId", UNSET)

        manufacturer_name = d.pop("ManufacturerName", UNSET)

        qualer_api_models_product_to_manufacturer_response_model = cls(
            manufacturer_id=manufacturer_id,
            manufacturer_name=manufacturer_name,
        )

        qualer_api_models_product_to_manufacturer_response_model.additional_properties = (
            d
        )
        return qualer_api_models_product_to_manufacturer_response_model

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
