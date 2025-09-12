from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse")


@_attrs_define
class QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse:
    """
    Attributes:
        field_id (Optional[str]):
        type_ (Optional[int]):
        value (Optional[str]):
        service_order_item_id (Optional[int]):
        service_order_item_task_id (Optional[int]):
    """

    field_id: Optional[str] = None
    type_: Optional[int] = None
    value: Optional[str] = None
    service_order_item_id: Optional[int] = None
    service_order_item_task_id: Optional[int] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_id = self.field_id

        type_ = self.type_

        value = self.value

        service_order_item_id = self.service_order_item_id

        service_order_item_task_id = self.service_order_item_task_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_id is not None:
            field_dict["FieldId"] = field_id
        if type_ is not None:
            field_dict["Type"] = type_
        if value is not None:
            field_dict["Value"] = value
        if service_order_item_id is not None:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if service_order_item_task_id is not None:
            field_dict["ServiceOrderItemTaskId"] = service_order_item_task_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_id = d.pop("FieldId", None)

        type_ = d.pop("Type", None)

        value = d.pop("Value", None)

        service_order_item_id = d.pop("ServiceOrderItemId", None)

        service_order_item_task_id = d.pop("ServiceOrderItemTaskId", None)

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
