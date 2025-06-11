from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsServiceOrdersToPaymentResponseModel")


@_attrs_define
class QualerApiModelsServiceOrdersToPaymentResponseModel:
    """
    Attributes:
        service_order_id (Union[Unset, int]):
        created_by_id (Union[Unset, int]):
        transaction_id (Union[Unset, str]):
        transaction_status (Union[Unset, str]):
        payment_type (Union[Unset, str]):
        service_order_payment_id (Union[Unset, int]):
        payment_amount (Union[Unset, float]):
        details (Union[Unset, str]):
    """

    service_order_id: Union[Unset, int] = UNSET
    created_by_id: Union[Unset, int] = UNSET
    transaction_id: Union[Unset, str] = UNSET
    transaction_status: Union[Unset, str] = UNSET
    payment_type: Union[Unset, str] = UNSET
    service_order_payment_id: Union[Unset, int] = UNSET
    payment_amount: Union[Unset, float] = UNSET
    details: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_order_id = self.service_order_id

        created_by_id = self.created_by_id

        transaction_id = self.transaction_id

        transaction_status = self.transaction_status

        payment_type = self.payment_type

        service_order_payment_id = self.service_order_payment_id

        payment_amount = self.payment_amount

        details = self.details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_id is not UNSET:
            field_dict["ServiceOrderId"] = service_order_id
        if created_by_id is not UNSET:
            field_dict["CreatedById"] = created_by_id
        if transaction_id is not UNSET:
            field_dict["TransactionId"] = transaction_id
        if transaction_status is not UNSET:
            field_dict["TransactionStatus"] = transaction_status
        if payment_type is not UNSET:
            field_dict["PaymentType"] = payment_type
        if service_order_payment_id is not UNSET:
            field_dict["ServiceOrderPaymentId"] = service_order_payment_id
        if payment_amount is not UNSET:
            field_dict["PaymentAmount"] = payment_amount
        if details is not UNSET:
            field_dict["Details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_id = d.pop("ServiceOrderId", UNSET)

        created_by_id = d.pop("CreatedById", UNSET)

        transaction_id = d.pop("TransactionId", UNSET)

        transaction_status = d.pop("TransactionStatus", UNSET)

        payment_type = d.pop("PaymentType", UNSET)

        service_order_payment_id = d.pop("ServiceOrderPaymentId", UNSET)

        payment_amount = d.pop("PaymentAmount", UNSET)

        details = d.pop("Details", UNSET)

        qualer_api_models_service_orders_to_payment_response_model = cls(
            service_order_id=service_order_id,
            created_by_id=created_by_id,
            transaction_id=transaction_id,
            transaction_status=transaction_status,
            payment_type=payment_type,
            service_order_payment_id=service_order_payment_id,
            payment_amount=payment_amount,
            details=details,
        )

        qualer_api_models_service_orders_to_payment_response_model.additional_properties = (
            d
        )
        return qualer_api_models_service_orders_to_payment_response_model

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
