import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel",
)


@_attrs_define
class QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel:
    """
    Attributes:
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        charge_date (Union[Unset, datetime.datetime]):
        price (Union[Unset, float]):
        unit_name (Union[Unset, str]):
        is_hourly_pricing (Union[Unset, bool]):
        time_spent_in_minutes (Union[Unset, float]):
        quantity (Union[Unset, float]):
        discount (Union[Unset, float]):
        is_taxable (Union[Unset, bool]):
        delivery_charge (Union[Unset, float]):
        free_quantity (Union[Unset, int]):
        created_by_id (Union[Unset, int]):
        service_order_charge_type (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    charge_date: Union[Unset, datetime.datetime] = UNSET
    price: Union[Unset, float] = UNSET
    unit_name: Union[Unset, str] = UNSET
    is_hourly_pricing: Union[Unset, bool] = UNSET
    time_spent_in_minutes: Union[Unset, float] = UNSET
    quantity: Union[Unset, float] = UNSET
    discount: Union[Unset, float] = UNSET
    is_taxable: Union[Unset, bool] = UNSET
    delivery_charge: Union[Unset, float] = UNSET
    free_quantity: Union[Unset, int] = UNSET
    created_by_id: Union[Unset, int] = UNSET
    service_order_charge_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        charge_date: Union[Unset, str] = UNSET
        if self.charge_date and not isinstance(self.charge_date, Unset):
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if description is not UNSET:
            field_dict["Description"] = description
        if charge_date is not UNSET:
            field_dict["ChargeDate"] = charge_date
        if price is not UNSET:
            field_dict["Price"] = price
        if unit_name is not UNSET:
            field_dict["UnitName"] = unit_name
        if is_hourly_pricing is not UNSET:
            field_dict["IsHourlyPricing"] = is_hourly_pricing
        if time_spent_in_minutes is not UNSET:
            field_dict["TimeSpentInMinutes"] = time_spent_in_minutes
        if quantity is not UNSET:
            field_dict["Quantity"] = quantity
        if discount is not UNSET:
            field_dict["Discount"] = discount
        if is_taxable is not UNSET:
            field_dict["IsTaxable"] = is_taxable
        if delivery_charge is not UNSET:
            field_dict["DeliveryCharge"] = delivery_charge
        if free_quantity is not UNSET:
            field_dict["FreeQuantity"] = free_quantity
        if created_by_id is not UNSET:
            field_dict["CreatedById"] = created_by_id
        if service_order_charge_type is not UNSET:
            field_dict["ServiceOrderChargeType"] = service_order_charge_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("Name", UNSET)

        description = d.pop("Description", UNSET)

        _charge_date = d.pop("ChargeDate", UNSET)
        charge_date: Union[Unset, datetime.datetime]
        if isinstance(_charge_date, Unset):
            charge_date = UNSET
        else:
            charge_date = isoparse(_charge_date)

        price = d.pop("Price", UNSET)

        unit_name = d.pop("UnitName", UNSET)

        is_hourly_pricing = d.pop("IsHourlyPricing", UNSET)

        time_spent_in_minutes = d.pop("TimeSpentInMinutes", UNSET)

        quantity = d.pop("Quantity", UNSET)

        discount = d.pop("Discount", UNSET)

        is_taxable = d.pop("IsTaxable", UNSET)

        delivery_charge = d.pop("DeliveryCharge", UNSET)

        free_quantity = d.pop("FreeQuantity", UNSET)

        created_by_id = d.pop("CreatedById", UNSET)

        service_order_charge_type = d.pop("ServiceOrderChargeType", UNSET)

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
