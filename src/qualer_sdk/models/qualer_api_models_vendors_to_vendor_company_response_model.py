import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualer_api_models_vendors_to_vendor_company_response_model_billing_address_type_0 import (
        QualerApiModelsVendorsToVendorCompanyResponseModelBillingAddressType0,
    )
    from ..models.qualer_api_models_vendors_to_vendor_company_response_model_shipping_address_type_0 import (
        QualerApiModelsVendorsToVendorCompanyResponseModelShippingAddressType0,
    )


T = TypeVar("T", bound="QualerApiModelsVendorsToVendorCompanyResponseModel")


@_attrs_define
class QualerApiModelsVendorsToVendorCompanyResponseModel:
    """
    Attributes:
        account_number_text (Union[Unset, str]):
        account_number (Union[Unset, int]):
        currency_id (Union[Unset, int]):
        company_id (Union[Unset, int]):
        company_name (Union[Unset, str]):
        domain_name (Union[Unset, str]):
        custom_name (Union[Unset, str]):
        billing_address (Union['QualerApiModelsVendorsToVendorCompanyResponseModelBillingAddressType0', None, Unset]):
        shipping_address (Union['QualerApiModelsVendorsToVendorCompanyResponseModelShippingAddressType0', None, Unset]):
        updated_on_utc (Union[Unset, datetime.datetime]):
    """

    account_number_text: Union[Unset, str] = UNSET
    account_number: Union[Unset, int] = UNSET
    currency_id: Union[Unset, int] = UNSET
    company_id: Union[Unset, int] = UNSET
    company_name: Union[Unset, str] = UNSET
    domain_name: Union[Unset, str] = UNSET
    custom_name: Union[Unset, str] = UNSET
    billing_address: Union[
        "QualerApiModelsVendorsToVendorCompanyResponseModelBillingAddressType0",
        None,
        Unset,
    ] = UNSET
    shipping_address: Union[
        "QualerApiModelsVendorsToVendorCompanyResponseModelShippingAddressType0",
        None,
        Unset,
    ] = UNSET
    updated_on_utc: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.qualer_api_models_vendors_to_vendor_company_response_model_billing_address_type_0 import (
            QualerApiModelsVendorsToVendorCompanyResponseModelBillingAddressType0,
        )
        from ..models.qualer_api_models_vendors_to_vendor_company_response_model_shipping_address_type_0 import (
            QualerApiModelsVendorsToVendorCompanyResponseModelShippingAddressType0,
        )

        account_number_text = self.account_number_text

        account_number = self.account_number

        currency_id = self.currency_id

        company_id = self.company_id

        company_name = self.company_name

        domain_name = self.domain_name

        custom_name = self.custom_name

        billing_address: Union[None, Unset, dict[str, Any]]
        if isinstance(self.billing_address, Unset):
            billing_address = UNSET
        elif isinstance(
            self.billing_address,
            QualerApiModelsVendorsToVendorCompanyResponseModelBillingAddressType0,
        ):
            billing_address = self.billing_address.to_dict()
        else:
            billing_address = self.billing_address

        shipping_address: Union[None, Unset, dict[str, Any]]
        if isinstance(self.shipping_address, Unset):
            shipping_address = UNSET
        elif isinstance(
            self.shipping_address,
            QualerApiModelsVendorsToVendorCompanyResponseModelShippingAddressType0,
        ):
            shipping_address = self.shipping_address.to_dict()
        else:
            shipping_address = self.shipping_address

        updated_on_utc: Union[Unset, str] = UNSET
        if self.updated_on_utc and not isinstance(self.updated_on_utc, Unset):
            updated_on_utc = self.updated_on_utc.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_number_text is not UNSET:
            field_dict["AccountNumberText"] = account_number_text
        if account_number is not UNSET:
            field_dict["AccountNumber"] = account_number
        if currency_id is not UNSET:
            field_dict["CurrencyId"] = currency_id
        if company_id is not UNSET:
            field_dict["CompanyId"] = company_id
        if company_name is not UNSET:
            field_dict["CompanyName"] = company_name
        if domain_name is not UNSET:
            field_dict["DomainName"] = domain_name
        if custom_name is not UNSET:
            field_dict["CustomName"] = custom_name
        if billing_address is not UNSET:
            field_dict["BillingAddress"] = billing_address
        if shipping_address is not UNSET:
            field_dict["ShippingAddress"] = shipping_address
        if updated_on_utc is not UNSET:
            field_dict["UpdatedOnUtc"] = updated_on_utc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_vendors_to_vendor_company_response_model_billing_address_type_0 import (
            QualerApiModelsVendorsToVendorCompanyResponseModelBillingAddressType0,
        )
        from ..models.qualer_api_models_vendors_to_vendor_company_response_model_shipping_address_type_0 import (
            QualerApiModelsVendorsToVendorCompanyResponseModelShippingAddressType0,
        )

        d = dict(src_dict)
        account_number_text = d.pop("AccountNumberText", UNSET)

        account_number = d.pop("AccountNumber", UNSET)

        currency_id = d.pop("CurrencyId", UNSET)

        company_id = d.pop("CompanyId", UNSET)

        company_name = d.pop("CompanyName", UNSET)

        domain_name = d.pop("DomainName", UNSET)

        custom_name = d.pop("CustomName", UNSET)

        def _parse_billing_address(
            data: object,
        ) -> Union[
            "QualerApiModelsVendorsToVendorCompanyResponseModelBillingAddressType0",
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
                billing_address_type_0 = QualerApiModelsVendorsToVendorCompanyResponseModelBillingAddressType0.from_dict(
                    data
                )

                return billing_address_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    "QualerApiModelsVendorsToVendorCompanyResponseModelBillingAddressType0",
                    None,
                    Unset,
                ],
                data,
            )

        billing_address = _parse_billing_address(d.pop("BillingAddress", UNSET))

        def _parse_shipping_address(
            data: object,
        ) -> Union[
            "QualerApiModelsVendorsToVendorCompanyResponseModelShippingAddressType0",
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
                shipping_address_type_0 = QualerApiModelsVendorsToVendorCompanyResponseModelShippingAddressType0.from_dict(
                    data
                )

                return shipping_address_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    "QualerApiModelsVendorsToVendorCompanyResponseModelShippingAddressType0",
                    None,
                    Unset,
                ],
                data,
            )

        shipping_address = _parse_shipping_address(d.pop("ShippingAddress", UNSET))

        _updated_on_utc = d.pop("UpdatedOnUtc", UNSET)
        updated_on_utc: Union[Unset, datetime.datetime]
        if isinstance(_updated_on_utc, Unset):
            updated_on_utc = UNSET
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

        qualer_api_models_vendors_to_vendor_company_response_model.additional_properties = (
            d
        )
        return qualer_api_models_vendors_to_vendor_company_response_model

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
