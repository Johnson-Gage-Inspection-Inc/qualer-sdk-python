from collections.abc import Mapping
from typing import Any, Dict, List, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetOrderStatusResponse200")


@_attrs_define
class GetOrderStatusResponse200:
    """Response model for getting current and next service order status.

    Attributes:
        current_service_order_status: The current status of the service order
        next_service_order_status: The next status according to the workflow
        password_reentering_required: Whether password re-entry is required
        email_reentering_required: Whether email re-entry is required
    """

    current_service_order_status: str
    next_service_order_status: str
    password_reentering_required: bool
    email_reentering_required: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_service_order_status = self.current_service_order_status
        next_service_order_status = self.next_service_order_status
        password_reentering_required = self.password_reentering_required
        email_reentering_required = self.email_reentering_required

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "CurrentServiceOrderStatus": current_service_order_status,
                "NextServiceOrderStatus": next_service_order_status,
                "PasswordReenteringRequired": password_reentering_required,
                "EmailReenteringRequired": email_reentering_required,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_service_order_status = d.pop("CurrentServiceOrderStatus")
        next_service_order_status = d.pop("NextServiceOrderStatus")
        password_reentering_required = d.pop("PasswordReenteringRequired")
        email_reentering_required = d.pop("EmailReenteringRequired")

        get_order_status_response_200 = cls(
            current_service_order_status=current_service_order_status,
            next_service_order_status=next_service_order_status,
            password_reentering_required=password_reentering_required,
            email_reentering_required=email_reentering_required,
        )

        get_order_status_response_200.additional_properties = d
        return get_order_status_response_200

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
