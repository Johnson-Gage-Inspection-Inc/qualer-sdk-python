import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.qualer_api_models_attributes_to_attribute_response import (
        AttributesToAttributeResponse,
    )
    from ..models.qualer_api_models_clients_to_client_company_response_model_billing_address_type_0 import (
        ClientsToClientCompanyResponseModelBillingAddressType0,
    )
    from ..models.qualer_api_models_clients_to_client_company_response_model_shipping_address_type_0 import (
        ClientsToClientCompanyResponseModelShippingAddressType0,
    )


T = TypeVar("T", bound="ClientsToClientCompanyResponseModel")


@_attrs_define
class ClientsToClientCompanyResponseModel:
    """
    Attributes:
        company_id (Optional[int]):
        account_number_text (Optional[str]):
        account_number (Optional[int]):
        currency_id (Optional[int]):
        client_status (Optional[str]):
        company_name (Optional[str]):
        company_description (Optional[str]):
        domain_name (Optional[str]):
        custom_client_name (Optional[str]):
        legacy_id (Optional[str]):
        updated_on_utc (Optional[datetime.datetime]):
        account_representative_employee_id (Optional[int]):
        account_representative_site_id (Optional[int]):
        account_manager_employee_id (Optional[int]):
        billing_address (Optional['ClientsToClientCompanyResponseModelBillingAddressType0']):
        shipping_address (Optional['ClientsToClientCompanyResponseModelShippingAddressType0']):
        attributes (Optional[List['AttributesToAttributeResponse']]):
    """

    company_id: Optional[int] = None
    account_number_text: Optional[str] = None
    account_number: Optional[int] = None
    currency_id: Optional[int] = None
    client_status: Optional[str] = None
    company_name: Optional[str] = None
    company_description: Optional[str] = None
    domain_name: Optional[str] = None
    custom_client_name: Optional[str] = None
    legacy_id: Optional[str] = None
    updated_on_utc: Optional[datetime.datetime] = None
    account_representative_employee_id: Optional[int] = None
    account_representative_site_id: Optional[int] = None
    account_manager_employee_id: Optional[int] = None
    billing_address: Optional["ClientsToClientCompanyResponseModelBillingAddressType0"] = None
    shipping_address: Optional["ClientsToClientCompanyResponseModelShippingAddressType0"] = None
    attributes: Optional[List["AttributesToAttributeResponse"]] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.qualer_api_models_clients_to_client_company_response_model_billing_address_type_0 import (
            ClientsToClientCompanyResponseModelBillingAddressType0,
        )
        from ..models.qualer_api_models_clients_to_client_company_response_model_shipping_address_type_0 import (
            ClientsToClientCompanyResponseModelShippingAddressType0,
        )

        company_id = self.company_id

        account_number_text = self.account_number_text

        account_number = self.account_number

        currency_id = self.currency_id

        client_status = self.client_status

        company_name = self.company_name

        company_description = self.company_description

        domain_name = self.domain_name

        custom_client_name = self.custom_client_name

        legacy_id = self.legacy_id

        updated_on_utc: Optional[str] = None
        if self.updated_on_utc:
            updated_on_utc = self.updated_on_utc.isoformat()

        account_representative_employee_id = self.account_representative_employee_id

        account_representative_site_id = self.account_representative_site_id

        account_manager_employee_id = self.account_manager_employee_id

        billing_address: Optional[Dict[str, Any]]
        if not self.billing_address:
            billing_address = None
        elif isinstance(
            self.billing_address,
            ClientsToClientCompanyResponseModelBillingAddressType0,
        ):
            billing_address = self.billing_address.to_dict()
        else:
            billing_address = self.billing_address

        shipping_address: Optional[Dict[str, Any]]
        if not self.shipping_address:
            shipping_address = None
        elif isinstance(
            self.shipping_address,
            ClientsToClientCompanyResponseModelShippingAddressType0,
        ):
            shipping_address = self.shipping_address.to_dict()
        else:
            shipping_address = self.shipping_address

        attributes: Optional[List[Dict[str, Any]]] = None
        if self.attributes:
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()
                attributes.append(attributes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_id is not None:
            field_dict["CompanyId"] = company_id
        if account_number_text is not None:
            field_dict["AccountNumberText"] = account_number_text
        if account_number is not None:
            field_dict["AccountNumber"] = account_number
        if currency_id is not None:
            field_dict["CurrencyId"] = currency_id
        if client_status is not None:
            field_dict["ClientStatus"] = client_status
        if company_name is not None:
            field_dict["CompanyName"] = company_name
        if company_description is not None:
            field_dict["CompanyDescription"] = company_description
        if domain_name is not None:
            field_dict["DomainName"] = domain_name
        if custom_client_name is not None:
            field_dict["CustomClientName"] = custom_client_name
        if legacy_id is not None:
            field_dict["LegacyId"] = legacy_id
        if updated_on_utc is not None:
            field_dict["UpdatedOnUtc"] = updated_on_utc
        if account_representative_employee_id is not None:
            field_dict["AccountRepresentativeEmployeeId"] = account_representative_employee_id
        if account_representative_site_id is not None:
            field_dict["AccountRepresentativeSiteId"] = account_representative_site_id
        if account_manager_employee_id is not None:
            field_dict["AccountManagerEmployeeId"] = account_manager_employee_id
        if billing_address is not None:
            field_dict["BillingAddress"] = billing_address
        if shipping_address is not None:
            field_dict["ShippingAddress"] = shipping_address
        if attributes is not None:
            field_dict["Attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_attributes_to_attribute_response import (
            AttributesToAttributeResponse,
        )
        from ..models.qualer_api_models_clients_to_client_company_response_model_billing_address_type_0 import (
            ClientsToClientCompanyResponseModelBillingAddressType0,
        )
        from ..models.qualer_api_models_clients_to_client_company_response_model_shipping_address_type_0 import (
            ClientsToClientCompanyResponseModelShippingAddressType0,
        )

        d = dict(src_dict)
        company_id = d.pop("CompanyId", None)

        account_number_text = d.pop("AccountNumberText", None)

        account_number = d.pop("AccountNumber", None)

        currency_id = d.pop("CurrencyId", None)

        client_status = d.pop("ClientStatus", None)

        company_name = d.pop("CompanyName", None)

        company_description = d.pop("CompanyDescription", None)

        domain_name = d.pop("DomainName", None)

        custom_client_name = d.pop("CustomClientName", None)

        legacy_id = d.pop("LegacyId", None)

        _updated_on_utc = d.pop("UpdatedOnUtc", None)
        updated_on_utc: Optional[datetime.datetime]
        if not _updated_on_utc:
            updated_on_utc = None
        else:
            updated_on_utc = isoparse(_updated_on_utc)

        account_representative_employee_id = d.pop("AccountRepresentativeEmployeeId", None)

        account_representative_site_id = d.pop("AccountRepresentativeSiteId", None)

        account_manager_employee_id = d.pop("AccountManagerEmployeeId", None)

        def _parse_billing_address(
            data: object,
        ) -> Optional["ClientsToClientCompanyResponseModelBillingAddressType0"]:
            if not data:
                return None
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                billing_address_type_0 = (
                    ClientsToClientCompanyResponseModelBillingAddressType0.from_dict(data)
                )

                return billing_address_type_0
            except Exception:
                pass
            return cast(
                Optional["ClientsToClientCompanyResponseModelBillingAddressType0"],
                data,
            )

        billing_address = _parse_billing_address(d.pop("BillingAddress", None))

        def _parse_shipping_address(
            data: object,
        ) -> Optional["ClientsToClientCompanyResponseModelShippingAddressType0"]:
            if not data:
                return None
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                shipping_address_type_0 = (
                    ClientsToClientCompanyResponseModelShippingAddressType0.from_dict(data)
                )

                return shipping_address_type_0
            except Exception:
                pass
            return cast(
                Optional["ClientsToClientCompanyResponseModelShippingAddressType0"],
                data,
            )

        shipping_address = _parse_shipping_address(d.pop("ShippingAddress", None))

        attributes = []
        _attributes = d.pop("Attributes", None)
        for attributes_item_data in _attributes or []:
            attributes_item = AttributesToAttributeResponse.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        qualer_api_models_clients_to_client_company_response_model = cls(
            company_id=company_id,
            account_number_text=account_number_text,
            account_number=account_number,
            currency_id=currency_id,
            client_status=client_status,
            company_name=company_name,
            company_description=company_description,
            domain_name=domain_name,
            custom_client_name=custom_client_name,
            legacy_id=legacy_id,
            updated_on_utc=updated_on_utc,
            account_representative_employee_id=account_representative_employee_id,
            account_representative_site_id=account_representative_site_id,
            account_manager_employee_id=account_manager_employee_id,
            billing_address=billing_address,
            shipping_address=shipping_address,
            attributes=attributes,
        )

        qualer_api_models_clients_to_client_company_response_model.additional_properties = d
        return qualer_api_models_clients_to_client_company_response_model

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
