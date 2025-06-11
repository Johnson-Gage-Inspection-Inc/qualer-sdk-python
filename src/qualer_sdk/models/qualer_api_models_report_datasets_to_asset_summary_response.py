import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsReportDatasetsToAssetSummaryResponse")


@_attrs_define
class QualerApiModelsReportDatasetsToAssetSummaryResponse:
    """
    Attributes:
        service_order_number (Union[Unset, int]):
        service_order_id (Union[Unset, int]):
        service_order_item_id (Union[Unset, int]):
        custom_order_number (Union[Unset, str]):
        order_item_number (Union[Unset, int]):
        is_limited (Union[Unset, bool]):
        certificate_number (Union[Unset, str]):
        serial_number (Union[Unset, str]):
        next_service_date (Union[Unset, datetime.datetime]):
        service_date (Union[Unset, datetime.datetime]):
        part_number (Union[Unset, str]):
        display_part_number (Union[Unset, str]):
        asset_tag (Union[Unset, str]):
        asset_user (Union[Unset, str]):
        asset_name (Union[Unset, str]):
        equipment_id (Union[Unset, str]):
        legacy_identifier (Union[Unset, str]):
        asset_description (Union[Unset, str]):
        class_ (Union[Unset, str]):
        condition (Union[Unset, str]):
        criticality (Union[Unset, str]):
        asset_pool (Union[Unset, str]):
        room (Union[Unset, str]):
        station (Union[Unset, str]):
        service_notes (Union[Unset, str]):
        service_level (Union[Unset, str]):
        service_level_code (Union[Unset, str]):
        next_service_level (Union[Unset, str]):
        next_service_level_code (Union[Unset, str]):
        asset_id (Union[Unset, int]):
        result_status (Union[Unset, int]):
        serial_number_change (Union[Unset, str]):
        provider_technician (Union[Unset, str]):
        provider_technician_alias (Union[Unset, str]):
        provider_phone (Union[Unset, str]):
        provider_company (Union[Unset, str]):
        qr_code (Union[Unset, str]):
        bar_code (Union[Unset, str]):
        bar_code_string (Union[Unset, str]):
        owner_company_id (Union[Unset, int]):
        owner_company_name (Union[Unset, str]):
        as_found_result (Union[Unset, int]):
        as_left_result (Union[Unset, int]):
        asset_tag_change (Union[Unset, str]):
        asset_user_change (Union[Unset, str]):
        due_date (Union[Unset, datetime.datetime]):
        parts_charge (Union[Unset, float]):
        parts_charge_before_discount (Union[Unset, float]):
        service_charge (Union[Unset, float]):
        repairs_charge (Union[Unset, float]):
        segment_name (Union[Unset, str]):
        schedule_name (Union[Unset, str]):
        next_segment_name (Union[Unset, str]):
        client_id (Union[Unset, int]):
        interval_length (Union[Unset, int]):
        interval_cycle (Union[Unset, str]):
    """

    service_order_number: Union[Unset, int] = UNSET
    service_order_id: Union[Unset, int] = UNSET
    service_order_item_id: Union[Unset, int] = UNSET
    custom_order_number: Union[Unset, str] = UNSET
    order_item_number: Union[Unset, int] = UNSET
    is_limited: Union[Unset, bool] = UNSET
    certificate_number: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    next_service_date: Union[Unset, datetime.datetime] = UNSET
    service_date: Union[Unset, datetime.datetime] = UNSET
    part_number: Union[Unset, str] = UNSET
    display_part_number: Union[Unset, str] = UNSET
    asset_tag: Union[Unset, str] = UNSET
    asset_user: Union[Unset, str] = UNSET
    asset_name: Union[Unset, str] = UNSET
    equipment_id: Union[Unset, str] = UNSET
    legacy_identifier: Union[Unset, str] = UNSET
    asset_description: Union[Unset, str] = UNSET
    class_: Union[Unset, str] = UNSET
    condition: Union[Unset, str] = UNSET
    criticality: Union[Unset, str] = UNSET
    asset_pool: Union[Unset, str] = UNSET
    room: Union[Unset, str] = UNSET
    station: Union[Unset, str] = UNSET
    service_notes: Union[Unset, str] = UNSET
    service_level: Union[Unset, str] = UNSET
    service_level_code: Union[Unset, str] = UNSET
    next_service_level: Union[Unset, str] = UNSET
    next_service_level_code: Union[Unset, str] = UNSET
    asset_id: Union[Unset, int] = UNSET
    result_status: Union[Unset, int] = UNSET
    serial_number_change: Union[Unset, str] = UNSET
    provider_technician: Union[Unset, str] = UNSET
    provider_technician_alias: Union[Unset, str] = UNSET
    provider_phone: Union[Unset, str] = UNSET
    provider_company: Union[Unset, str] = UNSET
    qr_code: Union[Unset, str] = UNSET
    bar_code: Union[Unset, str] = UNSET
    bar_code_string: Union[Unset, str] = UNSET
    owner_company_id: Union[Unset, int] = UNSET
    owner_company_name: Union[Unset, str] = UNSET
    as_found_result: Union[Unset, int] = UNSET
    as_left_result: Union[Unset, int] = UNSET
    asset_tag_change: Union[Unset, str] = UNSET
    asset_user_change: Union[Unset, str] = UNSET
    due_date: Union[Unset, datetime.datetime] = UNSET
    parts_charge: Union[Unset, float] = UNSET
    parts_charge_before_discount: Union[Unset, float] = UNSET
    service_charge: Union[Unset, float] = UNSET
    repairs_charge: Union[Unset, float] = UNSET
    segment_name: Union[Unset, str] = UNSET
    schedule_name: Union[Unset, str] = UNSET
    next_segment_name: Union[Unset, str] = UNSET
    client_id: Union[Unset, int] = UNSET
    interval_length: Union[Unset, int] = UNSET
    interval_cycle: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_order_number = self.service_order_number

        service_order_id = self.service_order_id

        service_order_item_id = self.service_order_item_id

        custom_order_number = self.custom_order_number

        order_item_number = self.order_item_number

        is_limited = self.is_limited

        certificate_number = self.certificate_number

        serial_number = self.serial_number

        next_service_date: Union[Unset, str] = UNSET
        if not isinstance(self.next_service_date, Unset):
            next_service_date = self.next_service_date.isoformat()

        service_date: Union[Unset, str] = UNSET
        if not isinstance(self.service_date, Unset):
            service_date = self.service_date.isoformat()

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

        result_status = self.result_status

        serial_number_change = self.serial_number_change

        provider_technician = self.provider_technician

        provider_technician_alias = self.provider_technician_alias

        provider_phone = self.provider_phone

        provider_company = self.provider_company

        qr_code = self.qr_code

        bar_code = self.bar_code

        bar_code_string = self.bar_code_string

        owner_company_id = self.owner_company_id

        owner_company_name = self.owner_company_name

        as_found_result = self.as_found_result

        as_left_result = self.as_left_result

        asset_tag_change = self.asset_tag_change

        asset_user_change = self.asset_user_change

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        parts_charge = self.parts_charge

        parts_charge_before_discount = self.parts_charge_before_discount

        service_charge = self.service_charge

        repairs_charge = self.repairs_charge

        segment_name = self.segment_name

        schedule_name = self.schedule_name

        next_segment_name = self.next_segment_name

        client_id = self.client_id

        interval_length = self.interval_length

        interval_cycle = self.interval_cycle

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_number is not UNSET:
            field_dict["ServiceOrderNumber"] = service_order_number
        if service_order_id is not UNSET:
            field_dict["ServiceOrderId"] = service_order_id
        if service_order_item_id is not UNSET:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if custom_order_number is not UNSET:
            field_dict["CustomOrderNumber"] = custom_order_number
        if order_item_number is not UNSET:
            field_dict["OrderItemNumber"] = order_item_number
        if is_limited is not UNSET:
            field_dict["IsLimited"] = is_limited
        if certificate_number is not UNSET:
            field_dict["CertificateNumber"] = certificate_number
        if serial_number is not UNSET:
            field_dict["SerialNumber"] = serial_number
        if next_service_date is not UNSET:
            field_dict["NextServiceDate"] = next_service_date
        if service_date is not UNSET:
            field_dict["ServiceDate"] = service_date
        if part_number is not UNSET:
            field_dict["PartNumber"] = part_number
        if display_part_number is not UNSET:
            field_dict["DisplayPartNumber"] = display_part_number
        if asset_tag is not UNSET:
            field_dict["AssetTag"] = asset_tag
        if asset_user is not UNSET:
            field_dict["AssetUser"] = asset_user
        if asset_name is not UNSET:
            field_dict["AssetName"] = asset_name
        if equipment_id is not UNSET:
            field_dict["EquipmentId"] = equipment_id
        if legacy_identifier is not UNSET:
            field_dict["LegacyIdentifier"] = legacy_identifier
        if asset_description is not UNSET:
            field_dict["AssetDescription"] = asset_description
        if class_ is not UNSET:
            field_dict["Class"] = class_
        if condition is not UNSET:
            field_dict["Condition"] = condition
        if criticality is not UNSET:
            field_dict["Criticality"] = criticality
        if asset_pool is not UNSET:
            field_dict["AssetPool"] = asset_pool
        if room is not UNSET:
            field_dict["Room"] = room
        if station is not UNSET:
            field_dict["Station"] = station
        if service_notes is not UNSET:
            field_dict["ServiceNotes"] = service_notes
        if service_level is not UNSET:
            field_dict["ServiceLevel"] = service_level
        if service_level_code is not UNSET:
            field_dict["ServiceLevelCode"] = service_level_code
        if next_service_level is not UNSET:
            field_dict["NextServiceLevel"] = next_service_level
        if next_service_level_code is not UNSET:
            field_dict["NextServiceLevelCode"] = next_service_level_code
        if asset_id is not UNSET:
            field_dict["AssetId"] = asset_id
        if result_status is not UNSET:
            field_dict["ResultStatus"] = result_status
        if serial_number_change is not UNSET:
            field_dict["SerialNumberChange"] = serial_number_change
        if provider_technician is not UNSET:
            field_dict["ProviderTechnician"] = provider_technician
        if provider_technician_alias is not UNSET:
            field_dict["ProviderTechnicianAlias"] = provider_technician_alias
        if provider_phone is not UNSET:
            field_dict["ProviderPhone"] = provider_phone
        if provider_company is not UNSET:
            field_dict["ProviderCompany"] = provider_company
        if qr_code is not UNSET:
            field_dict["QrCode"] = qr_code
        if bar_code is not UNSET:
            field_dict["BarCode"] = bar_code
        if bar_code_string is not UNSET:
            field_dict["BarCodeString"] = bar_code_string
        if owner_company_id is not UNSET:
            field_dict["OwnerCompanyId"] = owner_company_id
        if owner_company_name is not UNSET:
            field_dict["OwnerCompanyName"] = owner_company_name
        if as_found_result is not UNSET:
            field_dict["AsFoundResult"] = as_found_result
        if as_left_result is not UNSET:
            field_dict["AsLeftResult"] = as_left_result
        if asset_tag_change is not UNSET:
            field_dict["AssetTagChange"] = asset_tag_change
        if asset_user_change is not UNSET:
            field_dict["AssetUserChange"] = asset_user_change
        if due_date is not UNSET:
            field_dict["DueDate"] = due_date
        if parts_charge is not UNSET:
            field_dict["PartsCharge"] = parts_charge
        if parts_charge_before_discount is not UNSET:
            field_dict["PartsChargeBeforeDiscount"] = parts_charge_before_discount
        if service_charge is not UNSET:
            field_dict["ServiceCharge"] = service_charge
        if repairs_charge is not UNSET:
            field_dict["RepairsCharge"] = repairs_charge
        if segment_name is not UNSET:
            field_dict["SegmentName"] = segment_name
        if schedule_name is not UNSET:
            field_dict["ScheduleName"] = schedule_name
        if next_segment_name is not UNSET:
            field_dict["NextSegmentName"] = next_segment_name
        if client_id is not UNSET:
            field_dict["ClientId"] = client_id
        if interval_length is not UNSET:
            field_dict["IntervalLength"] = interval_length
        if interval_cycle is not UNSET:
            field_dict["IntervalCycle"] = interval_cycle

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_number = d.pop("ServiceOrderNumber", UNSET)

        service_order_id = d.pop("ServiceOrderId", UNSET)

        service_order_item_id = d.pop("ServiceOrderItemId", UNSET)

        custom_order_number = d.pop("CustomOrderNumber", UNSET)

        order_item_number = d.pop("OrderItemNumber", UNSET)

        is_limited = d.pop("IsLimited", UNSET)

        certificate_number = d.pop("CertificateNumber", UNSET)

        serial_number = d.pop("SerialNumber", UNSET)

        _next_service_date = d.pop("NextServiceDate", UNSET)
        next_service_date: Union[Unset, datetime.datetime]
        if isinstance(_next_service_date, Unset):
            next_service_date = UNSET
        else:
            next_service_date = isoparse(_next_service_date)

        _service_date = d.pop("ServiceDate", UNSET)
        service_date: Union[Unset, datetime.datetime]
        if isinstance(_service_date, Unset):
            service_date = UNSET
        else:
            service_date = isoparse(_service_date)

        part_number = d.pop("PartNumber", UNSET)

        display_part_number = d.pop("DisplayPartNumber", UNSET)

        asset_tag = d.pop("AssetTag", UNSET)

        asset_user = d.pop("AssetUser", UNSET)

        asset_name = d.pop("AssetName", UNSET)

        equipment_id = d.pop("EquipmentId", UNSET)

        legacy_identifier = d.pop("LegacyIdentifier", UNSET)

        asset_description = d.pop("AssetDescription", UNSET)

        class_ = d.pop("Class", UNSET)

        condition = d.pop("Condition", UNSET)

        criticality = d.pop("Criticality", UNSET)

        asset_pool = d.pop("AssetPool", UNSET)

        room = d.pop("Room", UNSET)

        station = d.pop("Station", UNSET)

        service_notes = d.pop("ServiceNotes", UNSET)

        service_level = d.pop("ServiceLevel", UNSET)

        service_level_code = d.pop("ServiceLevelCode", UNSET)

        next_service_level = d.pop("NextServiceLevel", UNSET)

        next_service_level_code = d.pop("NextServiceLevelCode", UNSET)

        asset_id = d.pop("AssetId", UNSET)

        result_status = d.pop("ResultStatus", UNSET)

        serial_number_change = d.pop("SerialNumberChange", UNSET)

        provider_technician = d.pop("ProviderTechnician", UNSET)

        provider_technician_alias = d.pop("ProviderTechnicianAlias", UNSET)

        provider_phone = d.pop("ProviderPhone", UNSET)

        provider_company = d.pop("ProviderCompany", UNSET)

        qr_code = d.pop("QrCode", UNSET)

        bar_code = d.pop("BarCode", UNSET)

        bar_code_string = d.pop("BarCodeString", UNSET)

        owner_company_id = d.pop("OwnerCompanyId", UNSET)

        owner_company_name = d.pop("OwnerCompanyName", UNSET)

        as_found_result = d.pop("AsFoundResult", UNSET)

        as_left_result = d.pop("AsLeftResult", UNSET)

        asset_tag_change = d.pop("AssetTagChange", UNSET)

        asset_user_change = d.pop("AssetUserChange", UNSET)

        _due_date = d.pop("DueDate", UNSET)
        due_date: Union[Unset, datetime.datetime]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        parts_charge = d.pop("PartsCharge", UNSET)

        parts_charge_before_discount = d.pop("PartsChargeBeforeDiscount", UNSET)

        service_charge = d.pop("ServiceCharge", UNSET)

        repairs_charge = d.pop("RepairsCharge", UNSET)

        segment_name = d.pop("SegmentName", UNSET)

        schedule_name = d.pop("ScheduleName", UNSET)

        next_segment_name = d.pop("NextSegmentName", UNSET)

        client_id = d.pop("ClientId", UNSET)

        interval_length = d.pop("IntervalLength", UNSET)

        interval_cycle = d.pop("IntervalCycle", UNSET)

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

        qualer_api_models_report_datasets_to_asset_summary_response.additional_properties = (
            d
        )
        return qualer_api_models_report_datasets_to_asset_summary_response

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
