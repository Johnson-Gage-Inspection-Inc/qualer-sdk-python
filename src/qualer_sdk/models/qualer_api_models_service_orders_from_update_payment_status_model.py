import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ServiceOrdersFromUpdatePaymentStatusModel")


@_attrs_define
class ServiceOrdersFromUpdatePaymentStatusModel:
    """
    Attributes:
        payment_status (Optional[str]):
        invoiced_on (Optional[datetime.datetime]):
    """

    payment_status: Optional[str] = None
    invoiced_on: Optional[datetime.datetime] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payment_status = self.payment_status
        invoiced_on = self.invoiced_on.isoformat() if self.invoiced_on else None
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payment_status is not None:
            field_dict["PaymentStatus"] = payment_status
        if invoiced_on is not None:
            field_dict["InvoicedOn"] = invoiced_on
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        payment_status = d.pop("PaymentStatus", None)
        def _parse_invoiced_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                invoiced_on_type_0 = isoparse(data)
                return invoiced_on_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)
        invoiced_on = _parse_invoiced_on(d.pop("InvoicedOn", None))
        qualer_api_models_service_orders_from_update_payment_status_model = cls(
            payment_status=payment_status,
            invoiced_on=invoiced_on,
        )
        qualer_api_models_service_orders_from_update_payment_status_model.additional_properties = d
        return qualer_api_models_service_orders_from_update_payment_status_model

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
