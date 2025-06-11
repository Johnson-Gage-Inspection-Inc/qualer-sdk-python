from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualer_api_models_service_orders_to_base_work_item_model import (
        QualerApiModelsServiceOrdersToBaseWorkItemModel,
    )
    from ..models.qualer_api_models_service_orders_to_charge_response_model_base_order_part_repair_price_model import (
        QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderPartRepairPriceModel,
    )
    from ..models.qualer_api_models_service_orders_to_charge_response_model_base_order_task_price_model import (
        QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderTaskPriceModel,
    )
    from ..models.qualer_api_models_service_orders_to_charge_response_model_base_price_model import (
        QualerApiModelsServiceOrdersToChargeResponseModelBasePriceModel,
    )


T = TypeVar("T", bound="QualerWebMvcAreasApiModelsServiceOrdersToChargeResponseModel")


@_attrs_define
class QualerWebMvcAreasApiModelsServiceOrdersToChargeResponseModel:
    """
    Attributes:
        charges (Union[Unset, list['QualerApiModelsServiceOrdersToChargeResponseModelBasePriceModel']]):
        tasks (Union[Unset, list['QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderTaskPriceModel']]):
        parts (Union[Unset, list['QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderPartRepairPriceModel']]):
        repairs (Union[Unset, list['QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderPartRepairPriceModel']]):
        work_items (Union[Unset, list['QualerApiModelsServiceOrdersToBaseWorkItemModel']]):
    """

    charges: Union[
        Unset, list["QualerApiModelsServiceOrdersToChargeResponseModelBasePriceModel"]
    ] = UNSET
    tasks: Union[
        Unset,
        list[
            "QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderTaskPriceModel"
        ],
    ] = UNSET
    parts: Union[
        Unset,
        list[
            "QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderPartRepairPriceModel"
        ],
    ] = UNSET
    repairs: Union[
        Unset,
        list[
            "QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderPartRepairPriceModel"
        ],
    ] = UNSET
    work_items: Union[
        Unset, list["QualerApiModelsServiceOrdersToBaseWorkItemModel"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charges: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.charges, Unset):
            charges = []
            for charges_item_data in self.charges:
                charges_item = charges_item_data.to_dict()
                charges.append(charges_item)

        tasks: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tasks, Unset):
            tasks = []
            for tasks_item_data in self.tasks:
                tasks_item = tasks_item_data.to_dict()
                tasks.append(tasks_item)

        parts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.parts, Unset):
            parts = []
            for parts_item_data in self.parts:
                parts_item = parts_item_data.to_dict()
                parts.append(parts_item)

        repairs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.repairs, Unset):
            repairs = []
            for repairs_item_data in self.repairs:
                repairs_item = repairs_item_data.to_dict()
                repairs.append(repairs_item)

        work_items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.work_items, Unset):
            work_items = []
            for work_items_item_data in self.work_items:
                work_items_item = work_items_item_data.to_dict()
                work_items.append(work_items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if charges is not UNSET:
            field_dict["Charges"] = charges
        if tasks is not UNSET:
            field_dict["Tasks"] = tasks
        if parts is not UNSET:
            field_dict["Parts"] = parts
        if repairs is not UNSET:
            field_dict["Repairs"] = repairs
        if work_items is not UNSET:
            field_dict["WorkItems"] = work_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_service_orders_to_base_work_item_model import (
            QualerApiModelsServiceOrdersToBaseWorkItemModel,
        )
        from ..models.qualer_api_models_service_orders_to_charge_response_model_base_order_part_repair_price_model import (
            QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderPartRepairPriceModel,
        )
        from ..models.qualer_api_models_service_orders_to_charge_response_model_base_order_task_price_model import (
            QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderTaskPriceModel,
        )
        from ..models.qualer_api_models_service_orders_to_charge_response_model_base_price_model import (
            QualerApiModelsServiceOrdersToChargeResponseModelBasePriceModel,
        )

        d = dict(src_dict)
        charges = []
        _charges = d.pop("Charges", UNSET)
        for charges_item_data in _charges or []:
            charges_item = QualerApiModelsServiceOrdersToChargeResponseModelBasePriceModel.from_dict(
                charges_item_data
            )

            charges.append(charges_item)

        tasks = []
        _tasks = d.pop("Tasks", UNSET)
        for tasks_item_data in _tasks or []:
            tasks_item = QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderTaskPriceModel.from_dict(
                tasks_item_data
            )

            tasks.append(tasks_item)

        parts = []
        _parts = d.pop("Parts", UNSET)
        for parts_item_data in _parts or []:
            parts_item = QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderPartRepairPriceModel.from_dict(
                parts_item_data
            )

            parts.append(parts_item)

        repairs = []
        _repairs = d.pop("Repairs", UNSET)
        for repairs_item_data in _repairs or []:
            repairs_item = QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderPartRepairPriceModel.from_dict(
                repairs_item_data
            )

            repairs.append(repairs_item)

        work_items = []
        _work_items = d.pop("WorkItems", UNSET)
        for work_items_item_data in _work_items or []:
            work_items_item = QualerApiModelsServiceOrdersToBaseWorkItemModel.from_dict(
                work_items_item_data
            )

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
