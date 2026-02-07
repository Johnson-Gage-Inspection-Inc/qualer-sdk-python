import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="AssetServiceRecordsToAssetServiceRecordResponseModel")


@_attrs_define
class AssetServiceRecordsToAssetServiceRecordResponseModel:
    """
    Attributes:
        asset_id (int):
        asset_service_record_id (int):
        service_date (datetime.datetime):
        service_schedule_segment_id (int):
        forward_segment_id (Optional[int]):
        forward_next_service (bool):
        service_order_number (Optional[int]):
        custom_order_number (str):
        order_item_number (Optional[int]):
        certificate_number (str):
        result_status (str):
        as_found_result (str):
        as_left_result (str):
        serial_number (str):
        asset_tag (str):
        asset_user (Optional[str]):
        asset_tag_change (Optional[str]):
        asset_user_change (Optional[str]):
        service_notes (Optional[str]):
        serial_number_change (Optional[str]):
        due_date (Optional[datetime.datetime]):
        next_service_date (Optional[datetime.datetime]):
        provider_technician (Optional[str]):
        provider_phone (Optional[str]):
        provider_company (Optional[str]):
        service_level (Optional[str]):
        service_level_code (Optional[str]):
        next_service_level (Optional[str]):
        next_service_level_code (Optional[str]):
        asset_name (str):
        asset_description (str):
        parts_charge (Optional[float]):
        parts_charge_before_discount (Optional[float]):
        service_charge (Optional[float]):
        repairs_charge (Optional[float]):
        guid (UUID):  A unique identifier for the asset service record.
        segment_name (Optional[str]):
        schedule_name (Optional[str]):
    """

    asset_id: int
    asset_service_record_id: int
    service_date: datetime.datetime
    service_schedule_segment_id: int
    forward_next_service: bool
    asset_tag: str
    asset_name: str
    asset_description: str
    guid: UUID
    result_status: str
    serial_number: str
    as_found_result: str
    as_left_result: str
    certificate_number: str
    custom_order_number: str
    forward_segment_id: Optional[int] = None
    service_order_number: Optional[int] = None
    order_item_number: Optional[int] = None
    asset_user: Optional[str] = None
    asset_tag_change: Optional[str] = None
    asset_user_change: Optional[str] = None
    service_notes: Optional[str] = None
    serial_number_change: Optional[str] = None
    due_date: Optional[datetime.datetime] = None
    next_service_date: Optional[datetime.datetime] = None
    provider_technician: Optional[str] = None
    provider_phone: Optional[str] = None
    provider_company: Optional[str] = None
    service_level: Optional[str] = None
    service_level_code: Optional[str] = None
    next_service_level: Optional[str] = None
    next_service_level_code: Optional[str] = None
    parts_charge: Optional[float] = None
    parts_charge_before_discount: Optional[float] = None
    service_charge: Optional[float] = None
    repairs_charge: Optional[float] = None
    segment_name: Optional[str] = None
    schedule_name: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asset_id = self.asset_id
        asset_service_record_id = self.asset_service_record_id
        service_schedule_segment_id = self.service_schedule_segment_id
        forward_segment_id = self.forward_segment_id
        forward_next_service = self.forward_next_service
        service_order_number = self.service_order_number
        custom_order_number = self.custom_order_number
        order_item_number = self.order_item_number
        certificate_number = self.certificate_number
        result_status = self.result_status
        as_found_result = self.as_found_result
        as_left_result = self.as_left_result
        service_date = self.service_date.isoformat()
        serial_number = self.serial_number
        asset_tag = self.asset_tag
        asset_user = self.asset_user
        asset_tag_change = self.asset_tag_change
        asset_user_change = self.asset_user_change
        service_notes = self.service_notes
        serial_number_change = self.serial_number_change
        due_date = self.due_date.isoformat() if self.due_date else None
        next_service_date = self.next_service_date.isoformat() if self.next_service_date else None
        provider_technician = self.provider_technician
        provider_phone = self.provider_phone
        provider_company = self.provider_company
        service_level = self.service_level
        service_level_code = self.service_level_code
        next_service_level = self.next_service_level
        next_service_level_code = self.next_service_level_code
        asset_name = self.asset_name
        asset_description = self.asset_description
        parts_charge = self.parts_charge
        parts_charge_before_discount = self.parts_charge_before_discount
        service_charge = self.service_charge
        repairs_charge = self.repairs_charge
        # Stringify UUIDs to ensure JSON-serializable output
        guid = str(self.guid)
        segment_name = self.segment_name
        schedule_name = self.schedule_name
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        # Required fields — always include them
        field_dict["AssetId"] = asset_id
        field_dict["AssetServiceRecordId"] = asset_service_record_id
        field_dict["ServiceScheduleSegmentId"] = service_schedule_segment_id
        field_dict["ForwardNextService"] = forward_next_service
        field_dict["CustomOrderNumber"] = custom_order_number
        field_dict["CertificateNumber"] = certificate_number
        field_dict["ResultStatus"] = result_status
        field_dict["AsFoundResult"] = as_found_result
        field_dict["AsLeftResult"] = as_left_result
        field_dict["ServiceDate"] = service_date
        field_dict["SerialNumber"] = serial_number
        field_dict["AssetTag"] = asset_tag
        field_dict["AssetName"] = asset_name
        field_dict["AssetDescription"] = asset_description
        # Optional fields — include only when present
        if forward_segment_id is not None:
            field_dict["ForwardSegmentId"] = forward_segment_id
        if service_order_number is not None:
            field_dict["ServiceOrderNumber"] = service_order_number
        if order_item_number is not None:
            field_dict["OrderItemNumber"] = order_item_number
        if asset_user is not None:
            field_dict["AssetUser"] = asset_user
        if asset_tag_change is not None:
            field_dict["AssetTagChange"] = asset_tag_change
        if asset_user_change is not None:
            field_dict["AssetUserChange"] = asset_user_change
        if service_notes is not None:
            field_dict["ServiceNotes"] = service_notes
        if serial_number_change is not None:
            field_dict["SerialNumberChange"] = serial_number_change
        if due_date is not None:
            field_dict["DueDate"] = due_date
        if next_service_date is not None:
            field_dict["NextServiceDate"] = next_service_date
        if provider_technician is not None:
            field_dict["ProviderTechnician"] = provider_technician
        if provider_phone is not None:
            field_dict["ProviderPhone"] = provider_phone
        if provider_company is not None:
            field_dict["ProviderCompany"] = provider_company
        if service_level is not None:
            field_dict["ServiceLevel"] = service_level
        if service_level_code is not None:
            field_dict["ServiceLevelCode"] = service_level_code
        if next_service_level is not None:
            field_dict["NextServiceLevel"] = next_service_level
        if next_service_level_code is not None:
            field_dict["NextServiceLevelCode"] = next_service_level_code
        if parts_charge is not None:
            field_dict["PartsCharge"] = parts_charge
        if parts_charge_before_discount is not None:
            field_dict["PartsChargeBeforeDiscount"] = parts_charge_before_discount
        if service_charge is not None:
            field_dict["ServiceCharge"] = service_charge
        if repairs_charge is not None:
            field_dict["RepairsCharge"] = repairs_charge
        # Guid is required — always include and stringify
        field_dict["Guid"] = guid
        if segment_name is not None:
            field_dict["SegmentName"] = segment_name
        if schedule_name is not None:
            field_dict["ScheduleName"] = schedule_name
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        try:
            asset_id = d.pop("AssetId")
        except KeyError:
            raise ValueError("Missing required field 'AssetId' in input dictionary.")
        try:
            asset_service_record_id = d.pop("AssetServiceRecordId")
        except KeyError:
            raise ValueError("Missing required field 'AssetServiceRecordId' in input dictionary.")
        try:
            service_schedule_segment_id = d.pop("ServiceScheduleSegmentId")
        except KeyError:
            raise ValueError("Missing required field 'ServiceScheduleSegmentId'.")
        forward_segment_id = d.pop("ForwardSegmentId", None)
        try:
            forward_next_service = d.pop("ForwardNextService")
        except KeyError:
            raise ValueError("Missing required field 'ForwardNextService' in input dictionary.")
        service_order_number = d.pop("ServiceOrderNumber", None)
        try:
            custom_order_number = d.pop("CustomOrderNumber")
        except KeyError:
            raise ValueError("Missing required field 'CustomOrderNumber' in input dictionary.")
        order_item_number = d.pop("OrderItemNumber", None)
        try:
            certificate_number = d.pop("CertificateNumber")
        except KeyError:
            raise ValueError("Missing required field 'CertificateNumber' in input dictionary.")

        try:
            raw_result_status = d.pop("ResultStatus")
        except KeyError:
            raise ValueError("Missing required field 'ResultStatus' in input dictionary.")
        result_status = cast(str, raw_result_status)

        try:
            raw_as_found = d.pop("AsFoundResult")
        except KeyError:
            raise ValueError("Missing required field 'AsFoundResult' in input dictionary.")
        as_found_result = cast(str, raw_as_found)

        try:
            raw_as_left = d.pop("AsLeftResult")
        except KeyError:
            raise ValueError("Missing required field 'AsLeftResult' in input dictionary.")
        as_left_result = cast(str, raw_as_left)

        def _parse_service_date(data: object) -> datetime.datetime:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                service_date_type_0 = isoparse(data)
                return service_date_type_0
            except Exception:
                pass
            return cast(datetime.datetime, data)

        try:
            service_date_data = d.pop("ServiceDate")
        except KeyError:
            raise ValueError("Missing required field 'ServiceDate' in input dictionary.")
        service_date = _parse_service_date(service_date_data)
        try:
            serial_number = d.pop("SerialNumber")
        except KeyError:
            raise ValueError("Missing required field 'SerialNumber' in input dictionary.")

        try:
            raw_asset_tag = d.pop("AssetTag")
        except KeyError:
            raise ValueError("Missing required field 'AssetTag' in input dictionary.")
        asset_tag = cast(str, raw_asset_tag)

        asset_user = cast(Optional[str], d.pop("AssetUser", None))

        asset_tag_change = cast(Optional[str], d.pop("AssetTagChange", None))

        asset_user_change = cast(Optional[str], d.pop("AssetUserChange", None))

        service_notes = cast(Optional[str], d.pop("ServiceNotes", None))

        serial_number_change = cast(Optional[str], d.pop("SerialNumberChange", None))

        def _parse_due_date(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_date_type_0 = isoparse(data)
                return due_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        due_date = _parse_due_date(d.pop("DueDate", None))

        def _parse_next_service_date(data: object) -> Optional[datetime.datetime]:
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

        provider_technician = cast(Optional[str], d.pop("ProviderTechnician", None))

        provider_phone = cast(Optional[str], d.pop("ProviderPhone", None))

        provider_company = cast(Optional[str], d.pop("ProviderCompany", None))

        service_level = cast(Optional[str], d.pop("ServiceLevel", None))

        service_level_code = cast(Optional[str], d.pop("ServiceLevelCode", None))

        next_service_level = cast(Optional[str], d.pop("NextServiceLevel", None))

        next_service_level_code = cast(Optional[str], d.pop("NextServiceLevelCode", None))

        try:
            raw_asset_name = d.pop("AssetName")
        except KeyError:
            raise ValueError("Missing required field 'AssetName' in input dictionary.")
        asset_name = cast(str, raw_asset_name)

        try:
            raw_asset_description = d.pop("AssetDescription")
        except KeyError:
            raise ValueError("Missing required field 'AssetDescription' in input dictionary.")
        asset_description = cast(str, raw_asset_description)

        parts_charge = cast(Optional[float], d.pop("PartsCharge", None))

        parts_charge_before_discount = cast(
            Optional[float], d.pop("PartsChargeBeforeDiscount", None)
        )

        service_charge = cast(Optional[float], d.pop("ServiceCharge", None))

        repairs_charge = cast(Optional[float], d.pop("RepairsCharge", None))

        def _parse_guid(data: object) -> Optional[UUID]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                guid_type_0 = UUID(data)
                return guid_type_0
            except Exception:
                return cast(Optional[UUID], data)

        try:
            raw_guid = d.pop("Guid")
        except KeyError:
            raise ValueError("Missing required field 'Guid' in input dictionary.")
        guid = _parse_guid(raw_guid)
        if guid is None:
            raise ValueError("Required field 'Guid' was empty or invalid.")

        segment_name = cast(Optional[str], d.pop("SegmentName", None))

        schedule_name = cast(Optional[str], d.pop("ScheduleName", None))
        model_obj = cls(
            asset_id=asset_id,
            asset_service_record_id=asset_service_record_id,
            service_schedule_segment_id=service_schedule_segment_id,
            forward_segment_id=forward_segment_id,
            forward_next_service=forward_next_service,
            service_order_number=service_order_number,
            custom_order_number=custom_order_number,
            order_item_number=order_item_number,
            certificate_number=certificate_number,
            result_status=result_status,
            as_found_result=as_found_result,
            as_left_result=as_left_result,
            service_date=service_date,
            serial_number=serial_number,
            asset_tag=asset_tag,
            asset_user=asset_user,
            asset_tag_change=asset_tag_change,
            asset_user_change=asset_user_change,
            service_notes=service_notes,
            serial_number_change=serial_number_change,
            due_date=due_date,
            next_service_date=next_service_date,
            provider_technician=provider_technician,
            provider_phone=provider_phone,
            provider_company=provider_company,
            service_level=service_level,
            service_level_code=service_level_code,
            next_service_level=next_service_level,
            next_service_level_code=next_service_level_code,
            asset_name=asset_name,
            asset_description=asset_description,
            parts_charge=parts_charge,
            parts_charge_before_discount=parts_charge_before_discount,
            service_charge=service_charge,
            repairs_charge=repairs_charge,
            guid=guid,
            segment_name=segment_name,
            schedule_name=schedule_name,
        )
        model_obj.additional_properties = d
        return model_obj

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
