import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsReportDatasetsToReferenceStandardResponse")


@_attrs_define
class QualerApiModelsReportDatasetsToReferenceStandardResponse:
    """
    Attributes:
        is_auxiliary (Union[Unset, bool]):
        last_service_date (Union[Unset, datetime.datetime]):
        next_service_date (Union[Unset, datetime.datetime]):
        certificate_number (Union[Unset, str]):
        calibrated_by (Union[Unset, str]):
        tool_name (Union[Unset, str]):
        tool_site (Union[Unset, str]):
        tool_room (Union[Unset, str]):
        tool_station (Union[Unset, str]):
        tool_location (Union[Unset, str]):
        asset_tag (Union[Unset, str]):
        lot_number (Union[Unset, str]):
        asset_user (Union[Unset, str]):
        tool_type_name (Union[Unset, str]):
        tool_description (Union[Unset, str]):
        tool_id (Union[Unset, int]):
        manufacturer (Union[Unset, str]):
        serial_number (Union[Unset, str]):
        area (Union[Unset, str]):
        service_order_item_id (Union[Unset, int]):
        manufacturer_part_number (Union[Unset, str]):
        equipment_id (Union[Unset, str]):
    """

    is_auxiliary: Union[Unset, bool] = UNSET
    last_service_date: Union[Unset, datetime.datetime] = UNSET
    next_service_date: Union[Unset, datetime.datetime] = UNSET
    certificate_number: Union[Unset, str] = UNSET
    calibrated_by: Union[Unset, str] = UNSET
    tool_name: Union[Unset, str] = UNSET
    tool_site: Union[Unset, str] = UNSET
    tool_room: Union[Unset, str] = UNSET
    tool_station: Union[Unset, str] = UNSET
    tool_location: Union[Unset, str] = UNSET
    asset_tag: Union[Unset, str] = UNSET
    lot_number: Union[Unset, str] = UNSET
    asset_user: Union[Unset, str] = UNSET
    tool_type_name: Union[Unset, str] = UNSET
    tool_description: Union[Unset, str] = UNSET
    tool_id: Union[Unset, int] = UNSET
    manufacturer: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    area: Union[Unset, str] = UNSET
    service_order_item_id: Union[Unset, int] = UNSET
    manufacturer_part_number: Union[Unset, str] = UNSET
    equipment_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_auxiliary = self.is_auxiliary

        last_service_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_service_date, Unset):
            last_service_date = self.last_service_date.isoformat()

        next_service_date: Union[Unset, str] = UNSET
        if not isinstance(self.next_service_date, Unset):
            next_service_date = self.next_service_date.isoformat()

        certificate_number = self.certificate_number

        calibrated_by = self.calibrated_by

        tool_name = self.tool_name

        tool_site = self.tool_site

        tool_room = self.tool_room

        tool_station = self.tool_station

        tool_location = self.tool_location

        asset_tag = self.asset_tag

        lot_number = self.lot_number

        asset_user = self.asset_user

        tool_type_name = self.tool_type_name

        tool_description = self.tool_description

        tool_id = self.tool_id

        manufacturer = self.manufacturer

        serial_number = self.serial_number

        area = self.area

        service_order_item_id = self.service_order_item_id

        manufacturer_part_number = self.manufacturer_part_number

        equipment_id = self.equipment_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_auxiliary is not UNSET:
            field_dict["IsAuxiliary"] = is_auxiliary
        if last_service_date is not UNSET:
            field_dict["LastServiceDate"] = last_service_date
        if next_service_date is not UNSET:
            field_dict["NextServiceDate"] = next_service_date
        if certificate_number is not UNSET:
            field_dict["CertificateNumber"] = certificate_number
        if calibrated_by is not UNSET:
            field_dict["CalibratedBy"] = calibrated_by
        if tool_name is not UNSET:
            field_dict["ToolName"] = tool_name
        if tool_site is not UNSET:
            field_dict["ToolSite"] = tool_site
        if tool_room is not UNSET:
            field_dict["ToolRoom"] = tool_room
        if tool_station is not UNSET:
            field_dict["ToolStation"] = tool_station
        if tool_location is not UNSET:
            field_dict["ToolLocation"] = tool_location
        if asset_tag is not UNSET:
            field_dict["AssetTag"] = asset_tag
        if lot_number is not UNSET:
            field_dict["LotNumber"] = lot_number
        if asset_user is not UNSET:
            field_dict["AssetUser"] = asset_user
        if tool_type_name is not UNSET:
            field_dict["ToolTypeName"] = tool_type_name
        if tool_description is not UNSET:
            field_dict["ToolDescription"] = tool_description
        if tool_id is not UNSET:
            field_dict["ToolId"] = tool_id
        if manufacturer is not UNSET:
            field_dict["Manufacturer"] = manufacturer
        if serial_number is not UNSET:
            field_dict["SerialNumber"] = serial_number
        if area is not UNSET:
            field_dict["Area"] = area
        if service_order_item_id is not UNSET:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if manufacturer_part_number is not UNSET:
            field_dict["ManufacturerPartNumber"] = manufacturer_part_number
        if equipment_id is not UNSET:
            field_dict["EquipmentId"] = equipment_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_auxiliary = d.pop("IsAuxiliary", UNSET)

        _last_service_date = d.pop("LastServiceDate", UNSET)
        last_service_date: Union[Unset, datetime.datetime]
        if isinstance(_last_service_date, Unset):
            last_service_date = UNSET
        else:
            last_service_date = isoparse(_last_service_date)

        _next_service_date = d.pop("NextServiceDate", UNSET)
        next_service_date: Union[Unset, datetime.datetime]
        if isinstance(_next_service_date, Unset):
            next_service_date = UNSET
        else:
            next_service_date = isoparse(_next_service_date)

        certificate_number = d.pop("CertificateNumber", UNSET)

        calibrated_by = d.pop("CalibratedBy", UNSET)

        tool_name = d.pop("ToolName", UNSET)

        tool_site = d.pop("ToolSite", UNSET)

        tool_room = d.pop("ToolRoom", UNSET)

        tool_station = d.pop("ToolStation", UNSET)

        tool_location = d.pop("ToolLocation", UNSET)

        asset_tag = d.pop("AssetTag", UNSET)

        lot_number = d.pop("LotNumber", UNSET)

        asset_user = d.pop("AssetUser", UNSET)

        tool_type_name = d.pop("ToolTypeName", UNSET)

        tool_description = d.pop("ToolDescription", UNSET)

        tool_id = d.pop("ToolId", UNSET)

        manufacturer = d.pop("Manufacturer", UNSET)

        serial_number = d.pop("SerialNumber", UNSET)

        area = d.pop("Area", UNSET)

        service_order_item_id = d.pop("ServiceOrderItemId", UNSET)

        manufacturer_part_number = d.pop("ManufacturerPartNumber", UNSET)

        equipment_id = d.pop("EquipmentId", UNSET)

        qualer_api_models_report_datasets_to_reference_standard_response = cls(
            is_auxiliary=is_auxiliary,
            last_service_date=last_service_date,
            next_service_date=next_service_date,
            certificate_number=certificate_number,
            calibrated_by=calibrated_by,
            tool_name=tool_name,
            tool_site=tool_site,
            tool_room=tool_room,
            tool_station=tool_station,
            tool_location=tool_location,
            asset_tag=asset_tag,
            lot_number=lot_number,
            asset_user=asset_user,
            tool_type_name=tool_type_name,
            tool_description=tool_description,
            tool_id=tool_id,
            manufacturer=manufacturer,
            serial_number=serial_number,
            area=area,
            service_order_item_id=service_order_item_id,
            manufacturer_part_number=manufacturer_part_number,
            equipment_id=equipment_id,
        )

        qualer_api_models_report_datasets_to_reference_standard_response.additional_properties = (
            d
        )
        return qualer_api_models_report_datasets_to_reference_standard_response

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
