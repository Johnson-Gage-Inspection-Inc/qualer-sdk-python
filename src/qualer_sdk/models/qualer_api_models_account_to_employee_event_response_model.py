import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="AccountToEmployeeEventResponseModel")


@_attrs_define
class AccountToEmployeeEventResponseModel:
    """
    Attributes:
        id (Optional[int]):
        subject (Optional[str]):
        created_on_utc (Optional[datetime.datetime]):
        event_type_id (Optional[int]):
        event_type_group (Optional[str]):
    """

    id: Optional[int] = None
    subject: Optional[str] = None
    created_on_utc: Optional[datetime.datetime] = None
    event_type_id: Optional[int] = None
    event_type_group: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        subject = self.subject

        created_on_utc: Optional[str] = None
        if self.created_on_utc:
            created_on_utc = self.created_on_utc.isoformat()

        event_type_id = self.event_type_id

        event_type_group = self.event_type_group

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not None:
            field_dict["Id"] = id
        if subject is not None:
            field_dict["Subject"] = subject
        if created_on_utc is not None:
            field_dict["CreatedOnUtc"] = created_on_utc
        if event_type_id is not None:
            field_dict["EventTypeId"] = event_type_id
        if event_type_group is not None:
            field_dict["EventTypeGroup"] = event_type_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("Id", None)

        subject = d.pop("Subject", None)

        _created_on_utc = d.pop("CreatedOnUtc", None)
        created_on_utc: Optional[datetime.datetime]
        if not _created_on_utc:
            created_on_utc = None
        else:
            created_on_utc = isoparse(_created_on_utc)

        event_type_id = d.pop("EventTypeId", None)

        event_type_group = d.pop("EventTypeGroup", None)

        qualer_api_models_account_to_employee_event_response_model = cls(
            id=id,
            subject=subject,
            created_on_utc=created_on_utc,
            event_type_id=event_type_id,
            event_type_group=event_type_group,
        )

        qualer_api_models_account_to_employee_event_response_model.additional_properties = d
        return qualer_api_models_account_to_employee_event_response_model

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
