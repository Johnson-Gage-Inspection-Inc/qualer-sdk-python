from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.qualer_api_models_address_address_model import AddressAddressModel


T = TypeVar("T", bound="VendorsFromSponsoredVendorCreateModel")


@_attrs_define
class VendorsFromSponsoredVendorCreateModel:
    """
    Attributes:
        account_number_text (Optional[str]):
        domain_name (Optional[str]):
        custom_vendor_name (Optional[str]):
        currency_id (Optional[int]):
        company_name (Optional[str]):
        billing_address (Optional[AddressAddressModel]):
        shipping_address (Optional[AddressAddressModel]):
    """

    account_number_text: Optional[str] = None
    domain_name: Optional[str] = None
    custom_vendor_name: Optional[str] = None
    currency_id: Optional[int] = None
    company_name: Optional[str] = None
    billing_address: Optional["AddressAddressModel"] = None
    shipping_address: Optional["AddressAddressModel"] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_number_text = self.account_number_text
        domain_name = self.domain_name
        custom_vendor_name = self.custom_vendor_name
        currency_id = self.currency_id
        company_name = self.company_name
        billing_address: Optional[Dict[str, Any]] = None
        if self.billing_address:
            billing_address = self.billing_address.to_dict()
        shipping_address: Optional[Dict[str, Any]] = None
        if self.shipping_address:
            shipping_address = self.shipping_address.to_dict()
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_number_text is not None:
            field_dict["AccountNumberText"] = account_number_text
        if domain_name is not None:
            field_dict["DomainName"] = domain_name
        if custom_vendor_name is not None:
            field_dict["CustomVendorName"] = custom_vendor_name
        if currency_id is not None:
            field_dict["CurrencyId"] = currency_id
        if company_name is not None:
            field_dict["CompanyName"] = company_name
        if billing_address is not None:
            field_dict["BillingAddress"] = billing_address
        if shipping_address is not None:
            field_dict["ShippingAddress"] = shipping_address
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_address_address_model import (
            AddressAddressModel,
        )

        d = dict(src_dict)
        account_number_text = d.pop("AccountNumberText", None)
        domain_name = d.pop("DomainName", None)
        custom_vendor_name = d.pop("CustomVendorName", None)
        currency_id = d.pop("CurrencyId", None)
        company_name = d.pop("CompanyName", None)
        _billing_address = d.pop("BillingAddress", None)
        billing_address: Optional[AddressAddressModel]
        if not _billing_address:
            billing_address = None
        else:
            billing_address = AddressAddressModel.from_dict(_billing_address)
        _shipping_address = d.pop("ShippingAddress", None)
        shipping_address: Optional[AddressAddressModel]
        if not _shipping_address:
            shipping_address = None
        else:
            shipping_address = AddressAddressModel.from_dict(_shipping_address)
        qualer_api_models_vendors_from_sponsored_vendor_create_model = cls(
            account_number_text=account_number_text,
            domain_name=domain_name,
            custom_vendor_name=custom_vendor_name,
            currency_id=currency_id,
            company_name=company_name,
            billing_address=billing_address,
            shipping_address=shipping_address,
        )
        qualer_api_models_vendors_from_sponsored_vendor_create_model.additional_properties = d
        return qualer_api_models_vendors_from_sponsored_vendor_create_model

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
