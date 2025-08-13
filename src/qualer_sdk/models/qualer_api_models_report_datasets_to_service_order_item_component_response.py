from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="QualerApiModelsReportDatasetsToServiceOrderItemComponentResponse"
)


@_attrs_define
class QualerApiModelsReportDatasetsToServiceOrderItemComponentResponse:
    """
    Attributes:
        order_item_id (Union[None, Unset, int]):
        component_asset_id (Union[None, Unset, int]):
        component_serial_number (Union[None, Unset, str]):
        component_asset_tag (Union[None, Unset, str]):
        component_asset_user (Union[None, Unset, str]):
        component_equipment_id (Union[None, Unset, str]):
        component_manufacturer_part_number (Union[None, Unset, str]):
        component_manufacturer (Union[None, Unset, str]):
        component_root_category (Union[None, Unset, str]):
        component_sub_category (Union[None, Unset, str]):
        component_location (Union[None, Unset, str]):
        component_display_name (Union[None, Unset, str]):
        component_display_part_number (Union[None, Unset, str]):
    """

    order_item_id: Union[None, Unset, int] = UNSET
    component_asset_id: Union[None, Unset, int] = UNSET
    component_serial_number: Union[None, Unset, str] = UNSET
    component_asset_tag: Union[None, Unset, str] = UNSET
    component_asset_user: Union[None, Unset, str] = UNSET
    component_equipment_id: Union[None, Unset, str] = UNSET
    component_manufacturer_part_number: Union[None, Unset, str] = UNSET
    component_manufacturer: Union[None, Unset, str] = UNSET
    component_root_category: Union[None, Unset, str] = UNSET
    component_sub_category: Union[None, Unset, str] = UNSET
    component_location: Union[None, Unset, str] = UNSET
    component_display_name: Union[None, Unset, str] = UNSET
    component_display_part_number: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_item_id is not UNSET:
            field_dict["OrderItemId"] = order_item_id
        if component_asset_id is not UNSET:
            field_dict["ComponentAssetId"] = component_asset_id
        if component_serial_number is not UNSET:
            field_dict["ComponentSerialNumber"] = component_serial_number
        if component_asset_tag is not UNSET:
            field_dict["ComponentAssetTag"] = component_asset_tag
        if component_asset_user is not UNSET:
            field_dict["ComponentAssetUser"] = component_asset_user
        if component_equipment_id is not UNSET:
            field_dict["ComponentEquipmentId"] = component_equipment_id
        if component_manufacturer_part_number is not UNSET:
            field_dict["ComponentManufacturerPartNumber"] = (
                component_manufacturer_part_number
            )
        if component_manufacturer is not UNSET:
            field_dict["ComponentManufacturer"] = component_manufacturer
        if component_root_category is not UNSET:
            field_dict["ComponentRootCategory"] = component_root_category
        if component_sub_category is not UNSET:
            field_dict["ComponentSubCategory"] = component_sub_category
        if component_location is not UNSET:
            field_dict["ComponentLocation"] = component_location
        if component_display_name is not UNSET:
            field_dict["ComponentDisplayName"] = component_display_name
        if component_display_part_number is not UNSET:
            field_dict["ComponentDisplayPartNumber"] = component_display_part_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_item_id = d.pop("OrderItemId", UNSET)

        component_asset_id = d.pop("ComponentAssetId", UNSET)

        component_serial_number = d.pop("ComponentSerialNumber", UNSET)

        component_asset_tag = d.pop("ComponentAssetTag", UNSET)

        component_asset_user = d.pop("ComponentAssetUser", UNSET)

        component_equipment_id = d.pop("ComponentEquipmentId", UNSET)

        component_manufacturer_part_number = d.pop(
            "ComponentManufacturerPartNumber", UNSET
        )

        component_manufacturer = d.pop("ComponentManufacturer", UNSET)

        component_root_category = d.pop("ComponentRootCategory", UNSET)

        component_sub_category = d.pop("ComponentSubCategory", UNSET)

        component_location = d.pop("ComponentLocation", UNSET)

        component_display_name = d.pop("ComponentDisplayName", UNSET)

        component_display_part_number = d.pop("ComponentDisplayPartNumber", UNSET)

        qualer_api_models_report_datasets_to_service_order_item_component_response = (
            cls(
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
        )

        qualer_api_models_report_datasets_to_service_order_item_component_response.additional_properties = (
            d
        )
        return (
            qualer_api_models_report_datasets_to_service_order_item_component_response
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
