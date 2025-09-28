from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReportDatasetsToServiceOrderAssigneeResponse")


@_attrs_define
class ReportDatasetsToServiceOrderAssigneeResponse:
    """
    Attributes:
        first_name (Optional[str]):
        last_name (Optional[str]):
        alias (Optional[str]):
        email (Optional[str]):
        title (Optional[str]):
    """

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    alias: Optional[str] = None
    email: Optional[str] = None
    title: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        first_name = self.first_name
        last_name = self.last_name
        alias = self.alias
        email = self.email
        title = self.title
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not None:
            field_dict["FirstName"] = first_name
        if last_name is not None:
            field_dict["LastName"] = last_name
        if alias is not None:
            field_dict["Alias"] = alias
        if email is not None:
            field_dict["Email"] = email
        if title is not None:
            field_dict["Title"] = title
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        first_name = d.pop("FirstName", None)
        last_name = d.pop("LastName", None)
        alias = d.pop("Alias", None)
        email = d.pop("Email", None)
        title = d.pop("Title", None)
        qualer_api_models_report_datasets_to_service_order_assignee_response = cls(
            first_name=first_name,
            last_name=last_name,
            alias=alias,
            email=email,
            title=title,
        )
        qualer_api_models_report_datasets_to_service_order_assignee_response.additional_properties = (
            d
        )
        return qualer_api_models_report_datasets_to_service_order_assignee_response

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
