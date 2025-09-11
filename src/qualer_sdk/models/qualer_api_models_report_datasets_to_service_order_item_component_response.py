from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QualerApiModelsReportDatasetsToServiceOrderItemComponentResponse")


@_attrs_define
class QualerApiModelsReportDatasetsToServiceOrderItemComponentResponse:
    """
    Attributes:
        order_item_id (Optional[int]):
        component_asset_id (Optional[int]):
        component_serial_number (Optional[str]):
        component_asset_tag (Optional[str]):
        component_asset_user (Optional[str]):
        component_equipment_id (Optional[str]):
        component_manufacturer_part_number (Optional[str]):
        component_manufacturer (Optional[str]):
        component_root_category (Optional[str]):
        component_sub_category (Optional[str]):
        component_location (Optional[str]):
        component_display_name (Optional[str]):
        component_display_part_number (Optional[str]):
    """

    order_item_id: Optional[int] = None
    component_asset_id: Optional[int] = None
    component_serial_number: Optional[str] = None
    component_asset_tag: Optional[str] = None
    component_asset_user: Optional[str] = None
    component_equipment_id: Optional[str] = None
    component_manufacturer_part_number: Optional[str] = None
    component_manufacturer: Optional[str] = None
    component_root_category: Optional[str] = None
    component_sub_category: Optional[str] = None
    component_location: Optional[str] = None
    component_display_name: Optional[str] = None
    component_display_part_number: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_item_id = self.order_item_id

        component_asset_id = self.component_asset_id

        component_serial_number = self.component_serial_number

        component_asset_tag = self.component_asset_tag

        component_asset_user = self.component_asset_user

        component_equipment_id = self.component_equipment_id

        component_manufacturer_part_number = self.component_manufacturer_part_number

        component_manufacturer = self.component_manufacturer

        component_root_category = self.component_root_category

        component_sub_category = self.component_sub_category

        component_location = self.component_location

        component_display_name = self.component_display_name

        component_display_part_number = self.component_display_part_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_item_id is not None:
            field_dict["OrderItemId"] = order_item_id
        if component_asset_id is not None:
            field_dict["ComponentAssetId"] = component_asset_id
        if component_serial_number is not None:
            field_dict["ComponentSerialNumber"] = component_serial_number
        if component_asset_tag is not None:
            field_dict["ComponentAssetTag"] = component_asset_tag
        if component_asset_user is not None:
            field_dict["ComponentAssetUser"] = component_asset_user
        if component_equipment_id is not None:
            field_dict["ComponentEquipmentId"] = component_equipment_id
        if component_manufacturer_part_number is not None:
            field_dict["ComponentManufacturerPartNumber"] = component_manufacturer_part_number
        if component_manufacturer is not None:
            field_dict["ComponentManufacturer"] = component_manufacturer
        if component_root_category is not None:
            field_dict["ComponentRootCategory"] = component_root_category
        if component_sub_category is not None:
            field_dict["ComponentSubCategory"] = component_sub_category
        if component_location is not None:
            field_dict["ComponentLocation"] = component_location
        if component_display_name is not None:
            field_dict["ComponentDisplayName"] = component_display_name
        if component_display_part_number is not None:
            field_dict["ComponentDisplayPartNumber"] = component_display_part_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_item_id = d.pop("OrderItemId", None)

        component_asset_id = d.pop("ComponentAssetId", None)

        component_serial_number = d.pop("ComponentSerialNumber", None)

        component_asset_tag = d.pop("ComponentAssetTag", None)

        component_asset_user = d.pop("ComponentAssetUser", None)

        component_equipment_id = d.pop("ComponentEquipmentId", None)

        component_manufacturer_part_number = d.pop("ComponentManufacturerPartNumber", None)

        component_manufacturer = d.pop("ComponentManufacturer", None)

        component_root_category = d.pop("ComponentRootCategory", None)

        component_sub_category = d.pop("ComponentSubCategory", None)

        component_location = d.pop("ComponentLocation", None)

        component_display_name = d.pop("ComponentDisplayName", None)

        component_display_part_number = d.pop("ComponentDisplayPartNumber", None)

        qualer_api_models_report_datasets_to_service_order_item_component_response = cls(
            order_item_id=order_item_id,
            component_asset_id=component_asset_id,
            component_serial_number=component_serial_number,
            component_asset_tag=component_asset_tag,
            component_asset_user=component_asset_user,
            component_equipment_id=component_equipment_id,
            component_manufacturer_part_number=component_manufacturer_part_number,
            component_manufacturer=component_manufacturer,
            component_root_category=component_root_category,
            component_sub_category=component_sub_category,
            component_location=component_location,
            component_display_name=component_display_name,
            component_display_part_number=component_display_part_number,
        )

        qualer_api_models_report_datasets_to_service_order_item_component_response.additional_properties = (
            d
        )
        return qualer_api_models_report_datasets_to_service_order_item_component_response

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
