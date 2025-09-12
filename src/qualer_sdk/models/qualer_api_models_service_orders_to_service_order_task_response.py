import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="QualerApiModelsServiceOrdersToServiceOrderTaskResponse")


@_attrs_define
class QualerApiModelsServiceOrdersToServiceOrderTaskResponse:
    """
    Attributes:
        service_order_task_id (Optional[int]):
        task_name (Optional[str]):
        task_order (Optional[int]):
        task_details (Optional[str]):
        time_spent (Optional[float]):
        time_spent_in_minutes (Optional[int]):
        start_time (Optional[datetime.datetime]):
        finish_time (Optional[datetime.datetime]):
        price (Optional[float]):
        is_hourly (Optional[bool]):
    """

    service_order_task_id: Optional[int] = None
    task_name: Optional[str] = None
    task_order: Optional[int] = None
    task_details: Optional[str] = None
    time_spent: Optional[float] = None
    time_spent_in_minutes: Optional[int] = None
    start_time: Optional[datetime.datetime] = None
    finish_time: Optional[datetime.datetime] = None
    price: Optional[float] = None
    is_hourly: Optional[bool] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_order_task_id = self.service_order_task_id

        task_name = self.task_name

        task_order = self.task_order

        task_details = self.task_details

        time_spent = self.time_spent

        time_spent_in_minutes = self.time_spent_in_minutes

        start_time: Optional[str] = None
        if self.start_time:
            start_time = self.start_time.isoformat()

        finish_time: Optional[str] = None
        if self.finish_time:
            finish_time = self.finish_time.isoformat()

        price = self.price

        is_hourly = self.is_hourly

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_task_id is not None:
            field_dict["ServiceOrderTaskId"] = service_order_task_id
        if task_name is not None:
            field_dict["TaskName"] = task_name
        if task_order is not None:
            field_dict["TaskOrder"] = task_order
        if task_details is not None:
            field_dict["TaskDetails"] = task_details
        if time_spent is not None:
            field_dict["TimeSpent"] = time_spent
        if time_spent_in_minutes is not None:
            field_dict["TimeSpentInMinutes"] = time_spent_in_minutes
        if start_time is not None:
            field_dict["StartTime"] = start_time
        if finish_time is not None:
            field_dict["FinishTime"] = finish_time
        if price is not None:
            field_dict["Price"] = price
        if is_hourly is not None:
            field_dict["IsHourly"] = is_hourly

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_task_id = d.pop("ServiceOrderTaskId", None)

        task_name = d.pop("TaskName", None)

        task_order = d.pop("TaskOrder", None)

        task_details = d.pop("TaskDetails", None)

        time_spent = d.pop("TimeSpent", None)

        time_spent_in_minutes = d.pop("TimeSpentInMinutes", None)

        _start_time = d.pop("StartTime", None)
        start_time: Optional[datetime.datetime]
        if not _start_time:
            start_time = None
        else:
            start_time = isoparse(_start_time)

        _finish_time = d.pop("FinishTime", None)
        finish_time: Optional[datetime.datetime]
        if not _finish_time:
            finish_time = None
        else:
            finish_time = isoparse(_finish_time)

        price = d.pop("Price", None)

        is_hourly = d.pop("IsHourly", None)

        qualer_api_models_service_orders_to_service_order_task_response = cls(
            service_order_task_id=service_order_task_id,
            task_name=task_name,
            task_order=task_order,
            task_details=task_details,
            time_spent=time_spent,
            time_spent_in_minutes=time_spent_in_minutes,
            start_time=start_time,
            finish_time=finish_time,
            price=price,
            is_hourly=is_hourly,
        )

        qualer_api_models_service_orders_to_service_order_task_response.additional_properties = d
        return qualer_api_models_service_orders_to_service_order_task_response

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
