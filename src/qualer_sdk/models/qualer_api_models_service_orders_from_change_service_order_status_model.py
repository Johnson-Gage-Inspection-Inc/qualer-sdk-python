from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.qualer_api_models_service_orders_from_change_service_order_status_model_service_order_status import (
    QualerApiModelsServiceOrdersFromChangeServiceOrderStatusModelServiceOrderStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsServiceOrdersFromChangeServiceOrderStatusModel")


@_attrs_define
class QualerApiModelsServiceOrdersFromChangeServiceOrderStatusModel:
    """
    Attributes:
        service_order_status (Union[Unset,
            QualerApiModelsServiceOrdersFromChangeServiceOrderStatusModelServiceOrderStatus]):
        reset_status (Union[Unset, bool]):
        email (Union[Unset, str]):
        password (Union[Unset, str]):
    """

    service_order_status: Union[
        Unset,
        QualerApiModelsServiceOrdersFromChangeServiceOrderStatusModelServiceOrderStatus,
    ] = UNSET
    reset_status: Union[Unset, bool] = UNSET
    email: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_order_status: Union[Unset, str] = UNSET
        if not isinstance(self.service_order_status, Unset):
            service_order_status = self.service_order_status.value

        reset_status = self.reset_status

        email = self.email

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_status is not UNSET:
            field_dict["ServiceOrderStatus"] = service_order_status
        if reset_status is not UNSET:
            field_dict["ResetStatus"] = reset_status
        if email is not UNSET:
            field_dict["Email"] = email
        if password is not UNSET:
            field_dict["Password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _service_order_status = d.pop("ServiceOrderStatus", UNSET)
        service_order_status: Union[
            Unset,
            QualerApiModelsServiceOrdersFromChangeServiceOrderStatusModelServiceOrderStatus,
        ]
        if isinstance(_service_order_status, Unset):
            service_order_status = UNSET
        elif _service_order_status is None:
            service_order_status = None
        else:
            service_order_status = QualerApiModelsServiceOrdersFromChangeServiceOrderStatusModelServiceOrderStatus(
                _service_order_status
            )

        reset_status = d.pop("ResetStatus", UNSET)

        email = d.pop("Email", UNSET)

        password = d.pop("Password", UNSET)

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
