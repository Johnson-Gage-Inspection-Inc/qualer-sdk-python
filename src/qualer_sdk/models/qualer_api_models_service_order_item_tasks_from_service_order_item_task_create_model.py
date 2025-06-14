from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel"
)


@_attrs_define
class QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel:
    """
    Attributes:
        service_order_item_id (Union[Unset, int]):
        task_name (Union[Unset, str]):
        task_description (Union[Unset, str]):
        as_found_details (Union[Unset, str]):
        as_left_details (Union[Unset, str]):
    """

    service_order_item_id: Union[Unset, int] = UNSET
    task_name: Union[Unset, str] = UNSET
    task_description: Union[Unset, str] = UNSET
    as_found_details: Union[Unset, str] = UNSET
    as_left_details: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_order_item_id = self.service_order_item_id

        task_name = self.task_name

        task_description = self.task_description

        as_found_details = self.as_found_details

        as_left_details = self.as_left_details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_item_id is not UNSET:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if task_name is not UNSET:
            field_dict["TaskName"] = task_name
        if task_description is not UNSET:
            field_dict["TaskDescription"] = task_description
        if as_found_details is not UNSET:
            field_dict["AsFoundDetails"] = as_found_details
        if as_left_details is not UNSET:
            field_dict["AsLeftDetails"] = as_left_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_item_id = d.pop("ServiceOrderItemId", UNSET)

        task_name = d.pop("TaskName", UNSET)

        task_description = d.pop("TaskDescription", UNSET)

        as_found_details = d.pop("AsFoundDetails", UNSET)

        as_left_details = d.pop("AsLeftDetails", UNSET)

        qualer_api_models_service_order_item_tasks_from_service_order_item_task_create_model = cls(
            service_order_item_id=service_order_item_id,
            task_name=task_name,
            task_description=task_description,
            as_found_details=as_found_details,
            as_left_details=as_left_details,
        )

        qualer_api_models_service_order_item_tasks_from_service_order_item_task_create_model.additional_properties = (
            d
        )
        return qualer_api_models_service_order_item_tasks_from_service_order_item_task_create_model

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
