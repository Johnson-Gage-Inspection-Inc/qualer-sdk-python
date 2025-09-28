import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.qualer_api_models_vendors_to_vendor_company_response_model_billing_address_type_0 import (
        VendorsToVendorCompanyResponseModelBillingAddressType0,
    )
    from ..models.qualer_api_models_vendors_to_vendor_company_response_model_shipping_address_type_0 import (
        VendorsToVendorCompanyResponseModelShippingAddressType0,
    )


T = TypeVar("T", bound="VendorsToVendorCompanyResponseModel")


@_attrs_define
class VendorsToVendorCompanyResponseModel:
    """
    Attributes:
        account_number_text (Optional[str]):
        account_number (Optional[int]):
        currency_id (Optional[int]):
        company_id (Optional[int]):
        company_name (Optional[str]):
        domain_name (Optional[str]):
        custom_name (Optional[str]):
        billing_address (Optional['VendorsToVendorCompanyResponseModelBillingAddressType0']):
        shipping_address (Optional['VendorsToVendorCompanyResponseModelShippingAddressType0']):
        updated_on_utc (Optional[datetime.datetime]):
    """

    account_number_text: Optional[str] = None
    account_number: Optional[int] = None
    currency_id: Optional[int] = None
    company_id: Optional[int] = None
    company_name: Optional[str] = None
    domain_name: Optional[str] = None
    custom_name: Optional[str] = None
    billing_address: Optional["VendorsToVendorCompanyResponseModelBillingAddressType0"] = None
    shipping_address: Optional["VendorsToVendorCompanyResponseModelShippingAddressType0"] = None
    updated_on_utc: Optional[datetime.datetime] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.qualer_api_models_vendors_to_vendor_company_response_model_billing_address_type_0 import (
            VendorsToVendorCompanyResponseModelBillingAddressType0,
        )
        from ..models.qualer_api_models_vendors_to_vendor_company_response_model_shipping_address_type_0 import (
            VendorsToVendorCompanyResponseModelShippingAddressType0,
        )
        account_number_text = self.account_number_text
        account_number = self.account_number
        currency_id = self.currency_id
        company_id = self.company_id
        company_name = self.company_name
        domain_name = self.domain_name
        custom_name = self.custom_name
        billing_address: Optional[Dict[str, Any]]
        if not self.billing_address:
            billing_address = None
        elif isinstance(
            self.billing_address,
            VendorsToVendorCompanyResponseModelBillingAddressType0,
        ):
            billing_address = self.billing_address.to_dict()
        else:
            billing_address = self.billing_address
        shipping_address: Optional[Dict[str, Any]]
        if not self.shipping_address:
            shipping_address = None
        elif isinstance(
            self.shipping_address,
            VendorsToVendorCompanyResponseModelShippingAddressType0,
        ):
            shipping_address = self.shipping_address.to_dict()
        else:
            shipping_address = self.shipping_address
        updated_on_utc: Optional[str] = None
        if self.updated_on_utc:
            updated_on_utc = self.updated_on_utc.isoformat()
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_number_text is not None:
            field_dict["AccountNumberText"] = account_number_text
        if account_number is not None:
            field_dict["AccountNumber"] = account_number
        if currency_id is not None:
            field_dict["CurrencyId"] = currency_id
        if company_id is not None:
            field_dict["CompanyId"] = company_id
        if company_name is not None:
            field_dict["CompanyName"] = company_name
        if domain_name is not None:
            field_dict["DomainName"] = domain_name
        if custom_name is not None:
            field_dict["CustomName"] = custom_name
        if billing_address is not None:
            field_dict["BillingAddress"] = billing_address
        if shipping_address is not None:
            field_dict["ShippingAddress"] = shipping_address
        if updated_on_utc is not None:
            field_dict["UpdatedOnUtc"] = updated_on_utc
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_vendors_to_vendor_company_response_model_billing_address_type_0 import (
            VendorsToVendorCompanyResponseModelBillingAddressType0,
        )
        from ..models.qualer_api_models_vendors_to_vendor_company_response_model_shipping_address_type_0 import (
            VendorsToVendorCompanyResponseModelShippingAddressType0,
        )
        d = dict(src_dict)
        account_number_text = d.pop("AccountNumberText", None)
        account_number = d.pop("AccountNumber", None)
        currency_id = d.pop("CurrencyId", None)
        company_id = d.pop("CompanyId", None)
        company_name = d.pop("CompanyName", None)
        domain_name = d.pop("DomainName", None)
        custom_name = d.pop("CustomName", None)
        def _parse_billing_address(
            data: object,
        ) -> Optional["VendorsToVendorCompanyResponseModelBillingAddressType0"]:
            if not data:
                return None
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                billing_address_type_0 = (
                    VendorsToVendorCompanyResponseModelBillingAddressType0.from_dict(data)
                )
                return billing_address_type_0
            except Exception:
                pass
            return cast(
                Optional["VendorsToVendorCompanyResponseModelBillingAddressType0"],
                data,
            )
        billing_address = _parse_billing_address(d.pop("BillingAddress", None))
        def _parse_shipping_address(
            data: object,
        ) -> Optional["VendorsToVendorCompanyResponseModelShippingAddressType0"]:
            if not data:
                return None
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                shipping_address_type_0 = (
                    VendorsToVendorCompanyResponseModelShippingAddressType0.from_dict(data)
                )
                return shipping_address_type_0
            except Exception:
                pass
            return cast(
                Optional["VendorsToVendorCompanyResponseModelShippingAddressType0"],
                data,
            )
        shipping_address = _parse_shipping_address(d.pop("ShippingAddress", None))
        _updated_on_utc = d.pop("UpdatedOnUtc", None)
        updated_on_utc: Optional[datetime.datetime]
        if not _updated_on_utc:
            updated_on_utc = None
        else:
            updated_on_utc = isoparse(_updated_on_utc)
        qualer_api_models_vendors_to_vendor_company_response_model = cls(
            account_number_text=account_number_text,
            account_number=account_number,
            currency_id=currency_id,
            company_id=company_id,
            company_name=company_name,
            domain_name=domain_name,
            custom_name=custom_name,
            billing_address=billing_address,
            shipping_address=shipping_address,
            updated_on_utc=updated_on_utc,
        )
        qualer_api_models_vendors_to_vendor_company_response_model.additional_properties = d
        return qualer_api_models_vendors_to_vendor_company_response_model

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
