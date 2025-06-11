import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsReportDatasetsToServiceOrderChargeResponse")


@_attrs_define
class QualerApiModelsReportDatasetsToServiceOrderChargeResponse:
    """
    Attributes:
        service_order_id (Union[Unset, int]):
        description (Union[Unset, str]):
        name (Union[Unset, str]):
        unit_name (Union[Unset, str]):
        quantity (Union[Unset, float]):
        discount (Union[Unset, float]):
        fixed_charge (Union[Unset, float]):
        price (Union[Unset, float]):
        subtotal (Union[Unset, float]):
        is_taxable (Union[Unset, bool]):
        time_spent_in_minutes (Union[Unset, float]):
        is_hourly_pricing (Union[Unset, bool]):
        created_by (Union[Unset, str]):
        charge_date (Union[Unset, datetime.datetime]):
    """

    service_order_id: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    unit_name: Union[Unset, str] = UNSET
    quantity: Union[Unset, float] = UNSET
    discount: Union[Unset, float] = UNSET
    fixed_charge: Union[Unset, float] = UNSET
    price: Union[Unset, float] = UNSET
    subtotal: Union[Unset, float] = UNSET
    is_taxable: Union[Unset, bool] = UNSET
    time_spent_in_minutes: Union[Unset, float] = UNSET
    is_hourly_pricing: Union[Unset, bool] = UNSET
    created_by: Union[Unset, str] = UNSET
    charge_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_order_id = self.service_order_id

        description = self.description

        name = self.name

        unit_name = self.unit_name

        quantity = self.quantity

        discount = self.discount

        fixed_charge = self.fixed_charge

        price = self.price

        subtotal = self.subtotal

        is_taxable = self.is_taxable

        time_spent_in_minutes = self.time_spent_in_minutes

        is_hourly_pricing = self.is_hourly_pricing

        created_by = self.created_by

        charge_date: Union[Unset, str] = UNSET
        if not isinstance(self.charge_date, Unset):
            charge_date = self.charge_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_id is not UNSET:
            field_dict["ServiceOrderId"] = service_order_id
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
        if fixed_charge is not UNSET:
            field_dict["FixedCharge"] = fixed_charge
        if price is not UNSET:
            field_dict["Price"] = price
        if subtotal is not UNSET:
            field_dict["Subtotal"] = subtotal
        if is_taxable is not UNSET:
            field_dict["IsTaxable"] = is_taxable
        if time_spent_in_minutes is not UNSET:
            field_dict["TimeSpentInMinutes"] = time_spent_in_minutes
        if is_hourly_pricing is not UNSET:
            field_dict["IsHourlyPricing"] = is_hourly_pricing
        if created_by is not UNSET:
            field_dict["CreatedBy"] = created_by
        if charge_date is not UNSET:
            field_dict["ChargeDate"] = charge_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_id = d.pop("ServiceOrderId", UNSET)

        description = d.pop("Description", UNSET)

        name = d.pop("Name", UNSET)

        unit_name = d.pop("UnitName", UNSET)

        quantity = d.pop("Quantity", UNSET)

        discount = d.pop("Discount", UNSET)

        fixed_charge = d.pop("FixedCharge", UNSET)

        price = d.pop("Price", UNSET)

        subtotal = d.pop("Subtotal", UNSET)

        is_taxable = d.pop("IsTaxable", UNSET)

        time_spent_in_minutes = d.pop("TimeSpentInMinutes", UNSET)

        is_hourly_pricing = d.pop("IsHourlyPricing", UNSET)

        created_by = d.pop("CreatedBy", UNSET)

        _charge_date = d.pop("ChargeDate", UNSET)
        charge_date: Union[Unset, datetime.datetime]
        if isinstance(_charge_date, Unset):
            charge_date = UNSET
        else:
            charge_date = isoparse(_charge_date)

        qualer_api_models_report_datasets_to_service_order_charge_response = cls(
            service_order_id=service_order_id,
            description=description,
            name=name,
            unit_name=unit_name,
            quantity=quantity,
            discount=discount,
            fixed_charge=fixed_charge,
            price=price,
            subtotal=subtotal,
            is_taxable=is_taxable,
            time_spent_in_minutes=time_spent_in_minutes,
            is_hourly_pricing=is_hourly_pricing,
            created_by=created_by,
            charge_date=charge_date,
        )

        qualer_api_models_report_datasets_to_service_order_charge_response.additional_properties = (
            d
        )
        return qualer_api_models_report_datasets_to_service_order_charge_response

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
