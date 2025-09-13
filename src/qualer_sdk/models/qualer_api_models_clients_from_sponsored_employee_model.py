from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ClientsFromSponsoredEmployeeModel")


@_attrs_define
class ClientsFromSponsoredEmployeeModel:
    """
    Attributes:
        client_company_id (Optional[int]):
        first_name (Optional[str]):
        last_name (Optional[str]):
        login_email (Optional[str]):
        password (Optional[str]):
        subscription_email (Optional[str]):
        mobile_phone (Optional[str]):
        office_phone (Optional[str]):
    """

    client_company_id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    login_email: Optional[str] = None
    password: Optional[str] = None
    subscription_email: Optional[str] = None
    mobile_phone: Optional[str] = None
    office_phone: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_company_id = self.client_company_id

        first_name = self.first_name

        last_name = self.last_name

        login_email = self.login_email

        password = self.password

        subscription_email = self.subscription_email

        mobile_phone = self.mobile_phone

        office_phone = self.office_phone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_company_id is not None:
            field_dict["ClientCompanyId"] = client_company_id
        if first_name is not None:
            field_dict["FirstName"] = first_name
        if last_name is not None:
            field_dict["LastName"] = last_name
        if login_email is not None:
            field_dict["LoginEmail"] = login_email
        if password is not None:
            field_dict["Password"] = password
        if subscription_email is not None:
            field_dict["SubscriptionEmail"] = subscription_email
        if mobile_phone is not None:
            field_dict["MobilePhone"] = mobile_phone
        if office_phone is not None:
            field_dict["OfficePhone"] = office_phone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_company_id = d.pop("ClientCompanyId", None)

        first_name = d.pop("FirstName", None)

        last_name = d.pop("LastName", None)

        login_email = d.pop("LoginEmail", None)

        password = d.pop("Password", None)

        subscription_email = d.pop("SubscriptionEmail", None)

        mobile_phone = d.pop("MobilePhone", None)

        office_phone = d.pop("OfficePhone", None)

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

        qualer_api_models_clients_from_sponsored_employee_model.additional_properties = d
        return qualer_api_models_clients_from_sponsored_employee_model

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
