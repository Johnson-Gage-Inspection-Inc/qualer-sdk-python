from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QualerApiModelsReportDatasetsToServiceOrderItemTaskResponse")


@_attrs_define
class QualerApiModelsReportDatasetsToServiceOrderItemTaskResponse:
    """
    Attributes:
        id (Optional[int]):
        service_order_item_id (Optional[int]):
        service_charge (Optional[float]):
        time_spent (Optional[float]):
        is_hourly (Optional[bool]):
        as_found_details (Optional[str]):
        as_left_details (Optional[str]):
        price (Optional[float]):
        task_name (Optional[str]):
        task_description (Optional[str]):
        level_description (Optional[str]):
        custom_text_value (Optional[str]):
    """

    id: Optional[int] = None
    service_order_item_id: Optional[int] = None
    service_charge: Optional[float] = None
    time_spent: Optional[float] = None
    is_hourly: Optional[bool] = None
    as_found_details: Optional[str] = None
    as_left_details: Optional[str] = None
    price: Optional[float] = None
    task_name: Optional[str] = None
    task_description: Optional[str] = None
    level_description: Optional[str] = None
    custom_text_value: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not None:
            field_dict["Id"] = id
        if service_order_item_id is not None:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if service_charge is not None:
            field_dict["ServiceCharge"] = service_charge
        if time_spent is not None:
            field_dict["TimeSpent"] = time_spent
        if is_hourly is not None:
            field_dict["IsHourly"] = is_hourly
        if as_found_details is not None:
            field_dict["AsFoundDetails"] = as_found_details
        if as_left_details is not None:
            field_dict["AsLeftDetails"] = as_left_details
        if price is not None:
            field_dict["Price"] = price
        if task_name is not None:
            field_dict["TaskName"] = task_name
        if task_description is not None:
            field_dict["TaskDescription"] = task_description
        if level_description is not None:
            field_dict["LevelDescription"] = level_description
        if custom_text_value is not None:
            field_dict["CustomTextValue"] = custom_text_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("Id", None)

        service_order_item_id = d.pop("ServiceOrderItemId", None)

        service_charge = d.pop("ServiceCharge", None)

        time_spent = d.pop("TimeSpent", None)

        is_hourly = d.pop("IsHourly", None)

        as_found_details = d.pop("AsFoundDetails", None)

        as_left_details = d.pop("AsLeftDetails", None)

        price = d.pop("Price", None)

        task_name = d.pop("TaskName", None)

        task_description = d.pop("TaskDescription", None)

        level_description = d.pop("LevelDescription", None)

        custom_text_value = d.pop("CustomTextValue", None)

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
