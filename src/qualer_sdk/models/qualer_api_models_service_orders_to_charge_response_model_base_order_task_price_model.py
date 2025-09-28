from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T",
    bound="ServiceOrdersToChargeResponseModelBaseOrderTaskPriceModel",
)


@_attrs_define
class ServiceOrdersToChargeResponseModelBaseOrderTaskPriceModel:
    """
    Attributes:
        contract_discount (Optional[float]):
        time_spent (Optional[float]):
        is_hourly (Optional[bool]):
        details (Optional[str]):
        name (Optional[str]):
        price (Optional[float]):
    """

    contract_discount: Optional[float] = None
    time_spent: Optional[float] = None
    is_hourly: Optional[bool] = None
    details: Optional[str] = None
    name: Optional[str] = None
    price: Optional[float] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contract_discount = self.contract_discount
        time_spent = self.time_spent
        is_hourly = self.is_hourly
        details = self.details
        name = self.name
        price = self.price
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contract_discount is not None:
            field_dict["ContractDiscount"] = contract_discount
        if time_spent is not None:
            field_dict["TimeSpent"] = time_spent
        if is_hourly is not None:
            field_dict["IsHourly"] = is_hourly
        if details is not None:
            field_dict["Details"] = details
        if name is not None:
            field_dict["Name"] = name
        if price is not None:
            field_dict["Price"] = price
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contract_discount = d.pop("ContractDiscount", None)
        time_spent = d.pop("TimeSpent", None)
        is_hourly = d.pop("IsHourly", None)
        details = d.pop("Details", None)
        name = d.pop("Name", None)
        price = d.pop("Price", None)
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
