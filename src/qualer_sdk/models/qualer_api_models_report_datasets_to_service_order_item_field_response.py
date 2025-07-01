from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse")


@_attrs_define
class QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse:
    """
    Attributes:
        field_id (Union[Unset, str]):
        type_ (Union[Unset, int]):
        value (Union[Unset, str]):
        service_order_item_id (Union[Unset, int]):
        service_order_item_task_id (Union[Unset, int]):
    """

    field_id: Union[Unset, str] = UNSET
    type_: Union[Unset, int] = UNSET
    value: Union[Unset, str] = UNSET
    service_order_item_id: Union[Unset, int] = UNSET
    service_order_item_task_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        type_ = self.type_

        value = self.value

        service_order_item_id = self.service_order_item_id

        service_order_item_task_id = self.service_order_item_task_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_id is not UNSET:
            field_dict["FieldId"] = field_id
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if value is not UNSET:
            field_dict["Value"] = value
        if service_order_item_id is not UNSET:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if service_order_item_task_id is not UNSET:
            field_dict["ServiceOrderItemTaskId"] = service_order_item_task_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_id = d.pop("FieldId", UNSET)

        type_ = d.pop("Type", UNSET)

        value = d.pop("Value", UNSET)

        service_order_item_id = d.pop("ServiceOrderItemId", UNSET)

        service_order_item_task_id = d.pop("ServiceOrderItemTaskId", UNSET)

        qualer_api_models_report_datasets_to_service_order_item_field_response = cls(
            field_id=field_id,
            type_=type_,
            value=value,
            service_order_item_id=service_order_item_id,
            service_order_item_task_id=service_order_item_task_id,
        )

        qualer_api_models_report_datasets_to_service_order_item_field_response.additional_properties = (
            d
        )
        return qualer_api_models_report_datasets_to_service_order_item_field_response

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
