from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServiceOrderDocumentsFromUploadDocumentsModel")


@_attrs_define
class ServiceOrderDocumentsFromUploadDocumentsModel:
    """
    Attributes:
        report_type (Optional[str]):
        is_private (Optional[bool]):
    """

    report_type: Optional[str] = None
    is_private: Optional[bool] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        report_type = self.report_type
        is_private = self.is_private
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if report_type is not None:
            field_dict["ReportType"] = report_type
        if is_private is not None:
            field_dict["IsPrivate"] = is_private
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        report_type = d.pop("ReportType", None)
        is_private = d.pop("IsPrivate", None)
        qualer_api_models_service_order_documents_from_upload_documents_model = cls(
            report_type=report_type,
            is_private=is_private,
        )
        qualer_api_models_service_order_documents_from_upload_documents_model.additional_properties = (
            d
        )
        return qualer_api_models_service_order_documents_from_upload_documents_model

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
