import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.qualer_api_models_clients_to_employee_employee_department_response import (
        QualerApiModelsClientsToEmployeeEmployeeDepartmentResponse,
    )


T = TypeVar("T", bound="QualerApiModelsClientsToEmployeeResponseModel")


@_attrs_define
class QualerApiModelsClientsToEmployeeResponseModel:
    """
    Attributes:
        employee_id (Optional[int]):
        first_name (Optional[str]):
        last_name (Optional[str]):
        company_id (Optional[int]):
        login_email (Optional[str]):
        departments (Optional[List['QualerApiModelsClientsToEmployeeEmployeeDepartmentResponse']]):
        subscription_email (Optional[str]):
        subscription_phone (Optional[str]):
        office_phone (Optional[str]):
        is_locked (Optional[bool]):
        image_url (Optional[str]):
        alias (Optional[str]):
        title (Optional[str]):
        is_deleted (Optional[bool]):
        last_seen_date_utc (Optional[datetime.datetime]):
        culture_name (Optional[str]):
        culture_ui_name (Optional[str]):
    """

    employee_id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    company_id: Optional[int] = None
    login_email: Optional[str] = None
    departments: Union[None, List["QualerApiModelsClientsToEmployeeEmployeeDepartmentResponse"]] = (
        None
    )
    subscription_email: Optional[str] = None
    subscription_phone: Optional[str] = None
    office_phone: Optional[str] = None
    is_locked: Optional[bool] = None
    image_url: Optional[str] = None
    alias: Optional[str] = None
    title: Optional[str] = None
    is_deleted: Optional[bool] = None
    last_seen_date_utc: Optional[datetime.datetime] = None
    culture_name: Optional[str] = None
    culture_ui_name: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        employee_id = self.employee_id

        first_name = self.first_name

        last_name = self.last_name

        company_id = self.company_id

        login_email = self.login_email

        departments: Optional[List[Dict[str, Any]]] = None
        if self.departments:
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

        last_seen_date_utc: Optional[str]
        if not self.last_seen_date_utc:
            last_seen_date_utc = None
        elif isinstance(self.last_seen_date_utc, datetime.datetime):
            last_seen_date_utc = self.last_seen_date_utc.isoformat()
        else:
            last_seen_date_utc = self.last_seen_date_utc

        culture_name = self.culture_name

        culture_ui_name = self.culture_ui_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if employee_id is not None:
            field_dict["EmployeeId"] = employee_id
        if first_name is not None:
            field_dict["FirstName"] = first_name
        if last_name is not None:
            field_dict["LastName"] = last_name
        if company_id is not None:
            field_dict["CompanyId"] = company_id
        if login_email is not None:
            field_dict["LoginEmail"] = login_email
        if departments is not None:
            field_dict["Departments"] = departments
        if subscription_email is not None:
            field_dict["SubscriptionEmail"] = subscription_email
        if subscription_phone is not None:
            field_dict["SubscriptionPhone"] = subscription_phone
        if office_phone is not None:
            field_dict["OfficePhone"] = office_phone
        if is_locked is not None:
            field_dict["IsLocked"] = is_locked
        if image_url is not None:
            field_dict["ImageUrl"] = image_url
        if alias is not None:
            field_dict["Alias"] = alias
        if title is not None:
            field_dict["Title"] = title
        if is_deleted is not None:
            field_dict["IsDeleted"] = is_deleted
        if last_seen_date_utc is not None:
            field_dict["LastSeenDateUtc"] = last_seen_date_utc
        if culture_name is not None:
            field_dict["CultureName"] = culture_name
        if culture_ui_name is not None:
            field_dict["CultureUiName"] = culture_ui_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_clients_to_employee_employee_department_response import (
            QualerApiModelsClientsToEmployeeEmployeeDepartmentResponse,
        )

        d = dict(src_dict)
        employee_id = d.pop("EmployeeId", None)

        first_name = d.pop("FirstName", None)

        last_name = d.pop("LastName", None)

        company_id = d.pop("CompanyId", None)

        login_email = d.pop("LoginEmail", None)

        departments = []
        _departments = d.pop("Departments", None)
        for departments_item_data in _departments or []:
            departments_item = QualerApiModelsClientsToEmployeeEmployeeDepartmentResponse.from_dict(
                departments_item_data
            )

            departments.append(departments_item)

        subscription_email = d.pop("SubscriptionEmail", None)

        subscription_phone = d.pop("SubscriptionPhone", None)

        office_phone = d.pop("OfficePhone", None)

        is_locked = d.pop("IsLocked", None)

        image_url = d.pop("ImageUrl", None)

        alias = d.pop("Alias", None)

        title = d.pop("Title", None)

        is_deleted = d.pop("IsDeleted", None)

        def _parse_last_seen_date_utc(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_seen_date_utc_type_0 = isoparse(data)

                return last_seen_date_utc_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        last_seen_date_utc = _parse_last_seen_date_utc(d.pop("LastSeenDateUtc", None))

        culture_name = d.pop("CultureName", None)

        culture_ui_name = d.pop("CultureUiName", None)

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
