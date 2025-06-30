import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.qualer_api_models_service_orders_from_order_item_update_model_as_found_check import (
    QualerApiModelsServiceOrdersFromOrderItemUpdateModelAsFoundCheck,
)
from ..models.qualer_api_models_service_orders_from_order_item_update_model_as_found_result import (
    QualerApiModelsServiceOrdersFromOrderItemUpdateModelAsFoundResult,
)
from ..models.qualer_api_models_service_orders_from_order_item_update_model_as_left_check import (
    QualerApiModelsServiceOrdersFromOrderItemUpdateModelAsLeftCheck,
)
from ..models.qualer_api_models_service_orders_from_order_item_update_model_as_left_result import (
    QualerApiModelsServiceOrdersFromOrderItemUpdateModelAsLeftResult,
)
from ..models.qualer_api_models_service_orders_from_order_item_update_model_result_status import (
    QualerApiModelsServiceOrdersFromOrderItemUpdateModelResultStatus,
)
from ..models.qualer_api_models_service_orders_from_order_item_update_model_work_status import (
    QualerApiModelsServiceOrdersFromOrderItemUpdateModelWorkStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsServiceOrdersFromOrderItemUpdateModel")


@_attrs_define
class QualerApiModelsServiceOrdersFromOrderItemUpdateModel:
    """
    Attributes:
        service_comments (Union[Unset, str]):
        private_comments (Union[Unset, str]):
        service_notes (Union[Unset, str]):
        service_total (Union[Unset, float]):
        repairs_total (Union[Unset, float]):
        parts_total (Union[Unset, float]):
        work_status (Union[Unset, QualerApiModelsServiceOrdersFromOrderItemUpdateModelWorkStatus]):
        custom_work_status (Union[Unset, str]):
        is_limited (Union[Unset, bool]):
        checked_on (Union[Unset, datetime.datetime]):
        checked_by_name (Union[Unset, str]):
        completed_on (Union[Unset, datetime.datetime]):
        completed_by_name (Union[Unset, str]):
        as_found_check (Union[Unset, QualerApiModelsServiceOrdersFromOrderItemUpdateModelAsFoundCheck]):
        as_left_check (Union[Unset, QualerApiModelsServiceOrdersFromOrderItemUpdateModelAsLeftCheck]):
        result_status (Union[Unset, QualerApiModelsServiceOrdersFromOrderItemUpdateModelResultStatus]):
        as_found_result (Union[Unset, QualerApiModelsServiceOrdersFromOrderItemUpdateModelAsFoundResult]):
        as_left_result (Union[Unset, QualerApiModelsServiceOrdersFromOrderItemUpdateModelAsLeftResult]):
        equipment_id (Union[Unset, str]):
        legacy_id (Union[Unset, str]):
        serial_number (Union[Unset, str]):
        serial_number_change (Union[Unset, str]):
        asset_tag (Union[Unset, str]):
        asset_tag_change (Union[Unset, str]):
        asset_user (Union[Unset, str]):
        asset_user_change (Union[Unset, str]):
        provider_technician (Union[Unset, str]):
        provider_phone (Union[Unset, str]):
        provider_company (Union[Unset, str]):
        certificate_number (Union[Unset, str]):
        service_date (Union[None, Unset, datetime.datetime]):
        next_service_date (Union[None, Unset, datetime.datetime]):
        vendor_tag (Union[Unset, str]):
    """

    service_comments: Union[Unset, str] = UNSET
    private_comments: Union[Unset, str] = UNSET
    service_notes: Union[Unset, str] = UNSET
    service_total: Union[Unset, float] = UNSET
    repairs_total: Union[Unset, float] = UNSET
    parts_total: Union[Unset, float] = UNSET
    work_status: Union[
        Unset, QualerApiModelsServiceOrdersFromOrderItemUpdateModelWorkStatus
    ] = UNSET
    custom_work_status: Union[Unset, str] = UNSET
    is_limited: Union[Unset, bool] = UNSET
    checked_on: Union[Unset, datetime.datetime] = UNSET
    checked_by_name: Union[Unset, str] = UNSET
    completed_on: Union[Unset, datetime.datetime] = UNSET
    completed_by_name: Union[Unset, str] = UNSET
    as_found_check: Union[
        Unset, QualerApiModelsServiceOrdersFromOrderItemUpdateModelAsFoundCheck
    ] = UNSET
    as_left_check: Union[
        Unset, QualerApiModelsServiceOrdersFromOrderItemUpdateModelAsLeftCheck
    ] = UNSET
    result_status: Union[
        Unset, QualerApiModelsServiceOrdersFromOrderItemUpdateModelResultStatus
    ] = UNSET
    as_found_result: Union[
        Unset, QualerApiModelsServiceOrdersFromOrderItemUpdateModelAsFoundResult
    ] = UNSET
    as_left_result: Union[
        Unset, QualerApiModelsServiceOrdersFromOrderItemUpdateModelAsLeftResult
    ] = UNSET
    equipment_id: Union[Unset, str] = UNSET
    legacy_id: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    serial_number_change: Union[Unset, str] = UNSET
    asset_tag: Union[Unset, str] = UNSET
    asset_tag_change: Union[Unset, str] = UNSET
    asset_user: Union[Unset, str] = UNSET
    asset_user_change: Union[Unset, str] = UNSET
    provider_technician: Union[Unset, str] = UNSET
    provider_phone: Union[Unset, str] = UNSET
    provider_company: Union[Unset, str] = UNSET
    certificate_number: Union[Unset, str] = UNSET
    service_date: Union[None, Unset, datetime.datetime] = UNSET
    next_service_date: Union[None, Unset, datetime.datetime] = UNSET
    vendor_tag: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_comments = self.service_comments

        private_comments = self.private_comments

        service_notes = self.service_notes

        service_total = self.service_total

        repairs_total = self.repairs_total

        parts_total = self.parts_total

        work_status: Union[Unset, str] = UNSET
        if not isinstance(self.work_status, Unset):
            work_status = self.work_status.value

        custom_work_status = self.custom_work_status

        is_limited = self.is_limited

        checked_on: Union[Unset, str] = UNSET
        if not isinstance(self.checked_on, Unset):
            checked_on = self.checked_on.isoformat()

        checked_by_name = self.checked_by_name

        completed_on: Union[Unset, str] = UNSET
        if not isinstance(self.completed_on, Unset):
            completed_on = self.completed_on.isoformat()

        completed_by_name = self.completed_by_name

        as_found_check: Union[Unset, str] = UNSET
        if not isinstance(self.as_found_check, Unset):
            as_found_check = self.as_found_check.value

        as_left_check: Union[Unset, str] = UNSET
        if not isinstance(self.as_left_check, Unset):
            as_left_check = self.as_left_check.value

        result_status: Union[Unset, str] = UNSET
        if not isinstance(self.result_status, Unset):
            result_status = self.result_status.value

        as_found_result: Union[Unset, str] = UNSET
        if not isinstance(self.as_found_result, Unset):
            as_found_result = self.as_found_result.value

        as_left_result: Union[Unset, str] = UNSET
        if not isinstance(self.as_left_result, Unset):
            as_left_result = self.as_left_result.value

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

        service_date: Union[None, Unset, str]
        if isinstance(self.service_date, Unset):
            service_date = UNSET
        elif isinstance(self.service_date, datetime.datetime):
            service_date = self.service_date.isoformat()
        else:
            service_date = self.service_date

        next_service_date: Union[None, Unset, str]
        if isinstance(self.next_service_date, Unset):
            next_service_date = UNSET
        elif isinstance(self.next_service_date, datetime.datetime):
            next_service_date = self.next_service_date.isoformat()
        else:
            next_service_date = self.next_service_date

        vendor_tag = self.vendor_tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_comments is not UNSET:
            field_dict["ServiceComments"] = service_comments
        if private_comments is not UNSET:
            field_dict["PrivateComments"] = private_comments
        if service_notes is not UNSET:
            field_dict["ServiceNotes"] = service_notes
        if service_total is not UNSET:
            field_dict["ServiceTotal"] = service_total
        if repairs_total is not UNSET:
            field_dict["RepairsTotal"] = repairs_total
        if parts_total is not UNSET:
            field_dict["PartsTotal"] = parts_total
        if work_status is not UNSET:
            field_dict["WorkStatus"] = work_status
        if custom_work_status is not UNSET:
            field_dict["CustomWorkStatus"] = custom_work_status
        if is_limited is not UNSET:
            field_dict["IsLimited"] = is_limited
        if checked_on is not UNSET:
            field_dict["CheckedOn"] = checked_on
        if checked_by_name is not UNSET:
            field_dict["CheckedByName"] = checked_by_name
        if completed_on is not UNSET:
            field_dict["CompletedOn"] = completed_on
        if completed_by_name is not UNSET:
            field_dict["CompletedByName"] = completed_by_name
        if as_found_check is not UNSET:
            field_dict["AsFoundCheck"] = as_found_check
        if as_left_check is not UNSET:
            field_dict["AsLeftCheck"] = as_left_check
        if result_status is not UNSET:
            field_dict["ResultStatus"] = result_status
        if as_found_result is not UNSET:
            field_dict["AsFoundResult"] = as_found_result
        if as_left_result is not UNSET:
            field_dict["AsLeftResult"] = as_left_result
        if equipment_id is not UNSET:
            field_dict["EquipmentId"] = equipment_id
        if legacy_id is not UNSET:
            field_dict["LegacyId"] = legacy_id
        if serial_number is not UNSET:
            field_dict["SerialNumber"] = serial_number
        if serial_number_change is not UNSET:
            field_dict["SerialNumberChange"] = serial_number_change
        if asset_tag is not UNSET:
            field_dict["AssetTag"] = asset_tag
        if asset_tag_change is not UNSET:
            field_dict["AssetTagChange"] = asset_tag_change
        if asset_user is not UNSET:
            field_dict["AssetUser"] = asset_user
        if asset_user_change is not UNSET:
            field_dict["AssetUserChange"] = asset_user_change
        if provider_technician is not UNSET:
            field_dict["ProviderTechnician"] = provider_technician
        if provider_phone is not UNSET:
            field_dict["ProviderPhone"] = provider_phone
        if provider_company is not UNSET:
            field_dict["ProviderCompany"] = provider_company
        if certificate_number is not UNSET:
            field_dict["CertificateNumber"] = certificate_number
        if service_date is not UNSET:
            field_dict["ServiceDate"] = service_date
        if next_service_date is not UNSET:
            field_dict["NextServiceDate"] = next_service_date
        if vendor_tag is not UNSET:
            field_dict["VendorTag"] = vendor_tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_comments = d.pop("ServiceComments", UNSET)

        private_comments = d.pop("PrivateComments", UNSET)

        service_notes = d.pop("ServiceNotes", UNSET)

        service_total = d.pop("ServiceTotal", UNSET)

        repairs_total = d.pop("RepairsTotal", UNSET)

        parts_total = d.pop("PartsTotal", UNSET)

        _work_status = d.pop("WorkStatus", UNSET)
        work_status: Union[
            Unset, QualerApiModelsServiceOrdersFromOrderItemUpdateModelWorkStatus
        ]
        if isinstance(_work_status, Unset):
            work_status = UNSET
        else:
            work_status = (
                QualerApiModelsServiceOrdersFromOrderItemUpdateModelWorkStatus(
                    _work_status
                )
            )

        custom_work_status = d.pop("CustomWorkStatus", UNSET)

        is_limited = d.pop("IsLimited", UNSET)

        _checked_on = d.pop("CheckedOn", UNSET)
        checked_on: Union[Unset, datetime.datetime]
        if isinstance(_checked_on, Unset):
            checked_on = UNSET
        else:
            checked_on = isoparse(_checked_on)

        checked_by_name = d.pop("CheckedByName", UNSET)

        _completed_on = d.pop("CompletedOn", UNSET)
        completed_on: Union[Unset, datetime.datetime]
        if isinstance(_completed_on, Unset):
            completed_on = UNSET
        else:
            completed_on = isoparse(_completed_on)

        completed_by_name = d.pop("CompletedByName", UNSET)

        _as_found_check = d.pop("AsFoundCheck", UNSET)
        as_found_check: Union[
            Unset, QualerApiModelsServiceOrdersFromOrderItemUpdateModelAsFoundCheck
        ]
        if isinstance(_as_found_check, Unset):
            as_found_check = UNSET
        else:
            as_found_check = (
                QualerApiModelsServiceOrdersFromOrderItemUpdateModelAsFoundCheck(
                    _as_found_check
                )
            )

        _as_left_check = d.pop("AsLeftCheck", UNSET)
        as_left_check: Union[
            Unset, QualerApiModelsServiceOrdersFromOrderItemUpdateModelAsLeftCheck
        ]
        if isinstance(_as_left_check, Unset):
            as_left_check = UNSET
        else:
            as_left_check = (
                QualerApiModelsServiceOrdersFromOrderItemUpdateModelAsLeftCheck(
                    _as_left_check
                )
            )

        _result_status = d.pop("ResultStatus", UNSET)
        result_status: Union[
            Unset, QualerApiModelsServiceOrdersFromOrderItemUpdateModelResultStatus
        ]
        if isinstance(_result_status, Unset):
            result_status = UNSET
        else:
            result_status = (
                QualerApiModelsServiceOrdersFromOrderItemUpdateModelResultStatus(
                    _result_status
                )
            )

        _as_found_result = d.pop("AsFoundResult", UNSET)
        as_found_result: Union[
            Unset, QualerApiModelsServiceOrdersFromOrderItemUpdateModelAsFoundResult
        ]
        if isinstance(_as_found_result, Unset):
            as_found_result = UNSET
        else:
            as_found_result = (
                QualerApiModelsServiceOrdersFromOrderItemUpdateModelAsFoundResult(
                    _as_found_result
                )
            )

        _as_left_result = d.pop("AsLeftResult", UNSET)
        as_left_result: Union[
            Unset, QualerApiModelsServiceOrdersFromOrderItemUpdateModelAsLeftResult
        ]
        if isinstance(_as_left_result, Unset):
            as_left_result = UNSET
        else:
            as_left_result = (
                QualerApiModelsServiceOrdersFromOrderItemUpdateModelAsLeftResult(
                    _as_left_result
                )
            )

        equipment_id = d.pop("EquipmentId", UNSET)

        legacy_id = d.pop("LegacyId", UNSET)

        serial_number = d.pop("SerialNumber", UNSET)

        serial_number_change = d.pop("SerialNumberChange", UNSET)

        asset_tag = d.pop("AssetTag", UNSET)

        asset_tag_change = d.pop("AssetTagChange", UNSET)

        asset_user = d.pop("AssetUser", UNSET)

        asset_user_change = d.pop("AssetUserChange", UNSET)

        provider_technician = d.pop("ProviderTechnician", UNSET)

        provider_phone = d.pop("ProviderPhone", UNSET)

        provider_company = d.pop("ProviderCompany", UNSET)

        certificate_number = d.pop("CertificateNumber", UNSET)

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

        vendor_tag = d.pop("VendorTag", UNSET)

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

        qualer_api_models_service_orders_from_order_item_update_model.additional_properties = (
            d
        )
        return qualer_api_models_service_orders_from_order_item_update_model

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
