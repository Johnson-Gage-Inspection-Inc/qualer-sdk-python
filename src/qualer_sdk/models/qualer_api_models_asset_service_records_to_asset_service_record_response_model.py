import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel"
)


@_attrs_define
class QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel:
    """
    Attributes:
        asset_id (Union[Unset, int]):
        asset_service_record_id (Union[Unset, int]):
        service_schedule_segment_id (Union[Unset, int]):
        forward_segment_id (Union[Unset, int]):
        forward_next_service (Union[Unset, bool]):
        service_order_number (Union[Unset, int]):
        custom_order_number (Union[Unset, str]):
        order_item_number (Union[Unset, int]):
        certificate_number (Union[Unset, str]):
        result_status (Union[Unset, str]):
        as_found_result (Union[Unset, str]):
        as_left_result (Union[Unset, str]):
        service_date (Union[Unset, datetime.datetime]):
        serial_number (Union[Unset, str]):
        asset_tag (Union[Unset, str]):
        asset_user (Union[Unset, str]):
        asset_tag_change (Union[Unset, str]):
        asset_user_change (Union[Unset, str]):
        service_notes (Union[Unset, str]):
        serial_number_change (Union[Unset, str]):
        due_date (Union[Unset, datetime.datetime]):
        next_service_date (Union[Unset, datetime.datetime]):
        provider_technician (Union[Unset, str]):
        provider_phone (Union[Unset, str]):
        provider_company (Union[Unset, str]):
        service_level (Union[Unset, str]):
        service_level_code (Union[Unset, str]):
        next_service_level (Union[Unset, str]):
        next_service_level_code (Union[Unset, str]):
        asset_name (Union[Unset, str]):
        asset_description (Union[Unset, str]):
        parts_charge (Union[Unset, float]):
        parts_charge_before_discount (Union[Unset, float]):
        service_charge (Union[Unset, float]):
        repairs_charge (Union[Unset, float]):
        guid (Union[Unset, UUID]):  Example: 00000000-0000-0000-0000-000000000000.
        segment_name (Union[Unset, str]):
        schedule_name (Union[Unset, str]):
    """

    asset_id: Union[Unset, int] = UNSET
    asset_service_record_id: Union[Unset, int] = UNSET
    service_schedule_segment_id: Union[Unset, int] = UNSET
    forward_segment_id: Union[Unset, int] = UNSET
    forward_next_service: Union[Unset, bool] = UNSET
    service_order_number: Union[Unset, int] = UNSET
    custom_order_number: Union[Unset, str] = UNSET
    order_item_number: Union[Unset, int] = UNSET
    certificate_number: Union[Unset, str] = UNSET
    result_status: Union[Unset, str] = UNSET
    as_found_result: Union[Unset, str] = UNSET
    as_left_result: Union[Unset, str] = UNSET
    service_date: Union[Unset, datetime.datetime] = UNSET
    serial_number: Union[Unset, str] = UNSET
    asset_tag: Union[Unset, str] = UNSET
    asset_user: Union[Unset, str] = UNSET
    asset_tag_change: Union[Unset, str] = UNSET
    asset_user_change: Union[Unset, str] = UNSET
    service_notes: Union[Unset, str] = UNSET
    serial_number_change: Union[Unset, str] = UNSET
    due_date: Union[Unset, datetime.datetime] = UNSET
    next_service_date: Union[Unset, datetime.datetime] = UNSET
    provider_technician: Union[Unset, str] = UNSET
    provider_phone: Union[Unset, str] = UNSET
    provider_company: Union[Unset, str] = UNSET
    service_level: Union[Unset, str] = UNSET
    service_level_code: Union[Unset, str] = UNSET
    next_service_level: Union[Unset, str] = UNSET
    next_service_level_code: Union[Unset, str] = UNSET
    asset_name: Union[Unset, str] = UNSET
    asset_description: Union[Unset, str] = UNSET
    parts_charge: Union[Unset, float] = UNSET
    parts_charge_before_discount: Union[Unset, float] = UNSET
    service_charge: Union[Unset, float] = UNSET
    repairs_charge: Union[Unset, float] = UNSET
    guid: Union[Unset, UUID] = UNSET
    segment_name: Union[Unset, str] = UNSET
    schedule_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        service_date: Union[Unset, str] = UNSET
        if not isinstance(self.service_date, Unset):
            service_date = self.service_date.isoformat()

        serial_number = self.serial_number

        asset_tag = self.asset_tag

        asset_user = self.asset_user

        asset_tag_change = self.asset_tag_change

        asset_user_change = self.asset_user_change

        service_notes = self.service_notes

        serial_number_change = self.serial_number_change

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        next_service_date: Union[Unset, str] = UNSET
        if not isinstance(self.next_service_date, Unset):
            next_service_date = self.next_service_date.isoformat()

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

        guid: Union[Unset, str] = UNSET
        if not isinstance(self.guid, Unset):
            guid = str(self.guid)

        segment_name = self.segment_name

        schedule_name = self.schedule_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["AssetId"] = asset_id
        if asset_service_record_id is not UNSET:
            field_dict["AssetServiceRecordId"] = asset_service_record_id
        if service_schedule_segment_id is not UNSET:
            field_dict["ServiceScheduleSegmentId"] = service_schedule_segment_id
        if forward_segment_id is not UNSET:
            field_dict["ForwardSegmentId"] = forward_segment_id
        if forward_next_service is not UNSET:
            field_dict["ForwardNextService"] = forward_next_service
        if service_order_number is not UNSET:
            field_dict["ServiceOrderNumber"] = service_order_number
        if custom_order_number is not UNSET:
            field_dict["CustomOrderNumber"] = custom_order_number
        if order_item_number is not UNSET:
            field_dict["OrderItemNumber"] = order_item_number
        if certificate_number is not UNSET:
            field_dict["CertificateNumber"] = certificate_number
        if result_status is not UNSET:
            field_dict["ResultStatus"] = result_status
        if as_found_result is not UNSET:
            field_dict["AsFoundResult"] = as_found_result
        if as_left_result is not UNSET:
            field_dict["AsLeftResult"] = as_left_result
        if service_date is not UNSET:
            field_dict["ServiceDate"] = service_date
        if serial_number is not UNSET:
            field_dict["SerialNumber"] = serial_number
        if asset_tag is not UNSET:
            field_dict["AssetTag"] = asset_tag
        if asset_user is not UNSET:
            field_dict["AssetUser"] = asset_user
        if asset_tag_change is not UNSET:
            field_dict["AssetTagChange"] = asset_tag_change
        if asset_user_change is not UNSET:
            field_dict["AssetUserChange"] = asset_user_change
        if service_notes is not UNSET:
            field_dict["ServiceNotes"] = service_notes
        if serial_number_change is not UNSET:
            field_dict["SerialNumberChange"] = serial_number_change
        if due_date is not UNSET:
            field_dict["DueDate"] = due_date
        if next_service_date is not UNSET:
            field_dict["NextServiceDate"] = next_service_date
        if provider_technician is not UNSET:
            field_dict["ProviderTechnician"] = provider_technician
        if provider_phone is not UNSET:
            field_dict["ProviderPhone"] = provider_phone
        if provider_company is not UNSET:
            field_dict["ProviderCompany"] = provider_company
        if service_level is not UNSET:
            field_dict["ServiceLevel"] = service_level
        if service_level_code is not UNSET:
            field_dict["ServiceLevelCode"] = service_level_code
        if next_service_level is not UNSET:
            field_dict["NextServiceLevel"] = next_service_level
        if next_service_level_code is not UNSET:
            field_dict["NextServiceLevelCode"] = next_service_level_code
        if asset_name is not UNSET:
            field_dict["AssetName"] = asset_name
        if asset_description is not UNSET:
            field_dict["AssetDescription"] = asset_description
        if parts_charge is not UNSET:
            field_dict["PartsCharge"] = parts_charge
        if parts_charge_before_discount is not UNSET:
            field_dict["PartsChargeBeforeDiscount"] = parts_charge_before_discount
        if service_charge is not UNSET:
            field_dict["ServiceCharge"] = service_charge
        if repairs_charge is not UNSET:
            field_dict["RepairsCharge"] = repairs_charge
        if guid is not UNSET:
            field_dict["Guid"] = guid
        if segment_name is not UNSET:
            field_dict["SegmentName"] = segment_name
        if schedule_name is not UNSET:
            field_dict["ScheduleName"] = schedule_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = d.pop("AssetId", UNSET)

        asset_service_record_id = d.pop("AssetServiceRecordId", UNSET)

        service_schedule_segment_id = d.pop("ServiceScheduleSegmentId", UNSET)

        forward_segment_id = d.pop("ForwardSegmentId", UNSET)

        forward_next_service = d.pop("ForwardNextService", UNSET)

        service_order_number = d.pop("ServiceOrderNumber", UNSET)

        custom_order_number = d.pop("CustomOrderNumber", UNSET)

        order_item_number = d.pop("OrderItemNumber", UNSET)

        certificate_number = d.pop("CertificateNumber", UNSET)

        result_status = d.pop("ResultStatus", UNSET)

        as_found_result = d.pop("AsFoundResult", UNSET)

        as_left_result = d.pop("AsLeftResult", UNSET)

        _service_date = d.pop("ServiceDate", UNSET)
        service_date: Union[Unset, datetime.datetime]
        if isinstance(_service_date, Unset):
            service_date = UNSET
        else:
            service_date = isoparse(_service_date)

        serial_number = d.pop("SerialNumber", UNSET)

        asset_tag = d.pop("AssetTag", UNSET)

        asset_user = d.pop("AssetUser", UNSET)

        asset_tag_change = d.pop("AssetTagChange", UNSET)

        asset_user_change = d.pop("AssetUserChange", UNSET)

        service_notes = d.pop("ServiceNotes", UNSET)

        serial_number_change = d.pop("SerialNumberChange", UNSET)

        _due_date = d.pop("DueDate", UNSET)
        due_date: Union[Unset, datetime.datetime]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        _next_service_date = d.pop("NextServiceDate", UNSET)
        next_service_date: Union[Unset, datetime.datetime]
        if isinstance(_next_service_date, Unset):
            next_service_date = UNSET
        else:
            next_service_date = isoparse(_next_service_date)

        provider_technician = d.pop("ProviderTechnician", UNSET)

        provider_phone = d.pop("ProviderPhone", UNSET)

        provider_company = d.pop("ProviderCompany", UNSET)

        service_level = d.pop("ServiceLevel", UNSET)

        service_level_code = d.pop("ServiceLevelCode", UNSET)

        next_service_level = d.pop("NextServiceLevel", UNSET)

        next_service_level_code = d.pop("NextServiceLevelCode", UNSET)

        asset_name = d.pop("AssetName", UNSET)

        asset_description = d.pop("AssetDescription", UNSET)

        parts_charge = d.pop("PartsCharge", UNSET)

        parts_charge_before_discount = d.pop("PartsChargeBeforeDiscount", UNSET)

        service_charge = d.pop("ServiceCharge", UNSET)

        repairs_charge = d.pop("RepairsCharge", UNSET)

        _guid = d.pop("Guid", UNSET)
        guid: Union[Unset, UUID]
        if isinstance(_guid, Unset):
            guid = UNSET
        else:
            guid = UUID(_guid)

        segment_name = d.pop("SegmentName", UNSET)

        schedule_name = d.pop("ScheduleName", UNSET)

        qualer_api_models_asset_service_records_to_asset_service_record_response_model = cls(
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

        qualer_api_models_asset_service_records_to_asset_service_record_response_model.additional_properties = (
            d
        )
        return qualer_api_models_asset_service_records_to_asset_service_record_response_model

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
