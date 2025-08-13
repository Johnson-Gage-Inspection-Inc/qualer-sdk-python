import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel"
)


@_attrs_define
class QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel:
    """
    Attributes:
        measurement_tool_id (Union[None, Unset, int]):
        last_service_date (Union[None, Unset, datetime.datetime]):
        next_service_date (Union[None, Unset, datetime.datetime]):
        calibrated_by (Union[None, Unset, str]):
        certificate_number (Union[None, Unset, str]):
        tool_name (Union[None, Unset, str]):
        tool_description (Union[None, Unset, str]):
        manufacturer (Union[None, Unset, str]):
        manufacturer_part_number (Union[None, Unset, str]):
        serial_number (Union[None, Unset, str]):
        asset_tag (Union[None, Unset, str]):
        asset_user (Union[None, Unset, str]):
        equipment_id (Union[None, Unset, str]):
    """

    measurement_tool_id: Union[None, Unset, int] = UNSET
    last_service_date: Union[None, Unset, datetime.datetime] = UNSET
    next_service_date: Union[None, Unset, datetime.datetime] = UNSET
    calibrated_by: Union[None, Unset, str] = UNSET
    certificate_number: Union[None, Unset, str] = UNSET
    tool_name: Union[None, Unset, str] = UNSET
    tool_description: Union[None, Unset, str] = UNSET
    manufacturer: Union[None, Unset, str] = UNSET
    manufacturer_part_number: Union[None, Unset, str] = UNSET
    serial_number: Union[None, Unset, str] = UNSET
    asset_tag: Union[None, Unset, str] = UNSET
    asset_user: Union[None, Unset, str] = UNSET
    equipment_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measurement_tool_id = self.measurement_tool_id

        last_service_date: Union[None, Unset, str]
        if isinstance(self.last_service_date, Unset):
            last_service_date = UNSET
        elif isinstance(self.last_service_date, datetime.datetime):
            last_service_date = self.last_service_date.isoformat()
        else:
            last_service_date = self.last_service_date

        next_service_date: Union[None, Unset, str]
        if isinstance(self.next_service_date, Unset):
            next_service_date = UNSET
        elif isinstance(self.next_service_date, datetime.datetime):
            next_service_date = self.next_service_date.isoformat()
        else:
            next_service_date = self.next_service_date

        calibrated_by = self.calibrated_by

        certificate_number = self.certificate_number

        tool_name = self.tool_name

        tool_description = self.tool_description

        manufacturer = self.manufacturer

        manufacturer_part_number = self.manufacturer_part_number

        serial_number = self.serial_number

        asset_tag = self.asset_tag

        asset_user = self.asset_user

        equipment_id = self.equipment_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measurement_tool_id is not UNSET:
            field_dict["MeasurementToolId"] = measurement_tool_id
        if last_service_date is not UNSET:
            field_dict["LastServiceDate"] = last_service_date
        if next_service_date is not UNSET:
            field_dict["NextServiceDate"] = next_service_date
        if calibrated_by is not UNSET:
            field_dict["CalibratedBy"] = calibrated_by
        if certificate_number is not UNSET:
            field_dict["CertificateNumber"] = certificate_number
        if tool_name is not UNSET:
            field_dict["ToolName"] = tool_name
        if tool_description is not UNSET:
            field_dict["ToolDescription"] = tool_description
        if manufacturer is not UNSET:
            field_dict["Manufacturer"] = manufacturer
        if manufacturer_part_number is not UNSET:
            field_dict["ManufacturerPartNumber"] = manufacturer_part_number
        if serial_number is not UNSET:
            field_dict["SerialNumber"] = serial_number
        if asset_tag is not UNSET:
            field_dict["AssetTag"] = asset_tag
        if asset_user is not UNSET:
            field_dict["AssetUser"] = asset_user
        if equipment_id is not UNSET:
            field_dict["EquipmentId"] = equipment_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        measurement_tool_id = d.pop("MeasurementToolId", UNSET)

        def _parse_last_service_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_service_date_type_0 = isoparse(data)

                return last_service_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_service_date = _parse_last_service_date(d.pop("LastServiceDate", UNSET))

        def _parse_next_service_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_service_date_type_0 = isoparse(data)

                return next_service_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        next_service_date = _parse_next_service_date(d.pop("NextServiceDate", UNSET))

        calibrated_by = d.pop("CalibratedBy", UNSET)

        certificate_number = d.pop("CertificateNumber", UNSET)

        tool_name = d.pop("ToolName", UNSET)

        tool_description = d.pop("ToolDescription", UNSET)

        manufacturer = d.pop("Manufacturer", UNSET)

        manufacturer_part_number = d.pop("ManufacturerPartNumber", UNSET)

        serial_number = d.pop("SerialNumber", UNSET)

        asset_tag = d.pop("AssetTag", UNSET)

        asset_user = d.pop("AssetUser", UNSET)

        equipment_id = d.pop("EquipmentId", UNSET)

        qualer_api_models_measurements_to_update_measurement_tool_response_model = cls(
            measurement_tool_id=measurement_tool_id,
            last_service_date=last_service_date,
            next_service_date=next_service_date,
            calibrated_by=calibrated_by,
            certificate_number=certificate_number,
            tool_name=tool_name,
            tool_description=tool_description,
            manufacturer=manufacturer,
            manufacturer_part_number=manufacturer_part_number,
            serial_number=serial_number,
            asset_tag=asset_tag,
            asset_user=asset_user,
            equipment_id=equipment_id,
        )

        qualer_api_models_measurements_to_update_measurement_tool_response_model.additional_properties = (
            d
        )
        return qualer_api_models_measurements_to_update_measurement_tool_response_model

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
