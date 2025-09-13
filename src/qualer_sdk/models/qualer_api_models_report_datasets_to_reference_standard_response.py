import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ReportDatasetsToReferenceStandardResponse")


@_attrs_define
class ReportDatasetsToReferenceStandardResponse:
    """
    Attributes:
        is_auxiliary (Optional[bool]):
        last_service_date (Optional[datetime.datetime]):
        next_service_date (Optional[datetime.datetime]):
        certificate_number (Optional[str]):
        calibrated_by (Optional[str]):
        tool_name (Optional[str]):
        tool_site (Optional[str]):
        tool_room (Optional[str]):
        tool_station (Optional[str]):
        tool_location (Optional[str]):
        asset_tag (Optional[str]):
        lot_number (Optional[str]):
        asset_user (Optional[str]):
        tool_type_name (Optional[str]):
        tool_description (Optional[str]):
        tool_id (Optional[int]):
        manufacturer (Optional[str]):
        serial_number (Optional[str]):
        area (Optional[str]):
        service_order_item_id (Optional[int]):
        manufacturer_part_number (Optional[str]):
        equipment_id (Optional[str]):
    """

    is_auxiliary: Optional[bool] = None
    last_service_date: Optional[datetime.datetime] = None
    next_service_date: Optional[datetime.datetime] = None
    certificate_number: Optional[str] = None
    calibrated_by: Optional[str] = None
    tool_name: Optional[str] = None
    tool_site: Optional[str] = None
    tool_room: Optional[str] = None
    tool_station: Optional[str] = None
    tool_location: Optional[str] = None
    asset_tag: Optional[str] = None
    lot_number: Optional[str] = None
    asset_user: Optional[str] = None
    tool_type_name: Optional[str] = None
    tool_description: Optional[str] = None
    tool_id: Optional[int] = None
    manufacturer: Optional[str] = None
    serial_number: Optional[str] = None
    area: Optional[str] = None
    service_order_item_id: Optional[int] = None
    manufacturer_part_number: Optional[str] = None
    equipment_id: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_auxiliary = self.is_auxiliary

        last_service_date: Optional[str]
        if not self.last_service_date:
            last_service_date = None
        elif isinstance(self.last_service_date, datetime.datetime):
            last_service_date = self.last_service_date.isoformat()
        else:
            last_service_date = self.last_service_date

        next_service_date: Optional[str]
        if not self.next_service_date:
            next_service_date = None
        elif isinstance(self.next_service_date, datetime.datetime):
            next_service_date = self.next_service_date.isoformat()
        else:
            next_service_date = self.next_service_date

        certificate_number: Optional[str]
        if not self.certificate_number:
            certificate_number = None
        else:
            certificate_number = self.certificate_number

        calibrated_by: Optional[str]
        if not self.calibrated_by:
            calibrated_by = None
        else:
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_auxiliary is not None:
            field_dict["IsAuxiliary"] = is_auxiliary
        if last_service_date is not None:
            field_dict["LastServiceDate"] = last_service_date
        if next_service_date is not None:
            field_dict["NextServiceDate"] = next_service_date
        if certificate_number is not None:
            field_dict["CertificateNumber"] = certificate_number
        if calibrated_by is not None:
            field_dict["CalibratedBy"] = calibrated_by
        if tool_name is not None:
            field_dict["ToolName"] = tool_name
        if tool_site is not None:
            field_dict["ToolSite"] = tool_site
        if tool_room is not None:
            field_dict["ToolRoom"] = tool_room
        if tool_station is not None:
            field_dict["ToolStation"] = tool_station
        if tool_location is not None:
            field_dict["ToolLocation"] = tool_location
        if asset_tag is not None:
            field_dict["AssetTag"] = asset_tag
        if lot_number is not None:
            field_dict["LotNumber"] = lot_number
        if asset_user is not None:
            field_dict["AssetUser"] = asset_user
        if tool_type_name is not None:
            field_dict["ToolTypeName"] = tool_type_name
        if tool_description is not None:
            field_dict["ToolDescription"] = tool_description
        if tool_id is not None:
            field_dict["ToolId"] = tool_id
        if manufacturer is not None:
            field_dict["Manufacturer"] = manufacturer
        if serial_number is not None:
            field_dict["SerialNumber"] = serial_number
        if area is not None:
            field_dict["Area"] = area
        if service_order_item_id is not None:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if manufacturer_part_number is not None:
            field_dict["ManufacturerPartNumber"] = manufacturer_part_number
        if equipment_id is not None:
            field_dict["EquipmentId"] = equipment_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_auxiliary = d.pop("IsAuxiliary", None)

        def _parse_last_service_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_service_date_type_0 = isoparse(data)

                return last_service_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        last_service_date = _parse_last_service_date(d.pop("LastServiceDate", None))

        def _parse_next_service_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_service_date_type_0 = isoparse(data)

                return next_service_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        next_service_date = _parse_next_service_date(d.pop("NextServiceDate", None))

        def _parse_certificate_number(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        certificate_number = _parse_certificate_number(d.pop("CertificateNumber", None))

        def _parse_calibrated_by(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        calibrated_by = _parse_calibrated_by(d.pop("CalibratedBy", None))

        tool_name = d.pop("ToolName", None)

        tool_site = d.pop("ToolSite", None)

        tool_room = d.pop("ToolRoom", None)

        tool_station = d.pop("ToolStation", None)

        tool_location = d.pop("ToolLocation", None)

        asset_tag = d.pop("AssetTag", None)

        lot_number = d.pop("LotNumber", None)

        asset_user = d.pop("AssetUser", None)

        tool_type_name = d.pop("ToolTypeName", None)

        tool_description = d.pop("ToolDescription", None)

        tool_id = d.pop("ToolId", None)

        manufacturer = d.pop("Manufacturer", None)

        serial_number = d.pop("SerialNumber", None)

        area = d.pop("Area", None)

        service_order_item_id = d.pop("ServiceOrderItemId", None)

        manufacturer_part_number = d.pop("ManufacturerPartNumber", None)

        equipment_id = d.pop("EquipmentId", None)

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

        qualer_api_models_report_datasets_to_reference_standard_response.additional_properties = d
        return qualer_api_models_report_datasets_to_reference_standard_response

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
