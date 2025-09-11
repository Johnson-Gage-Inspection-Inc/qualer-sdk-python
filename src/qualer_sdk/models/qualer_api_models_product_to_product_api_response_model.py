from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QualerApiModelsProductToProductApiResponseModel")


@_attrs_define
class QualerApiModelsProductToProductApiResponseModel:
    """
    Attributes:
        product_id (Optional[int]):
        parent_product_id (Optional[int]):
        category_id (Optional[int]):
        manufacturer_id (Optional[int]):
        manufacturer_name (Optional[str]):
        product_name (Optional[str]):
        parent_product_name (Optional[str]):
        manufacturer_part_number (Optional[str]):
        product_description (Optional[str]):
        is_family (Optional[bool]):
        is_discontinued (Optional[bool]):
        is_stock_item (Optional[bool]):
        unit_sale_price (Optional[float]):
        supplier_information (Optional[str]):
        quantity_on_hand (Optional[int]):
        product_code (Optional[str]):
        category_name (Optional[str]):
        parent_category_name (Optional[str]):
    """

    product_id: Optional[int] = None
    parent_product_id: Optional[int] = None
    category_id: Optional[int] = None
    manufacturer_id: Optional[int] = None
    manufacturer_name: Optional[str] = None
    product_name: Optional[str] = None
    parent_product_name: Optional[str] = None
    manufacturer_part_number: Optional[str] = None
    product_description: Optional[str] = None
    is_family: Optional[bool] = None
    is_discontinued: Optional[bool] = None
    is_stock_item: Optional[bool] = None
    unit_sale_price: Optional[float] = None
    supplier_information: Optional[str] = None
    quantity_on_hand: Optional[int] = None
    product_code: Optional[str] = None
    category_name: Optional[str] = None
    parent_category_name: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_id is not None:
            field_dict["ProductId"] = product_id
        if parent_product_id is not None:
            field_dict["ParentProductId"] = parent_product_id
        if category_id is not None:
            field_dict["CategoryId"] = category_id
        if manufacturer_id is not None:
            field_dict["ManufacturerId"] = manufacturer_id
        if manufacturer_name is not None:
            field_dict["ManufacturerName"] = manufacturer_name
        if product_name is not None:
            field_dict["ProductName"] = product_name
        if parent_product_name is not None:
            field_dict["ParentProductName"] = parent_product_name
        if manufacturer_part_number is not None:
            field_dict["ManufacturerPartNumber"] = manufacturer_part_number
        if product_description is not None:
            field_dict["ProductDescription"] = product_description
        if is_family is not None:
            field_dict["IsFamily"] = is_family
        if is_discontinued is not None:
            field_dict["IsDiscontinued"] = is_discontinued
        if is_stock_item is not None:
            field_dict["IsStockItem"] = is_stock_item
        if unit_sale_price is not None:
            field_dict["UnitSalePrice"] = unit_sale_price
        if supplier_information is not None:
            field_dict["SupplierInformation"] = supplier_information
        if quantity_on_hand is not None:
            field_dict["QuantityOnHand"] = quantity_on_hand
        if product_code is not None:
            field_dict["ProductCode"] = product_code
        if category_name is not None:
            field_dict["CategoryName"] = category_name
        if parent_category_name is not None:
            field_dict["ParentCategoryName"] = parent_category_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("ProductId", None)

        parent_product_id = d.pop("ParentProductId", None)

        category_id = d.pop("CategoryId", None)

        manufacturer_id = d.pop("ManufacturerId", None)

        manufacturer_name = d.pop("ManufacturerName", None)

        product_name = d.pop("ProductName", None)

        parent_product_name = d.pop("ParentProductName", None)

        manufacturer_part_number = d.pop("ManufacturerPartNumber", None)

        product_description = d.pop("ProductDescription", None)

        is_family = d.pop("IsFamily", None)

        is_discontinued = d.pop("IsDiscontinued", None)

        is_stock_item = d.pop("IsStockItem", None)

        unit_sale_price = d.pop("UnitSalePrice", None)

        supplier_information = d.pop("SupplierInformation", None)

        quantity_on_hand = d.pop("QuantityOnHand", None)

        product_code = d.pop("ProductCode", None)

        category_name = d.pop("CategoryName", None)

        parent_category_name = d.pop("ParentCategoryName", None)

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

        qualer_api_models_product_to_product_api_response_model.additional_properties = d
        return qualer_api_models_product_to_product_api_response_model

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
