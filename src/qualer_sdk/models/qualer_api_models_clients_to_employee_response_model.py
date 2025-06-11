import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualer_api_models_clients_to_employee_employee_department_response import (
        QualerApiModelsClientsToEmployeeEmployeeDepartmentResponse,
    )


T = TypeVar("T", bound="QualerApiModelsClientsToEmployeeResponseModel")


@_attrs_define
class QualerApiModelsClientsToEmployeeResponseModel:
    """
    Attributes:
        employee_id (Union[Unset, int]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        company_id (Union[Unset, int]):
        login_email (Union[Unset, str]):
        departments (Union[Unset, list['QualerApiModelsClientsToEmployeeEmployeeDepartmentResponse']]):
        subscription_email (Union[Unset, str]):
        subscription_phone (Union[Unset, str]):
        office_phone (Union[Unset, str]):
        is_locked (Union[Unset, bool]):
        image_url (Union[Unset, str]):
        alias (Union[Unset, str]):
        title (Union[Unset, str]):
        is_deleted (Union[Unset, bool]):
        last_seen_date_utc (Union[Unset, datetime.datetime]):
        culture_name (Union[Unset, str]):
        culture_ui_name (Union[Unset, str]):
    """

    employee_id: Union[Unset, int] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    company_id: Union[Unset, int] = UNSET
    login_email: Union[Unset, str] = UNSET
    departments: Union[
        Unset, list["QualerApiModelsClientsToEmployeeEmployeeDepartmentResponse"]
    ] = UNSET
    subscription_email: Union[Unset, str] = UNSET
    subscription_phone: Union[Unset, str] = UNSET
    office_phone: Union[Unset, str] = UNSET
    is_locked: Union[Unset, bool] = UNSET
    image_url: Union[Unset, str] = UNSET
    alias: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    is_deleted: Union[Unset, bool] = UNSET
    last_seen_date_utc: Union[Unset, datetime.datetime] = UNSET
    culture_name: Union[Unset, str] = UNSET
    culture_ui_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        employee_id = self.employee_id

        first_name = self.first_name

        last_name = self.last_name

        company_id = self.company_id

        login_email = self.login_email

        departments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.departments, Unset):
            departments = []
            for departments_item_data in self.departments:
                departments_item = departments_item_data.to_dict()
                departments.append(departments_item)

        subscription_email = self.subscription_email

        subscription_phone = self.subscription_phone

        office_phone = self.office_phone

        is_locked = self.is_locked

        image_url = self.image_url

        alias = self.alias

        title = self.title

        is_deleted = self.is_deleted

        last_seen_date_utc: Union[Unset, str] = UNSET
        if not isinstance(self.last_seen_date_utc, Unset):
            last_seen_date_utc = self.last_seen_date_utc.isoformat()

        culture_name = self.culture_name

        culture_ui_name = self.culture_ui_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if employee_id is not UNSET:
            field_dict["EmployeeId"] = employee_id
        if first_name is not UNSET:
            field_dict["FirstName"] = first_name
        if last_name is not UNSET:
            field_dict["LastName"] = last_name
        if company_id is not UNSET:
            field_dict["CompanyId"] = company_id
        if login_email is not UNSET:
            field_dict["LoginEmail"] = login_email
        if departments is not UNSET:
            field_dict["Departments"] = departments
        if subscription_email is not UNSET:
            field_dict["SubscriptionEmail"] = subscription_email
        if subscription_phone is not UNSET:
            field_dict["SubscriptionPhone"] = subscription_phone
        if office_phone is not UNSET:
            field_dict["OfficePhone"] = office_phone
        if is_locked is not UNSET:
            field_dict["IsLocked"] = is_locked
        if image_url is not UNSET:
            field_dict["ImageUrl"] = image_url
        if alias is not UNSET:
            field_dict["Alias"] = alias
        if title is not UNSET:
            field_dict["Title"] = title
        if is_deleted is not UNSET:
            field_dict["IsDeleted"] = is_deleted
        if last_seen_date_utc is not UNSET:
            field_dict["LastSeenDateUtc"] = last_seen_date_utc
        if culture_name is not UNSET:
            field_dict["CultureName"] = culture_name
        if culture_ui_name is not UNSET:
            field_dict["CultureUiName"] = culture_ui_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_clients_to_employee_employee_department_response import (
            QualerApiModelsClientsToEmployeeEmployeeDepartmentResponse,
        )

        d = dict(src_dict)
        employee_id = d.pop("EmployeeId", UNSET)

        first_name = d.pop("FirstName", UNSET)

        last_name = d.pop("LastName", UNSET)

        company_id = d.pop("CompanyId", UNSET)

        login_email = d.pop("LoginEmail", UNSET)

        departments = []
        _departments = d.pop("Departments", UNSET)
        for departments_item_data in _departments or []:
            departments_item = (
                QualerApiModelsClientsToEmployeeEmployeeDepartmentResponse.from_dict(
                    departments_item_data
                )
            )

            departments.append(departments_item)

        subscription_email = d.pop("SubscriptionEmail", UNSET)

        subscription_phone = d.pop("SubscriptionPhone", UNSET)

        office_phone = d.pop("OfficePhone", UNSET)

        is_locked = d.pop("IsLocked", UNSET)

        image_url = d.pop("ImageUrl", UNSET)

        alias = d.pop("Alias", UNSET)

        title = d.pop("Title", UNSET)

        is_deleted = d.pop("IsDeleted", UNSET)

        _last_seen_date_utc = d.pop("LastSeenDateUtc", UNSET)
        last_seen_date_utc: Union[Unset, datetime.datetime]
        if isinstance(_last_seen_date_utc, Unset):
            last_seen_date_utc = UNSET
        else:
            last_seen_date_utc = isoparse(_last_seen_date_utc)

        culture_name = d.pop("CultureName", UNSET)

        culture_ui_name = d.pop("CultureUiName", UNSET)

        qualer_api_models_clients_to_employee_response_model = cls(
            employee_id=employee_id,
            first_name=first_name,
            last_name=last_name,
            company_id=company_id,
            login_email=login_email,
            departments=departments,
            subscription_email=subscription_email,
            subscription_phone=subscription_phone,
            office_phone=office_phone,
            is_locked=is_locked,
            image_url=image_url,
            alias=alias,
            title=title,
            is_deleted=is_deleted,
            last_seen_date_utc=last_seen_date_utc,
            culture_name=culture_name,
            culture_ui_name=culture_ui_name,
        )

        qualer_api_models_clients_to_employee_response_model.additional_properties = d
        return qualer_api_models_clients_to_employee_response_model

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
