from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsServiceOrdersFromAddPaymentModel")


@_attrs_define
class QualerApiModelsServiceOrdersFromAddPaymentModel:
    """
    Attributes:
        payment_type (Union[None, Unset, str]):
        payment_amount (Union[None, Unset, float]):
        details (Union[None, Unset, str]):
    """

    payment_type: Union[None, Unset, str] = UNSET
    payment_amount: Union[None, Unset, float] = UNSET
    details: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payment_type = self.payment_type

        payment_amount = self.payment_amount

        details = self.details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payment_type is not UNSET:
            field_dict["PaymentType"] = payment_type
        if payment_amount is not UNSET:
            field_dict["PaymentAmount"] = payment_amount
        if details is not UNSET:
            field_dict["Details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        payment_type = d.pop("PaymentType", UNSET)

        payment_amount = d.pop("PaymentAmount", UNSET)

        details = d.pop("Details", UNSET)

        qualer_api_models_service_orders_from_add_payment_model = cls(
            payment_type=payment_type,
            payment_amount=payment_amount,
            details=details,
        )

        qualer_api_models_service_orders_from_add_payment_model.additional_properties = (
            d
        )
        return qualer_api_models_service_orders_from_add_payment_model

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
