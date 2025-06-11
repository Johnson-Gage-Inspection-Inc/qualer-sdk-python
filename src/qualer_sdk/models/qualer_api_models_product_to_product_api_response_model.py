from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsProductToProductApiResponseModel")


@_attrs_define
class QualerApiModelsProductToProductApiResponseModel:
    """
    Attributes:
        product_id (Union[Unset, int]):
        parent_product_id (Union[Unset, int]):
        category_id (Union[Unset, int]):
        manufacturer_id (Union[Unset, int]):
        manufacturer_name (Union[Unset, str]):
        product_name (Union[Unset, str]):
        parent_product_name (Union[Unset, str]):
        manufacturer_part_number (Union[Unset, str]):
        product_description (Union[Unset, str]):
        is_family (Union[Unset, bool]):
        is_discontinued (Union[Unset, bool]):
        is_stock_item (Union[Unset, bool]):
        unit_sale_price (Union[Unset, float]):
        supplier_information (Union[Unset, str]):
        quantity_on_hand (Union[Unset, int]):
        product_code (Union[Unset, str]):
        category_name (Union[Unset, str]):
        parent_category_name (Union[Unset, str]):
    """

    product_id: Union[Unset, int] = UNSET
    parent_product_id: Union[Unset, int] = UNSET
    category_id: Union[Unset, int] = UNSET
    manufacturer_id: Union[Unset, int] = UNSET
    manufacturer_name: Union[Unset, str] = UNSET
    product_name: Union[Unset, str] = UNSET
    parent_product_name: Union[Unset, str] = UNSET
    manufacturer_part_number: Union[Unset, str] = UNSET
    product_description: Union[Unset, str] = UNSET
    is_family: Union[Unset, bool] = UNSET
    is_discontinued: Union[Unset, bool] = UNSET
    is_stock_item: Union[Unset, bool] = UNSET
    unit_sale_price: Union[Unset, float] = UNSET
    supplier_information: Union[Unset, str] = UNSET
    quantity_on_hand: Union[Unset, int] = UNSET
    product_code: Union[Unset, str] = UNSET
    category_name: Union[Unset, str] = UNSET
    parent_category_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        parent_product_id = self.parent_product_id

        category_id = self.category_id

        manufacturer_id = self.manufacturer_id

        manufacturer_name = self.manufacturer_name

        product_name = self.product_name

        parent_product_name = self.parent_product_name

        manufacturer_part_number = self.manufacturer_part_number

        product_description = self.product_description

        is_family = self.is_family

        is_discontinued = self.is_discontinued

        is_stock_item = self.is_stock_item

        unit_sale_price = self.unit_sale_price

        supplier_information = self.supplier_information

        quantity_on_hand = self.quantity_on_hand

        product_code = self.product_code

        category_name = self.category_name

        parent_category_name = self.parent_category_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_id is not UNSET:
            field_dict["ProductId"] = product_id
        if parent_product_id is not UNSET:
            field_dict["ParentProductId"] = parent_product_id
        if category_id is not UNSET:
            field_dict["CategoryId"] = category_id
        if manufacturer_id is not UNSET:
            field_dict["ManufacturerId"] = manufacturer_id
        if manufacturer_name is not UNSET:
            field_dict["ManufacturerName"] = manufacturer_name
        if product_name is not UNSET:
            field_dict["ProductName"] = product_name
        if parent_product_name is not UNSET:
            field_dict["ParentProductName"] = parent_product_name
        if manufacturer_part_number is not UNSET:
            field_dict["ManufacturerPartNumber"] = manufacturer_part_number
        if product_description is not UNSET:
            field_dict["ProductDescription"] = product_description
        if is_family is not UNSET:
            field_dict["IsFamily"] = is_family
        if is_discontinued is not UNSET:
            field_dict["IsDiscontinued"] = is_discontinued
        if is_stock_item is not UNSET:
            field_dict["IsStockItem"] = is_stock_item
        if unit_sale_price is not UNSET:
            field_dict["UnitSalePrice"] = unit_sale_price
        if supplier_information is not UNSET:
            field_dict["SupplierInformation"] = supplier_information
        if quantity_on_hand is not UNSET:
            field_dict["QuantityOnHand"] = quantity_on_hand
        if product_code is not UNSET:
            field_dict["ProductCode"] = product_code
        if category_name is not UNSET:
            field_dict["CategoryName"] = category_name
        if parent_category_name is not UNSET:
            field_dict["ParentCategoryName"] = parent_category_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("ProductId", UNSET)

        parent_product_id = d.pop("ParentProductId", UNSET)

        category_id = d.pop("CategoryId", UNSET)

        manufacturer_id = d.pop("ManufacturerId", UNSET)

        manufacturer_name = d.pop("ManufacturerName", UNSET)

        product_name = d.pop("ProductName", UNSET)

        parent_product_name = d.pop("ParentProductName", UNSET)

        manufacturer_part_number = d.pop("ManufacturerPartNumber", UNSET)

        product_description = d.pop("ProductDescription", UNSET)

        is_family = d.pop("IsFamily", UNSET)

        is_discontinued = d.pop("IsDiscontinued", UNSET)

        is_stock_item = d.pop("IsStockItem", UNSET)

        unit_sale_price = d.pop("UnitSalePrice", UNSET)

        supplier_information = d.pop("SupplierInformation", UNSET)

        quantity_on_hand = d.pop("QuantityOnHand", UNSET)

        product_code = d.pop("ProductCode", UNSET)

        category_name = d.pop("CategoryName", UNSET)

        parent_category_name = d.pop("ParentCategoryName", UNSET)

        qualer_api_models_product_to_product_api_response_model = cls(
            product_id=product_id,
            parent_product_id=parent_product_id,
            category_id=category_id,
            manufacturer_id=manufacturer_id,
            manufacturer_name=manufacturer_name,
            product_name=product_name,
            parent_product_name=parent_product_name,
            manufacturer_part_number=manufacturer_part_number,
            product_description=product_description,
            is_family=is_family,
            is_discontinued=is_discontinued,
            is_stock_item=is_stock_item,
            unit_sale_price=unit_sale_price,
            supplier_information=supplier_information,
            quantity_on_hand=quantity_on_hand,
            product_code=product_code,
            category_name=category_name,
            parent_category_name=parent_category_name,
        )

        qualer_api_models_product_to_product_api_response_model.additional_properties = (
            d
        )
        return qualer_api_models_product_to_product_api_response_model

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
