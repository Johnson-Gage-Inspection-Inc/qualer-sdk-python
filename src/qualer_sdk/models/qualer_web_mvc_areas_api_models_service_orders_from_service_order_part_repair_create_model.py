import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar(
    "T",
    bound="QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel",
)


@_attrs_define
class QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel:
    """
    Attributes:
        name (Optional[str]):
        description (Optional[str]):
        charge_date (Optional[datetime.datetime]):
        price (Optional[float]):
        unit_name (Optional[str]):
        is_hourly_pricing (Optional[bool]):
        time_spent_in_minutes (Optional[float]):
        quantity (Optional[float]):
        discount (Optional[float]):
        is_taxable (Optional[bool]):
        delivery_charge (Optional[float]):
        free_quantity (Optional[int]):
        created_by_id (Optional[int]):
        service_order_charge_type (Optional[str]):
    """

    name: Optional[str] = None
    description: Optional[str] = None
    charge_date: Optional[datetime.datetime] = None
    price: Optional[float] = None
    unit_name: Optional[str] = None
    is_hourly_pricing: Optional[bool] = None
    time_spent_in_minutes: Optional[float] = None
    quantity: Optional[float] = None
    discount: Optional[float] = None
    is_taxable: Optional[bool] = None
    delivery_charge: Optional[float] = None
    free_quantity: Optional[int] = None
    created_by_id: Optional[int] = None
    service_order_charge_type: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        charge_date: Optional[str] = None
        if self.charge_date:
            charge_date = self.charge_date.isoformat()
        price = self.price
        unit_name = self.unit_name
        is_hourly_pricing = self.is_hourly_pricing
        time_spent_in_minutes = self.time_spent_in_minutes
        quantity = self.quantity
        discount = self.discount
        is_taxable = self.is_taxable
        delivery_charge = self.delivery_charge
        free_quantity = self.free_quantity
        created_by_id = self.created_by_id
        service_order_charge_type = self.service_order_charge_type
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not None:
            field_dict["Name"] = name
        if description is not None:
            field_dict["Description"] = description
        if charge_date is not None:
            field_dict["ChargeDate"] = charge_date
        if price is not None:
            field_dict["Price"] = price
        if unit_name is not None:
            field_dict["UnitName"] = unit_name
        if is_hourly_pricing is not None:
            field_dict["IsHourlyPricing"] = is_hourly_pricing
        if time_spent_in_minutes is not None:
            field_dict["TimeSpentInMinutes"] = time_spent_in_minutes
        if quantity is not None:
            field_dict["Quantity"] = quantity
        if discount is not None:
            field_dict["Discount"] = discount
        if is_taxable is not None:
            field_dict["IsTaxable"] = is_taxable
        if delivery_charge is not None:
            field_dict["DeliveryCharge"] = delivery_charge
        if free_quantity is not None:
            field_dict["FreeQuantity"] = free_quantity
        if created_by_id is not None:
            field_dict["CreatedById"] = created_by_id
        if service_order_charge_type is not None:
            field_dict["ServiceOrderChargeType"] = service_order_charge_type
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("Name", None)
        description = d.pop("Description", None)
        _charge_date = d.pop("ChargeDate", None)
        charge_date: Optional[datetime.datetime]
        if not _charge_date:
            charge_date = None
        else:
            charge_date = isoparse(_charge_date)
        price = d.pop("Price", None)
        unit_name = d.pop("UnitName", None)
        is_hourly_pricing = d.pop("IsHourlyPricing", None)
        time_spent_in_minutes = d.pop("TimeSpentInMinutes", None)
        quantity = d.pop("Quantity", None)
        discount = d.pop("Discount", None)
        is_taxable = d.pop("IsTaxable", None)
        delivery_charge = d.pop("DeliveryCharge", None)
        free_quantity = d.pop("FreeQuantity", None)
        created_by_id = d.pop("CreatedById", None)
        service_order_charge_type = d.pop("ServiceOrderChargeType", None)
        qualer_web_mvc_areas_api_models_service_orders_from_service_order_part_repair_create_model = cls(
            name=name,
            description=description,
            charge_date=charge_date,
            price=price,
            unit_name=unit_name,
            is_hourly_pricing=is_hourly_pricing,
            time_spent_in_minutes=time_spent_in_minutes,
            quantity=quantity,
            discount=discount,
            is_taxable=is_taxable,
            delivery_charge=delivery_charge,
            free_quantity=free_quantity,
            created_by_id=created_by_id,
            service_order_charge_type=service_order_charge_type,
        )
        qualer_web_mvc_areas_api_models_service_orders_from_service_order_part_repair_create_model.additional_properties = (
            d
        )
        return qualer_web_mvc_areas_api_models_service_orders_from_service_order_part_repair_create_model

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
