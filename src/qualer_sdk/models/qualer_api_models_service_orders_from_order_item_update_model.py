import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.service_order_check_result import ServiceOrderCheckResult as ServiceOrdersFromOrderItemUpdateModelAsFoundCheck
from ..models.service_order_check_result import ServiceOrderCheckResult as ServiceOrdersFromOrderItemUpdateModelAsLeftCheck
from ..models.service_result_status import ServiceResultStatus
from ..models.work_status import WorkStatus

T = TypeVar("T", bound="ServiceOrdersFromOrderItemUpdateModel")


@_attrs_define
class ServiceOrdersFromOrderItemUpdateModel:
    """
    Attributes:
        service_comments (Optional[str]):
        private_comments (Optional[str]):
        service_notes (Optional[str]):
        service_total (Optional[float]):
        repairs_total (Optional[float]):
        parts_total (Optional[float]):
        work_status (Optional[WorkStatus]):
        custom_work_status (Optional[str]):
        is_limited (Optional[bool]):
        checked_on (Optional[datetime.datetime]):
        checked_by_name (Optional[str]):
        completed_on (Optional[datetime.datetime]):
        completed_by_name (Optional[str]):
        as_found_check (Optional[ServiceOrdersFromOrderItemUpdateModelAsFoundCheck]):
        as_left_check (Optional[ServiceOrdersFromOrderItemUpdateModelAsLeftCheck]):
        result_status (Optional[ServiceResultStatus]):
        as_found_result (Optional[ServiceResultStatus]):
        as_left_result (Optional[ServiceResultStatus]):
        equipment_id (Optional[str]):
        legacy_id (Optional[str]):
        serial_number (Optional[str]):
        serial_number_change (Optional[str]):
        asset_tag (Optional[str]):
        asset_tag_change (Optional[str]):
        asset_user (Optional[str]):
        asset_user_change (Optional[str]):
        provider_technician (Optional[str]):
        provider_phone (Optional[str]):
        provider_company (Optional[str]):
        certificate_number (Optional[str]):
        service_date (Optional[datetime.datetime]):
        next_service_date (Optional[datetime.datetime]):
        vendor_tag (Optional[str]):
    """

    service_comments: Optional[str] = None
    private_comments: Optional[str] = None
    service_notes: Optional[str] = None
    service_total: Optional[float] = None
    repairs_total: Optional[float] = None
    parts_total: Optional[float] = None
    work_status: Optional[WorkStatus] = None
    custom_work_status: Optional[str] = None
    is_limited: Optional[bool] = None
    checked_on: Optional[datetime.datetime] = None
    checked_by_name: Optional[str] = None
    completed_on: Optional[datetime.datetime] = None
    completed_by_name: Optional[str] = None
    as_found_check: Optional[ServiceOrdersFromOrderItemUpdateModelAsFoundCheck] = None
    as_left_check: Optional["ServiceOrdersFromOrderItemUpdateModelAsLeftCheck"] = None
    result_status: Optional[ServiceResultStatus] = None
    as_found_result: Optional[ServiceResultStatus] = None
    as_left_result: Optional[ServiceResultStatus] = None
    equipment_id: Optional[str] = None
    legacy_id: Optional[str] = None
    serial_number: Optional[str] = None
    serial_number_change: Optional[str] = None
    asset_tag: Optional[str] = None
    asset_tag_change: Optional[str] = None
    asset_user: Optional[str] = None
    asset_user_change: Optional[str] = None
    provider_technician: Optional[str] = None
    provider_phone: Optional[str] = None
    provider_company: Optional[str] = None
    certificate_number: Optional[str] = None
    service_date: Optional[datetime.datetime] = None
    next_service_date: Optional[datetime.datetime] = None
    vendor_tag: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_comments = self.service_comments
        private_comments = self.private_comments
        service_notes = self.service_notes
        service_total = self.service_total
        repairs_total = self.repairs_total
        parts_total = self.parts_total
        work_status = self.work_status.value if self.work_status else None
        custom_work_status = self.custom_work_status
        is_limited = self.is_limited
        checked_on: Optional[str] = None
        if self.checked_on:
            checked_on = self.checked_on.isoformat()
        checked_by_name = self.checked_by_name
        completed_on: Optional[str] = None
        if self.completed_on:
            completed_on = self.completed_on.isoformat()
        completed_by_name = self.completed_by_name
        as_found_check = self.as_found_check.value if self.as_found_check else None
        as_left_check = self.as_left_check.value if self.as_left_check else None
        result_status = self.result_status.value if self.result_status else None
        as_found_result = self.as_found_result.value if self.as_found_result else None
        as_left_result = self.as_left_result.value if self.as_left_result else None
        equipment_id = self.equipment_id
        legacy_id = self.legacy_id
        serial_number = self.serial_number
        serial_number_change = self.serial_number_change
        asset_tag = self.asset_tag
        asset_tag_change = self.asset_tag_change
        asset_user = self.asset_user
        asset_user_change = self.asset_user_change
        provider_technician = self.provider_technician
        provider_phone = self.provider_phone
        provider_company = self.provider_company
        certificate_number = self.certificate_number
        service_date = self.service_date.isoformat() if self.service_date else None
        next_service_date = self.next_service_date.isoformat() if self.next_service_date else None
        vendor_tag = self.vendor_tag
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_comments is not None:
            field_dict["ServiceComments"] = service_comments
        if private_comments is not None:
            field_dict["PrivateComments"] = private_comments
        if service_notes is not None:
            field_dict["ServiceNotes"] = service_notes
        if service_total is not None:
            field_dict["ServiceTotal"] = service_total
        if repairs_total is not None:
            field_dict["RepairsTotal"] = repairs_total
        if parts_total is not None:
            field_dict["PartsTotal"] = parts_total
        if work_status is not None:
            field_dict["WorkStatus"] = work_status
        if custom_work_status is not None:
            field_dict["CustomWorkStatus"] = custom_work_status
        if is_limited is not None:
            field_dict["IsLimited"] = is_limited
        if checked_on is not None:
            field_dict["CheckedOn"] = checked_on
        if checked_by_name is not None:
            field_dict["CheckedByName"] = checked_by_name
        if completed_on is not None:
            field_dict["CompletedOn"] = completed_on
        if completed_by_name is not None:
            field_dict["CompletedByName"] = completed_by_name
        if as_found_check is not None:
            field_dict["AsFoundCheck"] = as_found_check
        if as_left_check is not None:
            field_dict["AsLeftCheck"] = as_left_check
        if result_status is not None:
            field_dict["ResultStatus"] = result_status
        if as_found_result is not None:
            field_dict["AsFoundResult"] = as_found_result
        if as_left_result is not None:
            field_dict["AsLeftResult"] = as_left_result
        if equipment_id is not None:
            field_dict["EquipmentId"] = equipment_id
        if legacy_id is not None:
            field_dict["LegacyId"] = legacy_id
        if serial_number is not None:
            field_dict["SerialNumber"] = serial_number
        if serial_number_change is not None:
            field_dict["SerialNumberChange"] = serial_number_change
        if asset_tag is not None:
            field_dict["AssetTag"] = asset_tag
        if asset_tag_change is not None:
            field_dict["AssetTagChange"] = asset_tag_change
        if asset_user is not None:
            field_dict["AssetUser"] = asset_user
        if asset_user_change is not None:
            field_dict["AssetUserChange"] = asset_user_change
        if provider_technician is not None:
            field_dict["ProviderTechnician"] = provider_technician
        if provider_phone is not None:
            field_dict["ProviderPhone"] = provider_phone
        if provider_company is not None:
            field_dict["ProviderCompany"] = provider_company
        if certificate_number is not None:
            field_dict["CertificateNumber"] = certificate_number
        if service_date is not None:
            field_dict["ServiceDate"] = service_date
        if next_service_date is not None:
            field_dict["NextServiceDate"] = next_service_date
        if vendor_tag is not None:
            field_dict["VendorTag"] = vendor_tag
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_comments = d.pop("ServiceComments", None)
        private_comments = d.pop("PrivateComments", None)
        service_notes = d.pop("ServiceNotes", None)
        service_total = d.pop("ServiceTotal", None)
        repairs_total = d.pop("RepairsTotal", None)
        parts_total = d.pop("PartsTotal", None)
        _work_status = d.pop("WorkStatus", None)
        work_status: Optional[WorkStatus]
        if not _work_status:
            work_status = None
        elif _work_status is None:
            work_status = None
        else:
            work_status = WorkStatus(_work_status)
        custom_work_status = d.pop("CustomWorkStatus", None)
        is_limited = d.pop("IsLimited", None)
        _checked_on = d.pop("CheckedOn", None)
        checked_on: Optional[datetime.datetime]
        if not _checked_on:
            checked_on = None
        else:
            checked_on = isoparse(_checked_on)
        checked_by_name = d.pop("CheckedByName", None)
        _completed_on = d.pop("CompletedOn", None)
        completed_on: Optional[datetime.datetime]
        if not _completed_on:
            completed_on = None
        else:
            completed_on = isoparse(_completed_on)
        completed_by_name = d.pop("CompletedByName", None)
        _as_found_check = d.pop("AsFoundCheck", None)
        as_found_check: Optional[ServiceOrdersFromOrderItemUpdateModelAsFoundCheck]
        if not _as_found_check:
            as_found_check = None
        else:
            as_found_check = ServiceOrdersFromOrderItemUpdateModelAsFoundCheck(_as_found_check)
        _as_left_check = d.pop("AsLeftCheck", None)
        as_left_check: Optional[ServiceOrdersFromOrderItemUpdateModelAsLeftCheck]
        if not _as_left_check:
            as_left_check = None
        else:
            as_left_check = ServiceOrdersFromOrderItemUpdateModelAsLeftCheck(_as_left_check)
        _result_status = d.pop("ResultStatus", None)
        result_status: Optional[ServiceResultStatus]
        if not _result_status:
            result_status = None
        elif _result_status is None:
            result_status = None
        else:
            result_status = ServiceResultStatus(_result_status)
        _as_found_result = d.pop("AsFoundResult", None)
        as_found_result: Optional[ServiceResultStatus]
        if not _as_found_result:
            as_found_result = None
        elif _as_found_result is None:
            as_found_result = None
        else:
            as_found_result = ServiceResultStatus(_as_found_result)
        _as_left_result = d.pop("AsLeftResult", None)
        as_left_result: Optional[ServiceResultStatus]
        if not _as_left_result:
            as_left_result = None
        elif _as_left_result is None:
            as_left_result = None
        else:
            as_left_result = ServiceResultStatus(_as_left_result)
        equipment_id = d.pop("EquipmentId", None)
        legacy_id = d.pop("LegacyId", None)
        serial_number = d.pop("SerialNumber", None)
        serial_number_change = d.pop("SerialNumberChange", None)
        asset_tag = d.pop("AssetTag", None)
        asset_tag_change = d.pop("AssetTagChange", None)
        asset_user = d.pop("AssetUser", None)
        asset_user_change = d.pop("AssetUserChange", None)
        provider_technician = d.pop("ProviderTechnician", None)
        provider_phone = d.pop("ProviderPhone", None)
        provider_company = d.pop("ProviderCompany", None)
        certificate_number = d.pop("CertificateNumber", None)
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
        vendor_tag = d.pop("VendorTag", None)
        qualer_api_models_service_orders_from_order_item_update_model = cls(
            service_comments=service_comments,
            private_comments=private_comments,
            service_notes=service_notes,
            service_total=service_total,
            repairs_total=repairs_total,
            parts_total=parts_total,
            work_status=work_status,
            custom_work_status=custom_work_status,
            is_limited=is_limited,
            checked_on=checked_on,
            checked_by_name=checked_by_name,
            completed_on=completed_on,
            completed_by_name=completed_by_name,
            as_found_check=as_found_check,
            as_left_check=as_left_check,
            result_status=result_status,
            as_found_result=as_found_result,
            as_left_result=as_left_result,
            equipment_id=equipment_id,
            legacy_id=legacy_id,
            serial_number=serial_number,
            serial_number_change=serial_number_change,
            asset_tag=asset_tag,
            asset_tag_change=asset_tag_change,
            asset_user=asset_user,
            asset_user_change=asset_user_change,
            provider_technician=provider_technician,
            provider_phone=provider_phone,
            provider_company=provider_company,
            certificate_number=certificate_number,
            service_date=service_date,
            next_service_date=next_service_date,
            vendor_tag=vendor_tag,
        )
        qualer_api_models_service_orders_from_order_item_update_model.additional_properties = d
        return qualer_api_models_service_orders_from_order_item_update_model

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
