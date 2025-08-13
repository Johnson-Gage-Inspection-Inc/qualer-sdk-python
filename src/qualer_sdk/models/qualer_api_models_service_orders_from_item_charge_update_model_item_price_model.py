from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="QualerApiModelsServiceOrdersFromItemChargeUpdateModelItemPriceModel"
)


@_attrs_define
class QualerApiModelsServiceOrdersFromItemChargeUpdateModelItemPriceModel:
    """
    Attributes:
        name (Union[None, Unset, str]):
        price (Union[None, Unset, float]):
    """

    name: Union[None, Unset, str] = UNSET
    price: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        price = self.price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if price is not UNSET:
            field_dict["Price"] = price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("Name", UNSET)

        price = d.pop("Price", UNSET)

        qualer_api_models_service_orders_from_item_charge_update_model_item_price_model = cls(
            name=name,
            price=price,
        )

        qualer_api_models_service_orders_from_item_charge_update_model_item_price_model.additional_properties = (
            d
        )
        return qualer_api_models_service_orders_from_item_charge_update_model_item_price_model

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
