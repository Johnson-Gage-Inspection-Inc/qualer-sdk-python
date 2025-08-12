from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsReportDatasetsToServiceOrderAssigneeResponse")


@_attrs_define
class QualerApiModelsReportDatasetsToServiceOrderAssigneeResponse:
    """
    Attributes:
        first_name (Union[None, Unset, str]):
        last_name (Union[None, Unset, str]):
        alias (Union[None, Unset, str]):
        email (Union[None, Unset, str]):
        title (Union[None, Unset, str]):
    """

    first_name: Union[None, Unset, str] = UNSET
    last_name: Union[None, Unset, str] = UNSET
    alias: Union[None, Unset, str] = UNSET
    email: Union[None, Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        alias = self.alias

        email = self.email

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["FirstName"] = first_name
        if last_name is not UNSET:
            field_dict["LastName"] = last_name
        if alias is not UNSET:
            field_dict["Alias"] = alias
        if email is not UNSET:
            field_dict["Email"] = email
        if title is not UNSET:
            field_dict["Title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        first_name = d.pop("FirstName", UNSET)

        last_name = d.pop("LastName", UNSET)

        alias = d.pop("Alias", UNSET)

        email = d.pop("Email", UNSET)

        title = d.pop("Title", UNSET)

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
