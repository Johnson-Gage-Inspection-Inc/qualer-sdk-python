import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ReportDatasetsToServiceOrderResponse")


@_attrs_define
class ReportDatasetsToServiceOrderResponse:
    """
    Attributes:
        guid (Optional[str]):
        account_number (Optional[str]):
        service_order_number (Optional[int]):
        service_order_number_text (Optional[str]):
        number_of_instruments (Optional[int]):
        parts_discount_total (Optional[float]):
        po_number (Optional[str]):
        secondary_po (Optional[str]):
        location (Optional[str]):
        shipped_date (Optional[datetime.datetime]):
        payment_terms (Optional[int]):
        site_access_notes (Optional[str]):
        grace_period (Optional[int]):
        trade_in_credit (Optional[float]):
        prepaid_credit (Optional[float]):
        interest_rate (Optional[float]):
        service_taxation (Optional[int]):
        service_order_id (Optional[int]):
        federal_number (Optional[str]):
        vendor_site_id (Optional[int]):
        vendor_site (Optional[str]):
        site_name (Optional[str]):
        site_code (Optional[str]):
        vendor_name (Optional[str]):
        domain_name (Optional[str]):
        client_company_domain (Optional[str]):
        provider_logo (Optional[str]):
        client_signature (Optional[str]):
        vendor_signature (Optional[str]):
        qr_code (Optional[str]):
        bar_code (Optional[str]):
        bar_code_string (Optional[str]):
        po_balance (Optional[float]):
        service_terms (Optional[str]):
        service_total (Optional[float]):
        repairs_total (Optional[float]):
        parts_total (Optional[float]):
        parts_total_before_discount (Optional[float]):
        effective_tax_rate (Optional[float]):
        tax_amount (Optional[float]):
        shipping_fee (Optional[float]):
        late_fee (Optional[float]):
        grand_total (Optional[float]):
        amount_paid (Optional[float]):
        balance_total (Optional[float]):
        travel_charge (Optional[float]):
        private_notes (Optional[str]):
        service_notes (Optional[str]):
        display_service_comments (Optional[bool]):
        display_part_repairs (Optional[bool]):
        print_separate_measurement (Optional[bool]):
        billing_address_1 (Optional[str]):
        billing_address_2 (Optional[str]):
        billing_first_name (Optional[str]):
        billing_last_name (Optional[str]):
        billing_company (Optional[str]):
        billing_country (Optional[str]):
        billing_city (Optional[str]):
        billing_state (Optional[str]):
        billing_zip (Optional[str]):
        billing_phone_number (Optional[str]):
        billing_fax_number (Optional[str]):
        billing_email (Optional[str]):
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
        shipping_method (Optional[str]):
        return_shipping_method (Optional[str]):
        tracking_number (Optional[str]):
        provider_billing_address_1 (Optional[str]):
        provider_billing_address_2 (Optional[str]):
        provider_billing_first_name (Optional[str]):
        provider_billing_last_name (Optional[str]):
        provider_billing_email (Optional[str]):
        provider_billing_company (Optional[str]):
        provider_billing_city (Optional[str]):
        provider_billing_zip (Optional[str]):
        provider_billing_phone_number (Optional[str]):
        provider_billing_country (Optional[str]):
        provider_billing_state (Optional[str]):
        provider_billing_fax_number (Optional[str]):
        provider_shipping_address_1 (Optional[str]):
        provider_shipping_address_2 (Optional[str]):
        provider_shipping_first_name (Optional[str]):
        provider_shipping_last_name (Optional[str]):
        provider_shipping_email (Optional[str]):
        provider_shipping_company (Optional[str]):
        provider_shipping_city (Optional[str]):
        provider_shipping_zip (Optional[str]):
        provider_shipping_phone_number (Optional[str]):
        provider_shipping_country (Optional[str]):
        provider_shipping_state (Optional[str]):
        provider_shipping_fax_number (Optional[str]):
        culture_name (Optional[str]):
        vendor_company_id (Optional[int]):
        client_vendor_id (Optional[int]):
        sign_off_date (Optional[datetime.datetime]):
        quality_control_date (Optional[datetime.datetime]):
        client_sign_off_on (Optional[datetime.datetime]):
        client_sign_off_by_name (Optional[str]):
        client_signed_on (Optional[datetime.datetime]):
        client_sticker_notes (Optional[str]):
        asset_sticker_notes (Optional[str]):
        order_sticker_notes (Optional[str]):
        quality_control_name (Optional[str]):
        fulfilled_by_name (Optional[str]):
        sign_off_name (Optional[str]):
        display_as_found (Optional[bool]):
        display_as_left (Optional[bool]):
        created_on (Optional[datetime.datetime]):
        invoiced_on (Optional[datetime.datetime]):
        submitted_on (Optional[datetime.datetime]):
        shipped_on (Optional[datetime.datetime]):
        completed_on (Optional[datetime.datetime]):
        accepted_on (Optional[datetime.datetime]):
        approved_on (Optional[datetime.datetime]):
        delivered_on (Optional[datetime.datetime]):
        paid_on (Optional[datetime.datetime]):
        cancelled_on (Optional[datetime.datetime]):
        fulfilled_on (Optional[datetime.datetime]):
        sign_off_on (Optional[datetime.datetime]):
        vendor_signed_on (Optional[datetime.datetime]):
        client_notes (Optional[str]):
        order_shipping_option (Optional[int]):
        shipment_status (Optional[int]):
        payment_status (Optional[int]):
        payment_option (Optional[str]):
        order_status (Optional[int]):
        created_by_name (Optional[str]):
        completed_by_name (Optional[str]):
        shipped_by_name (Optional[str]):
        accepted_by_name (Optional[str]):
        approve_by_name (Optional[str]):
        invoiced_by_name (Optional[str]):
        delivered_by_name (Optional[str]):
        paid_by_name (Optional[str]):
        cancelled_by_name (Optional[str]):
        sign_off_by_name (Optional[str]):
        owner_name (Optional[str]):
        owner_department (Optional[str]):
        assignee_name (Optional[str]):
        payment_due_on (Optional[datetime.datetime]):
        process_date_option (Optional[int]):
        desired_date (Optional[datetime.datetime]):
        deadline_date (Optional[datetime.datetime]):
        vendor_sign_off_on (Optional[datetime.datetime]):
        vendor_sign_off_by_name (Optional[str]):
        service_discount (Optional[float]):
        return_account (Optional[str]):
        business_hours_from (Optional[datetime.datetime]):
        business_hours_to (Optional[datetime.datetime]):
        client_company_alternative_names (Optional[str]):
        client_id (Optional[int]):
        client_class (Optional[str]):
        client_status (Optional[str]):
        client_invoicing (Optional[str]):
        client_standing (Optional[str]):
        client_category (Optional[str]):
        master_template_name (Optional[str]):
        client_site_code (Optional[str]):
        order_workflow_name (Optional[str]):
        request_workflow_name (Optional[str]):
    """

    guid: Optional[str] = None
    account_number: Optional[str] = None
    service_order_number: Optional[int] = None
    service_order_number_text: Optional[str] = None
    number_of_instruments: Optional[int] = None
    parts_discount_total: Optional[float] = None
    po_number: Optional[str] = None
    secondary_po: Optional[str] = None
    location: Optional[str] = None
    shipped_date: Optional[datetime.datetime] = None
    payment_terms: Optional[int] = None
    site_access_notes: Optional[str] = None
    grace_period: Optional[int] = None
    trade_in_credit: Optional[float] = None
    prepaid_credit: Optional[float] = None
    interest_rate: Optional[float] = None
    service_taxation: Optional[int] = None
    service_order_id: Optional[int] = None
    federal_number: Optional[str] = None
    vendor_site_id: Optional[int] = None
    vendor_site: Optional[str] = None
    site_name: Optional[str] = None
    site_code: Optional[str] = None
    vendor_name: Optional[str] = None
    domain_name: Optional[str] = None
    client_company_domain: Optional[str] = None
    provider_logo: Optional[str] = None
    client_signature: Optional[str] = None
    vendor_signature: Optional[str] = None
    qr_code: Optional[str] = None
    bar_code: Optional[str] = None
    bar_code_string: Optional[str] = None
    po_balance: Optional[float] = None
    service_terms: Optional[str] = None
    service_total: Optional[float] = None
    repairs_total: Optional[float] = None
    parts_total: Optional[float] = None
    parts_total_before_discount: Optional[float] = None
    effective_tax_rate: Optional[float] = None
    tax_amount: Optional[float] = None
    shipping_fee: Optional[float] = None
    late_fee: Optional[float] = None
    grand_total: Optional[float] = None
    amount_paid: Optional[float] = None
    balance_total: Optional[float] = None
    travel_charge: Optional[float] = None
    private_notes: Optional[str] = None
    service_notes: Optional[str] = None
    display_service_comments: Optional[bool] = None
    display_part_repairs: Optional[bool] = None
    print_separate_measurement: Optional[bool] = None
    billing_address_1: Optional[str] = None
    billing_address_2: Optional[str] = None
    billing_first_name: Optional[str] = None
    billing_last_name: Optional[str] = None
    billing_company: Optional[str] = None
    billing_country: Optional[str] = None
    billing_city: Optional[str] = None
    billing_state: Optional[str] = None
    billing_zip: Optional[str] = None
    billing_phone_number: Optional[str] = None
    billing_fax_number: Optional[str] = None
    billing_email: Optional[str] = None
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
    shipping_method: Optional[str] = None
    return_shipping_method: Optional[str] = None
    tracking_number: Optional[str] = None
    provider_billing_address_1: Optional[str] = None
    provider_billing_address_2: Optional[str] = None
    provider_billing_first_name: Optional[str] = None
    provider_billing_last_name: Optional[str] = None
    provider_billing_email: Optional[str] = None
    provider_billing_company: Optional[str] = None
    provider_billing_city: Optional[str] = None
    provider_billing_zip: Optional[str] = None
    provider_billing_phone_number: Optional[str] = None
    provider_billing_country: Optional[str] = None
    provider_billing_state: Optional[str] = None
    provider_billing_fax_number: Optional[str] = None
    provider_shipping_address_1: Optional[str] = None
    provider_shipping_address_2: Optional[str] = None
    provider_shipping_first_name: Optional[str] = None
    provider_shipping_last_name: Optional[str] = None
    provider_shipping_email: Optional[str] = None
    provider_shipping_company: Optional[str] = None
    provider_shipping_city: Optional[str] = None
    provider_shipping_zip: Optional[str] = None
    provider_shipping_phone_number: Optional[str] = None
    provider_shipping_country: Optional[str] = None
    provider_shipping_state: Optional[str] = None
    provider_shipping_fax_number: Optional[str] = None
    culture_name: Optional[str] = None
    vendor_company_id: Optional[int] = None
    client_vendor_id: Optional[int] = None
    sign_off_date: Optional[datetime.datetime] = None
    quality_control_date: Optional[datetime.datetime] = None
    client_sign_off_on: Optional[datetime.datetime] = None
    client_sign_off_by_name: Optional[str] = None
    client_signed_on: Optional[datetime.datetime] = None
    client_sticker_notes: Optional[str] = None
    asset_sticker_notes: Optional[str] = None
    order_sticker_notes: Optional[str] = None
    quality_control_name: Optional[str] = None
    fulfilled_by_name: Optional[str] = None
    sign_off_name: Optional[str] = None
    display_as_found: Optional[bool] = None
    display_as_left: Optional[bool] = None
    created_on: Optional[datetime.datetime] = None
    invoiced_on: Optional[datetime.datetime] = None
    submitted_on: Optional[datetime.datetime] = None
    shipped_on: Optional[datetime.datetime] = None
    completed_on: Optional[datetime.datetime] = None
    accepted_on: Optional[datetime.datetime] = None
    approved_on: Optional[datetime.datetime] = None
    delivered_on: Optional[datetime.datetime] = None
    paid_on: Optional[datetime.datetime] = None
    cancelled_on: Optional[datetime.datetime] = None
    fulfilled_on: Optional[datetime.datetime] = None
    sign_off_on: Optional[datetime.datetime] = None
    vendor_signed_on: Optional[datetime.datetime] = None
    client_notes: Optional[str] = None
    order_shipping_option: Optional[int] = None
    shipment_status: Optional[int] = None
    payment_status: Optional[int] = None
    payment_option: Optional[str] = None
    order_status: Optional[int] = None
    created_by_name: Optional[str] = None
    completed_by_name: Optional[str] = None
    shipped_by_name: Optional[str] = None
    accepted_by_name: Optional[str] = None
    approve_by_name: Optional[str] = None
    invoiced_by_name: Optional[str] = None
    delivered_by_name: Optional[str] = None
    paid_by_name: Optional[str] = None
    cancelled_by_name: Optional[str] = None
    sign_off_by_name: Optional[str] = None
    owner_name: Optional[str] = None
    owner_department: Optional[str] = None
    assignee_name: Optional[str] = None
    payment_due_on: Optional[datetime.datetime] = None
    process_date_option: Optional[int] = None
    desired_date: Optional[datetime.datetime] = None
    deadline_date: Optional[datetime.datetime] = None
    vendor_sign_off_on: Optional[datetime.datetime] = None
    vendor_sign_off_by_name: Optional[str] = None
    service_discount: Optional[float] = None
    return_account: Optional[str] = None
    business_hours_from: Optional[datetime.datetime] = None
    business_hours_to: Optional[datetime.datetime] = None
    client_company_alternative_names: Optional[str] = None
    client_id: Optional[int] = None
    client_class: Optional[str] = None
    client_status: Optional[str] = None
    client_invoicing: Optional[str] = None
    client_standing: Optional[str] = None
    client_category: Optional[str] = None
    master_template_name: Optional[str] = None
    client_site_code: Optional[str] = None
    order_workflow_name: Optional[str] = None
    request_workflow_name: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        guid = self.guid

        account_number = self.account_number

        service_order_number = self.service_order_number

        service_order_number_text = self.service_order_number_text

        number_of_instruments = self.number_of_instruments

        parts_discount_total = self.parts_discount_total

        po_number = self.po_number

        secondary_po = self.secondary_po

        location = self.location

        shipped_date: Optional[str]
        if not self.shipped_date:
            shipped_date = None
        elif isinstance(self.shipped_date, datetime.datetime):
            shipped_date = self.shipped_date.isoformat()
        else:
            shipped_date = self.shipped_date

        payment_terms = self.payment_terms

        site_access_notes = self.site_access_notes

        grace_period = self.grace_period

        trade_in_credit = self.trade_in_credit

        prepaid_credit = self.prepaid_credit

        interest_rate = self.interest_rate

        service_taxation = self.service_taxation

        service_order_id = self.service_order_id

        federal_number = self.federal_number

        vendor_site_id = self.vendor_site_id

        vendor_site = self.vendor_site

        site_name = self.site_name

        site_code = self.site_code

        vendor_name = self.vendor_name

        domain_name = self.domain_name

        client_company_domain = self.client_company_domain

        provider_logo = self.provider_logo

        client_signature = self.client_signature

        vendor_signature = self.vendor_signature

        qr_code = self.qr_code

        bar_code = self.bar_code

        bar_code_string = self.bar_code_string

        po_balance = self.po_balance

        service_terms = self.service_terms

        service_total = self.service_total

        repairs_total = self.repairs_total

        parts_total = self.parts_total

        parts_total_before_discount = self.parts_total_before_discount

        effective_tax_rate = self.effective_tax_rate

        tax_amount = self.tax_amount

        shipping_fee = self.shipping_fee

        late_fee = self.late_fee

        grand_total = self.grand_total

        amount_paid = self.amount_paid

        balance_total = self.balance_total

        travel_charge = self.travel_charge

        private_notes = self.private_notes

        service_notes = self.service_notes

        display_service_comments = self.display_service_comments

        display_part_repairs = self.display_part_repairs

        print_separate_measurement = self.print_separate_measurement

        billing_address_1 = self.billing_address_1

        billing_address_2 = self.billing_address_2

        billing_first_name = self.billing_first_name

        billing_last_name = self.billing_last_name

        billing_company = self.billing_company

        billing_country = self.billing_country

        billing_city = self.billing_city

        billing_state = self.billing_state

        billing_zip = self.billing_zip

        billing_phone_number = self.billing_phone_number

        billing_fax_number = self.billing_fax_number

        billing_email = self.billing_email

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

        shipping_method = self.shipping_method

        return_shipping_method = self.return_shipping_method

        tracking_number = self.tracking_number

        provider_billing_address_1 = self.provider_billing_address_1

        provider_billing_address_2 = self.provider_billing_address_2

        provider_billing_first_name = self.provider_billing_first_name

        provider_billing_last_name = self.provider_billing_last_name

        provider_billing_email = self.provider_billing_email

        provider_billing_company = self.provider_billing_company

        provider_billing_city = self.provider_billing_city

        provider_billing_zip = self.provider_billing_zip

        provider_billing_phone_number = self.provider_billing_phone_number

        provider_billing_country = self.provider_billing_country

        provider_billing_state = self.provider_billing_state

        provider_billing_fax_number = self.provider_billing_fax_number

        provider_shipping_address_1 = self.provider_shipping_address_1

        provider_shipping_address_2 = self.provider_shipping_address_2

        provider_shipping_first_name = self.provider_shipping_first_name

        provider_shipping_last_name = self.provider_shipping_last_name

        provider_shipping_email = self.provider_shipping_email

        provider_shipping_company = self.provider_shipping_company

        provider_shipping_city = self.provider_shipping_city

        provider_shipping_zip = self.provider_shipping_zip

        provider_shipping_phone_number = self.provider_shipping_phone_number

        provider_shipping_country = self.provider_shipping_country

        provider_shipping_state = self.provider_shipping_state

        provider_shipping_fax_number = self.provider_shipping_fax_number

        culture_name = self.culture_name

        vendor_company_id = self.vendor_company_id

        client_vendor_id = self.client_vendor_id

        sign_off_date: Optional[str]
        if not self.sign_off_date:
            sign_off_date = None
        elif isinstance(self.sign_off_date, datetime.datetime):
            sign_off_date = self.sign_off_date.isoformat()
        else:
            sign_off_date = self.sign_off_date

        quality_control_date: Optional[str] = None
        if self.quality_control_date:
            quality_control_date = self.quality_control_date.isoformat()

        client_sign_off_on: Optional[str]
        if not self.client_sign_off_on:
            client_sign_off_on = None
        elif isinstance(self.client_sign_off_on, datetime.datetime):
            client_sign_off_on = self.client_sign_off_on.isoformat()
        else:
            client_sign_off_on = self.client_sign_off_on

        client_sign_off_by_name = self.client_sign_off_by_name

        client_signed_on: Optional[str]
        if not self.client_signed_on:
            client_signed_on = None
        elif isinstance(self.client_signed_on, datetime.datetime):
            client_signed_on = self.client_signed_on.isoformat()
        else:
            client_signed_on = self.client_signed_on

        client_sticker_notes = self.client_sticker_notes

        asset_sticker_notes = self.asset_sticker_notes

        order_sticker_notes = self.order_sticker_notes

        quality_control_name = self.quality_control_name

        fulfilled_by_name = self.fulfilled_by_name

        sign_off_name = self.sign_off_name

        display_as_found = self.display_as_found

        display_as_left = self.display_as_left

        created_on: Optional[str] = None
        if self.created_on:
            created_on = self.created_on.isoformat()

        invoiced_on: Optional[str]
        if not self.invoiced_on:
            invoiced_on = None
        elif isinstance(self.invoiced_on, datetime.datetime):
            invoiced_on = self.invoiced_on.isoformat()
        else:
            invoiced_on = self.invoiced_on

        submitted_on: Optional[str]
        if not self.submitted_on:
            submitted_on = None
        elif isinstance(self.submitted_on, datetime.datetime):
            submitted_on = self.submitted_on.isoformat()
        else:
            submitted_on = self.submitted_on

        shipped_on: Optional[str]
        if not self.shipped_on:
            shipped_on = None
        elif isinstance(self.shipped_on, datetime.datetime):
            shipped_on = self.shipped_on.isoformat()
        else:
            shipped_on = self.shipped_on

        completed_on: Optional[str]
        if not self.completed_on:
            completed_on = None
        elif isinstance(self.completed_on, datetime.datetime):
            completed_on = self.completed_on.isoformat()
        else:
            completed_on = self.completed_on

        accepted_on: Optional[str]
        if not self.accepted_on:
            accepted_on = None
        elif isinstance(self.accepted_on, datetime.datetime):
            accepted_on = self.accepted_on.isoformat()
        else:
            accepted_on = self.accepted_on

        approved_on: Optional[str]
        if not self.approved_on:
            approved_on = None
        elif isinstance(self.approved_on, datetime.datetime):
            approved_on = self.approved_on.isoformat()
        else:
            approved_on = self.approved_on

        delivered_on: Optional[str]
        if not self.delivered_on:
            delivered_on = None
        elif isinstance(self.delivered_on, datetime.datetime):
            delivered_on = self.delivered_on.isoformat()
        else:
            delivered_on = self.delivered_on

        paid_on: Optional[str]
        if not self.paid_on:
            paid_on = None
        elif isinstance(self.paid_on, datetime.datetime):
            paid_on = self.paid_on.isoformat()
        else:
            paid_on = self.paid_on

        cancelled_on: Optional[str]
        if not self.cancelled_on:
            cancelled_on = None
        elif isinstance(self.cancelled_on, datetime.datetime):
            cancelled_on = self.cancelled_on.isoformat()
        else:
            cancelled_on = self.cancelled_on

        fulfilled_on: Optional[str]
        if not self.fulfilled_on:
            fulfilled_on = None
        elif isinstance(self.fulfilled_on, datetime.datetime):
            fulfilled_on = self.fulfilled_on.isoformat()
        else:
            fulfilled_on = self.fulfilled_on

        sign_off_on: Optional[str]
        if not self.sign_off_on:
            sign_off_on = None
        elif isinstance(self.sign_off_on, datetime.datetime):
            sign_off_on = self.sign_off_on.isoformat()
        else:
            sign_off_on = self.sign_off_on

        vendor_signed_on: Optional[str]
        if not self.vendor_signed_on:
            vendor_signed_on = None
        elif isinstance(self.vendor_signed_on, datetime.datetime):
            vendor_signed_on = self.vendor_signed_on.isoformat()
        else:
            vendor_signed_on = self.vendor_signed_on

        client_notes: Optional[str]
        if not self.client_notes:
            client_notes = None
        else:
            client_notes = self.client_notes

        order_shipping_option = self.order_shipping_option

        shipment_status = self.shipment_status

        payment_status = self.payment_status

        payment_option = self.payment_option

        order_status = self.order_status

        created_by_name = self.created_by_name

        completed_by_name: Optional[str]
        if not self.completed_by_name:
            completed_by_name = None
        else:
            completed_by_name = self.completed_by_name

        shipped_by_name: Optional[str]
        if not self.shipped_by_name:
            shipped_by_name = None
        else:
            shipped_by_name = self.shipped_by_name

        accepted_by_name: Optional[str]
        if not self.accepted_by_name:
            accepted_by_name = None
        else:
            accepted_by_name = self.accepted_by_name

        approve_by_name: Optional[str]
        if not self.approve_by_name:
            approve_by_name = None
        else:
            approve_by_name = self.approve_by_name

        invoiced_by_name: Optional[str]
        if not self.invoiced_by_name:
            invoiced_by_name = None
        else:
            invoiced_by_name = self.invoiced_by_name

        delivered_by_name: Optional[str]
        if not self.delivered_by_name:
            delivered_by_name = None
        else:
            delivered_by_name = self.delivered_by_name

        paid_by_name: Optional[str]
        if not self.paid_by_name:
            paid_by_name = None
        else:
            paid_by_name = self.paid_by_name

        cancelled_by_name: Optional[str]
        if not self.cancelled_by_name:
            cancelled_by_name = None
        else:
            cancelled_by_name = self.cancelled_by_name

        sign_off_by_name: Optional[str]
        if not self.sign_off_by_name:
            sign_off_by_name = None
        else:
            sign_off_by_name = self.sign_off_by_name

        owner_name: Optional[str]
        if not self.owner_name:
            owner_name = None
        else:
            owner_name = self.owner_name

        owner_department: Optional[str]
        if not self.owner_department:
            owner_department = None
        else:
            owner_department = self.owner_department

        assignee_name: Optional[str]
        if not self.assignee_name:
            assignee_name = None
        else:
            assignee_name = self.assignee_name

        payment_due_on: Optional[str]
        if not self.payment_due_on:
            payment_due_on = None
        elif isinstance(self.payment_due_on, datetime.datetime):
            payment_due_on = self.payment_due_on.isoformat()
        else:
            payment_due_on = self.payment_due_on

        process_date_option = self.process_date_option

        desired_date: Optional[str]
        if not self.desired_date:
            desired_date = None
        elif isinstance(self.desired_date, datetime.datetime):
            desired_date = self.desired_date.isoformat()
        else:
            desired_date = self.desired_date

        deadline_date: Optional[str]
        if not self.deadline_date:
            deadline_date = None
        elif isinstance(self.deadline_date, datetime.datetime):
            deadline_date = self.deadline_date.isoformat()
        else:
            deadline_date = self.deadline_date

        vendor_sign_off_on: Optional[str] = None
        if self.vendor_sign_off_on:
            vendor_sign_off_on = self.vendor_sign_off_on.isoformat()

        vendor_sign_off_by_name = self.vendor_sign_off_by_name

        service_discount = self.service_discount

        return_account = self.return_account

        business_hours_from: Optional[str]
        if not self.business_hours_from:
            business_hours_from = None
        elif isinstance(self.business_hours_from, datetime.datetime):
            business_hours_from = self.business_hours_from.isoformat()
        else:
            business_hours_from = self.business_hours_from

        business_hours_to: Optional[str]
        if not self.business_hours_to:
            business_hours_to = None
        elif isinstance(self.business_hours_to, datetime.datetime):
            business_hours_to = self.business_hours_to.isoformat()
        else:
            business_hours_to = self.business_hours_to

        client_company_alternative_names = self.client_company_alternative_names

        client_id = self.client_id

        client_class = self.client_class

        client_status = self.client_status

        client_invoicing = self.client_invoicing

        client_standing = self.client_standing

        client_category = self.client_category

        master_template_name = self.master_template_name

        client_site_code = self.client_site_code

        order_workflow_name = self.order_workflow_name

        request_workflow_name = self.request_workflow_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if guid is not None:
            field_dict["Guid"] = guid
        if account_number is not None:
            field_dict["AccountNumber"] = account_number
        if service_order_number is not None:
            field_dict["ServiceOrderNumber"] = service_order_number
        if service_order_number_text is not None:
            field_dict["ServiceOrderNumberText"] = service_order_number_text
        if number_of_instruments is not None:
            field_dict["NumberOfInstruments"] = number_of_instruments
        if parts_discount_total is not None:
            field_dict["PartsDiscountTotal"] = parts_discount_total
        if po_number is not None:
            field_dict["PoNumber"] = po_number
        if secondary_po is not None:
            field_dict["SecondaryPo"] = secondary_po
        if location is not None:
            field_dict["Location"] = location
        if shipped_date is not None:
            field_dict["ShippedDate"] = shipped_date
        if payment_terms is not None:
            field_dict["PaymentTerms"] = payment_terms
        if site_access_notes is not None:
            field_dict["SiteAccessNotes"] = site_access_notes
        if grace_period is not None:
            field_dict["GracePeriod"] = grace_period
        if trade_in_credit is not None:
            field_dict["TradeInCredit"] = trade_in_credit
        if prepaid_credit is not None:
            field_dict["PrepaidCredit"] = prepaid_credit
        if interest_rate is not None:
            field_dict["InterestRate"] = interest_rate
        if service_taxation is not None:
            field_dict["ServiceTaxation"] = service_taxation
        if service_order_id is not None:
            field_dict["ServiceOrderId"] = service_order_id
        if federal_number is not None:
            field_dict["FederalNumber"] = federal_number
        if vendor_site_id is not None:
            field_dict["VendorSiteId"] = vendor_site_id
        if vendor_site is not None:
            field_dict["VendorSite"] = vendor_site
        if site_name is not None:
            field_dict["SiteName"] = site_name
        if site_code is not None:
            field_dict["SiteCode"] = site_code
        if vendor_name is not None:
            field_dict["VendorName"] = vendor_name
        if domain_name is not None:
            field_dict["DomainName"] = domain_name
        if client_company_domain is not None:
            field_dict["ClientCompanyDomain"] = client_company_domain
        if provider_logo is not None:
            field_dict["ProviderLogo"] = provider_logo
        if client_signature is not None:
            field_dict["ClientSignature"] = client_signature
        if vendor_signature is not None:
            field_dict["VendorSignature"] = vendor_signature
        if qr_code is not None:
            field_dict["QrCode"] = qr_code
        if bar_code is not None:
            field_dict["BarCode"] = bar_code
        if bar_code_string is not None:
            field_dict["BarCodeString"] = bar_code_string
        if po_balance is not None:
            field_dict["PoBalance"] = po_balance
        if service_terms is not None:
            field_dict["ServiceTerms"] = service_terms
        if service_total is not None:
            field_dict["ServiceTotal"] = service_total
        if repairs_total is not None:
            field_dict["RepairsTotal"] = repairs_total
        if parts_total is not None:
            field_dict["PartsTotal"] = parts_total
        if parts_total_before_discount is not None:
            field_dict["PartsTotalBeforeDiscount"] = parts_total_before_discount
        if effective_tax_rate is not None:
            field_dict["EffectiveTaxRate"] = effective_tax_rate
        if tax_amount is not None:
            field_dict["TaxAmount"] = tax_amount
        if shipping_fee is not None:
            field_dict["ShippingFee"] = shipping_fee
        if late_fee is not None:
            field_dict["LateFee"] = late_fee
        if grand_total is not None:
            field_dict["GrandTotal"] = grand_total
        if amount_paid is not None:
            field_dict["AmountPaid"] = amount_paid
        if balance_total is not None:
            field_dict["BalanceTotal"] = balance_total
        if travel_charge is not None:
            field_dict["TravelCharge"] = travel_charge
        if private_notes is not None:
            field_dict["PrivateNotes"] = private_notes
        if service_notes is not None:
            field_dict["ServiceNotes"] = service_notes
        if display_service_comments is not None:
            field_dict["DisplayServiceComments"] = display_service_comments
        if display_part_repairs is not None:
            field_dict["DisplayPartRepairs"] = display_part_repairs
        if print_separate_measurement is not None:
            field_dict["PrintSeparateMeasurement"] = print_separate_measurement
        if billing_address_1 is not None:
            field_dict["BillingAddress1"] = billing_address_1
        if billing_address_2 is not None:
            field_dict["BillingAddress2"] = billing_address_2
        if billing_first_name is not None:
            field_dict["BillingFirstName"] = billing_first_name
        if billing_last_name is not None:
            field_dict["BillingLastName"] = billing_last_name
        if billing_company is not None:
            field_dict["BillingCompany"] = billing_company
        if billing_country is not None:
            field_dict["BillingCountry"] = billing_country
        if billing_city is not None:
            field_dict["BillingCity"] = billing_city
        if billing_state is not None:
            field_dict["BillingState"] = billing_state
        if billing_zip is not None:
            field_dict["BillingZip"] = billing_zip
        if billing_phone_number is not None:
            field_dict["BillingPhoneNumber"] = billing_phone_number
        if billing_fax_number is not None:
            field_dict["BillingFaxNumber"] = billing_fax_number
        if billing_email is not None:
            field_dict["BillingEmail"] = billing_email
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
        if shipping_method is not None:
            field_dict["ShippingMethod"] = shipping_method
        if return_shipping_method is not None:
            field_dict["ReturnShippingMethod"] = return_shipping_method
        if tracking_number is not None:
            field_dict["TrackingNumber"] = tracking_number
        if provider_billing_address_1 is not None:
            field_dict["ProviderBillingAddress1"] = provider_billing_address_1
        if provider_billing_address_2 is not None:
            field_dict["ProviderBillingAddress2"] = provider_billing_address_2
        if provider_billing_first_name is not None:
            field_dict["ProviderBillingFirstName"] = provider_billing_first_name
        if provider_billing_last_name is not None:
            field_dict["ProviderBillingLastName"] = provider_billing_last_name
        if provider_billing_email is not None:
            field_dict["ProviderBillingEmail"] = provider_billing_email
        if provider_billing_company is not None:
            field_dict["ProviderBillingCompany"] = provider_billing_company
        if provider_billing_city is not None:
            field_dict["ProviderBillingCity"] = provider_billing_city
        if provider_billing_zip is not None:
            field_dict["ProviderBillingZip"] = provider_billing_zip
        if provider_billing_phone_number is not None:
            field_dict["ProviderBillingPhoneNumber"] = provider_billing_phone_number
        if provider_billing_country is not None:
            field_dict["ProviderBillingCountry"] = provider_billing_country
        if provider_billing_state is not None:
            field_dict["ProviderBillingState"] = provider_billing_state
        if provider_billing_fax_number is not None:
            field_dict["ProviderBillingFaxNumber"] = provider_billing_fax_number
        if provider_shipping_address_1 is not None:
            field_dict["ProviderShippingAddress1"] = provider_shipping_address_1
        if provider_shipping_address_2 is not None:
            field_dict["ProviderShippingAddress2"] = provider_shipping_address_2
        if provider_shipping_first_name is not None:
            field_dict["ProviderShippingFirstName"] = provider_shipping_first_name
        if provider_shipping_last_name is not None:
            field_dict["ProviderShippingLastName"] = provider_shipping_last_name
        if provider_shipping_email is not None:
            field_dict["ProviderShippingEmail"] = provider_shipping_email
        if provider_shipping_company is not None:
            field_dict["ProviderShippingCompany"] = provider_shipping_company
        if provider_shipping_city is not None:
            field_dict["ProviderShippingCity"] = provider_shipping_city
        if provider_shipping_zip is not None:
            field_dict["ProviderShippingZip"] = provider_shipping_zip
        if provider_shipping_phone_number is not None:
            field_dict["ProviderShippingPhoneNumber"] = provider_shipping_phone_number
        if provider_shipping_country is not None:
            field_dict["ProviderShippingCountry"] = provider_shipping_country
        if provider_shipping_state is not None:
            field_dict["ProviderShippingState"] = provider_shipping_state
        if provider_shipping_fax_number is not None:
            field_dict["ProviderShippingFaxNumber"] = provider_shipping_fax_number
        if culture_name is not None:
            field_dict["CultureName"] = culture_name
        if vendor_company_id is not None:
            field_dict["VendorCompanyId"] = vendor_company_id
        if client_vendor_id is not None:
            field_dict["ClientVendorId"] = client_vendor_id
        if sign_off_date is not None:
            field_dict["SignOffDate"] = sign_off_date
        if quality_control_date is not None:
            field_dict["QualityControlDate"] = quality_control_date
        if client_sign_off_on is not None:
            field_dict["ClientSignOffOn"] = client_sign_off_on
        if client_sign_off_by_name is not None:
            field_dict["ClientSignOffByName"] = client_sign_off_by_name
        if client_signed_on is not None:
            field_dict["ClientSignedOn"] = client_signed_on
        if client_sticker_notes is not None:
            field_dict["ClientStickerNotes"] = client_sticker_notes
        if asset_sticker_notes is not None:
            field_dict["AssetStickerNotes"] = asset_sticker_notes
        if order_sticker_notes is not None:
            field_dict["OrderStickerNotes"] = order_sticker_notes
        if quality_control_name is not None:
            field_dict["QualityControlName"] = quality_control_name
        if fulfilled_by_name is not None:
            field_dict["FulfilledByName"] = fulfilled_by_name
        if sign_off_name is not None:
            field_dict["SignOffName"] = sign_off_name
        if display_as_found is not None:
            field_dict["DisplayAsFound"] = display_as_found
        if display_as_left is not None:
            field_dict["DisplayAsLeft"] = display_as_left
        if created_on is not None:
            field_dict["CreatedOn"] = created_on
        if invoiced_on is not None:
            field_dict["InvoicedOn"] = invoiced_on
        if submitted_on is not None:
            field_dict["SubmittedOn"] = submitted_on
        if shipped_on is not None:
            field_dict["ShippedOn"] = shipped_on
        if completed_on is not None:
            field_dict["CompletedOn"] = completed_on
        if accepted_on is not None:
            field_dict["AcceptedOn"] = accepted_on
        if approved_on is not None:
            field_dict["ApprovedOn"] = approved_on
        if delivered_on is not None:
            field_dict["DeliveredOn"] = delivered_on
        if paid_on is not None:
            field_dict["PaidOn"] = paid_on
        if cancelled_on is not None:
            field_dict["CancelledOn"] = cancelled_on
        if fulfilled_on is not None:
            field_dict["FulfilledOn"] = fulfilled_on
        if sign_off_on is not None:
            field_dict["SignOffOn"] = sign_off_on
        if vendor_signed_on is not None:
            field_dict["VendorSignedOn"] = vendor_signed_on
        if client_notes is not None:
            field_dict["ClientNotes"] = client_notes
        if order_shipping_option is not None:
            field_dict["OrderShippingOption"] = order_shipping_option
        if shipment_status is not None:
            field_dict["ShipmentStatus"] = shipment_status
        if payment_status is not None:
            field_dict["PaymentStatus"] = payment_status
        if payment_option is not None:
            field_dict["PaymentOption"] = payment_option
        if order_status is not None:
            field_dict["OrderStatus"] = order_status
        if created_by_name is not None:
            field_dict["CreatedByName"] = created_by_name
        if completed_by_name is not None:
            field_dict["CompletedByName"] = completed_by_name
        if shipped_by_name is not None:
            field_dict["ShippedByName"] = shipped_by_name
        if accepted_by_name is not None:
            field_dict["AcceptedByName"] = accepted_by_name
        if approve_by_name is not None:
            field_dict["ApproveByName"] = approve_by_name
        if invoiced_by_name is not None:
            field_dict["InvoicedByName"] = invoiced_by_name
        if delivered_by_name is not None:
            field_dict["DeliveredByName"] = delivered_by_name
        if paid_by_name is not None:
            field_dict["PaidByName"] = paid_by_name
        if cancelled_by_name is not None:
            field_dict["CancelledByName"] = cancelled_by_name
        if sign_off_by_name is not None:
            field_dict["SignOffByName"] = sign_off_by_name
        if owner_name is not None:
            field_dict["OwnerName"] = owner_name
        if owner_department is not None:
            field_dict["OwnerDepartment"] = owner_department
        if assignee_name is not None:
            field_dict["AssigneeName"] = assignee_name
        if payment_due_on is not None:
            field_dict["PaymentDueOn"] = payment_due_on
        if process_date_option is not None:
            field_dict["ProcessDateOption"] = process_date_option
        if desired_date is not None:
            field_dict["DesiredDate"] = desired_date
        if deadline_date is not None:
            field_dict["DeadlineDate"] = deadline_date
        if vendor_sign_off_on is not None:
            field_dict["VendorSignOffOn"] = vendor_sign_off_on
        if vendor_sign_off_by_name is not None:
            field_dict["VendorSignOffByName"] = vendor_sign_off_by_name
        if service_discount is not None:
            field_dict["ServiceDiscount"] = service_discount
        if return_account is not None:
            field_dict["ReturnAccount"] = return_account
        if business_hours_from is not None:
            field_dict["BusinessHoursFrom"] = business_hours_from
        if business_hours_to is not None:
            field_dict["BusinessHoursTo"] = business_hours_to
        if client_company_alternative_names is not None:
            field_dict["ClientCompanyAlternativeNames"] = client_company_alternative_names
        if client_id is not None:
            field_dict["ClientId"] = client_id
        if client_class is not None:
            field_dict["ClientClass"] = client_class
        if client_status is not None:
            field_dict["ClientStatus"] = client_status
        if client_invoicing is not None:
            field_dict["ClientInvoicing"] = client_invoicing
        if client_standing is not None:
            field_dict["ClientStanding"] = client_standing
        if client_category is not None:
            field_dict["ClientCategory"] = client_category
        if master_template_name is not None:
            field_dict["MasterTemplateName"] = master_template_name
        if client_site_code is not None:
            field_dict["ClientSiteCode"] = client_site_code
        if order_workflow_name is not None:
            field_dict["OrderWorkflowName"] = order_workflow_name
        if request_workflow_name is not None:
            field_dict["RequestWorkflowName"] = request_workflow_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        guid = d.pop("Guid", None)

        account_number = d.pop("AccountNumber", None)

        service_order_number = d.pop("ServiceOrderNumber", None)

        service_order_number_text = d.pop("ServiceOrderNumberText", None)

        number_of_instruments = d.pop("NumberOfInstruments", None)

        parts_discount_total = d.pop("PartsDiscountTotal", None)

        po_number = d.pop("PoNumber", None)

        secondary_po = d.pop("SecondaryPo", None)

        location = d.pop("Location", None)

        def _parse_shipped_date(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shipped_date_type_0 = isoparse(data)

                return shipped_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        shipped_date = _parse_shipped_date(d.pop("ShippedDate", None))

        payment_terms = d.pop("PaymentTerms", None)

        site_access_notes = d.pop("SiteAccessNotes", None)

        grace_period = d.pop("GracePeriod", None)

        trade_in_credit = d.pop("TradeInCredit", None)

        prepaid_credit = d.pop("PrepaidCredit", None)

        interest_rate = d.pop("InterestRate", None)

        service_taxation = d.pop("ServiceTaxation", None)

        service_order_id = d.pop("ServiceOrderId", None)

        federal_number = d.pop("FederalNumber", None)

        vendor_site_id = d.pop("VendorSiteId", None)

        vendor_site = d.pop("VendorSite", None)

        site_name = d.pop("SiteName", None)

        site_code = d.pop("SiteCode", None)

        vendor_name = d.pop("VendorName", None)

        domain_name = d.pop("DomainName", None)

        client_company_domain = d.pop("ClientCompanyDomain", None)

        provider_logo = d.pop("ProviderLogo", None)

        client_signature = d.pop("ClientSignature", None)

        vendor_signature = d.pop("VendorSignature", None)

        qr_code = d.pop("QrCode", None)

        bar_code = d.pop("BarCode", None)

        bar_code_string = d.pop("BarCodeString", None)

        po_balance = d.pop("PoBalance", None)

        service_terms = d.pop("ServiceTerms", None)

        service_total = d.pop("ServiceTotal", None)

        repairs_total = d.pop("RepairsTotal", None)

        parts_total = d.pop("PartsTotal", None)

        parts_total_before_discount = d.pop("PartsTotalBeforeDiscount", None)

        effective_tax_rate = d.pop("EffectiveTaxRate", None)

        tax_amount = d.pop("TaxAmount", None)

        shipping_fee = d.pop("ShippingFee", None)

        late_fee = d.pop("LateFee", None)

        grand_total = d.pop("GrandTotal", None)

        amount_paid = d.pop("AmountPaid", None)

        balance_total = d.pop("BalanceTotal", None)

        travel_charge = d.pop("TravelCharge", None)

        private_notes = d.pop("PrivateNotes", None)

        service_notes = d.pop("ServiceNotes", None)

        display_service_comments = d.pop("DisplayServiceComments", None)

        display_part_repairs = d.pop("DisplayPartRepairs", None)

        print_separate_measurement = d.pop("PrintSeparateMeasurement", None)

        billing_address_1 = d.pop("BillingAddress1", None)

        billing_address_2 = d.pop("BillingAddress2", None)

        billing_first_name = d.pop("BillingFirstName", None)

        billing_last_name = d.pop("BillingLastName", None)

        billing_company = d.pop("BillingCompany", None)

        billing_country = d.pop("BillingCountry", None)

        billing_city = d.pop("BillingCity", None)

        billing_state = d.pop("BillingState", None)

        billing_zip = d.pop("BillingZip", None)

        billing_phone_number = d.pop("BillingPhoneNumber", None)

        billing_fax_number = d.pop("BillingFaxNumber", None)

        billing_email = d.pop("BillingEmail", None)

        shipping_address_1 = d.pop("ShippingAddress1", None)

        shipping_address_2 = d.pop("ShippingAddress2", None)

        shipping_first_name = d.pop("ShippingFirstName", None)

        shipping_last_name = d.pop("ShippingLastName", None)

        shipping_email = d.pop("ShippingEmail", None)

        shipping_company = d.pop("ShippingCompany", None)

        shipping_city = d.pop("ShippingCity", None)

        shipping_zip = d.pop("ShippingZip", None)

        shipping_phone_number = d.pop("ShippingPhoneNumber", None)

        shipping_fax_number = d.pop("ShippingFaxNumber", None)

        shipping_country = d.pop("ShippingCountry", None)

        shipping_state = d.pop("ShippingState", None)

        shipping_method = d.pop("ShippingMethod", None)

        return_shipping_method = d.pop("ReturnShippingMethod", None)

        tracking_number = d.pop("TrackingNumber", None)

        provider_billing_address_1 = d.pop("ProviderBillingAddress1", None)

        provider_billing_address_2 = d.pop("ProviderBillingAddress2", None)

        provider_billing_first_name = d.pop("ProviderBillingFirstName", None)

        provider_billing_last_name = d.pop("ProviderBillingLastName", None)

        provider_billing_email = d.pop("ProviderBillingEmail", None)

        provider_billing_company = d.pop("ProviderBillingCompany", None)

        provider_billing_city = d.pop("ProviderBillingCity", None)

        provider_billing_zip = d.pop("ProviderBillingZip", None)

        provider_billing_phone_number = d.pop("ProviderBillingPhoneNumber", None)

        provider_billing_country = d.pop("ProviderBillingCountry", None)

        provider_billing_state = d.pop("ProviderBillingState", None)

        provider_billing_fax_number = d.pop("ProviderBillingFaxNumber", None)

        provider_shipping_address_1 = d.pop("ProviderShippingAddress1", None)

        provider_shipping_address_2 = d.pop("ProviderShippingAddress2", None)

        provider_shipping_first_name = d.pop("ProviderShippingFirstName", None)

        provider_shipping_last_name = d.pop("ProviderShippingLastName", None)

        provider_shipping_email = d.pop("ProviderShippingEmail", None)

        provider_shipping_company = d.pop("ProviderShippingCompany", None)

        provider_shipping_city = d.pop("ProviderShippingCity", None)

        provider_shipping_zip = d.pop("ProviderShippingZip", None)

        provider_shipping_phone_number = d.pop("ProviderShippingPhoneNumber", None)

        provider_shipping_country = d.pop("ProviderShippingCountry", None)

        provider_shipping_state = d.pop("ProviderShippingState", None)

        provider_shipping_fax_number = d.pop("ProviderShippingFaxNumber", None)

        culture_name = d.pop("CultureName", None)

        vendor_company_id = d.pop("VendorCompanyId", None)

        client_vendor_id = d.pop("ClientVendorId", None)

        def _parse_sign_off_date(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sign_off_date_type_0 = isoparse(data)

                return sign_off_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        sign_off_date = _parse_sign_off_date(d.pop("SignOffDate", None))

        _quality_control_date = d.pop("QualityControlDate", None)
        quality_control_date: Optional[datetime.datetime]
        if not _quality_control_date:
            quality_control_date = None
        elif _quality_control_date is None:
            quality_control_date = None
        else:
            quality_control_date = isoparse(_quality_control_date)

        def _parse_client_sign_off_on(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                client_sign_off_on_type_0 = isoparse(data)

                return client_sign_off_on_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        client_sign_off_on = _parse_client_sign_off_on(d.pop("ClientSignOffOn", None))

        client_sign_off_by_name = d.pop("ClientSignOffByName", None)

        def _parse_client_signed_on(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                client_signed_on_type_0 = isoparse(data)

                return client_signed_on_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        client_signed_on = _parse_client_signed_on(d.pop("ClientSignedOn", None))

        client_sticker_notes = d.pop("ClientStickerNotes", None)

        asset_sticker_notes = d.pop("AssetStickerNotes", None)

        order_sticker_notes = d.pop("OrderStickerNotes", None)

        quality_control_name = d.pop("QualityControlName", None)

        fulfilled_by_name = d.pop("FulfilledByName", None)

        sign_off_name = d.pop("SignOffName", None)

        display_as_found = d.pop("DisplayAsFound", None)

        display_as_left = d.pop("DisplayAsLeft", None)

        _created_on = d.pop("CreatedOn", None)
        created_on: Optional[datetime.datetime]
        if not _created_on:
            created_on = None
        else:
            created_on = isoparse(_created_on)

        def _parse_invoiced_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                invoiced_on_type_0 = isoparse(data)

                return invoiced_on_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        invoiced_on = _parse_invoiced_on(d.pop("InvoicedOn", None))

        def _parse_submitted_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                submitted_on_type_0 = isoparse(data)

                return submitted_on_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        submitted_on = _parse_submitted_on(d.pop("SubmittedOn", None))

        def _parse_shipped_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shipped_on_type_0 = isoparse(data)

                return shipped_on_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        shipped_on = _parse_shipped_on(d.pop("ShippedOn", None))

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

        def _parse_accepted_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                accepted_on_type_0 = isoparse(data)

                return accepted_on_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        accepted_on = _parse_accepted_on(d.pop("AcceptedOn", None))

        def _parse_approved_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_on_type_0 = isoparse(data)

                return approved_on_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        approved_on = _parse_approved_on(d.pop("ApprovedOn", None))

        def _parse_delivered_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delivered_on_type_0 = isoparse(data)

                return delivered_on_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        delivered_on = _parse_delivered_on(d.pop("DeliveredOn", None))

        def _parse_paid_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                paid_on_type_0 = isoparse(data)

                return paid_on_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        paid_on = _parse_paid_on(d.pop("PaidOn", None))

        def _parse_cancelled_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cancelled_on_type_0 = isoparse(data)

                return cancelled_on_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        cancelled_on = _parse_cancelled_on(d.pop("CancelledOn", None))

        def _parse_fulfilled_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fulfilled_on_type_0 = isoparse(data)

                return fulfilled_on_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        fulfilled_on = _parse_fulfilled_on(d.pop("FulfilledOn", None))

        def _parse_sign_off_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sign_off_on_type_0 = isoparse(data)

                return sign_off_on_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        sign_off_on = _parse_sign_off_on(d.pop("SignOffOn", None))

        def _parse_vendor_signed_on(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                vendor_signed_on_type_0 = isoparse(data)

                return vendor_signed_on_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        vendor_signed_on = _parse_vendor_signed_on(d.pop("VendorSignedOn", None))

        def _parse_client_notes(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        client_notes = _parse_client_notes(d.pop("ClientNotes", None))

        order_shipping_option = d.pop("OrderShippingOption", None)

        shipment_status = d.pop("ShipmentStatus", None)

        payment_status = d.pop("PaymentStatus", None)

        payment_option = d.pop("PaymentOption", None)

        order_status = d.pop("OrderStatus", None)

        created_by_name = d.pop("CreatedByName", None)

        def _parse_completed_by_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        completed_by_name = _parse_completed_by_name(d.pop("CompletedByName", None))

        def _parse_shipped_by_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        shipped_by_name = _parse_shipped_by_name(d.pop("ShippedByName", None))

        def _parse_accepted_by_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        accepted_by_name = _parse_accepted_by_name(d.pop("AcceptedByName", None))

        def _parse_approve_by_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        approve_by_name = _parse_approve_by_name(d.pop("ApproveByName", None))

        def _parse_invoiced_by_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        invoiced_by_name = _parse_invoiced_by_name(d.pop("InvoicedByName", None))

        def _parse_delivered_by_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        delivered_by_name = _parse_delivered_by_name(d.pop("DeliveredByName", None))

        def _parse_paid_by_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        paid_by_name = _parse_paid_by_name(d.pop("PaidByName", None))

        def _parse_cancelled_by_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        cancelled_by_name = _parse_cancelled_by_name(d.pop("CancelledByName", None))

        def _parse_sign_off_by_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        sign_off_by_name = _parse_sign_off_by_name(d.pop("SignOffByName", None))

        def _parse_owner_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        owner_name = _parse_owner_name(d.pop("OwnerName", None))

        def _parse_owner_department(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        owner_department = _parse_owner_department(d.pop("OwnerDepartment", None))

        def _parse_assignee_name(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        assignee_name = _parse_assignee_name(d.pop("AssigneeName", None))

        def _parse_payment_due_on(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                payment_due_on_type_0 = isoparse(data)

                return payment_due_on_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        payment_due_on = _parse_payment_due_on(d.pop("PaymentDueOn", None))

        process_date_option = d.pop("ProcessDateOption", None)

        def _parse_desired_date(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                desired_date_type_0 = isoparse(data)

                return desired_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        desired_date = _parse_desired_date(d.pop("DesiredDate", None))

        def _parse_deadline_date(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deadline_date_type_0 = isoparse(data)

                return deadline_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        deadline_date = _parse_deadline_date(d.pop("DeadlineDate", None))

        _vendor_sign_off_on = d.pop("VendorSignOffOn", None)
        vendor_sign_off_on: Optional[datetime.datetime]
        if not _vendor_sign_off_on:
            vendor_sign_off_on = None
        else:
            vendor_sign_off_on = isoparse(_vendor_sign_off_on)

        vendor_sign_off_by_name = d.pop("VendorSignOffByName", None)

        service_discount = d.pop("ServiceDiscount", None)

        return_account = d.pop("ReturnAccount", None)

        def _parse_business_hours_from(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                business_hours_from_type_0 = isoparse(data)

                return business_hours_from_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        business_hours_from = _parse_business_hours_from(d.pop("BusinessHoursFrom", None))

        def _parse_business_hours_to(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                business_hours_to_type_0 = isoparse(data)

                return business_hours_to_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        business_hours_to = _parse_business_hours_to(d.pop("BusinessHoursTo", None))

        client_company_alternative_names = d.pop("ClientCompanyAlternativeNames", None)

        client_id = d.pop("ClientId", None)

        client_class = d.pop("ClientClass", None)

        client_status = d.pop("ClientStatus", None)

        client_invoicing = d.pop("ClientInvoicing", None)

        client_standing = d.pop("ClientStanding", None)

        client_category = d.pop("ClientCategory", None)

        master_template_name = d.pop("MasterTemplateName", None)

        client_site_code = d.pop("ClientSiteCode", None)

        order_workflow_name = d.pop("OrderWorkflowName", None)

        request_workflow_name = d.pop("RequestWorkflowName", None)

        qualer_api_models_report_datasets_to_service_order_response = cls(
            guid=guid,
            account_number=account_number,
            service_order_number=service_order_number,
            service_order_number_text=service_order_number_text,
            number_of_instruments=number_of_instruments,
            parts_discount_total=parts_discount_total,
            po_number=po_number,
            secondary_po=secondary_po,
            location=location,
            shipped_date=shipped_date,
            payment_terms=payment_terms,
            site_access_notes=site_access_notes,
            grace_period=grace_period,
            trade_in_credit=trade_in_credit,
            prepaid_credit=prepaid_credit,
            interest_rate=interest_rate,
            service_taxation=service_taxation,
            service_order_id=service_order_id,
            federal_number=federal_number,
            vendor_site_id=vendor_site_id,
            vendor_site=vendor_site,
            site_name=site_name,
            site_code=site_code,
            vendor_name=vendor_name,
            domain_name=domain_name,
            client_company_domain=client_company_domain,
            provider_logo=provider_logo,
            client_signature=client_signature,
            vendor_signature=vendor_signature,
            qr_code=qr_code,
            bar_code=bar_code,
            bar_code_string=bar_code_string,
            po_balance=po_balance,
            service_terms=service_terms,
            service_total=service_total,
            repairs_total=repairs_total,
            parts_total=parts_total,
            parts_total_before_discount=parts_total_before_discount,
            effective_tax_rate=effective_tax_rate,
            tax_amount=tax_amount,
            shipping_fee=shipping_fee,
            late_fee=late_fee,
            grand_total=grand_total,
            amount_paid=amount_paid,
            balance_total=balance_total,
            travel_charge=travel_charge,
            private_notes=private_notes,
            service_notes=service_notes,
            display_service_comments=display_service_comments,
            display_part_repairs=display_part_repairs,
            print_separate_measurement=print_separate_measurement,
            billing_address_1=billing_address_1,
            billing_address_2=billing_address_2,
            billing_first_name=billing_first_name,
            billing_last_name=billing_last_name,
            billing_company=billing_company,
            billing_country=billing_country,
            billing_city=billing_city,
            billing_state=billing_state,
            billing_zip=billing_zip,
            billing_phone_number=billing_phone_number,
            billing_fax_number=billing_fax_number,
            billing_email=billing_email,
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
            shipping_method=shipping_method,
            return_shipping_method=return_shipping_method,
            tracking_number=tracking_number,
            provider_billing_address_1=provider_billing_address_1,
            provider_billing_address_2=provider_billing_address_2,
            provider_billing_first_name=provider_billing_first_name,
            provider_billing_last_name=provider_billing_last_name,
            provider_billing_email=provider_billing_email,
            provider_billing_company=provider_billing_company,
            provider_billing_city=provider_billing_city,
            provider_billing_zip=provider_billing_zip,
            provider_billing_phone_number=provider_billing_phone_number,
            provider_billing_country=provider_billing_country,
            provider_billing_state=provider_billing_state,
            provider_billing_fax_number=provider_billing_fax_number,
            provider_shipping_address_1=provider_shipping_address_1,
            provider_shipping_address_2=provider_shipping_address_2,
            provider_shipping_first_name=provider_shipping_first_name,
            provider_shipping_last_name=provider_shipping_last_name,
            provider_shipping_email=provider_shipping_email,
            provider_shipping_company=provider_shipping_company,
            provider_shipping_city=provider_shipping_city,
            provider_shipping_zip=provider_shipping_zip,
            provider_shipping_phone_number=provider_shipping_phone_number,
            provider_shipping_country=provider_shipping_country,
            provider_shipping_state=provider_shipping_state,
            provider_shipping_fax_number=provider_shipping_fax_number,
            culture_name=culture_name,
            vendor_company_id=vendor_company_id,
            client_vendor_id=client_vendor_id,
            sign_off_date=sign_off_date,
            quality_control_date=quality_control_date,
            client_sign_off_on=client_sign_off_on,
            client_sign_off_by_name=client_sign_off_by_name,
            client_signed_on=client_signed_on,
            client_sticker_notes=client_sticker_notes,
            asset_sticker_notes=asset_sticker_notes,
            order_sticker_notes=order_sticker_notes,
            quality_control_name=quality_control_name,
            fulfilled_by_name=fulfilled_by_name,
            sign_off_name=sign_off_name,
            display_as_found=display_as_found,
            display_as_left=display_as_left,
            created_on=created_on,
            invoiced_on=invoiced_on,
            submitted_on=submitted_on,
            shipped_on=shipped_on,
            completed_on=completed_on,
            accepted_on=accepted_on,
            approved_on=approved_on,
            delivered_on=delivered_on,
            paid_on=paid_on,
            cancelled_on=cancelled_on,
            fulfilled_on=fulfilled_on,
            sign_off_on=sign_off_on,
            vendor_signed_on=vendor_signed_on,
            client_notes=client_notes,
            order_shipping_option=order_shipping_option,
            shipment_status=shipment_status,
            payment_status=payment_status,
            payment_option=payment_option,
            order_status=order_status,
            created_by_name=created_by_name,
            completed_by_name=completed_by_name,
            shipped_by_name=shipped_by_name,
            accepted_by_name=accepted_by_name,
            approve_by_name=approve_by_name,
            invoiced_by_name=invoiced_by_name,
            delivered_by_name=delivered_by_name,
            paid_by_name=paid_by_name,
            cancelled_by_name=cancelled_by_name,
            sign_off_by_name=sign_off_by_name,
            owner_name=owner_name,
            owner_department=owner_department,
            assignee_name=assignee_name,
            payment_due_on=payment_due_on,
            process_date_option=process_date_option,
            desired_date=desired_date,
            deadline_date=deadline_date,
            vendor_sign_off_on=vendor_sign_off_on,
            vendor_sign_off_by_name=vendor_sign_off_by_name,
            service_discount=service_discount,
            return_account=return_account,
            business_hours_from=business_hours_from,
            business_hours_to=business_hours_to,
            client_company_alternative_names=client_company_alternative_names,
            client_id=client_id,
            client_class=client_class,
            client_status=client_status,
            client_invoicing=client_invoicing,
            client_standing=client_standing,
            client_category=client_category,
            master_template_name=master_template_name,
            client_site_code=client_site_code,
            order_workflow_name=order_workflow_name,
            request_workflow_name=request_workflow_name,
        )

        qualer_api_models_report_datasets_to_service_order_response.additional_properties = d
        return qualer_api_models_report_datasets_to_service_order_response

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
