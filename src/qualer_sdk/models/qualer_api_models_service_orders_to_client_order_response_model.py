import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

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
        service_order_id (Optional[int]):
        parent_order_id (Optional[int]):
        client_legacy_id (Optional[str]):
        owner_name (Optional[str]):
        submited_by_name (Optional[str]):
        sign_off_by_name (Optional[str]):
        vendor_sign_off_by_name (Optional[str]):
        approved_by_name (Optional[str]):
        accepted_by_name (Optional[str]):
        ready_for_quality_control_by_name (Optional[str]):
        quality_control_by_name (Optional[str]):
        created_by_name (Optional[str]):
        completed_by_name (Optional[str]):
        shipped_by_name (Optional[str]):
        delivered_by_name (Optional[str]):
        invoiced_by_name (Optional[str]):
        paid_by_name (Optional[str]):
        cancelled_by_name (Optional[str]):
        closed_by_name (Optional[str]):
        client_company_id (Optional[int]):
        client_company_name (Optional[str]):
        client_domain_name (Optional[str]):
        client_alternative_names (Optional[str]):
        service_comments (Optional[str]):
        service_private_comments (Optional[str]):
        created_on (Optional[datetime.datetime]):
        approved_on (Optional[datetime.datetime]):
        sign_off_on (Optional[datetime.datetime]):
        vendor_sign_off_on (Optional[datetime.datetime]):
        completed_on (Optional[datetime.datetime]):
        submited_on (Optional[datetime.datetime]):
        shipped_on (Optional[datetime.datetime]):
        accepted_on (Optional[datetime.datetime]):
        ready_for_quality_control_on (Optional[datetime.datetime]):
        quality_control_on (Optional[datetime.datetime]):
        delivered_on (Optional[datetime.datetime]):
        invoiced_on (Optional[datetime.datetime]):
        last_invoiced_on (Optional[datetime.datetime]):
        payment_due_on (Optional[datetime.datetime]):
        paid_on (Optional[datetime.datetime]):
        late_fee_on (Optional[datetime.datetime]):
        cancelled_on (Optional[datetime.datetime]):
        closed_on (Optional[datetime.datetime]):
        last_updated_on (Optional[datetime.datetime]):
        last_updated_by (Optional[str]):
        submited_by_id (Optional[int]):
        sign_off_by_id (Optional[int]):
        vendor_sign_off_by_id (Optional[int]):
        approved_by_id (Optional[int]):
        late_fee_by_id (Optional[int]):
        accepted_by_id (Optional[int]):
        ready_for_quality_control_by_id (Optional[int]):
        quality_control_by_id (Optional[int]):
        created_by_id (Optional[int]):
        completed_by_id (Optional[int]):
        shipped_by_id (Optional[int]):
        delivered_by_id (Optional[int]):
        invoiced_by_id (Optional[int]):
        paid_by_id (Optional[int]):
        cancelled_by_id (Optional[int]):
        closed_by_id (Optional[int]):
        po_number (Optional[str]):
        secondary_po (Optional[str]):
        service_total (Optional[float]):
        repairs_total (Optional[float]):
        parts_total (Optional[float]):
        parts_total_before_discount (Optional[float]):
        parts_discount_total (Optional[float]):
        effective_tax_rate (Optional[float]):
        tax_amount (Optional[float]):
        shipping_fee (Optional[float]):
        travel_charge (Optional[float]):
        late_fee (Optional[float]):
        is_tax_exempt (Optional[bool]):
        service_discount (Optional[float]):
        trade_in_credit (Optional[float]):
        prepaid_credit (Optional[float]):
        grand_total (Optional[float]):
        paid_amount (Optional[float]):
        remaining_balance (Optional[float]):
        service_discount_details (Optional[str]):
        trade_in_credit_details (Optional[str]):
        prepaid_credit_details (Optional[str]):
        payment_notes (Optional[str]):
        service_order_number (Optional[int]):
        legacy_order_number (Optional[str]):
        custom_order_number (Optional[str]):
        payment_status (Optional[str]):
        payment_option (Optional[str]):
        shipment_status (Optional[str]):
        order_status (Optional[str]):
        owner_id (Optional[int]):
        owner_department (Optional[str]):
        client_site (Optional[str]):
        client_site_code (Optional[str]):
        vendor_site (Optional[str]):
        internal (Optional[bool]):
        guid (Optional[UUID]):  Example: 00000000-0000-0000-0000-000000000000.
        business_from_time (Optional[datetime.datetime]):
        business_to_time (Optional[datetime.datetime]):
        site_access_notes (Optional[str]):
        desired_date (Optional[datetime.datetime]):
        deadline_date (Optional[datetime.datetime]):
        request_from_date (Optional[datetime.datetime]):
        request_from_time (Optional[datetime.datetime]):
        request_to_date (Optional[datetime.datetime]):
        request_to_time (Optional[datetime.datetime]):
        order_notes (Optional[str]):
        billing_address (Union['QualerApiModelsServiceOrdersToClientOrderResponseModelBillingAddressType0', None,
            None]):
        shipping_address (Union['QualerApiModelsServiceOrdersToClientOrderResponseModelShippingAddressType0', None,
            None]):
    """

    service_order_id: Optional[int] = None
    parent_order_id: Optional[int] = None
    client_legacy_id: Optional[str] = None
    owner_name: Optional[str] = None
    submited_by_name: Optional[str] = None
    sign_off_by_name: Optional[str] = None
    vendor_sign_off_by_name: Optional[str] = None
    approved_by_name: Optional[str] = None
    accepted_by_name: Optional[str] = None
    ready_for_quality_control_by_name: Optional[str] = None
    quality_control_by_name: Optional[str] = None
    created_by_name: Optional[str] = None
    completed_by_name: Optional[str] = None
    shipped_by_name: Optional[str] = None
    delivered_by_name: Optional[str] = None
    invoiced_by_name: Optional[str] = None
    paid_by_name: Optional[str] = None
    cancelled_by_name: Optional[str] = None
    closed_by_name: Optional[str] = None
    client_company_id: Optional[int] = None
    client_company_name: Optional[str] = None
    client_domain_name: Optional[str] = None
    client_alternative_names: Optional[str] = None
    service_comments: Optional[str] = None
    service_private_comments: Optional[str] = None
    created_on: Optional[datetime.datetime] = None
    approved_on: Optional[datetime.datetime] = None
    sign_off_on: Optional[datetime.datetime] = None
    vendor_sign_off_on: Optional[datetime.datetime] = None
    completed_on: Optional[datetime.datetime] = None
    submited_on: Optional[datetime.datetime] = None
    shipped_on: Optional[datetime.datetime] = None
    accepted_on: Optional[datetime.datetime] = None
    ready_for_quality_control_on: Optional[datetime.datetime] = None
    quality_control_on: Optional[datetime.datetime] = None
    delivered_on: Optional[datetime.datetime] = None
    invoiced_on: Optional[datetime.datetime] = None
    last_invoiced_on: Optional[datetime.datetime] = None
    payment_due_on: Optional[datetime.datetime] = None
    paid_on: Optional[datetime.datetime] = None
    late_fee_on: Optional[datetime.datetime] = None
    cancelled_on: Optional[datetime.datetime] = None
    closed_on: Optional[datetime.datetime] = None
    last_updated_on: Optional[datetime.datetime] = None
    last_updated_by: Optional[str] = None
    submited_by_id: Optional[int] = None
    sign_off_by_id: Optional[int] = None
    vendor_sign_off_by_id: Optional[int] = None
    approved_by_id: Optional[int] = None
    late_fee_by_id: Optional[int] = None
    accepted_by_id: Optional[int] = None
    ready_for_quality_control_by_id: Optional[int] = None
    quality_control_by_id: Optional[int] = None
    created_by_id: Optional[int] = None
    completed_by_id: Optional[int] = None
    shipped_by_id: Optional[int] = None
    delivered_by_id: Optional[int] = None
    invoiced_by_id: Optional[int] = None
    paid_by_id: Optional[int] = None
    cancelled_by_id: Optional[int] = None
    closed_by_id: Optional[int] = None
    po_number: Optional[str] = None
    secondary_po: Optional[str] = None
    service_total: Optional[float] = None
    repairs_total: Optional[float] = None
    parts_total: Optional[float] = None
    parts_total_before_discount: Optional[float] = None
    parts_discount_total: Optional[float] = None
    effective_tax_rate: Optional[float] = None
    tax_amount: Optional[float] = None
    shipping_fee: Optional[float] = None
    travel_charge: Optional[float] = None
    late_fee: Optional[float] = None
    is_tax_exempt: Optional[bool] = None
    service_discount: Optional[float] = None
    trade_in_credit: Optional[float] = None
    prepaid_credit: Optional[float] = None
    grand_total: Optional[float] = None
    paid_amount: Optional[float] = None
    remaining_balance: Optional[float] = None
    service_discount_details: Optional[str] = None
    trade_in_credit_details: Optional[str] = None
    prepaid_credit_details: Optional[str] = None
    payment_notes: Optional[str] = None
    service_order_number: Optional[int] = None
    legacy_order_number: Optional[str] = None
    custom_order_number: Optional[str] = None
    payment_status: Optional[str] = None
    payment_option: Optional[str] = None
    shipment_status: Optional[str] = None
    order_status: Optional[str] = None
    owner_id: Optional[int] = None
    owner_department: Optional[str] = None
    client_site: Optional[str] = None
    client_site_code: Optional[str] = None
    vendor_site: Optional[str] = None
    internal: Optional[bool] = None
    guid: Optional[UUID] = None
    business_from_time: Optional[datetime.datetime] = None
    business_to_time: Optional[datetime.datetime] = None
    site_access_notes: Optional[str] = None
    desired_date: Optional[datetime.datetime] = None
    deadline_date: Optional[datetime.datetime] = None
    request_from_date: Optional[datetime.datetime] = None
    request_from_time: Optional[datetime.datetime] = None
    request_to_date: Optional[datetime.datetime] = None
    request_to_time: Optional[datetime.datetime] = None
    order_notes: Optional[str] = None
    billing_address: Union[
        "QualerApiModelsServiceOrdersToClientOrderResponseModelBillingAddressType0",
        None,
        None,
    ] = None
    shipping_address: Union[
        "QualerApiModelsServiceOrdersToClientOrderResponseModelShippingAddressType0",
        None,
        None,
    ] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        created_on: Optional[str]
        if not self.created_on:
            created_on = None
        elif isinstance(self.created_on, datetime.datetime):
            created_on = self.created_on.isoformat()
        else:
            created_on = self.created_on

        approved_on: Optional[str]
        if not self.approved_on:
            approved_on = None
        elif isinstance(self.approved_on, datetime.datetime):
            approved_on = self.approved_on.isoformat()
        else:
            approved_on = self.approved_on

        sign_off_on: Optional[str]
        if not self.sign_off_on:
            sign_off_on = None
        elif isinstance(self.sign_off_on, datetime.datetime):
            sign_off_on = self.sign_off_on.isoformat()
        else:
            sign_off_on = self.sign_off_on

        vendor_sign_off_on: Optional[str]
        if not self.vendor_sign_off_on:
            vendor_sign_off_on = None
        elif isinstance(self.vendor_sign_off_on, datetime.datetime):
            vendor_sign_off_on = self.vendor_sign_off_on.isoformat()
        else:
            vendor_sign_off_on = self.vendor_sign_off_on

        completed_on: Optional[str]
        if not self.completed_on:
            completed_on = None
        elif isinstance(self.completed_on, datetime.datetime):
            completed_on = self.completed_on.isoformat()
        else:
            completed_on = self.completed_on

        submited_on: Optional[str]
        if not self.submited_on:
            submited_on = None
        elif isinstance(self.submited_on, datetime.datetime):
            submited_on = self.submited_on.isoformat()
        else:
            submited_on = self.submited_on

        shipped_on: Optional[str]
        if not self.shipped_on:
            shipped_on = None
        elif isinstance(self.shipped_on, datetime.datetime):
            shipped_on = self.shipped_on.isoformat()
        else:
            shipped_on = self.shipped_on

        accepted_on: Optional[str]
        if not self.accepted_on:
            accepted_on = None
        elif isinstance(self.accepted_on, datetime.datetime):
            accepted_on = self.accepted_on.isoformat()
        else:
            accepted_on = self.accepted_on

        ready_for_quality_control_on: Optional[str]
        if not self.ready_for_quality_control_on:
            ready_for_quality_control_on = None
        elif isinstance(self.ready_for_quality_control_on, datetime.datetime):
            ready_for_quality_control_on = self.ready_for_quality_control_on.isoformat()
        else:
            ready_for_quality_control_on = self.ready_for_quality_control_on

        quality_control_on: Optional[str]
        if not self.quality_control_on:
            quality_control_on = None
        elif isinstance(self.quality_control_on, datetime.datetime):
            quality_control_on = self.quality_control_on.isoformat()
        else:
            quality_control_on = self.quality_control_on

        delivered_on: Optional[str]
        if not self.delivered_on:
            delivered_on = None
        elif isinstance(self.delivered_on, datetime.datetime):
            delivered_on = self.delivered_on.isoformat()
        else:
            delivered_on = self.delivered_on

        invoiced_on: Optional[str]
        if not self.invoiced_on:
            invoiced_on = None
        elif isinstance(self.invoiced_on, datetime.datetime):
            invoiced_on = self.invoiced_on.isoformat()
        else:
            invoiced_on = self.invoiced_on

        last_invoiced_on: Optional[str]
        if not self.last_invoiced_on:
            last_invoiced_on = None
        elif isinstance(self.last_invoiced_on, datetime.datetime):
            last_invoiced_on = self.last_invoiced_on.isoformat()
        else:
            last_invoiced_on = self.last_invoiced_on

        payment_due_on: Optional[str]
        if not self.payment_due_on:
            payment_due_on = None
        elif isinstance(self.payment_due_on, datetime.datetime):
            payment_due_on = self.payment_due_on.isoformat()
        else:
            payment_due_on = self.payment_due_on

        paid_on: Optional[str]
        if not self.paid_on:
            paid_on = None
        elif isinstance(self.paid_on, datetime.datetime):
            paid_on = self.paid_on.isoformat()
        else:
            paid_on = self.paid_on

        late_fee_on: Optional[str]
        if not self.late_fee_on:
            late_fee_on = None
        elif isinstance(self.late_fee_on, datetime.datetime):
            late_fee_on = self.late_fee_on.isoformat()
        else:
            late_fee_on = self.late_fee_on

        cancelled_on: Optional[str]
        if not self.cancelled_on:
            cancelled_on = None
        elif isinstance(self.cancelled_on, datetime.datetime):
            cancelled_on = self.cancelled_on.isoformat()
        else:
            cancelled_on = self.cancelled_on

        closed_on: Optional[str]
        if not self.closed_on:
            closed_on = None
        elif isinstance(self.closed_on, datetime.datetime):
            closed_on = self.closed_on.isoformat()
        else:
            closed_on = self.closed_on

        last_updated_on: Optional[str] = None
        if self.last_updated_on:
            last_updated_on = self.last_updated_on.isoformat()

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

        guid: Optional[str] = None
        if self.guid:
            guid = str(self.guid)

        business_from_time: Optional[str]
        if not self.business_from_time:
            business_from_time = None
        elif isinstance(self.business_from_time, datetime.datetime):
            business_from_time = self.business_from_time.isoformat()
        else:
            business_from_time = self.business_from_time

        business_to_time: Optional[str]
        if not self.business_to_time:
            business_to_time = None
        elif isinstance(self.business_to_time, datetime.datetime):
            business_to_time = self.business_to_time.isoformat()
        else:
            business_to_time = self.business_to_time

        site_access_notes = self.site_access_notes

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

        request_from_date: Optional[str]
        if not self.request_from_date:
            request_from_date = None
        elif isinstance(self.request_from_date, datetime.datetime):
            request_from_date = self.request_from_date.isoformat()
        else:
            request_from_date = self.request_from_date

        request_from_time: Optional[str]
        if not self.request_from_time:
            request_from_time = None
        elif isinstance(self.request_from_time, datetime.datetime):
            request_from_time = self.request_from_time.isoformat()
        else:
            request_from_time = self.request_from_time

        request_to_date: Optional[str]
        if not self.request_to_date:
            request_to_date = None
        elif isinstance(self.request_to_date, datetime.datetime):
            request_to_date = self.request_to_date.isoformat()
        else:
            request_to_date = self.request_to_date

        request_to_time: Optional[str]
        if not self.request_to_time:
            request_to_time = None
        elif isinstance(self.request_to_time, datetime.datetime):
            request_to_time = self.request_to_time.isoformat()
        else:
            request_to_time = self.request_to_time

        order_notes = self.order_notes

        billing_address: Optional[Dict[str, Any]]
        if not self.billing_address:
            billing_address = None
        elif isinstance(
            self.billing_address,
            QualerApiModelsServiceOrdersToClientOrderResponseModelBillingAddressType0,
        ):
            billing_address = self.billing_address.to_dict()
        else:
            billing_address = self.billing_address

        shipping_address: Optional[Dict[str, Any]]
        if not self.shipping_address:
            shipping_address = None
        elif isinstance(
            self.shipping_address,
            QualerApiModelsServiceOrdersToClientOrderResponseModelShippingAddressType0,
        ):
            shipping_address = self.shipping_address.to_dict()
        else:
            shipping_address = self.shipping_address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_id is not None:
            field_dict["ServiceOrderId"] = service_order_id
        if parent_order_id is not None:
            field_dict["ParentOrderId"] = parent_order_id
        if client_legacy_id is not None:
            field_dict["ClientLegacyId"] = client_legacy_id
        if owner_name is not None:
            field_dict["OwnerName"] = owner_name
        if submited_by_name is not None:
            field_dict["SubmitedByName"] = submited_by_name
        if sign_off_by_name is not None:
            field_dict["SignOffByName"] = sign_off_by_name
        if vendor_sign_off_by_name is not None:
            field_dict["VendorSignOffByName"] = vendor_sign_off_by_name
        if approved_by_name is not None:
            field_dict["ApprovedByName"] = approved_by_name
        if accepted_by_name is not None:
            field_dict["AcceptedByName"] = accepted_by_name
        if ready_for_quality_control_by_name is not None:
            field_dict["ReadyForQualityControlByName"] = ready_for_quality_control_by_name
        if quality_control_by_name is not None:
            field_dict["QualityControlByName"] = quality_control_by_name
        if created_by_name is not None:
            field_dict["CreatedByName"] = created_by_name
        if completed_by_name is not None:
            field_dict["CompletedByName"] = completed_by_name
        if shipped_by_name is not None:
            field_dict["ShippedByName"] = shipped_by_name
        if delivered_by_name is not None:
            field_dict["DeliveredByName"] = delivered_by_name
        if invoiced_by_name is not None:
            field_dict["InvoicedByName"] = invoiced_by_name
        if paid_by_name is not None:
            field_dict["PaidByName"] = paid_by_name
        if cancelled_by_name is not None:
            field_dict["CancelledByName"] = cancelled_by_name
        if closed_by_name is not None:
            field_dict["ClosedByName"] = closed_by_name
        if client_company_id is not None:
            field_dict["ClientCompanyId"] = client_company_id
        if client_company_name is not None:
            field_dict["ClientCompanyName"] = client_company_name
        if client_domain_name is not None:
            field_dict["ClientDomainName"] = client_domain_name
        if client_alternative_names is not None:
            field_dict["ClientAlternativeNames"] = client_alternative_names
        if service_comments is not None:
            field_dict["ServiceComments"] = service_comments
        if service_private_comments is not None:
            field_dict["ServicePrivateComments"] = service_private_comments
        if created_on is not None:
            field_dict["CreatedOn"] = created_on
        if approved_on is not None:
            field_dict["ApprovedOn"] = approved_on
        if sign_off_on is not None:
            field_dict["SignOffOn"] = sign_off_on
        if vendor_sign_off_on is not None:
            field_dict["VendorSignOffOn"] = vendor_sign_off_on
        if completed_on is not None:
            field_dict["CompletedOn"] = completed_on
        if submited_on is not None:
            field_dict["SubmitedOn"] = submited_on
        if shipped_on is not None:
            field_dict["ShippedOn"] = shipped_on
        if accepted_on is not None:
            field_dict["AcceptedOn"] = accepted_on
        if ready_for_quality_control_on is not None:
            field_dict["ReadyForQualityControlOn"] = ready_for_quality_control_on
        if quality_control_on is not None:
            field_dict["QualityControlOn"] = quality_control_on
        if delivered_on is not None:
            field_dict["DeliveredOn"] = delivered_on
        if invoiced_on is not None:
            field_dict["InvoicedOn"] = invoiced_on
        if last_invoiced_on is not None:
            field_dict["LastInvoicedOn"] = last_invoiced_on
        if payment_due_on is not None:
            field_dict["PaymentDueOn"] = payment_due_on
        if paid_on is not None:
            field_dict["PaidOn"] = paid_on
        if late_fee_on is not None:
            field_dict["LateFeeOn"] = late_fee_on
        if cancelled_on is not None:
            field_dict["CancelledOn"] = cancelled_on
        if closed_on is not None:
            field_dict["ClosedOn"] = closed_on
        if last_updated_on is not None:
            field_dict["LastUpdatedOn"] = last_updated_on
        if last_updated_by is not None:
            field_dict["LastUpdatedBy"] = last_updated_by
        if submited_by_id is not None:
            field_dict["SubmitedById"] = submited_by_id
        if sign_off_by_id is not None:
            field_dict["SignOffById"] = sign_off_by_id
        if vendor_sign_off_by_id is not None:
            field_dict["VendorSignOffById"] = vendor_sign_off_by_id
        if approved_by_id is not None:
            field_dict["ApprovedById"] = approved_by_id
        if late_fee_by_id is not None:
            field_dict["LateFeeById"] = late_fee_by_id
        if accepted_by_id is not None:
            field_dict["AcceptedById"] = accepted_by_id
        if ready_for_quality_control_by_id is not None:
            field_dict["ReadyForQualityControlById"] = ready_for_quality_control_by_id
        if quality_control_by_id is not None:
            field_dict["QualityControlById"] = quality_control_by_id
        if created_by_id is not None:
            field_dict["CreatedById"] = created_by_id
        if completed_by_id is not None:
            field_dict["CompletedById"] = completed_by_id
        if shipped_by_id is not None:
            field_dict["ShippedById"] = shipped_by_id
        if delivered_by_id is not None:
            field_dict["DeliveredById"] = delivered_by_id
        if invoiced_by_id is not None:
            field_dict["InvoicedById"] = invoiced_by_id
        if paid_by_id is not None:
            field_dict["PaidById"] = paid_by_id
        if cancelled_by_id is not None:
            field_dict["CancelledById"] = cancelled_by_id
        if closed_by_id is not None:
            field_dict["ClosedById"] = closed_by_id
        if po_number is not None:
            field_dict["PoNumber"] = po_number
        if secondary_po is not None:
            field_dict["SecondaryPo"] = secondary_po
        if service_total is not None:
            field_dict["ServiceTotal"] = service_total
        if repairs_total is not None:
            field_dict["RepairsTotal"] = repairs_total
        if parts_total is not None:
            field_dict["PartsTotal"] = parts_total
        if parts_total_before_discount is not None:
            field_dict["PartsTotalBeforeDiscount"] = parts_total_before_discount
        if parts_discount_total is not None:
            field_dict["PartsDiscountTotal"] = parts_discount_total
        if effective_tax_rate is not None:
            field_dict["EffectiveTaxRate"] = effective_tax_rate
        if tax_amount is not None:
            field_dict["TaxAmount"] = tax_amount
        if shipping_fee is not None:
            field_dict["ShippingFee"] = shipping_fee
        if travel_charge is not None:
            field_dict["TravelCharge"] = travel_charge
        if late_fee is not None:
            field_dict["LateFee"] = late_fee
        if is_tax_exempt is not None:
            field_dict["IsTaxExempt"] = is_tax_exempt
        if service_discount is not None:
            field_dict["ServiceDiscount"] = service_discount
        if trade_in_credit is not None:
            field_dict["TradeInCredit"] = trade_in_credit
        if prepaid_credit is not None:
            field_dict["PrepaidCredit"] = prepaid_credit
        if grand_total is not None:
            field_dict["GrandTotal"] = grand_total
        if paid_amount is not None:
            field_dict["PaidAmount"] = paid_amount
        if remaining_balance is not None:
            field_dict["RemainingBalance"] = remaining_balance
        if service_discount_details is not None:
            field_dict["ServiceDiscountDetails"] = service_discount_details
        if trade_in_credit_details is not None:
            field_dict["TradeInCreditDetails"] = trade_in_credit_details
        if prepaid_credit_details is not None:
            field_dict["PrepaidCreditDetails"] = prepaid_credit_details
        if payment_notes is not None:
            field_dict["PaymentNotes"] = payment_notes
        if service_order_number is not None:
            field_dict["ServiceOrderNumber"] = service_order_number
        if legacy_order_number is not None:
            field_dict["LegacyOrderNumber"] = legacy_order_number
        if custom_order_number is not None:
            field_dict["CustomOrderNumber"] = custom_order_number
        if payment_status is not None:
            field_dict["PaymentStatus"] = payment_status
        if payment_option is not None:
            field_dict["PaymentOption"] = payment_option
        if shipment_status is not None:
            field_dict["ShipmentStatus"] = shipment_status
        if order_status is not None:
            field_dict["OrderStatus"] = order_status
        if owner_id is not None:
            field_dict["OwnerId"] = owner_id
        if owner_department is not None:
            field_dict["OwnerDepartment"] = owner_department
        if client_site is not None:
            field_dict["ClientSite"] = client_site
        if client_site_code is not None:
            field_dict["ClientSiteCode"] = client_site_code
        if vendor_site is not None:
            field_dict["VendorSite"] = vendor_site
        if internal is not None:
            field_dict["Internal"] = internal
        if guid is not None:
            field_dict["Guid"] = guid
        if business_from_time is not None:
            field_dict["BusinessFromTime"] = business_from_time
        if business_to_time is not None:
            field_dict["BusinessToTime"] = business_to_time
        if site_access_notes is not None:
            field_dict["SiteAccessNotes"] = site_access_notes
        if desired_date is not None:
            field_dict["DesiredDate"] = desired_date
        if deadline_date is not None:
            field_dict["DeadlineDate"] = deadline_date
        if request_from_date is not None:
            field_dict["RequestFromDate"] = request_from_date
        if request_from_time is not None:
            field_dict["RequestFromTime"] = request_from_time
        if request_to_date is not None:
            field_dict["RequestToDate"] = request_to_date
        if request_to_time is not None:
            field_dict["RequestToTime"] = request_to_time
        if order_notes is not None:
            field_dict["OrderNotes"] = order_notes
        if billing_address is not None:
            field_dict["BillingAddress"] = billing_address
        if shipping_address is not None:
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
        service_order_id = d.pop("ServiceOrderId", None)

        parent_order_id = d.pop("ParentOrderId", None)

        client_legacy_id = d.pop("ClientLegacyId", None)

        owner_name = d.pop("OwnerName", None)

        submited_by_name = d.pop("SubmitedByName", None)

        sign_off_by_name = d.pop("SignOffByName", None)

        vendor_sign_off_by_name = d.pop("VendorSignOffByName", None)

        approved_by_name = d.pop("ApprovedByName", None)

        accepted_by_name = d.pop("AcceptedByName", None)

        ready_for_quality_control_by_name = d.pop("ReadyForQualityControlByName", None)

        quality_control_by_name = d.pop("QualityControlByName", None)

        created_by_name = d.pop("CreatedByName", None)

        completed_by_name = d.pop("CompletedByName", None)

        shipped_by_name = d.pop("ShippedByName", None)

        delivered_by_name = d.pop("DeliveredByName", None)

        invoiced_by_name = d.pop("InvoicedByName", None)

        paid_by_name = d.pop("PaidByName", None)

        cancelled_by_name = d.pop("CancelledByName", None)

        closed_by_name = d.pop("ClosedByName", None)

        client_company_id = d.pop("ClientCompanyId", None)

        client_company_name = d.pop("ClientCompanyName", None)

        client_domain_name = d.pop("ClientDomainName", None)

        client_alternative_names = d.pop("ClientAlternativeNames", None)

        service_comments = d.pop("ServiceComments", None)

        service_private_comments = d.pop("ServicePrivateComments", None)

        def _parse_created_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_on_type_0 = isoparse(data)

                return created_on_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        created_on = _parse_created_on(d.pop("CreatedOn", None))

        def _parse_approved_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_on_type_0 = isoparse(data)

                return approved_on_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        approved_on = _parse_approved_on(d.pop("ApprovedOn", None))

        def _parse_sign_off_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sign_off_on_type_0 = isoparse(data)

                return sign_off_on_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        sign_off_on = _parse_sign_off_on(d.pop("SignOffOn", None))

        def _parse_vendor_sign_off_on(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                vendor_sign_off_on_type_0 = isoparse(data)

                return vendor_sign_off_on_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        vendor_sign_off_on = _parse_vendor_sign_off_on(d.pop("VendorSignOffOn", None))

        def _parse_completed_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_on_type_0 = isoparse(data)

                return completed_on_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        completed_on = _parse_completed_on(d.pop("CompletedOn", None))

        def _parse_submited_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                submited_on_type_0 = isoparse(data)

                return submited_on_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        submited_on = _parse_submited_on(d.pop("SubmitedOn", None))

        def _parse_shipped_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shipped_on_type_0 = isoparse(data)

                return shipped_on_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        shipped_on = _parse_shipped_on(d.pop("ShippedOn", None))

        def _parse_accepted_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                accepted_on_type_0 = isoparse(data)

                return accepted_on_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        accepted_on = _parse_accepted_on(d.pop("AcceptedOn", None))

        def _parse_ready_for_quality_control_on(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ready_for_quality_control_on_type_0 = isoparse(data)

                return ready_for_quality_control_on_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        ready_for_quality_control_on = _parse_ready_for_quality_control_on(
            d.pop("ReadyForQualityControlOn", None)
        )

        def _parse_quality_control_on(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                quality_control_on_type_0 = isoparse(data)

                return quality_control_on_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        quality_control_on = _parse_quality_control_on(d.pop("QualityControlOn", None))

        def _parse_delivered_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delivered_on_type_0 = isoparse(data)

                return delivered_on_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        delivered_on = _parse_delivered_on(d.pop("DeliveredOn", None))

        def _parse_invoiced_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                invoiced_on_type_0 = isoparse(data)

                return invoiced_on_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        invoiced_on = _parse_invoiced_on(d.pop("InvoicedOn", None))

        def _parse_last_invoiced_on(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_invoiced_on_type_0 = isoparse(data)

                return last_invoiced_on_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        last_invoiced_on = _parse_last_invoiced_on(d.pop("LastInvoicedOn", None))

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
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        payment_due_on = _parse_payment_due_on(d.pop("PaymentDueOn", None))

        def _parse_paid_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                paid_on_type_0 = isoparse(data)

                return paid_on_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        paid_on = _parse_paid_on(d.pop("PaidOn", None))

        def _parse_late_fee_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                late_fee_on_type_0 = isoparse(data)

                return late_fee_on_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        late_fee_on = _parse_late_fee_on(d.pop("LateFeeOn", None))

        def _parse_cancelled_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cancelled_on_type_0 = isoparse(data)

                return cancelled_on_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        cancelled_on = _parse_cancelled_on(d.pop("CancelledOn", None))

        def _parse_closed_on(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closed_on_type_0 = isoparse(data)

                return closed_on_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        closed_on = _parse_closed_on(d.pop("ClosedOn", None))

        _last_updated_on = d.pop("LastUpdatedOn", None)
        last_updated_on: Optional[datetime.datetime]
        if not _last_updated_on:
            last_updated_on = None
        else:
            last_updated_on = isoparse(_last_updated_on)

        last_updated_by = d.pop("LastUpdatedBy", None)

        submited_by_id = d.pop("SubmitedById", None)

        sign_off_by_id = d.pop("SignOffById", None)

        vendor_sign_off_by_id = d.pop("VendorSignOffById", None)

        approved_by_id = d.pop("ApprovedById", None)

        late_fee_by_id = d.pop("LateFeeById", None)

        accepted_by_id = d.pop("AcceptedById", None)

        ready_for_quality_control_by_id = d.pop("ReadyForQualityControlById", None)

        quality_control_by_id = d.pop("QualityControlById", None)

        created_by_id = d.pop("CreatedById", None)

        completed_by_id = d.pop("CompletedById", None)

        shipped_by_id = d.pop("ShippedById", None)

        delivered_by_id = d.pop("DeliveredById", None)

        invoiced_by_id = d.pop("InvoicedById", None)

        paid_by_id = d.pop("PaidById", None)

        cancelled_by_id = d.pop("CancelledById", None)

        closed_by_id = d.pop("ClosedById", None)

        po_number = d.pop("PoNumber", None)

        secondary_po = d.pop("SecondaryPo", None)

        service_total = d.pop("ServiceTotal", None)

        repairs_total = d.pop("RepairsTotal", None)

        parts_total = d.pop("PartsTotal", None)

        parts_total_before_discount = d.pop("PartsTotalBeforeDiscount", None)

        parts_discount_total = d.pop("PartsDiscountTotal", None)

        effective_tax_rate = d.pop("EffectiveTaxRate", None)

        tax_amount = d.pop("TaxAmount", None)

        shipping_fee = d.pop("ShippingFee", None)

        travel_charge = d.pop("TravelCharge", None)

        late_fee = d.pop("LateFee", None)

        is_tax_exempt = d.pop("IsTaxExempt", None)

        service_discount = d.pop("ServiceDiscount", None)

        trade_in_credit = d.pop("TradeInCredit", None)

        prepaid_credit = d.pop("PrepaidCredit", None)

        grand_total = d.pop("GrandTotal", None)

        paid_amount = d.pop("PaidAmount", None)

        remaining_balance = d.pop("RemainingBalance", None)

        service_discount_details = d.pop("ServiceDiscountDetails", None)

        trade_in_credit_details = d.pop("TradeInCreditDetails", None)

        prepaid_credit_details = d.pop("PrepaidCreditDetails", None)

        payment_notes = d.pop("PaymentNotes", None)

        service_order_number = d.pop("ServiceOrderNumber", None)

        legacy_order_number = d.pop("LegacyOrderNumber", None)

        custom_order_number = d.pop("CustomOrderNumber", None)

        payment_status = d.pop("PaymentStatus", None)

        payment_option = d.pop("PaymentOption", None)

        shipment_status = d.pop("ShipmentStatus", None)

        order_status = d.pop("OrderStatus", None)

        owner_id = d.pop("OwnerId", None)

        owner_department = d.pop("OwnerDepartment", None)

        client_site = d.pop("ClientSite", None)

        client_site_code = d.pop("ClientSiteCode", None)

        vendor_site = d.pop("VendorSite", None)

        internal = d.pop("Internal", None)

        _guid = d.pop("Guid", None)
        guid: Optional[UUID]
        if not _guid:
            guid = None
        else:
            guid = UUID(_guid)

        def _parse_business_from_time(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                business_from_time_type_0 = isoparse(data)

                return business_from_time_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        business_from_time = _parse_business_from_time(d.pop("BusinessFromTime", None))

        def _parse_business_to_time(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                business_to_time_type_0 = isoparse(data)

                return business_to_time_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        business_to_time = _parse_business_to_time(d.pop("BusinessToTime", None))

        site_access_notes = d.pop("SiteAccessNotes", None)

        def _parse_desired_date(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                desired_date_type_0 = isoparse(data)

                return desired_date_type_0
            except:  # noqa: E722
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
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        deadline_date = _parse_deadline_date(d.pop("DeadlineDate", None))

        def _parse_request_from_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                request_from_date_type_0 = isoparse(data)

                return request_from_date_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        request_from_date = _parse_request_from_date(d.pop("RequestFromDate", None))

        def _parse_request_from_time(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                request_from_time_type_0 = isoparse(data)

                return request_from_time_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        request_from_time = _parse_request_from_time(d.pop("RequestFromTime", None))

        def _parse_request_to_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                request_to_date_type_0 = isoparse(data)

                return request_to_date_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        request_to_date = _parse_request_to_date(d.pop("RequestToDate", None))

        def _parse_request_to_time(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                request_to_time_type_0 = isoparse(data)

                return request_to_time_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        request_to_time = _parse_request_to_time(d.pop("RequestToTime", None))

        order_notes = d.pop("OrderNotes", None)

        def _parse_billing_address(
            data: object,
        ) -> Union[
            "QualerApiModelsServiceOrdersToClientOrderResponseModelBillingAddressType0",
            None,
            None,
        ]:
            if not data:
                return None
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
                    None,
                ],
                data,
            )

        billing_address = _parse_billing_address(d.pop("BillingAddress", None))

        def _parse_shipping_address(
            data: object,
        ) -> Union[
            "QualerApiModelsServiceOrdersToClientOrderResponseModelShippingAddressType0",
            None,
            None,
        ]:
            if not data:
                return None
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
                    None,
                ],
                data,
            )

        shipping_address = _parse_shipping_address(d.pop("ShippingAddress", None))

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

        qualer_api_models_service_orders_to_client_order_response_model.additional_properties = d
        return qualer_api_models_service_orders_to_client_order_response_model

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
