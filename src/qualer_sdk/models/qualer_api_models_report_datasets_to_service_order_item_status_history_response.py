import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="QualerApiModelsReportDatasetsToServiceOrderItemStatusHistoryResponse"
)


@_attrs_define
class QualerApiModelsReportDatasetsToServiceOrderItemStatusHistoryResponse:
    """
    Attributes:
        service_order_item_id (Union[None, Unset, int]):
        previous_status_name (Union[None, Unset, str]):
        selected_status_name (Union[None, Unset, str]):
        explanation (Union[None, Unset, str]):
        is_password_reentered (Union[None, Unset, bool]):
        created_on (Union[None, Unset, datetime.datetime]):
        created_on_utc (Union[None, Unset, datetime.datetime]):
        employee_id (Union[None, Unset, int]):
        first_name (Union[None, Unset, str]):
        last_name (Union[None, Unset, str]):
        alias (Union[None, Unset, str]):
    """

    service_order_item_id: Union[None, Unset, int] = UNSET
    previous_status_name: Union[None, Unset, str] = UNSET
    selected_status_name: Union[None, Unset, str] = UNSET
    explanation: Union[None, Unset, str] = UNSET
    is_password_reentered: Union[None, Unset, bool] = UNSET
    created_on: Union[None, Unset, datetime.datetime] = UNSET
    created_on_utc: Union[None, Unset, datetime.datetime] = UNSET
    employee_id: Union[None, Unset, int] = UNSET
    first_name: Union[None, Unset, str] = UNSET
    last_name: Union[None, Unset, str] = UNSET
    alias: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_order_item_id = self.service_order_item_id

        previous_status_name = self.previous_status_name

        selected_status_name = self.selected_status_name

        explanation = self.explanation

        is_password_reentered = self.is_password_reentered

        created_on: Union[None, Unset, str] = UNSET
        if self.created_on and not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        created_on_utc: Union[None, Unset, str] = UNSET
        if self.created_on_utc and not isinstance(self.created_on_utc, Unset):
            created_on_utc = self.created_on_utc.isoformat()

        employee_id = self.employee_id

        first_name = self.first_name

        last_name = self.last_name

        alias = self.alias

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_item_id is not UNSET:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if previous_status_name is not UNSET:
            field_dict["PreviousStatusName"] = previous_status_name
        if selected_status_name is not UNSET:
            field_dict["SelectedStatusName"] = selected_status_name
        if explanation is not UNSET:
            field_dict["Explanation"] = explanation
        if is_password_reentered is not UNSET:
            field_dict["IsPasswordReentered"] = is_password_reentered
        if created_on is not UNSET:
            field_dict["CreatedOn"] = created_on
        if created_on_utc is not UNSET:
            field_dict["CreatedOnUtc"] = created_on_utc
        if employee_id is not UNSET:
            field_dict["EmployeeId"] = employee_id
        if first_name is not UNSET:
            field_dict["FirstName"] = first_name
        if last_name is not UNSET:
            field_dict["LastName"] = last_name
        if alias is not UNSET:
            field_dict["Alias"] = alias

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_item_id = d.pop("ServiceOrderItemId", UNSET)

        previous_status_name = d.pop("PreviousStatusName", UNSET)

        selected_status_name = d.pop("SelectedStatusName", UNSET)

        explanation = d.pop("Explanation", UNSET)

        is_password_reentered = d.pop("IsPasswordReentered", UNSET)

        _created_on = d.pop("CreatedOn", UNSET)
        created_on: Union[None, Unset, datetime.datetime]
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = isoparse(_created_on)

        _created_on_utc = d.pop("CreatedOnUtc", UNSET)
        created_on_utc: Union[None, Unset, datetime.datetime]
        if isinstance(_created_on_utc, Unset):
            created_on_utc = UNSET
        else:
            created_on_utc = isoparse(_created_on_utc)

        employee_id = d.pop("EmployeeId", UNSET)

        first_name = d.pop("FirstName", UNSET)

        last_name = d.pop("LastName", UNSET)

        alias = d.pop("Alias", UNSET)

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
