from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.qualer_api_models_service_orders_to_base_work_item_model_order_item_task_price_model import (
        ServiceOrdersToBaseWorkItemModelOrderItemTaskPriceModel,
    )
    from ..models.qualer_api_models_service_orders_to_base_work_item_model_order_part_repair_price_model import (
        ServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel,
    )


T = TypeVar("T", bound="ServiceOrdersToBaseWorkItemModel")


@_attrs_define
class ServiceOrdersToBaseWorkItemModel:
    """
    Attributes:
        tasks (Optional[List['ServiceOrdersToBaseWorkItemModelOrderItemTaskPriceModel']]):
        parts (Optional[List['ServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel']]):
        repairs (Optional[List['ServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel']]):
        work_item_id (Optional[int]):
        vendor_tag (Optional[str]):
    """

    tasks: Union[
        None,
        None,
        List["ServiceOrdersToBaseWorkItemModelOrderItemTaskPriceModel"],
    ] = None
    parts: Union[
        None,
        None,
        List["ServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel"],
    ] = None
    repairs: Union[
        None,
        None,
        List["ServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel"],
    ] = None
    work_item_id: Optional[int] = None
    vendor_tag: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tasks: Optional[List[Dict[str, Any]]] = None
        if self.tasks:
            tasks = []
            for tasks_item_data in self.tasks:
                tasks_item = tasks_item_data.to_dict()
                tasks.append(tasks_item)
        parts: Optional[List[Dict[str, Any]]] = None
        if self.parts:
            parts = []
            for parts_item_data in self.parts:
                parts_item = parts_item_data.to_dict()
                parts.append(parts_item)
        repairs: Optional[List[Dict[str, Any]]] = None
        if self.repairs:
            repairs = []
            for repairs_item_data in self.repairs:
                repairs_item = repairs_item_data.to_dict()
                repairs.append(repairs_item)
        work_item_id = self.work_item_id
        vendor_tag = self.vendor_tag
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tasks is not None:
            field_dict["Tasks"] = tasks
        if parts is not None:
            field_dict["Parts"] = parts
        if repairs is not None:
            field_dict["Repairs"] = repairs
        if work_item_id is not None:
            field_dict["WorkItemId"] = work_item_id
        if vendor_tag is not None:
            field_dict["VendorTag"] = vendor_tag
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_service_orders_to_base_work_item_model_order_item_task_price_model import (
            ServiceOrdersToBaseWorkItemModelOrderItemTaskPriceModel,
        )
        from ..models.qualer_api_models_service_orders_to_base_work_item_model_order_part_repair_price_model import (
            ServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel,
        )

        d = dict(src_dict)
        tasks = []
        _tasks = d.pop("Tasks", None)
        for tasks_item_data in _tasks or []:
            tasks_item = ServiceOrdersToBaseWorkItemModelOrderItemTaskPriceModel.from_dict(
                tasks_item_data
            )
            tasks.append(tasks_item)
        parts = []
        _parts = d.pop("Parts", None)
        for parts_item_data in _parts or []:
            parts_item = ServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel.from_dict(
                parts_item_data
            )
            parts.append(parts_item)
        repairs = []
        _repairs = d.pop("Repairs", None)
        for repairs_item_data in _repairs or []:
            repairs_item = ServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel.from_dict(
                repairs_item_data
            )
            repairs.append(repairs_item)
        work_item_id = d.pop("WorkItemId", None)
        vendor_tag = d.pop("VendorTag", None)
        qualer_api_models_service_orders_to_base_work_item_model = cls(
            tasks=tasks,
            parts=parts,
            repairs=repairs,
            work_item_id=work_item_id,
            vendor_tag=vendor_tag,
        )
        qualer_api_models_service_orders_to_base_work_item_model.additional_properties = d
        return qualer_api_models_service_orders_to_base_work_item_model

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
