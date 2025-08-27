import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsReportDatasetsToServiceOrderResponse")


@_attrs_define
class QualerApiModelsReportDatasetsToServiceOrderResponse:
    """
    Attributes:
        guid (Union[None, Unset, str]):
        account_number (Union[None, Unset, str]):
        service_order_number (Union[None, Unset, int]):
        service_order_number_text (Union[None, Unset, str]):
        number_of_instruments (Union[None, Unset, int]):
        parts_discount_total (Union[None, Unset, float]):
        po_number (Union[None, Unset, str]):
        secondary_po (Union[None, Unset, str]):
        location (Union[None, Unset, str]):
        shipped_date (Union[None, Unset, datetime.datetime]):
        payment_terms (Union[None, Unset, int]):
        site_access_notes (Union[None, Unset, str]):
        grace_period (Union[None, Unset, int]):
        trade_in_credit (Union[None, Unset, float]):
        prepaid_credit (Union[None, Unset, float]):
        interest_rate (Union[None, Unset, float]):
        service_taxation (Union[None, Unset, int]):
        service_order_id (Union[None, Unset, int]):
        federal_number (Union[None, Unset, str]):
        vendor_site_id (Union[None, Unset, int]):
        vendor_site (Union[None, Unset, str]):
        site_name (Union[None, Unset, str]):
        site_code (Union[None, Unset, str]):
        vendor_name (Union[None, Unset, str]):
        domain_name (Union[None, Unset, str]):
        client_company_domain (Union[None, Unset, str]):
        provider_logo (Union[None, Unset, str]):
        client_signature (Union[None, Unset, str]):
        vendor_signature (Union[None, Unset, str]):
        qr_code (Union[None, Unset, str]):
        bar_code (Union[None, Unset, str]):
        bar_code_string (Union[None, Unset, str]):
        po_balance (Union[None, Unset, float]):
        service_terms (Union[None, Unset, str]):
        service_total (Union[None, Unset, float]):
        repairs_total (Union[None, Unset, float]):
        parts_total (Union[None, Unset, float]):
        parts_total_before_discount (Union[None, Unset, float]):
        effective_tax_rate (Union[None, Unset, float]):
        tax_amount (Union[None, Unset, float]):
        shipping_fee (Union[None, Unset, float]):
        late_fee (Union[None, Unset, float]):
        grand_total (Union[None, Unset, float]):
        amount_paid (Union[None, Unset, float]):
        balance_total (Union[None, Unset, float]):
        travel_charge (Union[None, Unset, float]):
        private_notes (Union[None, Unset, str]):
        service_notes (Union[None, Unset, str]):
        display_service_comments (Union[None, Unset, bool]):
        display_part_repairs (Union[None, Unset, bool]):
        print_separate_measurement (Union[None, Unset, bool]):
        billing_address_1 (Union[None, Unset, str]):
        billing_address_2 (Union[None, Unset, str]):
        billing_first_name (Union[None, Unset, str]):
        billing_last_name (Union[None, Unset, str]):
        billing_company (Union[None, Unset, str]):
        billing_country (Union[None, Unset, str]):
        billing_city (Union[None, Unset, str]):
        billing_state (Union[None, Unset, str]):
        billing_zip (Union[None, Unset, str]):
        billing_phone_number (Union[None, Unset, str]):
        billing_fax_number (Union[None, Unset, str]):
        billing_email (Union[None, Unset, str]):
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
        shipping_method (Union[None, Unset, str]):
        return_shipping_method (Union[None, Unset, str]):
        tracking_number (Union[None, Unset, str]):
        provider_billing_address_1 (Union[None, Unset, str]):
        provider_billing_address_2 (Union[None, Unset, str]):
        provider_billing_first_name (Union[None, Unset, str]):
        provider_billing_last_name (Union[None, Unset, str]):
        provider_billing_email (Union[None, Unset, str]):
        provider_billing_company (Union[None, Unset, str]):
        provider_billing_city (Union[None, Unset, str]):
        provider_billing_zip (Union[None, Unset, str]):
        provider_billing_phone_number (Union[None, Unset, str]):
        provider_billing_country (Union[None, Unset, str]):
        provider_billing_state (Union[None, Unset, str]):
        provider_billing_fax_number (Union[None, Unset, str]):
        provider_shipping_address_1 (Union[None, Unset, str]):
        provider_shipping_address_2 (Union[None, Unset, str]):
        provider_shipping_first_name (Union[None, Unset, str]):
        provider_shipping_last_name (Union[None, Unset, str]):
        provider_shipping_email (Union[None, Unset, str]):
        provider_shipping_company (Union[None, Unset, str]):
        provider_shipping_city (Union[None, Unset, str]):
        provider_shipping_zip (Union[None, Unset, str]):
        provider_shipping_phone_number (Union[None, Unset, str]):
        provider_shipping_country (Union[None, Unset, str]):
        provider_shipping_state (Union[None, Unset, str]):
        provider_shipping_fax_number (Union[None, Unset, str]):
        culture_name (Union[None, Unset, str]):
        vendor_company_id (Union[None, Unset, int]):
        client_vendor_id (Union[None, Unset, int]):
        sign_off_date (Union[None, Unset, datetime.datetime]):
        quality_control_date (Union[None, Unset, datetime.datetime]):
        client_sign_off_on (Union[None, Unset, datetime.datetime]):
        client_sign_off_by_name (Union[None, Unset, str]):
        client_signed_on (Union[None, Unset, datetime.datetime]):
        client_sticker_notes (Union[None, Unset, str]):
        asset_sticker_notes (Union[None, Unset, str]):
        order_sticker_notes (Union[None, Unset, str]):
        quality_control_name (Union[None, Unset, str]):
        fulfilled_by_name (Union[None, Unset, str]):
        sign_off_name (Union[None, Unset, str]):
        display_as_found (Union[None, Unset, bool]):
        display_as_left (Union[None, Unset, bool]):
        created_on (Union[None, Unset, datetime.datetime]):
        invoiced_on (Union[None, Unset, datetime.datetime]):
        submitted_on (Union[None, Unset, datetime.datetime]):
        shipped_on (Union[None, Unset, datetime.datetime]):
        completed_on (Union[None, Unset, datetime.datetime]):
        accepted_on (Union[None, Unset, datetime.datetime]):
        approved_on (Union[None, Unset, datetime.datetime]):
        delivered_on (Union[None, Unset, datetime.datetime]):
        paid_on (Union[None, Unset, datetime.datetime]):
        cancelled_on (Union[None, Unset, datetime.datetime]):
        fulfilled_on (Union[None, Unset, datetime.datetime]):
        sign_off_on (Union[None, Unset, datetime.datetime]):
        vendor_signed_on (Union[None, Unset, datetime.datetime]):
        client_notes (Union[None, Unset, str]):
        order_shipping_option (Union[None, Unset, int]):
        shipment_status (Union[None, Unset, int]):
        payment_status (Union[None, Unset, int]):
        payment_option (Union[None, Unset, str]):
        order_status (Union[None, Unset, int]):
        created_by_name (Union[None, Unset, str]):
        completed_by_name (Union[None, Unset, str]):
        shipped_by_name (Union[None, Unset, str]):
        accepted_by_name (Union[None, Unset, str]):
        approve_by_name (Union[None, Unset, str]):
        invoiced_by_name (Union[None, Unset, str]):
        delivered_by_name (Union[None, Unset, str]):
        paid_by_name (Union[None, Unset, str]):
        cancelled_by_name (Union[None, Unset, str]):
        sign_off_by_name (Union[None, Unset, str]):
        owner_name (Union[None, Unset, str]):
        owner_department (Union[None, Unset, str]):
        assignee_name (Union[None, Unset, str]):
        payment_due_on (Union[None, Unset, datetime.datetime]):
        process_date_option (Union[None, Unset, int]):
        desired_date (Union[None, Unset, datetime.datetime]):
        deadline_date (Union[None, Unset, datetime.datetime]):
        vendor_sign_off_on (Union[None, Unset, datetime.datetime]):
        vendor_sign_off_by_name (Union[None, Unset, str]):
        service_discount (Union[None, Unset, float]):
        return_account (Union[None, Unset, str]):
        business_hours_from (Union[None, Unset, datetime.datetime]):
        business_hours_to (Union[None, Unset, datetime.datetime]):
        client_company_alternative_names (Union[None, Unset, str]):
        client_id (Union[None, Unset, int]):
        client_class (Union[None, Unset, str]):
        client_status (Union[None, Unset, str]):
        client_invoicing (Union[None, Unset, str]):
        client_standing (Union[None, Unset, str]):
        client_category (Union[None, Unset, str]):
        master_template_name (Union[None, Unset, str]):
        client_site_code (Union[None, Unset, str]):
        order_workflow_name (Union[None, Unset, str]):
        request_workflow_name (Union[None, Unset, str]):
    """

    guid: Union[None, Unset, str] = UNSET
    account_number: Union[None, Unset, str] = UNSET
    service_order_number: Union[None, Unset, int] = UNSET
    service_order_number_text: Union[None, Unset, str] = UNSET
    number_of_instruments: Union[None, Unset, int] = UNSET
    parts_discount_total: Union[None, Unset, float] = UNSET
    po_number: Union[None, Unset, str] = UNSET
    secondary_po: Union[None, Unset, str] = UNSET
    location: Union[None, Unset, str] = UNSET
    shipped_date: Union[None, Unset, datetime.datetime] = UNSET
    payment_terms: Union[None, Unset, int] = UNSET
    site_access_notes: Union[None, Unset, str] = UNSET
    grace_period: Union[None, Unset, int] = UNSET
    trade_in_credit: Union[None, Unset, float] = UNSET
    prepaid_credit: Union[None, Unset, float] = UNSET
    interest_rate: Union[None, Unset, float] = UNSET
    service_taxation: Union[None, Unset, int] = UNSET
    service_order_id: Union[None, Unset, int] = UNSET
    federal_number: Union[None, Unset, str] = UNSET
    vendor_site_id: Union[None, Unset, int] = UNSET
    vendor_site: Union[None, Unset, str] = UNSET
    site_name: Union[None, Unset, str] = UNSET
    site_code: Union[None, Unset, str] = UNSET
    vendor_name: Union[None, Unset, str] = UNSET
    domain_name: Union[None, Unset, str] = UNSET
    client_company_domain: Union[None, Unset, str] = UNSET
    provider_logo: Union[None, Unset, str] = UNSET
    client_signature: Union[None, Unset, str] = UNSET
    vendor_signature: Union[None, Unset, str] = UNSET
    qr_code: Union[None, Unset, str] = UNSET
    bar_code: Union[None, Unset, str] = UNSET
    bar_code_string: Union[None, Unset, str] = UNSET
    po_balance: Union[None, Unset, float] = UNSET
    service_terms: Union[None, Unset, str] = UNSET
    service_total: Union[None, Unset, float] = UNSET
    repairs_total: Union[None, Unset, float] = UNSET
    parts_total: Union[None, Unset, float] = UNSET
    parts_total_before_discount: Union[None, Unset, float] = UNSET
    effective_tax_rate: Union[None, Unset, float] = UNSET
    tax_amount: Union[None, Unset, float] = UNSET
    shipping_fee: Union[None, Unset, float] = UNSET
    late_fee: Union[None, Unset, float] = UNSET
    grand_total: Union[None, Unset, float] = UNSET
    amount_paid: Union[None, Unset, float] = UNSET
    balance_total: Union[None, Unset, float] = UNSET
    travel_charge: Union[None, Unset, float] = UNSET
    private_notes: Union[None, Unset, str] = UNSET
    service_notes: Union[None, Unset, str] = UNSET
    display_service_comments: Union[None, Unset, bool] = UNSET
    display_part_repairs: Union[None, Unset, bool] = UNSET
    print_separate_measurement: Union[None, Unset, bool] = UNSET
    billing_address_1: Union[None, Unset, str] = UNSET
    billing_address_2: Union[None, Unset, str] = UNSET
    billing_first_name: Union[None, Unset, str] = UNSET
    billing_last_name: Union[None, Unset, str] = UNSET
    billing_company: Union[None, Unset, str] = UNSET
    billing_country: Union[None, Unset, str] = UNSET
    billing_city: Union[None, Unset, str] = UNSET
    billing_state: Union[None, Unset, str] = UNSET
    billing_zip: Union[None, Unset, str] = UNSET
    billing_phone_number: Union[None, Unset, str] = UNSET
    billing_fax_number: Union[None, Unset, str] = UNSET
    billing_email: Union[None, Unset, str] = UNSET
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
    shipping_method: Union[None, Unset, str] = UNSET
    return_shipping_method: Union[None, Unset, str] = UNSET
    tracking_number: Union[None, Unset, str] = UNSET
    provider_billing_address_1: Union[None, Unset, str] = UNSET
    provider_billing_address_2: Union[None, Unset, str] = UNSET
    provider_billing_first_name: Union[None, Unset, str] = UNSET
    provider_billing_last_name: Union[None, Unset, str] = UNSET
    provider_billing_email: Union[None, Unset, str] = UNSET
    provider_billing_company: Union[None, Unset, str] = UNSET
    provider_billing_city: Union[None, Unset, str] = UNSET
    provider_billing_zip: Union[None, Unset, str] = UNSET
    provider_billing_phone_number: Union[None, Unset, str] = UNSET
    provider_billing_country: Union[None, Unset, str] = UNSET
    provider_billing_state: Union[None, Unset, str] = UNSET
    provider_billing_fax_number: Union[None, Unset, str] = UNSET
    provider_shipping_address_1: Union[None, Unset, str] = UNSET
    provider_shipping_address_2: Union[None, Unset, str] = UNSET
    provider_shipping_first_name: Union[None, Unset, str] = UNSET
    provider_shipping_last_name: Union[None, Unset, str] = UNSET
    provider_shipping_email: Union[None, Unset, str] = UNSET
    provider_shipping_company: Union[None, Unset, str] = UNSET
    provider_shipping_city: Union[None, Unset, str] = UNSET
    provider_shipping_zip: Union[None, Unset, str] = UNSET
    provider_shipping_phone_number: Union[None, Unset, str] = UNSET
    provider_shipping_country: Union[None, Unset, str] = UNSET
    provider_shipping_state: Union[None, Unset, str] = UNSET
    provider_shipping_fax_number: Union[None, Unset, str] = UNSET
    culture_name: Union[None, Unset, str] = UNSET
    vendor_company_id: Union[None, Unset, int] = UNSET
    client_vendor_id: Union[None, Unset, int] = UNSET
    sign_off_date: Union[None, Unset, datetime.datetime] = UNSET
    quality_control_date: Union[None, Unset, datetime.datetime] = UNSET
    client_sign_off_on: Union[None, Unset, datetime.datetime] = UNSET
    client_sign_off_by_name: Union[None, Unset, str] = UNSET
    client_signed_on: Union[None, Unset, datetime.datetime] = UNSET
    client_sticker_notes: Union[None, Unset, str] = UNSET
    asset_sticker_notes: Union[None, Unset, str] = UNSET
    order_sticker_notes: Union[None, Unset, str] = UNSET
    quality_control_name: Union[None, Unset, str] = UNSET
    fulfilled_by_name: Union[None, Unset, str] = UNSET
    sign_off_name: Union[None, Unset, str] = UNSET
    display_as_found: Union[None, Unset, bool] = UNSET
    display_as_left: Union[None, Unset, bool] = UNSET
    created_on: Union[None, Unset, datetime.datetime] = UNSET
    invoiced_on: Union[None, Unset, datetime.datetime] = UNSET
    submitted_on: Union[None, Unset, datetime.datetime] = UNSET
    shipped_on: Union[None, Unset, datetime.datetime] = UNSET
    completed_on: Union[None, Unset, datetime.datetime] = UNSET
    accepted_on: Union[None, Unset, datetime.datetime] = UNSET
    approved_on: Union[None, Unset, datetime.datetime] = UNSET
    delivered_on: Union[None, Unset, datetime.datetime] = UNSET
    paid_on: Union[None, Unset, datetime.datetime] = UNSET
    cancelled_on: Union[None, Unset, datetime.datetime] = UNSET
    fulfilled_on: Union[None, Unset, datetime.datetime] = UNSET
    sign_off_on: Union[None, Unset, datetime.datetime] = UNSET
    vendor_signed_on: Union[None, Unset, datetime.datetime] = UNSET
    client_notes: Union[None, Unset, str] = UNSET
    order_shipping_option: Union[None, Unset, int] = UNSET
    shipment_status: Union[None, Unset, int] = UNSET
    payment_status: Union[None, Unset, int] = UNSET
    payment_option: Union[None, Unset, str] = UNSET
    order_status: Union[None, Unset, int] = UNSET
    created_by_name: Union[None, Unset, str] = UNSET
    completed_by_name: Union[None, Unset, str] = UNSET
    shipped_by_name: Union[None, Unset, str] = UNSET
    accepted_by_name: Union[None, Unset, str] = UNSET
    approve_by_name: Union[None, Unset, str] = UNSET
    invoiced_by_name: Union[None, Unset, str] = UNSET
    delivered_by_name: Union[None, Unset, str] = UNSET
    paid_by_name: Union[None, Unset, str] = UNSET
    cancelled_by_name: Union[None, Unset, str] = UNSET
    sign_off_by_name: Union[None, Unset, str] = UNSET
    owner_name: Union[None, Unset, str] = UNSET
    owner_department: Union[None, Unset, str] = UNSET
    assignee_name: Union[None, Unset, str] = UNSET
    payment_due_on: Union[None, Unset, datetime.datetime] = UNSET
    process_date_option: Union[None, Unset, int] = UNSET
    desired_date: Union[None, Unset, datetime.datetime] = UNSET
    deadline_date: Union[None, Unset, datetime.datetime] = UNSET
    vendor_sign_off_on: Union[None, Unset, datetime.datetime] = UNSET
    vendor_sign_off_by_name: Union[None, Unset, str] = UNSET
    service_discount: Union[None, Unset, float] = UNSET
    return_account: Union[None, Unset, str] = UNSET
    business_hours_from: Union[None, Unset, datetime.datetime] = UNSET
    business_hours_to: Union[None, Unset, datetime.datetime] = UNSET
    client_company_alternative_names: Union[None, Unset, str] = UNSET
    client_id: Union[None, Unset, int] = UNSET
    client_class: Union[None, Unset, str] = UNSET
    client_status: Union[None, Unset, str] = UNSET
    client_invoicing: Union[None, Unset, str] = UNSET
    client_standing: Union[None, Unset, str] = UNSET
    client_category: Union[None, Unset, str] = UNSET
    master_template_name: Union[None, Unset, str] = UNSET
    client_site_code: Union[None, Unset, str] = UNSET
    order_workflow_name: Union[None, Unset, str] = UNSET
    request_workflow_name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        guid = self.guid

        account_number = self.account_number

        service_order_number = self.service_order_number

        service_order_number_text = self.service_order_number_text

        number_of_instruments = self.number_of_instruments

        parts_discount_total = self.parts_discount_total

        po_number = self.po_number

        secondary_po = self.secondary_po

        location = self.location

        shipped_date: Union[None, Unset, str]
        if isinstance(self.shipped_date, Unset):
            shipped_date = UNSET
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

        sign_off_date: Union[None, Unset, str]
        if isinstance(self.sign_off_date, Unset):
            sign_off_date = UNSET
        elif isinstance(self.sign_off_date, datetime.datetime):
            sign_off_date = self.sign_off_date.isoformat()
        else:
            sign_off_date = self.sign_off_date

        quality_control_date: Union[None, Unset, str] = UNSET
        if self.quality_control_date and not isinstance(
            self.quality_control_date, Unset
        ):
            quality_control_date = self.quality_control_date.isoformat()

        client_sign_off_on: Union[None, Unset, str]
        if isinstance(self.client_sign_off_on, Unset):
            client_sign_off_on = UNSET
        elif isinstance(self.client_sign_off_on, datetime.datetime):
            client_sign_off_on = self.client_sign_off_on.isoformat()
        else:
            client_sign_off_on = self.client_sign_off_on

        client_sign_off_by_name = self.client_sign_off_by_name

        client_signed_on: Union[None, Unset, str]
        if isinstance(self.client_signed_on, Unset):
            client_signed_on = UNSET
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

        created_on: Union[None, Unset, str] = UNSET
        if self.created_on and not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        invoiced_on: Union[None, Unset, str]
        if isinstance(self.invoiced_on, Unset):
            invoiced_on = UNSET
        elif isinstance(self.invoiced_on, datetime.datetime):
            invoiced_on = self.invoiced_on.isoformat()
        else:
            invoiced_on = self.invoiced_on

        submitted_on: Union[None, Unset, str]
        if isinstance(self.submitted_on, Unset):
            submitted_on = UNSET
        elif isinstance(self.submitted_on, datetime.datetime):
            submitted_on = self.submitted_on.isoformat()
        else:
            submitted_on = self.submitted_on

        shipped_on: Union[None, Unset, str]
        if isinstance(self.shipped_on, Unset):
            shipped_on = UNSET
        elif isinstance(self.shipped_on, datetime.datetime):
            shipped_on = self.shipped_on.isoformat()
        else:
            shipped_on = self.shipped_on

        completed_on: Union[None, Unset, str]
        if isinstance(self.completed_on, Unset):
            completed_on = UNSET
        elif isinstance(self.completed_on, datetime.datetime):
            completed_on = self.completed_on.isoformat()
        else:
            completed_on = self.completed_on

        accepted_on: Union[None, Unset, str]
        if isinstance(self.accepted_on, Unset):
            accepted_on = UNSET
        elif isinstance(self.accepted_on, datetime.datetime):
            accepted_on = self.accepted_on.isoformat()
        else:
            accepted_on = self.accepted_on

        approved_on: Union[None, Unset, str]
        if isinstance(self.approved_on, Unset):
            approved_on = UNSET
        elif isinstance(self.approved_on, datetime.datetime):
            approved_on = self.approved_on.isoformat()
        else:
            approved_on = self.approved_on

        delivered_on: Union[None, Unset, str]
        if isinstance(self.delivered_on, Unset):
            delivered_on = UNSET
        elif isinstance(self.delivered_on, datetime.datetime):
            delivered_on = self.delivered_on.isoformat()
        else:
            delivered_on = self.delivered_on

        paid_on: Union[None, Unset, str]
        if isinstance(self.paid_on, Unset):
            paid_on = UNSET
        elif isinstance(self.paid_on, datetime.datetime):
            paid_on = self.paid_on.isoformat()
        else:
            paid_on = self.paid_on

        cancelled_on: Union[None, Unset, str]
        if isinstance(self.cancelled_on, Unset):
            cancelled_on = UNSET
        elif isinstance(self.cancelled_on, datetime.datetime):
            cancelled_on = self.cancelled_on.isoformat()
        else:
            cancelled_on = self.cancelled_on

        fulfilled_on: Union[None, Unset, str]
        if isinstance(self.fulfilled_on, Unset):
            fulfilled_on = UNSET
        elif isinstance(self.fulfilled_on, datetime.datetime):
            fulfilled_on = self.fulfilled_on.isoformat()
        else:
            fulfilled_on = self.fulfilled_on

        sign_off_on: Union[None, Unset, str]
        if isinstance(self.sign_off_on, Unset):
            sign_off_on = UNSET
        elif isinstance(self.sign_off_on, datetime.datetime):
            sign_off_on = self.sign_off_on.isoformat()
        else:
            sign_off_on = self.sign_off_on

        vendor_signed_on: Union[None, Unset, str]
        if isinstance(self.vendor_signed_on, Unset):
            vendor_signed_on = UNSET
        elif isinstance(self.vendor_signed_on, datetime.datetime):
            vendor_signed_on = self.vendor_signed_on.isoformat()
        else:
            vendor_signed_on = self.vendor_signed_on

        client_notes: Union[None, Unset, str]
        if isinstance(self.client_notes, Unset):
            client_notes = UNSET
        else:
            client_notes = self.client_notes

        order_shipping_option = self.order_shipping_option

        shipment_status = self.shipment_status

        payment_status = self.payment_status

        payment_option = self.payment_option

        order_status = self.order_status

        created_by_name = self.created_by_name

        completed_by_name: Union[None, Unset, str]
        if isinstance(self.completed_by_name, Unset):
            completed_by_name = UNSET
        else:
            completed_by_name = self.completed_by_name

        shipped_by_name: Union[None, Unset, str]
        if isinstance(self.shipped_by_name, Unset):
            shipped_by_name = UNSET
        else:
            shipped_by_name = self.shipped_by_name

        accepted_by_name: Union[None, Unset, str]
        if isinstance(self.accepted_by_name, Unset):
            accepted_by_name = UNSET
        else:
            accepted_by_name = self.accepted_by_name

        approve_by_name: Union[None, Unset, str]
        if isinstance(self.approve_by_name, Unset):
            approve_by_name = UNSET
        else:
            approve_by_name = self.approve_by_name

        invoiced_by_name: Union[None, Unset, str]
        if isinstance(self.invoiced_by_name, Unset):
            invoiced_by_name = UNSET
        else:
            invoiced_by_name = self.invoiced_by_name

        delivered_by_name: Union[None, Unset, str]
        if isinstance(self.delivered_by_name, Unset):
            delivered_by_name = UNSET
        else:
            delivered_by_name = self.delivered_by_name

        paid_by_name: Union[None, Unset, str]
        if isinstance(self.paid_by_name, Unset):
            paid_by_name = UNSET
        else:
            paid_by_name = self.paid_by_name

        cancelled_by_name: Union[None, Unset, str]
        if isinstance(self.cancelled_by_name, Unset):
            cancelled_by_name = UNSET
        else:
            cancelled_by_name = self.cancelled_by_name

        sign_off_by_name: Union[None, Unset, str]
        if isinstance(self.sign_off_by_name, Unset):
            sign_off_by_name = UNSET
        else:
            sign_off_by_name = self.sign_off_by_name

        owner_name: Union[None, Unset, str]
        if isinstance(self.owner_name, Unset):
            owner_name = UNSET
        else:
            owner_name = self.owner_name

        owner_department: Union[None, Unset, str]
        if isinstance(self.owner_department, Unset):
            owner_department = UNSET
        else:
            owner_department = self.owner_department

        assignee_name: Union[None, Unset, str]
        if isinstance(self.assignee_name, Unset):
            assignee_name = UNSET
        else:
            assignee_name = self.assignee_name

        payment_due_on: Union[None, Unset, str]
        if isinstance(self.payment_due_on, Unset):
            payment_due_on = UNSET
        elif isinstance(self.payment_due_on, datetime.datetime):
            payment_due_on = self.payment_due_on.isoformat()
        else:
            payment_due_on = self.payment_due_on

        process_date_option = self.process_date_option

        desired_date: Union[None, Unset, str]
        if isinstance(self.desired_date, Unset):
            desired_date = UNSET
        elif isinstance(self.desired_date, datetime.datetime):
            desired_date = self.desired_date.isoformat()
        else:
            desired_date = self.desired_date

        deadline_date: Union[None, Unset, str]
        if isinstance(self.deadline_date, Unset):
            deadline_date = UNSET
        elif isinstance(self.deadline_date, datetime.datetime):
            deadline_date = self.deadline_date.isoformat()
        else:
            deadline_date = self.deadline_date

        vendor_sign_off_on: Union[None, Unset, str] = UNSET
        if self.vendor_sign_off_on and not isinstance(self.vendor_sign_off_on, Unset):
            vendor_sign_off_on = self.vendor_sign_off_on.isoformat()

        vendor_sign_off_by_name = self.vendor_sign_off_by_name

        service_discount = self.service_discount

        return_account = self.return_account

        business_hours_from: Union[None, Unset, str]
        if isinstance(self.business_hours_from, Unset):
            business_hours_from = UNSET
        elif isinstance(self.business_hours_from, datetime.datetime):
            business_hours_from = self.business_hours_from.isoformat()
        else:
            business_hours_from = self.business_hours_from

        business_hours_to: Union[None, Unset, str]
        if isinstance(self.business_hours_to, Unset):
            business_hours_to = UNSET
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if guid is not UNSET:
            field_dict["Guid"] = guid
        if account_number is not UNSET:
            field_dict["AccountNumber"] = account_number
        if service_order_number is not UNSET:
            field_dict["ServiceOrderNumber"] = service_order_number
        if service_order_number_text is not UNSET:
            field_dict["ServiceOrderNumberText"] = service_order_number_text
        if number_of_instruments is not UNSET:
            field_dict["NumberOfInstruments"] = number_of_instruments
        if parts_discount_total is not UNSET:
            field_dict["PartsDiscountTotal"] = parts_discount_total
        if po_number is not UNSET:
            field_dict["PoNumber"] = po_number
        if secondary_po is not UNSET:
            field_dict["SecondaryPo"] = secondary_po
        if location is not UNSET:
            field_dict["Location"] = location
        if shipped_date is not UNSET:
            field_dict["ShippedDate"] = shipped_date
        if payment_terms is not UNSET:
            field_dict["PaymentTerms"] = payment_terms
        if site_access_notes is not UNSET:
            field_dict["SiteAccessNotes"] = site_access_notes
        if grace_period is not UNSET:
            field_dict["GracePeriod"] = grace_period
        if trade_in_credit is not UNSET:
            field_dict["TradeInCredit"] = trade_in_credit
        if prepaid_credit is not UNSET:
            field_dict["PrepaidCredit"] = prepaid_credit
        if interest_rate is not UNSET:
            field_dict["InterestRate"] = interest_rate
        if service_taxation is not UNSET:
            field_dict["ServiceTaxation"] = service_taxation
        if service_order_id is not UNSET:
            field_dict["ServiceOrderId"] = service_order_id
        if federal_number is not UNSET:
            field_dict["FederalNumber"] = federal_number
        if vendor_site_id is not UNSET:
            field_dict["VendorSiteId"] = vendor_site_id
        if vendor_site is not UNSET:
            field_dict["VendorSite"] = vendor_site
        if site_name is not UNSET:
            field_dict["SiteName"] = site_name
        if site_code is not UNSET:
            field_dict["SiteCode"] = site_code
        if vendor_name is not UNSET:
            field_dict["VendorName"] = vendor_name
        if domain_name is not UNSET:
            field_dict["DomainName"] = domain_name
        if client_company_domain is not UNSET:
            field_dict["ClientCompanyDomain"] = client_company_domain
        if provider_logo is not UNSET:
            field_dict["ProviderLogo"] = provider_logo
        if client_signature is not UNSET:
            field_dict["ClientSignature"] = client_signature
        if vendor_signature is not UNSET:
            field_dict["VendorSignature"] = vendor_signature
        if qr_code is not UNSET:
            field_dict["QrCode"] = qr_code
        if bar_code is not UNSET:
            field_dict["BarCode"] = bar_code
        if bar_code_string is not UNSET:
            field_dict["BarCodeString"] = bar_code_string
        if po_balance is not UNSET:
            field_dict["PoBalance"] = po_balance
        if service_terms is not UNSET:
            field_dict["ServiceTerms"] = service_terms
        if service_total is not UNSET:
            field_dict["ServiceTotal"] = service_total
        if repairs_total is not UNSET:
            field_dict["RepairsTotal"] = repairs_total
        if parts_total is not UNSET:
            field_dict["PartsTotal"] = parts_total
        if parts_total_before_discount is not UNSET:
            field_dict["PartsTotalBeforeDiscount"] = parts_total_before_discount
        if effective_tax_rate is not UNSET:
            field_dict["EffectiveTaxRate"] = effective_tax_rate
        if tax_amount is not UNSET:
            field_dict["TaxAmount"] = tax_amount
        if shipping_fee is not UNSET:
            field_dict["ShippingFee"] = shipping_fee
        if late_fee is not UNSET:
            field_dict["LateFee"] = late_fee
        if grand_total is not UNSET:
            field_dict["GrandTotal"] = grand_total
        if amount_paid is not UNSET:
            field_dict["AmountPaid"] = amount_paid
        if balance_total is not UNSET:
            field_dict["BalanceTotal"] = balance_total
        if travel_charge is not UNSET:
            field_dict["TravelCharge"] = travel_charge
        if private_notes is not UNSET:
            field_dict["PrivateNotes"] = private_notes
        if service_notes is not UNSET:
            field_dict["ServiceNotes"] = service_notes
        if display_service_comments is not UNSET:
            field_dict["DisplayServiceComments"] = display_service_comments
        if display_part_repairs is not UNSET:
            field_dict["DisplayPartRepairs"] = display_part_repairs
        if print_separate_measurement is not UNSET:
            field_dict["PrintSeparateMeasurement"] = print_separate_measurement
        if billing_address_1 is not UNSET:
            field_dict["BillingAddress1"] = billing_address_1
        if billing_address_2 is not UNSET:
            field_dict["BillingAddress2"] = billing_address_2
        if billing_first_name is not UNSET:
            field_dict["BillingFirstName"] = billing_first_name
        if billing_last_name is not UNSET:
            field_dict["BillingLastName"] = billing_last_name
        if billing_company is not UNSET:
            field_dict["BillingCompany"] = billing_company
        if billing_country is not UNSET:
            field_dict["BillingCountry"] = billing_country
        if billing_city is not UNSET:
            field_dict["BillingCity"] = billing_city
        if billing_state is not UNSET:
            field_dict["BillingState"] = billing_state
        if billing_zip is not UNSET:
            field_dict["BillingZip"] = billing_zip
        if billing_phone_number is not UNSET:
            field_dict["BillingPhoneNumber"] = billing_phone_number
        if billing_fax_number is not UNSET:
            field_dict["BillingFaxNumber"] = billing_fax_number
        if billing_email is not UNSET:
            field_dict["BillingEmail"] = billing_email
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
        if shipping_method is not UNSET:
            field_dict["ShippingMethod"] = shipping_method
        if return_shipping_method is not UNSET:
            field_dict["ReturnShippingMethod"] = return_shipping_method
        if tracking_number is not UNSET:
            field_dict["TrackingNumber"] = tracking_number
        if provider_billing_address_1 is not UNSET:
            field_dict["ProviderBillingAddress1"] = provider_billing_address_1
        if provider_billing_address_2 is not UNSET:
            field_dict["ProviderBillingAddress2"] = provider_billing_address_2
        if provider_billing_first_name is not UNSET:
            field_dict["ProviderBillingFirstName"] = provider_billing_first_name
        if provider_billing_last_name is not UNSET:
            field_dict["ProviderBillingLastName"] = provider_billing_last_name
        if provider_billing_email is not UNSET:
            field_dict["ProviderBillingEmail"] = provider_billing_email
        if provider_billing_company is not UNSET:
            field_dict["ProviderBillingCompany"] = provider_billing_company
        if provider_billing_city is not UNSET:
            field_dict["ProviderBillingCity"] = provider_billing_city
        if provider_billing_zip is not UNSET:
            field_dict["ProviderBillingZip"] = provider_billing_zip
        if provider_billing_phone_number is not UNSET:
            field_dict["ProviderBillingPhoneNumber"] = provider_billing_phone_number
        if provider_billing_country is not UNSET:
            field_dict["ProviderBillingCountry"] = provider_billing_country
        if provider_billing_state is not UNSET:
            field_dict["ProviderBillingState"] = provider_billing_state
        if provider_billing_fax_number is not UNSET:
            field_dict["ProviderBillingFaxNumber"] = provider_billing_fax_number
        if provider_shipping_address_1 is not UNSET:
            field_dict["ProviderShippingAddress1"] = provider_shipping_address_1
        if provider_shipping_address_2 is not UNSET:
            field_dict["ProviderShippingAddress2"] = provider_shipping_address_2
        if provider_shipping_first_name is not UNSET:
            field_dict["ProviderShippingFirstName"] = provider_shipping_first_name
        if provider_shipping_last_name is not UNSET:
            field_dict["ProviderShippingLastName"] = provider_shipping_last_name
        if provider_shipping_email is not UNSET:
            field_dict["ProviderShippingEmail"] = provider_shipping_email
        if provider_shipping_company is not UNSET:
            field_dict["ProviderShippingCompany"] = provider_shipping_company
        if provider_shipping_city is not UNSET:
            field_dict["ProviderShippingCity"] = provider_shipping_city
        if provider_shipping_zip is not UNSET:
            field_dict["ProviderShippingZip"] = provider_shipping_zip
        if provider_shipping_phone_number is not UNSET:
            field_dict["ProviderShippingPhoneNumber"] = provider_shipping_phone_number
        if provider_shipping_country is not UNSET:
            field_dict["ProviderShippingCountry"] = provider_shipping_country
        if provider_shipping_state is not UNSET:
            field_dict["ProviderShippingState"] = provider_shipping_state
        if provider_shipping_fax_number is not UNSET:
            field_dict["ProviderShippingFaxNumber"] = provider_shipping_fax_number
        if culture_name is not UNSET:
            field_dict["CultureName"] = culture_name
        if vendor_company_id is not UNSET:
            field_dict["VendorCompanyId"] = vendor_company_id
        if client_vendor_id is not UNSET:
            field_dict["ClientVendorId"] = client_vendor_id
        if sign_off_date is not UNSET:
            field_dict["SignOffDate"] = sign_off_date
        if quality_control_date is not UNSET:
            field_dict["QualityControlDate"] = quality_control_date
        if client_sign_off_on is not UNSET:
            field_dict["ClientSignOffOn"] = client_sign_off_on
        if client_sign_off_by_name is not UNSET:
            field_dict["ClientSignOffByName"] = client_sign_off_by_name
        if client_signed_on is not UNSET:
            field_dict["ClientSignedOn"] = client_signed_on
        if client_sticker_notes is not UNSET:
            field_dict["ClientStickerNotes"] = client_sticker_notes
        if asset_sticker_notes is not UNSET:
            field_dict["AssetStickerNotes"] = asset_sticker_notes
        if order_sticker_notes is not UNSET:
            field_dict["OrderStickerNotes"] = order_sticker_notes
        if quality_control_name is not UNSET:
            field_dict["QualityControlName"] = quality_control_name
        if fulfilled_by_name is not UNSET:
            field_dict["FulfilledByName"] = fulfilled_by_name
        if sign_off_name is not UNSET:
            field_dict["SignOffName"] = sign_off_name
        if display_as_found is not UNSET:
            field_dict["DisplayAsFound"] = display_as_found
        if display_as_left is not UNSET:
            field_dict["DisplayAsLeft"] = display_as_left
        if created_on is not UNSET:
            field_dict["CreatedOn"] = created_on
        if invoiced_on is not UNSET:
            field_dict["InvoicedOn"] = invoiced_on
        if submitted_on is not UNSET:
            field_dict["SubmittedOn"] = submitted_on
        if shipped_on is not UNSET:
            field_dict["ShippedOn"] = shipped_on
        if completed_on is not UNSET:
            field_dict["CompletedOn"] = completed_on
        if accepted_on is not UNSET:
            field_dict["AcceptedOn"] = accepted_on
        if approved_on is not UNSET:
            field_dict["ApprovedOn"] = approved_on
        if delivered_on is not UNSET:
            field_dict["DeliveredOn"] = delivered_on
        if paid_on is not UNSET:
            field_dict["PaidOn"] = paid_on
        if cancelled_on is not UNSET:
            field_dict["CancelledOn"] = cancelled_on
        if fulfilled_on is not UNSET:
            field_dict["FulfilledOn"] = fulfilled_on
        if sign_off_on is not UNSET:
            field_dict["SignOffOn"] = sign_off_on
        if vendor_signed_on is not UNSET:
            field_dict["VendorSignedOn"] = vendor_signed_on
        if client_notes is not UNSET:
            field_dict["ClientNotes"] = client_notes
        if order_shipping_option is not UNSET:
            field_dict["OrderShippingOption"] = order_shipping_option
        if shipment_status is not UNSET:
            field_dict["ShipmentStatus"] = shipment_status
        if payment_status is not UNSET:
            field_dict["PaymentStatus"] = payment_status
        if payment_option is not UNSET:
            field_dict["PaymentOption"] = payment_option
        if order_status is not UNSET:
            field_dict["OrderStatus"] = order_status
        if created_by_name is not UNSET:
            field_dict["CreatedByName"] = created_by_name
        if completed_by_name is not UNSET:
            field_dict["CompletedByName"] = completed_by_name
        if shipped_by_name is not UNSET:
            field_dict["ShippedByName"] = shipped_by_name
        if accepted_by_name is not UNSET:
            field_dict["AcceptedByName"] = accepted_by_name
        if approve_by_name is not UNSET:
            field_dict["ApproveByName"] = approve_by_name
        if invoiced_by_name is not UNSET:
            field_dict["InvoicedByName"] = invoiced_by_name
        if delivered_by_name is not UNSET:
            field_dict["DeliveredByName"] = delivered_by_name
        if paid_by_name is not UNSET:
            field_dict["PaidByName"] = paid_by_name
        if cancelled_by_name is not UNSET:
            field_dict["CancelledByName"] = cancelled_by_name
        if sign_off_by_name is not UNSET:
            field_dict["SignOffByName"] = sign_off_by_name
        if owner_name is not UNSET:
            field_dict["OwnerName"] = owner_name
        if owner_department is not UNSET:
            field_dict["OwnerDepartment"] = owner_department
        if assignee_name is not UNSET:
            field_dict["AssigneeName"] = assignee_name
        if payment_due_on is not UNSET:
            field_dict["PaymentDueOn"] = payment_due_on
        if process_date_option is not UNSET:
            field_dict["ProcessDateOption"] = process_date_option
        if desired_date is not UNSET:
            field_dict["DesiredDate"] = desired_date
        if deadline_date is not UNSET:
            field_dict["DeadlineDate"] = deadline_date
        if vendor_sign_off_on is not UNSET:
            field_dict["VendorSignOffOn"] = vendor_sign_off_on
        if vendor_sign_off_by_name is not UNSET:
            field_dict["VendorSignOffByName"] = vendor_sign_off_by_name
        if service_discount is not UNSET:
            field_dict["ServiceDiscount"] = service_discount
        if return_account is not UNSET:
            field_dict["ReturnAccount"] = return_account
        if business_hours_from is not UNSET:
            field_dict["BusinessHoursFrom"] = business_hours_from
        if business_hours_to is not UNSET:
            field_dict["BusinessHoursTo"] = business_hours_to
        if client_company_alternative_names is not UNSET:
            field_dict["ClientCompanyAlternativeNames"] = (
                client_company_alternative_names
            )
        if client_id is not UNSET:
            field_dict["ClientId"] = client_id
        if client_class is not UNSET:
            field_dict["ClientClass"] = client_class
        if client_status is not UNSET:
            field_dict["ClientStatus"] = client_status
        if client_invoicing is not UNSET:
            field_dict["ClientInvoicing"] = client_invoicing
        if client_standing is not UNSET:
            field_dict["ClientStanding"] = client_standing
        if client_category is not UNSET:
            field_dict["ClientCategory"] = client_category
        if master_template_name is not UNSET:
            field_dict["MasterTemplateName"] = master_template_name
        if client_site_code is not UNSET:
            field_dict["ClientSiteCode"] = client_site_code
        if order_workflow_name is not UNSET:
            field_dict["OrderWorkflowName"] = order_workflow_name
        if request_workflow_name is not UNSET:
            field_dict["RequestWorkflowName"] = request_workflow_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        guid = d.pop("Guid", UNSET)

        account_number = d.pop("AccountNumber", UNSET)

        service_order_number = d.pop("ServiceOrderNumber", UNSET)

        service_order_number_text = d.pop("ServiceOrderNumberText", UNSET)

        number_of_instruments = d.pop("NumberOfInstruments", UNSET)

        parts_discount_total = d.pop("PartsDiscountTotal", UNSET)

        po_number = d.pop("PoNumber", UNSET)

        secondary_po = d.pop("SecondaryPo", UNSET)

        location = d.pop("Location", UNSET)

        def _parse_shipped_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shipped_date_type_0 = isoparse(data)

                return shipped_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        shipped_date = _parse_shipped_date(d.pop("ShippedDate", UNSET))

        payment_terms = d.pop("PaymentTerms", UNSET)

        site_access_notes = d.pop("SiteAccessNotes", UNSET)

        grace_period = d.pop("GracePeriod", UNSET)

        trade_in_credit = d.pop("TradeInCredit", UNSET)

        prepaid_credit = d.pop("PrepaidCredit", UNSET)

        interest_rate = d.pop("InterestRate", UNSET)

        service_taxation = d.pop("ServiceTaxation", UNSET)

        service_order_id = d.pop("ServiceOrderId", UNSET)

        federal_number = d.pop("FederalNumber", UNSET)

        vendor_site_id = d.pop("VendorSiteId", UNSET)

        vendor_site = d.pop("VendorSite", UNSET)

        site_name = d.pop("SiteName", UNSET)

        site_code = d.pop("SiteCode", UNSET)

        vendor_name = d.pop("VendorName", UNSET)

        domain_name = d.pop("DomainName", UNSET)

        client_company_domain = d.pop("ClientCompanyDomain", UNSET)

        provider_logo = d.pop("ProviderLogo", UNSET)

        client_signature = d.pop("ClientSignature", UNSET)

        vendor_signature = d.pop("VendorSignature", UNSET)

        qr_code = d.pop("QrCode", UNSET)

        bar_code = d.pop("BarCode", UNSET)

        bar_code_string = d.pop("BarCodeString", UNSET)

        po_balance = d.pop("PoBalance", UNSET)

        service_terms = d.pop("ServiceTerms", UNSET)

        service_total = d.pop("ServiceTotal", UNSET)

        repairs_total = d.pop("RepairsTotal", UNSET)

        parts_total = d.pop("PartsTotal", UNSET)

        parts_total_before_discount = d.pop("PartsTotalBeforeDiscount", UNSET)

        effective_tax_rate = d.pop("EffectiveTaxRate", UNSET)

        tax_amount = d.pop("TaxAmount", UNSET)

        shipping_fee = d.pop("ShippingFee", UNSET)

        late_fee = d.pop("LateFee", UNSET)

        grand_total = d.pop("GrandTotal", UNSET)

        amount_paid = d.pop("AmountPaid", UNSET)

        balance_total = d.pop("BalanceTotal", UNSET)

        travel_charge = d.pop("TravelCharge", UNSET)

        private_notes = d.pop("PrivateNotes", UNSET)

        service_notes = d.pop("ServiceNotes", UNSET)

        display_service_comments = d.pop("DisplayServiceComments", UNSET)

        display_part_repairs = d.pop("DisplayPartRepairs", UNSET)

        print_separate_measurement = d.pop("PrintSeparateMeasurement", UNSET)

        billing_address_1 = d.pop("BillingAddress1", UNSET)

        billing_address_2 = d.pop("BillingAddress2", UNSET)

        billing_first_name = d.pop("BillingFirstName", UNSET)

        billing_last_name = d.pop("BillingLastName", UNSET)

        billing_company = d.pop("BillingCompany", UNSET)

        billing_country = d.pop("BillingCountry", UNSET)

        billing_city = d.pop("BillingCity", UNSET)

        billing_state = d.pop("BillingState", UNSET)

        billing_zip = d.pop("BillingZip", UNSET)

        billing_phone_number = d.pop("BillingPhoneNumber", UNSET)

        billing_fax_number = d.pop("BillingFaxNumber", UNSET)

        billing_email = d.pop("BillingEmail", UNSET)

        shipping_address_1 = d.pop("ShippingAddress1", UNSET)

        shipping_address_2 = d.pop("ShippingAddress2", UNSET)

        shipping_first_name = d.pop("ShippingFirstName", UNSET)

        shipping_last_name = d.pop("ShippingLastName", UNSET)

        shipping_email = d.pop("ShippingEmail", UNSET)

        shipping_company = d.pop("ShippingCompany", UNSET)

        shipping_city = d.pop("ShippingCity", UNSET)

        shipping_zip = d.pop("ShippingZip", UNSET)

        shipping_phone_number = d.pop("ShippingPhoneNumber", UNSET)

        shipping_fax_number = d.pop("ShippingFaxNumber", UNSET)

        shipping_country = d.pop("ShippingCountry", UNSET)

        shipping_state = d.pop("ShippingState", UNSET)

        shipping_method = d.pop("ShippingMethod", UNSET)

        return_shipping_method = d.pop("ReturnShippingMethod", UNSET)

        tracking_number = d.pop("TrackingNumber", UNSET)

        provider_billing_address_1 = d.pop("ProviderBillingAddress1", UNSET)

        provider_billing_address_2 = d.pop("ProviderBillingAddress2", UNSET)

        provider_billing_first_name = d.pop("ProviderBillingFirstName", UNSET)

        provider_billing_last_name = d.pop("ProviderBillingLastName", UNSET)

        provider_billing_email = d.pop("ProviderBillingEmail", UNSET)

        provider_billing_company = d.pop("ProviderBillingCompany", UNSET)

        provider_billing_city = d.pop("ProviderBillingCity", UNSET)

        provider_billing_zip = d.pop("ProviderBillingZip", UNSET)

        provider_billing_phone_number = d.pop("ProviderBillingPhoneNumber", UNSET)

        provider_billing_country = d.pop("ProviderBillingCountry", UNSET)

        provider_billing_state = d.pop("ProviderBillingState", UNSET)

        provider_billing_fax_number = d.pop("ProviderBillingFaxNumber", UNSET)

        provider_shipping_address_1 = d.pop("ProviderShippingAddress1", UNSET)

        provider_shipping_address_2 = d.pop("ProviderShippingAddress2", UNSET)

        provider_shipping_first_name = d.pop("ProviderShippingFirstName", UNSET)

        provider_shipping_last_name = d.pop("ProviderShippingLastName", UNSET)

        provider_shipping_email = d.pop("ProviderShippingEmail", UNSET)

        provider_shipping_company = d.pop("ProviderShippingCompany", UNSET)

        provider_shipping_city = d.pop("ProviderShippingCity", UNSET)

        provider_shipping_zip = d.pop("ProviderShippingZip", UNSET)

        provider_shipping_phone_number = d.pop("ProviderShippingPhoneNumber", UNSET)

        provider_shipping_country = d.pop("ProviderShippingCountry", UNSET)

        provider_shipping_state = d.pop("ProviderShippingState", UNSET)

        provider_shipping_fax_number = d.pop("ProviderShippingFaxNumber", UNSET)

        culture_name = d.pop("CultureName", UNSET)

        vendor_company_id = d.pop("VendorCompanyId", UNSET)

        client_vendor_id = d.pop("ClientVendorId", UNSET)

        def _parse_sign_off_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sign_off_date_type_0 = isoparse(data)

                return sign_off_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        sign_off_date = _parse_sign_off_date(d.pop("SignOffDate", UNSET))

        _quality_control_date = d.pop("QualityControlDate", UNSET)
        quality_control_date: Union[None, Unset, datetime.datetime]
        if isinstance(_quality_control_date, Unset):
            quality_control_date = UNSET
        elif _quality_control_date is None:
            quality_control_date = None
        else:
            quality_control_date = isoparse(_quality_control_date)

        def _parse_client_sign_off_on(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                client_sign_off_on_type_0 = isoparse(data)

                return client_sign_off_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        client_sign_off_on = _parse_client_sign_off_on(d.pop("ClientSignOffOn", UNSET))

        client_sign_off_by_name = d.pop("ClientSignOffByName", UNSET)

        def _parse_client_signed_on(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                client_signed_on_type_0 = isoparse(data)

                return client_signed_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        client_signed_on = _parse_client_signed_on(d.pop("ClientSignedOn", UNSET))

        client_sticker_notes = d.pop("ClientStickerNotes", UNSET)

        asset_sticker_notes = d.pop("AssetStickerNotes", UNSET)

        order_sticker_notes = d.pop("OrderStickerNotes", UNSET)

        quality_control_name = d.pop("QualityControlName", UNSET)

        fulfilled_by_name = d.pop("FulfilledByName", UNSET)

        sign_off_name = d.pop("SignOffName", UNSET)

        display_as_found = d.pop("DisplayAsFound", UNSET)

        display_as_left = d.pop("DisplayAsLeft", UNSET)

        _created_on = d.pop("CreatedOn", UNSET)
        created_on: Union[None, Unset, datetime.datetime]
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = isoparse(_created_on)

        def _parse_invoiced_on(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                invoiced_on_type_0 = isoparse(data)

                return invoiced_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        invoiced_on = _parse_invoiced_on(d.pop("InvoicedOn", UNSET))

        def _parse_submitted_on(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                submitted_on_type_0 = isoparse(data)

                return submitted_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        submitted_on = _parse_submitted_on(d.pop("SubmittedOn", UNSET))

        def _parse_shipped_on(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shipped_on_type_0 = isoparse(data)

                return shipped_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        shipped_on = _parse_shipped_on(d.pop("ShippedOn", UNSET))

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

        def _parse_accepted_on(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                accepted_on_type_0 = isoparse(data)

                return accepted_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        accepted_on = _parse_accepted_on(d.pop("AcceptedOn", UNSET))

        def _parse_approved_on(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_on_type_0 = isoparse(data)

                return approved_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        approved_on = _parse_approved_on(d.pop("ApprovedOn", UNSET))

        def _parse_delivered_on(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delivered_on_type_0 = isoparse(data)

                return delivered_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        delivered_on = _parse_delivered_on(d.pop("DeliveredOn", UNSET))

        def _parse_paid_on(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                paid_on_type_0 = isoparse(data)

                return paid_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        paid_on = _parse_paid_on(d.pop("PaidOn", UNSET))

        def _parse_cancelled_on(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cancelled_on_type_0 = isoparse(data)

                return cancelled_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        cancelled_on = _parse_cancelled_on(d.pop("CancelledOn", UNSET))

        def _parse_fulfilled_on(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fulfilled_on_type_0 = isoparse(data)

                return fulfilled_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        fulfilled_on = _parse_fulfilled_on(d.pop("FulfilledOn", UNSET))

        def _parse_sign_off_on(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sign_off_on_type_0 = isoparse(data)

                return sign_off_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        sign_off_on = _parse_sign_off_on(d.pop("SignOffOn", UNSET))

        def _parse_vendor_signed_on(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                vendor_signed_on_type_0 = isoparse(data)

                return vendor_signed_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        vendor_signed_on = _parse_vendor_signed_on(d.pop("VendorSignedOn", UNSET))

        def _parse_client_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        client_notes = _parse_client_notes(d.pop("ClientNotes", UNSET))

        order_shipping_option = d.pop("OrderShippingOption", UNSET)

        shipment_status = d.pop("ShipmentStatus", UNSET)

        payment_status = d.pop("PaymentStatus", UNSET)

        payment_option = d.pop("PaymentOption", UNSET)

        order_status = d.pop("OrderStatus", UNSET)

        created_by_name = d.pop("CreatedByName", UNSET)

        def _parse_completed_by_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        completed_by_name = _parse_completed_by_name(d.pop("CompletedByName", UNSET))

        def _parse_shipped_by_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shipped_by_name = _parse_shipped_by_name(d.pop("ShippedByName", UNSET))

        def _parse_accepted_by_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        accepted_by_name = _parse_accepted_by_name(d.pop("AcceptedByName", UNSET))

        def _parse_approve_by_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        approve_by_name = _parse_approve_by_name(d.pop("ApproveByName", UNSET))

        def _parse_invoiced_by_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        invoiced_by_name = _parse_invoiced_by_name(d.pop("InvoicedByName", UNSET))

        def _parse_delivered_by_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        delivered_by_name = _parse_delivered_by_name(d.pop("DeliveredByName", UNSET))

        def _parse_paid_by_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        paid_by_name = _parse_paid_by_name(d.pop("PaidByName", UNSET))

        def _parse_cancelled_by_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cancelled_by_name = _parse_cancelled_by_name(d.pop("CancelledByName", UNSET))

        def _parse_sign_off_by_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sign_off_by_name = _parse_sign_off_by_name(d.pop("SignOffByName", UNSET))

        def _parse_owner_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        owner_name = _parse_owner_name(d.pop("OwnerName", UNSET))

        def _parse_owner_department(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        owner_department = _parse_owner_department(d.pop("OwnerDepartment", UNSET))

        def _parse_assignee_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        assignee_name = _parse_assignee_name(d.pop("AssigneeName", UNSET))

        def _parse_payment_due_on(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                payment_due_on_type_0 = isoparse(data)

                return payment_due_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        payment_due_on = _parse_payment_due_on(d.pop("PaymentDueOn", UNSET))

        process_date_option = d.pop("ProcessDateOption", UNSET)

        def _parse_desired_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                desired_date_type_0 = isoparse(data)

                return desired_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        desired_date = _parse_desired_date(d.pop("DesiredDate", UNSET))

        def _parse_deadline_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deadline_date_type_0 = isoparse(data)

                return deadline_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        deadline_date = _parse_deadline_date(d.pop("DeadlineDate", UNSET))

        _vendor_sign_off_on = d.pop("VendorSignOffOn", UNSET)
        vendor_sign_off_on: Union[None, Unset, datetime.datetime]
        if isinstance(_vendor_sign_off_on, Unset):
            vendor_sign_off_on = UNSET
        else:
            vendor_sign_off_on = isoparse(_vendor_sign_off_on)

        vendor_sign_off_by_name = d.pop("VendorSignOffByName", UNSET)

        service_discount = d.pop("ServiceDiscount", UNSET)

        return_account = d.pop("ReturnAccount", UNSET)

        def _parse_business_hours_from(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                business_hours_from_type_0 = isoparse(data)

                return business_hours_from_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        business_hours_from = _parse_business_hours_from(
            d.pop("BusinessHoursFrom", UNSET)
        )

        def _parse_business_hours_to(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                business_hours_to_type_0 = isoparse(data)

                return business_hours_to_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        business_hours_to = _parse_business_hours_to(d.pop("BusinessHoursTo", UNSET))

        client_company_alternative_names = d.pop("ClientCompanyAlternativeNames", UNSET)

        client_id = d.pop("ClientId", UNSET)

        client_class = d.pop("ClientClass", UNSET)

        client_status = d.pop("ClientStatus", UNSET)

        client_invoicing = d.pop("ClientInvoicing", UNSET)

        client_standing = d.pop("ClientStanding", UNSET)

        client_category = d.pop("ClientCategory", UNSET)

        master_template_name = d.pop("MasterTemplateName", UNSET)

        client_site_code = d.pop("ClientSiteCode", UNSET)

        order_workflow_name = d.pop("OrderWorkflowName", UNSET)

        request_workflow_name = d.pop("RequestWorkflowName", UNSET)

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

        qualer_api_models_report_datasets_to_service_order_response.additional_properties = (
            d
        )
        return qualer_api_models_report_datasets_to_service_order_response

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
