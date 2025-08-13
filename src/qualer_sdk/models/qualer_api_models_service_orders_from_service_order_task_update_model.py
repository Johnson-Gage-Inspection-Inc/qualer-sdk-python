import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsServiceOrdersFromServiceOrderTaskUpdateModel")


@_attrs_define
class QualerApiModelsServiceOrdersFromServiceOrderTaskUpdateModel:
    """
    Attributes:
        service_order_task_id (Union[None, Unset, int]):
        task_name (Union[None, Unset, str]):
        task_details (Union[None, Unset, str]):
        start_time (Union[None, Unset, datetime.datetime]):
        finish_time (Union[None, Unset, datetime.datetime]):
        time_spent_minutes (Union[None, Unset, int]):
        price (Union[None, Unset, float]):
        is_hourly (Union[None, Unset, bool]):
    """

    service_order_task_id: Union[None, Unset, int] = UNSET
    task_name: Union[None, Unset, str] = UNSET
    task_details: Union[None, Unset, str] = UNSET
    start_time: Union[None, Unset, datetime.datetime] = UNSET
    finish_time: Union[None, Unset, datetime.datetime] = UNSET
    time_spent_minutes: Union[None, Unset, int] = UNSET
    price: Union[None, Unset, float] = UNSET
    is_hourly: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_order_task_id = self.service_order_task_id

        task_name = self.task_name

        task_details = self.task_details

        start_time: Union[None, Unset, str] = UNSET
        if self.start_time and not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        finish_time: Union[None, Unset, str] = UNSET
        if self.finish_time and not isinstance(self.finish_time, Unset):
            finish_time = self.finish_time.isoformat()

        time_spent_minutes = self.time_spent_minutes

        price = self.price

        is_hourly = self.is_hourly

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_task_id is not UNSET:
            field_dict["ServiceOrderTaskId"] = service_order_task_id
        if task_name is not UNSET:
            field_dict["TaskName"] = task_name
        if task_details is not UNSET:
            field_dict["TaskDetails"] = task_details
        if start_time is not UNSET:
            field_dict["StartTime"] = start_time
        if finish_time is not UNSET:
            field_dict["FinishTime"] = finish_time
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
        service_order_task_id = d.pop("ServiceOrderTaskId", UNSET)

        task_name = d.pop("TaskName", UNSET)

        task_details = d.pop("TaskDetails", UNSET)

        _start_time = d.pop("StartTime", UNSET)
        start_time: Union[None, Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _finish_time = d.pop("FinishTime", UNSET)
        finish_time: Union[None, Unset, datetime.datetime]
        if isinstance(_finish_time, Unset):
            finish_time = UNSET
        else:
            finish_time = isoparse(_finish_time)

        time_spent_minutes = d.pop("TimeSpentMinutes", UNSET)

        price = d.pop("Price", UNSET)

        is_hourly = d.pop("IsHourly", UNSET)

        qualer_api_models_service_orders_from_service_order_task_update_model = cls(
            service_order_task_id=service_order_task_id,
            task_name=task_name,
            task_details=task_details,
            start_time=start_time,
            finish_time=finish_time,
            time_spent_minutes=time_spent_minutes,
            price=price,
            is_hourly=is_hourly,
        )

        qualer_api_models_service_orders_from_service_order_task_update_model.additional_properties = (
            d
        )
        return qualer_api_models_service_orders_from_service_order_task_update_model

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
