from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_order_status import ServiceOrderStatus

T = TypeVar("T", bound="ServiceOrdersFromChangeServiceOrderStatusModel")


@_attrs_define
class ServiceOrdersFromChangeServiceOrderStatusModel:
    """
    Attributes:
        service_order_status (Optional[ServiceOrderStatus]):
        reset_status (Optional[bool]):
        email (Optional[str]):
        password (Optional[str]):
    """

    service_order_status: Optional[ServiceOrderStatus] = None
    reset_status: Optional[bool] = None
    email: Optional[str] = None
    password: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_order_status: Optional[str] = (
            self.service_order_status.value if self.service_order_status else None
        )

        reset_status = self.reset_status

        email = self.email

        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_status is not None:
            field_dict["ServiceOrderStatus"] = service_order_status
        if reset_status is not None:
            field_dict["ResetStatus"] = reset_status
        if email is not None:
            field_dict["Email"] = email
        if password is not None:
            field_dict["Password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _service_order_status = d.pop("ServiceOrderStatus", None)
        service_order_status = ServiceOrderStatus.parse(_service_order_status)

        reset_status = d.pop("ResetStatus", None)

        email = d.pop("Email", None)

        password = d.pop("Password", None)

        qualer_api_models_service_orders_from_change_service_order_status_model = cls(
            service_order_status=service_order_status,
            reset_status=reset_status,
            email=email,
            password=password,
        )

        (
            qualer_api_models_service_orders_from_change_service_order_status_model.additional_properties
        ) = d
        return qualer_api_models_service_orders_from_change_service_order_status_model

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
