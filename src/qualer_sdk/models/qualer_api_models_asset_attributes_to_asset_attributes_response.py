from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QualerApiModelsAssetAttributesToAssetAttributesResponse")


@_attrs_define
class QualerApiModelsAssetAttributesToAssetAttributesResponse:
    """
    Attributes:
        name (Optional[str]):
        value (Optional[str]):
    """

    name: Optional[str] = None
    value: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not None:
            field_dict["Name"] = name
        if value is not None:
            field_dict["Value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("Name", None)

        value = d.pop("Value", None)

        qualer_api_models_asset_attributes_to_asset_attributes_response = cls(
            name=name,
            value=value,
        )

        qualer_api_models_asset_attributes_to_asset_attributes_response.additional_properties = d
        return qualer_api_models_asset_attributes_to_asset_attributes_response

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
