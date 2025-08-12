from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualer_api_models_service_orders_to_base_work_item_model_order_item_task_price_model import (
        QualerApiModelsServiceOrdersToBaseWorkItemModelOrderItemTaskPriceModel,
    )
    from ..models.qualer_api_models_service_orders_to_base_work_item_model_order_part_repair_price_model import (
        QualerApiModelsServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel,
    )


T = TypeVar("T", bound="QualerApiModelsServiceOrdersToBaseWorkItemModel")


@_attrs_define
class QualerApiModelsServiceOrdersToBaseWorkItemModel:
    """
    Attributes:
        tasks (Union[Unset, list['QualerApiModelsServiceOrdersToBaseWorkItemModelOrderItemTaskPriceModel']]):
        parts (Union[Unset, list['QualerApiModelsServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel']]):
        repairs (Union[Unset, list['QualerApiModelsServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel']]):
        work_item_id (Union[Unset, int]):
        vendor_tag (Union[Unset, str]):
    """

    tasks: Union[
        Unset,
        list["QualerApiModelsServiceOrdersToBaseWorkItemModelOrderItemTaskPriceModel"],
    ] = UNSET
    parts: Union[
        Unset,
        list[
            "QualerApiModelsServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel"
        ],
    ] = UNSET
    repairs: Union[
        Unset,
        list[
            "QualerApiModelsServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel"
        ],
    ] = UNSET
    work_item_id: Union[Unset, int] = UNSET
    vendor_tag: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tasks: Union[Unset, list[dict[str, Any]]] = UNSET
        if self.tasks and not isinstance(self.tasks, Unset):
            tasks = []
            for tasks_item_data in self.tasks:
                tasks_item = tasks_item_data.to_dict()
                tasks.append(tasks_item)

        parts: Union[Unset, list[dict[str, Any]]] = UNSET
        if self.parts and not isinstance(self.parts, Unset):
            parts = []
            for parts_item_data in self.parts:
                parts_item = parts_item_data.to_dict()
                parts.append(parts_item)

        repairs: Union[Unset, list[dict[str, Any]]] = UNSET
        if self.repairs and not isinstance(self.repairs, Unset):
            repairs = []
            for repairs_item_data in self.repairs:
                repairs_item = repairs_item_data.to_dict()
                repairs.append(repairs_item)

        work_item_id = self.work_item_id

        vendor_tag = self.vendor_tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tasks is not UNSET:
            field_dict["Tasks"] = tasks
        if parts is not UNSET:
            field_dict["Parts"] = parts
        if repairs is not UNSET:
            field_dict["Repairs"] = repairs
        if work_item_id is not UNSET:
            field_dict["WorkItemId"] = work_item_id
        if vendor_tag is not UNSET:
            field_dict["VendorTag"] = vendor_tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_service_orders_to_base_work_item_model_order_item_task_price_model import (
            QualerApiModelsServiceOrdersToBaseWorkItemModelOrderItemTaskPriceModel,
        )
        from ..models.qualer_api_models_service_orders_to_base_work_item_model_order_part_repair_price_model import (
            QualerApiModelsServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel,
        )

        d = dict(src_dict)
        tasks = []
        _tasks = d.pop("Tasks", UNSET)
        for tasks_item_data in _tasks or []:
            tasks_item = QualerApiModelsServiceOrdersToBaseWorkItemModelOrderItemTaskPriceModel.from_dict(
                tasks_item_data
            )

            tasks.append(tasks_item)

        parts = []
        _parts = d.pop("Parts", UNSET)
        for parts_item_data in _parts or []:
            parts_item = QualerApiModelsServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel.from_dict(
                parts_item_data
            )

            parts.append(parts_item)

        repairs = []
        _repairs = d.pop("Repairs", UNSET)
        for repairs_item_data in _repairs or []:
            repairs_item = QualerApiModelsServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel.from_dict(
                repairs_item_data
            )

            repairs.append(repairs_item)

        work_item_id = d.pop("WorkItemId", UNSET)

        vendor_tag = d.pop("VendorTag", UNSET)

        qualer_api_models_service_orders_to_base_work_item_model = cls(
            tasks=tasks,
            parts=parts,
            repairs=repairs,
            work_item_id=work_item_id,
            vendor_tag=vendor_tag,
        )

        qualer_api_models_service_orders_to_base_work_item_model.additional_properties = (
            d
        )
        return qualer_api_models_service_orders_to_base_work_item_model

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
