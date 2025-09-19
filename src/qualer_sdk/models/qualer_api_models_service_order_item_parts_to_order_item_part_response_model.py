from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.qualer_api_models_service_order_item_parts_to_order_item_part_response_model_service_order_charge_type import (
    ServiceOrderItemPartsToOrderItemPartResponseModelServiceOrderChargeType,
)

T = TypeVar("T", bound="ServiceOrderItemPartsToOrderItemPartResponseModel")


@_attrs_define
class ServiceOrderItemPartsToOrderItemPartResponseModel:
    """
    Attributes:
        service_order_item_part_id (Optional[int]):
        service_order_item_id (Optional[int]):
        name (Optional[str]):
        description (Optional[str]):
        discount (Optional[float]):
        is_taxable (Optional[bool]):
        is_hourly_pricing (Optional[bool]):
        price (Optional[float]):
        unit_name (Optional[str]):
        quantity (Optional[float]):
        delivery_charge (Optional[float]):
        time_spent_in_minutes (Optional[float]):
        free_quantity (Optional[int]):
        service_order_charge_type (Optional[
            ServiceOrderItemPartsToOrderItemPartResponseModelServiceOrderChargeType]):
    """

    service_order_item_part_id: Optional[int] = None
    service_order_item_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    discount: Optional[float] = None
    is_taxable: Optional[bool] = None
    is_hourly_pricing: Optional[bool] = None
    price: Optional[float] = None
    unit_name: Optional[str] = None
    quantity: Optional[float] = None
    delivery_charge: Optional[float] = None
    time_spent_in_minutes: Optional[float] = None
    free_quantity: Optional[int] = None
    service_order_charge_type: Optional[
        ServiceOrderItemPartsToOrderItemPartResponseModelServiceOrderChargeType
    ] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_order_item_part_id = self.service_order_item_part_id

        service_order_item_id = self.service_order_item_id

        name = self.name

        description = self.description

        discount = self.discount

        is_taxable = self.is_taxable

        is_hourly_pricing = self.is_hourly_pricing

        price = self.price

        unit_name = self.unit_name

        quantity = self.quantity

        delivery_charge = self.delivery_charge

        time_spent_in_minutes = self.time_spent_in_minutes

        free_quantity = self.free_quantity

        service_order_charge_type: Optional[str] = None
        if self.service_order_charge_type:
            service_order_charge_type = self.service_order_charge_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_item_part_id is not None:
            field_dict["ServiceOrderItemPartId"] = service_order_item_part_id
        if service_order_item_id is not None:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if name is not None:
            field_dict["Name"] = name
        if description is not None:
            field_dict["Description"] = description
        if discount is not None:
            field_dict["Discount"] = discount
        if is_taxable is not None:
            field_dict["IsTaxable"] = is_taxable
        if is_hourly_pricing is not None:
            field_dict["IsHourlyPricing"] = is_hourly_pricing
        if price is not None:
            field_dict["Price"] = price
        if unit_name is not None:
            field_dict["UnitName"] = unit_name
        if quantity is not None:
            field_dict["Quantity"] = quantity
        if delivery_charge is not None:
            field_dict["DeliveryCharge"] = delivery_charge
        if time_spent_in_minutes is not None:
            field_dict["TimeSpentInMinutes"] = time_spent_in_minutes
        if free_quantity is not None:
            field_dict["FreeQuantity"] = free_quantity
        if service_order_charge_type is not None:
            field_dict["ServiceOrderChargeType"] = service_order_charge_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_item_part_id = d.pop("ServiceOrderItemPartId", None)

        service_order_item_id = d.pop("ServiceOrderItemId", None)

        name = d.pop("Name", None)

        description = d.pop("Description", None)

        discount = d.pop("Discount", None)

        is_taxable = d.pop("IsTaxable", None)

        is_hourly_pricing = d.pop("IsHourlyPricing", None)

        price = d.pop("Price", None)

        unit_name = d.pop("UnitName", None)

        quantity = d.pop("Quantity", None)

        delivery_charge = d.pop("DeliveryCharge", None)

        time_spent_in_minutes = d.pop("TimeSpentInMinutes", None)

        free_quantity = d.pop("FreeQuantity", None)

        _service_order_charge_type = d.pop("ServiceOrderChargeType", None)
        service_order_charge_type: Optional[
            ServiceOrderItemPartsToOrderItemPartResponseModelServiceOrderChargeType
        ]
        if not _service_order_charge_type:
            service_order_charge_type = None
        else:
            service_order_charge_type = (
                ServiceOrderItemPartsToOrderItemPartResponseModelServiceOrderChargeType(
                    _service_order_charge_type
                )
            )

        qualer_api_models_service_order_item_parts_to_order_item_part_response_model = cls(
            service_order_item_part_id=service_order_item_part_id,
            service_order_item_id=service_order_item_id,
            name=name,
            description=description,
            discount=discount,
            is_taxable=is_taxable,
            is_hourly_pricing=is_hourly_pricing,
            price=price,
            unit_name=unit_name,
            quantity=quantity,
            delivery_charge=delivery_charge,
            time_spent_in_minutes=time_spent_in_minutes,
            free_quantity=free_quantity,
            service_order_charge_type=service_order_charge_type,
        )

        qualer_api_models_service_order_item_parts_to_order_item_part_response_model.additional_properties = (
            d
        )
        return qualer_api_models_service_order_item_parts_to_order_item_part_response_model

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
