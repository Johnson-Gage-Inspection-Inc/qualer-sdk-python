from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsClientAttributesFromClientAttributeModel")


@_attrs_define
class QualerApiModelsClientAttributesFromClientAttributeModel:
    """
    Attributes:
        client_site_id (Union[Unset, int]):
        name (Union[Unset, str]):
        value (Union[Unset, str]):
    """

    client_site_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_site_id = self.client_site_id

        name = self.name

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_site_id is not UNSET:
            field_dict["ClientSiteId"] = client_site_id
        if name is not UNSET:
            field_dict["Name"] = name
        if value is not UNSET:
            field_dict["Value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_site_id = d.pop("ClientSiteId", UNSET)

        name = d.pop("Name", UNSET)

        value = d.pop("Value", UNSET)

        qualer_api_models_client_attributes_from_client_attribute_model = cls(
            client_site_id=client_site_id,
            name=name,
            value=value,
        )

        qualer_api_models_client_attributes_from_client_attribute_model.additional_properties = (
            d
        )
        return qualer_api_models_client_attributes_from_client_attribute_model

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
