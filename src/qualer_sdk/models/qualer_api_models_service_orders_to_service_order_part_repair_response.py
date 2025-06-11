import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsServiceOrdersToServiceOrderPartRepairResponse")


@_attrs_define
class QualerApiModelsServiceOrdersToServiceOrderPartRepairResponse:
    """
    Attributes:
        service_order_item_part_id (Union[Unset, int]):
        price (Union[Unset, float]):
        description (Union[Unset, str]):
        name (Union[Unset, str]):
        unit_name (Union[Unset, str]):
        quantity (Union[Unset, float]):
        discount (Union[Unset, float]):
        delivery_charge (Union[Unset, float]):
        is_taxable (Union[Unset, bool]):
        time_spent_in_minutes (Union[Unset, float]):
        is_hourly_pricing (Union[Unset, bool]):
        free_quantity (Union[Unset, int]):
        currency_iso_symbol (Union[Unset, str]):
        created_by_id (Union[Unset, int]):
        created_by (Union[Unset, str]):
        created_on_utc (Union[Unset, datetime.datetime]):
        charge_date (Union[Unset, datetime.datetime]):
        contract_repairs_discount (Union[Unset, float]):
        contract_parts_discount (Union[Unset, float]):
        service_order_charge_type (Union[Unset, str]):
        total_discount (Union[Unset, float]):
        total_price (Union[Unset, float]):
        discount_price (Union[Unset, float]):
    """

    service_order_item_part_id: Union[Unset, int] = UNSET
    price: Union[Unset, float] = UNSET
    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    unit_name: Union[Unset, str] = UNSET
    quantity: Union[Unset, float] = UNSET
    discount: Union[Unset, float] = UNSET
    delivery_charge: Union[Unset, float] = UNSET
    is_taxable: Union[Unset, bool] = UNSET
    time_spent_in_minutes: Union[Unset, float] = UNSET
    is_hourly_pricing: Union[Unset, bool] = UNSET
    free_quantity: Union[Unset, int] = UNSET
    currency_iso_symbol: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, int] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_on_utc: Union[Unset, datetime.datetime] = UNSET
    charge_date: Union[Unset, datetime.datetime] = UNSET
    contract_repairs_discount: Union[Unset, float] = UNSET
    contract_parts_discount: Union[Unset, float] = UNSET
    service_order_charge_type: Union[Unset, str] = UNSET
    total_discount: Union[Unset, float] = UNSET
    total_price: Union[Unset, float] = UNSET
    discount_price: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        created_on_utc: Union[Unset, str] = UNSET
        if not isinstance(self.created_on_utc, Unset):
            created_on_utc = self.created_on_utc.isoformat()

        charge_date: Union[Unset, str] = UNSET
        if not isinstance(self.charge_date, Unset):
            charge_date = self.charge_date.isoformat()

        contract_repairs_discount = self.contract_repairs_discount

        contract_parts_discount = self.contract_parts_discount

        service_order_charge_type = self.service_order_charge_type

        total_discount = self.total_discount

        total_price = self.total_price

        discount_price = self.discount_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_item_part_id is not UNSET:
            field_dict["ServiceOrderItemPartId"] = service_order_item_part_id
        if price is not UNSET:
            field_dict["Price"] = price
        if description is not UNSET:
            field_dict["Description"] = description
        if name is not UNSET:
            field_dict["Name"] = name
        if unit_name is not UNSET:
            field_dict["UnitName"] = unit_name
        if quantity is not UNSET:
            field_dict["Quantity"] = quantity
        if discount is not UNSET:
            field_dict["Discount"] = discount
        if delivery_charge is not UNSET:
            field_dict["DeliveryCharge"] = delivery_charge
        if is_taxable is not UNSET:
            field_dict["IsTaxable"] = is_taxable
        if time_spent_in_minutes is not UNSET:
            field_dict["TimeSpentInMinutes"] = time_spent_in_minutes
        if is_hourly_pricing is not UNSET:
            field_dict["IsHourlyPricing"] = is_hourly_pricing
        if free_quantity is not UNSET:
            field_dict["FreeQuantity"] = free_quantity
        if currency_iso_symbol is not UNSET:
            field_dict["CurrencyIsoSymbol"] = currency_iso_symbol
        if created_by_id is not UNSET:
            field_dict["CreatedById"] = created_by_id
        if created_by is not UNSET:
            field_dict["CreatedBy"] = created_by
        if created_on_utc is not UNSET:
            field_dict["CreatedOnUtc"] = created_on_utc
        if charge_date is not UNSET:
            field_dict["ChargeDate"] = charge_date
        if contract_repairs_discount is not UNSET:
            field_dict["ContractRepairsDiscount"] = contract_repairs_discount
        if contract_parts_discount is not UNSET:
            field_dict["ContractPartsDiscount"] = contract_parts_discount
        if service_order_charge_type is not UNSET:
            field_dict["ServiceOrderChargeType"] = service_order_charge_type
        if total_discount is not UNSET:
            field_dict["TotalDiscount"] = total_discount
        if total_price is not UNSET:
            field_dict["TotalPrice"] = total_price
        if discount_price is not UNSET:
            field_dict["DiscountPrice"] = discount_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_item_part_id = d.pop("ServiceOrderItemPartId", UNSET)

        price = d.pop("Price", UNSET)

        description = d.pop("Description", UNSET)

        name = d.pop("Name", UNSET)

        unit_name = d.pop("UnitName", UNSET)

        quantity = d.pop("Quantity", UNSET)

        discount = d.pop("Discount", UNSET)

        delivery_charge = d.pop("DeliveryCharge", UNSET)

        is_taxable = d.pop("IsTaxable", UNSET)

        time_spent_in_minutes = d.pop("TimeSpentInMinutes", UNSET)

        is_hourly_pricing = d.pop("IsHourlyPricing", UNSET)

        free_quantity = d.pop("FreeQuantity", UNSET)

        currency_iso_symbol = d.pop("CurrencyIsoSymbol", UNSET)

        created_by_id = d.pop("CreatedById", UNSET)

        created_by = d.pop("CreatedBy", UNSET)

        _created_on_utc = d.pop("CreatedOnUtc", UNSET)
        created_on_utc: Union[Unset, datetime.datetime]
        if isinstance(_created_on_utc, Unset):
            created_on_utc = UNSET
        else:
            created_on_utc = isoparse(_created_on_utc)

        _charge_date = d.pop("ChargeDate", UNSET)
        charge_date: Union[Unset, datetime.datetime]
        if isinstance(_charge_date, Unset):
            charge_date = UNSET
        else:
            charge_date = isoparse(_charge_date)

        contract_repairs_discount = d.pop("ContractRepairsDiscount", UNSET)

        contract_parts_discount = d.pop("ContractPartsDiscount", UNSET)

        service_order_charge_type = d.pop("ServiceOrderChargeType", UNSET)

        total_discount = d.pop("TotalDiscount", UNSET)

        total_price = d.pop("TotalPrice", UNSET)

        discount_price = d.pop("DiscountPrice", UNSET)

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
