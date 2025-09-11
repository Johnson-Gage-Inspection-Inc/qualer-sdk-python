from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QualerApiModelsReportDatasetsToServiceOrderTaskResponse")


@_attrs_define
class QualerApiModelsReportDatasetsToServiceOrderTaskResponse:
    """
    Attributes:
        task_name (Optional[str]):
        task_order (Optional[int]):
        task_details (Optional[str]):
        time_spent (Optional[float]):
        time_spent_hours (Optional[float]):
        time_spent_minutes (Optional[float]):
        price (Optional[float]):
        is_hourly (Optional[bool]):
    """

    task_name: Optional[str] = None
    task_order: Optional[int] = None
    task_details: Optional[str] = None
    time_spent: Optional[float] = None
    time_spent_hours: Optional[float] = None
    time_spent_minutes: Optional[float] = None
    price: Optional[float] = None
    is_hourly: Optional[bool] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        task_name = self.task_name

        task_order = self.task_order

        task_details = self.task_details

        time_spent = self.time_spent

        time_spent_hours = self.time_spent_hours

        time_spent_minutes = self.time_spent_minutes

        price = self.price

        is_hourly = self.is_hourly

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_name is not None:
            field_dict["TaskName"] = task_name
        if task_order is not None:
            field_dict["TaskOrder"] = task_order
        if task_details is not None:
            field_dict["TaskDetails"] = task_details
        if time_spent is not None:
            field_dict["TimeSpent"] = time_spent
        if time_spent_hours is not None:
            field_dict["TimeSpentHours"] = time_spent_hours
        if time_spent_minutes is not None:
            field_dict["TimeSpentMinutes"] = time_spent_minutes
        if price is not None:
            field_dict["Price"] = price
        if is_hourly is not None:
            field_dict["IsHourly"] = is_hourly

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task_name = d.pop("TaskName", None)

        task_order = d.pop("TaskOrder", None)

        task_details = d.pop("TaskDetails", None)

        time_spent = d.pop("TimeSpent", None)

        time_spent_hours = d.pop("TimeSpentHours", None)

        time_spent_minutes = d.pop("TimeSpentMinutes", None)

        price = d.pop("Price", None)

        is_hourly = d.pop("IsHourly", None)

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

        qualer_api_models_report_datasets_to_service_order_task_response.additional_properties = d
        return qualer_api_models_report_datasets_to_service_order_task_response

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
