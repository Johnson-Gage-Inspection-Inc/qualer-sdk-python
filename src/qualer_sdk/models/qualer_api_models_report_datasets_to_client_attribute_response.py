from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsReportDatasetsToClientAttributeResponse")


@_attrs_define
class QualerApiModelsReportDatasetsToClientAttributeResponse:
    """
    Attributes:
        attribute_name (Union[None, Unset, str]):
        attribute_value (Union[None, Unset, str]):
    """

    attribute_name: Union[None, Unset, str] = UNSET
    attribute_value: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribute_name = self.attribute_name

        attribute_value = self.attribute_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attribute_name is not UNSET:
            field_dict["AttributeName"] = attribute_name
        if attribute_value is not UNSET:
            field_dict["AttributeValue"] = attribute_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attribute_name = d.pop("AttributeName", UNSET)

        attribute_value = d.pop("AttributeValue", UNSET)

        qualer_api_models_report_datasets_to_client_attribute_response = cls(
            attribute_name=attribute_name,
            attribute_value=attribute_value,
        )

        qualer_api_models_report_datasets_to_client_attribute_response.additional_properties = (
            d
        )
        return qualer_api_models_report_datasets_to_client_attribute_response

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
