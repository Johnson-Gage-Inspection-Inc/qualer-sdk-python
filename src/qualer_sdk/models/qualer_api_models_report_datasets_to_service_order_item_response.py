import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsReportDatasetsToServiceOrderItemResponse")


@_attrs_define
class QualerApiModelsReportDatasetsToServiceOrderItemResponse:
    """
    Attributes:
        certificate_number (Union[Unset, str]):
        document_number (Union[Unset, str]):
        revision (Union[Unset, str]):
        effective_date (Union[None, Unset, datetime.datetime]):
        document_section (Union[Unset, str]):
        service_level (Union[Unset, str]):
        service_level_code (Union[Unset, str]):
        service_type (Union[Unset, str]):
        order_item_number (Union[Unset, int]):
        service_charge (Union[Unset, float]):
        updated_by (Union[Unset, str]):
        updated_on (Union[None, Unset, datetime.datetime]):
        work_status (Union[Unset, int]):
        custom_work_status (Union[Unset, str]):
        service_comments (Union[Unset, str]):
        client_notes (Union[Unset, str]):
        vendor_service_notes (Union[Unset, str]):
        display_name (Union[Unset, str]):
        display_part_number (Union[Unset, str]):
        part_number (Union[Unset, str]):
        schedule_name (Union[Unset, str]):
        segment_name (Union[Unset, str]):
        next_segment_name (Union[Unset, str]):
        interval_length (Union[Unset, int]):
        interval_cycle (Union[Unset, str]):
        service_options (Union[Unset, str]):
        service_options_price (Union[Unset, str]):
        service_options_document_numbers (Union[Unset, str]):
        location (Union[Unset, str]):
        station (Union[Unset, str]):
        room (Union[Unset, str]):
        site (Union[Unset, str]):
        vendor_id (Union[Unset, int]):
        service_order_number (Union[Unset, int]):
        custom_order_number (Union[Unset, str]):
        linked_order_number (Union[Unset, str]):
        asset_id (Union[Unset, int]):
        asset_class (Union[Unset, str]):
        asset_condition (Union[Unset, str]):
        asset_criticality (Union[Unset, str]):
        asset_pool (Union[Unset, str]):
        asset_name (Union[Unset, str]):
        asset_description (Union[Unset, str]):
        asset_document_number (Union[Unset, str]):
        asset_document_section (Union[Unset, str]):
        document_number_values (Union[Unset, str]):
        product_name (Union[Unset, str]):
        product_description (Union[Unset, str]):
        asset_maker (Union[Unset, str]):
        category_name (Union[Unset, str]):
        root_category_name (Union[Unset, str]):
        vendor_tag (Union[Unset, str]):
        result_status (Union[None, Unset, int]):
        service_date (Union[None, Unset, datetime.datetime]):
        next_service_date (Union[None, Unset, datetime.datetime]):
        original_due_date (Union[None, Unset, datetime.datetime]):
        asset_tag (Union[None, Unset, str]):
        department (Union[None, Unset, str]):
        asset_user (Union[None, Unset, str]):
        equipment_id (Union[None, Unset, str]):
        legacy_identifier (Union[None, Unset, str]):
        activation_date (Union[None, Unset, datetime.datetime]):
        purchase_date (Union[None, Unset, datetime.datetime]):
        part_name (Union[None, Unset, str]):
        part_description (Union[None, Unset, str]):
        is_taxable (Union[Unset, bool]):
        is_limited (Union[Unset, bool]):
        quantity (Union[None, Unset, float]):
        discount (Union[None, Unset, float]):
        price (Union[None, Unset, float]):
        time_spent_in_minutes (Union[None, Unset, float]):
        is_hourly_pricing (Union[None, Unset, bool]):
        delivery_charge (Union[None, Unset, float]):
        serial_number (Union[Unset, str]):
        part_repair_charges (Union[None, Unset, float]):
        part_repair_price (Union[None, Unset, float]):
        override_parts_total (Union[Unset, bool]):
        override_repairs_total (Union[Unset, bool]):
        asset_custodian_name (Union[None, Unset, str]):
        as_found_specification_group_name (Union[None, Unset, str]):
        as_found_specification_company_name (Union[None, Unset, str]):
        as_left_specification_group_name (Union[None, Unset, str]):
        as_left_specification_company_name (Union[None, Unset, str]):
        order_id (Union[None, Unset, int]):
        parent_order_id (Union[None, Unset, int]):
        order_item_id (Union[None, Unset, int]):
        order_item_part_id (Union[None, Unset, int]):
        as_found_specification_group_id (Union[None, Unset, int]):
        as_left_specification_group_id (Union[None, Unset, int]):
        as_found_status (Union[None, Unset, int]):
        as_left_status (Union[None, Unset, int]):
        as_found_result (Union[None, Unset, int]):
        as_left_result (Union[None, Unset, int]):
        completed_on (Union[None, Unset, datetime.datetime]):
        received_on (Union[None, Unset, datetime.datetime]):
        completed_by_name (Union[None, Unset, str]):
        service_charge_base (Union[None, Unset, float]):
        service_total (Union[None, Unset, float]):
        repairs_total (Union[None, Unset, float]):
        parts_total (Union[None, Unset, float]):
        parts_total_before_discount (Union[None, Unset, float]):
        parent_manufacturer (Union[None, Unset, str]):
        parent_location (Union[None, Unset, str]):
        parent_manufacturer_part_number (Union[None, Unset, str]):
        parent_display_part_number (Union[None, Unset, str]):
        parent_asset_id (Union[None, Unset, int]):
        parent_category_name (Union[None, Unset, str]):
        parent_root_category_name (Union[None, Unset, str]):
        parent_serial_number (Union[None, Unset, str]):
        parent_asset_tag (Union[None, Unset, str]):
        parent_asset_user (Union[None, Unset, str]):
        parent_display_name (Union[None, Unset, str]):
        parent_equipment_id (Union[None, Unset, str]):
        asset_shipping_address_1 (Union[None, Unset, str]):
        asset_shipping_address_2 (Union[None, Unset, str]):
        asset_shipping_first_name (Union[None, Unset, str]):
        asset_shipping_last_name (Union[None, Unset, str]):
        asset_shipping_email (Union[None, Unset, str]):
        asset_shipping_company (Union[None, Unset, str]):
        asset_shipping_city (Union[None, Unset, str]):
        asset_shipping_zip (Union[None, Unset, str]):
        asset_shipping_phone_number (Union[None, Unset, str]):
        asset_shipping_fax_number (Union[None, Unset, str]):
        asset_shipping_country (Union[None, Unset, str]):
        asset_shipping_state (Union[None, Unset, str]):
        shipping_address_1 (Union[None, Unset, str]):
        shipping_address_2 (Union[None, Unset, str]):
        shipping_first_name (Union[None, Unset, str]):
        shipping_last_name (Union[None, Unset, str]):
        shipping_email (Union[None, Unset, str]):
        shipping_company (Union[None, Unset, str]):
        shipping_city (Union[None, Unset, str]):
        shipping_zip (Union[None, Unset, str]):
        shipping_phone_number (Union[None, Unset, str]):
        shipping_fax_number (Union[None, Unset, str]):
        shipping_country (Union[None, Unset, str]):
        shipping_state (Union[None, Unset, str]):
        asset_service_notes (Union[None, Unset, str]):
        service_option_service_code (Union[None, Unset, str]):
    """

    certificate_number: Union[Unset, str] = UNSET
    document_number: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    effective_date: Union[None, Unset, datetime.datetime] = UNSET
    document_section: Union[Unset, str] = UNSET
    service_level: Union[Unset, str] = UNSET
    service_level_code: Union[Unset, str] = UNSET
    service_type: Union[Unset, str] = UNSET
    order_item_number: Union[Unset, int] = UNSET
    service_charge: Union[Unset, float] = UNSET
    updated_by: Union[Unset, str] = UNSET
    updated_on: Union[None, Unset, datetime.datetime] = UNSET
    work_status: Union[None, Unset, int] = UNSET
    custom_work_status: Union[Unset, str] = UNSET
    service_comments: Union[Unset, str] = UNSET
    client_notes: Union[Unset, str] = UNSET
    vendor_service_notes: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_part_number: Union[Unset, str] = UNSET
    part_number: Union[Unset, str] = UNSET
    schedule_name: Union[Unset, str] = UNSET
    segment_name: Union[Unset, str] = UNSET
    next_segment_name: Union[Unset, str] = UNSET
    interval_length: Union[Unset, int] = UNSET
    interval_cycle: Union[Unset, str] = UNSET
    service_options: Union[Unset, str] = UNSET
    service_options_price: Union[Unset, str] = UNSET
    service_options_document_numbers: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    station: Union[Unset, str] = UNSET
    room: Union[Unset, str] = UNSET
    site: Union[Unset, str] = UNSET
    vendor_id: Union[Unset, int] = UNSET
    service_order_number: Union[Unset, int] = UNSET
    custom_order_number: Union[Unset, str] = UNSET
    linked_order_number: Union[Unset, str] = UNSET
    asset_id: Union[Unset, int] = UNSET
    asset_class: Union[Unset, str] = UNSET
    asset_condition: Union[Unset, str] = UNSET
    asset_criticality: Union[Unset, str] = UNSET
    asset_pool: Union[Unset, str] = UNSET
    asset_name: Union[Unset, str] = UNSET
    asset_description: Union[Unset, str] = UNSET
    asset_document_number: Union[Unset, str] = UNSET
    asset_document_section: Union[Unset, str] = UNSET
    document_number_values: Union[Unset, str] = UNSET
    product_name: Union[Unset, str] = UNSET
    product_description: Union[Unset, str] = UNSET
    asset_maker: Union[Unset, str] = UNSET
    category_name: Union[Unset, str] = UNSET
    root_category_name: Union[Unset, str] = UNSET
    vendor_tag: Union[Unset, str] = UNSET
    result_status: Union[None, Unset, int] = UNSET
    service_date: Union[None, Unset, datetime.datetime] = UNSET
    next_service_date: Union[None, Unset, datetime.datetime] = UNSET
    original_due_date: Union[None, Unset, datetime.datetime] = UNSET
    asset_tag: Union[None, Unset, str] = UNSET
    department: Union[None, Unset, str] = UNSET
    asset_user: Union[None, Unset, str] = UNSET
    equipment_id: Union[None, Unset, str] = UNSET
    legacy_identifier: Union[None, Unset, str] = UNSET
    activation_date: Union[None, Unset, datetime.datetime] = UNSET
    purchase_date: Union[None, Unset, datetime.datetime] = UNSET
    part_name: Union[None, Unset, str] = UNSET
    part_description: Union[None, Unset, str] = UNSET
    is_taxable: Union[Unset, bool] = UNSET
    is_limited: Union[Unset, bool] = UNSET
    quantity: Union[None, Unset, float] = UNSET
    discount: Union[None, Unset, float] = UNSET
    price: Union[None, Unset, float] = UNSET
    time_spent_in_minutes: Union[None, Unset, float] = UNSET
    is_hourly_pricing: Union[None, Unset, bool] = UNSET
    delivery_charge: Union[None, Unset, float] = UNSET
    serial_number: Union[Unset, str] = UNSET
    part_repair_charges: Union[None, Unset, float] = UNSET
    part_repair_price: Union[None, Unset, float] = UNSET
    override_parts_total: Union[Unset, bool] = UNSET
    override_repairs_total: Union[Unset, bool] = UNSET
    asset_custodian_name: Union[None, Unset, str] = UNSET
    as_found_specification_group_name: Union[None, Unset, str] = UNSET
    as_found_specification_company_name: Union[None, Unset, str] = UNSET
    as_left_specification_group_name: Union[None, Unset, str] = UNSET
    as_left_specification_company_name: Union[None, Unset, str] = UNSET
    order_id: Union[None, Unset, int] = UNSET
    parent_order_id: Union[None, Unset, int] = UNSET
    order_item_id: Union[None, Unset, int] = UNSET
    order_item_part_id: Union[None, Unset, int] = UNSET
    as_found_specification_group_id: Union[None, Unset, int] = UNSET
    as_left_specification_group_id: Union[None, Unset, int] = UNSET
    as_found_status: Union[None, Unset, int] = UNSET
    as_left_status: Union[None, Unset, int] = UNSET
    as_found_result: Union[None, Unset, int] = UNSET
    as_left_result: Union[None, Unset, int] = UNSET
    completed_on: Union[None, Unset, datetime.datetime] = UNSET
    received_on: Union[None, Unset, datetime.datetime] = UNSET
    completed_by_name: Union[None, Unset, str] = UNSET
    service_charge_base: Union[None, Unset, float] = UNSET
    service_total: Union[None, Unset, float] = UNSET
    repairs_total: Union[None, Unset, float] = UNSET
    parts_total: Union[None, Unset, float] = UNSET
    parts_total_before_discount: Union[None, Unset, float] = UNSET
    parent_manufacturer: Union[None, Unset, str] = UNSET
    parent_location: Union[None, Unset, str] = UNSET
    parent_manufacturer_part_number: Union[None, Unset, str] = UNSET
    parent_display_part_number: Union[None, Unset, str] = UNSET
    parent_asset_id: Union[None, Unset, int] = UNSET
    parent_category_name: Union[None, Unset, str] = UNSET
    parent_root_category_name: Union[None, Unset, str] = UNSET
    parent_serial_number: Union[None, Unset, str] = UNSET
    parent_asset_tag: Union[None, Unset, str] = UNSET
    parent_asset_user: Union[None, Unset, str] = UNSET
    parent_display_name: Union[None, Unset, str] = UNSET
    parent_equipment_id: Union[None, Unset, str] = UNSET
    asset_shipping_address_1: Union[None, Unset, str] = UNSET
    asset_shipping_address_2: Union[None, Unset, str] = UNSET
    asset_shipping_first_name: Union[None, Unset, str] = UNSET
    asset_shipping_last_name: Union[None, Unset, str] = UNSET
    asset_shipping_email: Union[None, Unset, str] = UNSET
    asset_shipping_company: Union[None, Unset, str] = UNSET
    asset_shipping_city: Union[None, Unset, str] = UNSET
    asset_shipping_zip: Union[None, Unset, str] = UNSET
    asset_shipping_phone_number: Union[None, Unset, str] = UNSET
    asset_shipping_fax_number: Union[None, Unset, str] = UNSET
    asset_shipping_country: Union[None, Unset, str] = UNSET
    asset_shipping_state: Union[None, Unset, str] = UNSET
    shipping_address_1: Union[None, Unset, str] = UNSET
    shipping_address_2: Union[None, Unset, str] = UNSET
    shipping_first_name: Union[None, Unset, str] = UNSET
    shipping_last_name: Union[None, Unset, str] = UNSET
    shipping_email: Union[None, Unset, str] = UNSET
    shipping_company: Union[None, Unset, str] = UNSET
    shipping_city: Union[None, Unset, str] = UNSET
    shipping_zip: Union[None, Unset, str] = UNSET
    shipping_phone_number: Union[None, Unset, str] = UNSET
    shipping_fax_number: Union[None, Unset, str] = UNSET
    shipping_country: Union[None, Unset, str] = UNSET
    shipping_state: Union[None, Unset, str] = UNSET
    asset_service_notes: Union[None, Unset, str] = UNSET
    service_option_service_code: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        certificate_number = self.certificate_number

        document_number = self.document_number

        revision = self.revision

        effective_date: Union[None, Unset, str]
        if isinstance(self.effective_date, Unset):
            effective_date = UNSET
        elif isinstance(self.effective_date, datetime.datetime):
            effective_date = self.effective_date.isoformat()
        else:
            effective_date = self.effective_date

        document_section = self.document_section

        service_level = self.service_level

        service_level_code = self.service_level_code

        service_type = self.service_type

        order_item_number = self.order_item_number

        service_charge = self.service_charge

        updated_by = self.updated_by

        updated_on: Union[None, Unset, str]
        if isinstance(self.updated_on, Unset):
            updated_on = UNSET
        elif isinstance(self.updated_on, datetime.datetime):
            updated_on = self.updated_on.isoformat()
        else:
            updated_on = self.updated_on

        work_status: Union[None, Unset, str]

        if isinstance(self.work_status, Unset):

            work_status = UNSET

        else:

            work_status = self.work_status
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

        result_status: Union[None, Unset, int]
        if isinstance(self.result_status, Unset):
            result_status = UNSET
        else:
            result_status: Union[None, Unset, str]

            if isinstance(self.result_status, Unset):

                result_status = UNSET

            else:

                result_status = self.result_status
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

        original_due_date: Union[None, Unset, str]
        if isinstance(self.original_due_date, Unset):
            original_due_date = UNSET
        elif isinstance(self.original_due_date, datetime.datetime):
            original_due_date = self.original_due_date.isoformat()
        else:
            original_due_date = self.original_due_date

        asset_tag: Union[None, Unset, str]
        if isinstance(self.asset_tag, Unset):
            asset_tag = UNSET
        else:
            asset_tag = self.asset_tag

        department: Union[None, Unset, str]
        if isinstance(self.department, Unset):
            department = UNSET
        else:
            department = self.department

        asset_user: Union[None, Unset, str]
        if isinstance(self.asset_user, Unset):
            asset_user = UNSET
        else:
            asset_user = self.asset_user

        equipment_id: Union[None, Unset, str]
        if isinstance(self.equipment_id, Unset):
            equipment_id = UNSET
        else:
            equipment_id = self.equipment_id

        legacy_identifier: Union[None, Unset, str]
        if isinstance(self.legacy_identifier, Unset):
            legacy_identifier = UNSET
        else:
            legacy_identifier = self.legacy_identifier

        activation_date: Union[None, Unset, str]
        if isinstance(self.activation_date, Unset):
            activation_date = UNSET
        elif isinstance(self.activation_date, datetime.datetime):
            activation_date = self.activation_date.isoformat()
        else:
            activation_date = self.activation_date

        purchase_date: Union[None, Unset, str]
        if isinstance(self.purchase_date, Unset):
            purchase_date = UNSET
        elif isinstance(self.purchase_date, datetime.datetime):
            purchase_date = self.purchase_date.isoformat()
        else:
            purchase_date = self.purchase_date

        part_name: Union[None, Unset, str]
        if isinstance(self.part_name, Unset):
            part_name = UNSET
        else:
            part_name = self.part_name

        part_description: Union[None, Unset, str]
        if isinstance(self.part_description, Unset):
            part_description = UNSET
        else:
            part_description = self.part_description

        is_taxable = self.is_taxable

        is_limited = self.is_limited

        quantity: Union[None, Unset, float]
        if isinstance(self.quantity, Unset):
            quantity = UNSET
        else:
            quantity = self.quantity

        discount: Union[None, Unset, float]
        if isinstance(self.discount, Unset):
            discount = UNSET
        else:
            discount = self.discount

        price: Union[None, Unset, float]
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        time_spent_in_minutes: Union[None, Unset, float]
        if isinstance(self.time_spent_in_minutes, Unset):
            time_spent_in_minutes = UNSET
        else:
            time_spent_in_minutes = self.time_spent_in_minutes

        is_hourly_pricing: Union[None, Unset, bool]
        if isinstance(self.is_hourly_pricing, Unset):
            is_hourly_pricing = UNSET
        else:
            is_hourly_pricing = self.is_hourly_pricing

        delivery_charge: Union[None, Unset, float]
        if isinstance(self.delivery_charge, Unset):
            delivery_charge = UNSET
        else:
            delivery_charge = self.delivery_charge

        serial_number = self.serial_number

        part_repair_charges: Union[None, Unset, float]
        if isinstance(self.part_repair_charges, Unset):
            part_repair_charges = UNSET
        else:
            part_repair_charges = self.part_repair_charges

        part_repair_price: Union[None, Unset, float]
        if isinstance(self.part_repair_price, Unset):
            part_repair_price = UNSET
        else:
            part_repair_price = self.part_repair_price

        override_parts_total = self.override_parts_total

        override_repairs_total = self.override_repairs_total

        asset_custodian_name: Union[None, Unset, str]
        if isinstance(self.asset_custodian_name, Unset):
            asset_custodian_name = UNSET
        else:
            asset_custodian_name = self.asset_custodian_name

        as_found_specification_group_name: Union[None, Unset, str]
        if isinstance(self.as_found_specification_group_name, Unset):
            as_found_specification_group_name = UNSET
        else:
            as_found_specification_group_name = self.as_found_specification_group_name

        as_found_specification_company_name: Union[None, Unset, str]
        if isinstance(self.as_found_specification_company_name, Unset):
            as_found_specification_company_name = UNSET
        else:
            as_found_specification_company_name = (
                self.as_found_specification_company_name
            )

        as_left_specification_group_name: Union[None, Unset, str]
        if isinstance(self.as_left_specification_group_name, Unset):
            as_left_specification_group_name = UNSET
        else:
            as_left_specification_group_name = self.as_left_specification_group_name

        as_left_specification_company_name: Union[None, Unset, str]
        if isinstance(self.as_left_specification_company_name, Unset):
            as_left_specification_company_name = UNSET
        else:
            as_left_specification_company_name = self.as_left_specification_company_name

        order_id: Union[None, Unset, int]
        if isinstance(self.order_id, Unset):
            order_id = UNSET
        else:
            order_id = self.order_id

        parent_order_id: Union[None, Unset, int]
        if isinstance(self.parent_order_id, Unset):
            parent_order_id = UNSET
        else:
            parent_order_id = self.parent_order_id

        order_item_id: Union[None, Unset, int]
        if isinstance(self.order_item_id, Unset):
            order_item_id = UNSET
        else:
            order_item_id = self.order_item_id

        order_item_part_id: Union[None, Unset, int]
        if isinstance(self.order_item_part_id, Unset):
            order_item_part_id = UNSET
        else:
            order_item_part_id = self.order_item_part_id

        as_found_specification_group_id: Union[None, Unset, int]
        if isinstance(self.as_found_specification_group_id, Unset):
            as_found_specification_group_id = UNSET
        else:
            as_found_specification_group_id = self.as_found_specification_group_id

        as_left_specification_group_id: Union[None, Unset, int]
        if isinstance(self.as_left_specification_group_id, Unset):
            as_left_specification_group_id = UNSET
        else:
            as_left_specification_group_id = self.as_left_specification_group_id

        as_found_status: Union[None, Unset, int]
        if isinstance(self.as_found_status, Unset):
            as_found_status = UNSET
        else:
            as_found_status = self.as_found_status

        as_left_status: Union[None, Unset, int]
        if isinstance(self.as_left_status, Unset):
            as_left_status = UNSET
        else:
            as_left_status = self.as_left_status

        as_found_result: Union[None, Unset, int]
        if isinstance(self.as_found_result, Unset):
            as_found_result = UNSET
        else:
            as_found_result: Union[None, Unset, str]

            if isinstance(self.as_found_result, Unset):

                as_found_result = UNSET

            else:

                as_found_result = self.as_found_result
        as_left_result: Union[None, Unset, int]
        if isinstance(self.as_left_result, Unset):
            as_left_result = UNSET
        else:
            as_left_result: Union[None, Unset, str]

            if isinstance(self.as_left_result, Unset):

                as_left_result = UNSET

            else:

                as_left_result = self.as_left_result
        completed_on: Union[None, Unset, str]
        if isinstance(self.completed_on, Unset):
            completed_on = UNSET
        elif isinstance(self.completed_on, datetime.datetime):
            completed_on = self.completed_on.isoformat()
        else:
            completed_on = self.completed_on

        received_on: Union[None, Unset, str]
        if isinstance(self.received_on, Unset):
            received_on = UNSET
        elif isinstance(self.received_on, datetime.datetime):
            received_on = self.received_on.isoformat()
        else:
            received_on = self.received_on

        completed_by_name: Union[None, Unset, str]
        if isinstance(self.completed_by_name, Unset):
            completed_by_name = UNSET
        else:
            completed_by_name = self.completed_by_name

        service_charge_base: Union[None, Unset, float]
        if isinstance(self.service_charge_base, Unset):
            service_charge_base = UNSET
        else:
            service_charge_base = self.service_charge_base

        service_total: Union[None, Unset, float]
        if isinstance(self.service_total, Unset):
            service_total = UNSET
        else:
            service_total = self.service_total

        repairs_total: Union[None, Unset, float]
        if isinstance(self.repairs_total, Unset):
            repairs_total = UNSET
        else:
            repairs_total = self.repairs_total

        parts_total: Union[None, Unset, float]
        if isinstance(self.parts_total, Unset):
            parts_total = UNSET
        else:
            parts_total = self.parts_total

        parts_total_before_discount: Union[None, Unset, float]
        if isinstance(self.parts_total_before_discount, Unset):
            parts_total_before_discount = UNSET
        else:
            parts_total_before_discount = self.parts_total_before_discount

        parent_manufacturer: Union[None, Unset, str]
        if isinstance(self.parent_manufacturer, Unset):
            parent_manufacturer = UNSET
        else:
            parent_manufacturer = self.parent_manufacturer

        parent_location: Union[None, Unset, str]
        if isinstance(self.parent_location, Unset):
            parent_location = UNSET
        else:
            parent_location = self.parent_location

        parent_manufacturer_part_number: Union[None, Unset, str]
        if isinstance(self.parent_manufacturer_part_number, Unset):
            parent_manufacturer_part_number = UNSET
        else:
            parent_manufacturer_part_number = self.parent_manufacturer_part_number

        parent_display_part_number: Union[None, Unset, str]
        if isinstance(self.parent_display_part_number, Unset):
            parent_display_part_number = UNSET
        else:
            parent_display_part_number = self.parent_display_part_number

        parent_asset_id: Union[None, Unset, int]
        if isinstance(self.parent_asset_id, Unset):
            parent_asset_id = UNSET
        else:
            parent_asset_id = self.parent_asset_id

        parent_category_name: Union[None, Unset, str]
        if isinstance(self.parent_category_name, Unset):
            parent_category_name = UNSET
        else:
            parent_category_name = self.parent_category_name

        parent_root_category_name: Union[None, Unset, str]
        if isinstance(self.parent_root_category_name, Unset):
            parent_root_category_name = UNSET
        else:
            parent_root_category_name = self.parent_root_category_name

        parent_serial_number: Union[None, Unset, str]
        if isinstance(self.parent_serial_number, Unset):
            parent_serial_number = UNSET
        else:
            parent_serial_number = self.parent_serial_number

        parent_asset_tag: Union[None, Unset, str]
        if isinstance(self.parent_asset_tag, Unset):
            parent_asset_tag = UNSET
        else:
            parent_asset_tag = self.parent_asset_tag

        parent_asset_user: Union[None, Unset, str]
        if isinstance(self.parent_asset_user, Unset):
            parent_asset_user = UNSET
        else:
            parent_asset_user = self.parent_asset_user

        parent_display_name: Union[None, Unset, str]
        if isinstance(self.parent_display_name, Unset):
            parent_display_name = UNSET
        else:
            parent_display_name = self.parent_display_name

        parent_equipment_id: Union[None, Unset, str]
        if isinstance(self.parent_equipment_id, Unset):
            parent_equipment_id = UNSET
        else:
            parent_equipment_id = self.parent_equipment_id

        asset_shipping_address_1: Union[None, Unset, str]
        if isinstance(self.asset_shipping_address_1, Unset):
            asset_shipping_address_1 = UNSET
        else:
            asset_shipping_address_1 = self.asset_shipping_address_1

        asset_shipping_address_2: Union[None, Unset, str]
        if isinstance(self.asset_shipping_address_2, Unset):
            asset_shipping_address_2 = UNSET
        else:
            asset_shipping_address_2 = self.asset_shipping_address_2

        asset_shipping_first_name: Union[None, Unset, str]
        if isinstance(self.asset_shipping_first_name, Unset):
            asset_shipping_first_name = UNSET
        else:
            asset_shipping_first_name = self.asset_shipping_first_name

        asset_shipping_last_name: Union[None, Unset, str]
        if isinstance(self.asset_shipping_last_name, Unset):
            asset_shipping_last_name = UNSET
        else:
            asset_shipping_last_name = self.asset_shipping_last_name

        asset_shipping_email: Union[None, Unset, str]
        if isinstance(self.asset_shipping_email, Unset):
            asset_shipping_email = UNSET
        else:
            asset_shipping_email = self.asset_shipping_email

        asset_shipping_company: Union[None, Unset, str]
        if isinstance(self.asset_shipping_company, Unset):
            asset_shipping_company = UNSET
        else:
            asset_shipping_company = self.asset_shipping_company

        asset_shipping_city: Union[None, Unset, str]
        if isinstance(self.asset_shipping_city, Unset):
            asset_shipping_city = UNSET
        else:
            asset_shipping_city = self.asset_shipping_city

        asset_shipping_zip: Union[None, Unset, str]
        if isinstance(self.asset_shipping_zip, Unset):
            asset_shipping_zip = UNSET
        else:
            asset_shipping_zip = self.asset_shipping_zip

        asset_shipping_phone_number: Union[None, Unset, str]
        if isinstance(self.asset_shipping_phone_number, Unset):
            asset_shipping_phone_number = UNSET
        else:
            asset_shipping_phone_number = self.asset_shipping_phone_number

        asset_shipping_fax_number: Union[None, Unset, str]
        if isinstance(self.asset_shipping_fax_number, Unset):
            asset_shipping_fax_number = UNSET
        else:
            asset_shipping_fax_number = self.asset_shipping_fax_number

        asset_shipping_country: Union[None, Unset, str]
        if isinstance(self.asset_shipping_country, Unset):
            asset_shipping_country = UNSET
        else:
            asset_shipping_country = self.asset_shipping_country

        asset_shipping_state: Union[None, Unset, str]
        if isinstance(self.asset_shipping_state, Unset):
            asset_shipping_state = UNSET
        else:
            asset_shipping_state = self.asset_shipping_state

        shipping_address_1: Union[None, Unset, str]
        if isinstance(self.shipping_address_1, Unset):
            shipping_address_1 = UNSET
        else:
            shipping_address_1 = self.shipping_address_1

        shipping_address_2: Union[None, Unset, str]
        if isinstance(self.shipping_address_2, Unset):
            shipping_address_2 = UNSET
        else:
            shipping_address_2 = self.shipping_address_2

        shipping_first_name: Union[None, Unset, str]
        if isinstance(self.shipping_first_name, Unset):
            shipping_first_name = UNSET
        else:
            shipping_first_name = self.shipping_first_name

        shipping_last_name: Union[None, Unset, str]
        if isinstance(self.shipping_last_name, Unset):
            shipping_last_name = UNSET
        else:
            shipping_last_name = self.shipping_last_name

        shipping_email: Union[None, Unset, str]
        if isinstance(self.shipping_email, Unset):
            shipping_email = UNSET
        else:
            shipping_email = self.shipping_email

        shipping_company: Union[None, Unset, str]
        if isinstance(self.shipping_company, Unset):
            shipping_company = UNSET
        else:
            shipping_company = self.shipping_company

        shipping_city: Union[None, Unset, str]
        if isinstance(self.shipping_city, Unset):
            shipping_city = UNSET
        else:
            shipping_city = self.shipping_city

        shipping_zip: Union[None, Unset, str]
        if isinstance(self.shipping_zip, Unset):
            shipping_zip = UNSET
        else:
            shipping_zip = self.shipping_zip

        shipping_phone_number: Union[None, Unset, str]
        if isinstance(self.shipping_phone_number, Unset):
            shipping_phone_number = UNSET
        else:
            shipping_phone_number = self.shipping_phone_number

        shipping_fax_number: Union[None, Unset, str]
        if isinstance(self.shipping_fax_number, Unset):
            shipping_fax_number = UNSET
        else:
            shipping_fax_number = self.shipping_fax_number

        shipping_country: Union[None, Unset, str]
        if isinstance(self.shipping_country, Unset):
            shipping_country = UNSET
        else:
            shipping_country = self.shipping_country

        shipping_state: Union[None, Unset, str]
        if isinstance(self.shipping_state, Unset):
            shipping_state = UNSET
        else:
            shipping_state = self.shipping_state

        asset_service_notes: Union[None, Unset, str]
        if isinstance(self.asset_service_notes, Unset):
            asset_service_notes = UNSET
        else:
            asset_service_notes = self.asset_service_notes

        service_option_service_code: Union[None, Unset, str]
        if isinstance(self.service_option_service_code, Unset):
            service_option_service_code = UNSET
        else:
            service_option_service_code = self.service_option_service_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if certificate_number is not UNSET:
            field_dict["CertificateNumber"] = certificate_number
        if document_number is not UNSET:
            field_dict["DocumentNumber"] = document_number
        if revision is not UNSET:
            field_dict["Revision"] = revision
        if effective_date is not UNSET:
            field_dict["EffectiveDate"] = effective_date
        if document_section is not UNSET:
            field_dict["DocumentSection"] = document_section
        if service_level is not UNSET:
            field_dict["ServiceLevel"] = service_level
        if service_level_code is not UNSET:
            field_dict["ServiceLevelCode"] = service_level_code
        if service_type is not UNSET:
            field_dict["ServiceType"] = service_type
        if order_item_number is not UNSET:
            field_dict["OrderItemNumber"] = order_item_number
        if service_charge is not UNSET:
            field_dict["ServiceCharge"] = service_charge
        if updated_by is not UNSET:
            field_dict["UpdatedBy"] = updated_by
        if updated_on is not UNSET:
            field_dict["UpdatedOn"] = updated_on
        if work_status is not UNSET:
            field_dict["WorkStatus"] = work_status
        if custom_work_status is not UNSET:
            field_dict["CustomWorkStatus"] = custom_work_status
        if service_comments is not UNSET:
            field_dict["ServiceComments"] = service_comments
        if client_notes is not UNSET:
            field_dict["ClientNotes"] = client_notes
        if vendor_service_notes is not UNSET:
            field_dict["VendorServiceNotes"] = vendor_service_notes
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if display_part_number is not UNSET:
            field_dict["DisplayPartNumber"] = display_part_number
        if part_number is not UNSET:
            field_dict["PartNumber"] = part_number
        if schedule_name is not UNSET:
            field_dict["ScheduleName"] = schedule_name
        if segment_name is not UNSET:
            field_dict["SegmentName"] = segment_name
        if next_segment_name is not UNSET:
            field_dict["NextSegmentName"] = next_segment_name
        if interval_length is not UNSET:
            field_dict["IntervalLength"] = interval_length
        if interval_cycle is not UNSET:
            field_dict["IntervalCycle"] = interval_cycle
        if service_options is not UNSET:
            field_dict["ServiceOptions"] = service_options
        if service_options_price is not UNSET:
            field_dict["ServiceOptionsPrice"] = service_options_price
        if service_options_document_numbers is not UNSET:
            field_dict["ServiceOptionsDocumentNumbers"] = (
                service_options_document_numbers
            )
        if location is not UNSET:
            field_dict["Location"] = location
        if station is not UNSET:
            field_dict["Station"] = station
        if room is not UNSET:
            field_dict["Room"] = room
        if site is not UNSET:
            field_dict["Site"] = site
        if vendor_id is not UNSET:
            field_dict["VendorId"] = vendor_id
        if service_order_number is not UNSET:
            field_dict["ServiceOrderNumber"] = service_order_number
        if custom_order_number is not UNSET:
            field_dict["CustomOrderNumber"] = custom_order_number
        if linked_order_number is not UNSET:
            field_dict["LinkedOrderNumber"] = linked_order_number
        if asset_id is not UNSET:
            field_dict["AssetId"] = asset_id
        if asset_class is not UNSET:
            field_dict["AssetClass"] = asset_class
        if asset_condition is not UNSET:
            field_dict["AssetCondition"] = asset_condition
        if asset_criticality is not UNSET:
            field_dict["AssetCriticality"] = asset_criticality
        if asset_pool is not UNSET:
            field_dict["AssetPool"] = asset_pool
        if asset_name is not UNSET:
            field_dict["AssetName"] = asset_name
        if asset_description is not UNSET:
            field_dict["AssetDescription"] = asset_description
        if asset_document_number is not UNSET:
            field_dict["AssetDocumentNumber"] = asset_document_number
        if asset_document_section is not UNSET:
            field_dict["AssetDocumentSection"] = asset_document_section
        if document_number_values is not UNSET:
            field_dict["DocumentNumberValues"] = document_number_values
        if product_name is not UNSET:
            field_dict["ProductName"] = product_name
        if product_description is not UNSET:
            field_dict["ProductDescription"] = product_description
        if asset_maker is not UNSET:
            field_dict["AssetMaker"] = asset_maker
        if category_name is not UNSET:
            field_dict["CategoryName"] = category_name
        if root_category_name is not UNSET:
            field_dict["RootCategoryName"] = root_category_name
        if vendor_tag is not UNSET:
            field_dict["VendorTag"] = vendor_tag
        if result_status is not UNSET:
            field_dict["ResultStatus"] = result_status
        if service_date is not UNSET:
            field_dict["ServiceDate"] = service_date
        if next_service_date is not UNSET:
            field_dict["NextServiceDate"] = next_service_date
        if original_due_date is not UNSET:
            field_dict["OriginalDueDate"] = original_due_date
        if asset_tag is not UNSET:
            field_dict["AssetTag"] = asset_tag
        if department is not UNSET:
            field_dict["Department"] = department
        if asset_user is not UNSET:
            field_dict["AssetUser"] = asset_user
        if equipment_id is not UNSET:
            field_dict["EquipmentId"] = equipment_id
        if legacy_identifier is not UNSET:
            field_dict["LegacyIdentifier"] = legacy_identifier
        if activation_date is not UNSET:
            field_dict["ActivationDate"] = activation_date
        if purchase_date is not UNSET:
            field_dict["PurchaseDate"] = purchase_date
        if part_name is not UNSET:
            field_dict["PartName"] = part_name
        if part_description is not UNSET:
            field_dict["PartDescription"] = part_description
        if is_taxable is not UNSET:
            field_dict["IsTaxable"] = is_taxable
        if is_limited is not UNSET:
            field_dict["IsLimited"] = is_limited
        if quantity is not UNSET:
            field_dict["Quantity"] = quantity
        if discount is not UNSET:
            field_dict["Discount"] = discount
        if price is not UNSET:
            field_dict["Price"] = price
        if time_spent_in_minutes is not UNSET:
            field_dict["TimeSpentInMinutes"] = time_spent_in_minutes
        if is_hourly_pricing is not UNSET:
            field_dict["IsHourlyPricing"] = is_hourly_pricing
        if delivery_charge is not UNSET:
            field_dict["DeliveryCharge"] = delivery_charge
        if serial_number is not UNSET:
            field_dict["SerialNumber"] = serial_number
        if part_repair_charges is not UNSET:
            field_dict["PartRepairCharges"] = part_repair_charges
        if part_repair_price is not UNSET:
            field_dict["PartRepairPrice"] = part_repair_price
        if override_parts_total is not UNSET:
            field_dict["OverridePartsTotal"] = override_parts_total
        if override_repairs_total is not UNSET:
            field_dict["OverrideRepairsTotal"] = override_repairs_total
        if asset_custodian_name is not UNSET:
            field_dict["AssetCustodianName"] = asset_custodian_name
        if as_found_specification_group_name is not UNSET:
            field_dict["AsFoundSpecificationGroupName"] = (
                as_found_specification_group_name
            )
        if as_found_specification_company_name is not UNSET:
            field_dict["AsFoundSpecificationCompanyName"] = (
                as_found_specification_company_name
            )
        if as_left_specification_group_name is not UNSET:
            field_dict["AsLeftSpecificationGroupName"] = (
                as_left_specification_group_name
            )
        if as_left_specification_company_name is not UNSET:
            field_dict["AsLeftSpecificationCompanyName"] = (
                as_left_specification_company_name
            )
        if order_id is not UNSET:
            field_dict["OrderId"] = order_id
        if parent_order_id is not UNSET:
            field_dict["ParentOrderId"] = parent_order_id
        if order_item_id is not UNSET:
            field_dict["OrderItemId"] = order_item_id
        if order_item_part_id is not UNSET:
            field_dict["OrderItemPartId"] = order_item_part_id
        if as_found_specification_group_id is not UNSET:
            field_dict["AsFoundSpecificationGroupId"] = as_found_specification_group_id
        if as_left_specification_group_id is not UNSET:
            field_dict["AsLeftSpecificationGroupId"] = as_left_specification_group_id
        if as_found_status is not UNSET:
            field_dict["AsFoundStatus"] = as_found_status
        if as_left_status is not UNSET:
            field_dict["AsLeftStatus"] = as_left_status
        if as_found_result is not UNSET:
            field_dict["AsFoundResult"] = as_found_result
        if as_left_result is not UNSET:
            field_dict["AsLeftResult"] = as_left_result
        if completed_on is not UNSET:
            field_dict["CompletedOn"] = completed_on
        if received_on is not UNSET:
            field_dict["ReceivedOn"] = received_on
        if completed_by_name is not UNSET:
            field_dict["CompletedByName"] = completed_by_name
        if service_charge_base is not UNSET:
            field_dict["ServiceChargeBase"] = service_charge_base
        if service_total is not UNSET:
            field_dict["ServiceTotal"] = service_total
        if repairs_total is not UNSET:
            field_dict["RepairsTotal"] = repairs_total
        if parts_total is not UNSET:
            field_dict["PartsTotal"] = parts_total
        if parts_total_before_discount is not UNSET:
            field_dict["PartsTotalBeforeDiscount"] = parts_total_before_discount
        if parent_manufacturer is not UNSET:
            field_dict["ParentManufacturer"] = parent_manufacturer
        if parent_location is not UNSET:
            field_dict["ParentLocation"] = parent_location
        if parent_manufacturer_part_number is not UNSET:
            field_dict["ParentManufacturerPartNumber"] = parent_manufacturer_part_number
        if parent_display_part_number is not UNSET:
            field_dict["ParentDisplayPartNumber"] = parent_display_part_number
        if parent_asset_id is not UNSET:
            field_dict["ParentAssetId"] = parent_asset_id
        if parent_category_name is not UNSET:
            field_dict["ParentCategoryName"] = parent_category_name
        if parent_root_category_name is not UNSET:
            field_dict["ParentRootCategoryName"] = parent_root_category_name
        if parent_serial_number is not UNSET:
            field_dict["ParentSerialNumber"] = parent_serial_number
        if parent_asset_tag is not UNSET:
            field_dict["ParentAssetTag"] = parent_asset_tag
        if parent_asset_user is not UNSET:
            field_dict["ParentAssetUser"] = parent_asset_user
        if parent_display_name is not UNSET:
            field_dict["ParentDisplayName"] = parent_display_name
        if parent_equipment_id is not UNSET:
            field_dict["ParentEquipmentId"] = parent_equipment_id
        if asset_shipping_address_1 is not UNSET:
            field_dict["AssetShippingAddress1"] = asset_shipping_address_1
        if asset_shipping_address_2 is not UNSET:
            field_dict["AssetShippingAddress2"] = asset_shipping_address_2
        if asset_shipping_first_name is not UNSET:
            field_dict["AssetShippingFirstName"] = asset_shipping_first_name
        if asset_shipping_last_name is not UNSET:
            field_dict["AssetShippingLastName"] = asset_shipping_last_name
        if asset_shipping_email is not UNSET:
            field_dict["AssetShippingEmail"] = asset_shipping_email
        if asset_shipping_company is not UNSET:
            field_dict["AssetShippingCompany"] = asset_shipping_company
        if asset_shipping_city is not UNSET:
            field_dict["AssetShippingCity"] = asset_shipping_city
        if asset_shipping_zip is not UNSET:
            field_dict["AssetShippingZip"] = asset_shipping_zip
        if asset_shipping_phone_number is not UNSET:
            field_dict["AssetShippingPhoneNumber"] = asset_shipping_phone_number
        if asset_shipping_fax_number is not UNSET:
            field_dict["AssetShippingFaxNumber"] = asset_shipping_fax_number
        if asset_shipping_country is not UNSET:
            field_dict["AssetShippingCountry"] = asset_shipping_country
        if asset_shipping_state is not UNSET:
            field_dict["AssetShippingState"] = asset_shipping_state
        if shipping_address_1 is not UNSET:
            field_dict["ShippingAddress1"] = shipping_address_1
        if shipping_address_2 is not UNSET:
            field_dict["ShippingAddress2"] = shipping_address_2
        if shipping_first_name is not UNSET:
            field_dict["ShippingFirstName"] = shipping_first_name
        if shipping_last_name is not UNSET:
            field_dict["ShippingLastName"] = shipping_last_name
        if shipping_email is not UNSET:
            field_dict["ShippingEmail"] = shipping_email
        if shipping_company is not UNSET:
            field_dict["ShippingCompany"] = shipping_company
        if shipping_city is not UNSET:
            field_dict["ShippingCity"] = shipping_city
        if shipping_zip is not UNSET:
            field_dict["ShippingZip"] = shipping_zip
        if shipping_phone_number is not UNSET:
            field_dict["ShippingPhoneNumber"] = shipping_phone_number
        if shipping_fax_number is not UNSET:
            field_dict["ShippingFaxNumber"] = shipping_fax_number
        if shipping_country is not UNSET:
            field_dict["ShippingCountry"] = shipping_country
        if shipping_state is not UNSET:
            field_dict["ShippingState"] = shipping_state
        if asset_service_notes is not UNSET:
            field_dict["AssetServiceNotes"] = asset_service_notes
        if service_option_service_code is not UNSET:
            field_dict["ServiceOptionServiceCode"] = service_option_service_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        certificate_number = d.pop("CertificateNumber", UNSET)

        document_number = d.pop("DocumentNumber", UNSET)

        revision = d.pop("Revision", UNSET)

        def _parse_effective_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_date_type_0 = isoparse(data)

                return effective_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        effective_date = _parse_effective_date(d.pop("EffectiveDate", UNSET))

        document_section = d.pop("DocumentSection", UNSET)

        service_level = d.pop("ServiceLevel", UNSET)

        service_level_code = d.pop("ServiceLevelCode", UNSET)

        service_type = d.pop("ServiceType", UNSET)

        order_item_number = d.pop("OrderItemNumber", UNSET)

        service_charge = d.pop("ServiceCharge", UNSET)

        updated_by = d.pop("UpdatedBy", UNSET)

        def _parse_updated_on(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_on_type_0 = isoparse(data)

                return updated_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        updated_on = _parse_updated_on(d.pop("UpdatedOn", UNSET))

        work_status = d.pop("WorkStatus", UNSET)

        custom_work_status = d.pop("CustomWorkStatus", UNSET)

        service_comments = d.pop("ServiceComments", UNSET)

        client_notes = d.pop("ClientNotes", UNSET)

        vendor_service_notes = d.pop("VendorServiceNotes", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        display_part_number = d.pop("DisplayPartNumber", UNSET)

        part_number = d.pop("PartNumber", UNSET)

        schedule_name = d.pop("ScheduleName", UNSET)

        segment_name = d.pop("SegmentName", UNSET)

        next_segment_name = d.pop("NextSegmentName", UNSET)

        interval_length = d.pop("IntervalLength", UNSET)

        interval_cycle = d.pop("IntervalCycle", UNSET)

        service_options = d.pop("ServiceOptions", UNSET)

        service_options_price = d.pop("ServiceOptionsPrice", UNSET)

        service_options_document_numbers = d.pop("ServiceOptionsDocumentNumbers", UNSET)

        location = d.pop("Location", UNSET)

        station = d.pop("Station", UNSET)

        room = d.pop("Room", UNSET)

        site = d.pop("Site", UNSET)

        vendor_id = d.pop("VendorId", UNSET)

        service_order_number = d.pop("ServiceOrderNumber", UNSET)

        custom_order_number = d.pop("CustomOrderNumber", UNSET)

        linked_order_number = d.pop("LinkedOrderNumber", UNSET)

        asset_id = d.pop("AssetId", UNSET)

        asset_class = d.pop("AssetClass", UNSET)

        asset_condition = d.pop("AssetCondition", UNSET)

        asset_criticality = d.pop("AssetCriticality", UNSET)

        asset_pool = d.pop("AssetPool", UNSET)

        asset_name = d.pop("AssetName", UNSET)

        asset_description = d.pop("AssetDescription", UNSET)

        asset_document_number = d.pop("AssetDocumentNumber", UNSET)

        asset_document_section = d.pop("AssetDocumentSection", UNSET)

        document_number_values = d.pop("DocumentNumberValues", UNSET)

        product_name = d.pop("ProductName", UNSET)

        product_description = d.pop("ProductDescription", UNSET)

        asset_maker = d.pop("AssetMaker", UNSET)

        category_name = d.pop("CategoryName", UNSET)

        root_category_name = d.pop("RootCategoryName", UNSET)

        vendor_tag = d.pop("VendorTag", UNSET)

        def _parse_result_status(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        result_status = _parse_result_status(d.pop("ResultStatus", UNSET))

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

        def _parse_original_due_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                original_due_date_type_0 = isoparse(data)

                return original_due_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        original_due_date = _parse_original_due_date(d.pop("OriginalDueDate", UNSET))

        def _parse_asset_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_tag = _parse_asset_tag(d.pop("AssetTag", UNSET))

        def _parse_department(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        department = _parse_department(d.pop("Department", UNSET))

        def _parse_asset_user(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_user = _parse_asset_user(d.pop("AssetUser", UNSET))

        def _parse_equipment_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        equipment_id = _parse_equipment_id(d.pop("EquipmentId", UNSET))

        def _parse_legacy_identifier(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        legacy_identifier = _parse_legacy_identifier(d.pop("LegacyIdentifier", UNSET))

        def _parse_activation_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                activation_date_type_0 = isoparse(data)

                return activation_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        activation_date = _parse_activation_date(d.pop("ActivationDate", UNSET))

        def _parse_purchase_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                purchase_date_type_0 = isoparse(data)

                return purchase_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        purchase_date = _parse_purchase_date(d.pop("PurchaseDate", UNSET))

        def _parse_part_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        part_name = _parse_part_name(d.pop("PartName", UNSET))

        def _parse_part_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        part_description = _parse_part_description(d.pop("PartDescription", UNSET))

        is_taxable = d.pop("IsTaxable", UNSET)

        is_limited = d.pop("IsLimited", UNSET)

        def _parse_quantity(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        quantity = _parse_quantity(d.pop("Quantity", UNSET))

        def _parse_discount(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        discount = _parse_discount(d.pop("Discount", UNSET))

        def _parse_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        price = _parse_price(d.pop("Price", UNSET))

        def _parse_time_spent_in_minutes(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        time_spent_in_minutes = _parse_time_spent_in_minutes(
            d.pop("TimeSpentInMinutes", UNSET)
        )

        def _parse_is_hourly_pricing(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_hourly_pricing = _parse_is_hourly_pricing(d.pop("IsHourlyPricing", UNSET))

        def _parse_delivery_charge(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        delivery_charge = _parse_delivery_charge(d.pop("DeliveryCharge", UNSET))

        serial_number = d.pop("SerialNumber", UNSET)

        def _parse_part_repair_charges(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        part_repair_charges = _parse_part_repair_charges(
            d.pop("PartRepairCharges", UNSET)
        )

        def _parse_part_repair_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        part_repair_price = _parse_part_repair_price(d.pop("PartRepairPrice", UNSET))

        override_parts_total = d.pop("OverridePartsTotal", UNSET)

        override_repairs_total = d.pop("OverrideRepairsTotal", UNSET)

        def _parse_asset_custodian_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_custodian_name = _parse_asset_custodian_name(
            d.pop("AssetCustodianName", UNSET)
        )

        def _parse_as_found_specification_group_name(
            data: object,
        ) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        as_found_specification_group_name = _parse_as_found_specification_group_name(
            d.pop("AsFoundSpecificationGroupName", UNSET)
        )

        def _parse_as_found_specification_company_name(
            data: object,
        ) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        as_found_specification_company_name = (
            _parse_as_found_specification_company_name(
                d.pop("AsFoundSpecificationCompanyName", UNSET)
            )
        )

        def _parse_as_left_specification_group_name(
            data: object,
        ) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        as_left_specification_group_name = _parse_as_left_specification_group_name(
            d.pop("AsLeftSpecificationGroupName", UNSET)
        )

        def _parse_as_left_specification_company_name(
            data: object,
        ) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        as_left_specification_company_name = _parse_as_left_specification_company_name(
            d.pop("AsLeftSpecificationCompanyName", UNSET)
        )

        def _parse_order_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        order_id = _parse_order_id(d.pop("OrderId", UNSET))

        def _parse_parent_order_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        parent_order_id = _parse_parent_order_id(d.pop("ParentOrderId", UNSET))

        def _parse_order_item_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        order_item_id = _parse_order_item_id(d.pop("OrderItemId", UNSET))

        def _parse_order_item_part_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        order_item_part_id = _parse_order_item_part_id(d.pop("OrderItemPartId", UNSET))

        def _parse_as_found_specification_group_id(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        as_found_specification_group_id = _parse_as_found_specification_group_id(
            d.pop("AsFoundSpecificationGroupId", UNSET)
        )

        def _parse_as_left_specification_group_id(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        as_left_specification_group_id = _parse_as_left_specification_group_id(
            d.pop("AsLeftSpecificationGroupId", UNSET)
        )

        def _parse_as_found_status(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        as_found_status = _parse_as_found_status(d.pop("AsFoundStatus", UNSET))

        def _parse_as_left_status(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        as_left_status = _parse_as_left_status(d.pop("AsLeftStatus", UNSET))

        def _parse_as_found_result(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        as_found_result = _parse_as_found_result(d.pop("AsFoundResult", UNSET))

        def _parse_as_left_result(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        as_left_result = _parse_as_left_result(d.pop("AsLeftResult", UNSET))

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

        def _parse_received_on(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                received_on_type_0 = isoparse(data)

                return received_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        received_on = _parse_received_on(d.pop("ReceivedOn", UNSET))

        def _parse_completed_by_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        completed_by_name = _parse_completed_by_name(d.pop("CompletedByName", UNSET))

        def _parse_service_charge_base(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        service_charge_base = _parse_service_charge_base(
            d.pop("ServiceChargeBase", UNSET)
        )

        def _parse_service_total(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        service_total = _parse_service_total(d.pop("ServiceTotal", UNSET))

        def _parse_repairs_total(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        repairs_total = _parse_repairs_total(d.pop("RepairsTotal", UNSET))

        def _parse_parts_total(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        parts_total = _parse_parts_total(d.pop("PartsTotal", UNSET))

        def _parse_parts_total_before_discount(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        parts_total_before_discount = _parse_parts_total_before_discount(
            d.pop("PartsTotalBeforeDiscount", UNSET)
        )

        def _parse_parent_manufacturer(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_manufacturer = _parse_parent_manufacturer(
            d.pop("ParentManufacturer", UNSET)
        )

        def _parse_parent_location(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_location = _parse_parent_location(d.pop("ParentLocation", UNSET))

        def _parse_parent_manufacturer_part_number(
            data: object,
        ) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_manufacturer_part_number = _parse_parent_manufacturer_part_number(
            d.pop("ParentManufacturerPartNumber", UNSET)
        )

        def _parse_parent_display_part_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_display_part_number = _parse_parent_display_part_number(
            d.pop("ParentDisplayPartNumber", UNSET)
        )

        def _parse_parent_asset_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        parent_asset_id = _parse_parent_asset_id(d.pop("ParentAssetId", UNSET))

        def _parse_parent_category_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_category_name = _parse_parent_category_name(
            d.pop("ParentCategoryName", UNSET)
        )

        def _parse_parent_root_category_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_root_category_name = _parse_parent_root_category_name(
            d.pop("ParentRootCategoryName", UNSET)
        )

        def _parse_parent_serial_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_serial_number = _parse_parent_serial_number(
            d.pop("ParentSerialNumber", UNSET)
        )

        def _parse_parent_asset_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_asset_tag = _parse_parent_asset_tag(d.pop("ParentAssetTag", UNSET))

        def _parse_parent_asset_user(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_asset_user = _parse_parent_asset_user(d.pop("ParentAssetUser", UNSET))

        def _parse_parent_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_display_name = _parse_parent_display_name(
            d.pop("ParentDisplayName", UNSET)
        )

        def _parse_parent_equipment_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_equipment_id = _parse_parent_equipment_id(
            d.pop("ParentEquipmentId", UNSET)
        )

        def _parse_asset_shipping_address_1(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_shipping_address_1 = _parse_asset_shipping_address_1(
            d.pop("AssetShippingAddress1", UNSET)
        )

        def _parse_asset_shipping_address_2(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_shipping_address_2 = _parse_asset_shipping_address_2(
            d.pop("AssetShippingAddress2", UNSET)
        )

        def _parse_asset_shipping_first_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_shipping_first_name = _parse_asset_shipping_first_name(
            d.pop("AssetShippingFirstName", UNSET)
        )

        def _parse_asset_shipping_last_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_shipping_last_name = _parse_asset_shipping_last_name(
            d.pop("AssetShippingLastName", UNSET)
        )

        def _parse_asset_shipping_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_shipping_email = _parse_asset_shipping_email(
            d.pop("AssetShippingEmail", UNSET)
        )

        def _parse_asset_shipping_company(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_shipping_company = _parse_asset_shipping_company(
            d.pop("AssetShippingCompany", UNSET)
        )

        def _parse_asset_shipping_city(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_shipping_city = _parse_asset_shipping_city(
            d.pop("AssetShippingCity", UNSET)
        )

        def _parse_asset_shipping_zip(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_shipping_zip = _parse_asset_shipping_zip(d.pop("AssetShippingZip", UNSET))

        def _parse_asset_shipping_phone_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_shipping_phone_number = _parse_asset_shipping_phone_number(
            d.pop("AssetShippingPhoneNumber", UNSET)
        )

        def _parse_asset_shipping_fax_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_shipping_fax_number = _parse_asset_shipping_fax_number(
            d.pop("AssetShippingFaxNumber", UNSET)
        )

        def _parse_asset_shipping_country(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_shipping_country = _parse_asset_shipping_country(
            d.pop("AssetShippingCountry", UNSET)
        )

        def _parse_asset_shipping_state(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_shipping_state = _parse_asset_shipping_state(
            d.pop("AssetShippingState", UNSET)
        )

        def _parse_shipping_address_1(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shipping_address_1 = _parse_shipping_address_1(d.pop("ShippingAddress1", UNSET))

        def _parse_shipping_address_2(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shipping_address_2 = _parse_shipping_address_2(d.pop("ShippingAddress2", UNSET))

        def _parse_shipping_first_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shipping_first_name = _parse_shipping_first_name(
            d.pop("ShippingFirstName", UNSET)
        )

        def _parse_shipping_last_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shipping_last_name = _parse_shipping_last_name(d.pop("ShippingLastName", UNSET))

        def _parse_shipping_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shipping_email = _parse_shipping_email(d.pop("ShippingEmail", UNSET))

        def _parse_shipping_company(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shipping_company = _parse_shipping_company(d.pop("ShippingCompany", UNSET))

        def _parse_shipping_city(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shipping_city = _parse_shipping_city(d.pop("ShippingCity", UNSET))

        def _parse_shipping_zip(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shipping_zip = _parse_shipping_zip(d.pop("ShippingZip", UNSET))

        def _parse_shipping_phone_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shipping_phone_number = _parse_shipping_phone_number(
            d.pop("ShippingPhoneNumber", UNSET)
        )

        def _parse_shipping_fax_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shipping_fax_number = _parse_shipping_fax_number(
            d.pop("ShippingFaxNumber", UNSET)
        )

        def _parse_shipping_country(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shipping_country = _parse_shipping_country(d.pop("ShippingCountry", UNSET))

        def _parse_shipping_state(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shipping_state = _parse_shipping_state(d.pop("ShippingState", UNSET))

        def _parse_asset_service_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_service_notes = _parse_asset_service_notes(
            d.pop("AssetServiceNotes", UNSET)
        )

        def _parse_service_option_service_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        service_option_service_code = _parse_service_option_service_code(
            d.pop("ServiceOptionServiceCode", UNSET)
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

        qualer_api_models_report_datasets_to_service_order_item_response.additional_properties = (
            d
        )
        return qualer_api_models_report_datasets_to_service_order_item_response

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
