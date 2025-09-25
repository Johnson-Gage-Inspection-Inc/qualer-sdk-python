import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.qualer_api_models_service_options_to_service_option_response_model import (
        ServiceOptionsToServiceOptionResponseModel,
    )


T = TypeVar("T", bound="ServiceOrdersToClientOrderItemResponseModel")


@_attrs_define
class ServiceOrdersToClientOrderItemResponseModel:
    """
    Attributes:
        work_item_id (int):
        serial_number (str):
        asset_id (int):
        asset_name (str):
        client_notes (Optional[str]):
        service_comments (Optional[str]):
        private_comments (Optional[str]):
        order_item_number (Optional[int]):
        service_order_id (Optional[int]):
        channel_count (Optional[int]):
        service_total (Optional[float]):
        repairs_total (Optional[float]):
        parts_total (Optional[float]):
        parts_total_before_discount (Optional[float]):
        override_service_total (Optional[bool]):
        override_repairs_total (Optional[bool]):
        override_parts_total (Optional[bool]):
        service_type (Optional[str]):
        document_number (Optional[str]):
        document_section (Optional[str]):
        work_status (Optional[str]):
        custom_work_status (Optional[str]):
        is_limited (Optional[bool]):
        checked_on (Optional[datetime.datetime]):
        checked_by_name (Optional[str]):
        checked_by_id (Optional[int]):
        completed_on (Optional[datetime.datetime]):
        completed_by_name (Optional[str]):
        completed_by_id (Optional[int]):
        updated_by_id (Optional[int]):
        updated_by (Optional[str]):
        as_found_check (Optional[str]):
        as_left_check (Optional[str]):
        item_result_status (Optional[str]):
        item_as_found_result (Optional[str]):
        item_as_left_result (Optional[str]):
        as_found_specification (Optional[int]):
        as_left_specification (Optional[int]):
        created_on_utc (Optional[datetime.datetime]):
        updated_on_utc (Optional[datetime.datetime]):
        equipment_id (Optional[str]):
        service_level (Optional[str]):
        service_level_code (Optional[str]):
        service_level_document_number (Optional[str]):
        service_level_document_section (Optional[str]):
        next_service_level (Optional[str]):
        next_service_level_code (Optional[str]):
        result_status (Optional[str]):
        as_found_result (Optional[str]):
        as_left_result (Optional[str]):
        serial_number_change (Optional[str]):
        asset_tag (Optional[str]):
        asset_user (Optional[str]):
        asset_tag_change (Optional[str]):
        asset_user_change (Optional[str]):
        asset_description (Optional[str]):
        asset_site_name (Optional[str]):
        asset_site_id (Optional[int]):
        asset_company_name (Optional[str]):
        asset_company_id (Optional[int]):
        client_company_id (Optional[int]):
        vendor_company_id (Optional[int]):
        service_notes (Optional[str]):
        provider_technician (Optional[str]):
        provider_phone (Optional[str]):
        provider_company (Optional[str]):
        service_charge (Optional[float]):
        repairs_charge (Optional[float]):
        parts_charge (Optional[float]):
        parts_charge_before_discount (Optional[float]):
        custom_order_number (Optional[str]):
        certificate_number (Optional[str]):
        service_date (Optional[datetime.datetime]):
        due_date (Optional[datetime.datetime]):
        next_service_date (Optional[datetime.datetime]):
        maintenance_task (Optional[str]):
        maintenance_plan (Optional[str]):
        service_options (Optional[List['ServiceOptionsToServiceOptionResponseModel']]):
        vendor_tag (Optional[str]):
        legacy_id (Optional[str]):
        asset_ownership (Optional[str]):
    """

    work_item_id: int
    serial_number: str
    asset_id: int
    asset_name: str
    client_notes: Optional[str] = None
    service_comments: Optional[str] = None
    private_comments: Optional[str] = None
    order_item_number: Optional[int] = None
    service_order_id: Optional[int] = None
    channel_count: Optional[int] = None
    service_total: Optional[float] = None
    repairs_total: Optional[float] = None
    parts_total: Optional[float] = None
    parts_total_before_discount: Optional[float] = None
    override_service_total: Optional[bool] = None
    override_repairs_total: Optional[bool] = None
    override_parts_total: Optional[bool] = None
    service_type: Optional[str] = None
    document_number: Optional[str] = None
    document_section: Optional[str] = None
    work_status: Optional[str] = None
    custom_work_status: Optional[str] = None
    is_limited: Optional[bool] = None
    checked_on: Optional[datetime.datetime] = None
    checked_by_name: Optional[str] = None
    checked_by_id: Optional[int] = None
    completed_on: Optional[datetime.datetime] = None
    completed_by_name: Optional[str] = None
    completed_by_id: Optional[int] = None
    updated_by_id: Optional[int] = None
    updated_by: Optional[str] = None
    as_found_check: Optional[str] = None
    as_left_check: Optional[str] = None
    item_result_status: Optional[str] = None
    item_as_found_result: Optional[str] = None
    item_as_left_result: Optional[str] = None
    as_found_specification: Optional[int] = None
    as_left_specification: Optional[int] = None
    created_on_utc: Optional[datetime.datetime] = None
    updated_on_utc: Optional[datetime.datetime] = None
    equipment_id: Optional[str] = None
    service_level: Optional[str] = None
    service_level_code: Optional[str] = None
    service_level_document_number: Optional[str] = None
    service_level_document_section: Optional[str] = None
    next_service_level: Optional[str] = None
    next_service_level_code: Optional[str] = None
    result_status: Optional[str] = None
    as_found_result: Optional[str] = None
    as_left_result: Optional[str] = None
    serial_number_change: Optional[str] = None
    asset_tag: Optional[str] = None
    asset_user: Optional[str] = None
    asset_tag_change: Optional[str] = None
    asset_user_change: Optional[str] = None
    asset_description: Optional[str] = None
    asset_site_name: Optional[str] = None
    asset_site_id: Optional[int] = None
    asset_company_name: Optional[str] = None
    asset_company_id: Optional[int] = None
    client_company_id: Optional[int] = None
    vendor_company_id: Optional[int] = None
    service_notes: Optional[str] = None
    provider_technician: Optional[str] = None
    provider_phone: Optional[str] = None
    provider_company: Optional[str] = None
    service_charge: Optional[float] = None
    repairs_charge: Optional[float] = None
    parts_charge: Optional[float] = None
    parts_charge_before_discount: Optional[float] = None
    custom_order_number: Optional[str] = None
    certificate_number: Optional[str] = None
    service_date: Optional[datetime.datetime] = None
    due_date: Optional[datetime.datetime] = None
    next_service_date: Optional[datetime.datetime] = None
    maintenance_task: Optional[str] = None
    maintenance_plan: Optional[str] = None
    service_options: Optional[List["ServiceOptionsToServiceOptionResponseModel"]] = None
    vendor_tag: Optional[str] = None
    legacy_id: Optional[str] = None
    asset_ownership: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        work_status: Optional[str]

        if not self.work_status:

            work_status = None

        else:

            work_status = self.work_status
        custom_work_status = self.custom_work_status

        is_limited = self.is_limited

        checked_on: Optional[str]
        if not self.checked_on:
            checked_on = None
        elif isinstance(self.checked_on, datetime.datetime):
            checked_on = self.checked_on.isoformat()
        else:
            checked_on = self.checked_on

        checked_by_name = self.checked_by_name

        checked_by_id = self.checked_by_id

        completed_on: Optional[str]
        if not self.completed_on:
            completed_on = None
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

        item_result_status: Optional[str]
        if not self.item_result_status:
            item_result_status = None
        else:
            item_result_status = self.item_result_status

        item_as_found_result: Optional[str]
        if not self.item_as_found_result:
            item_as_found_result = None
        else:
            item_as_found_result = self.item_as_found_result

        item_as_left_result: Optional[str]
        if not self.item_as_left_result:
            item_as_left_result = None
        else:
            item_as_left_result = self.item_as_left_result

        as_found_specification: Optional[int]
        if not self.as_found_specification:
            as_found_specification = None
        else:
            as_found_specification = self.as_found_specification

        as_left_specification: Optional[int]
        if not self.as_left_specification:
            as_left_specification = None
        else:
            as_left_specification = self.as_left_specification

        created_on_utc: Optional[str]
        if not self.created_on_utc:
            created_on_utc = None
        elif isinstance(self.created_on_utc, datetime.datetime):
            created_on_utc = self.created_on_utc.isoformat()
        else:
            created_on_utc = self.created_on_utc

        updated_on_utc: Optional[str]
        if not self.updated_on_utc:
            updated_on_utc = None
        elif isinstance(self.updated_on_utc, datetime.datetime):
            updated_on_utc = self.updated_on_utc.isoformat()
        else:
            updated_on_utc = self.updated_on_utc

        equipment_id: Optional[str]
        if not self.equipment_id:
            equipment_id = None
        else:
            equipment_id = self.equipment_id

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

        service_level_document_number: Optional[str]
        if not self.service_level_document_number:
            service_level_document_number = None
        else:
            service_level_document_number = self.service_level_document_number

        service_level_document_section: Optional[str]
        if not self.service_level_document_section:
            service_level_document_section = None
        else:
            service_level_document_section = self.service_level_document_section

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
        serial_number: Optional[str]
        if not self.serial_number:
            serial_number = None
        else:
            serial_number = self.serial_number

        serial_number_change: Optional[str]
        if not self.serial_number_change:
            serial_number_change = None
        else:
            serial_number_change = self.serial_number_change

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

        asset_tag_change: Optional[str]
        if not self.asset_tag_change:
            asset_tag_change = None
        else:
            asset_tag_change = self.asset_tag_change

        asset_user_change: Optional[str]
        if not self.asset_user_change:
            asset_user_change = None
        else:
            asset_user_change = self.asset_user_change

        asset_id: Optional[int]
        if not self.asset_id:
            asset_id = None
        else:
            asset_id = self.asset_id

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

        asset_site_name: Optional[str]
        if not self.asset_site_name:
            asset_site_name = None
        else:
            asset_site_name = self.asset_site_name

        asset_site_id: Optional[int]
        if not self.asset_site_id:
            asset_site_id = None
        else:
            asset_site_id = self.asset_site_id

        asset_company_name: Optional[str]
        if not self.asset_company_name:
            asset_company_name = None
        else:
            asset_company_name = self.asset_company_name

        asset_company_id: Optional[int]
        if not self.asset_company_id:
            asset_company_id = None
        else:
            asset_company_id = self.asset_company_id

        client_company_id: Optional[int]
        if not self.client_company_id:
            client_company_id = None
        else:
            client_company_id = self.client_company_id

        vendor_company_id: Optional[int]
        if not self.vendor_company_id:
            vendor_company_id = None
        else:
            vendor_company_id = self.vendor_company_id

        service_notes: Optional[str]
        if not self.service_notes:
            service_notes = None
        else:
            service_notes = self.service_notes

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

        custom_order_number: Optional[str]
        if not self.custom_order_number:
            custom_order_number = None
        else:
            custom_order_number = self.custom_order_number

        certificate_number: Optional[str]
        if not self.certificate_number:
            certificate_number = None
        else:
            certificate_number = self.certificate_number

        service_date: Optional[str]
        if not self.service_date:
            service_date = None
        elif isinstance(self.service_date, datetime.datetime):
            service_date = self.service_date.isoformat()
        else:
            service_date = self.service_date

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

        maintenance_task = self.maintenance_task

        maintenance_plan: Optional[str]
        if not self.maintenance_plan:
            maintenance_plan = None
        else:
            maintenance_plan = self.maintenance_plan

        service_options: Optional[List[Dict[str, Any]]] = None
        if self.service_options:
            service_options = []
            for service_options_item_data in self.service_options:
                service_options_item = service_options_item_data.to_dict()
                service_options.append(service_options_item)

        vendor_tag = self.vendor_tag

        legacy_id = self.legacy_id

        asset_ownership = self.asset_ownership

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if work_item_id is not None:
            field_dict["WorkItemId"] = work_item_id
        if client_notes is not None:
            field_dict["ClientNotes"] = client_notes
        if service_comments is not None:
            field_dict["ServiceComments"] = service_comments
        if private_comments is not None:
            field_dict["PrivateComments"] = private_comments
        if order_item_number is not None:
            field_dict["OrderItemNumber"] = order_item_number
        if service_order_id is not None:
            field_dict["ServiceOrderId"] = service_order_id
        if channel_count is not None:
            field_dict["ChannelCount"] = channel_count
        if service_total is not None:
            field_dict["ServiceTotal"] = service_total
        if repairs_total is not None:
            field_dict["RepairsTotal"] = repairs_total
        if parts_total is not None:
            field_dict["PartsTotal"] = parts_total
        if parts_total_before_discount is not None:
            field_dict["PartsTotalBeforeDiscount"] = parts_total_before_discount
        if override_service_total is not None:
            field_dict["OverrideServiceTotal"] = override_service_total
        if override_repairs_total is not None:
            field_dict["OverrideRepairsTotal"] = override_repairs_total
        if override_parts_total is not None:
            field_dict["OverridePartsTotal"] = override_parts_total
        if service_type is not None:
            field_dict["ServiceType"] = service_type
        if document_number is not None:
            field_dict["DocumentNumber"] = document_number
        if document_section is not None:
            field_dict["DocumentSection"] = document_section
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
        if checked_by_id is not None:
            field_dict["CheckedById"] = checked_by_id
        if completed_on is not None:
            field_dict["CompletedOn"] = completed_on
        if completed_by_name is not None:
            field_dict["CompletedByName"] = completed_by_name
        if completed_by_id is not None:
            field_dict["CompletedById"] = completed_by_id
        if updated_by_id is not None:
            field_dict["UpdatedById"] = updated_by_id
        if updated_by is not None:
            field_dict["UpdatedBy"] = updated_by
        if as_found_check is not None:
            field_dict["AsFoundCheck"] = as_found_check
        if as_left_check is not None:
            field_dict["AsLeftCheck"] = as_left_check
        if item_result_status is not None:
            field_dict["ItemResultStatus"] = item_result_status
        if item_as_found_result is not None:
            field_dict["ItemAsFoundResult"] = item_as_found_result
        if item_as_left_result is not None:
            field_dict["ItemAsLeftResult"] = item_as_left_result
        if as_found_specification is not None:
            field_dict["AsFoundSpecification"] = as_found_specification
        if as_left_specification is not None:
            field_dict["AsLeftSpecification"] = as_left_specification
        if created_on_utc is not None:
            field_dict["CreatedOnUtc"] = created_on_utc
        if updated_on_utc is not None:
            field_dict["UpdatedOnUtc"] = updated_on_utc
        if equipment_id is not None:
            field_dict["EquipmentId"] = equipment_id
        if service_level is not None:
            field_dict["ServiceLevel"] = service_level
        if service_level_code is not None:
            field_dict["ServiceLevelCode"] = service_level_code
        if service_level_document_number is not None:
            field_dict["ServiceLevelDocumentNumber"] = service_level_document_number
        if service_level_document_section is not None:
            field_dict["ServiceLevelDocumentSection"] = service_level_document_section
        if next_service_level is not None:
            field_dict["NextServiceLevel"] = next_service_level
        if next_service_level_code is not None:
            field_dict["NextServiceLevelCode"] = next_service_level_code
        if result_status is not None:
            field_dict["ResultStatus"] = result_status
        if as_found_result is not None:
            field_dict["AsFoundResult"] = as_found_result
        if as_left_result is not None:
            field_dict["AsLeftResult"] = as_left_result
        if serial_number is not None:
            field_dict["SerialNumber"] = serial_number
        if serial_number_change is not None:
            field_dict["SerialNumberChange"] = serial_number_change
        if asset_tag is not None:
            field_dict["AssetTag"] = asset_tag
        if asset_user is not None:
            field_dict["AssetUser"] = asset_user
        if asset_tag_change is not None:
            field_dict["AssetTagChange"] = asset_tag_change
        if asset_user_change is not None:
            field_dict["AssetUserChange"] = asset_user_change
        if asset_id is not None:
            field_dict["AssetId"] = asset_id
        if asset_name is not None:
            field_dict["AssetName"] = asset_name
        if asset_description is not None:
            field_dict["AssetDescription"] = asset_description
        if asset_site_name is not None:
            field_dict["AssetSiteName"] = asset_site_name
        if asset_site_id is not None:
            field_dict["AssetSiteId"] = asset_site_id
        if asset_company_name is not None:
            field_dict["AssetCompanyName"] = asset_company_name
        if asset_company_id is not None:
            field_dict["AssetCompanyId"] = asset_company_id
        if client_company_id is not None:
            field_dict["ClientCompanyId"] = client_company_id
        if vendor_company_id is not None:
            field_dict["VendorCompanyId"] = vendor_company_id
        if service_notes is not None:
            field_dict["ServiceNotes"] = service_notes
        if provider_technician is not None:
            field_dict["ProviderTechnician"] = provider_technician
        if provider_phone is not None:
            field_dict["ProviderPhone"] = provider_phone
        if provider_company is not None:
            field_dict["ProviderCompany"] = provider_company
        if service_charge is not None:
            field_dict["ServiceCharge"] = service_charge
        if repairs_charge is not None:
            field_dict["RepairsCharge"] = repairs_charge
        if parts_charge is not None:
            field_dict["PartsCharge"] = parts_charge
        if parts_charge_before_discount is not None:
            field_dict["PartsChargeBeforeDiscount"] = parts_charge_before_discount
        if custom_order_number is not None:
            field_dict["CustomOrderNumber"] = custom_order_number
        if certificate_number is not None:
            field_dict["CertificateNumber"] = certificate_number
        if service_date is not None:
            field_dict["ServiceDate"] = service_date
        if due_date is not None:
            field_dict["DueDate"] = due_date
        if next_service_date is not None:
            field_dict["NextServiceDate"] = next_service_date
        if maintenance_task is not None:
            field_dict["MaintenanceTask"] = maintenance_task
        if maintenance_plan is not None:
            field_dict["MaintenancePlan"] = maintenance_plan
        if service_options is not None:
            field_dict["ServiceOptions"] = service_options
        if vendor_tag is not None:
            field_dict["VendorTag"] = vendor_tag
        if legacy_id is not None:
            field_dict["LegacyId"] = legacy_id
        if asset_ownership is not None:
            field_dict["AssetOwnership"] = asset_ownership

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_service_options_to_service_option_response_model import (
            ServiceOptionsToServiceOptionResponseModel,
        )

        d = dict(src_dict)
        work_item_id = d.pop("WorkItemId", None)

        client_notes = d.pop("ClientNotes", None)

        service_comments = d.pop("ServiceComments", None)

        private_comments = d.pop("PrivateComments", None)

        order_item_number = d.pop("OrderItemNumber", None)

        service_order_id = d.pop("ServiceOrderId", None)

        channel_count = d.pop("ChannelCount", None)

        service_total = d.pop("ServiceTotal", None)

        repairs_total = d.pop("RepairsTotal", None)

        parts_total = d.pop("PartsTotal", None)

        parts_total_before_discount = d.pop("PartsTotalBeforeDiscount", None)

        override_service_total = d.pop("OverrideServiceTotal", None)

        override_repairs_total = d.pop("OverrideRepairsTotal", None)

        override_parts_total = d.pop("OverridePartsTotal", None)

        service_type = d.pop("ServiceType", None)

        document_number = d.pop("DocumentNumber", None)

        document_section = d.pop("DocumentSection", None)

        work_status = d.pop("WorkStatus", None)

        custom_work_status = d.pop("CustomWorkStatus", None)

        is_limited = d.pop("IsLimited", None)

        def _parse_checked_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                checked_on_type_0 = isoparse(data)

                return checked_on_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        checked_on = _parse_checked_on(d.pop("CheckedOn", None))

        checked_by_name = d.pop("CheckedByName", None)

        checked_by_id = d.pop("CheckedById", None)

        def _parse_completed_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_on_type_0 = isoparse(data)

                return completed_on_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        completed_on = _parse_completed_on(d.pop("CompletedOn", None))

        completed_by_name = d.pop("CompletedByName", None)

        completed_by_id = d.pop("CompletedById", None)

        updated_by_id = d.pop("UpdatedById", None)

        updated_by = d.pop("UpdatedBy", None)

        as_found_check = d.pop("AsFoundCheck", None)

        as_left_check = d.pop("AsLeftCheck", None)

        def _parse_item_result_status(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        item_result_status = _parse_item_result_status(d.pop("ItemResultStatus", None))

        def _parse_item_as_found_result(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        item_as_found_result = _parse_item_as_found_result(d.pop("ItemAsFoundResult", None))

        def _parse_item_as_left_result(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        item_as_left_result = _parse_item_as_left_result(d.pop("ItemAsLeftResult", None))

        def _parse_as_found_specification(data: object) -> Optional[int]:
            if not data:
                return None
            return cast(Optional[int], data)

        as_found_specification = _parse_as_found_specification(d.pop("AsFoundSpecification", None))

        def _parse_as_left_specification(data: object) -> Optional[int]:
            if not data:
                return None
            return cast(Optional[int], data)

        as_left_specification = _parse_as_left_specification(d.pop("AsLeftSpecification", None))

        def _parse_created_on_utc(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_on_utc_type_0 = isoparse(data)

                return created_on_utc_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        created_on_utc = _parse_created_on_utc(d.pop("CreatedOnUtc", None))

        def _parse_updated_on_utc(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_on_utc_type_0 = isoparse(data)

                return updated_on_utc_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        updated_on_utc = _parse_updated_on_utc(d.pop("UpdatedOnUtc", None))

        def _parse_equipment_id(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        equipment_id = _parse_equipment_id(d.pop("EquipmentId", None))

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

        def _parse_service_level_document_number(
            data: object,
        ) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        service_level_document_number = _parse_service_level_document_number(
            d.pop("ServiceLevelDocumentNumber", None)
        )

        def _parse_service_level_document_section(
            data: object,
        ) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        service_level_document_section = _parse_service_level_document_section(
            d.pop("ServiceLevelDocumentSection", None)
        )

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

        def _parse_serial_number(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        serial_number = _parse_serial_number(d.pop("SerialNumber", None))

        def _parse_serial_number_change(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        serial_number_change = _parse_serial_number_change(d.pop("SerialNumberChange", None))

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

        def _parse_asset_id(data: object) -> Optional[int]:
            if not data:
                return None
            return cast(Optional[int], data)

        asset_id = _parse_asset_id(d.pop("AssetId", None))

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

        def _parse_asset_site_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        asset_site_name = _parse_asset_site_name(d.pop("AssetSiteName", None))

        def _parse_asset_site_id(data: object) -> Optional[int]:
            if not data:
                return None
            return cast(Optional[int], data)

        asset_site_id = _parse_asset_site_id(d.pop("AssetSiteId", None))

        def _parse_asset_company_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        asset_company_name = _parse_asset_company_name(d.pop("AssetCompanyName", None))

        def _parse_asset_company_id(data: object) -> Optional[int]:
            if not data:
                return None
            return cast(Optional[int], data)

        asset_company_id = _parse_asset_company_id(d.pop("AssetCompanyId", None))

        def _parse_client_company_id(data: object) -> Optional[int]:
            if not data:
                return None
            return cast(Optional[int], data)

        client_company_id = _parse_client_company_id(d.pop("ClientCompanyId", None))

        def _parse_vendor_company_id(data: object) -> Optional[int]:
            if not data:
                return None
            return cast(Optional[int], data)

        vendor_company_id = _parse_vendor_company_id(d.pop("VendorCompanyId", None))

        def _parse_service_notes(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        service_notes = _parse_service_notes(d.pop("ServiceNotes", None))

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

        def _parse_custom_order_number(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        custom_order_number = _parse_custom_order_number(d.pop("CustomOrderNumber", None))

        def _parse_certificate_number(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        certificate_number = _parse_certificate_number(d.pop("CertificateNumber", None))

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

        maintenance_task = d.pop("MaintenanceTask", None)

        def _parse_maintenance_plan(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        maintenance_plan = _parse_maintenance_plan(d.pop("MaintenancePlan", None))

        service_options = []
        _service_options = d.pop("ServiceOptions", None)
        for service_options_item_data in _service_options or []:
            service_options_item = ServiceOptionsToServiceOptionResponseModel.from_dict(
                service_options_item_data
            )

            service_options.append(service_options_item)

        vendor_tag = d.pop("VendorTag", None)

        legacy_id = d.pop("LegacyId", None)

        asset_ownership = d.pop("AssetOwnership", None)

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
