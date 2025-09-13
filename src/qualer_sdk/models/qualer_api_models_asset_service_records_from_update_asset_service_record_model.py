import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="AssetServiceRecordsFromUpdateAssetServiceRecordModel")


@_attrs_define
class AssetServiceRecordsFromUpdateAssetServiceRecordModel:
    """
    Attributes:
        service_order_number (Optional[int]):
        custom_order_number (Optional[str]):
        order_item_number (Optional[int]):
        certificate_number (Optional[str]):
        result_status (Optional[str]):
        as_found_result (Optional[str]):
        as_left_result (Optional[str]):
        applied_interval (Optional[int]):
        as_found_tolerance (Optional[float]):
        as_left_tolerance (Optional[float]):
        service_date (Optional[datetime.datetime]):
        serial_number (Optional[str]):
        asset_tag (Optional[str]):
        asset_user (Optional[str]):
        service_notes (Optional[str]):
        due_date (Optional[datetime.datetime]):
        next_service_date (Optional[datetime.datetime]):
        provider_technician (Optional[str]):
        provider_phone (Optional[str]):
        provider_company (Optional[str]):
        service_level (Optional[str]):
        service_level_code (Optional[str]):
        next_service_level (Optional[str]):
        next_service_level_code (Optional[str]):
        asset_name (Optional[str]):
        asset_description (Optional[str]):
        parts_charge (Optional[float]):
        parts_charge_before_discount (Optional[float]):
        service_charge (Optional[float]):
        repairs_charge (Optional[float]):
        segment_name (Optional[str]):
        schedule_name (Optional[str]):
    """

    service_order_number: Optional[int] = None
    custom_order_number: Optional[str] = None
    order_item_number: Optional[int] = None
    certificate_number: Optional[str] = None
    result_status: Optional[str] = None
    as_found_result: Optional[str] = None
    as_left_result: Optional[str] = None
    applied_interval: Optional[int] = None
    as_found_tolerance: Optional[float] = None
    as_left_tolerance: Optional[float] = None
    service_date: Optional[datetime.datetime] = None
    serial_number: Optional[str] = None
    asset_tag: Optional[str] = None
    asset_user: Optional[str] = None
    service_notes: Optional[str] = None
    due_date: Optional[datetime.datetime] = None
    next_service_date: Optional[datetime.datetime] = None
    provider_technician: Optional[str] = None
    provider_phone: Optional[str] = None
    provider_company: Optional[str] = None
    service_level: Optional[str] = None
    service_level_code: Optional[str] = None
    next_service_level: Optional[str] = None
    next_service_level_code: Optional[str] = None
    asset_name: Optional[str] = None
    asset_description: Optional[str] = None
    parts_charge: Optional[float] = None
    parts_charge_before_discount: Optional[float] = None
    service_charge: Optional[float] = None
    repairs_charge: Optional[float] = None
    segment_name: Optional[str] = None
    schedule_name: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_order_number = self.service_order_number

        custom_order_number = self.custom_order_number

        order_item_number = self.order_item_number

        certificate_number = self.certificate_number

        result_status: Optional[str]
        if not self.result_status:
            result_status = None
        else:
            result_status: Optional[str]

            if not self.result_status:

                result_status = None
            else:
                result_status = self.result_status
        as_found_result: Optional[str]
        if not self.as_found_result:
            as_found_result = None
        else:
            as_found_result: Optional[str]

            if not self.as_found_result:

                as_found_result = None
            else:
                as_found_result = self.as_found_result
        as_left_result: Optional[str]
        if not self.as_left_result:
            as_left_result = None
        else:
            as_left_result: Optional[str]

            if not self.as_left_result:

                as_left_result = None
            else:
                as_left_result = self.as_left_result
        applied_interval: Optional[int]
        if not self.applied_interval:
            applied_interval = None
        else:
            applied_interval = self.applied_interval

        as_found_tolerance: Optional[float]
        if not self.as_found_tolerance:
            as_found_tolerance = None
        else:
            as_found_tolerance = self.as_found_tolerance

        as_left_tolerance: Optional[float]
        if not self.as_left_tolerance:
            as_left_tolerance = None
        else:
            as_left_tolerance = self.as_left_tolerance

        service_date: Optional[str]
        if not self.service_date:
            service_date = None
        elif isinstance(self.service_date, datetime.datetime):
            service_date = self.service_date.isoformat()
        else:
            service_date = self.service_date

        serial_number = self.serial_number

        asset_tag: Optional[str]
        if not self.asset_tag:
            asset_tag = None
        else:
            asset_tag = self.asset_tag

        asset_user: Optional[str]
        if not self.asset_user:
            asset_user = None
        else:
            asset_user = self.asset_user

        service_notes: Optional[str]
        if not self.service_notes:
            service_notes = None
        else:
            service_notes = self.service_notes

        due_date: Optional[str]
        if not self.due_date:
            due_date = None
        elif isinstance(self.due_date, datetime.datetime):
            due_date = self.due_date.isoformat()
        else:
            due_date = self.due_date

        next_service_date: Optional[str]
        if not self.next_service_date:
            next_service_date = None
        elif isinstance(self.next_service_date, datetime.datetime):
            next_service_date = self.next_service_date.isoformat()
        else:
            next_service_date = self.next_service_date

        provider_technician: Optional[str]
        if not self.provider_technician:
            provider_technician = None
        else:
            provider_technician = self.provider_technician

        provider_phone: Optional[str]
        if not self.provider_phone:
            provider_phone = None
        else:
            provider_phone = self.provider_phone

        provider_company: Optional[str]
        if not self.provider_company:
            provider_company = None
        else:
            provider_company = self.provider_company

        service_level: Optional[str]
        if not self.service_level:
            service_level = None
        else:
            service_level = self.service_level

        service_level_code: Optional[str]
        if not self.service_level_code:
            service_level_code = None
        else:
            service_level_code = self.service_level_code

        next_service_level: Optional[str]
        if not self.next_service_level:
            next_service_level = None
        else:
            next_service_level = self.next_service_level

        next_service_level_code: Optional[str]
        if not self.next_service_level_code:
            next_service_level_code = None
        else:
            next_service_level_code = self.next_service_level_code

        asset_name: Optional[str]
        if not self.asset_name:
            asset_name = None
        else:
            asset_name = self.asset_name

        asset_description: Optional[str]
        if not self.asset_description:
            asset_description = None
        else:
            asset_description = self.asset_description

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

        segment_name: Optional[str]
        if not self.segment_name:
            segment_name = None
        else:
            segment_name = self.segment_name

        schedule_name: Optional[str]
        if not self.schedule_name:
            schedule_name = None
        else:
            schedule_name = self.schedule_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_number is not None:
            field_dict["ServiceOrderNumber"] = service_order_number
        if custom_order_number is not None:
            field_dict["CustomOrderNumber"] = custom_order_number
        if order_item_number is not None:
            field_dict["OrderItemNumber"] = order_item_number
        if certificate_number is not None:
            field_dict["CertificateNumber"] = certificate_number
        if result_status is not None:
            field_dict["ResultStatus"] = result_status
        if as_found_result is not None:
            field_dict["AsFoundResult"] = as_found_result
        if as_left_result is not None:
            field_dict["AsLeftResult"] = as_left_result
        if applied_interval is not None:
            field_dict["AppliedInterval"] = applied_interval
        if as_found_tolerance is not None:
            field_dict["AsFoundTolerance"] = as_found_tolerance
        if as_left_tolerance is not None:
            field_dict["AsLeftTolerance"] = as_left_tolerance
        if service_date is not None:
            field_dict["ServiceDate"] = service_date
        if serial_number is not None:
            field_dict["SerialNumber"] = serial_number
        if asset_tag is not None:
            field_dict["AssetTag"] = asset_tag
        if asset_user is not None:
            field_dict["AssetUser"] = asset_user
        if service_notes is not None:
            field_dict["ServiceNotes"] = service_notes
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
        if asset_name is not None:
            field_dict["AssetName"] = asset_name
        if asset_description is not None:
            field_dict["AssetDescription"] = asset_description
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_number = d.pop("ServiceOrderNumber", None)

        custom_order_number = d.pop("CustomOrderNumber", None)

        order_item_number = d.pop("OrderItemNumber", None)

        certificate_number = d.pop("CertificateNumber", None)

        def _parse_result_status(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        result_status = _parse_result_status(d.pop("ResultStatus", None))

        def _parse_as_found_result(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        as_found_result = _parse_as_found_result(d.pop("AsFoundResult", None))

        def _parse_as_left_result(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        as_left_result = _parse_as_left_result(d.pop("AsLeftResult", None))

        def _parse_applied_interval(data: object) -> Optional[int]:
            if not data:
                return None
            return cast(Optional[int], data)

        applied_interval = _parse_applied_interval(d.pop("AppliedInterval", None))

        def _parse_as_found_tolerance(data: object) -> Optional[float]:
            if not data:
                return None
            return cast(Optional[float], data)

        as_found_tolerance = _parse_as_found_tolerance(d.pop("AsFoundTolerance", None))

        def _parse_as_left_tolerance(data: object) -> Optional[float]:
            if not data:
                return None
            return cast(Optional[float], data)

        as_left_tolerance = _parse_as_left_tolerance(d.pop("AsLeftTolerance", None))

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

        serial_number = d.pop("SerialNumber", None)

        def _parse_asset_tag(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        asset_tag = _parse_asset_tag(d.pop("AssetTag", None))

        def _parse_asset_user(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        asset_user = _parse_asset_user(d.pop("AssetUser", None))

        def _parse_service_notes(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        service_notes = _parse_service_notes(d.pop("ServiceNotes", None))

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

        def _parse_provider_technician(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        provider_technician = _parse_provider_technician(d.pop("ProviderTechnician", None))

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

        def _parse_service_level(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        service_level = _parse_service_level(d.pop("ServiceLevel", None))

        def _parse_service_level_code(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        service_level_code = _parse_service_level_code(d.pop("ServiceLevelCode", None))

        def _parse_next_service_level(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        next_service_level = _parse_next_service_level(d.pop("NextServiceLevel", None))

        def _parse_next_service_level_code(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        next_service_level_code = _parse_next_service_level_code(
            d.pop("NextServiceLevelCode", None)
        )

        def _parse_asset_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        asset_name = _parse_asset_name(d.pop("AssetName", None))

        def _parse_asset_description(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        asset_description = _parse_asset_description(d.pop("AssetDescription", None))

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

        qualer_api_models_asset_service_records_from_update_asset_service_record_model = cls(
            service_order_number=service_order_number,
            custom_order_number=custom_order_number,
            order_item_number=order_item_number,
            certificate_number=certificate_number,
            result_status=result_status,
            as_found_result=as_found_result,
            as_left_result=as_left_result,
            applied_interval=applied_interval,
            as_found_tolerance=as_found_tolerance,
            as_left_tolerance=as_left_tolerance,
            service_date=service_date,
            serial_number=serial_number,
            asset_tag=asset_tag,
            asset_user=asset_user,
            service_notes=service_notes,
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
            segment_name=segment_name,
            schedule_name=schedule_name,
        )

        qualer_api_models_asset_service_records_from_update_asset_service_record_model.additional_properties = (
            d
        )
        return qualer_api_models_asset_service_records_from_update_asset_service_record_model

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
