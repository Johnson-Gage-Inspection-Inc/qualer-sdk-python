from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.qualer_api_models_clients_from_sponsored_client_create_model_client_status import (
    QualerApiModelsClientsFromSponsoredClientCreateModelClientStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualer_api_models_address_address_model import (
        QualerApiModelsAddressAddressModel,
    )


T = TypeVar("T", bound="QualerApiModelsClientsFromSponsoredClientCreateModel")


@_attrs_define
class QualerApiModelsClientsFromSponsoredClientCreateModel:
    """
    Attributes:
        account_number_text (Union[Unset, str]):
        client_status (Union[Unset, QualerApiModelsClientsFromSponsoredClientCreateModelClientStatus]):
        domain_name (Union[Unset, str]):
        custom_client_name (Union[Unset, str]):
        legacy_id (Union[Unset, str]):
        currency_id (Union[Unset, int]):
        account_representative_employee_id (Union[Unset, int]):
        account_representative_site_id (Union[Unset, int]):
        account_manager_employee_id (Union[Unset, int]):
        company_name (Union[Unset, str]):
        billing_address (Union[Unset, QualerApiModelsAddressAddressModel]):
        shipping_address (Union[Unset, QualerApiModelsAddressAddressModel]):
    """

    account_number_text: Union[Unset, str] = UNSET
    client_status: Union[
        Unset, QualerApiModelsClientsFromSponsoredClientCreateModelClientStatus
    ] = UNSET
    domain_name: Union[Unset, str] = UNSET
    custom_client_name: Union[Unset, str] = UNSET
    legacy_id: Union[Unset, str] = UNSET
    currency_id: Union[Unset, int] = UNSET
    account_representative_employee_id: Union[Unset, int] = UNSET
    account_representative_site_id: Union[Unset, int] = UNSET
    account_manager_employee_id: Union[Unset, int] = UNSET
    company_name: Union[Unset, str] = UNSET
    billing_address: Union[Unset, "QualerApiModelsAddressAddressModel"] = UNSET
    shipping_address: Union[Unset, "QualerApiModelsAddressAddressModel"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_number_text = self.account_number_text

        client_status: Union[Unset, str] = UNSET
        if not isinstance(self.client_status, Unset):
            client_status = self.client_status.value

        domain_name = self.domain_name

        custom_client_name = self.custom_client_name

        legacy_id = self.legacy_id

        currency_id = self.currency_id

        account_representative_employee_id = self.account_representative_employee_id

        account_representative_site_id = self.account_representative_site_id

        account_manager_employee_id = self.account_manager_employee_id

        company_name = self.company_name

        billing_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.billing_address, Unset):
            billing_address = self.billing_address.to_dict()

        shipping_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shipping_address, Unset):
            shipping_address = self.shipping_address.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_number_text is not UNSET:
            field_dict["AccountNumberText"] = account_number_text
        if client_status is not UNSET:
            field_dict["ClientStatus"] = client_status
        if domain_name is not UNSET:
            field_dict["DomainName"] = domain_name
        if custom_client_name is not UNSET:
            field_dict["CustomClientName"] = custom_client_name
        if legacy_id is not UNSET:
            field_dict["LegacyId"] = legacy_id
        if currency_id is not UNSET:
            field_dict["CurrencyId"] = currency_id
        if account_representative_employee_id is not UNSET:
            field_dict["AccountRepresentativeEmployeeId"] = (
                account_representative_employee_id
            )
        if account_representative_site_id is not UNSET:
            field_dict["AccountRepresentativeSiteId"] = account_representative_site_id
        if account_manager_employee_id is not UNSET:
            field_dict["AccountManagerEmployeeId"] = account_manager_employee_id
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

        _client_status = d.pop("ClientStatus", UNSET)
        client_status: Union[
            Unset, QualerApiModelsClientsFromSponsoredClientCreateModelClientStatus
        ]
        if isinstance(_client_status, Unset):
            client_status = UNSET
        else:
            client_status = (
                QualerApiModelsClientsFromSponsoredClientCreateModelClientStatus(
                    _client_status
                )
            )

        domain_name = d.pop("DomainName", UNSET)

        custom_client_name = d.pop("CustomClientName", UNSET)

        legacy_id = d.pop("LegacyId", UNSET)

        currency_id = d.pop("CurrencyId", UNSET)

        account_representative_employee_id = d.pop(
            "AccountRepresentativeEmployeeId", UNSET
        )

        account_representative_site_id = d.pop("AccountRepresentativeSiteId", UNSET)

        account_manager_employee_id = d.pop("AccountManagerEmployeeId", UNSET)

        company_name = d.pop("CompanyName", UNSET)

        _billing_address = d.pop("BillingAddress", UNSET)
        billing_address: Union[Unset, QualerApiModelsAddressAddressModel]
        if isinstance(_billing_address, Unset):
            billing_address = UNSET
        else:
            billing_address = QualerApiModelsAddressAddressModel.from_dict(
                _billing_address
            )

        _shipping_address = d.pop("ShippingAddress", UNSET)
        shipping_address: Union[Unset, QualerApiModelsAddressAddressModel]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = QualerApiModelsAddressAddressModel.from_dict(
                _shipping_address
            )

        qualer_api_models_clients_from_sponsored_client_create_model = cls(
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

        qualer_api_models_clients_from_sponsored_client_create_model.additional_properties = (
            d
        )
        return qualer_api_models_clients_from_sponsored_client_create_model

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
