from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualer_api_models_address_address_model import (
        QualerApiModelsAddressAddressModel,
    )


T = TypeVar("T", bound="QualerApiModelsVendorsFromSponsoredVendorCreateModel")


@_attrs_define
class QualerApiModelsVendorsFromSponsoredVendorCreateModel:
    """
    Attributes:
        account_number_text (Union[None, Unset, str]):
        domain_name (Union[None, Unset, str]):
        custom_vendor_name (Union[None, Unset, str]):
        currency_id (Union[None, Unset, int]):
        company_name (Union[None, Unset, str]):
        billing_address (Union[None, Unset, QualerApiModelsAddressAddressModel]):
        shipping_address (Union[None, Unset, QualerApiModelsAddressAddressModel]):
    """

    account_number_text: Union[None, Unset, str] = UNSET
    domain_name: Union[None, Unset, str] = UNSET
    custom_vendor_name: Union[None, Unset, str] = UNSET
    currency_id: Union[None, Unset, int] = UNSET
    company_name: Union[None, Unset, str] = UNSET
    billing_address: Union[None, Unset, "QualerApiModelsAddressAddressModel"] = UNSET
    shipping_address: Union[None, Unset, "QualerApiModelsAddressAddressModel"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_number_text = self.account_number_text

        domain_name = self.domain_name

        custom_vendor_name = self.custom_vendor_name

        currency_id = self.currency_id

        company_name = self.company_name

        billing_address: Union[None, Unset, dict[str, Any]] = UNSET
        if self.billing_address and not isinstance(self.billing_address, Unset):
            billing_address = self.billing_address.to_dict()

        shipping_address: Union[None, Unset, dict[str, Any]] = UNSET
        if self.shipping_address and not isinstance(self.shipping_address, Unset):
            shipping_address = self.shipping_address.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_number_text is not UNSET:
            field_dict["AccountNumberText"] = account_number_text
        if domain_name is not UNSET:
            field_dict["DomainName"] = domain_name
        if custom_vendor_name is not UNSET:
            field_dict["CustomVendorName"] = custom_vendor_name
        if currency_id is not UNSET:
            field_dict["CurrencyId"] = currency_id
        if company_name is not UNSET:
            field_dict["CompanyName"] = company_name
        if billing_address is not UNSET:
            field_dict["BillingAddress"] = billing_address
        if shipping_address is not UNSET:
            field_dict["ShippingAddress"] = shipping_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_address_address_model import (
            QualerApiModelsAddressAddressModel,
        )

        d = dict(src_dict)
        account_number_text = d.pop("AccountNumberText", UNSET)

        domain_name = d.pop("DomainName", UNSET)

        custom_vendor_name = d.pop("CustomVendorName", UNSET)

        currency_id = d.pop("CurrencyId", UNSET)

        company_name = d.pop("CompanyName", UNSET)

        _billing_address = d.pop("BillingAddress", UNSET)
        billing_address: Union[None, Unset, QualerApiModelsAddressAddressModel]
        if isinstance(_billing_address, Unset):
            billing_address = UNSET
        else:
            billing_address = QualerApiModelsAddressAddressModel.from_dict(
                _billing_address
            )

        _shipping_address = d.pop("ShippingAddress", UNSET)
        shipping_address: Union[None, Unset, QualerApiModelsAddressAddressModel]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = QualerApiModelsAddressAddressModel.from_dict(
                _shipping_address
            )

        qualer_api_models_vendors_from_sponsored_vendor_create_model = cls(
            account_number_text=account_number_text,
            domain_name=domain_name,
            custom_vendor_name=custom_vendor_name,
            currency_id=currency_id,
            company_name=company_name,
            billing_address=billing_address,
            shipping_address=shipping_address,
        )

        qualer_api_models_vendors_from_sponsored_vendor_create_model.additional_properties = (
            d
        )
        return qualer_api_models_vendors_from_sponsored_vendor_create_model

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
