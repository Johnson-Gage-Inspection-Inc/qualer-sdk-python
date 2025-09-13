from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.qualer_api_models_service_orders_from_change_service_order_status_model_service_order_status import (
    ServiceOrdersFromChangeServiceOrderStatusModelServiceOrderStatus,
)

T = TypeVar("T", bound="ServiceOrdersFromChangeServiceOrderStatusModel")


@_attrs_define
class ServiceOrdersFromChangeServiceOrderStatusModel:
    """
    Attributes:
        service_order_status (Union[None,
            ServiceOrdersFromChangeServiceOrderStatusModelServiceOrderStatus]):
        reset_status (Optional[bool]):
        email (Optional[str]):
        password (Optional[str]):
    """

    service_order_status: Union[
        None,
        None,
        ServiceOrdersFromChangeServiceOrderStatusModelServiceOrderStatus,
    ] = None
    reset_status: Optional[bool] = None
    email: Optional[str] = None
    password: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_order_status: Optional[str] = None
        if self.service_order_status and not isinstance(self.service_order_status, None):
            service_order_status = self.service_order_status.value

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
        service_order_status: Union[
            None,
            None,
            ServiceOrdersFromChangeServiceOrderStatusModelServiceOrderStatus,
        ]
        if not _service_order_status:
            service_order_status = None
        elif _service_order_status is None:
            service_order_status = None
        else:
            service_order_status = ServiceOrdersFromChangeServiceOrderStatusModelServiceOrderStatus(
                _service_order_status
            )

        reset_status = d.pop("ResetStatus", None)

        email = d.pop("Email", None)

        password = d.pop("Password", None)

        qualer_api_models_service_orders_from_change_service_order_status_model = cls(
            service_order_status=service_order_status,
            reset_status=reset_status,
            email=email,
            password=password,
        )

        qualer_api_models_service_orders_from_change_service_order_status_model.additional_properties = (
            d
        )
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
