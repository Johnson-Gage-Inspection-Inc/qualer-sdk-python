from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QualerApiModelsServiceOrdersToBaseWorkItemModelOrderItemTaskPriceModel")


@_attrs_define
class QualerApiModelsServiceOrdersToBaseWorkItemModelOrderItemTaskPriceModel:
    """
    Attributes:
        contract_discount (Optional[float]):
        name (Optional[str]):
        price (Optional[float]):
    """

    contract_discount: Optional[float] = None
    name: Optional[str] = None
    price: Optional[float] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contract_discount = self.contract_discount

        name = self.name

        price = self.price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contract_discount is not None:
            field_dict["ContractDiscount"] = contract_discount
        if name is not None:
            field_dict["Name"] = name
        if price is not None:
            field_dict["Price"] = price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contract_discount = d.pop("ContractDiscount", None)

        name = d.pop("Name", None)

        price = d.pop("Price", None)

        qualer_api_models_service_orders_to_base_work_item_model_order_item_task_price_model = cls(
            contract_discount=contract_discount,
            name=name,
            price=price,
        )

        qualer_api_models_service_orders_to_base_work_item_model_order_item_task_price_model.additional_properties = (
            d
        )
        return qualer_api_models_service_orders_to_base_work_item_model_order_item_task_price_model

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
