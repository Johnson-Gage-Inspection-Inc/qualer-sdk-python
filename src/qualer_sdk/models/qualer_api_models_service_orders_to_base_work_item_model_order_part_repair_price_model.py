from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T",
    bound="ServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel",
)


@_attrs_define
class ServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel:
    """
    Attributes:
        delivery_charge (Optional[float]):
        quantity (Optional[float]):
        time_spent_in_minutes (Optional[float]):
        is_hourly_pricing (Optional[bool]):
        description (Optional[str]):
        name (Optional[str]):
        price (Optional[float]):
        unit_name (Optional[str]):
        is_taxable (Optional[bool]):
    """

    delivery_charge: Optional[float] = None
    quantity: Optional[float] = None
    time_spent_in_minutes: Optional[float] = None
    is_hourly_pricing: Optional[bool] = None
    description: Optional[str] = None
    name: Optional[str] = None
    price: Optional[float] = None
    unit_name: Optional[str] = None
    is_taxable: Optional[bool] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        delivery_charge = self.delivery_charge
        quantity = self.quantity
        time_spent_in_minutes = self.time_spent_in_minutes
        is_hourly_pricing = self.is_hourly_pricing
        description = self.description
        name = self.name
        price = self.price
        unit_name = self.unit_name
        is_taxable = self.is_taxable
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delivery_charge is not None:
            field_dict["DeliveryCharge"] = delivery_charge
        if quantity is not None:
            field_dict["Quantity"] = quantity
        if time_spent_in_minutes is not None:
            field_dict["TimeSpentInMinutes"] = time_spent_in_minutes
        if is_hourly_pricing is not None:
            field_dict["IsHourlyPricing"] = is_hourly_pricing
        if description is not None:
            field_dict["Description"] = description
        if name is not None:
            field_dict["Name"] = name
        if price is not None:
            field_dict["Price"] = price
        if unit_name is not None:
            field_dict["UnitName"] = unit_name
        if is_taxable is not None:
            field_dict["IsTaxable"] = is_taxable
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delivery_charge = d.pop("DeliveryCharge", None)
        quantity = d.pop("Quantity", None)
        time_spent_in_minutes = d.pop("TimeSpentInMinutes", None)
        is_hourly_pricing = d.pop("IsHourlyPricing", None)
        description = d.pop("Description", None)
        name = d.pop("Name", None)
        price = d.pop("Price", None)
        unit_name = d.pop("UnitName", None)
        is_taxable = d.pop("IsTaxable", None)
        qualer_api_models_service_orders_to_base_work_item_model_order_part_repair_price_model = (
            cls(
                delivery_charge=delivery_charge,
                quantity=quantity,
                time_spent_in_minutes=time_spent_in_minutes,
                is_hourly_pricing=is_hourly_pricing,
                description=description,
                name=name,
                price=price,
                unit_name=unit_name,
                is_taxable=is_taxable,
            )
        )
        qualer_api_models_service_orders_to_base_work_item_model_order_part_repair_price_model.additional_properties = (
            d
        )
        return (
            qualer_api_models_service_orders_to_base_work_item_model_order_part_repair_price_model
        )

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
