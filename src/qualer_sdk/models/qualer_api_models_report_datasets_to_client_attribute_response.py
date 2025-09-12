from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QualerApiModelsReportDatasetsToClientAttributeResponse")


@_attrs_define
class QualerApiModelsReportDatasetsToClientAttributeResponse:
    """
    Attributes:
        attribute_name (Optional[str]):
        attribute_value (Optional[str]):
    """

    attribute_name: Optional[str] = None
    attribute_value: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute_name = self.attribute_name

        attribute_value = self.attribute_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attribute_name is not None:
            field_dict["AttributeName"] = attribute_name
        if attribute_value is not None:
            field_dict["AttributeValue"] = attribute_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attribute_name = d.pop("AttributeName", None)

        attribute_value = d.pop("AttributeValue", None)

        qualer_api_models_report_datasets_to_client_attribute_response = cls(
            attribute_name=attribute_name,
            attribute_value=attribute_value,
        )

        qualer_api_models_report_datasets_to_client_attribute_response.additional_properties = d
        return qualer_api_models_report_datasets_to_client_attribute_response

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
