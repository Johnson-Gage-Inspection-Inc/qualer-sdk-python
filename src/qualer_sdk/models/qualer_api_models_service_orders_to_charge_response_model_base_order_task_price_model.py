from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderTaskPriceModel",
)


@_attrs_define
class QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderTaskPriceModel:
    """
    Attributes:
        contract_discount (Union[None, Unset, float]):
        time_spent (Union[None, Unset, float]):
        is_hourly (Union[None, Unset, bool]):
        details (Union[None, Unset, str]):
        name (Union[None, Unset, str]):
        price (Union[None, Unset, float]):
    """

    contract_discount: Union[None, Unset, float] = UNSET
    time_spent: Union[None, Unset, float] = UNSET
    is_hourly: Union[None, Unset, bool] = UNSET
    details: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    price: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contract_discount = self.contract_discount

        time_spent = self.time_spent

        is_hourly = self.is_hourly

        details = self.details

        name = self.name

        price = self.price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contract_discount is not UNSET:
            field_dict["ContractDiscount"] = contract_discount
        if time_spent is not UNSET:
            field_dict["TimeSpent"] = time_spent
        if is_hourly is not UNSET:
            field_dict["IsHourly"] = is_hourly
        if details is not UNSET:
            field_dict["Details"] = details
        if name is not UNSET:
            field_dict["Name"] = name
        if price is not UNSET:
            field_dict["Price"] = price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contract_discount = d.pop("ContractDiscount", UNSET)

        time_spent = d.pop("TimeSpent", UNSET)

        is_hourly = d.pop("IsHourly", UNSET)

        details = d.pop("Details", UNSET)

        name = d.pop("Name", UNSET)

        price = d.pop("Price", UNSET)

        qualer_api_models_service_orders_to_charge_response_model_base_order_task_price_model = cls(
            contract_discount=contract_discount,
            time_spent=time_spent,
            is_hourly=is_hourly,
            details=details,
            name=name,
            price=price,
        )

        qualer_api_models_service_orders_to_charge_response_model_base_order_task_price_model.additional_properties = (
            d
        )
        return qualer_api_models_service_orders_to_charge_response_model_base_order_task_price_model

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
