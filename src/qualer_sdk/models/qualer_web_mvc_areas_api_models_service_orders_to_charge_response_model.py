from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.qualer_api_models_service_orders_to_base_work_item_model import (
        ServiceOrdersToBaseWorkItemModel,
    )
    from ..models.qualer_api_models_service_orders_to_charge_response_model_base_order_part_repair_price_model import (
        ServiceOrdersToChargeResponseModelBaseOrderPartRepairPriceModel,
    )
    from ..models.qualer_api_models_service_orders_to_charge_response_model_base_order_task_price_model import (
        ServiceOrdersToChargeResponseModelBaseOrderTaskPriceModel,
    )
    from ..models.qualer_api_models_service_orders_to_charge_response_model_base_price_model import (
        ServiceOrdersToChargeResponseModelBasePriceModel,
    )


T = TypeVar("T", bound="QualerWebMvcAreasApiModelsServiceOrdersToChargeResponseModel")


@_attrs_define
class QualerWebMvcAreasApiModelsServiceOrdersToChargeResponseModel:
    """
    Attributes:
        charges (Optional[List['ServiceOrdersToChargeResponseModelBasePriceModel']]):
        tasks (Optional[List['ServiceOrdersToChargeResponseModelBaseOrderTaskPriceModel']]):
        parts (Optional[List['ServiceOrdersToChargeResponseModelBaseOrderPartRepairPriceModel']]):
        repairs (Optional[List['ServiceOrdersToChargeResponseModelBaseOrderPartRepairPriceModel']]):
        work_items (Optional[List['ServiceOrdersToBaseWorkItemModel']]):
    """

    charges: Union[
        None,
        None,
        List["ServiceOrdersToChargeResponseModelBasePriceModel"],
    ] = None
    tasks: Union[
        None,
        None,
        List["ServiceOrdersToChargeResponseModelBaseOrderTaskPriceModel"],
    ] = None
    parts: Union[
        None,
        None,
        List["ServiceOrdersToChargeResponseModelBaseOrderPartRepairPriceModel"],
    ] = None
    repairs: Union[
        None,
        None,
        List["ServiceOrdersToChargeResponseModelBaseOrderPartRepairPriceModel"],
    ] = None
    work_items: Optional[List["ServiceOrdersToBaseWorkItemModel"]] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        charges: Optional[List[Dict[str, Any]]] = None
        if self.charges:
            charges = []
            for charges_item_data in self.charges:
                charges_item = charges_item_data.to_dict()
                charges.append(charges_item)

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

        work_items: Optional[List[Dict[str, Any]]] = None
        if self.work_items:
            work_items = []
            for work_items_item_data in self.work_items:
                work_items_item = work_items_item_data.to_dict()
                work_items.append(work_items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if charges is not None:
            field_dict["Charges"] = charges
        if tasks is not None:
            field_dict["Tasks"] = tasks
        if parts is not None:
            field_dict["Parts"] = parts
        if repairs is not None:
            field_dict["Repairs"] = repairs
        if work_items is not None:
            field_dict["WorkItems"] = work_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_service_orders_to_base_work_item_model import (
            ServiceOrdersToBaseWorkItemModel,
        )
        from ..models.qualer_api_models_service_orders_to_charge_response_model_base_order_part_repair_price_model import (
            ServiceOrdersToChargeResponseModelBaseOrderPartRepairPriceModel,
        )
        from ..models.qualer_api_models_service_orders_to_charge_response_model_base_order_task_price_model import (
            ServiceOrdersToChargeResponseModelBaseOrderTaskPriceModel,
        )
        from ..models.qualer_api_models_service_orders_to_charge_response_model_base_price_model import (
            ServiceOrdersToChargeResponseModelBasePriceModel,
        )

        d = dict(src_dict)
        charges = []
        _charges = d.pop("Charges", None)
        for charges_item_data in _charges or []:
            charges_item = ServiceOrdersToChargeResponseModelBasePriceModel.from_dict(
                charges_item_data
            )

            charges.append(charges_item)

        tasks = []
        _tasks = d.pop("Tasks", None)
        for tasks_item_data in _tasks or []:
            tasks_item = ServiceOrdersToChargeResponseModelBaseOrderTaskPriceModel.from_dict(
                tasks_item_data
            )

            tasks.append(tasks_item)

        parts = []
        _parts = d.pop("Parts", None)
        for parts_item_data in _parts or []:
            parts_item = ServiceOrdersToChargeResponseModelBaseOrderPartRepairPriceModel.from_dict(
                parts_item_data
            )

            parts.append(parts_item)

        repairs = []
        _repairs = d.pop("Repairs", None)
        for repairs_item_data in _repairs or []:
            repairs_item = (
                ServiceOrdersToChargeResponseModelBaseOrderPartRepairPriceModel.from_dict(
                    repairs_item_data
                )
            )

            repairs.append(repairs_item)

        work_items = []
        _work_items = d.pop("WorkItems", None)
        for work_items_item_data in _work_items or []:
            work_items_item = ServiceOrdersToBaseWorkItemModel.from_dict(work_items_item_data)

            work_items.append(work_items_item)

        qualer_web_mvc_areas_api_models_service_orders_to_charge_response_model = cls(
            charges=charges,
            tasks=tasks,
            parts=parts,
            repairs=repairs,
            work_items=work_items,
        )

        qualer_web_mvc_areas_api_models_service_orders_to_charge_response_model.additional_properties = (
            d
        )
        return qualer_web_mvc_areas_api_models_service_orders_to_charge_response_model

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
