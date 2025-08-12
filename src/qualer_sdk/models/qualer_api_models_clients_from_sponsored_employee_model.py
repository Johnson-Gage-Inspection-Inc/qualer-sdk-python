from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsClientsFromSponsoredEmployeeModel")


@_attrs_define
class QualerApiModelsClientsFromSponsoredEmployeeModel:
    """
    Attributes:
        client_company_id (Union[None, Unset, int]):
        first_name (Union[None, Unset, str]):
        last_name (Union[None, Unset, str]):
        login_email (Union[None, Unset, str]):
        password (Union[None, Unset, str]):
        subscription_email (Union[None, Unset, str]):
        mobile_phone (Union[None, Unset, str]):
        office_phone (Union[None, Unset, str]):
    """

    client_company_id: Union[None, Unset, int] = UNSET
    first_name: Union[None, Unset, str] = UNSET
    last_name: Union[None, Unset, str] = UNSET
    login_email: Union[None, Unset, str] = UNSET
    password: Union[None, Unset, str] = UNSET
    subscription_email: Union[None, Unset, str] = UNSET
    mobile_phone: Union[None, Unset, str] = UNSET
    office_phone: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_company_id = self.client_company_id

        first_name = self.first_name

        last_name = self.last_name

        login_email = self.login_email

        password = self.password

        subscription_email = self.subscription_email

        mobile_phone = self.mobile_phone

        office_phone = self.office_phone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_company_id is not UNSET:
            field_dict["ClientCompanyId"] = client_company_id
        if first_name is not UNSET:
            field_dict["FirstName"] = first_name
        if last_name is not UNSET:
            field_dict["LastName"] = last_name
        if login_email is not UNSET:
            field_dict["LoginEmail"] = login_email
        if password is not UNSET:
            field_dict["Password"] = password
        if subscription_email is not UNSET:
            field_dict["SubscriptionEmail"] = subscription_email
        if mobile_phone is not UNSET:
            field_dict["MobilePhone"] = mobile_phone
        if office_phone is not UNSET:
            field_dict["OfficePhone"] = office_phone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_company_id = d.pop("ClientCompanyId", UNSET)

        first_name = d.pop("FirstName", UNSET)

        last_name = d.pop("LastName", UNSET)

        login_email = d.pop("LoginEmail", UNSET)

        password = d.pop("Password", UNSET)

        subscription_email = d.pop("SubscriptionEmail", UNSET)

        mobile_phone = d.pop("MobilePhone", UNSET)

        office_phone = d.pop("OfficePhone", UNSET)

        qualer_api_models_clients_from_sponsored_employee_model = cls(
            client_company_id=client_company_id,
            first_name=first_name,
            last_name=last_name,
            login_email=login_email,
            password=password,
            subscription_email=subscription_email,
            mobile_phone=mobile_phone,
            office_phone=office_phone,
        )

        qualer_api_models_clients_from_sponsored_employee_model.additional_properties = (
            d
        )
        return qualer_api_models_clients_from_sponsored_employee_model

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
