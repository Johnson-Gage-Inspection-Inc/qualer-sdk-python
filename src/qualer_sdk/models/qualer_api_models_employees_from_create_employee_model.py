from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsEmployeesFromCreateEmployeeModel")


@_attrs_define
class QualerApiModelsEmployeesFromCreateEmployeeModel:
    """
    Attributes:
        login_email (Union[None, Unset, str]):
        password (Union[None, Unset, str]):
        first_name (Union[None, Unset, str]):
        last_name (Union[None, Unset, str]):
        subscription_email (Union[None, Unset, str]):
        mobile_phone (Union[None, Unset, str]):
        office_phone (Union[None, Unset, str]):
        alias (Union[None, Unset, str]):
        title (Union[None, Unset, str]):
        culture_name (Union[None, Unset, str]):
        culture_ui_name (Union[None, Unset, str]):
        image_url (Union[None, Unset, str]):
    """

    login_email: Union[None, Unset, str] = UNSET
    password: Union[None, Unset, str] = UNSET
    first_name: Union[None, Unset, str] = UNSET
    last_name: Union[None, Unset, str] = UNSET
    subscription_email: Union[None, Unset, str] = UNSET
    mobile_phone: Union[None, Unset, str] = UNSET
    office_phone: Union[None, Unset, str] = UNSET
    alias: Union[None, Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    culture_name: Union[None, Unset, str] = UNSET
    culture_ui_name: Union[None, Unset, str] = UNSET
    image_url: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        login_email = self.login_email

        password = self.password

        first_name = self.first_name

        last_name = self.last_name

        subscription_email = self.subscription_email

        mobile_phone = self.mobile_phone

        office_phone = self.office_phone

        alias = self.alias

        title = self.title

        culture_name = self.culture_name

        culture_ui_name = self.culture_ui_name

        image_url = self.image_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if login_email is not UNSET:
            field_dict["LoginEmail"] = login_email
        if password is not UNSET:
            field_dict["Password"] = password
        if first_name is not UNSET:
            field_dict["FirstName"] = first_name
        if last_name is not UNSET:
            field_dict["LastName"] = last_name
        if subscription_email is not UNSET:
            field_dict["SubscriptionEmail"] = subscription_email
        if mobile_phone is not UNSET:
            field_dict["MobilePhone"] = mobile_phone
        if office_phone is not UNSET:
            field_dict["OfficePhone"] = office_phone
        if alias is not UNSET:
            field_dict["Alias"] = alias
        if title is not UNSET:
            field_dict["Title"] = title
        if culture_name is not UNSET:
            field_dict["CultureName"] = culture_name
        if culture_ui_name is not UNSET:
            field_dict["CultureUiName"] = culture_ui_name
        if image_url is not UNSET:
            field_dict["ImageUrl"] = image_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        login_email = d.pop("LoginEmail", UNSET)

        password = d.pop("Password", UNSET)

        first_name = d.pop("FirstName", UNSET)

        last_name = d.pop("LastName", UNSET)

        subscription_email = d.pop("SubscriptionEmail", UNSET)

        mobile_phone = d.pop("MobilePhone", UNSET)

        office_phone = d.pop("OfficePhone", UNSET)

        alias = d.pop("Alias", UNSET)

        title = d.pop("Title", UNSET)

        culture_name = d.pop("CultureName", UNSET)

        culture_ui_name = d.pop("CultureUiName", UNSET)

        image_url = d.pop("ImageUrl", UNSET)

        qualer_api_models_employees_from_create_employee_model = cls(
            login_email=login_email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            subscription_email=subscription_email,
            mobile_phone=mobile_phone,
            office_phone=office_phone,
            alias=alias,
            title=title,
            culture_name=culture_name,
            culture_ui_name=culture_ui_name,
            image_url=image_url,
        )

        qualer_api_models_employees_from_create_employee_model.additional_properties = d
        return qualer_api_models_employees_from_create_employee_model

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
