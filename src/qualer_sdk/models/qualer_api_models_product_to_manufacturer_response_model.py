from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProductToManufacturerResponseModel")


@_attrs_define
class ProductToManufacturerResponseModel:
    """
    Attributes:
        manufacturer_id (Optional[int]):
        manufacturer_name (Optional[str]):
    """

    manufacturer_id: Optional[int] = None
    manufacturer_name: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        manufacturer_id = self.manufacturer_id
        manufacturer_name = self.manufacturer_name
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if manufacturer_id is not None:
            field_dict["ManufacturerId"] = manufacturer_id
        if manufacturer_name is not None:
            field_dict["ManufacturerName"] = manufacturer_name
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        manufacturer_id = d.pop("ManufacturerId", None)
        manufacturer_name = d.pop("ManufacturerName", None)
        qualer_api_models_product_to_manufacturer_response_model = cls(
            manufacturer_id=manufacturer_id,
            manufacturer_name=manufacturer_name,
        )
        qualer_api_models_product_to_manufacturer_response_model.additional_properties = d
        return qualer_api_models_product_to_manufacturer_response_model

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
