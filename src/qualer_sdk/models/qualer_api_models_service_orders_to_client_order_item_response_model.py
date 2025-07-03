import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualer_api_models_service_options_to_service_option_response_model import (
        QualerApiModelsServiceOptionsToServiceOptionResponseModel,
    )


T = TypeVar("T", bound="QualerApiModelsServiceOrdersToClientOrderItemResponseModel")


@_attrs_define
class QualerApiModelsServiceOrdersToClientOrderItemResponseModel:
    """
    Attributes:
        work_item_id (Union[Unset, int]):
        client_notes (Union[Unset, str]):
        service_comments (Union[Unset, str]):
        private_comments (Union[Unset, str]):
        order_item_number (Union[Unset, int]):
        service_order_id (Union[Unset, int]):
        channel_count (Union[Unset, int]):
        service_total (Union[Unset, float]):
        repairs_total (Union[Unset, float]):
        parts_total (Union[Unset, float]):
        parts_total_before_discount (Union[Unset, float]):
        override_service_total (Union[Unset, bool]):
        override_repairs_total (Union[Unset, bool]):
        override_parts_total (Union[Unset, bool]):
        service_type (Union[Unset, str]):
        document_number (Union[Unset, str]):
        document_section (Union[Unset, str]):
        work_status (Union[Unset, str]):
        custom_work_status (Union[Unset, str]):
        is_limited (Union[Unset, bool]):
        checked_on (Union[None, Unset, datetime.datetime]):
        checked_by_name (Union[Unset, str]):
        checked_by_id (Union[Unset, int]):
        completed_on (Union[None, Unset, datetime.datetime]):
        completed_by_name (Union[Unset, str]):
        completed_by_id (Union[Unset, int]):
        updated_by_id (Union[Unset, int]):
        updated_by (Union[Unset, str]):
        as_found_check (Union[Unset, str]):
        as_left_check (Union[Unset, str]):
        item_result_status (Union[None, Unset, str]):
        item_as_found_result (Union[None, Unset, str]):
        item_as_left_result (Union[None, Unset, str]):
        as_found_specification (Union[None, Unset, int]):
        as_left_specification (Union[None, Unset, int]):
        created_on_utc (Union[None, Unset, datetime.datetime]):
        updated_on_utc (Union[None, Unset, datetime.datetime]):
        equipment_id (Union[None, Unset, str]):
        service_level (Union[None, Unset, str]):
        service_level_code (Union[None, Unset, str]):
        service_level_document_number (Union[None, Unset, str]):
        service_level_document_section (Union[None, Unset, str]):
        next_service_level (Union[None, Unset, str]):
        next_service_level_code (Union[None, Unset, str]):
        result_status (Union[None, Unset, str]):
        as_found_result (Union[None, Unset, str]):
        as_left_result (Union[None, Unset, str]):
        serial_number (Union[None, Unset, str]):
        serial_number_change (Union[None, Unset, str]):
        asset_tag (Union[None, Unset, str]):
        asset_user (Union[None, Unset, str]):
        asset_tag_change (Union[None, Unset, str]):
        asset_user_change (Union[None, Unset, str]):
        asset_id (Union[None, Unset, int]):
        asset_name (Union[None, Unset, str]):
        asset_description (Union[None, Unset, str]):
        asset_site_name (Union[None, Unset, str]):
        asset_site_id (Union[None, Unset, int]):
        asset_company_name (Union[None, Unset, str]):
        asset_company_id (Union[None, Unset, int]):
        client_company_id (Union[None, Unset, int]):
        vendor_company_id (Union[None, Unset, int]):
        service_notes (Union[None, Unset, str]):
        provider_technician (Union[None, Unset, str]):
        provider_phone (Union[None, Unset, str]):
        provider_company (Union[None, Unset, str]):
        service_charge (Union[None, Unset, float]):
        repairs_charge (Union[None, Unset, float]):
        parts_charge (Union[None, Unset, float]):
        parts_charge_before_discount (Union[None, Unset, float]):
        custom_order_number (Union[None, Unset, str]):
        certificate_number (Union[None, Unset, str]):
        service_date (Union[None, Unset, datetime.datetime]):
        due_date (Union[None, Unset, datetime.datetime]):
        next_service_date (Union[None, Unset, datetime.datetime]):
        maintenance_task (Union[Unset, str]):
        maintenance_plan (Union[None, Unset, str]):
        service_options (Union[Unset, list['QualerApiModelsServiceOptionsToServiceOptionResponseModel']]):
        vendor_tag (Union[Unset, str]):
        legacy_id (Union[Unset, str]):
        asset_ownership (Union[Unset, str]):
    """

    work_item_id: Union[Unset, int] = UNSET
    client_notes: Union[Unset, str] = UNSET
    service_comments: Union[Unset, str] = UNSET
    private_comments: Union[Unset, str] = UNSET
    order_item_number: Union[Unset, int] = UNSET
    service_order_id: Union[Unset, int] = UNSET
    channel_count: Union[Unset, int] = UNSET
    service_total: Union[Unset, float] = UNSET
    repairs_total: Union[Unset, float] = UNSET
    parts_total: Union[Unset, float] = UNSET
    parts_total_before_discount: Union[Unset, float] = UNSET
    override_service_total: Union[Unset, bool] = UNSET
    override_repairs_total: Union[Unset, bool] = UNSET
    override_parts_total: Union[Unset, bool] = UNSET
    service_type: Union[Unset, str] = UNSET
    document_number: Union[Unset, str] = UNSET
    document_section: Union[Unset, str] = UNSET
    work_status: Union[None, Unset, str] = UNSET
    custom_work_status: Union[Unset, str] = UNSET
    is_limited: Union[Unset, bool] = UNSET
    checked_on: Union[None, Unset, datetime.datetime] = UNSET
    checked_by_name: Union[Unset, str] = UNSET
    checked_by_id: Union[Unset, int] = UNSET
    completed_on: Union[None, Unset, datetime.datetime] = UNSET
    completed_by_name: Union[Unset, str] = UNSET
    completed_by_id: Union[Unset, int] = UNSET
    updated_by_id: Union[Unset, int] = UNSET
    updated_by: Union[Unset, str] = UNSET
    as_found_check: Union[Unset, str] = UNSET
    as_left_check: Union[Unset, str] = UNSET
    item_result_status: Union[None, Unset, str] = UNSET
    item_as_found_result: Union[None, Unset, str] = UNSET
    item_as_left_result: Union[None, Unset, str] = UNSET
    as_found_specification: Union[None, Unset, int] = UNSET
    as_left_specification: Union[None, Unset, int] = UNSET
    created_on_utc: Union[None, Unset, datetime.datetime] = UNSET
    updated_on_utc: Union[None, Unset, datetime.datetime] = UNSET
    equipment_id: Union[None, Unset, str] = UNSET
    service_level: Union[None, Unset, str] = UNSET
    service_level_code: Union[None, Unset, str] = UNSET
    service_level_document_number: Union[None, Unset, str] = UNSET
    service_level_document_section: Union[None, Unset, str] = UNSET
    next_service_level: Union[None, Unset, str] = UNSET
    next_service_level_code: Union[None, Unset, str] = UNSET
    result_status: Union[None, Unset, str] = UNSET
    as_found_result: Union[None, Unset, str] = UNSET
    as_left_result: Union[None, Unset, str] = UNSET
    serial_number: Union[None, Unset, str] = UNSET
    serial_number_change: Union[None, Unset, str] = UNSET
    asset_tag: Union[None, Unset, str] = UNSET
    asset_user: Union[None, Unset, str] = UNSET
    asset_tag_change: Union[None, Unset, str] = UNSET
    asset_user_change: Union[None, Unset, str] = UNSET
    asset_id: Union[None, Unset, int] = UNSET
    asset_name: Union[None, Unset, str] = UNSET
    asset_description: Union[None, Unset, str] = UNSET
    asset_site_name: Union[None, Unset, str] = UNSET
    asset_site_id: Union[None, Unset, int] = UNSET
    asset_company_name: Union[None, Unset, str] = UNSET
    asset_company_id: Union[None, Unset, int] = UNSET
    client_company_id: Union[None, Unset, int] = UNSET
    vendor_company_id: Union[None, Unset, int] = UNSET
    service_notes: Union[None, Unset, str] = UNSET
    provider_technician: Union[None, Unset, str] = UNSET
    provider_phone: Union[None, Unset, str] = UNSET
    provider_company: Union[None, Unset, str] = UNSET
    service_charge: Union[None, Unset, float] = UNSET
    repairs_charge: Union[None, Unset, float] = UNSET
    parts_charge: Union[None, Unset, float] = UNSET
    parts_charge_before_discount: Union[None, Unset, float] = UNSET
    custom_order_number: Union[None, Unset, str] = UNSET
    certificate_number: Union[None, Unset, str] = UNSET
    service_date: Union[None, Unset, datetime.datetime] = UNSET
    due_date: Union[None, Unset, datetime.datetime] = UNSET
    next_service_date: Union[None, Unset, datetime.datetime] = UNSET
    maintenance_task: Union[Unset, str] = UNSET
    maintenance_plan: Union[None, Unset, str] = UNSET
    service_options: Union[
        Unset, list["QualerApiModelsServiceOptionsToServiceOptionResponseModel"]
    ] = UNSET
    vendor_tag: Union[Unset, str] = UNSET
    legacy_id: Union[Unset, str] = UNSET
    asset_ownership: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        work_item_id = self.work_item_id

        client_notes = self.client_notes

        service_comments = self.service_comments

        private_comments = self.private_comments

        order_item_number = self.order_item_number

        service_order_id = self.service_order_id

        channel_count = self.channel_count

        service_total = self.service_total

        repairs_total = self.repairs_total

        parts_total = self.parts_total

        parts_total_before_discount = self.parts_total_before_discount

        override_service_total = self.override_service_total

        override_repairs_total = self.override_repairs_total

        override_parts_total = self.override_parts_total

        service_type = self.service_type

        document_number = self.document_number

        document_section = self.document_section

        work_status: Union[None, Unset, str]

        if isinstance(self.work_status, Unset):

            work_status = UNSET

        else:

            work_status = self.work_status
        custom_work_status = self.custom_work_status

        is_limited = self.is_limited

        checked_on: Union[None, Unset, str]
        if isinstance(self.checked_on, Unset):
            checked_on = UNSET
        elif isinstance(self.checked_on, datetime.datetime):
            checked_on = self.checked_on.isoformat()
        else:
            checked_on = self.checked_on

        checked_by_name = self.checked_by_name

        checked_by_id = self.checked_by_id

        completed_on: Union[None, Unset, str]
        if isinstance(self.completed_on, Unset):
            completed_on = UNSET
        elif isinstance(self.completed_on, datetime.datetime):
            completed_on = self.completed_on.isoformat()
        else:
            completed_on = self.completed_on

        completed_by_name = self.completed_by_name

        completed_by_id = self.completed_by_id

        updated_by_id = self.updated_by_id

        updated_by = self.updated_by

        as_found_check = self.as_found_check

        as_left_check = self.as_left_check

        item_result_status: Union[None, Unset, str]
        if isinstance(self.item_result_status, Unset):
            item_result_status = UNSET
        else:
            item_result_status = self.item_result_status

        item_as_found_result: Union[None, Unset, str]
        if isinstance(self.item_as_found_result, Unset):
            item_as_found_result = UNSET
        else:
            item_as_found_result = self.item_as_found_result

        item_as_left_result: Union[None, Unset, str]
        if isinstance(self.item_as_left_result, Unset):
            item_as_left_result = UNSET
        else:
            item_as_left_result = self.item_as_left_result

        as_found_specification: Union[None, Unset, int]
        if isinstance(self.as_found_specification, Unset):
            as_found_specification = UNSET
        else:
            as_found_specification = self.as_found_specification

        as_left_specification: Union[None, Unset, int]
        if isinstance(self.as_left_specification, Unset):
            as_left_specification = UNSET
        else:
            as_left_specification = self.as_left_specification

        created_on_utc: Union[None, Unset, str]
        if isinstance(self.created_on_utc, Unset):
            created_on_utc = UNSET
        elif isinstance(self.created_on_utc, datetime.datetime):
            created_on_utc = self.created_on_utc.isoformat()
        else:
            created_on_utc = self.created_on_utc

        updated_on_utc: Union[None, Unset, str]
        if isinstance(self.updated_on_utc, Unset):
            updated_on_utc = UNSET
        elif isinstance(self.updated_on_utc, datetime.datetime):
            updated_on_utc = self.updated_on_utc.isoformat()
        else:
            updated_on_utc = self.updated_on_utc

        equipment_id: Union[None, Unset, str]
        if isinstance(self.equipment_id, Unset):
            equipment_id = UNSET
        else:
            equipment_id = self.equipment_id

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

        service_level_document_number: Union[None, Unset, str]
        if isinstance(self.service_level_document_number, Unset):
            service_level_document_number = UNSET
        else:
            service_level_document_number = self.service_level_document_number

        service_level_document_section: Union[None, Unset, str]
        if isinstance(self.service_level_document_section, Unset):
            service_level_document_section = UNSET
        else:
            service_level_document_section = self.service_level_document_section

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
        serial_number: Union[None, Unset, str]
        if isinstance(self.serial_number, Unset):
            serial_number = UNSET
        else:
            serial_number = self.serial_number

        serial_number_change: Union[None, Unset, str]
        if isinstance(self.serial_number_change, Unset):
            serial_number_change = UNSET
        else:
            serial_number_change = self.serial_number_change

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

        asset_tag_change: Union[None, Unset, str]
        if isinstance(self.asset_tag_change, Unset):
            asset_tag_change = UNSET
        else:
            asset_tag_change = self.asset_tag_change

        asset_user_change: Union[None, Unset, str]
        if isinstance(self.asset_user_change, Unset):
            asset_user_change = UNSET
        else:
            asset_user_change = self.asset_user_change

        asset_id: Union[None, Unset, int]
        if isinstance(self.asset_id, Unset):
            asset_id = UNSET
        else:
            asset_id = self.asset_id

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

        asset_site_name: Union[None, Unset, str]
        if isinstance(self.asset_site_name, Unset):
            asset_site_name = UNSET
        else:
            asset_site_name = self.asset_site_name

        asset_site_id: Union[None, Unset, int]
        if isinstance(self.asset_site_id, Unset):
            asset_site_id = UNSET
        else:
            asset_site_id = self.asset_site_id

        asset_company_name: Union[None, Unset, str]
        if isinstance(self.asset_company_name, Unset):
            asset_company_name = UNSET
        else:
            asset_company_name = self.asset_company_name

        asset_company_id: Union[None, Unset, int]
        if isinstance(self.asset_company_id, Unset):
            asset_company_id = UNSET
        else:
            asset_company_id = self.asset_company_id

        client_company_id: Union[None, Unset, int]
        if isinstance(self.client_company_id, Unset):
            client_company_id = UNSET
        else:
            client_company_id = self.client_company_id

        vendor_company_id: Union[None, Unset, int]
        if isinstance(self.vendor_company_id, Unset):
            vendor_company_id = UNSET
        else:
            vendor_company_id = self.vendor_company_id

        service_notes: Union[None, Unset, str]
        if isinstance(self.service_notes, Unset):
            service_notes = UNSET
        else:
            service_notes = self.service_notes

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

        custom_order_number: Union[None, Unset, str]
        if isinstance(self.custom_order_number, Unset):
            custom_order_number = UNSET
        else:
            custom_order_number = self.custom_order_number

        certificate_number: Union[None, Unset, str]
        if isinstance(self.certificate_number, Unset):
            certificate_number = UNSET
        else:
            certificate_number = self.certificate_number

        service_date: Union[None, Unset, str]
        if isinstance(self.service_date, Unset):
            service_date = UNSET
        elif isinstance(self.service_date, datetime.datetime):
            service_date = self.service_date.isoformat()
        else:
            service_date = self.service_date

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

        maintenance_task = self.maintenance_task

        maintenance_plan: Union[None, Unset, str]
        if isinstance(self.maintenance_plan, Unset):
            maintenance_plan = UNSET
        else:
            maintenance_plan = self.maintenance_plan

        service_options: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.service_options, Unset):
            service_options = []
            for service_options_item_data in self.service_options:
                service_options_item = service_options_item_data.to_dict()
                service_options.append(service_options_item)

        vendor_tag = self.vendor_tag

        legacy_id = self.legacy_id

        asset_ownership = self.asset_ownership

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if work_item_id is not UNSET:
            field_dict["WorkItemId"] = work_item_id
        if client_notes is not UNSET:
            field_dict["ClientNotes"] = client_notes
        if service_comments is not UNSET:
            field_dict["ServiceComments"] = service_comments
        if private_comments is not UNSET:
            field_dict["PrivateComments"] = private_comments
        if order_item_number is not UNSET:
            field_dict["OrderItemNumber"] = order_item_number
        if service_order_id is not UNSET:
            field_dict["ServiceOrderId"] = service_order_id
        if channel_count is not UNSET:
            field_dict["ChannelCount"] = channel_count
        if service_total is not UNSET:
            field_dict["ServiceTotal"] = service_total
        if repairs_total is not UNSET:
            field_dict["RepairsTotal"] = repairs_total
        if parts_total is not UNSET:
            field_dict["PartsTotal"] = parts_total
        if parts_total_before_discount is not UNSET:
            field_dict["PartsTotalBeforeDiscount"] = parts_total_before_discount
        if override_service_total is not UNSET:
            field_dict["OverrideServiceTotal"] = override_service_total
        if override_repairs_total is not UNSET:
            field_dict["OverrideRepairsTotal"] = override_repairs_total
        if override_parts_total is not UNSET:
            field_dict["OverridePartsTotal"] = override_parts_total
        if service_type is not UNSET:
            field_dict["ServiceType"] = service_type
        if document_number is not UNSET:
            field_dict["DocumentNumber"] = document_number
        if document_section is not UNSET:
            field_dict["DocumentSection"] = document_section
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
        if checked_by_id is not UNSET:
            field_dict["CheckedById"] = checked_by_id
        if completed_on is not UNSET:
            field_dict["CompletedOn"] = completed_on
        if completed_by_name is not UNSET:
            field_dict["CompletedByName"] = completed_by_name
        if completed_by_id is not UNSET:
            field_dict["CompletedById"] = completed_by_id
        if updated_by_id is not UNSET:
            field_dict["UpdatedById"] = updated_by_id
        if updated_by is not UNSET:
            field_dict["UpdatedBy"] = updated_by
        if as_found_check is not UNSET:
            field_dict["AsFoundCheck"] = as_found_check
        if as_left_check is not UNSET:
            field_dict["AsLeftCheck"] = as_left_check
        if item_result_status is not UNSET:
            field_dict["ItemResultStatus"] = item_result_status
        if item_as_found_result is not UNSET:
            field_dict["ItemAsFoundResult"] = item_as_found_result
        if item_as_left_result is not UNSET:
            field_dict["ItemAsLeftResult"] = item_as_left_result
        if as_found_specification is not UNSET:
            field_dict["AsFoundSpecification"] = as_found_specification
        if as_left_specification is not UNSET:
            field_dict["AsLeftSpecification"] = as_left_specification
        if created_on_utc is not UNSET:
            field_dict["CreatedOnUtc"] = created_on_utc
        if updated_on_utc is not UNSET:
            field_dict["UpdatedOnUtc"] = updated_on_utc
        if equipment_id is not UNSET:
            field_dict["EquipmentId"] = equipment_id
        if service_level is not UNSET:
            field_dict["ServiceLevel"] = service_level
        if service_level_code is not UNSET:
            field_dict["ServiceLevelCode"] = service_level_code
        if service_level_document_number is not UNSET:
            field_dict["ServiceLevelDocumentNumber"] = service_level_document_number
        if service_level_document_section is not UNSET:
            field_dict["ServiceLevelDocumentSection"] = service_level_document_section
        if next_service_level is not UNSET:
            field_dict["NextServiceLevel"] = next_service_level
        if next_service_level_code is not UNSET:
            field_dict["NextServiceLevelCode"] = next_service_level_code
        if result_status is not UNSET:
            field_dict["ResultStatus"] = result_status
        if as_found_result is not UNSET:
            field_dict["AsFoundResult"] = as_found_result
        if as_left_result is not UNSET:
            field_dict["AsLeftResult"] = as_left_result
        if serial_number is not UNSET:
            field_dict["SerialNumber"] = serial_number
        if serial_number_change is not UNSET:
            field_dict["SerialNumberChange"] = serial_number_change
        if asset_tag is not UNSET:
            field_dict["AssetTag"] = asset_tag
        if asset_user is not UNSET:
            field_dict["AssetUser"] = asset_user
        if asset_tag_change is not UNSET:
            field_dict["AssetTagChange"] = asset_tag_change
        if asset_user_change is not UNSET:
            field_dict["AssetUserChange"] = asset_user_change
        if asset_id is not UNSET:
            field_dict["AssetId"] = asset_id
        if asset_name is not UNSET:
            field_dict["AssetName"] = asset_name
        if asset_description is not UNSET:
            field_dict["AssetDescription"] = asset_description
        if asset_site_name is not UNSET:
            field_dict["AssetSiteName"] = asset_site_name
        if asset_site_id is not UNSET:
            field_dict["AssetSiteId"] = asset_site_id
        if asset_company_name is not UNSET:
            field_dict["AssetCompanyName"] = asset_company_name
        if asset_company_id is not UNSET:
            field_dict["AssetCompanyId"] = asset_company_id
        if client_company_id is not UNSET:
            field_dict["ClientCompanyId"] = client_company_id
        if vendor_company_id is not UNSET:
            field_dict["VendorCompanyId"] = vendor_company_id
        if service_notes is not UNSET:
            field_dict["ServiceNotes"] = service_notes
        if provider_technician is not UNSET:
            field_dict["ProviderTechnician"] = provider_technician
        if provider_phone is not UNSET:
            field_dict["ProviderPhone"] = provider_phone
        if provider_company is not UNSET:
            field_dict["ProviderCompany"] = provider_company
        if service_charge is not UNSET:
            field_dict["ServiceCharge"] = service_charge
        if repairs_charge is not UNSET:
            field_dict["RepairsCharge"] = repairs_charge
        if parts_charge is not UNSET:
            field_dict["PartsCharge"] = parts_charge
        if parts_charge_before_discount is not UNSET:
            field_dict["PartsChargeBeforeDiscount"] = parts_charge_before_discount
        if custom_order_number is not UNSET:
            field_dict["CustomOrderNumber"] = custom_order_number
        if certificate_number is not UNSET:
            field_dict["CertificateNumber"] = certificate_number
        if service_date is not UNSET:
            field_dict["ServiceDate"] = service_date
        if due_date is not UNSET:
            field_dict["DueDate"] = due_date
        if next_service_date is not UNSET:
            field_dict["NextServiceDate"] = next_service_date
        if maintenance_task is not UNSET:
            field_dict["MaintenanceTask"] = maintenance_task
        if maintenance_plan is not UNSET:
            field_dict["MaintenancePlan"] = maintenance_plan
        if service_options is not UNSET:
            field_dict["ServiceOptions"] = service_options
        if vendor_tag is not UNSET:
            field_dict["VendorTag"] = vendor_tag
        if legacy_id is not UNSET:
            field_dict["LegacyId"] = legacy_id
        if asset_ownership is not UNSET:
            field_dict["AssetOwnership"] = asset_ownership

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_service_options_to_service_option_response_model import (
            QualerApiModelsServiceOptionsToServiceOptionResponseModel,
        )

        d = dict(src_dict)
        work_item_id = d.pop("WorkItemId", UNSET)

        client_notes = d.pop("ClientNotes", UNSET)

        service_comments = d.pop("ServiceComments", UNSET)

        private_comments = d.pop("PrivateComments", UNSET)

        order_item_number = d.pop("OrderItemNumber", UNSET)

        service_order_id = d.pop("ServiceOrderId", UNSET)

        channel_count = d.pop("ChannelCount", UNSET)

        service_total = d.pop("ServiceTotal", UNSET)

        repairs_total = d.pop("RepairsTotal", UNSET)

        parts_total = d.pop("PartsTotal", UNSET)

        parts_total_before_discount = d.pop("PartsTotalBeforeDiscount", UNSET)

        override_service_total = d.pop("OverrideServiceTotal", UNSET)

        override_repairs_total = d.pop("OverrideRepairsTotal", UNSET)

        override_parts_total = d.pop("OverridePartsTotal", UNSET)

        service_type = d.pop("ServiceType", UNSET)

        document_number = d.pop("DocumentNumber", UNSET)

        document_section = d.pop("DocumentSection", UNSET)

        work_status = d.pop("WorkStatus", UNSET)

        custom_work_status = d.pop("CustomWorkStatus", UNSET)

        is_limited = d.pop("IsLimited", UNSET)

        def _parse_checked_on(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                checked_on_type_0 = isoparse(data)

                return checked_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        checked_on = _parse_checked_on(d.pop("CheckedOn", UNSET))

        checked_by_name = d.pop("CheckedByName", UNSET)

        checked_by_id = d.pop("CheckedById", UNSET)

        def _parse_completed_on(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_on_type_0 = isoparse(data)

                return completed_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        completed_on = _parse_completed_on(d.pop("CompletedOn", UNSET))

        completed_by_name = d.pop("CompletedByName", UNSET)

        completed_by_id = d.pop("CompletedById", UNSET)

        updated_by_id = d.pop("UpdatedById", UNSET)

        updated_by = d.pop("UpdatedBy", UNSET)

        as_found_check = d.pop("AsFoundCheck", UNSET)

        as_left_check = d.pop("AsLeftCheck", UNSET)

        def _parse_item_result_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        item_result_status = _parse_item_result_status(d.pop("ItemResultStatus", UNSET))

        def _parse_item_as_found_result(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        item_as_found_result = _parse_item_as_found_result(
            d.pop("ItemAsFoundResult", UNSET)
        )

        def _parse_item_as_left_result(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        item_as_left_result = _parse_item_as_left_result(
            d.pop("ItemAsLeftResult", UNSET)
        )

        def _parse_as_found_specification(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        as_found_specification = _parse_as_found_specification(
            d.pop("AsFoundSpecification", UNSET)
        )

        def _parse_as_left_specification(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        as_left_specification = _parse_as_left_specification(
            d.pop("AsLeftSpecification", UNSET)
        )

        def _parse_created_on_utc(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_on_utc_type_0 = isoparse(data)

                return created_on_utc_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        created_on_utc = _parse_created_on_utc(d.pop("CreatedOnUtc", UNSET))

        def _parse_updated_on_utc(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_on_utc_type_0 = isoparse(data)

                return updated_on_utc_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        updated_on_utc = _parse_updated_on_utc(d.pop("UpdatedOnUtc", UNSET))

        def _parse_equipment_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        equipment_id = _parse_equipment_id(d.pop("EquipmentId", UNSET))

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

        def _parse_service_level_document_number(
            data: object,
        ) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        service_level_document_number = _parse_service_level_document_number(
            d.pop("ServiceLevelDocumentNumber", UNSET)
        )

        def _parse_service_level_document_section(
            data: object,
        ) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        service_level_document_section = _parse_service_level_document_section(
            d.pop("ServiceLevelDocumentSection", UNSET)
        )

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

        def _parse_serial_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        serial_number = _parse_serial_number(d.pop("SerialNumber", UNSET))

        def _parse_serial_number_change(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        serial_number_change = _parse_serial_number_change(
            d.pop("SerialNumberChange", UNSET)
        )

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

        def _parse_asset_tag_change(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_tag_change = _parse_asset_tag_change(d.pop("AssetTagChange", UNSET))

        def _parse_asset_user_change(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_user_change = _parse_asset_user_change(d.pop("AssetUserChange", UNSET))

        def _parse_asset_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        asset_id = _parse_asset_id(d.pop("AssetId", UNSET))

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

        def _parse_asset_site_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_site_name = _parse_asset_site_name(d.pop("AssetSiteName", UNSET))

        def _parse_asset_site_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        asset_site_id = _parse_asset_site_id(d.pop("AssetSiteId", UNSET))

        def _parse_asset_company_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_company_name = _parse_asset_company_name(d.pop("AssetCompanyName", UNSET))

        def _parse_asset_company_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        asset_company_id = _parse_asset_company_id(d.pop("AssetCompanyId", UNSET))

        def _parse_client_company_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        client_company_id = _parse_client_company_id(d.pop("ClientCompanyId", UNSET))

        def _parse_vendor_company_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        vendor_company_id = _parse_vendor_company_id(d.pop("VendorCompanyId", UNSET))

        def _parse_service_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        service_notes = _parse_service_notes(d.pop("ServiceNotes", UNSET))

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

        def _parse_custom_order_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        custom_order_number = _parse_custom_order_number(
            d.pop("CustomOrderNumber", UNSET)
        )

        def _parse_certificate_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        certificate_number = _parse_certificate_number(
            d.pop("CertificateNumber", UNSET)
        )

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

        maintenance_task = d.pop("MaintenanceTask", UNSET)

        def _parse_maintenance_plan(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        maintenance_plan = _parse_maintenance_plan(d.pop("MaintenancePlan", UNSET))

        service_options = []
        _service_options = d.pop("ServiceOptions", UNSET)
        for service_options_item_data in _service_options or []:
            service_options_item = (
                QualerApiModelsServiceOptionsToServiceOptionResponseModel.from_dict(
                    service_options_item_data
                )
            )

            service_options.append(service_options_item)

        vendor_tag = d.pop("VendorTag", UNSET)

        legacy_id = d.pop("LegacyId", UNSET)

        asset_ownership = d.pop("AssetOwnership", UNSET)

        qualer_api_models_service_orders_to_client_order_item_response_model = cls(
            work_item_id=work_item_id,
            client_notes=client_notes,
            service_comments=service_comments,
            private_comments=private_comments,
            order_item_number=order_item_number,
            service_order_id=service_order_id,
            channel_count=channel_count,
            service_total=service_total,
            repairs_total=repairs_total,
            parts_total=parts_total,
            parts_total_before_discount=parts_total_before_discount,
            override_service_total=override_service_total,
            override_repairs_total=override_repairs_total,
            override_parts_total=override_parts_total,
            service_type=service_type,
            document_number=document_number,
            document_section=document_section,
            work_status=work_status,
            custom_work_status=custom_work_status,
            is_limited=is_limited,
            checked_on=checked_on,
            checked_by_name=checked_by_name,
            checked_by_id=checked_by_id,
            completed_on=completed_on,
            completed_by_name=completed_by_name,
            completed_by_id=completed_by_id,
            updated_by_id=updated_by_id,
            updated_by=updated_by,
            as_found_check=as_found_check,
            as_left_check=as_left_check,
            item_result_status=item_result_status,
            item_as_found_result=item_as_found_result,
            item_as_left_result=item_as_left_result,
            as_found_specification=as_found_specification,
            as_left_specification=as_left_specification,
            created_on_utc=created_on_utc,
            updated_on_utc=updated_on_utc,
            equipment_id=equipment_id,
            service_level=service_level,
            service_level_code=service_level_code,
            service_level_document_number=service_level_document_number,
            service_level_document_section=service_level_document_section,
            next_service_level=next_service_level,
            next_service_level_code=next_service_level_code,
            result_status=result_status,
            as_found_result=as_found_result,
            as_left_result=as_left_result,
            serial_number=serial_number,
            serial_number_change=serial_number_change,
            asset_tag=asset_tag,
            asset_user=asset_user,
            asset_tag_change=asset_tag_change,
            asset_user_change=asset_user_change,
            asset_id=asset_id,
            asset_name=asset_name,
            asset_description=asset_description,
            asset_site_name=asset_site_name,
            asset_site_id=asset_site_id,
            asset_company_name=asset_company_name,
            asset_company_id=asset_company_id,
            client_company_id=client_company_id,
            vendor_company_id=vendor_company_id,
            service_notes=service_notes,
            provider_technician=provider_technician,
            provider_phone=provider_phone,
            provider_company=provider_company,
            service_charge=service_charge,
            repairs_charge=repairs_charge,
            parts_charge=parts_charge,
            parts_charge_before_discount=parts_charge_before_discount,
            custom_order_number=custom_order_number,
            certificate_number=certificate_number,
            service_date=service_date,
            due_date=due_date,
            next_service_date=next_service_date,
            maintenance_task=maintenance_task,
            maintenance_plan=maintenance_plan,
            service_options=service_options,
            vendor_tag=vendor_tag,
            legacy_id=legacy_id,
            asset_ownership=asset_ownership,
        )

        qualer_api_models_service_orders_to_client_order_item_response_model.additional_properties = (
            d
        )
        return qualer_api_models_service_orders_to_client_order_item_response_model

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
