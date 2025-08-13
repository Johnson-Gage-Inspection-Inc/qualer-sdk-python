from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderPartRepairPriceModel",
)


@_attrs_define
class QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderPartRepairPriceModel:
    """
    Attributes:
        delivery_charge (Union[None, Unset, float]):
        quantity (Union[None, Unset, float]):
        time_spent_in_minutes (Union[None, Unset, float]):
        is_hourly_pricing (Union[None, Unset, bool]):
        description (Union[None, Unset, str]):
        name (Union[None, Unset, str]):
        price (Union[None, Unset, float]):
        is_taxable (Union[None, Unset, bool]):
    """

    delivery_charge: Union[None, Unset, float] = UNSET
    quantity: Union[None, Unset, float] = UNSET
    time_spent_in_minutes: Union[None, Unset, float] = UNSET
    is_hourly_pricing: Union[None, Unset, bool] = UNSET
    description: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    price: Union[None, Unset, float] = UNSET
    is_taxable: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delivery_charge = self.delivery_charge

        quantity = self.quantity

        time_spent_in_minutes = self.time_spent_in_minutes

        is_hourly_pricing = self.is_hourly_pricing

        description = self.description

        name = self.name

        price = self.price

        is_taxable = self.is_taxable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delivery_charge is not UNSET:
            field_dict["DeliveryCharge"] = delivery_charge
        if quantity is not UNSET:
            field_dict["Quantity"] = quantity
        if time_spent_in_minutes is not UNSET:
            field_dict["TimeSpentInMinutes"] = time_spent_in_minutes
        if is_hourly_pricing is not UNSET:
            field_dict["IsHourlyPricing"] = is_hourly_pricing
        if description is not UNSET:
            field_dict["Description"] = description
        if name is not UNSET:
            field_dict["Name"] = name
        if price is not UNSET:
            field_dict["Price"] = price
        if is_taxable is not UNSET:
            field_dict["IsTaxable"] = is_taxable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delivery_charge = d.pop("DeliveryCharge", UNSET)

        quantity = d.pop("Quantity", UNSET)

        time_spent_in_minutes = d.pop("TimeSpentInMinutes", UNSET)

        is_hourly_pricing = d.pop("IsHourlyPricing", UNSET)

        description = d.pop("Description", UNSET)

        name = d.pop("Name", UNSET)

        price = d.pop("Price", UNSET)

        is_taxable = d.pop("IsTaxable", UNSET)

        qualer_api_models_service_orders_to_charge_response_model_base_order_part_repair_price_model = cls(
            delivery_charge=delivery_charge,
            quantity=quantity,
            time_spent_in_minutes=time_spent_in_minutes,
            is_hourly_pricing=is_hourly_pricing,
            description=description,
            name=name,
            price=price,
            is_taxable=is_taxable,
        )

        qualer_api_models_service_orders_to_charge_response_model_base_order_part_repair_price_model.additional_properties = (
            d
        )
        return qualer_api_models_service_orders_to_charge_response_model_base_order_part_repair_price_model

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
