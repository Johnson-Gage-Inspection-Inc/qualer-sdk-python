import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar(
    "T",
    bound="MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModelMeasurementToolResponseModel",
)


@_attrs_define
class MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModelMeasurementToolResponseModel:
    """
    Attributes:
        last_service_date (Optional[datetime.datetime]):
        next_service_date (Optional[datetime.datetime]):
        calibrated_by (Optional[str]):
        certificate_number (Optional[str]):
        tool_name (Optional[str]):
        tool_description (Optional[str]):
        manufacturer (Optional[str]):
        manufacturer_part_number (Optional[str]):
        serial_number (Optional[str]):
        asset_tag (Optional[str]):
        asset_user (Optional[str]):
        equipment_id (Optional[str]):
    """

    last_service_date: Optional[datetime.datetime] = None
    next_service_date: Optional[datetime.datetime] = None
    calibrated_by: Optional[str] = None
    certificate_number: Optional[str] = None
    tool_name: Optional[str] = None
    tool_description: Optional[str] = None
    manufacturer: Optional[str] = None
    manufacturer_part_number: Optional[str] = None
    serial_number: Optional[str] = None
    asset_tag: Optional[str] = None
    asset_user: Optional[str] = None
    equipment_id: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        last_service_date = self.last_service_date.isoformat() if self.last_service_date else None
        next_service_date = self.next_service_date.isoformat() if self.next_service_date else None
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
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_service_date is not None:
            field_dict["LastServiceDate"] = last_service_date
        if next_service_date is not None:
            field_dict["NextServiceDate"] = next_service_date
        if calibrated_by is not None:
            field_dict["CalibratedBy"] = calibrated_by
        if certificate_number is not None:
            field_dict["CertificateNumber"] = certificate_number
        if tool_name is not None:
            field_dict["ToolName"] = tool_name
        if tool_description is not None:
            field_dict["ToolDescription"] = tool_description
        if manufacturer is not None:
            field_dict["Manufacturer"] = manufacturer
        if manufacturer_part_number is not None:
            field_dict["ManufacturerPartNumber"] = manufacturer_part_number
        if serial_number is not None:
            field_dict["SerialNumber"] = serial_number
        if asset_tag is not None:
            field_dict["AssetTag"] = asset_tag
        if asset_user is not None:
            field_dict["AssetUser"] = asset_user
        if equipment_id is not None:
            field_dict["EquipmentId"] = equipment_id
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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
        calibrated_by = d.pop("CalibratedBy", None)
        certificate_number = d.pop("CertificateNumber", None)
        tool_name = d.pop("ToolName", None)
        tool_description = d.pop("ToolDescription", None)
        manufacturer = d.pop("Manufacturer", None)
        manufacturer_part_number = d.pop("ManufacturerPartNumber", None)
        serial_number = d.pop("SerialNumber", None)
        asset_tag = d.pop("AssetTag", None)
        asset_user = d.pop("AssetUser", None)
        equipment_id = d.pop("EquipmentId", None)
        qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_measurement_set_response_model_measurement_point_response_model_measurement_tool_response_model = cls(
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
        qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_measurement_set_response_model_measurement_point_response_model_measurement_tool_response_model.additional_properties = (
            d
        )
        return qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_measurement_set_response_model_measurement_point_response_model_measurement_tool_response_model

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
