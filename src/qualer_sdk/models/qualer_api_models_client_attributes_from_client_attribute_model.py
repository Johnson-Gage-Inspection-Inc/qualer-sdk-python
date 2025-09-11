from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QualerApiModelsClientAttributesFromClientAttributeModel")


@_attrs_define
class QualerApiModelsClientAttributesFromClientAttributeModel:
    """
    Attributes:
        client_site_id (Optional[int]):
        name (Optional[str]):
        value (Optional[str]):
    """

    client_site_id: Optional[int] = None
    name: Optional[str] = None
    value: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_site_id = self.client_site_id

        name = self.name

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_site_id is not None:
            field_dict["ClientSiteId"] = client_site_id
        if name is not None:
            field_dict["Name"] = name
        if value is not None:
            field_dict["Value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_site_id = d.pop("ClientSiteId", None)

        name = d.pop("Name", None)

        value = d.pop("Value", None)

        qualer_api_models_client_attributes_from_client_attribute_model = cls(
            client_site_id=client_site_id,
            name=name,
            value=value,
        )

        qualer_api_models_client_attributes_from_client_attribute_model.additional_properties = d
        return qualer_api_models_client_attributes_from_client_attribute_model

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
