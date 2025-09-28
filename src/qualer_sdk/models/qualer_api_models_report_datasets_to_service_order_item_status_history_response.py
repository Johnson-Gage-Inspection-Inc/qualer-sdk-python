import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ReportDatasetsToServiceOrderItemStatusHistoryResponse")


@_attrs_define
class ReportDatasetsToServiceOrderItemStatusHistoryResponse:
    """
    Attributes:
        service_order_item_id (Optional[int]):
        previous_status_name (Optional[str]):
        selected_status_name (Optional[str]):
        explanation (Optional[str]):
        is_password_reentered (Optional[bool]):
        created_on (Optional[datetime.datetime]):
        created_on_utc (Optional[datetime.datetime]):
        employee_id (Optional[int]):
        first_name (Optional[str]):
        last_name (Optional[str]):
        alias (Optional[str]):
    """

    service_order_item_id: Optional[int] = None
    previous_status_name: Optional[str] = None
    selected_status_name: Optional[str] = None
    explanation: Optional[str] = None
    is_password_reentered: Optional[bool] = None
    created_on: Optional[datetime.datetime] = None
    created_on_utc: Optional[datetime.datetime] = None
    employee_id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    alias: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_order_item_id = self.service_order_item_id
        previous_status_name = self.previous_status_name
        selected_status_name = self.selected_status_name
        explanation = self.explanation
        is_password_reentered = self.is_password_reentered
        created_on: Optional[str] = None
        if self.created_on:
            created_on = self.created_on.isoformat()
        created_on_utc: Optional[str] = None
        if self.created_on_utc:
            created_on_utc = self.created_on_utc.isoformat()
        employee_id = self.employee_id
        first_name = self.first_name
        last_name = self.last_name
        alias = self.alias
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_item_id is not None:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if previous_status_name is not None:
            field_dict["PreviousStatusName"] = previous_status_name
        if selected_status_name is not None:
            field_dict["SelectedStatusName"] = selected_status_name
        if explanation is not None:
            field_dict["Explanation"] = explanation
        if is_password_reentered is not None:
            field_dict["IsPasswordReentered"] = is_password_reentered
        if created_on is not None:
            field_dict["CreatedOn"] = created_on
        if created_on_utc is not None:
            field_dict["CreatedOnUtc"] = created_on_utc
        if employee_id is not None:
            field_dict["EmployeeId"] = employee_id
        if first_name is not None:
            field_dict["FirstName"] = first_name
        if last_name is not None:
            field_dict["LastName"] = last_name
        if alias is not None:
            field_dict["Alias"] = alias
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_item_id = d.pop("ServiceOrderItemId", None)
        previous_status_name = d.pop("PreviousStatusName", None)
        selected_status_name = d.pop("SelectedStatusName", None)
        explanation = d.pop("Explanation", None)
        is_password_reentered = d.pop("IsPasswordReentered", None)
        _created_on = d.pop("CreatedOn", None)
        created_on: Optional[datetime.datetime]
        if not _created_on:
            created_on = None
        else:
            created_on = isoparse(_created_on)
        _created_on_utc = d.pop("CreatedOnUtc", None)
        created_on_utc: Optional[datetime.datetime]
        if not _created_on_utc:
            created_on_utc = None
        else:
            created_on_utc = isoparse(_created_on_utc)
        employee_id = d.pop("EmployeeId", None)
        first_name = d.pop("FirstName", None)
        last_name = d.pop("LastName", None)
        alias = d.pop("Alias", None)
        qualer_api_models_report_datasets_to_service_order_item_status_history_response = cls(
            service_order_item_id=service_order_item_id,
            previous_status_name=previous_status_name,
            selected_status_name=selected_status_name,
            explanation=explanation,
            is_password_reentered=is_password_reentered,
            created_on=created_on,
            created_on_utc=created_on_utc,
            employee_id=employee_id,
            first_name=first_name,
            last_name=last_name,
            alias=alias,
        )
        qualer_api_models_report_datasets_to_service_order_item_status_history_response.additional_properties = (
            d
        )
        return qualer_api_models_report_datasets_to_service_order_item_status_history_response

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
