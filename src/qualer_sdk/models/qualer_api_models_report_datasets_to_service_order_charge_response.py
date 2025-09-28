import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ReportDatasetsToServiceOrderChargeResponse")


@_attrs_define
class ReportDatasetsToServiceOrderChargeResponse:
    """
    Attributes:
        service_order_id (Optional[int]):
        description (Optional[str]):
        name (Optional[str]):
        unit_name (Optional[str]):
        quantity (Optional[float]):
        discount (Optional[float]):
        fixed_charge (Optional[float]):
        price (Optional[float]):
        subtotal (Optional[float]):
        is_taxable (Optional[bool]):
        time_spent_in_minutes (Optional[float]):
        is_hourly_pricing (Optional[bool]):
        created_by (Optional[str]):
        charge_date (Optional[datetime.datetime]):
    """

    service_order_id: Optional[int] = None
    description: Optional[str] = None
    name: Optional[str] = None
    unit_name: Optional[str] = None
    quantity: Optional[float] = None
    discount: Optional[float] = None
    fixed_charge: Optional[float] = None
    price: Optional[float] = None
    subtotal: Optional[float] = None
    is_taxable: Optional[bool] = None
    time_spent_in_minutes: Optional[float] = None
    is_hourly_pricing: Optional[bool] = None
    created_by: Optional[str] = None
    charge_date: Optional[datetime.datetime] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
        charge_date = self.charge_date.isoformat() if self.charge_date else None
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_id is not None:
            field_dict["ServiceOrderId"] = service_order_id
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
        if fixed_charge is not None:
            field_dict["FixedCharge"] = fixed_charge
        if price is not None:
            field_dict["Price"] = price
        if subtotal is not None:
            field_dict["Subtotal"] = subtotal
        if is_taxable is not None:
            field_dict["IsTaxable"] = is_taxable
        if time_spent_in_minutes is not None:
            field_dict["TimeSpentInMinutes"] = time_spent_in_minutes
        if is_hourly_pricing is not None:
            field_dict["IsHourlyPricing"] = is_hourly_pricing
        if created_by is not None:
            field_dict["CreatedBy"] = created_by
        if charge_date is not None:
            field_dict["ChargeDate"] = charge_date
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_id = d.pop("ServiceOrderId", None)
        description = d.pop("Description", None)
        name = d.pop("Name", None)
        unit_name = d.pop("UnitName", None)
        quantity = d.pop("Quantity", None)
        discount = d.pop("Discount", None)
        fixed_charge = d.pop("FixedCharge", None)
        price = d.pop("Price", None)
        subtotal = d.pop("Subtotal", None)
        is_taxable = d.pop("IsTaxable", None)
        time_spent_in_minutes = d.pop("TimeSpentInMinutes", None)
        is_hourly_pricing = d.pop("IsHourlyPricing", None)
        created_by = d.pop("CreatedBy", None)

        def _parse_charge_date(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                charge_date_type_0 = isoparse(data)
                return charge_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        charge_date = _parse_charge_date(d.pop("ChargeDate", None))
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
        qualer_api_models_report_datasets_to_service_order_charge_response.additional_properties = d
        return qualer_api_models_report_datasets_to_service_order_charge_response

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
