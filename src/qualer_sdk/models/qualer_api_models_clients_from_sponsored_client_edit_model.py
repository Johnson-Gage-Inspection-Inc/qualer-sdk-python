from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.qualer_api_models_clients_from_sponsored_client_edit_model_client_status import (
    QualerApiModelsClientsFromSponsoredClientEditModelClientStatus,
)

if TYPE_CHECKING:
    from ..models.qualer_api_models_address_address_model import QualerApiModelsAddressAddressModel


T = TypeVar("T", bound="QualerApiModelsClientsFromSponsoredClientEditModel")


@_attrs_define
class QualerApiModelsClientsFromSponsoredClientEditModel:
    """
    Attributes:
        company_id (Optional[int]):
        account_number_text (Optional[str]):
        client_status (Optional[QualerApiModelsClientsFromSponsoredClientEditModelClientStatus]):
        domain_name (Optional[str]):
        custom_client_name (Optional[str]):
        legacy_id (Optional[str]):
        currency_id (Optional[int]):
        account_representative_employee_id (Optional[int]):
        account_representative_site_id (Optional[int]):
        account_manager_employee_id (Optional[int]):
        company_name (Optional[str]):
        billing_address (Optional[QualerApiModelsAddressAddressModel]):
        shipping_address (Optional[QualerApiModelsAddressAddressModel]):
    """

    company_id: Optional[int] = None
    account_number_text: Optional[str] = None
    client_status: Optional["QualerApiModelsClientsFromSponsoredClientEditModelClientStatus"] = None
    domain_name: Optional[str] = None
    custom_client_name: Optional[str] = None
    legacy_id: Optional[str] = None
    currency_id: Optional[int] = None
    account_representative_employee_id: Optional[int] = None
    account_representative_site_id: Optional[int] = None
    account_manager_employee_id: Optional[int] = None
    company_name: Optional[str] = None
    billing_address: Optional["QualerApiModelsAddressAddressModel"] = None
    shipping_address: Optional["QualerApiModelsAddressAddressModel"] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        company_id = self.company_id

        account_number_text = self.account_number_text

        client_status: Optional[str] = None
        if self.client_status:
            client_status = self.client_status.value

        domain_name = self.domain_name

        custom_client_name = self.custom_client_name

        legacy_id = self.legacy_id

        currency_id = self.currency_id

        account_representative_employee_id = self.account_representative_employee_id

        account_representative_site_id = self.account_representative_site_id

        account_manager_employee_id = self.account_manager_employee_id

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
        if company_id is not None:
            field_dict["CompanyId"] = company_id
        if account_number_text is not None:
            field_dict["AccountNumberText"] = account_number_text
        if client_status is not None:
            field_dict["ClientStatus"] = client_status
        if domain_name is not None:
            field_dict["DomainName"] = domain_name
        if custom_client_name is not None:
            field_dict["CustomClientName"] = custom_client_name
        if legacy_id is not None:
            field_dict["LegacyId"] = legacy_id
        if currency_id is not None:
            field_dict["CurrencyId"] = currency_id
        if account_representative_employee_id is not None:
            field_dict["AccountRepresentativeEmployeeId"] = account_representative_employee_id
        if account_representative_site_id is not None:
            field_dict["AccountRepresentativeSiteId"] = account_representative_site_id
        if account_manager_employee_id is not None:
            field_dict["AccountManagerEmployeeId"] = account_manager_employee_id
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
            QualerApiModelsAddressAddressModel,
        )

        d = dict(src_dict)
        company_id = d.pop("CompanyId", None)

        account_number_text = d.pop("AccountNumberText", None)

        _client_status = d.pop("ClientStatus", None)
        client_status: Optional[QualerApiModelsClientsFromSponsoredClientEditModelClientStatus]
        if not _client_status:
            client_status = None
        else:
            client_status = QualerApiModelsClientsFromSponsoredClientEditModelClientStatus(
                _client_status
            )

        domain_name = d.pop("DomainName", None)

        custom_client_name = d.pop("CustomClientName", None)

        legacy_id = d.pop("LegacyId", None)

        currency_id = d.pop("CurrencyId", None)

        account_representative_employee_id = d.pop("AccountRepresentativeEmployeeId", None)

        account_representative_site_id = d.pop("AccountRepresentativeSiteId", None)

        account_manager_employee_id = d.pop("AccountManagerEmployeeId", None)

        company_name = d.pop("CompanyName", None)

        _billing_address = d.pop("BillingAddress", None)
        billing_address: Optional[QualerApiModelsAddressAddressModel]
        if not _billing_address:
            billing_address = None
        else:
            billing_address = QualerApiModelsAddressAddressModel.from_dict(_billing_address)

        _shipping_address = d.pop("ShippingAddress", None)
        shipping_address: Optional[QualerApiModelsAddressAddressModel]
        if not _shipping_address:
            shipping_address = None
        else:
            shipping_address = QualerApiModelsAddressAddressModel.from_dict(_shipping_address)

        qualer_api_models_clients_from_sponsored_client_edit_model = cls(
            company_id=company_id,
            account_number_text=account_number_text,
            client_status=client_status,
            domain_name=domain_name,
            custom_client_name=custom_client_name,
            legacy_id=legacy_id,
            currency_id=currency_id,
            account_representative_employee_id=account_representative_employee_id,
            account_representative_site_id=account_representative_site_id,
            account_manager_employee_id=account_manager_employee_id,
            company_name=company_name,
            billing_address=billing_address,
            shipping_address=shipping_address,
        )

        qualer_api_models_clients_from_sponsored_client_edit_model.additional_properties = d
        return qualer_api_models_clients_from_sponsored_client_edit_model

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
