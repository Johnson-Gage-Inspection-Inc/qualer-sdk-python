from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="QualerApiModelsServiceOrdersToBaseWorkItemModelOrderItemTaskPriceModel"
)


@_attrs_define
class QualerApiModelsServiceOrdersToBaseWorkItemModelOrderItemTaskPriceModel:
    """
    Attributes:
        contract_discount (Union[Unset, float]):
        name (Union[Unset, str]):
        price (Union[Unset, float]):
    """

    contract_discount: Union[Unset, float] = UNSET
    name: Union[Unset, str] = UNSET
    price: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contract_discount = self.contract_discount

        name = self.name

        price = self.price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contract_discount is not UNSET:
            field_dict["ContractDiscount"] = contract_discount
        if name is not UNSET:
            field_dict["Name"] = name
        if price is not UNSET:
            field_dict["Price"] = price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contract_discount = d.pop("ContractDiscount", UNSET)

        name = d.pop("Name", UNSET)

        price = d.pop("Price", UNSET)

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
