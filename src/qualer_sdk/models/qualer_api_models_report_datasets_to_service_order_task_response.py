from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsReportDatasetsToServiceOrderTaskResponse")


@_attrs_define
class QualerApiModelsReportDatasetsToServiceOrderTaskResponse:
    """
    Attributes:
        task_name (Union[None, Unset, str]):
        task_order (Union[None, Unset, int]):
        task_details (Union[None, Unset, str]):
        time_spent (Union[None, Unset, float]):
        time_spent_hours (Union[None, Unset, float]):
        time_spent_minutes (Union[None, Unset, float]):
        price (Union[None, Unset, float]):
        is_hourly (Union[None, Unset, bool]):
    """

    task_name: Union[None, Unset, str] = UNSET
    task_order: Union[None, Unset, int] = UNSET
    task_details: Union[None, Unset, str] = UNSET
    time_spent: Union[None, Unset, float] = UNSET
    time_spent_hours: Union[None, Unset, float] = UNSET
    time_spent_minutes: Union[None, Unset, float] = UNSET
    price: Union[None, Unset, float] = UNSET
    is_hourly: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_name = self.task_name

        task_order = self.task_order

        task_details = self.task_details

        time_spent = self.time_spent

        time_spent_hours = self.time_spent_hours

        time_spent_minutes = self.time_spent_minutes

        price = self.price

        is_hourly = self.is_hourly

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_name is not UNSET:
            field_dict["TaskName"] = task_name
        if task_order is not UNSET:
            field_dict["TaskOrder"] = task_order
        if task_details is not UNSET:
            field_dict["TaskDetails"] = task_details
        if time_spent is not UNSET:
            field_dict["TimeSpent"] = time_spent
        if time_spent_hours is not UNSET:
            field_dict["TimeSpentHours"] = time_spent_hours
        if time_spent_minutes is not UNSET:
            field_dict["TimeSpentMinutes"] = time_spent_minutes
        if price is not UNSET:
            field_dict["Price"] = price
        if is_hourly is not UNSET:
            field_dict["IsHourly"] = is_hourly

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task_name = d.pop("TaskName", UNSET)

        task_order = d.pop("TaskOrder", UNSET)

        task_details = d.pop("TaskDetails", UNSET)

        time_spent = d.pop("TimeSpent", UNSET)

        time_spent_hours = d.pop("TimeSpentHours", UNSET)

        time_spent_minutes = d.pop("TimeSpentMinutes", UNSET)

        price = d.pop("Price", UNSET)

        is_hourly = d.pop("IsHourly", UNSET)

        qualer_api_models_report_datasets_to_service_order_task_response = cls(
            task_name=task_name,
            task_order=task_order,
            task_details=task_details,
            time_spent=time_spent,
            time_spent_hours=time_spent_hours,
            time_spent_minutes=time_spent_minutes,
            price=price,
            is_hourly=is_hourly,
        )

        qualer_api_models_report_datasets_to_service_order_task_response.additional_properties = (
            d
        )
        return qualer_api_models_report_datasets_to_service_order_task_response

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
