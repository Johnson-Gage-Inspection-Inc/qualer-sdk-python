import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="QualerApiModelsServiceOrdersToServiceOrderPartRepairResponse")


@_attrs_define
class QualerApiModelsServiceOrdersToServiceOrderPartRepairResponse:
    """
    Attributes:
        service_order_item_part_id (Optional[int]):
        price (Optional[float]):
        description (Optional[str]):
        name (Optional[str]):
        unit_name (Optional[str]):
        quantity (Optional[float]):
        discount (Optional[float]):
        delivery_charge (Optional[float]):
        is_taxable (Optional[bool]):
        time_spent_in_minutes (Optional[float]):
        is_hourly_pricing (Optional[bool]):
        free_quantity (Optional[int]):
        currency_iso_symbol (Optional[str]):
        created_by_id (Optional[int]):
        created_by (Optional[str]):
        created_on_utc (Optional[datetime.datetime]):
        charge_date (Optional[datetime.datetime]):
        contract_repairs_discount (Optional[float]):
        contract_parts_discount (Optional[float]):
        service_order_charge_type (Optional[str]):
        total_discount (Optional[float]):
        total_price (Optional[float]):
        discount_price (Optional[float]):
    """

    service_order_item_part_id: Optional[int] = None
    price: Optional[float] = None
    description: Optional[str] = None
    name: Optional[str] = None
    unit_name: Optional[str] = None
    quantity: Optional[float] = None
    discount: Optional[float] = None
    delivery_charge: Optional[float] = None
    is_taxable: Optional[bool] = None
    time_spent_in_minutes: Optional[float] = None
    is_hourly_pricing: Optional[bool] = None
    free_quantity: Optional[int] = None
    currency_iso_symbol: Optional[str] = None
    created_by_id: Optional[int] = None
    created_by: Optional[str] = None
    created_on_utc: Optional[datetime.datetime] = None
    charge_date: Optional[datetime.datetime] = None
    contract_repairs_discount: Optional[float] = None
    contract_parts_discount: Optional[float] = None
    service_order_charge_type: Optional[str] = None
    total_discount: Optional[float] = None
    total_price: Optional[float] = None
    discount_price: Optional[float] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_order_item_part_id = self.service_order_item_part_id

        price = self.price

        description = self.description

        name = self.name

        unit_name = self.unit_name

        quantity = self.quantity

        discount = self.discount

        delivery_charge = self.delivery_charge

        is_taxable = self.is_taxable

        time_spent_in_minutes = self.time_spent_in_minutes

        is_hourly_pricing = self.is_hourly_pricing

        free_quantity = self.free_quantity

        currency_iso_symbol = self.currency_iso_symbol

        created_by_id = self.created_by_id

        created_by = self.created_by

        created_on_utc: Optional[str] = None
        if self.created_on_utc:
            created_on_utc = self.created_on_utc.isoformat()

        charge_date: Optional[str] = None
        if self.charge_date:
            charge_date = self.charge_date.isoformat()

        contract_repairs_discount = self.contract_repairs_discount

        contract_parts_discount = self.contract_parts_discount

        service_order_charge_type = self.service_order_charge_type

        total_discount = self.total_discount

        total_price = self.total_price

        discount_price = self.discount_price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_item_part_id is not None:
            field_dict["ServiceOrderItemPartId"] = service_order_item_part_id
        if price is not None:
            field_dict["Price"] = price
        if description is not None:
            field_dict["Description"] = description
        if name is not None:
            field_dict["Name"] = name
        if unit_name is not None:
            field_dict["UnitName"] = unit_name
        if quantity is not None:
            field_dict["Quantity"] = quantity
        if discount is not None:
            field_dict["Discount"] = discount
        if delivery_charge is not None:
            field_dict["DeliveryCharge"] = delivery_charge
        if is_taxable is not None:
            field_dict["IsTaxable"] = is_taxable
        if time_spent_in_minutes is not None:
            field_dict["TimeSpentInMinutes"] = time_spent_in_minutes
        if is_hourly_pricing is not None:
            field_dict["IsHourlyPricing"] = is_hourly_pricing
        if free_quantity is not None:
            field_dict["FreeQuantity"] = free_quantity
        if currency_iso_symbol is not None:
            field_dict["CurrencyIsoSymbol"] = currency_iso_symbol
        if created_by_id is not None:
            field_dict["CreatedById"] = created_by_id
        if created_by is not None:
            field_dict["CreatedBy"] = created_by
        if created_on_utc is not None:
            field_dict["CreatedOnUtc"] = created_on_utc
        if charge_date is not None:
            field_dict["ChargeDate"] = charge_date
        if contract_repairs_discount is not None:
            field_dict["ContractRepairsDiscount"] = contract_repairs_discount
        if contract_parts_discount is not None:
            field_dict["ContractPartsDiscount"] = contract_parts_discount
        if service_order_charge_type is not None:
            field_dict["ServiceOrderChargeType"] = service_order_charge_type
        if total_discount is not None:
            field_dict["TotalDiscount"] = total_discount
        if total_price is not None:
            field_dict["TotalPrice"] = total_price
        if discount_price is not None:
            field_dict["DiscountPrice"] = discount_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_item_part_id = d.pop("ServiceOrderItemPartId", None)

        price = d.pop("Price", None)

        description = d.pop("Description", None)

        name = d.pop("Name", None)

        unit_name = d.pop("UnitName", None)

        quantity = d.pop("Quantity", None)

        discount = d.pop("Discount", None)

        delivery_charge = d.pop("DeliveryCharge", None)

        is_taxable = d.pop("IsTaxable", None)

        time_spent_in_minutes = d.pop("TimeSpentInMinutes", None)

        is_hourly_pricing = d.pop("IsHourlyPricing", None)

        free_quantity = d.pop("FreeQuantity", None)

        currency_iso_symbol = d.pop("CurrencyIsoSymbol", None)

        created_by_id = d.pop("CreatedById", None)

        created_by = d.pop("CreatedBy", None)

        _created_on_utc = d.pop("CreatedOnUtc", None)
        created_on_utc: Optional[datetime.datetime]
        if not _created_on_utc:
            created_on_utc = None
        else:
            created_on_utc = isoparse(_created_on_utc)

        _charge_date = d.pop("ChargeDate", None)
        charge_date: Optional[datetime.datetime]
        if not _charge_date:
            charge_date = None
        else:
            charge_date = isoparse(_charge_date)

        contract_repairs_discount = d.pop("ContractRepairsDiscount", None)

        contract_parts_discount = d.pop("ContractPartsDiscount", None)

        service_order_charge_type = d.pop("ServiceOrderChargeType", None)

        total_discount = d.pop("TotalDiscount", None)

        total_price = d.pop("TotalPrice", None)

        discount_price = d.pop("DiscountPrice", None)

        qualer_api_models_service_orders_to_service_order_part_repair_response = cls(
            service_order_item_part_id=service_order_item_part_id,
            price=price,
            description=description,
            name=name,
            unit_name=unit_name,
            quantity=quantity,
            discount=discount,
            delivery_charge=delivery_charge,
            is_taxable=is_taxable,
            time_spent_in_minutes=time_spent_in_minutes,
            is_hourly_pricing=is_hourly_pricing,
            free_quantity=free_quantity,
            currency_iso_symbol=currency_iso_symbol,
            created_by_id=created_by_id,
            created_by=created_by,
            created_on_utc=created_on_utc,
            charge_date=charge_date,
            contract_repairs_discount=contract_repairs_discount,
            contract_parts_discount=contract_parts_discount,
            service_order_charge_type=service_order_charge_type,
            total_discount=total_discount,
            total_price=total_price,
            discount_price=discount_price,
        )

        qualer_api_models_service_orders_to_service_order_part_repair_response.additional_properties = (
            d
        )
        return qualer_api_models_service_orders_to_service_order_part_repair_response

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
