import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="QualerApiModelsAssetServiceRecordsFromAddAssetServiceRecordModel"
)


@_attrs_define
class QualerApiModelsAssetServiceRecordsFromAddAssetServiceRecordModel:
    """
    Attributes:
        service_order_number (Union[Unset, int]):
        custom_order_number (Union[Unset, str]):
        order_item_number (Union[Unset, int]):
        certificate_number (Union[Unset, str]):
        result_status (Union[None, Unset, str]):
        as_found_result (Union[None, Unset, str]):
        as_left_result (Union[None, Unset, str]):
        applied_interval (Union[None, Unset, int]):
        as_found_tolerance (Union[None, Unset, float]):
        as_left_tolerance (Union[None, Unset, float]):
        service_date (Union[None, Unset, datetime.datetime]):
        serial_number (Union[None, Unset, str]):
        asset_tag (Union[None, Unset, str]):
        asset_user (Union[None, Unset, str]):
        service_notes (Union[None, Unset, str]):
        due_date (Union[None, Unset, datetime.datetime]):
        next_service_date (Union[None, Unset, datetime.datetime]):
        provider_technician (Union[None, Unset, str]):
        provider_phone (Union[None, Unset, str]):
        provider_company (Union[None, Unset, str]):
        service_level (Union[None, Unset, str]):
        service_level_code (Union[None, Unset, str]):
        next_service_level (Union[None, Unset, str]):
        next_service_level_code (Union[None, Unset, str]):
        asset_name (Union[None, Unset, str]):
        asset_description (Union[None, Unset, str]):
        parts_charge (Union[None, Unset, float]):
        parts_charge_before_discount (Union[None, Unset, float]):
        service_charge (Union[None, Unset, float]):
        repairs_charge (Union[None, Unset, float]):
        segment_name (Union[None, Unset, str]):
        schedule_name (Union[None, Unset, str]):
    """

    service_order_number: Union[Unset, int] = UNSET
    custom_order_number: Union[Unset, str] = UNSET
    order_item_number: Union[Unset, int] = UNSET
    certificate_number: Union[Unset, str] = UNSET
    result_status: Union[None, Unset, str] = UNSET
    as_found_result: Union[None, Unset, str] = UNSET
    as_left_result: Union[None, Unset, str] = UNSET
    applied_interval: Union[None, Unset, int] = UNSET
    as_found_tolerance: Union[None, Unset, float] = UNSET
    as_left_tolerance: Union[None, Unset, float] = UNSET
    service_date: Union[None, Unset, datetime.datetime] = UNSET
    serial_number: Union[None, Unset, str] = UNSET
    asset_tag: Union[None, Unset, str] = UNSET
    asset_user: Union[None, Unset, str] = UNSET
    service_notes: Union[None, Unset, str] = UNSET
    due_date: Union[None, Unset, datetime.datetime] = UNSET
    next_service_date: Union[None, Unset, datetime.datetime] = UNSET
    provider_technician: Union[None, Unset, str] = UNSET
    provider_phone: Union[None, Unset, str] = UNSET
    provider_company: Union[None, Unset, str] = UNSET
    service_level: Union[None, Unset, str] = UNSET
    service_level_code: Union[None, Unset, str] = UNSET
    next_service_level: Union[None, Unset, str] = UNSET
    next_service_level_code: Union[None, Unset, str] = UNSET
    asset_name: Union[None, Unset, str] = UNSET
    asset_description: Union[None, Unset, str] = UNSET
    parts_charge: Union[None, Unset, float] = UNSET
    parts_charge_before_discount: Union[None, Unset, float] = UNSET
    service_charge: Union[None, Unset, float] = UNSET
    repairs_charge: Union[None, Unset, float] = UNSET
    segment_name: Union[None, Unset, str] = UNSET
    schedule_name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_order_number = self.service_order_number

        custom_order_number = self.custom_order_number

        order_item_number = self.order_item_number

        certificate_number = self.certificate_number

        result_status: Union[None, Unset, str]
        if isinstance(self.result_status, Unset):
            result_status = UNSET
        else:
            result_status: Union[None, Unset, str]

            if isinstance(self.result_status, Unset):

                result_status = UNSET

            else:

                result_status = self.result_status
        as_found_result: Union[None, Unset, str]
        if isinstance(self.as_found_result, Unset):
            as_found_result = UNSET
        else:
            as_found_result: Union[None, Unset, str]

            if isinstance(self.as_found_result, Unset):

                as_found_result = UNSET

            else:

                as_found_result = self.as_found_result
        as_left_result: Union[None, Unset, str]
        if isinstance(self.as_left_result, Unset):
            as_left_result = UNSET
        else:
            as_left_result: Union[None, Unset, str]

            if isinstance(self.as_left_result, Unset):

                as_left_result = UNSET

            else:

                as_left_result = self.as_left_result
        applied_interval: Union[None, Unset, int]
        if isinstance(self.applied_interval, Unset):
            applied_interval = UNSET
        else:
            applied_interval = self.applied_interval

        as_found_tolerance: Union[None, Unset, float]
        if isinstance(self.as_found_tolerance, Unset):
            as_found_tolerance = UNSET
        else:
            as_found_tolerance = self.as_found_tolerance

        as_left_tolerance: Union[None, Unset, float]
        if isinstance(self.as_left_tolerance, Unset):
            as_left_tolerance = UNSET
        else:
            as_left_tolerance = self.as_left_tolerance

        service_date: Union[None, Unset, str]
        if isinstance(self.service_date, Unset):
            service_date = UNSET
        elif isinstance(self.service_date, datetime.datetime):
            service_date = self.service_date.isoformat()
        else:
            service_date = self.service_date

        serial_number: Union[None, Unset, str]
        if isinstance(self.serial_number, Unset):
            serial_number = UNSET
        else:
            serial_number = self.serial_number

        asset_tag: Union[None, Unset, str]
        if isinstance(self.asset_tag, Unset):
            asset_tag = UNSET
        else:
            asset_tag = self.asset_tag

        asset_user: Union[None, Unset, str]
        if isinstance(self.asset_user, Unset):
            asset_user = UNSET
        else:
            asset_user = self.asset_user

        service_notes: Union[None, Unset, str]
        if isinstance(self.service_notes, Unset):
            service_notes = UNSET
        else:
            service_notes = self.service_notes

        due_date: Union[None, Unset, str]
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        elif isinstance(self.due_date, datetime.datetime):
            due_date = self.due_date.isoformat()
        else:
            due_date = self.due_date

        next_service_date: Union[None, Unset, str]
        if isinstance(self.next_service_date, Unset):
            next_service_date = UNSET
        elif isinstance(self.next_service_date, datetime.datetime):
            next_service_date = self.next_service_date.isoformat()
        else:
            next_service_date = self.next_service_date

        provider_technician: Union[None, Unset, str]
        if isinstance(self.provider_technician, Unset):
            provider_technician = UNSET
        else:
            provider_technician = self.provider_technician

        provider_phone: Union[None, Unset, str]
        if isinstance(self.provider_phone, Unset):
            provider_phone = UNSET
        else:
            provider_phone = self.provider_phone

        provider_company: Union[None, Unset, str]
        if isinstance(self.provider_company, Unset):
            provider_company = UNSET
        else:
            provider_company = self.provider_company

        service_level: Union[None, Unset, str]
        if isinstance(self.service_level, Unset):
            service_level = UNSET
        else:
            service_level = self.service_level

        service_level_code: Union[None, Unset, str]
        if isinstance(self.service_level_code, Unset):
            service_level_code = UNSET
        else:
            service_level_code = self.service_level_code

        next_service_level: Union[None, Unset, str]
        if isinstance(self.next_service_level, Unset):
            next_service_level = UNSET
        else:
            next_service_level = self.next_service_level

        next_service_level_code: Union[None, Unset, str]
        if isinstance(self.next_service_level_code, Unset):
            next_service_level_code = UNSET
        else:
            next_service_level_code = self.next_service_level_code

        asset_name: Union[None, Unset, str]
        if isinstance(self.asset_name, Unset):
            asset_name = UNSET
        else:
            asset_name = self.asset_name

        asset_description: Union[None, Unset, str]
        if isinstance(self.asset_description, Unset):
            asset_description = UNSET
        else:
            asset_description = self.asset_description

        parts_charge: Union[None, Unset, float]
        if isinstance(self.parts_charge, Unset):
            parts_charge = UNSET
        else:
            parts_charge = self.parts_charge

        parts_charge_before_discount: Union[None, Unset, float]
        if isinstance(self.parts_charge_before_discount, Unset):
            parts_charge_before_discount = UNSET
        else:
            parts_charge_before_discount = self.parts_charge_before_discount

        service_charge: Union[None, Unset, float]
        if isinstance(self.service_charge, Unset):
            service_charge = UNSET
        else:
            service_charge = self.service_charge

        repairs_charge: Union[None, Unset, float]
        if isinstance(self.repairs_charge, Unset):
            repairs_charge = UNSET
        else:
            repairs_charge = self.repairs_charge

        segment_name: Union[None, Unset, str]
        if isinstance(self.segment_name, Unset):
            segment_name = UNSET
        else:
            segment_name = self.segment_name

        schedule_name: Union[None, Unset, str]
        if isinstance(self.schedule_name, Unset):
            schedule_name = UNSET
        else:
            schedule_name = self.schedule_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if applied_interval is not UNSET:
            field_dict["AppliedInterval"] = applied_interval
        if as_found_tolerance is not UNSET:
            field_dict["AsFoundTolerance"] = as_found_tolerance
        if as_left_tolerance is not UNSET:
            field_dict["AsLeftTolerance"] = as_left_tolerance
        if service_date is not UNSET:
            field_dict["ServiceDate"] = service_date
        if serial_number is not UNSET:
            field_dict["SerialNumber"] = serial_number
        if asset_tag is not UNSET:
            field_dict["AssetTag"] = asset_tag
        if asset_user is not UNSET:
            field_dict["AssetUser"] = asset_user
        if service_notes is not UNSET:
            field_dict["ServiceNotes"] = service_notes
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
        if segment_name is not UNSET:
            field_dict["SegmentName"] = segment_name
        if schedule_name is not UNSET:
            field_dict["ScheduleName"] = schedule_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_number = d.pop("ServiceOrderNumber", UNSET)

        custom_order_number = d.pop("CustomOrderNumber", UNSET)

        order_item_number = d.pop("OrderItemNumber", UNSET)

        certificate_number = d.pop("CertificateNumber", UNSET)

        def _parse_result_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        result_status = _parse_result_status(d.pop("ResultStatus", UNSET))

        def _parse_as_found_result(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        as_found_result = _parse_as_found_result(d.pop("AsFoundResult", UNSET))

        def _parse_as_left_result(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        as_left_result = _parse_as_left_result(d.pop("AsLeftResult", UNSET))

        def _parse_applied_interval(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        applied_interval = _parse_applied_interval(d.pop("AppliedInterval", UNSET))

        def _parse_as_found_tolerance(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        as_found_tolerance = _parse_as_found_tolerance(d.pop("AsFoundTolerance", UNSET))

        def _parse_as_left_tolerance(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        as_left_tolerance = _parse_as_left_tolerance(d.pop("AsLeftTolerance", UNSET))

        def _parse_service_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                service_date_type_0 = isoparse(data)

                return service_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        service_date = _parse_service_date(d.pop("ServiceDate", UNSET))

        def _parse_serial_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        serial_number = _parse_serial_number(d.pop("SerialNumber", UNSET))

        def _parse_asset_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_tag = _parse_asset_tag(d.pop("AssetTag", UNSET))

        def _parse_asset_user(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_user = _parse_asset_user(d.pop("AssetUser", UNSET))

        def _parse_service_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        service_notes = _parse_service_notes(d.pop("ServiceNotes", UNSET))

        def _parse_due_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_date_type_0 = isoparse(data)

                return due_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        due_date = _parse_due_date(d.pop("DueDate", UNSET))

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

        def _parse_provider_technician(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        provider_technician = _parse_provider_technician(
            d.pop("ProviderTechnician", UNSET)
        )

        def _parse_provider_phone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        provider_phone = _parse_provider_phone(d.pop("ProviderPhone", UNSET))

        def _parse_provider_company(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        provider_company = _parse_provider_company(d.pop("ProviderCompany", UNSET))

        def _parse_service_level(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        service_level = _parse_service_level(d.pop("ServiceLevel", UNSET))

        def _parse_service_level_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        service_level_code = _parse_service_level_code(d.pop("ServiceLevelCode", UNSET))

        def _parse_next_service_level(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        next_service_level = _parse_next_service_level(d.pop("NextServiceLevel", UNSET))

        def _parse_next_service_level_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        next_service_level_code = _parse_next_service_level_code(
            d.pop("NextServiceLevelCode", UNSET)
        )

        def _parse_asset_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_name = _parse_asset_name(d.pop("AssetName", UNSET))

        def _parse_asset_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_description = _parse_asset_description(d.pop("AssetDescription", UNSET))

        def _parse_parts_charge(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        parts_charge = _parse_parts_charge(d.pop("PartsCharge", UNSET))

        def _parse_parts_charge_before_discount(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        parts_charge_before_discount = _parse_parts_charge_before_discount(
            d.pop("PartsChargeBeforeDiscount", UNSET)
        )

        def _parse_service_charge(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        service_charge = _parse_service_charge(d.pop("ServiceCharge", UNSET))

        def _parse_repairs_charge(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        repairs_charge = _parse_repairs_charge(d.pop("RepairsCharge", UNSET))

        def _parse_segment_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        segment_name = _parse_segment_name(d.pop("SegmentName", UNSET))

        def _parse_schedule_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        schedule_name = _parse_schedule_name(d.pop("ScheduleName", UNSET))

        qualer_api_models_asset_service_records_from_add_asset_service_record_model = (
            cls(
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
        )

        qualer_api_models_asset_service_records_from_add_asset_service_record_model.additional_properties = (
            d
        )
        return (
            qualer_api_models_asset_service_records_from_add_asset_service_record_model
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
