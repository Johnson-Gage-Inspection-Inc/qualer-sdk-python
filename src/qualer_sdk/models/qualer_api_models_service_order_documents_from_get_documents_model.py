from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServiceOrderDocumentsFromGetDocumentsModel")


@_attrs_define
class ServiceOrderDocumentsFromGetDocumentsModel:
    """
    Attributes:
        file_name (Optional[str]):
    """

    file_name: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file_name = self.file_name
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_name is not None:
            field_dict["FileName"] = file_name
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_name = d.pop("FileName", None)
        qualer_api_models_service_order_documents_from_get_documents_model = cls(
            file_name=file_name,
        )
        qualer_api_models_service_order_documents_from_get_documents_model.additional_properties = d
        return qualer_api_models_service_order_documents_from_get_documents_model

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
