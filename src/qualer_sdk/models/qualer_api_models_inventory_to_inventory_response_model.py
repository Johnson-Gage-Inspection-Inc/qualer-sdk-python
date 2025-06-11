from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsInventoryToInventoryResponseModel")


@_attrs_define
class QualerApiModelsInventoryToInventoryResponseModel:
    """
    Attributes:
        product_id (Union[Unset, int]):
        manufacturer (Union[Unset, str]):
        part_number (Union[Unset, str]):
        is_stock_item (Union[Unset, bool]):
        quantity_on_hand (Union[Unset, int]):
    """

    product_id: Union[Unset, int] = UNSET
    manufacturer: Union[Unset, str] = UNSET
    part_number: Union[Unset, str] = UNSET
    is_stock_item: Union[Unset, bool] = UNSET
    quantity_on_hand: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        manufacturer = self.manufacturer

        part_number = self.part_number

        is_stock_item = self.is_stock_item

        quantity_on_hand = self.quantity_on_hand

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_id is not UNSET:
            field_dict["ProductId"] = product_id
        if manufacturer is not UNSET:
            field_dict["Manufacturer"] = manufacturer
        if part_number is not UNSET:
            field_dict["PartNumber"] = part_number
        if is_stock_item is not UNSET:
            field_dict["IsStockItem"] = is_stock_item
        if quantity_on_hand is not UNSET:
            field_dict["QuantityOnHand"] = quantity_on_hand

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("ProductId", UNSET)

        manufacturer = d.pop("Manufacturer", UNSET)

        part_number = d.pop("PartNumber", UNSET)

        is_stock_item = d.pop("IsStockItem", UNSET)

        quantity_on_hand = d.pop("QuantityOnHand", UNSET)

        qualer_api_models_inventory_to_inventory_response_model = cls(
            product_id=product_id,
            manufacturer=manufacturer,
            part_number=part_number,
            is_stock_item=is_stock_item,
            quantity_on_hand=quantity_on_hand,
        )

        qualer_api_models_inventory_to_inventory_response_model.additional_properties = (
            d
        )
        return qualer_api_models_inventory_to_inventory_response_model

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
