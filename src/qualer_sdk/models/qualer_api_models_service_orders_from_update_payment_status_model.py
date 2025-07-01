import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsServiceOrdersFromUpdatePaymentStatusModel")


@_attrs_define
class QualerApiModelsServiceOrdersFromUpdatePaymentStatusModel:
    """
    Attributes:
        payment_status (Union[Unset, str]):
        invoiced_on (Union[None, Unset, datetime.datetime]):
    """

    payment_status: Union[Unset, str] = UNSET
    invoiced_on: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payment_status = self.payment_status

        invoiced_on: Union[None, Unset, str]
        if isinstance(self.invoiced_on, Unset):
            invoiced_on = UNSET
        elif isinstance(self.invoiced_on, datetime.datetime):
            invoiced_on = self.invoiced_on.isoformat()
        else:
            invoiced_on = self.invoiced_on

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payment_status is not UNSET:
            field_dict["PaymentStatus"] = payment_status
        if invoiced_on is not UNSET:
            field_dict["InvoicedOn"] = invoiced_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        payment_status = d.pop("PaymentStatus", UNSET)

        def _parse_invoiced_on(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                invoiced_on_type_0 = isoparse(data)

                return invoiced_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        invoiced_on = _parse_invoiced_on(d.pop("InvoicedOn", UNSET))

        qualer_api_models_service_orders_from_update_payment_status_model = cls(
            payment_status=payment_status,
            invoiced_on=invoiced_on,
        )

        qualer_api_models_service_orders_from_update_payment_status_model.additional_properties = (
            d
        )
        return qualer_api_models_service_orders_from_update_payment_status_model

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
