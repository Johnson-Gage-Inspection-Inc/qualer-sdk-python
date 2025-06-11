from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsClientsFromSendEmployeeEmailModel")


@_attrs_define
class QualerApiModelsClientsFromSendEmployeeEmailModel:
    """
    Attributes:
        subject (Union[Unset, str]):
        body (Union[Unset, str]):
    """

    subject: Union[Unset, str] = UNSET
    body: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subject = self.subject

        body = self.body

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subject is not UNSET:
            field_dict["Subject"] = subject
        if body is not UNSET:
            field_dict["Body"] = body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subject = d.pop("Subject", UNSET)

        body = d.pop("Body", UNSET)

        qualer_api_models_clients_from_send_employee_email_model = cls(
            subject=subject,
            body=body,
        )

        qualer_api_models_clients_from_send_employee_email_model.additional_properties = (
            d
        )
        return qualer_api_models_clients_from_send_employee_email_model

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
