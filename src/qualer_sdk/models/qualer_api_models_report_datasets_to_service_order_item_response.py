import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.work_status import WorkStatus

T = TypeVar("T", bound="ReportDatasetsToServiceOrderItemResponse")


@_attrs_define
class ReportDatasetsToServiceOrderItemResponse:
    """
    Attributes:
        certificate_number (Optional[str]):
        document_number (Optional[str]):
        revision (Optional[str]):
        effective_date (Optional[datetime.datetime]):
        document_section (Optional[str]):
        service_level (Optional[str]):
        service_level_code (Optional[str]):
        service_type (Optional[str]):
        order_item_number (Optional[int]):
        service_charge (Optional[float]):
        updated_by (Optional[str]):
        updated_on (Optional[datetime.datetime]):
        work_status (Optional[WorkStatus]):
        custom_work_status (Optional[str]):
        service_comments (Optional[str]):
        client_notes (Optional[str]):
        vendor_service_notes (Optional[str]):
        display_name (Optional[str]):
        display_part_number (Optional[str]):
        part_number (Optional[str]):
        schedule_name (Optional[str]):
        segment_name (Optional[str]):
        next_segment_name (Optional[str]):
        interval_length (Optional[int]):
        interval_cycle (Optional[str]):
        service_options (Optional[str]):
        service_options_price (Optional[str]):
        service_options_document_numbers (Optional[str]):
        location (Optional[str]):
        station (Optional[str]):
        room (Optional[str]):
        site (Optional[str]):
        vendor_id (Optional[int]):
        service_order_number (Optional[int]):
        custom_order_number (Optional[str]):
        linked_order_number (Optional[str]):
        asset_id (Optional[int]):
        asset_class (Optional[str]):
        asset_condition (Optional[str]):
        asset_criticality (Optional[str]):
        asset_pool (Optional[str]):
        asset_name (Optional[str]):
        asset_description (Optional[str]):
        asset_document_number (Optional[str]):
        asset_document_section (Optional[str]):
        document_number_values (Optional[str]):
        product_name (Optional[str]):
        product_description (Optional[str]):
        asset_maker (Optional[str]):
        category_name (Optional[str]):
        root_category_name (Optional[str]):
        vendor_tag (Optional[str]):
        result_status (Optional[int]):
        service_date (Optional[datetime.datetime]):
        next_service_date (Optional[datetime.datetime]):
        original_due_date (Optional[datetime.datetime]):
        asset_tag (Optional[str]):
        department (Optional[str]):
        asset_user (Optional[str]):
        equipment_id (Optional[str]):
        legacy_identifier (Optional[str]):
        activation_date (Optional[datetime.datetime]):
        purchase_date (Optional[datetime.datetime]):
        part_name (Optional[str]):
        part_description (Optional[str]):
        is_taxable (Optional[bool]):
        is_limited (Optional[bool]):
        quantity (Optional[float]):
        discount (Optional[float]):
        price (Optional[float]):
        time_spent_in_minutes (Optional[float]):
        is_hourly_pricing (Optional[bool]):
        delivery_charge (Optional[float]):
        serial_number (Optional[str]):
        part_repair_charges (Optional[float]):
        part_repair_price (Optional[float]):
        override_parts_total (Optional[bool]):
        override_repairs_total (Optional[bool]):
        asset_custodian_name (Optional[str]):
        as_found_specification_group_name (Optional[str]):
        as_found_specification_company_name (Optional[str]):
        as_left_specification_group_name (Optional[str]):
        as_left_specification_company_name (Optional[str]):
        order_id (Optional[int]):
        parent_order_id (Optional[int]):
        order_item_id (Optional[int]):
        order_item_part_id (Optional[int]):
        as_found_specification_group_id (Optional[int]):
        as_left_specification_group_id (Optional[int]):
        as_found_status (Optional[int]):
        as_left_status (Optional[int]):
        as_found_result (Optional[int]):
        as_left_result (Optional[int]):
        completed_on (Optional[datetime.datetime]):
        received_on (Optional[datetime.datetime]):
        completed_by_name (Optional[str]):
        service_charge_base (Optional[float]):
        service_total (Optional[float]):
        repairs_total (Optional[float]):
        parts_total (Optional[float]):
        parts_total_before_discount (Optional[float]):
        parent_manufacturer (Optional[str]):
        parent_location (Optional[str]):
        parent_manufacturer_part_number (Optional[str]):
        parent_display_part_number (Optional[str]):
        parent_asset_id (Optional[int]):
        parent_category_name (Optional[str]):
        parent_root_category_name (Optional[str]):
        parent_serial_number (Optional[str]):
        parent_asset_tag (Optional[str]):
        parent_asset_user (Optional[str]):
        parent_display_name (Optional[str]):
        parent_equipment_id (Optional[str]):
        asset_shipping_address_1 (Optional[str]):
        asset_shipping_address_2 (Optional[str]):
        asset_shipping_first_name (Optional[str]):
        asset_shipping_last_name (Optional[str]):
        asset_shipping_email (Optional[str]):
        asset_shipping_company (Optional[str]):
        asset_shipping_city (Optional[str]):
        asset_shipping_zip (Optional[str]):
        asset_shipping_phone_number (Optional[str]):
        asset_shipping_fax_number (Optional[str]):
        asset_shipping_country (Optional[str]):
        asset_shipping_state (Optional[str]):
        shipping_address_1 (Optional[str]):
        shipping_address_2 (Optional[str]):
        shipping_first_name (Optional[str]):
        shipping_last_name (Optional[str]):
        shipping_email (Optional[str]):
        shipping_company (Optional[str]):
        shipping_city (Optional[str]):
        shipping_zip (Optional[str]):
        shipping_phone_number (Optional[str]):
        shipping_fax_number (Optional[str]):
        shipping_country (Optional[str]):
        shipping_state (Optional[str]):
        asset_service_notes (Optional[str]):
        service_option_service_code (Optional[str]):
    """

    certificate_number: Optional[str] = None
    document_number: Optional[str] = None
    revision: Optional[str] = None
    effective_date: Optional[datetime.datetime] = None
    document_section: Optional[str] = None
    service_level: Optional[str] = None
    service_level_code: Optional[str] = None
    service_type: Optional[str] = None
    order_item_number: Optional[int] = None
    service_charge: Optional[float] = None
    updated_by: Optional[str] = None
    updated_on: Optional[datetime.datetime] = None
    work_status: Optional[WorkStatus] = None
    custom_work_status: Optional[str] = None
    service_comments: Optional[str] = None
    client_notes: Optional[str] = None
    vendor_service_notes: Optional[str] = None
    display_name: Optional[str] = None
    display_part_number: Optional[str] = None
    part_number: Optional[str] = None
    schedule_name: Optional[str] = None
    segment_name: Optional[str] = None
    next_segment_name: Optional[str] = None
    interval_length: Optional[int] = None
    interval_cycle: Optional[str] = None
    service_options: Optional[str] = None
    service_options_price: Optional[str] = None
    service_options_document_numbers: Optional[str] = None
    location: Optional[str] = None
    station: Optional[str] = None
    room: Optional[str] = None
    site: Optional[str] = None
    vendor_id: Optional[int] = None
    service_order_number: Optional[int] = None
    custom_order_number: Optional[str] = None
    linked_order_number: Optional[str] = None
    asset_id: Optional[int] = None
    asset_class: Optional[str] = None
    asset_condition: Optional[str] = None
    asset_criticality: Optional[str] = None
    asset_pool: Optional[str] = None
    asset_name: Optional[str] = None
    asset_description: Optional[str] = None
    asset_document_number: Optional[str] = None
    asset_document_section: Optional[str] = None
    document_number_values: Optional[str] = None
    product_name: Optional[str] = None
    product_description: Optional[str] = None
    asset_maker: Optional[str] = None
    category_name: Optional[str] = None
    root_category_name: Optional[str] = None
    vendor_tag: Optional[str] = None
    result_status: Optional[int] = None
    service_date: Optional[datetime.datetime] = None
    next_service_date: Optional[datetime.datetime] = None
    original_due_date: Optional[datetime.datetime] = None
    asset_tag: Optional[str] = None
    department: Optional[str] = None
    asset_user: Optional[str] = None
    equipment_id: Optional[str] = None
    legacy_identifier: Optional[str] = None
    activation_date: Optional[datetime.datetime] = None
    purchase_date: Optional[datetime.datetime] = None
    part_name: Optional[str] = None
    part_description: Optional[str] = None
    is_taxable: Optional[bool] = None
    is_limited: Optional[bool] = None
    quantity: Optional[float] = None
    discount: Optional[float] = None
    price: Optional[float] = None
    time_spent_in_minutes: Optional[float] = None
    is_hourly_pricing: Optional[bool] = None
    delivery_charge: Optional[float] = None
    serial_number: Optional[str] = None
    part_repair_charges: Optional[float] = None
    part_repair_price: Optional[float] = None
    override_parts_total: Optional[bool] = None
    override_repairs_total: Optional[bool] = None
    asset_custodian_name: Optional[str] = None
    as_found_specification_group_name: Optional[str] = None
    as_found_specification_company_name: Optional[str] = None
    as_left_specification_group_name: Optional[str] = None
    as_left_specification_company_name: Optional[str] = None
    order_id: Optional[int] = None
    parent_order_id: Optional[int] = None
    order_item_id: Optional[int] = None
    order_item_part_id: Optional[int] = None
    as_found_specification_group_id: Optional[int] = None
    as_left_specification_group_id: Optional[int] = None
    as_found_status: Optional[int] = None
    as_left_status: Optional[int] = None
    as_found_result: Optional[int] = None
    as_left_result: Optional[int] = None
    completed_on: Optional[datetime.datetime] = None
    received_on: Optional[datetime.datetime] = None
    completed_by_name: Optional[str] = None
    service_charge_base: Optional[float] = None
    service_total: Optional[float] = None
    repairs_total: Optional[float] = None
    parts_total: Optional[float] = None
    parts_total_before_discount: Optional[float] = None
    parent_manufacturer: Optional[str] = None
    parent_location: Optional[str] = None
    parent_manufacturer_part_number: Optional[str] = None
    parent_display_part_number: Optional[str] = None
    parent_asset_id: Optional[int] = None
    parent_category_name: Optional[str] = None
    parent_root_category_name: Optional[str] = None
    parent_serial_number: Optional[str] = None
    parent_asset_tag: Optional[str] = None
    parent_asset_user: Optional[str] = None
    parent_display_name: Optional[str] = None
    parent_equipment_id: Optional[str] = None
    asset_shipping_address_1: Optional[str] = None
    asset_shipping_address_2: Optional[str] = None
    asset_shipping_first_name: Optional[str] = None
    asset_shipping_last_name: Optional[str] = None
    asset_shipping_email: Optional[str] = None
    asset_shipping_company: Optional[str] = None
    asset_shipping_city: Optional[str] = None
    asset_shipping_zip: Optional[str] = None
    asset_shipping_phone_number: Optional[str] = None
    asset_shipping_fax_number: Optional[str] = None
    asset_shipping_country: Optional[str] = None
    asset_shipping_state: Optional[str] = None
    shipping_address_1: Optional[str] = None
    shipping_address_2: Optional[str] = None
    shipping_first_name: Optional[str] = None
    shipping_last_name: Optional[str] = None
    shipping_email: Optional[str] = None
    shipping_company: Optional[str] = None
    shipping_city: Optional[str] = None
    shipping_zip: Optional[str] = None
    shipping_phone_number: Optional[str] = None
    shipping_fax_number: Optional[str] = None
    shipping_country: Optional[str] = None
    shipping_state: Optional[str] = None
    asset_service_notes: Optional[str] = None
    service_option_service_code: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        certificate_number = self.certificate_number
        document_number = self.document_number
        revision = self.revision
        effective_date = self.effective_date.isoformat() if self.effective_date else None
        document_section = self.document_section
        service_level = self.service_level
        service_level_code = self.service_level_code
        service_type = self.service_type
        order_item_number = self.order_item_number
        service_charge = self.service_charge
        updated_by = self.updated_by
        updated_on: Optional[str] = None
        if self.updated_on:
            updated_on = self.updated_on.isoformat()
        work_status = self.work_status.value if self.work_status else None
        custom_work_status = self.custom_work_status
        service_comments = self.service_comments
        client_notes = self.client_notes
        vendor_service_notes = self.vendor_service_notes
        display_name = self.display_name
        display_part_number = self.display_part_number
        part_number = self.part_number
        schedule_name = self.schedule_name
        segment_name = self.segment_name
        next_segment_name = self.next_segment_name
        interval_length = self.interval_length
        interval_cycle = self.interval_cycle
        service_options = self.service_options
        service_options_price = self.service_options_price
        service_options_document_numbers = self.service_options_document_numbers
        location = self.location
        station = self.station
        room = self.room
        site = self.site
        vendor_id = self.vendor_id
        service_order_number = self.service_order_number
        custom_order_number = self.custom_order_number
        linked_order_number = self.linked_order_number
        asset_id = self.asset_id
        asset_class = self.asset_class
        asset_condition = self.asset_condition
        asset_criticality = self.asset_criticality
        asset_pool = self.asset_pool
        asset_name = self.asset_name
        asset_description = self.asset_description
        asset_document_number = self.asset_document_number
        asset_document_section = self.asset_document_section
        document_number_values = self.document_number_values
        product_name = self.product_name
        product_description = self.product_description
        asset_maker = self.asset_maker
        category_name = self.category_name
        root_category_name = self.root_category_name
        vendor_tag = self.vendor_tag
        result_status: Optional[int]
        if not self.result_status:
            result_status = None
        else:
            result_status: Optional[str]
            if not self.result_status:
                result_status = None
            else:
                result_status = self.result_status
        service_date = self.service_date.isoformat() if self.service_date else None
        next_service_date = self.next_service_date.isoformat() if self.next_service_date else None
        original_due_date = self.original_due_date.isoformat() if self.original_due_date else None
        asset_tag = self.asset_tag
        department = self.department
        asset_user = self.asset_user
        equipment_id = self.equipment_id
        legacy_identifier = self.legacy_identifier
        activation_date = self.activation_date.isoformat() if self.activation_date else None
        purchase_date = self.purchase_date.isoformat() if self.purchase_date else None
        part_name = self.part_name
        part_description = self.part_description
        is_taxable = self.is_taxable
        is_limited = self.is_limited
        quantity: Optional[float]
        if not self.quantity:
            quantity = None
        else:
            quantity = self.quantity
        discount: Optional[float]
        if not self.discount:
            discount = None
        else:
            discount = self.discount
        price: Optional[float]
        if not self.price:
            price = None
        else:
            price = self.price
        time_spent_in_minutes: Optional[float]
        if not self.time_spent_in_minutes:
            time_spent_in_minutes = None
        else:
            time_spent_in_minutes = self.time_spent_in_minutes
        is_hourly_pricing: Optional[bool]
        if not self.is_hourly_pricing:
            is_hourly_pricing = None
        else:
            is_hourly_pricing = self.is_hourly_pricing
        delivery_charge: Optional[float]
        if not self.delivery_charge:
            delivery_charge = None
        else:
            delivery_charge = self.delivery_charge
        serial_number = self.serial_number
        part_repair_charges: Optional[float]
        if not self.part_repair_charges:
            part_repair_charges = None
        else:
            part_repair_charges = self.part_repair_charges
        part_repair_price: Optional[float]
        if not self.part_repair_price:
            part_repair_price = None
        else:
            part_repair_price = self.part_repair_price
        override_parts_total = self.override_parts_total
        override_repairs_total = self.override_repairs_total
        asset_custodian_name = self.asset_custodian_name
        as_found_specification_group_name = self.as_found_specification_group_name
        as_found_specification_company_name = self.as_found_specification_company_name
        as_left_specification_group_name = self.as_left_specification_group_name
        as_left_specification_company_name = self.as_left_specification_company_name
        order_id: Optional[int]
        if not self.order_id:
            order_id = None
        else:
            order_id = self.order_id
        parent_order_id: Optional[int]
        if not self.parent_order_id:
            parent_order_id = None
        else:
            parent_order_id = self.parent_order_id
        order_item_id: Optional[int]
        if not self.order_item_id:
            order_item_id = None
        else:
            order_item_id = self.order_item_id
        order_item_part_id: Optional[int]
        if not self.order_item_part_id:
            order_item_part_id = None
        else:
            order_item_part_id = self.order_item_part_id
        as_found_specification_group_id: Optional[int]
        if not self.as_found_specification_group_id:
            as_found_specification_group_id = None
        else:
            as_found_specification_group_id = self.as_found_specification_group_id
        as_left_specification_group_id: Optional[int]
        if not self.as_left_specification_group_id:
            as_left_specification_group_id = None
        else:
            as_left_specification_group_id = self.as_left_specification_group_id
        as_found_status: Optional[int]
        if not self.as_found_status:
            as_found_status = None
        else:
            as_found_status = self.as_found_status
        as_left_status: Optional[int]
        if not self.as_left_status:
            as_left_status = None
        else:
            as_left_status = self.as_left_status
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
        completed_on = self.completed_on.isoformat() if self.completed_on else None
        received_on = self.received_on.isoformat() if self.received_on else None
        completed_by_name = self.completed_by_name
        service_charge_base: Optional[float]
        if not self.service_charge_base:
            service_charge_base = None
        else:
            service_charge_base = self.service_charge_base
        service_total: Optional[float]
        if not self.service_total:
            service_total = None
        else:
            service_total = self.service_total
        repairs_total: Optional[float]
        if not self.repairs_total:
            repairs_total = None
        else:
            repairs_total = self.repairs_total
        parts_total: Optional[float]
        if not self.parts_total:
            parts_total = None
        else:
            parts_total = self.parts_total
        parts_total_before_discount: Optional[float]
        if not self.parts_total_before_discount:
            parts_total_before_discount = None
        else:
            parts_total_before_discount = self.parts_total_before_discount
        parent_manufacturer = self.parent_manufacturer
        parent_location = self.parent_location
        parent_manufacturer_part_number = self.parent_manufacturer_part_number
        parent_display_part_number = self.parent_display_part_number
        parent_asset_id: Optional[int]
        if not self.parent_asset_id:
            parent_asset_id = None
        else:
            parent_asset_id = self.parent_asset_id
        parent_category_name = self.parent_category_name
        parent_root_category_name = self.parent_root_category_name
        parent_serial_number = self.parent_serial_number
        parent_asset_tag = self.parent_asset_tag
        parent_asset_user = self.parent_asset_user
        parent_display_name = self.parent_display_name
        parent_equipment_id = self.parent_equipment_id
        asset_shipping_address_1 = self.asset_shipping_address_1
        asset_shipping_address_2 = self.asset_shipping_address_2
        asset_shipping_first_name = self.asset_shipping_first_name
        asset_shipping_last_name = self.asset_shipping_last_name
        asset_shipping_email = self.asset_shipping_email
        asset_shipping_company = self.asset_shipping_company
        asset_shipping_city = self.asset_shipping_city
        asset_shipping_zip = self.asset_shipping_zip
        asset_shipping_phone_number = self.asset_shipping_phone_number
        asset_shipping_fax_number = self.asset_shipping_fax_number
        asset_shipping_country = self.asset_shipping_country
        asset_shipping_state = self.asset_shipping_state
        shipping_address_1 = self.shipping_address_1
        shipping_address_2 = self.shipping_address_2
        shipping_first_name = self.shipping_first_name
        shipping_last_name = self.shipping_last_name
        shipping_email = self.shipping_email
        shipping_company = self.shipping_company
        shipping_city = self.shipping_city
        shipping_zip = self.shipping_zip
        shipping_phone_number = self.shipping_phone_number
        shipping_fax_number = self.shipping_fax_number
        shipping_country = self.shipping_country
        shipping_state = self.shipping_state
        asset_service_notes = self.asset_service_notes
        service_option_service_code = self.service_option_service_code
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if certificate_number is not None:
            field_dict["CertificateNumber"] = certificate_number
        if document_number is not None:
            field_dict["DocumentNumber"] = document_number
        if revision is not None:
            field_dict["Revision"] = revision
        if effective_date is not None:
            field_dict["EffectiveDate"] = effective_date
        if document_section is not None:
            field_dict["DocumentSection"] = document_section
        if service_level is not None:
            field_dict["ServiceLevel"] = service_level
        if service_level_code is not None:
            field_dict["ServiceLevelCode"] = service_level_code
        if service_type is not None:
            field_dict["ServiceType"] = service_type
        if order_item_number is not None:
            field_dict["OrderItemNumber"] = order_item_number
        if service_charge is not None:
            field_dict["ServiceCharge"] = service_charge
        if updated_by is not None:
            field_dict["UpdatedBy"] = updated_by
        if updated_on is not None:
            field_dict["UpdatedOn"] = updated_on
        if work_status is not None:
            field_dict["WorkStatus"] = work_status
        if custom_work_status is not None:
            field_dict["CustomWorkStatus"] = custom_work_status
        if service_comments is not None:
            field_dict["ServiceComments"] = service_comments
        if client_notes is not None:
            field_dict["ClientNotes"] = client_notes
        if vendor_service_notes is not None:
            field_dict["VendorServiceNotes"] = vendor_service_notes
        if display_name is not None:
            field_dict["DisplayName"] = display_name
        if display_part_number is not None:
            field_dict["DisplayPartNumber"] = display_part_number
        if part_number is not None:
            field_dict["PartNumber"] = part_number
        if schedule_name is not None:
            field_dict["ScheduleName"] = schedule_name
        if segment_name is not None:
            field_dict["SegmentName"] = segment_name
        if next_segment_name is not None:
            field_dict["NextSegmentName"] = next_segment_name
        if interval_length is not None:
            field_dict["IntervalLength"] = interval_length
        if interval_cycle is not None:
            field_dict["IntervalCycle"] = interval_cycle
        if service_options is not None:
            field_dict["ServiceOptions"] = service_options
        if service_options_price is not None:
            field_dict["ServiceOptionsPrice"] = service_options_price
        if service_options_document_numbers is not None:
            field_dict["ServiceOptionsDocumentNumbers"] = service_options_document_numbers
        if location is not None:
            field_dict["Location"] = location
        if station is not None:
            field_dict["Station"] = station
        if room is not None:
            field_dict["Room"] = room
        if site is not None:
            field_dict["Site"] = site
        if vendor_id is not None:
            field_dict["VendorId"] = vendor_id
        if service_order_number is not None:
            field_dict["ServiceOrderNumber"] = service_order_number
        if custom_order_number is not None:
            field_dict["CustomOrderNumber"] = custom_order_number
        if linked_order_number is not None:
            field_dict["LinkedOrderNumber"] = linked_order_number
        if asset_id is not None:
            field_dict["AssetId"] = asset_id
        if asset_class is not None:
            field_dict["AssetClass"] = asset_class
        if asset_condition is not None:
            field_dict["AssetCondition"] = asset_condition
        if asset_criticality is not None:
            field_dict["AssetCriticality"] = asset_criticality
        if asset_pool is not None:
            field_dict["AssetPool"] = asset_pool
        if asset_name is not None:
            field_dict["AssetName"] = asset_name
        if asset_description is not None:
            field_dict["AssetDescription"] = asset_description
        if asset_document_number is not None:
            field_dict["AssetDocumentNumber"] = asset_document_number
        if asset_document_section is not None:
            field_dict["AssetDocumentSection"] = asset_document_section
        if document_number_values is not None:
            field_dict["DocumentNumberValues"] = document_number_values
        if product_name is not None:
            field_dict["ProductName"] = product_name
        if product_description is not None:
            field_dict["ProductDescription"] = product_description
        if asset_maker is not None:
            field_dict["AssetMaker"] = asset_maker
        if category_name is not None:
            field_dict["CategoryName"] = category_name
        if root_category_name is not None:
            field_dict["RootCategoryName"] = root_category_name
        if vendor_tag is not None:
            field_dict["VendorTag"] = vendor_tag
        if result_status is not None:
            field_dict["ResultStatus"] = result_status
        if service_date is not None:
            field_dict["ServiceDate"] = service_date
        if next_service_date is not None:
            field_dict["NextServiceDate"] = next_service_date
        if original_due_date is not None:
            field_dict["OriginalDueDate"] = original_due_date
        if asset_tag is not None:
            field_dict["AssetTag"] = asset_tag
        if department is not None:
            field_dict["Department"] = department
        if asset_user is not None:
            field_dict["AssetUser"] = asset_user
        if equipment_id is not None:
            field_dict["EquipmentId"] = equipment_id
        if legacy_identifier is not None:
            field_dict["LegacyIdentifier"] = legacy_identifier
        if activation_date is not None:
            field_dict["ActivationDate"] = activation_date
        if purchase_date is not None:
            field_dict["PurchaseDate"] = purchase_date
        if part_name is not None:
            field_dict["PartName"] = part_name
        if part_description is not None:
            field_dict["PartDescription"] = part_description
        if is_taxable is not None:
            field_dict["IsTaxable"] = is_taxable
        if is_limited is not None:
            field_dict["IsLimited"] = is_limited
        if quantity is not None:
            field_dict["Quantity"] = quantity
        if discount is not None:
            field_dict["Discount"] = discount
        if price is not None:
            field_dict["Price"] = price
        if time_spent_in_minutes is not None:
            field_dict["TimeSpentInMinutes"] = time_spent_in_minutes
        if is_hourly_pricing is not None:
            field_dict["IsHourlyPricing"] = is_hourly_pricing
        if delivery_charge is not None:
            field_dict["DeliveryCharge"] = delivery_charge
        if serial_number is not None:
            field_dict["SerialNumber"] = serial_number
        if part_repair_charges is not None:
            field_dict["PartRepairCharges"] = part_repair_charges
        if part_repair_price is not None:
            field_dict["PartRepairPrice"] = part_repair_price
        if override_parts_total is not None:
            field_dict["OverridePartsTotal"] = override_parts_total
        if override_repairs_total is not None:
            field_dict["OverrideRepairsTotal"] = override_repairs_total
        if asset_custodian_name is not None:
            field_dict["AssetCustodianName"] = asset_custodian_name
        if as_found_specification_group_name is not None:
            field_dict["AsFoundSpecificationGroupName"] = as_found_specification_group_name
        if as_found_specification_company_name is not None:
            field_dict["AsFoundSpecificationCompanyName"] = as_found_specification_company_name
        if as_left_specification_group_name is not None:
            field_dict["AsLeftSpecificationGroupName"] = as_left_specification_group_name
        if as_left_specification_company_name is not None:
            field_dict["AsLeftSpecificationCompanyName"] = as_left_specification_company_name
        if order_id is not None:
            field_dict["OrderId"] = order_id
        if parent_order_id is not None:
            field_dict["ParentOrderId"] = parent_order_id
        if order_item_id is not None:
            field_dict["OrderItemId"] = order_item_id
        if order_item_part_id is not None:
            field_dict["OrderItemPartId"] = order_item_part_id
        if as_found_specification_group_id is not None:
            field_dict["AsFoundSpecificationGroupId"] = as_found_specification_group_id
        if as_left_specification_group_id is not None:
            field_dict["AsLeftSpecificationGroupId"] = as_left_specification_group_id
        if as_found_status is not None:
            field_dict["AsFoundStatus"] = as_found_status
        if as_left_status is not None:
            field_dict["AsLeftStatus"] = as_left_status
        if as_found_result is not None:
            field_dict["AsFoundResult"] = as_found_result
        if as_left_result is not None:
            field_dict["AsLeftResult"] = as_left_result
        if completed_on is not None:
            field_dict["CompletedOn"] = completed_on
        if received_on is not None:
            field_dict["ReceivedOn"] = received_on
        if completed_by_name is not None:
            field_dict["CompletedByName"] = completed_by_name
        if service_charge_base is not None:
            field_dict["ServiceChargeBase"] = service_charge_base
        if service_total is not None:
            field_dict["ServiceTotal"] = service_total
        if repairs_total is not None:
            field_dict["RepairsTotal"] = repairs_total
        if parts_total is not None:
            field_dict["PartsTotal"] = parts_total
        if parts_total_before_discount is not None:
            field_dict["PartsTotalBeforeDiscount"] = parts_total_before_discount
        if parent_manufacturer is not None:
            field_dict["ParentManufacturer"] = parent_manufacturer
        if parent_location is not None:
            field_dict["ParentLocation"] = parent_location
        if parent_manufacturer_part_number is not None:
            field_dict["ParentManufacturerPartNumber"] = parent_manufacturer_part_number
        if parent_display_part_number is not None:
            field_dict["ParentDisplayPartNumber"] = parent_display_part_number
        if parent_asset_id is not None:
            field_dict["ParentAssetId"] = parent_asset_id
        if parent_category_name is not None:
            field_dict["ParentCategoryName"] = parent_category_name
        if parent_root_category_name is not None:
            field_dict["ParentRootCategoryName"] = parent_root_category_name
        if parent_serial_number is not None:
            field_dict["ParentSerialNumber"] = parent_serial_number
        if parent_asset_tag is not None:
            field_dict["ParentAssetTag"] = parent_asset_tag
        if parent_asset_user is not None:
            field_dict["ParentAssetUser"] = parent_asset_user
        if parent_display_name is not None:
            field_dict["ParentDisplayName"] = parent_display_name
        if parent_equipment_id is not None:
            field_dict["ParentEquipmentId"] = parent_equipment_id
        if asset_shipping_address_1 is not None:
            field_dict["AssetShippingAddress1"] = asset_shipping_address_1
        if asset_shipping_address_2 is not None:
            field_dict["AssetShippingAddress2"] = asset_shipping_address_2
        if asset_shipping_first_name is not None:
            field_dict["AssetShippingFirstName"] = asset_shipping_first_name
        if asset_shipping_last_name is not None:
            field_dict["AssetShippingLastName"] = asset_shipping_last_name
        if asset_shipping_email is not None:
            field_dict["AssetShippingEmail"] = asset_shipping_email
        if asset_shipping_company is not None:
            field_dict["AssetShippingCompany"] = asset_shipping_company
        if asset_shipping_city is not None:
            field_dict["AssetShippingCity"] = asset_shipping_city
        if asset_shipping_zip is not None:
            field_dict["AssetShippingZip"] = asset_shipping_zip
        if asset_shipping_phone_number is not None:
            field_dict["AssetShippingPhoneNumber"] = asset_shipping_phone_number
        if asset_shipping_fax_number is not None:
            field_dict["AssetShippingFaxNumber"] = asset_shipping_fax_number
        if asset_shipping_country is not None:
            field_dict["AssetShippingCountry"] = asset_shipping_country
        if asset_shipping_state is not None:
            field_dict["AssetShippingState"] = asset_shipping_state
        if shipping_address_1 is not None:
            field_dict["ShippingAddress1"] = shipping_address_1
        if shipping_address_2 is not None:
            field_dict["ShippingAddress2"] = shipping_address_2
        if shipping_first_name is not None:
            field_dict["ShippingFirstName"] = shipping_first_name
        if shipping_last_name is not None:
            field_dict["ShippingLastName"] = shipping_last_name
        if shipping_email is not None:
            field_dict["ShippingEmail"] = shipping_email
        if shipping_company is not None:
            field_dict["ShippingCompany"] = shipping_company
        if shipping_city is not None:
            field_dict["ShippingCity"] = shipping_city
        if shipping_zip is not None:
            field_dict["ShippingZip"] = shipping_zip
        if shipping_phone_number is not None:
            field_dict["ShippingPhoneNumber"] = shipping_phone_number
        if shipping_fax_number is not None:
            field_dict["ShippingFaxNumber"] = shipping_fax_number
        if shipping_country is not None:
            field_dict["ShippingCountry"] = shipping_country
        if shipping_state is not None:
            field_dict["ShippingState"] = shipping_state
        if asset_service_notes is not None:
            field_dict["AssetServiceNotes"] = asset_service_notes
        if service_option_service_code is not None:
            field_dict["ServiceOptionServiceCode"] = service_option_service_code
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        certificate_number = d.pop("CertificateNumber", None)
        document_number = d.pop("DocumentNumber", None)
        revision = d.pop("Revision", None)
        def _parse_effective_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_date_type_0 = isoparse(data)
                return effective_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)
        effective_date = _parse_effective_date(d.pop("EffectiveDate", None))
        document_section = d.pop("DocumentSection", None)
        service_level = d.pop("ServiceLevel", None)
        service_level_code = d.pop("ServiceLevelCode", None)
        service_type = d.pop("ServiceType", None)
        order_item_number = d.pop("OrderItemNumber", None)
        service_charge = d.pop("ServiceCharge", None)
        updated_by = d.pop("UpdatedBy", None)
        _updated_on = d.pop("UpdatedOn", None)
        updated_on: Optional[datetime.datetime]
        if not _updated_on:
            updated_on = None
        else:
            updated_on = isoparse(_updated_on)
        _work_status = d.pop("WorkStatus", None)
        work_status: Optional[WorkStatus]
        if not _work_status:
            work_status = None
        elif _work_status is None:
            work_status = None
        else:
            work_status = WorkStatus(_work_status)
        custom_work_status = d.pop("CustomWorkStatus", None)
        service_comments = d.pop("ServiceComments", None)
        client_notes = d.pop("ClientNotes", None)
        vendor_service_notes = d.pop("VendorServiceNotes", None)
        display_name = d.pop("DisplayName", None)
        display_part_number = d.pop("DisplayPartNumber", None)
        part_number = d.pop("PartNumber", None)
        schedule_name = d.pop("ScheduleName", None)
        segment_name = d.pop("SegmentName", None)
        next_segment_name = d.pop("NextSegmentName", None)
        interval_length = d.pop("IntervalLength", None)
        interval_cycle = d.pop("IntervalCycle", None)
        service_options = d.pop("ServiceOptions", None)
        service_options_price = d.pop("ServiceOptionsPrice", None)
        service_options_document_numbers = d.pop("ServiceOptionsDocumentNumbers", None)
        location = d.pop("Location", None)
        station = d.pop("Station", None)
        room = d.pop("Room", None)
        site = d.pop("Site", None)
        vendor_id = d.pop("VendorId", None)
        service_order_number = d.pop("ServiceOrderNumber", None)
        custom_order_number = d.pop("CustomOrderNumber", None)
        linked_order_number = d.pop("LinkedOrderNumber", None)
        asset_id = d.pop("AssetId", None)
        asset_class = d.pop("AssetClass", None)
        asset_condition = d.pop("AssetCondition", None)
        asset_criticality = d.pop("AssetCriticality", None)
        asset_pool = d.pop("AssetPool", None)
        asset_name = d.pop("AssetName", None)
        asset_description = d.pop("AssetDescription", None)
        asset_document_number = d.pop("AssetDocumentNumber", None)
        asset_document_section = d.pop("AssetDocumentSection", None)
        document_number_values = d.pop("DocumentNumberValues", None)
        product_name = d.pop("ProductName", None)
        product_description = d.pop("ProductDescription", None)
        asset_maker = d.pop("AssetMaker", None)
        category_name = d.pop("CategoryName", None)
        root_category_name = d.pop("RootCategoryName", None)
        vendor_tag = d.pop("VendorTag", None)
        def _parse_result_status(data: object) -> Optional[int]:
            if not data:
                return None
            return cast(Optional[int], data)
        result_status = _parse_result_status(d.pop("ResultStatus", None))
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
        def _parse_original_due_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                original_due_date_type_0 = isoparse(data)
                return original_due_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)
        original_due_date = _parse_original_due_date(d.pop("OriginalDueDate", None))
        def _parse_asset_tag(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        asset_tag = _parse_asset_tag(d.pop("AssetTag", None))
        def _parse_department(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        department = _parse_department(d.pop("Department", None))
        def _parse_asset_user(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        asset_user = _parse_asset_user(d.pop("AssetUser", None))
        def _parse_equipment_id(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        equipment_id = _parse_equipment_id(d.pop("EquipmentId", None))
        def _parse_legacy_identifier(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        legacy_identifier = _parse_legacy_identifier(d.pop("LegacyIdentifier", None))
        def _parse_activation_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                activation_date_type_0 = isoparse(data)
                return activation_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)
        activation_date = _parse_activation_date(d.pop("ActivationDate", None))
        def _parse_purchase_date(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                purchase_date_type_0 = isoparse(data)
                return purchase_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)
        purchase_date = _parse_purchase_date(d.pop("PurchaseDate", None))
        def _parse_part_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        part_name = _parse_part_name(d.pop("PartName", None))
        def _parse_part_description(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        part_description = _parse_part_description(d.pop("PartDescription", None))
        is_taxable = d.pop("IsTaxable", None)
        is_limited = d.pop("IsLimited", None)
        def _parse_quantity(data: object) -> Optional[float]:
            if not data:
                return None
            return cast(Optional[float], data)
        quantity = _parse_quantity(d.pop("Quantity", None))
        def _parse_discount(data: object) -> Optional[float]:
            if not data:
                return None
            return cast(Optional[float], data)
        discount = _parse_discount(d.pop("Discount", None))
        def _parse_price(data: object) -> Optional[float]:
            if not data:
                return None
            return cast(Optional[float], data)
        price = _parse_price(d.pop("Price", None))
        def _parse_time_spent_in_minutes(data: object) -> Optional[float]:
            if not data:
                return None
            return cast(Optional[float], data)
        time_spent_in_minutes = _parse_time_spent_in_minutes(d.pop("TimeSpentInMinutes", None))
        def _parse_is_hourly_pricing(data: object) -> Optional[bool]:
            if not data:
                return None
            return cast(Optional[bool], data)
        is_hourly_pricing = _parse_is_hourly_pricing(d.pop("IsHourlyPricing", None))
        def _parse_delivery_charge(data: object) -> Optional[float]:
            if not data:
                return None
            return cast(Optional[float], data)
        delivery_charge = _parse_delivery_charge(d.pop("DeliveryCharge", None))
        serial_number = d.pop("SerialNumber", None)
        def _parse_part_repair_charges(data: object) -> Optional[float]:
            if not data:
                return None
            return cast(Optional[float], data)
        part_repair_charges = _parse_part_repair_charges(d.pop("PartRepairCharges", None))
        def _parse_part_repair_price(data: object) -> Optional[float]:
            if not data:
                return None
            return cast(Optional[float], data)
        part_repair_price = _parse_part_repair_price(d.pop("PartRepairPrice", None))
        override_parts_total = d.pop("OverridePartsTotal", None)
        override_repairs_total = d.pop("OverrideRepairsTotal", None)
        def _parse_asset_custodian_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        asset_custodian_name = _parse_asset_custodian_name(d.pop("AssetCustodianName", None))
        def _parse_as_found_specification_group_name(
            data: object,
        ) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        as_found_specification_group_name = _parse_as_found_specification_group_name(
            d.pop("AsFoundSpecificationGroupName", None)
        )
        def _parse_as_found_specification_company_name(
            data: object,
        ) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        as_found_specification_company_name = _parse_as_found_specification_company_name(
            d.pop("AsFoundSpecificationCompanyName", None)
        )
        def _parse_as_left_specification_group_name(
            data: object,
        ) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        as_left_specification_group_name = _parse_as_left_specification_group_name(
            d.pop("AsLeftSpecificationGroupName", None)
        )
        def _parse_as_left_specification_company_name(
            data: object,
        ) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        as_left_specification_company_name = _parse_as_left_specification_company_name(
            d.pop("AsLeftSpecificationCompanyName", None)
        )
        def _parse_order_id(data: object) -> Optional[int]:
            if not data:
                return None
            return cast(Optional[int], data)
        order_id = _parse_order_id(d.pop("OrderId", None))
        def _parse_parent_order_id(data: object) -> Optional[int]:
            if not data:
                return None
            return cast(Optional[int], data)
        parent_order_id = _parse_parent_order_id(d.pop("ParentOrderId", None))
        def _parse_order_item_id(data: object) -> Optional[int]:
            if not data:
                return None
            return cast(Optional[int], data)
        order_item_id = _parse_order_item_id(d.pop("OrderItemId", None))
        def _parse_order_item_part_id(data: object) -> Optional[int]:
            if not data:
                return None
            return cast(Optional[int], data)
        order_item_part_id = _parse_order_item_part_id(d.pop("OrderItemPartId", None))
        def _parse_as_found_specification_group_id(
            data: object,
        ) -> Optional[int]:
            if not data:
                return None
            return cast(Optional[int], data)
        as_found_specification_group_id = _parse_as_found_specification_group_id(
            d.pop("AsFoundSpecificationGroupId", None)
        )
        def _parse_as_left_specification_group_id(
            data: object,
        ) -> Optional[int]:
            if not data:
                return None
            return cast(Optional[int], data)
        as_left_specification_group_id = _parse_as_left_specification_group_id(
            d.pop("AsLeftSpecificationGroupId", None)
        )
        def _parse_as_found_status(data: object) -> Optional[int]:
            if not data:
                return None
            return cast(Optional[int], data)
        as_found_status = _parse_as_found_status(d.pop("AsFoundStatus", None))
        def _parse_as_left_status(data: object) -> Optional[int]:
            if not data:
                return None
            return cast(Optional[int], data)
        as_left_status = _parse_as_left_status(d.pop("AsLeftStatus", None))
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
        def _parse_received_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                received_on_type_0 = isoparse(data)
                return received_on_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)
        received_on = _parse_received_on(d.pop("ReceivedOn", None))
        def _parse_completed_by_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        completed_by_name = _parse_completed_by_name(d.pop("CompletedByName", None))
        def _parse_service_charge_base(data: object) -> Optional[float]:
            if not data:
                return None
            return cast(Optional[float], data)
        service_charge_base = _parse_service_charge_base(d.pop("ServiceChargeBase", None))
        def _parse_service_total(data: object) -> Optional[float]:
            if not data:
                return None
            return cast(Optional[float], data)
        service_total = _parse_service_total(d.pop("ServiceTotal", None))
        def _parse_repairs_total(data: object) -> Optional[float]:
            if not data:
                return None
            return cast(Optional[float], data)
        repairs_total = _parse_repairs_total(d.pop("RepairsTotal", None))
        def _parse_parts_total(data: object) -> Optional[float]:
            if not data:
                return None
            return cast(Optional[float], data)
        parts_total = _parse_parts_total(d.pop("PartsTotal", None))
        def _parse_parts_total_before_discount(
            data: object,
        ) -> Optional[float]:
            if not data:
                return None
            return cast(Optional[float], data)
        parts_total_before_discount = _parse_parts_total_before_discount(
            d.pop("PartsTotalBeforeDiscount", None)
        )
        def _parse_parent_manufacturer(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        parent_manufacturer = _parse_parent_manufacturer(d.pop("ParentManufacturer", None))
        def _parse_parent_location(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        parent_location = _parse_parent_location(d.pop("ParentLocation", None))
        def _parse_parent_manufacturer_part_number(
            data: object,
        ) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        parent_manufacturer_part_number = _parse_parent_manufacturer_part_number(
            d.pop("ParentManufacturerPartNumber", None)
        )
        def _parse_parent_display_part_number(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        parent_display_part_number = _parse_parent_display_part_number(
            d.pop("ParentDisplayPartNumber", None)
        )
        def _parse_parent_asset_id(data: object) -> Optional[int]:
            if not data:
                return None
            return cast(Optional[int], data)
        parent_asset_id = _parse_parent_asset_id(d.pop("ParentAssetId", None))
        def _parse_parent_category_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        parent_category_name = _parse_parent_category_name(d.pop("ParentCategoryName", None))
        def _parse_parent_root_category_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        parent_root_category_name = _parse_parent_root_category_name(
            d.pop("ParentRootCategoryName", None)
        )
        def _parse_parent_serial_number(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        parent_serial_number = _parse_parent_serial_number(d.pop("ParentSerialNumber", None))
        def _parse_parent_asset_tag(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        parent_asset_tag = _parse_parent_asset_tag(d.pop("ParentAssetTag", None))
        def _parse_parent_asset_user(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        parent_asset_user = _parse_parent_asset_user(d.pop("ParentAssetUser", None))
        def _parse_parent_display_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        parent_display_name = _parse_parent_display_name(d.pop("ParentDisplayName", None))
        def _parse_parent_equipment_id(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        parent_equipment_id = _parse_parent_equipment_id(d.pop("ParentEquipmentId", None))
        def _parse_asset_shipping_address_1(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        asset_shipping_address_1 = _parse_asset_shipping_address_1(
            d.pop("AssetShippingAddress1", None)
        )
        def _parse_asset_shipping_address_2(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        asset_shipping_address_2 = _parse_asset_shipping_address_2(
            d.pop("AssetShippingAddress2", None)
        )
        def _parse_asset_shipping_first_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        asset_shipping_first_name = _parse_asset_shipping_first_name(
            d.pop("AssetShippingFirstName", None)
        )
        def _parse_asset_shipping_last_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        asset_shipping_last_name = _parse_asset_shipping_last_name(
            d.pop("AssetShippingLastName", None)
        )
        def _parse_asset_shipping_email(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        asset_shipping_email = _parse_asset_shipping_email(d.pop("AssetShippingEmail", None))
        def _parse_asset_shipping_company(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        asset_shipping_company = _parse_asset_shipping_company(d.pop("AssetShippingCompany", None))
        def _parse_asset_shipping_city(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        asset_shipping_city = _parse_asset_shipping_city(d.pop("AssetShippingCity", None))
        def _parse_asset_shipping_zip(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        asset_shipping_zip = _parse_asset_shipping_zip(d.pop("AssetShippingZip", None))
        def _parse_asset_shipping_phone_number(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        asset_shipping_phone_number = _parse_asset_shipping_phone_number(
            d.pop("AssetShippingPhoneNumber", None)
        )
        def _parse_asset_shipping_fax_number(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        asset_shipping_fax_number = _parse_asset_shipping_fax_number(
            d.pop("AssetShippingFaxNumber", None)
        )
        def _parse_asset_shipping_country(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        asset_shipping_country = _parse_asset_shipping_country(d.pop("AssetShippingCountry", None))
        def _parse_asset_shipping_state(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        asset_shipping_state = _parse_asset_shipping_state(d.pop("AssetShippingState", None))
        def _parse_shipping_address_1(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        shipping_address_1 = _parse_shipping_address_1(d.pop("ShippingAddress1", None))
        def _parse_shipping_address_2(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        shipping_address_2 = _parse_shipping_address_2(d.pop("ShippingAddress2", None))
        def _parse_shipping_first_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        shipping_first_name = _parse_shipping_first_name(d.pop("ShippingFirstName", None))
        def _parse_shipping_last_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        shipping_last_name = _parse_shipping_last_name(d.pop("ShippingLastName", None))
        def _parse_shipping_email(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        shipping_email = _parse_shipping_email(d.pop("ShippingEmail", None))
        def _parse_shipping_company(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        shipping_company = _parse_shipping_company(d.pop("ShippingCompany", None))
        def _parse_shipping_city(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        shipping_city = _parse_shipping_city(d.pop("ShippingCity", None))
        def _parse_shipping_zip(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        shipping_zip = _parse_shipping_zip(d.pop("ShippingZip", None))
        def _parse_shipping_phone_number(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        shipping_phone_number = _parse_shipping_phone_number(d.pop("ShippingPhoneNumber", None))
        def _parse_shipping_fax_number(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        shipping_fax_number = _parse_shipping_fax_number(d.pop("ShippingFaxNumber", None))
        def _parse_shipping_country(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        shipping_country = _parse_shipping_country(d.pop("ShippingCountry", None))
        def _parse_shipping_state(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        shipping_state = _parse_shipping_state(d.pop("ShippingState", None))
        def _parse_asset_service_notes(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        asset_service_notes = _parse_asset_service_notes(d.pop("AssetServiceNotes", None))
        def _parse_service_option_service_code(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)
        service_option_service_code = _parse_service_option_service_code(
            d.pop("ServiceOptionServiceCode", None)
        )
        qualer_api_models_report_datasets_to_service_order_item_response = cls(
            certificate_number=certificate_number,
            document_number=document_number,
            revision=revision,
            effective_date=effective_date,
            document_section=document_section,
            service_level=service_level,
            service_level_code=service_level_code,
            service_type=service_type,
            order_item_number=order_item_number,
            service_charge=service_charge,
            updated_by=updated_by,
            updated_on=updated_on,
            work_status=work_status,
            custom_work_status=custom_work_status,
            service_comments=service_comments,
            client_notes=client_notes,
            vendor_service_notes=vendor_service_notes,
            display_name=display_name,
            display_part_number=display_part_number,
            part_number=part_number,
            schedule_name=schedule_name,
            segment_name=segment_name,
            next_segment_name=next_segment_name,
            interval_length=interval_length,
            interval_cycle=interval_cycle,
            service_options=service_options,
            service_options_price=service_options_price,
            service_options_document_numbers=service_options_document_numbers,
            location=location,
            station=station,
            room=room,
            site=site,
            vendor_id=vendor_id,
            service_order_number=service_order_number,
            custom_order_number=custom_order_number,
            linked_order_number=linked_order_number,
            asset_id=asset_id,
            asset_class=asset_class,
            asset_condition=asset_condition,
            asset_criticality=asset_criticality,
            asset_pool=asset_pool,
            asset_name=asset_name,
            asset_description=asset_description,
            asset_document_number=asset_document_number,
            asset_document_section=asset_document_section,
            document_number_values=document_number_values,
            product_name=product_name,
            product_description=product_description,
            asset_maker=asset_maker,
            category_name=category_name,
            root_category_name=root_category_name,
            vendor_tag=vendor_tag,
            result_status=result_status,
            service_date=service_date,
            next_service_date=next_service_date,
            original_due_date=original_due_date,
            asset_tag=asset_tag,
            department=department,
            asset_user=asset_user,
            equipment_id=equipment_id,
            legacy_identifier=legacy_identifier,
            activation_date=activation_date,
            purchase_date=purchase_date,
            part_name=part_name,
            part_description=part_description,
            is_taxable=is_taxable,
            is_limited=is_limited,
            quantity=quantity,
            discount=discount,
            price=price,
            time_spent_in_minutes=time_spent_in_minutes,
            is_hourly_pricing=is_hourly_pricing,
            delivery_charge=delivery_charge,
            serial_number=serial_number,
            part_repair_charges=part_repair_charges,
            part_repair_price=part_repair_price,
            override_parts_total=override_parts_total,
            override_repairs_total=override_repairs_total,
            asset_custodian_name=asset_custodian_name,
            as_found_specification_group_name=as_found_specification_group_name,
            as_found_specification_company_name=as_found_specification_company_name,
            as_left_specification_group_name=as_left_specification_group_name,
            as_left_specification_company_name=as_left_specification_company_name,
            order_id=order_id,
            parent_order_id=parent_order_id,
            order_item_id=order_item_id,
            order_item_part_id=order_item_part_id,
            as_found_specification_group_id=as_found_specification_group_id,
            as_left_specification_group_id=as_left_specification_group_id,
            as_found_status=as_found_status,
            as_left_status=as_left_status,
            as_found_result=as_found_result,
            as_left_result=as_left_result,
            completed_on=completed_on,
            received_on=received_on,
            completed_by_name=completed_by_name,
            service_charge_base=service_charge_base,
            service_total=service_total,
            repairs_total=repairs_total,
            parts_total=parts_total,
            parts_total_before_discount=parts_total_before_discount,
            parent_manufacturer=parent_manufacturer,
            parent_location=parent_location,
            parent_manufacturer_part_number=parent_manufacturer_part_number,
            parent_display_part_number=parent_display_part_number,
            parent_asset_id=parent_asset_id,
            parent_category_name=parent_category_name,
            parent_root_category_name=parent_root_category_name,
            parent_serial_number=parent_serial_number,
            parent_asset_tag=parent_asset_tag,
            parent_asset_user=parent_asset_user,
            parent_display_name=parent_display_name,
            parent_equipment_id=parent_equipment_id,
            asset_shipping_address_1=asset_shipping_address_1,
            asset_shipping_address_2=asset_shipping_address_2,
            asset_shipping_first_name=asset_shipping_first_name,
            asset_shipping_last_name=asset_shipping_last_name,
            asset_shipping_email=asset_shipping_email,
            asset_shipping_company=asset_shipping_company,
            asset_shipping_city=asset_shipping_city,
            asset_shipping_zip=asset_shipping_zip,
            asset_shipping_phone_number=asset_shipping_phone_number,
            asset_shipping_fax_number=asset_shipping_fax_number,
            asset_shipping_country=asset_shipping_country,
            asset_shipping_state=asset_shipping_state,
            shipping_address_1=shipping_address_1,
            shipping_address_2=shipping_address_2,
            shipping_first_name=shipping_first_name,
            shipping_last_name=shipping_last_name,
            shipping_email=shipping_email,
            shipping_company=shipping_company,
            shipping_city=shipping_city,
            shipping_zip=shipping_zip,
            shipping_phone_number=shipping_phone_number,
            shipping_fax_number=shipping_fax_number,
            shipping_country=shipping_country,
            shipping_state=shipping_state,
            asset_service_notes=asset_service_notes,
            service_option_service_code=service_option_service_code,
        )
        qualer_api_models_report_datasets_to_service_order_item_response.additional_properties = d
        return qualer_api_models_report_datasets_to_service_order_item_response

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
