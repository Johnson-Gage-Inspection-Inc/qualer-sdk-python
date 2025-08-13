from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsReportDatasetsToServiceOrderItemTaskResponse")


@_attrs_define
class QualerApiModelsReportDatasetsToServiceOrderItemTaskResponse:
    """
    Attributes:
        id (Union[None, Unset, int]):
        service_order_item_id (Union[None, Unset, int]):
        service_charge (Union[None, Unset, float]):
        time_spent (Union[None, Unset, float]):
        is_hourly (Union[None, Unset, bool]):
        as_found_details (Union[None, Unset, str]):
        as_left_details (Union[None, Unset, str]):
        price (Union[None, Unset, float]):
        task_name (Union[None, Unset, str]):
        task_description (Union[None, Unset, str]):
        level_description (Union[None, Unset, str]):
        custom_text_value (Union[None, Unset, str]):
    """

    id: Union[None, Unset, int] = UNSET
    service_order_item_id: Union[None, Unset, int] = UNSET
    service_charge: Union[None, Unset, float] = UNSET
    time_spent: Union[None, Unset, float] = UNSET
    is_hourly: Union[None, Unset, bool] = UNSET
    as_found_details: Union[None, Unset, str] = UNSET
    as_left_details: Union[None, Unset, str] = UNSET
    price: Union[None, Unset, float] = UNSET
    task_name: Union[None, Unset, str] = UNSET
    task_description: Union[None, Unset, str] = UNSET
    level_description: Union[None, Unset, str] = UNSET
    custom_text_value: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        service_order_item_id = self.service_order_item_id

        service_charge = self.service_charge

        time_spent = self.time_spent

        is_hourly = self.is_hourly

        as_found_details = self.as_found_details

        as_left_details = self.as_left_details

        price = self.price

        task_name = self.task_name

        task_description = self.task_description

        level_description = self.level_description

        custom_text_value = self.custom_text_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if service_order_item_id is not UNSET:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if service_charge is not UNSET:
            field_dict["ServiceCharge"] = service_charge
        if time_spent is not UNSET:
            field_dict["TimeSpent"] = time_spent
        if is_hourly is not UNSET:
            field_dict["IsHourly"] = is_hourly
        if as_found_details is not UNSET:
            field_dict["AsFoundDetails"] = as_found_details
        if as_left_details is not UNSET:
            field_dict["AsLeftDetails"] = as_left_details
        if price is not UNSET:
            field_dict["Price"] = price
        if task_name is not UNSET:
            field_dict["TaskName"] = task_name
        if task_description is not UNSET:
            field_dict["TaskDescription"] = task_description
        if level_description is not UNSET:
            field_dict["LevelDescription"] = level_description
        if custom_text_value is not UNSET:
            field_dict["CustomTextValue"] = custom_text_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("Id", UNSET)

        service_order_item_id = d.pop("ServiceOrderItemId", UNSET)

        service_charge = d.pop("ServiceCharge", UNSET)

        time_spent = d.pop("TimeSpent", UNSET)

        is_hourly = d.pop("IsHourly", UNSET)

        as_found_details = d.pop("AsFoundDetails", UNSET)

        as_left_details = d.pop("AsLeftDetails", UNSET)

        price = d.pop("Price", UNSET)

        task_name = d.pop("TaskName", UNSET)

        task_description = d.pop("TaskDescription", UNSET)

        level_description = d.pop("LevelDescription", UNSET)

        custom_text_value = d.pop("CustomTextValue", UNSET)

        qualer_api_models_report_datasets_to_service_order_item_task_response = cls(
            id=id,
            service_order_item_id=service_order_item_id,
            service_charge=service_charge,
            time_spent=time_spent,
            is_hourly=is_hourly,
            as_found_details=as_found_details,
            as_left_details=as_left_details,
            price=price,
            task_name=task_name,
            task_description=task_description,
            level_description=level_description,
            custom_text_value=custom_text_value,
        )

        qualer_api_models_report_datasets_to_service_order_item_task_response.additional_properties = (
            d
        )
        return qualer_api_models_report_datasets_to_service_order_item_task_response

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
