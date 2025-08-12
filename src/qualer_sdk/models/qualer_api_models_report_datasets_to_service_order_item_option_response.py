from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsReportDatasetsToServiceOrderItemOptionResponse")


@_attrs_define
class QualerApiModelsReportDatasetsToServiceOrderItemOptionResponse:
    """
    Attributes:
        service_order_item_id (Union[None, Unset, int]):
        service_charge (Union[None, Unset, float]):
        time_spent (Union[None, Unset, float]):
        is_hourly (Union[None, Unset, bool]):
        price (Union[None, Unset, float]):
        task_name (Union[None, Unset, str]):
    """

    service_order_item_id: Union[None, Unset, int] = UNSET
    service_charge: Union[None, Unset, float] = UNSET
    time_spent: Union[None, Unset, float] = UNSET
    is_hourly: Union[None, Unset, bool] = UNSET
    price: Union[None, Unset, float] = UNSET
    task_name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_order_item_id = self.service_order_item_id

        service_charge = self.service_charge

        time_spent = self.time_spent

        is_hourly = self.is_hourly

        price = self.price

        task_name = self.task_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_item_id is not UNSET:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if service_charge is not UNSET:
            field_dict["ServiceCharge"] = service_charge
        if time_spent is not UNSET:
            field_dict["TimeSpent"] = time_spent
        if is_hourly is not UNSET:
            field_dict["IsHourly"] = is_hourly
        if price is not UNSET:
            field_dict["Price"] = price
        if task_name is not UNSET:
            field_dict["TaskName"] = task_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_item_id = d.pop("ServiceOrderItemId", UNSET)

        service_charge = d.pop("ServiceCharge", UNSET)

        time_spent = d.pop("TimeSpent", UNSET)

        is_hourly = d.pop("IsHourly", UNSET)

        price = d.pop("Price", UNSET)

        task_name = d.pop("TaskName", UNSET)

        qualer_api_models_report_datasets_to_service_order_item_option_response = cls(
            service_order_item_id=service_order_item_id,
            service_charge=service_charge,
            time_spent=time_spent,
            is_hourly=is_hourly,
            price=price,
            task_name=task_name,
        )

        qualer_api_models_report_datasets_to_service_order_item_option_response.additional_properties = (
            d
        )
        return qualer_api_models_report_datasets_to_service_order_item_option_response

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
