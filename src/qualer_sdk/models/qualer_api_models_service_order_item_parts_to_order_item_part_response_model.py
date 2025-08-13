from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.qualer_api_models_service_order_item_parts_to_order_item_part_response_model_service_order_charge_type import (
    QualerApiModelsServiceOrderItemPartsToOrderItemPartResponseModelServiceOrderChargeType,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="QualerApiModelsServiceOrderItemPartsToOrderItemPartResponseModel"
)


@_attrs_define
class QualerApiModelsServiceOrderItemPartsToOrderItemPartResponseModel:
    """
    Attributes:
        service_order_item_part_id (Union[None, Unset, int]):
        service_order_item_id (Union[None, Unset, int]):
        name (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        discount (Union[None, Unset, float]):
        is_taxable (Union[None, Unset, bool]):
        is_hourly_pricing (Union[None, Unset, bool]):
        price (Union[None, Unset, float]):
        unit_name (Union[None, Unset, str]):
        quantity (Union[None, Unset, float]):
        delivery_charge (Union[None, Unset, float]):
        time_spent_in_minutes (Union[None, Unset, float]):
        free_quantity (Union[None, Unset, int]):
        service_order_charge_type (Union[None, Unset,
            QualerApiModelsServiceOrderItemPartsToOrderItemPartResponseModelServiceOrderChargeType]):
    """

    service_order_item_part_id: Union[None, Unset, int] = UNSET
    service_order_item_id: Union[None, Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    discount: Union[None, Unset, float] = UNSET
    is_taxable: Union[None, Unset, bool] = UNSET
    is_hourly_pricing: Union[None, Unset, bool] = UNSET
    price: Union[None, Unset, float] = UNSET
    unit_name: Union[None, Unset, str] = UNSET
    quantity: Union[None, Unset, float] = UNSET
    delivery_charge: Union[None, Unset, float] = UNSET
    time_spent_in_minutes: Union[None, Unset, float] = UNSET
    free_quantity: Union[None, Unset, int] = UNSET
    service_order_charge_type: Union[
        None,
        Unset,
        QualerApiModelsServiceOrderItemPartsToOrderItemPartResponseModelServiceOrderChargeType,
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_order_item_part_id = self.service_order_item_part_id

        service_order_item_id = self.service_order_item_id

        name = self.name

        description = self.description

        discount = self.discount

        is_taxable = self.is_taxable

        is_hourly_pricing = self.is_hourly_pricing

        price = self.price

        unit_name = self.unit_name

        quantity = self.quantity

        delivery_charge = self.delivery_charge

        time_spent_in_minutes = self.time_spent_in_minutes

        free_quantity = self.free_quantity

        service_order_charge_type: Union[None, Unset, str] = UNSET
        if self.service_order_charge_type and not isinstance(
            self.service_order_charge_type, Unset
        ):
            service_order_charge_type = self.service_order_charge_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_item_part_id is not UNSET:
            field_dict["ServiceOrderItemPartId"] = service_order_item_part_id
        if service_order_item_id is not UNSET:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if name is not UNSET:
            field_dict["Name"] = name
        if description is not UNSET:
            field_dict["Description"] = description
        if discount is not UNSET:
            field_dict["Discount"] = discount
        if is_taxable is not UNSET:
            field_dict["IsTaxable"] = is_taxable
        if is_hourly_pricing is not UNSET:
            field_dict["IsHourlyPricing"] = is_hourly_pricing
        if price is not UNSET:
            field_dict["Price"] = price
        if unit_name is not UNSET:
            field_dict["UnitName"] = unit_name
        if quantity is not UNSET:
            field_dict["Quantity"] = quantity
        if delivery_charge is not UNSET:
            field_dict["DeliveryCharge"] = delivery_charge
        if time_spent_in_minutes is not UNSET:
            field_dict["TimeSpentInMinutes"] = time_spent_in_minutes
        if free_quantity is not UNSET:
            field_dict["FreeQuantity"] = free_quantity
        if service_order_charge_type is not UNSET:
            field_dict["ServiceOrderChargeType"] = service_order_charge_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_item_part_id = d.pop("ServiceOrderItemPartId", UNSET)

        service_order_item_id = d.pop("ServiceOrderItemId", UNSET)

        name = d.pop("Name", UNSET)

        description = d.pop("Description", UNSET)

        discount = d.pop("Discount", UNSET)

        is_taxable = d.pop("IsTaxable", UNSET)

        is_hourly_pricing = d.pop("IsHourlyPricing", UNSET)

        price = d.pop("Price", UNSET)

        unit_name = d.pop("UnitName", UNSET)

        quantity = d.pop("Quantity", UNSET)

        delivery_charge = d.pop("DeliveryCharge", UNSET)

        time_spent_in_minutes = d.pop("TimeSpentInMinutes", UNSET)

        free_quantity = d.pop("FreeQuantity", UNSET)

        _service_order_charge_type = d.pop("ServiceOrderChargeType", UNSET)
        service_order_charge_type: Union[
            None,
            Unset,
            QualerApiModelsServiceOrderItemPartsToOrderItemPartResponseModelServiceOrderChargeType,
        ]
        if isinstance(_service_order_charge_type, Unset):
            service_order_charge_type = UNSET
        else:
            service_order_charge_type = QualerApiModelsServiceOrderItemPartsToOrderItemPartResponseModelServiceOrderChargeType(
                _service_order_charge_type
            )

        qualer_api_models_service_order_item_parts_to_order_item_part_response_model = (
            cls(
                service_order_item_part_id=service_order_item_part_id,
                service_order_item_id=service_order_item_id,
                name=name,
                description=description,
                discount=discount,
                is_taxable=is_taxable,
                is_hourly_pricing=is_hourly_pricing,
                price=price,
                unit_name=unit_name,
                quantity=quantity,
                delivery_charge=delivery_charge,
                time_spent_in_minutes=time_spent_in_minutes,
                free_quantity=free_quantity,
                service_order_charge_type=service_order_charge_type,
            )
        )

        qualer_api_models_service_order_item_parts_to_order_item_part_response_model.additional_properties = (
            d
        )
        return (
            qualer_api_models_service_order_item_parts_to_order_item_part_response_model
        )

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
