from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServiceOrdersToPaymentResponseModel")


@_attrs_define
class ServiceOrdersToPaymentResponseModel:
    """
    Attributes:
        service_order_id (Optional[int]):
        created_by_id (Optional[int]):
        transaction_id (Optional[str]):
        transaction_status (Optional[str]):
        payment_type (Optional[str]):
        service_order_payment_id (Optional[int]):
        payment_amount (Optional[float]):
        details (Optional[str]):
    """

    service_order_id: Optional[int] = None
    created_by_id: Optional[int] = None
    transaction_id: Optional[str] = None
    transaction_status: Optional[str] = None
    payment_type: Optional[str] = None
    service_order_payment_id: Optional[int] = None
    payment_amount: Optional[float] = None
    details: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_order_id = self.service_order_id
        created_by_id = self.created_by_id
        transaction_id = self.transaction_id
        transaction_status = self.transaction_status
        payment_type = self.payment_type
        service_order_payment_id = self.service_order_payment_id
        payment_amount = self.payment_amount
        details = self.details
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_id is not None:
            field_dict["ServiceOrderId"] = service_order_id
        if created_by_id is not None:
            field_dict["CreatedById"] = created_by_id
        if transaction_id is not None:
            field_dict["TransactionId"] = transaction_id
        if transaction_status is not None:
            field_dict["TransactionStatus"] = transaction_status
        if payment_type is not None:
            field_dict["PaymentType"] = payment_type
        if service_order_payment_id is not None:
            field_dict["ServiceOrderPaymentId"] = service_order_payment_id
        if payment_amount is not None:
            field_dict["PaymentAmount"] = payment_amount
        if details is not None:
            field_dict["Details"] = details
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_id = d.pop("ServiceOrderId", None)
        created_by_id = d.pop("CreatedById", None)
        transaction_id = d.pop("TransactionId", None)
        transaction_status = d.pop("TransactionStatus", None)
        payment_type = d.pop("PaymentType", None)
        service_order_payment_id = d.pop("ServiceOrderPaymentId", None)
        payment_amount = d.pop("PaymentAmount", None)
        details = d.pop("Details", None)
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
        qualer_api_models_service_orders_to_payment_response_model.additional_properties = d
        return qualer_api_models_service_orders_to_payment_response_model

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
