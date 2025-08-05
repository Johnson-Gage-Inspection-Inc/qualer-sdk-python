import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualer_api_models_attributes_to_attribute_response import (
        QualerApiModelsAttributesToAttributeResponse,
    )
    from ..models.qualer_api_models_clients_to_client_company_response_model_billing_address_type_0 import (
        QualerApiModelsClientsToClientCompanyResponseModelBillingAddressType0,
    )
    from ..models.qualer_api_models_clients_to_client_company_response_model_shipping_address_type_0 import (
        QualerApiModelsClientsToClientCompanyResponseModelShippingAddressType0,
    )


T = TypeVar("T", bound="QualerApiModelsClientsToClientCompanyResponseModel")


@_attrs_define
class QualerApiModelsClientsToClientCompanyResponseModel:
    """
    Attributes:
        company_id (Union[Unset, int]):
        account_number_text (Union[Unset, str]):
        account_number (Union[Unset, int]):
        currency_id (Union[Unset, int]):
        client_status (Union[Unset, str]):
        company_name (Union[Unset, str]):
        company_description (Union[Unset, str]):
        domain_name (Union[Unset, str]):
        custom_client_name (Union[Unset, str]):
        legacy_id (Union[Unset, str]):
        updated_on_utc (Union[Unset, datetime.datetime]):
        account_representative_employee_id (Union[Unset, int]):
        account_representative_site_id (Union[Unset, int]):
        account_manager_employee_id (Union[Unset, int]):
        billing_address (Union['QualerApiModelsClientsToClientCompanyResponseModelBillingAddressType0', None, Unset]):
        shipping_address (Union['QualerApiModelsClientsToClientCompanyResponseModelShippingAddressType0', None, Unset]):
        attributes (Union[Unset, list['QualerApiModelsAttributesToAttributeResponse']]):
    """

    company_id: Union[Unset, int] = UNSET
    account_number_text: Union[Unset, str] = UNSET
    account_number: Union[Unset, int] = UNSET
    currency_id: Union[Unset, int] = UNSET
    client_status: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    company_description: Union[Unset, str] = UNSET
    domain_name: Union[Unset, str] = UNSET
    custom_client_name: Union[Unset, str] = UNSET
    legacy_id: Union[Unset, str] = UNSET
    updated_on_utc: Union[Unset, datetime.datetime] = UNSET
    account_representative_employee_id: Union[Unset, int] = UNSET
    account_representative_site_id: Union[Unset, int] = UNSET
    account_manager_employee_id: Union[Unset, int] = UNSET
    billing_address: Union[
        "QualerApiModelsClientsToClientCompanyResponseModelBillingAddressType0",
        None,
        Unset,
    ] = UNSET
    shipping_address: Union[
        "QualerApiModelsClientsToClientCompanyResponseModelShippingAddressType0",
        None,
        Unset,
    ] = UNSET
    attributes: Union[Unset, list["QualerApiModelsAttributesToAttributeResponse"]] = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.qualer_api_models_clients_to_client_company_response_model_billing_address_type_0 import (
            QualerApiModelsClientsToClientCompanyResponseModelBillingAddressType0,
        )
        from ..models.qualer_api_models_clients_to_client_company_response_model_shipping_address_type_0 import (
            QualerApiModelsClientsToClientCompanyResponseModelShippingAddressType0,
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

        updated_on_utc: Union[Unset, str] = UNSET
        if not isinstance(self.updated_on_utc, Unset):
            updated_on_utc = self.updated_on_utc.isoformat()

        account_representative_employee_id = self.account_representative_employee_id

        account_representative_site_id = self.account_representative_site_id

        account_manager_employee_id = self.account_manager_employee_id

        billing_address: Union[None, Unset, dict[str, Any]]
        if isinstance(self.billing_address, Unset):
            billing_address = UNSET
        elif isinstance(
            self.billing_address,
            QualerApiModelsClientsToClientCompanyResponseModelBillingAddressType0,
        ):
            billing_address = self.billing_address.to_dict()
        else:
            billing_address = self.billing_address

        shipping_address: Union[None, Unset, dict[str, Any]]
        if isinstance(self.shipping_address, Unset):
            shipping_address = UNSET
        elif isinstance(
            self.shipping_address,
            QualerApiModelsClientsToClientCompanyResponseModelShippingAddressType0,
        ):
            shipping_address = self.shipping_address.to_dict()
        else:
            shipping_address = self.shipping_address

        attributes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()
                attributes.append(attributes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_id is not UNSET:
            field_dict["CompanyId"] = company_id
        if account_number_text is not UNSET:
            field_dict["AccountNumberText"] = account_number_text
        if account_number is not UNSET:
            field_dict["AccountNumber"] = account_number
        if currency_id is not UNSET:
            field_dict["CurrencyId"] = currency_id
        if client_status is not UNSET:
            field_dict["ClientStatus"] = client_status
        if company_name is not UNSET:
            field_dict["CompanyName"] = company_name
        if company_description is not UNSET:
            field_dict["CompanyDescription"] = company_description
        if domain_name is not UNSET:
            field_dict["DomainName"] = domain_name
        if custom_client_name is not UNSET:
            field_dict["CustomClientName"] = custom_client_name
        if legacy_id is not UNSET:
            field_dict["LegacyId"] = legacy_id
        if updated_on_utc is not UNSET:
            field_dict["UpdatedOnUtc"] = updated_on_utc
        if account_representative_employee_id is not UNSET:
            field_dict["AccountRepresentativeEmployeeId"] = (
                account_representative_employee_id
            )
        if account_representative_site_id is not UNSET:
            field_dict["AccountRepresentativeSiteId"] = account_representative_site_id
        if account_manager_employee_id is not UNSET:
            field_dict["AccountManagerEmployeeId"] = account_manager_employee_id
        if billing_address is not UNSET:
            field_dict["BillingAddress"] = billing_address
        if shipping_address is not UNSET:
            field_dict["ShippingAddress"] = shipping_address
        if attributes is not UNSET:
            field_dict["Attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_attributes_to_attribute_response import (
            QualerApiModelsAttributesToAttributeResponse,
        )
        from ..models.qualer_api_models_clients_to_client_company_response_model_billing_address_type_0 import (
            QualerApiModelsClientsToClientCompanyResponseModelBillingAddressType0,
        )
        from ..models.qualer_api_models_clients_to_client_company_response_model_shipping_address_type_0 import (
            QualerApiModelsClientsToClientCompanyResponseModelShippingAddressType0,
        )

        d = dict(src_dict)
        company_id = d.pop("CompanyId", UNSET)

        account_number_text = d.pop("AccountNumberText", UNSET)

        account_number = d.pop("AccountNumber", UNSET)

        currency_id = d.pop("CurrencyId", UNSET)

        client_status = d.pop("ClientStatus", UNSET)

        company_name = d.pop("CompanyName", UNSET)

        company_description = d.pop("CompanyDescription", UNSET)

        domain_name = d.pop("DomainName", UNSET)

        custom_client_name = d.pop("CustomClientName", UNSET)

        legacy_id = d.pop("LegacyId", UNSET)

        _updated_on_utc = d.pop("UpdatedOnUtc", UNSET)
        updated_on_utc: Union[Unset, datetime.datetime]
        if isinstance(_updated_on_utc, Unset):
            updated_on_utc = UNSET
        else:
            updated_on_utc = isoparse(_updated_on_utc)

        account_representative_employee_id = d.pop(
            "AccountRepresentativeEmployeeId", UNSET
        )

        account_representative_site_id = d.pop("AccountRepresentativeSiteId", UNSET)

        account_manager_employee_id = d.pop("AccountManagerEmployeeId", UNSET)

        def _parse_billing_address(
            data: object,
        ) -> Union[
            "QualerApiModelsClientsToClientCompanyResponseModelBillingAddressType0",
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
                billing_address_type_0 = QualerApiModelsClientsToClientCompanyResponseModelBillingAddressType0.from_dict(
                    data
                )

                return billing_address_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    "QualerApiModelsClientsToClientCompanyResponseModelBillingAddressType0",
                    None,
                    Unset,
                ],
                data,
            )

        billing_address = _parse_billing_address(d.pop("BillingAddress", UNSET))

        def _parse_shipping_address(
            data: object,
        ) -> Union[
            "QualerApiModelsClientsToClientCompanyResponseModelShippingAddressType0",
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
                shipping_address_type_0 = QualerApiModelsClientsToClientCompanyResponseModelShippingAddressType0.from_dict(
                    data
                )

                return shipping_address_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    "QualerApiModelsClientsToClientCompanyResponseModelShippingAddressType0",
                    None,
                    Unset,
                ],
                data,
            )

        shipping_address = _parse_shipping_address(d.pop("ShippingAddress", UNSET))

        attributes = []
        _attributes = d.pop("Attributes", UNSET)
        for attributes_item_data in _attributes or []:
            attributes_item = QualerApiModelsAttributesToAttributeResponse.from_dict(
                attributes_item_data
            )

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

        qualer_api_models_clients_to_client_company_response_model.additional_properties = (
            d
        )
        return qualer_api_models_clients_to_client_company_response_model

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
