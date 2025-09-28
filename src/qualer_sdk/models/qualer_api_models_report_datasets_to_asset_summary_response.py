import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ReportDatasetsToAssetSummaryResponse")


@_attrs_define
class ReportDatasetsToAssetSummaryResponse:
    """
    Attributes:
        service_order_number (Optional[int]):
        service_order_id (Optional[int]):
        service_order_item_id (Optional[int]):
        custom_order_number (Optional[str]):
        order_item_number (Optional[int]):
        is_limited (Optional[bool]):
        certificate_number (Optional[str]):
        serial_number (Optional[str]):
        next_service_date (Optional[datetime.datetime]):
        service_date (Optional[datetime.datetime]):
        part_number (Optional[str]):
        display_part_number (Optional[str]):
        asset_tag (Optional[str]):
        asset_user (Optional[str]):
        asset_name (Optional[str]):
        equipment_id (Optional[str]):
        legacy_identifier (Optional[str]):
        asset_description (Optional[str]):
        class_ (Optional[str]):
        condition (Optional[str]):
        criticality (Optional[str]):
        asset_pool (Optional[str]):
        room (Optional[str]):
        station (Optional[str]):
        service_notes (Optional[str]):
        service_level (Optional[str]):
        service_level_code (Optional[str]):
        next_service_level (Optional[str]):
        next_service_level_code (Optional[str]):
        asset_id (Optional[int]):
        result_status (Optional[int]):
        serial_number_change (Optional[str]):
        provider_technician (Optional[str]):
        provider_technician_alias (Optional[str]):
        provider_phone (Optional[str]):
        provider_company (Optional[str]):
        qr_code (Optional[str]):
        bar_code (Optional[str]):
        bar_code_string (Optional[str]):
        owner_company_id (Optional[int]):
        owner_company_name (Optional[str]):
        as_found_result (Optional[int]):
        as_left_result (Optional[int]):
        asset_tag_change (Optional[str]):
        asset_user_change (Optional[str]):
        due_date (Optional[datetime.datetime]):
        parts_charge (Optional[float]):
        parts_charge_before_discount (Optional[float]):
        service_charge (Optional[float]):
        repairs_charge (Optional[float]):
        segment_name (Optional[str]):
        schedule_name (Optional[str]):
        next_segment_name (Optional[str]):
        client_id (Optional[int]):
        interval_length (Optional[int]):
        interval_cycle (Optional[str]):
    """

    service_order_number: Optional[int] = None
    service_order_id: Optional[int] = None
    service_order_item_id: Optional[int] = None
    custom_order_number: Optional[str] = None
    order_item_number: Optional[int] = None
    is_limited: Optional[bool] = None
    certificate_number: Optional[str] = None
    serial_number: Optional[str] = None
    next_service_date: Optional[datetime.datetime] = None
    service_date: Optional[datetime.datetime] = None
    part_number: Optional[str] = None
    display_part_number: Optional[str] = None
    asset_tag: Optional[str] = None
    asset_user: Optional[str] = None
    asset_name: Optional[str] = None
    equipment_id: Optional[str] = None
    legacy_identifier: Optional[str] = None
    asset_description: Optional[str] = None
    class_: Optional[str] = None
    condition: Optional[str] = None
    criticality: Optional[str] = None
    asset_pool: Optional[str] = None
    room: Optional[str] = None
    station: Optional[str] = None
    service_notes: Optional[str] = None
    service_level: Optional[str] = None
    service_level_code: Optional[str] = None
    next_service_level: Optional[str] = None
    next_service_level_code: Optional[str] = None
    asset_id: Optional[int] = None
    result_status: Optional[int] = None
    serial_number_change: Optional[str] = None
    provider_technician: Optional[str] = None
    provider_technician_alias: Optional[str] = None
    provider_phone: Optional[str] = None
    provider_company: Optional[str] = None
    qr_code: Optional[str] = None
    bar_code: Optional[str] = None
    bar_code_string: Optional[str] = None
    owner_company_id: Optional[int] = None
    owner_company_name: Optional[str] = None
    as_found_result: Optional[int] = None
    as_left_result: Optional[int] = None
    asset_tag_change: Optional[str] = None
    asset_user_change: Optional[str] = None
    due_date: Optional[datetime.datetime] = None
    parts_charge: Optional[float] = None
    parts_charge_before_discount: Optional[float] = None
    service_charge: Optional[float] = None
    repairs_charge: Optional[float] = None
    segment_name: Optional[str] = None
    schedule_name: Optional[str] = None
    next_segment_name: Optional[str] = None
    client_id: Optional[int] = None
    interval_length: Optional[int] = None
    interval_cycle: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_order_number = self.service_order_number
        service_order_id = self.service_order_id
        service_order_item_id = self.service_order_item_id
        custom_order_number = self.custom_order_number
        order_item_number = self.order_item_number
        is_limited = self.is_limited
        certificate_number = self.certificate_number
        serial_number = self.serial_number
        next_service_date = self.next_service_date.isoformat() if self.next_service_date else None
        service_date = self.service_date.isoformat() if self.service_date else None
        part_number = self.part_number
        display_part_number = self.display_part_number
        asset_tag = self.asset_tag
        asset_user = self.asset_user
        asset_name = self.asset_name
        equipment_id = self.equipment_id
        legacy_identifier = self.legacy_identifier
        asset_description = self.asset_description
        class_ = self.class_
        condition = self.condition
        criticality = self.criticality
        asset_pool = self.asset_pool
        room = self.room
        station = self.station
        service_notes = self.service_notes
        service_level = self.service_level
        service_level_code = self.service_level_code
        next_service_level = self.next_service_level
        next_service_level_code = self.next_service_level_code
        asset_id = self.asset_id
        result_status: Optional[int]
        if not self.result_status:
            result_status = None
        else:
            result_status: Optional[str]
            if not self.result_status:
                result_status = None
            else:
                result_status = self.result_status
        serial_number_change = self.serial_number_change
        provider_technician = self.provider_technician
        provider_technician_alias = self.provider_technician_alias
        provider_phone = self.provider_phone
        provider_company = self.provider_company
        qr_code = self.qr_code
        bar_code = self.bar_code
        bar_code_string = self.bar_code_string
        owner_company_id: Optional[int]
        if not self.owner_company_id:
            owner_company_id = None
        else:
            owner_company_id = self.owner_company_id
        owner_company_name = self.owner_company_name
        as_found_result: Optional[int]
        if not self.as_found_result:
            as_found_result = None
        else:
            as_found_result: Optional[str]
            if not self.as_found_result:
                as_found_result = None
            else:
                as_found_result = self.as_found_result
        as_left_result: Optional[int]
        if not self.as_left_result:
            as_left_result = None
        else:
            as_left_result: Optional[str]
            if not self.as_left_result:
                as_left_result = None
            else:
                as_left_result = self.as_left_result
        asset_tag_change = self.asset_tag_change
        asset_user_change = self.asset_user_change
        due_date = self.due_date.isoformat() if self.due_date else None
        parts_charge: Optional[float]
        if not self.parts_charge:
            parts_charge = None
        else:
            parts_charge = self.parts_charge
        parts_charge_before_discount: Optional[float]
        if not self.parts_charge_before_discount:
            parts_charge_before_discount = None
        else:
            parts_charge_before_discount = self.parts_charge_before_discount
        service_charge: Optional[float]
        if not self.service_charge:
            service_charge = None
        else:
            service_charge = self.service_charge
        repairs_charge: Optional[float]
        if not self.repairs_charge:
            repairs_charge = None
        else:
            repairs_charge = self.repairs_charge
        segment_name = self.segment_name
        schedule_name = self.schedule_name
        next_segment_name = self.next_segment_name
        client_id: Optional[int]
        if not self.client_id:
            client_id = None
        else:
            client_id = self.client_id
        interval_length: Optional[int]
        if not self.interval_length:
            interval_length = None
        else:
            interval_length = self.interval_length
        interval_cycle = self.interval_cycle
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_number is not None:
            field_dict["ServiceOrderNumber"] = service_order_number
        if service_order_id is not None:
            field_dict["ServiceOrderId"] = service_order_id
        if service_order_item_id is not None:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if custom_order_number is not None:
            field_dict["CustomOrderNumber"] = custom_order_number
        if order_item_number is not None:
            field_dict["OrderItemNumber"] = order_item_number
        if is_limited is not None:
            field_dict["IsLimited"] = is_limited
        if certificate_number is not None:
            field_dict["CertificateNumber"] = certificate_number
        if serial_number is not None:
            field_dict["SerialNumber"] = serial_number
        if next_service_date is not None:
            field_dict["NextServiceDate"] = next_service_date
        if service_date is not None:
            field_dict["ServiceDate"] = service_date
        if part_number is not None:
            field_dict["PartNumber"] = part_number
        if display_part_number is not None:
            field_dict["DisplayPartNumber"] = display_part_number
        if asset_tag is not None:
            field_dict["AssetTag"] = asset_tag
        if asset_user is not None:
            field_dict["AssetUser"] = asset_user
        if asset_name is not None:
            field_dict["AssetName"] = asset_name
        if equipment_id is not None:
            field_dict["EquipmentId"] = equipment_id
        if legacy_identifier is not None:
            field_dict["LegacyIdentifier"] = legacy_identifier
        if asset_description is not None:
            field_dict["AssetDescription"] = asset_description
        if class_ is not None:
            field_dict["Class"] = class_
        if condition is not None:
            field_dict["Condition"] = condition
        if criticality is not None:
            field_dict["Criticality"] = criticality
        if asset_pool is not None:
            field_dict["AssetPool"] = asset_pool
        if room is not None:
            field_dict["Room"] = room
        if station is not None:
            field_dict["Station"] = station
        if service_notes is not None:
            field_dict["ServiceNotes"] = service_notes
        if service_level is not None:
            field_dict["ServiceLevel"] = service_level
        if service_level_code is not None:
            field_dict["ServiceLevelCode"] = service_level_code
        if next_service_level is not None:
            field_dict["NextServiceLevel"] = next_service_level
        if next_service_level_code is not None:
            field_dict["NextServiceLevelCode"] = next_service_level_code
        if asset_id is not None:
            field_dict["AssetId"] = asset_id
        if result_status is not None:
            field_dict["ResultStatus"] = result_status
        if serial_number_change is not None:
            field_dict["SerialNumberChange"] = serial_number_change
        if provider_technician is not None:
            field_dict["ProviderTechnician"] = provider_technician
        if provider_technician_alias is not None:
            field_dict["ProviderTechnicianAlias"] = provider_technician_alias
        if provider_phone is not None:
            field_dict["ProviderPhone"] = provider_phone
        if provider_company is not None:
            field_dict["ProviderCompany"] = provider_company
        if qr_code is not None:
            field_dict["QrCode"] = qr_code
        if bar_code is not None:
            field_dict["BarCode"] = bar_code
        if bar_code_string is not None:
            field_dict["BarCodeString"] = bar_code_string
        if owner_company_id is not None:
            field_dict["OwnerCompanyId"] = owner_company_id
        if owner_company_name is not None:
            field_dict["OwnerCompanyName"] = owner_company_name
        if as_found_result is not None:
            field_dict["AsFoundResult"] = as_found_result
        if as_left_result is not None:
            field_dict["AsLeftResult"] = as_left_result
        if asset_tag_change is not None:
            field_dict["AssetTagChange"] = asset_tag_change
        if asset_user_change is not None:
            field_dict["AssetUserChange"] = asset_user_change
        if due_date is not None:
            field_dict["DueDate"] = due_date
        if parts_charge is not None:
            field_dict["PartsCharge"] = parts_charge
        if parts_charge_before_discount is not None:
            field_dict["PartsChargeBeforeDiscount"] = parts_charge_before_discount
        if service_charge is not None:
            field_dict["ServiceCharge"] = service_charge
        if repairs_charge is not None:
            field_dict["RepairsCharge"] = repairs_charge
        if segment_name is not None:
            field_dict["SegmentName"] = segment_name
        if schedule_name is not None:
            field_dict["ScheduleName"] = schedule_name
        if next_segment_name is not None:
            field_dict["NextSegmentName"] = next_segment_name
        if client_id is not None:
            field_dict["ClientId"] = client_id
        if interval_length is not None:
            field_dict["IntervalLength"] = interval_length
        if interval_cycle is not None:
            field_dict["IntervalCycle"] = interval_cycle
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_number = d.pop("ServiceOrderNumber", None)
        service_order_id = d.pop("ServiceOrderId", None)
        service_order_item_id = d.pop("ServiceOrderItemId", None)
        custom_order_number = d.pop("CustomOrderNumber", None)
        order_item_number = d.pop("OrderItemNumber", None)
        is_limited = d.pop("IsLimited", None)
        certificate_number = d.pop("CertificateNumber", None)
        serial_number = d.pop("SerialNumber", None)
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
        def _parse_service_date(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                service_date_type_0 = isoparse(data)
                return service_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)
        service_date = _parse_service_date(d.pop("ServiceDate", None))
        part_number = d.pop("PartNumber", None)
        display_part_number = d.pop("DisplayPartNumber", None)
        asset_tag = d.pop("AssetTag", None)
        asset_user = d.pop("AssetUser", None)
        asset_name = d.pop("AssetName", None)
        equipment_id = d.pop("EquipmentId", None)
        legacy_identifier = d.pop("LegacyIdentifier", None)
        asset_description = d.pop("AssetDescription", None)
        class_ = d.pop("Class", None)
        condition = d.pop("Condition", None)
        criticality = d.pop("Criticality", None)
        asset_pool = d.pop("AssetPool", None)
        room = d.pop("Room", None)
        station = d.pop("Station", None)
        service_notes = d.pop("ServiceNotes", None)
        service_level = d.pop("ServiceLevel", None)
        service_level_code = d.pop("ServiceLevelCode", None)
        next_service_level = d.pop("NextServiceLevel", None)
        next_service_level_code = d.pop("NextServiceLevelCode", None)
        asset_id = d.pop("AssetId", None)
        def _parse_result_status(data: object) -> Optional[int]:
            if not data:
                return None
            return cast(Optional[int], data)
        result_status = _parse_result_status(d.pop("ResultStatus", None))
        def _parse_serial_number_change(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        serial_number_change = _parse_serial_number_change(d.pop("SerialNumberChange", None))
        def _parse_provider_technician(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        provider_technician = _parse_provider_technician(d.pop("ProviderTechnician", None))
        def _parse_provider_technician_alias(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        provider_technician_alias = _parse_provider_technician_alias(
            d.pop("ProviderTechnicianAlias", None)
        )
        def _parse_provider_phone(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        provider_phone = _parse_provider_phone(d.pop("ProviderPhone", None))
        def _parse_provider_company(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        provider_company = _parse_provider_company(d.pop("ProviderCompany", None))
        def _parse_qr_code(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        qr_code = _parse_qr_code(d.pop("QrCode", None))
        def _parse_bar_code(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        bar_code = _parse_bar_code(d.pop("BarCode", None))
        def _parse_bar_code_string(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        bar_code_string = _parse_bar_code_string(d.pop("BarCodeString", None))
        def _parse_owner_company_id(data: object) -> Optional[int]:
            if not data:
                return None
            return cast(Optional[int], data)
        owner_company_id = _parse_owner_company_id(d.pop("OwnerCompanyId", None))
        def _parse_owner_company_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        owner_company_name = _parse_owner_company_name(d.pop("OwnerCompanyName", None))
        def _parse_as_found_result(data: object) -> Optional[int]:
            if not data:
                return None
            return cast(Optional[int], data)
        as_found_result = _parse_as_found_result(d.pop("AsFoundResult", None))
        def _parse_as_left_result(data: object) -> Optional[int]:
            if not data:
                return None
            return cast(Optional[int], data)
        as_left_result = _parse_as_left_result(d.pop("AsLeftResult", None))
        def _parse_asset_tag_change(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        asset_tag_change = _parse_asset_tag_change(d.pop("AssetTagChange", None))
        def _parse_asset_user_change(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        asset_user_change = _parse_asset_user_change(d.pop("AssetUserChange", None))
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
        def _parse_parts_charge(data: object) -> Optional[float]:
            if not data:
                return None
            return cast(Optional[float], data)
        parts_charge = _parse_parts_charge(d.pop("PartsCharge", None))
        def _parse_parts_charge_before_discount(
            data: object,
        ) -> Optional[float]:
            if not data:
                return None
            return cast(Optional[float], data)
        parts_charge_before_discount = _parse_parts_charge_before_discount(
            d.pop("PartsChargeBeforeDiscount", None)
        )
        def _parse_service_charge(data: object) -> Optional[float]:
            if not data:
                return None
            return cast(Optional[float], data)
        service_charge = _parse_service_charge(d.pop("ServiceCharge", None))
        def _parse_repairs_charge(data: object) -> Optional[float]:
            if not data:
                return None
            return cast(Optional[float], data)
        repairs_charge = _parse_repairs_charge(d.pop("RepairsCharge", None))
        def _parse_segment_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        segment_name = _parse_segment_name(d.pop("SegmentName", None))
        def _parse_schedule_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        schedule_name = _parse_schedule_name(d.pop("ScheduleName", None))
        def _parse_next_segment_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        next_segment_name = _parse_next_segment_name(d.pop("NextSegmentName", None))
        def _parse_client_id(data: object) -> Optional[int]:
            if not data:
                return None
            return cast(Optional[int], data)
        client_id = _parse_client_id(d.pop("ClientId", None))
        def _parse_interval_length(data: object) -> Optional[int]:
            if not data:
                return None
            return cast(Optional[int], data)
        interval_length = _parse_interval_length(d.pop("IntervalLength", None))
        def _parse_interval_cycle(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        interval_cycle = _parse_interval_cycle(d.pop("IntervalCycle", None))
        qualer_api_models_report_datasets_to_asset_summary_response = cls(
            service_order_number=service_order_number,
            service_order_id=service_order_id,
            service_order_item_id=service_order_item_id,
            custom_order_number=custom_order_number,
            order_item_number=order_item_number,
            is_limited=is_limited,
            certificate_number=certificate_number,
            serial_number=serial_number,
            next_service_date=next_service_date,
            service_date=service_date,
            part_number=part_number,
            display_part_number=display_part_number,
            asset_tag=asset_tag,
            asset_user=asset_user,
            asset_name=asset_name,
            equipment_id=equipment_id,
            legacy_identifier=legacy_identifier,
            asset_description=asset_description,
            class_=class_,
            condition=condition,
            criticality=criticality,
            asset_pool=asset_pool,
            room=room,
            station=station,
            service_notes=service_notes,
            service_level=service_level,
            service_level_code=service_level_code,
            next_service_level=next_service_level,
            next_service_level_code=next_service_level_code,
            asset_id=asset_id,
            result_status=result_status,
            serial_number_change=serial_number_change,
            provider_technician=provider_technician,
            provider_technician_alias=provider_technician_alias,
            provider_phone=provider_phone,
            provider_company=provider_company,
            qr_code=qr_code,
            bar_code=bar_code,
            bar_code_string=bar_code_string,
            owner_company_id=owner_company_id,
            owner_company_name=owner_company_name,
            as_found_result=as_found_result,
            as_left_result=as_left_result,
            asset_tag_change=asset_tag_change,
            asset_user_change=asset_user_change,
            due_date=due_date,
            parts_charge=parts_charge,
            parts_charge_before_discount=parts_charge_before_discount,
            service_charge=service_charge,
            repairs_charge=repairs_charge,
            segment_name=segment_name,
            schedule_name=schedule_name,
            next_segment_name=next_segment_name,
            client_id=client_id,
            interval_length=interval_length,
            interval_cycle=interval_cycle,
        )
        qualer_api_models_report_datasets_to_asset_summary_response.additional_properties = d
        return qualer_api_models_report_datasets_to_asset_summary_response

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
