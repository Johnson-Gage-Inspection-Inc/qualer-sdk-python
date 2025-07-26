import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualer_api_models_service_orders_to_client_order_response_model_billing_address_type_0 import (
        QualerApiModelsServiceOrdersToClientOrderResponseModelBillingAddressType0,
    )
    from ..models.qualer_api_models_service_orders_to_client_order_response_model_shipping_address_type_0 import (
        QualerApiModelsServiceOrdersToClientOrderResponseModelShippingAddressType0,
    )


T = TypeVar("T", bound="QualerApiModelsServiceOrdersToClientOrderResponseModel")


@_attrs_define
class QualerApiModelsServiceOrdersToClientOrderResponseModel:
    """
    Attributes:
        service_order_id (Union[Unset, int]):
        parent_order_id (Union[Unset, int]):
        client_legacy_id (Union[Unset, str]):
        owner_name (Union[Unset, str]):
        submited_by_name (Union[Unset, str]):
        sign_off_by_name (Union[Unset, str]):
        vendor_sign_off_by_name (Union[Unset, str]):
        approved_by_name (Union[Unset, str]):
        accepted_by_name (Union[Unset, str]):
        ready_for_quality_control_by_name (Union[Unset, str]):
        quality_control_by_name (Union[Unset, str]):
        created_by_name (Union[Unset, str]):
        completed_by_name (Union[Unset, str]):
        shipped_by_name (Union[Unset, str]):
        delivered_by_name (Union[Unset, str]):
        invoiced_by_name (Union[Unset, str]):
        paid_by_name (Union[Unset, str]):
        cancelled_by_name (Union[Unset, str]):
        closed_by_name (Union[Unset, str]):
        client_company_id (Union[Unset, int]):
        client_company_name (Union[Unset, str]):
        client_domain_name (Union[Unset, str]):
        client_alternative_names (Union[Unset, str]):
        service_comments (Union[Unset, str]):
        service_private_comments (Union[Unset, str]):
        created_on (Union[None, Unset, datetime.datetime]):
        approved_on (Union[None, Unset, datetime.datetime]):
        sign_off_on (Union[None, Unset, datetime.datetime]):
        vendor_sign_off_on (Union[None, Unset, datetime.datetime]):
        completed_on (Union[None, Unset, datetime.datetime]):
        submited_on (Union[None, Unset, datetime.datetime]):
        shipped_on (Union[None, Unset, datetime.datetime]):
        accepted_on (Union[None, Unset, datetime.datetime]):
        ready_for_quality_control_on (Union[None, Unset, datetime.datetime]):
        quality_control_on (Union[None, Unset, datetime.datetime]):
        delivered_on (Union[None, Unset, datetime.datetime]):
        invoiced_on (Union[None, Unset, datetime.datetime]):
        last_invoiced_on (Union[None, Unset, datetime.datetime]):
        payment_due_on (Union[None, Unset, datetime.datetime]):
        paid_on (Union[None, Unset, datetime.datetime]):
        late_fee_on (Union[None, Unset, datetime.datetime]):
        cancelled_on (Union[None, Unset, datetime.datetime]):
        closed_on (Union[None, Unset, datetime.datetime]):
        last_updated_on (Union[None, Unset, datetime.datetime]):
        last_updated_by (Union[Unset, str]):
        submited_by_id (Union[Unset, int]):
        sign_off_by_id (Union[Unset, int]):
        vendor_sign_off_by_id (Union[Unset, int]):
        approved_by_id (Union[Unset, int]):
        late_fee_by_id (Union[Unset, int]):
        accepted_by_id (Union[Unset, int]):
        ready_for_quality_control_by_id (Union[Unset, int]):
        quality_control_by_id (Union[Unset, int]):
        created_by_id (Union[Unset, int]):
        completed_by_id (Union[Unset, int]):
        shipped_by_id (Union[Unset, int]):
        delivered_by_id (Union[Unset, int]):
        invoiced_by_id (Union[Unset, int]):
        paid_by_id (Union[Unset, int]):
        cancelled_by_id (Union[Unset, int]):
        closed_by_id (Union[Unset, int]):
        po_number (Union[Unset, str]):
        secondary_po (Union[Unset, str]):
        service_total (Union[Unset, float]):
        repairs_total (Union[Unset, float]):
        parts_total (Union[Unset, float]):
        parts_total_before_discount (Union[Unset, float]):
        parts_discount_total (Union[Unset, float]):
        effective_tax_rate (Union[Unset, float]):
        tax_amount (Union[Unset, float]):
        shipping_fee (Union[Unset, float]):
        travel_charge (Union[Unset, float]):
        late_fee (Union[Unset, float]):
        is_tax_exempt (Union[Unset, bool]):
        service_discount (Union[Unset, float]):
        trade_in_credit (Union[Unset, float]):
        prepaid_credit (Union[Unset, float]):
        grand_total (Union[Unset, float]):
        paid_amount (Union[Unset, float]):
        remaining_balance (Union[Unset, float]):
        service_discount_details (Union[Unset, str]):
        trade_in_credit_details (Union[Unset, str]):
        prepaid_credit_details (Union[Unset, str]):
        payment_notes (Union[Unset, str]):
        service_order_number (Union[Unset, int]):
        legacy_order_number (Union[Unset, str]):
        custom_order_number (Union[Unset, str]):
        payment_status (Union[Unset, str]):
        payment_option (Union[Unset, str]):
        shipment_status (Union[Unset, str]):
        order_status (Union[Unset, str]):
        owner_id (Union[Unset, int]):
        owner_department (Union[Unset, str]):
        client_site (Union[Unset, str]):
        client_site_code (Union[Unset, str]):
        vendor_site (Union[Unset, str]):
        internal (Union[Unset, bool]):
        guid (Union[Unset, UUID]):  Example: 00000000-0000-0000-0000-000000000000.
        business_from_time (Union[None, Unset, datetime.datetime]):
        business_to_time (Union[None, Unset, datetime.datetime]):
        site_access_notes (Union[Unset, str]):
        desired_date (Union[None, Unset, datetime.datetime]):
        deadline_date (Union[None, Unset, datetime.datetime]):
        request_from_date (Union[None, Unset, datetime.datetime]):
        request_from_time (Union[None, Unset, datetime.datetime]):
        request_to_date (Union[None, Unset, datetime.datetime]):
        request_to_time (Union[None, Unset, datetime.datetime]):
        order_notes (Union[Unset, str]):
        billing_address (Union['QualerApiModelsServiceOrdersToClientOrderResponseModelBillingAddressType0', None,
            Unset]):
        shipping_address (Union['QualerApiModelsServiceOrdersToClientOrderResponseModelShippingAddressType0', None,
            Unset]):
    """

    service_order_id: Union[Unset, int] = UNSET
    parent_order_id: Union[Unset, int] = UNSET
    client_legacy_id: Union[Unset, str] = UNSET
    owner_name: Union[Unset, str] = UNSET
    submited_by_name: Union[Unset, str] = UNSET
    sign_off_by_name: Union[Unset, str] = UNSET
    vendor_sign_off_by_name: Union[Unset, str] = UNSET
    approved_by_name: Union[Unset, str] = UNSET
    accepted_by_name: Union[Unset, str] = UNSET
    ready_for_quality_control_by_name: Union[Unset, str] = UNSET
    quality_control_by_name: Union[Unset, str] = UNSET
    created_by_name: Union[Unset, str] = UNSET
    completed_by_name: Union[Unset, str] = UNSET
    shipped_by_name: Union[Unset, str] = UNSET
    delivered_by_name: Union[Unset, str] = UNSET
    invoiced_by_name: Union[Unset, str] = UNSET
    paid_by_name: Union[Unset, str] = UNSET
    cancelled_by_name: Union[Unset, str] = UNSET
    closed_by_name: Union[Unset, str] = UNSET
    client_company_id: Union[Unset, int] = UNSET
    client_company_name: Union[Unset, str] = UNSET
    client_domain_name: Union[Unset, str] = UNSET
    client_alternative_names: Union[Unset, str] = UNSET
    service_comments: Union[Unset, str] = UNSET
    service_private_comments: Union[Unset, str] = UNSET
    created_on: Union[None, Unset, datetime.datetime] = UNSET
    approved_on: Union[None, Unset, datetime.datetime] = UNSET
    sign_off_on: Union[None, Unset, datetime.datetime] = UNSET
    vendor_sign_off_on: Union[None, Unset, datetime.datetime] = UNSET
    completed_on: Union[None, Unset, datetime.datetime] = UNSET
    submited_on: Union[None, Unset, datetime.datetime] = UNSET
    shipped_on: Union[None, Unset, datetime.datetime] = UNSET
    accepted_on: Union[None, Unset, datetime.datetime] = UNSET
    ready_for_quality_control_on: Union[None, Unset, datetime.datetime] = UNSET
    quality_control_on: Union[None, Unset, datetime.datetime] = UNSET
    delivered_on: Union[None, Unset, datetime.datetime] = UNSET
    invoiced_on: Union[None, Unset, datetime.datetime] = UNSET
    last_invoiced_on: Union[None, Unset, datetime.datetime] = UNSET
    payment_due_on: Union[None, Unset, datetime.datetime] = UNSET
    paid_on: Union[None, Unset, datetime.datetime] = UNSET
    late_fee_on: Union[None, Unset, datetime.datetime] = UNSET
    cancelled_on: Union[None, Unset, datetime.datetime] = UNSET
    closed_on: Union[None, Unset, datetime.datetime] = UNSET
    last_updated_on: Union[None, Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, str] = UNSET
    submited_by_id: Union[Unset, int] = UNSET
    sign_off_by_id: Union[Unset, int] = UNSET
    vendor_sign_off_by_id: Union[Unset, int] = UNSET
    approved_by_id: Union[Unset, int] = UNSET
    late_fee_by_id: Union[Unset, int] = UNSET
    accepted_by_id: Union[Unset, int] = UNSET
    ready_for_quality_control_by_id: Union[Unset, int] = UNSET
    quality_control_by_id: Union[Unset, int] = UNSET
    created_by_id: Union[Unset, int] = UNSET
    completed_by_id: Union[Unset, int] = UNSET
    shipped_by_id: Union[Unset, int] = UNSET
    delivered_by_id: Union[Unset, int] = UNSET
    invoiced_by_id: Union[Unset, int] = UNSET
    paid_by_id: Union[Unset, int] = UNSET
    cancelled_by_id: Union[Unset, int] = UNSET
    closed_by_id: Union[Unset, int] = UNSET
    po_number: Union[Unset, str] = UNSET
    secondary_po: Union[Unset, str] = UNSET
    service_total: Union[Unset, float] = UNSET
    repairs_total: Union[Unset, float] = UNSET
    parts_total: Union[Unset, float] = UNSET
    parts_total_before_discount: Union[Unset, float] = UNSET
    parts_discount_total: Union[Unset, float] = UNSET
    effective_tax_rate: Union[Unset, float] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    shipping_fee: Union[Unset, float] = UNSET
    travel_charge: Union[Unset, float] = UNSET
    late_fee: Union[Unset, float] = UNSET
    is_tax_exempt: Union[Unset, bool] = UNSET
    service_discount: Union[Unset, float] = UNSET
    trade_in_credit: Union[Unset, float] = UNSET
    prepaid_credit: Union[Unset, float] = UNSET
    grand_total: Union[Unset, float] = UNSET
    paid_amount: Union[Unset, float] = UNSET
    remaining_balance: Union[Unset, float] = UNSET
    service_discount_details: Union[Unset, str] = UNSET
    trade_in_credit_details: Union[Unset, str] = UNSET
    prepaid_credit_details: Union[Unset, str] = UNSET
    payment_notes: Union[Unset, str] = UNSET
    service_order_number: Union[Unset, int] = UNSET
    legacy_order_number: Union[Unset, str] = UNSET
    custom_order_number: Union[Unset, str] = UNSET
    payment_status: Union[Unset, str] = UNSET
    payment_option: Union[Unset, str] = UNSET
    shipment_status: Union[Unset, str] = UNSET
    order_status: Union[Unset, str] = UNSET
    owner_id: Union[Unset, int] = UNSET
    owner_department: Union[Unset, str] = UNSET
    client_site: Union[Unset, str] = UNSET
    client_site_code: Union[Unset, str] = UNSET
    vendor_site: Union[Unset, str] = UNSET
    internal: Union[Unset, bool] = UNSET
    guid: Union[Unset, UUID] = UNSET
    business_from_time: Union[None, Unset, datetime.datetime] = UNSET
    business_to_time: Union[None, Unset, datetime.datetime] = UNSET
    site_access_notes: Union[Unset, str] = UNSET
    desired_date: Union[None, Unset, datetime.datetime] = UNSET
    deadline_date: Union[None, Unset, datetime.datetime] = UNSET
    request_from_date: Union[None, Unset, datetime.datetime] = UNSET
    request_from_time: Union[None, Unset, datetime.datetime] = UNSET
    request_to_date: Union[None, Unset, datetime.datetime] = UNSET
    request_to_time: Union[None, Unset, datetime.datetime] = UNSET
    order_notes: Union[Unset, str] = UNSET
    billing_address: Union[
        "QualerApiModelsServiceOrdersToClientOrderResponseModelBillingAddressType0",
        None,
        Unset,
    ] = UNSET
    shipping_address: Union[
        "QualerApiModelsServiceOrdersToClientOrderResponseModelShippingAddressType0",
        None,
        Unset,
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.qualer_api_models_service_orders_to_client_order_response_model_billing_address_type_0 import (
            QualerApiModelsServiceOrdersToClientOrderResponseModelBillingAddressType0,
        )
        from ..models.qualer_api_models_service_orders_to_client_order_response_model_shipping_address_type_0 import (
            QualerApiModelsServiceOrdersToClientOrderResponseModelShippingAddressType0,
        )

        service_order_id = self.service_order_id

        parent_order_id = self.parent_order_id

        client_legacy_id = self.client_legacy_id

        owner_name = self.owner_name

        submited_by_name = self.submited_by_name

        sign_off_by_name = self.sign_off_by_name

        vendor_sign_off_by_name = self.vendor_sign_off_by_name

        approved_by_name = self.approved_by_name

        accepted_by_name = self.accepted_by_name

        ready_for_quality_control_by_name = self.ready_for_quality_control_by_name

        quality_control_by_name = self.quality_control_by_name

        created_by_name = self.created_by_name

        completed_by_name = self.completed_by_name

        shipped_by_name = self.shipped_by_name

        delivered_by_name = self.delivered_by_name

        invoiced_by_name = self.invoiced_by_name

        paid_by_name = self.paid_by_name

        cancelled_by_name = self.cancelled_by_name

        closed_by_name = self.closed_by_name

        client_company_id = self.client_company_id

        client_company_name = self.client_company_name

        client_domain_name = self.client_domain_name

        client_alternative_names = self.client_alternative_names

        service_comments = self.service_comments

        service_private_comments = self.service_private_comments

        created_on: Union[None, Unset, str]
        if isinstance(self.created_on, Unset):
            created_on = UNSET
        elif isinstance(self.created_on, datetime.datetime):
            created_on = self.created_on.isoformat()
        else:
            created_on = self.created_on

        approved_on: Union[None, Unset, str]
        if isinstance(self.approved_on, Unset):
            approved_on = UNSET
        elif isinstance(self.approved_on, datetime.datetime):
            approved_on = self.approved_on.isoformat()
        else:
            approved_on = self.approved_on

        sign_off_on: Union[None, Unset, str]
        if isinstance(self.sign_off_on, Unset):
            sign_off_on = UNSET
        elif isinstance(self.sign_off_on, datetime.datetime):
            sign_off_on = self.sign_off_on.isoformat()
        else:
            sign_off_on = self.sign_off_on

        vendor_sign_off_on: Union[None, Unset, str]
        if isinstance(self.vendor_sign_off_on, Unset):
            vendor_sign_off_on = UNSET
        elif isinstance(self.vendor_sign_off_on, datetime.datetime):
            vendor_sign_off_on = self.vendor_sign_off_on.isoformat()
        else:
            vendor_sign_off_on = self.vendor_sign_off_on

        completed_on: Union[None, Unset, str]
        if isinstance(self.completed_on, Unset):
            completed_on = UNSET
        elif isinstance(self.completed_on, datetime.datetime):
            completed_on = self.completed_on.isoformat()
        else:
            completed_on = self.completed_on

        submited_on: Union[None, Unset, str]
        if isinstance(self.submited_on, Unset):
            submited_on = UNSET
        elif isinstance(self.submited_on, datetime.datetime):
            submited_on = self.submited_on.isoformat()
        else:
            submited_on = self.submited_on

        shipped_on: Union[None, Unset, str]
        if isinstance(self.shipped_on, Unset):
            shipped_on = UNSET
        elif isinstance(self.shipped_on, datetime.datetime):
            shipped_on = self.shipped_on.isoformat()
        else:
            shipped_on = self.shipped_on

        accepted_on: Union[None, Unset, str]
        if isinstance(self.accepted_on, Unset):
            accepted_on = UNSET
        elif isinstance(self.accepted_on, datetime.datetime):
            accepted_on = self.accepted_on.isoformat()
        else:
            accepted_on = self.accepted_on

        ready_for_quality_control_on: Union[None, Unset, str]
        if isinstance(self.ready_for_quality_control_on, Unset):
            ready_for_quality_control_on = UNSET
        elif isinstance(self.ready_for_quality_control_on, datetime.datetime):
            ready_for_quality_control_on = self.ready_for_quality_control_on.isoformat()
        else:
            ready_for_quality_control_on = self.ready_for_quality_control_on

        quality_control_on: Union[None, Unset, str]
        if isinstance(self.quality_control_on, Unset):
            quality_control_on = UNSET
        elif isinstance(self.quality_control_on, datetime.datetime):
            quality_control_on = self.quality_control_on.isoformat()
        else:
            quality_control_on = self.quality_control_on

        delivered_on: Union[None, Unset, str]
        if isinstance(self.delivered_on, Unset):
            delivered_on = UNSET
        elif isinstance(self.delivered_on, datetime.datetime):
            delivered_on = self.delivered_on.isoformat()
        else:
            delivered_on = self.delivered_on

        invoiced_on: Union[None, Unset, str]
        if isinstance(self.invoiced_on, Unset):
            invoiced_on = UNSET
        elif isinstance(self.invoiced_on, datetime.datetime):
            invoiced_on = self.invoiced_on.isoformat()
        else:
            invoiced_on = self.invoiced_on

        last_invoiced_on: Union[None, Unset, str]
        if isinstance(self.last_invoiced_on, Unset):
            last_invoiced_on = UNSET
        elif isinstance(self.last_invoiced_on, datetime.datetime):
            last_invoiced_on = self.last_invoiced_on.isoformat()
        else:
            last_invoiced_on = self.last_invoiced_on

        payment_due_on: Union[None, Unset, str]
        if isinstance(self.payment_due_on, Unset):
            payment_due_on = UNSET
        elif isinstance(self.payment_due_on, datetime.datetime):
            payment_due_on = self.payment_due_on.isoformat()
        else:
            payment_due_on = self.payment_due_on

        paid_on: Union[None, Unset, str]
        if isinstance(self.paid_on, Unset):
            paid_on = UNSET
        elif isinstance(self.paid_on, datetime.datetime):
            paid_on = self.paid_on.isoformat()
        else:
            paid_on = self.paid_on

        late_fee_on: Union[None, Unset, str]
        if isinstance(self.late_fee_on, Unset):
            late_fee_on = UNSET
        elif isinstance(self.late_fee_on, datetime.datetime):
            late_fee_on = self.late_fee_on.isoformat()
        else:
            late_fee_on = self.late_fee_on

        cancelled_on: Union[None, Unset, str]
        if isinstance(self.cancelled_on, Unset):
            cancelled_on = UNSET
        elif isinstance(self.cancelled_on, datetime.datetime):
            cancelled_on = self.cancelled_on.isoformat()
        else:
            cancelled_on = self.cancelled_on

        closed_on: Union[None, Unset, str]
        if isinstance(self.closed_on, Unset):
            closed_on = UNSET
        elif isinstance(self.closed_on, datetime.datetime):
            closed_on = self.closed_on.isoformat()
        else:
            closed_on = self.closed_on

        last_updated_on: Union[None, Unset, str]
        if isinstance(self.last_updated_on, Unset):
            last_updated_on = UNSET
        elif isinstance(self.last_updated_on, datetime.datetime):
            last_updated_on = self.last_updated_on.isoformat()
        else:
            last_updated_on = self.last_updated_on

        last_updated_by = self.last_updated_by

        submited_by_id = self.submited_by_id

        sign_off_by_id = self.sign_off_by_id

        vendor_sign_off_by_id = self.vendor_sign_off_by_id

        approved_by_id = self.approved_by_id

        late_fee_by_id = self.late_fee_by_id

        accepted_by_id = self.accepted_by_id

        ready_for_quality_control_by_id = self.ready_for_quality_control_by_id

        quality_control_by_id = self.quality_control_by_id

        created_by_id = self.created_by_id

        completed_by_id = self.completed_by_id

        shipped_by_id = self.shipped_by_id

        delivered_by_id = self.delivered_by_id

        invoiced_by_id = self.invoiced_by_id

        paid_by_id = self.paid_by_id

        cancelled_by_id = self.cancelled_by_id

        closed_by_id = self.closed_by_id

        po_number = self.po_number

        secondary_po = self.secondary_po

        service_total = self.service_total

        repairs_total = self.repairs_total

        parts_total = self.parts_total

        parts_total_before_discount = self.parts_total_before_discount

        parts_discount_total = self.parts_discount_total

        effective_tax_rate = self.effective_tax_rate

        tax_amount = self.tax_amount

        shipping_fee = self.shipping_fee

        travel_charge = self.travel_charge

        late_fee = self.late_fee

        is_tax_exempt = self.is_tax_exempt

        service_discount = self.service_discount

        trade_in_credit = self.trade_in_credit

        prepaid_credit = self.prepaid_credit

        grand_total = self.grand_total

        paid_amount = self.paid_amount

        remaining_balance = self.remaining_balance

        service_discount_details = self.service_discount_details

        trade_in_credit_details = self.trade_in_credit_details

        prepaid_credit_details = self.prepaid_credit_details

        payment_notes = self.payment_notes

        service_order_number = self.service_order_number

        legacy_order_number = self.legacy_order_number

        custom_order_number = self.custom_order_number

        payment_status = self.payment_status

        payment_option = self.payment_option

        shipment_status = self.shipment_status

        order_status = self.order_status

        owner_id = self.owner_id

        owner_department = self.owner_department

        client_site = self.client_site

        client_site_code = self.client_site_code

        vendor_site = self.vendor_site

        internal = self.internal

        guid: Union[Unset, str] = UNSET
        if not isinstance(self.guid, Unset):
            guid = str(self.guid)

        business_from_time: Union[None, Unset, str]
        if isinstance(self.business_from_time, Unset):
            business_from_time = UNSET
        elif isinstance(self.business_from_time, datetime.datetime):
            business_from_time = self.business_from_time.isoformat()
        else:
            business_from_time = self.business_from_time

        business_to_time: Union[None, Unset, str]
        if isinstance(self.business_to_time, Unset):
            business_to_time = UNSET
        elif isinstance(self.business_to_time, datetime.datetime):
            business_to_time = self.business_to_time.isoformat()
        else:
            business_to_time = self.business_to_time

        site_access_notes = self.site_access_notes

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

        request_from_date: Union[None, Unset, str]
        if isinstance(self.request_from_date, Unset):
            request_from_date = UNSET
        elif isinstance(self.request_from_date, datetime.datetime):
            request_from_date = self.request_from_date.isoformat()
        else:
            request_from_date = self.request_from_date

        request_from_time: Union[None, Unset, str]
        if isinstance(self.request_from_time, Unset):
            request_from_time = UNSET
        elif isinstance(self.request_from_time, datetime.datetime):
            request_from_time = self.request_from_time.isoformat()
        else:
            request_from_time = self.request_from_time

        request_to_date: Union[None, Unset, str]
        if isinstance(self.request_to_date, Unset):
            request_to_date = UNSET
        elif isinstance(self.request_to_date, datetime.datetime):
            request_to_date = self.request_to_date.isoformat()
        else:
            request_to_date = self.request_to_date

        request_to_time: Union[None, Unset, str]
        if isinstance(self.request_to_time, Unset):
            request_to_time = UNSET
        elif isinstance(self.request_to_time, datetime.datetime):
            request_to_time = self.request_to_time.isoformat()
        else:
            request_to_time = self.request_to_time

        order_notes = self.order_notes

        billing_address: Union[None, Unset, dict[str, Any]]
        if isinstance(self.billing_address, Unset):
            billing_address = UNSET
        elif isinstance(
            self.billing_address,
            QualerApiModelsServiceOrdersToClientOrderResponseModelBillingAddressType0,
        ):
            billing_address = self.billing_address.to_dict()
        else:
            billing_address = self.billing_address

        shipping_address: Union[None, Unset, dict[str, Any]]
        if isinstance(self.shipping_address, Unset):
            shipping_address = UNSET
        elif isinstance(
            self.shipping_address,
            QualerApiModelsServiceOrdersToClientOrderResponseModelShippingAddressType0,
        ):
            shipping_address = self.shipping_address.to_dict()
        else:
            shipping_address = self.shipping_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_id is not UNSET:
            field_dict["ServiceOrderId"] = service_order_id
        if parent_order_id is not UNSET:
            field_dict["ParentOrderId"] = parent_order_id
        if client_legacy_id is not UNSET:
            field_dict["ClientLegacyId"] = client_legacy_id
        if owner_name is not UNSET:
            field_dict["OwnerName"] = owner_name
        if submited_by_name is not UNSET:
            field_dict["SubmitedByName"] = submited_by_name
        if sign_off_by_name is not UNSET:
            field_dict["SignOffByName"] = sign_off_by_name
        if vendor_sign_off_by_name is not UNSET:
            field_dict["VendorSignOffByName"] = vendor_sign_off_by_name
        if approved_by_name is not UNSET:
            field_dict["ApprovedByName"] = approved_by_name
        if accepted_by_name is not UNSET:
            field_dict["AcceptedByName"] = accepted_by_name
        if ready_for_quality_control_by_name is not UNSET:
            field_dict["ReadyForQualityControlByName"] = (
                ready_for_quality_control_by_name
            )
        if quality_control_by_name is not UNSET:
            field_dict["QualityControlByName"] = quality_control_by_name
        if created_by_name is not UNSET:
            field_dict["CreatedByName"] = created_by_name
        if completed_by_name is not UNSET:
            field_dict["CompletedByName"] = completed_by_name
        if shipped_by_name is not UNSET:
            field_dict["ShippedByName"] = shipped_by_name
        if delivered_by_name is not UNSET:
            field_dict["DeliveredByName"] = delivered_by_name
        if invoiced_by_name is not UNSET:
            field_dict["InvoicedByName"] = invoiced_by_name
        if paid_by_name is not UNSET:
            field_dict["PaidByName"] = paid_by_name
        if cancelled_by_name is not UNSET:
            field_dict["CancelledByName"] = cancelled_by_name
        if closed_by_name is not UNSET:
            field_dict["ClosedByName"] = closed_by_name
        if client_company_id is not UNSET:
            field_dict["ClientCompanyId"] = client_company_id
        if client_company_name is not UNSET:
            field_dict["ClientCompanyName"] = client_company_name
        if client_domain_name is not UNSET:
            field_dict["ClientDomainName"] = client_domain_name
        if client_alternative_names is not UNSET:
            field_dict["ClientAlternativeNames"] = client_alternative_names
        if service_comments is not UNSET:
            field_dict["ServiceComments"] = service_comments
        if service_private_comments is not UNSET:
            field_dict["ServicePrivateComments"] = service_private_comments
        if created_on is not UNSET:
            field_dict["CreatedOn"] = created_on
        if approved_on is not UNSET:
            field_dict["ApprovedOn"] = approved_on
        if sign_off_on is not UNSET:
            field_dict["SignOffOn"] = sign_off_on
        if vendor_sign_off_on is not UNSET:
            field_dict["VendorSignOffOn"] = vendor_sign_off_on
        if completed_on is not UNSET:
            field_dict["CompletedOn"] = completed_on
        if submited_on is not UNSET:
            field_dict["SubmitedOn"] = submited_on
        if shipped_on is not UNSET:
            field_dict["ShippedOn"] = shipped_on
        if accepted_on is not UNSET:
            field_dict["AcceptedOn"] = accepted_on
        if ready_for_quality_control_on is not UNSET:
            field_dict["ReadyForQualityControlOn"] = ready_for_quality_control_on
        if quality_control_on is not UNSET:
            field_dict["QualityControlOn"] = quality_control_on
        if delivered_on is not UNSET:
            field_dict["DeliveredOn"] = delivered_on
        if invoiced_on is not UNSET:
            field_dict["InvoicedOn"] = invoiced_on
        if last_invoiced_on is not UNSET:
            field_dict["LastInvoicedOn"] = last_invoiced_on
        if payment_due_on is not UNSET:
            field_dict["PaymentDueOn"] = payment_due_on
        if paid_on is not UNSET:
            field_dict["PaidOn"] = paid_on
        if late_fee_on is not UNSET:
            field_dict["LateFeeOn"] = late_fee_on
        if cancelled_on is not UNSET:
            field_dict["CancelledOn"] = cancelled_on
        if closed_on is not UNSET:
            field_dict["ClosedOn"] = closed_on
        if last_updated_on is not UNSET:
            field_dict["LastUpdatedOn"] = last_updated_on
        if last_updated_by is not UNSET:
            field_dict["LastUpdatedBy"] = last_updated_by
        if submited_by_id is not UNSET:
            field_dict["SubmitedById"] = submited_by_id
        if sign_off_by_id is not UNSET:
            field_dict["SignOffById"] = sign_off_by_id
        if vendor_sign_off_by_id is not UNSET:
            field_dict["VendorSignOffById"] = vendor_sign_off_by_id
        if approved_by_id is not UNSET:
            field_dict["ApprovedById"] = approved_by_id
        if late_fee_by_id is not UNSET:
            field_dict["LateFeeById"] = late_fee_by_id
        if accepted_by_id is not UNSET:
            field_dict["AcceptedById"] = accepted_by_id
        if ready_for_quality_control_by_id is not UNSET:
            field_dict["ReadyForQualityControlById"] = ready_for_quality_control_by_id
        if quality_control_by_id is not UNSET:
            field_dict["QualityControlById"] = quality_control_by_id
        if created_by_id is not UNSET:
            field_dict["CreatedById"] = created_by_id
        if completed_by_id is not UNSET:
            field_dict["CompletedById"] = completed_by_id
        if shipped_by_id is not UNSET:
            field_dict["ShippedById"] = shipped_by_id
        if delivered_by_id is not UNSET:
            field_dict["DeliveredById"] = delivered_by_id
        if invoiced_by_id is not UNSET:
            field_dict["InvoicedById"] = invoiced_by_id
        if paid_by_id is not UNSET:
            field_dict["PaidById"] = paid_by_id
        if cancelled_by_id is not UNSET:
            field_dict["CancelledById"] = cancelled_by_id
        if closed_by_id is not UNSET:
            field_dict["ClosedById"] = closed_by_id
        if po_number is not UNSET:
            field_dict["PoNumber"] = po_number
        if secondary_po is not UNSET:
            field_dict["SecondaryPo"] = secondary_po
        if service_total is not UNSET:
            field_dict["ServiceTotal"] = service_total
        if repairs_total is not UNSET:
            field_dict["RepairsTotal"] = repairs_total
        if parts_total is not UNSET:
            field_dict["PartsTotal"] = parts_total
        if parts_total_before_discount is not UNSET:
            field_dict["PartsTotalBeforeDiscount"] = parts_total_before_discount
        if parts_discount_total is not UNSET:
            field_dict["PartsDiscountTotal"] = parts_discount_total
        if effective_tax_rate is not UNSET:
            field_dict["EffectiveTaxRate"] = effective_tax_rate
        if tax_amount is not UNSET:
            field_dict["TaxAmount"] = tax_amount
        if shipping_fee is not UNSET:
            field_dict["ShippingFee"] = shipping_fee
        if travel_charge is not UNSET:
            field_dict["TravelCharge"] = travel_charge
        if late_fee is not UNSET:
            field_dict["LateFee"] = late_fee
        if is_tax_exempt is not UNSET:
            field_dict["IsTaxExempt"] = is_tax_exempt
        if service_discount is not UNSET:
            field_dict["ServiceDiscount"] = service_discount
        if trade_in_credit is not UNSET:
            field_dict["TradeInCredit"] = trade_in_credit
        if prepaid_credit is not UNSET:
            field_dict["PrepaidCredit"] = prepaid_credit
        if grand_total is not UNSET:
            field_dict["GrandTotal"] = grand_total
        if paid_amount is not UNSET:
            field_dict["PaidAmount"] = paid_amount
        if remaining_balance is not UNSET:
            field_dict["RemainingBalance"] = remaining_balance
        if service_discount_details is not UNSET:
            field_dict["ServiceDiscountDetails"] = service_discount_details
        if trade_in_credit_details is not UNSET:
            field_dict["TradeInCreditDetails"] = trade_in_credit_details
        if prepaid_credit_details is not UNSET:
            field_dict["PrepaidCreditDetails"] = prepaid_credit_details
        if payment_notes is not UNSET:
            field_dict["PaymentNotes"] = payment_notes
        if service_order_number is not UNSET:
            field_dict["ServiceOrderNumber"] = service_order_number
        if legacy_order_number is not UNSET:
            field_dict["LegacyOrderNumber"] = legacy_order_number
        if custom_order_number is not UNSET:
            field_dict["CustomOrderNumber"] = custom_order_number
        if payment_status is not UNSET:
            field_dict["PaymentStatus"] = payment_status
        if payment_option is not UNSET:
            field_dict["PaymentOption"] = payment_option
        if shipment_status is not UNSET:
            field_dict["ShipmentStatus"] = shipment_status
        if order_status is not UNSET:
            field_dict["OrderStatus"] = order_status
        if owner_id is not UNSET:
            field_dict["OwnerId"] = owner_id
        if owner_department is not UNSET:
            field_dict["OwnerDepartment"] = owner_department
        if client_site is not UNSET:
            field_dict["ClientSite"] = client_site
        if client_site_code is not UNSET:
            field_dict["ClientSiteCode"] = client_site_code
        if vendor_site is not UNSET:
            field_dict["VendorSite"] = vendor_site
        if internal is not UNSET:
            field_dict["Internal"] = internal
        if guid is not UNSET:
            field_dict["Guid"] = guid
        if business_from_time is not UNSET:
            field_dict["BusinessFromTime"] = business_from_time
        if business_to_time is not UNSET:
            field_dict["BusinessToTime"] = business_to_time
        if site_access_notes is not UNSET:
            field_dict["SiteAccessNotes"] = site_access_notes
        if desired_date is not UNSET:
            field_dict["DesiredDate"] = desired_date
        if deadline_date is not UNSET:
            field_dict["DeadlineDate"] = deadline_date
        if request_from_date is not UNSET:
            field_dict["RequestFromDate"] = request_from_date
        if request_from_time is not UNSET:
            field_dict["RequestFromTime"] = request_from_time
        if request_to_date is not UNSET:
            field_dict["RequestToDate"] = request_to_date
        if request_to_time is not UNSET:
            field_dict["RequestToTime"] = request_to_time
        if order_notes is not UNSET:
            field_dict["OrderNotes"] = order_notes
        if billing_address is not UNSET:
            field_dict["BillingAddress"] = billing_address
        if shipping_address is not UNSET:
            field_dict["ShippingAddress"] = shipping_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_service_orders_to_client_order_response_model_billing_address_type_0 import (
            QualerApiModelsServiceOrdersToClientOrderResponseModelBillingAddressType0,
        )
        from ..models.qualer_api_models_service_orders_to_client_order_response_model_shipping_address_type_0 import (
            QualerApiModelsServiceOrdersToClientOrderResponseModelShippingAddressType0,
        )

        d = dict(src_dict)
        service_order_id = d.pop("ServiceOrderId", UNSET)

        parent_order_id = d.pop("ParentOrderId", UNSET)

        client_legacy_id = d.pop("ClientLegacyId", UNSET)

        owner_name = d.pop("OwnerName", UNSET)

        submited_by_name = d.pop("SubmitedByName", UNSET)

        sign_off_by_name = d.pop("SignOffByName", UNSET)

        vendor_sign_off_by_name = d.pop("VendorSignOffByName", UNSET)

        approved_by_name = d.pop("ApprovedByName", UNSET)

        accepted_by_name = d.pop("AcceptedByName", UNSET)

        ready_for_quality_control_by_name = d.pop("ReadyForQualityControlByName", UNSET)

        quality_control_by_name = d.pop("QualityControlByName", UNSET)

        created_by_name = d.pop("CreatedByName", UNSET)

        completed_by_name = d.pop("CompletedByName", UNSET)

        shipped_by_name = d.pop("ShippedByName", UNSET)

        delivered_by_name = d.pop("DeliveredByName", UNSET)

        invoiced_by_name = d.pop("InvoicedByName", UNSET)

        paid_by_name = d.pop("PaidByName", UNSET)

        cancelled_by_name = d.pop("CancelledByName", UNSET)

        closed_by_name = d.pop("ClosedByName", UNSET)

        client_company_id = d.pop("ClientCompanyId", UNSET)

        client_company_name = d.pop("ClientCompanyName", UNSET)

        client_domain_name = d.pop("ClientDomainName", UNSET)

        client_alternative_names = d.pop("ClientAlternativeNames", UNSET)

        service_comments = d.pop("ServiceComments", UNSET)

        service_private_comments = d.pop("ServicePrivateComments", UNSET)

        def _parse_created_on(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_on_type_0 = isoparse(data)

                return created_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        created_on = _parse_created_on(d.pop("CreatedOn", UNSET))

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

        def _parse_vendor_sign_off_on(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                vendor_sign_off_on_type_0 = isoparse(data)

                return vendor_sign_off_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        vendor_sign_off_on = _parse_vendor_sign_off_on(d.pop("VendorSignOffOn", UNSET))

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

        def _parse_submited_on(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                submited_on_type_0 = isoparse(data)

                return submited_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        submited_on = _parse_submited_on(d.pop("SubmitedOn", UNSET))

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

        def _parse_ready_for_quality_control_on(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ready_for_quality_control_on_type_0 = isoparse(data)

                return ready_for_quality_control_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        ready_for_quality_control_on = _parse_ready_for_quality_control_on(
            d.pop("ReadyForQualityControlOn", UNSET)
        )

        def _parse_quality_control_on(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                quality_control_on_type_0 = isoparse(data)

                return quality_control_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        quality_control_on = _parse_quality_control_on(d.pop("QualityControlOn", UNSET))

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

        def _parse_last_invoiced_on(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_invoiced_on_type_0 = isoparse(data)

                return last_invoiced_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_invoiced_on = _parse_last_invoiced_on(d.pop("LastInvoicedOn", UNSET))

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

        def _parse_late_fee_on(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                late_fee_on_type_0 = isoparse(data)

                return late_fee_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        late_fee_on = _parse_late_fee_on(d.pop("LateFeeOn", UNSET))

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

        def _parse_closed_on(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closed_on_type_0 = isoparse(data)

                return closed_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        closed_on = _parse_closed_on(d.pop("ClosedOn", UNSET))

        def _parse_last_updated_on(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_updated_on_type_0 = isoparse(data)

                return last_updated_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_updated_on = _parse_last_updated_on(d.pop("LastUpdatedOn", UNSET))

        last_updated_by = d.pop("LastUpdatedBy", UNSET)

        submited_by_id = d.pop("SubmitedById", UNSET)

        sign_off_by_id = d.pop("SignOffById", UNSET)

        vendor_sign_off_by_id = d.pop("VendorSignOffById", UNSET)

        approved_by_id = d.pop("ApprovedById", UNSET)

        late_fee_by_id = d.pop("LateFeeById", UNSET)

        accepted_by_id = d.pop("AcceptedById", UNSET)

        ready_for_quality_control_by_id = d.pop("ReadyForQualityControlById", UNSET)

        quality_control_by_id = d.pop("QualityControlById", UNSET)

        created_by_id = d.pop("CreatedById", UNSET)

        completed_by_id = d.pop("CompletedById", UNSET)

        shipped_by_id = d.pop("ShippedById", UNSET)

        delivered_by_id = d.pop("DeliveredById", UNSET)

        invoiced_by_id = d.pop("InvoicedById", UNSET)

        paid_by_id = d.pop("PaidById", UNSET)

        cancelled_by_id = d.pop("CancelledById", UNSET)

        closed_by_id = d.pop("ClosedById", UNSET)

        po_number = d.pop("PoNumber", UNSET)

        secondary_po = d.pop("SecondaryPo", UNSET)

        service_total = d.pop("ServiceTotal", UNSET)

        repairs_total = d.pop("RepairsTotal", UNSET)

        parts_total = d.pop("PartsTotal", UNSET)

        parts_total_before_discount = d.pop("PartsTotalBeforeDiscount", UNSET)

        parts_discount_total = d.pop("PartsDiscountTotal", UNSET)

        effective_tax_rate = d.pop("EffectiveTaxRate", UNSET)

        tax_amount = d.pop("TaxAmount", UNSET)

        shipping_fee = d.pop("ShippingFee", UNSET)

        travel_charge = d.pop("TravelCharge", UNSET)

        late_fee = d.pop("LateFee", UNSET)

        is_tax_exempt = d.pop("IsTaxExempt", UNSET)

        service_discount = d.pop("ServiceDiscount", UNSET)

        trade_in_credit = d.pop("TradeInCredit", UNSET)

        prepaid_credit = d.pop("PrepaidCredit", UNSET)

        grand_total = d.pop("GrandTotal", UNSET)

        paid_amount = d.pop("PaidAmount", UNSET)

        remaining_balance = d.pop("RemainingBalance", UNSET)

        service_discount_details = d.pop("ServiceDiscountDetails", UNSET)

        trade_in_credit_details = d.pop("TradeInCreditDetails", UNSET)

        prepaid_credit_details = d.pop("PrepaidCreditDetails", UNSET)

        payment_notes = d.pop("PaymentNotes", UNSET)

        service_order_number = d.pop("ServiceOrderNumber", UNSET)

        legacy_order_number = d.pop("LegacyOrderNumber", UNSET)

        custom_order_number = d.pop("CustomOrderNumber", UNSET)

        payment_status = d.pop("PaymentStatus", UNSET)

        payment_option = d.pop("PaymentOption", UNSET)

        shipment_status = d.pop("ShipmentStatus", UNSET)

        order_status = d.pop("OrderStatus", UNSET)

        owner_id = d.pop("OwnerId", UNSET)

        owner_department = d.pop("OwnerDepartment", UNSET)

        client_site = d.pop("ClientSite", UNSET)

        client_site_code = d.pop("ClientSiteCode", UNSET)

        vendor_site = d.pop("VendorSite", UNSET)

        internal = d.pop("Internal", UNSET)

        _guid = d.pop("Guid", UNSET)
        guid: Union[Unset, UUID]
        if isinstance(_guid, Unset):
            guid = UNSET
        else:
            guid = UUID(_guid)

        def _parse_business_from_time(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                business_from_time_type_0 = isoparse(data)

                return business_from_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        business_from_time = _parse_business_from_time(d.pop("BusinessFromTime", UNSET))

        def _parse_business_to_time(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                business_to_time_type_0 = isoparse(data)

                return business_to_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        business_to_time = _parse_business_to_time(d.pop("BusinessToTime", UNSET))

        site_access_notes = d.pop("SiteAccessNotes", UNSET)

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

        def _parse_request_from_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                request_from_date_type_0 = isoparse(data)

                return request_from_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        request_from_date = _parse_request_from_date(d.pop("RequestFromDate", UNSET))

        def _parse_request_from_time(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                request_from_time_type_0 = isoparse(data)

                return request_from_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        request_from_time = _parse_request_from_time(d.pop("RequestFromTime", UNSET))

        def _parse_request_to_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                request_to_date_type_0 = isoparse(data)

                return request_to_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        request_to_date = _parse_request_to_date(d.pop("RequestToDate", UNSET))

        def _parse_request_to_time(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                request_to_time_type_0 = isoparse(data)

                return request_to_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        request_to_time = _parse_request_to_time(d.pop("RequestToTime", UNSET))

        order_notes = d.pop("OrderNotes", UNSET)

        def _parse_billing_address(
            data: object,
        ) -> Union[
            "QualerApiModelsServiceOrdersToClientOrderResponseModelBillingAddressType0",
            None,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                billing_address_type_0 = QualerApiModelsServiceOrdersToClientOrderResponseModelBillingAddressType0.from_dict(
                    data
                )

                return billing_address_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    "QualerApiModelsServiceOrdersToClientOrderResponseModelBillingAddressType0",
                    None,
                    Unset,
                ],
                data,
            )

        billing_address = _parse_billing_address(d.pop("BillingAddress", UNSET))

        def _parse_shipping_address(
            data: object,
        ) -> Union[
            "QualerApiModelsServiceOrdersToClientOrderResponseModelShippingAddressType0",
            None,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                shipping_address_type_0 = QualerApiModelsServiceOrdersToClientOrderResponseModelShippingAddressType0.from_dict(
                    data
                )

                return shipping_address_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    "QualerApiModelsServiceOrdersToClientOrderResponseModelShippingAddressType0",
                    None,
                    Unset,
                ],
                data,
            )

        shipping_address = _parse_shipping_address(d.pop("ShippingAddress", UNSET))

        qualer_api_models_service_orders_to_client_order_response_model = cls(
            service_order_id=service_order_id,
            parent_order_id=parent_order_id,
            client_legacy_id=client_legacy_id,
            owner_name=owner_name,
            submited_by_name=submited_by_name,
            sign_off_by_name=sign_off_by_name,
            vendor_sign_off_by_name=vendor_sign_off_by_name,
            approved_by_name=approved_by_name,
            accepted_by_name=accepted_by_name,
            ready_for_quality_control_by_name=ready_for_quality_control_by_name,
            quality_control_by_name=quality_control_by_name,
            created_by_name=created_by_name,
            completed_by_name=completed_by_name,
            shipped_by_name=shipped_by_name,
            delivered_by_name=delivered_by_name,
            invoiced_by_name=invoiced_by_name,
            paid_by_name=paid_by_name,
            cancelled_by_name=cancelled_by_name,
            closed_by_name=closed_by_name,
            client_company_id=client_company_id,
            client_company_name=client_company_name,
            client_domain_name=client_domain_name,
            client_alternative_names=client_alternative_names,
            service_comments=service_comments,
            service_private_comments=service_private_comments,
            created_on=created_on,
            approved_on=approved_on,
            sign_off_on=sign_off_on,
            vendor_sign_off_on=vendor_sign_off_on,
            completed_on=completed_on,
            submited_on=submited_on,
            shipped_on=shipped_on,
            accepted_on=accepted_on,
            ready_for_quality_control_on=ready_for_quality_control_on,
            quality_control_on=quality_control_on,
            delivered_on=delivered_on,
            invoiced_on=invoiced_on,
            last_invoiced_on=last_invoiced_on,
            payment_due_on=payment_due_on,
            paid_on=paid_on,
            late_fee_on=late_fee_on,
            cancelled_on=cancelled_on,
            closed_on=closed_on,
            last_updated_on=last_updated_on,
            last_updated_by=last_updated_by,
            submited_by_id=submited_by_id,
            sign_off_by_id=sign_off_by_id,
            vendor_sign_off_by_id=vendor_sign_off_by_id,
            approved_by_id=approved_by_id,
            late_fee_by_id=late_fee_by_id,
            accepted_by_id=accepted_by_id,
            ready_for_quality_control_by_id=ready_for_quality_control_by_id,
            quality_control_by_id=quality_control_by_id,
            created_by_id=created_by_id,
            completed_by_id=completed_by_id,
            shipped_by_id=shipped_by_id,
            delivered_by_id=delivered_by_id,
            invoiced_by_id=invoiced_by_id,
            paid_by_id=paid_by_id,
            cancelled_by_id=cancelled_by_id,
            closed_by_id=closed_by_id,
            po_number=po_number,
            secondary_po=secondary_po,
            service_total=service_total,
            repairs_total=repairs_total,
            parts_total=parts_total,
            parts_total_before_discount=parts_total_before_discount,
            parts_discount_total=parts_discount_total,
            effective_tax_rate=effective_tax_rate,
            tax_amount=tax_amount,
            shipping_fee=shipping_fee,
            travel_charge=travel_charge,
            late_fee=late_fee,
            is_tax_exempt=is_tax_exempt,
            service_discount=service_discount,
            trade_in_credit=trade_in_credit,
            prepaid_credit=prepaid_credit,
            grand_total=grand_total,
            paid_amount=paid_amount,
            remaining_balance=remaining_balance,
            service_discount_details=service_discount_details,
            trade_in_credit_details=trade_in_credit_details,
            prepaid_credit_details=prepaid_credit_details,
            payment_notes=payment_notes,
            service_order_number=service_order_number,
            legacy_order_number=legacy_order_number,
            custom_order_number=custom_order_number,
            payment_status=payment_status,
            payment_option=payment_option,
            shipment_status=shipment_status,
            order_status=order_status,
            owner_id=owner_id,
            owner_department=owner_department,
            client_site=client_site,
            client_site_code=client_site_code,
            vendor_site=vendor_site,
            internal=internal,
            guid=guid,
            business_from_time=business_from_time,
            business_to_time=business_to_time,
            site_access_notes=site_access_notes,
            desired_date=desired_date,
            deadline_date=deadline_date,
            request_from_date=request_from_date,
            request_from_time=request_from_time,
            request_to_date=request_to_date,
            request_to_time=request_to_time,
            order_notes=order_notes,
            billing_address=billing_address,
            shipping_address=shipping_address,
        )

        qualer_api_models_service_orders_to_client_order_response_model.additional_properties = (
            d
        )
        return qualer_api_models_service_orders_to_client_order_response_model

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
