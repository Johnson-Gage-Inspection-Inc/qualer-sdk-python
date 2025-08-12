import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsAccountToEmployeeEventResponseModel")


@_attrs_define
class QualerApiModelsAccountToEmployeeEventResponseModel:
    """
    Attributes:
        id (Union[Unset, int]):
        subject (Union[Unset, str]):
        created_on_utc (Union[Unset, datetime.datetime]):
        event_type_id (Union[Unset, int]):
        event_type_group (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    subject: Union[Unset, str] = UNSET
    created_on_utc: Union[Unset, datetime.datetime] = UNSET
    event_type_id: Union[Unset, int] = UNSET
    event_type_group: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        subject = self.subject

        created_on_utc: Union[Unset, str] = UNSET
        if self.created_on_utc and not isinstance(self.created_on_utc, Unset):
            created_on_utc = self.created_on_utc.isoformat()

        event_type_id = self.event_type_id

        event_type_group = self.event_type_group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if subject is not UNSET:
            field_dict["Subject"] = subject
        if created_on_utc is not UNSET:
            field_dict["CreatedOnUtc"] = created_on_utc
        if event_type_id is not UNSET:
            field_dict["EventTypeId"] = event_type_id
        if event_type_group is not UNSET:
            field_dict["EventTypeGroup"] = event_type_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("Id", UNSET)

        subject = d.pop("Subject", UNSET)

        _created_on_utc = d.pop("CreatedOnUtc", UNSET)
        created_on_utc: Union[Unset, datetime.datetime]
        if isinstance(_created_on_utc, Unset):
            created_on_utc = UNSET
        else:
            created_on_utc = isoparse(_created_on_utc)

        event_type_id = d.pop("EventTypeId", UNSET)

        event_type_group = d.pop("EventTypeGroup", UNSET)

        qualer_api_models_account_to_employee_event_response_model = cls(
            id=id,
            subject=subject,
            created_on_utc=created_on_utc,
            event_type_id=event_type_id,
            event_type_group=event_type_group,
        )

        qualer_api_models_account_to_employee_event_response_model.additional_properties = (
            d
        )
        return qualer_api_models_account_to_employee_event_response_model

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
