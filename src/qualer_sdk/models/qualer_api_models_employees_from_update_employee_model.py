from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EmployeesFromUpdateEmployeeModel")


@_attrs_define
class EmployeesFromUpdateEmployeeModel:
    """
    Attributes:
        first_name (Optional[str]):
        last_name (Optional[str]):
        subscription_email (Optional[str]):
        mobile_phone (Optional[str]):
        office_phone (Optional[str]):
        alias (Optional[str]):
        title (Optional[str]):
        culture_name (Optional[str]):
        culture_ui_name (Optional[str]):
        image_url (Optional[str]):
    """

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    subscription_email: Optional[str] = None
    mobile_phone: Optional[str] = None
    office_phone: Optional[str] = None
    alias: Optional[str] = None
    title: Optional[str] = None
    culture_name: Optional[str] = None
    culture_ui_name: Optional[str] = None
    image_url: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not None:
            field_dict["FirstName"] = first_name
        if last_name is not None:
            field_dict["LastName"] = last_name
        if subscription_email is not None:
            field_dict["SubscriptionEmail"] = subscription_email
        if mobile_phone is not None:
            field_dict["MobilePhone"] = mobile_phone
        if office_phone is not None:
            field_dict["OfficePhone"] = office_phone
        if alias is not None:
            field_dict["Alias"] = alias
        if title is not None:
            field_dict["Title"] = title
        if culture_name is not None:
            field_dict["CultureName"] = culture_name
        if culture_ui_name is not None:
            field_dict["CultureUiName"] = culture_ui_name
        if image_url is not None:
            field_dict["ImageUrl"] = image_url
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        first_name = d.pop("FirstName", None)
        last_name = d.pop("LastName", None)
        subscription_email = d.pop("SubscriptionEmail", None)
        mobile_phone = d.pop("MobilePhone", None)
        office_phone = d.pop("OfficePhone", None)
        alias = d.pop("Alias", None)
        title = d.pop("Title", None)
        culture_name = d.pop("CultureName", None)
        culture_ui_name = d.pop("CultureUiName", None)
        image_url = d.pop("ImageUrl", None)
        qualer_api_models_employees_from_update_employee_model = cls(
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
        qualer_api_models_employees_from_update_employee_model.additional_properties = d
        return qualer_api_models_employees_from_update_employee_model

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
