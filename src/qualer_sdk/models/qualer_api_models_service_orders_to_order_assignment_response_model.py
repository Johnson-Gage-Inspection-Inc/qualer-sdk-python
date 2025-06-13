import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsServiceOrdersToOrderAssignmentResponseModel")


@_attrs_define
class QualerApiModelsServiceOrdersToOrderAssignmentResponseModel:
    """
    Attributes:
        work_item_id (Union[Unset, int]):
        employee_id (Union[Unset, int]):
        company_id (Union[Unset, int]):
        subscription_email (Union[Unset, str]):
        subscription_phone (Union[Unset, str]):
        office_phone (Union[Unset, str]):
        is_locked (Union[Unset, bool]):
        image_url (Union[Unset, str]):
        alias (Union[Unset, str]):
        title (Union[Unset, str]):
        is_deleted (Union[Unset, bool]):
        last_seen_date_utc (Union[None, Unset, datetime.datetime]):
    """

    work_item_id: Union[Unset, int] = UNSET
    employee_id: Union[Unset, int] = UNSET
    company_id: Union[Unset, int] = UNSET
    subscription_email: Union[Unset, str] = UNSET
    subscription_phone: Union[Unset, str] = UNSET
    office_phone: Union[Unset, str] = UNSET
    is_locked: Union[Unset, bool] = UNSET
    image_url: Union[Unset, str] = UNSET
    alias: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    is_deleted: Union[Unset, bool] = UNSET
    last_seen_date_utc: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        work_item_id = self.work_item_id

        employee_id = self.employee_id

        company_id = self.company_id

        subscription_email = self.subscription_email

        subscription_phone = self.subscription_phone

        office_phone = self.office_phone

        is_locked = self.is_locked

        image_url = self.image_url

        alias = self.alias

        title = self.title

        is_deleted = self.is_deleted

        last_seen_date_utc: Union[None, Unset, str]
        if isinstance(self.last_seen_date_utc, Unset):
            last_seen_date_utc = UNSET
        elif isinstance(self.last_seen_date_utc, datetime.datetime):
            last_seen_date_utc = self.last_seen_date_utc.isoformat()
        else:
            last_seen_date_utc = self.last_seen_date_utc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if work_item_id is not UNSET:
            field_dict["WorkItemId"] = work_item_id
        if employee_id is not UNSET:
            field_dict["EmployeeId"] = employee_id
        if company_id is not UNSET:
            field_dict["CompanyId"] = company_id
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        work_item_id = d.pop("WorkItemId", UNSET)

        employee_id = d.pop("EmployeeId", UNSET)

        company_id = d.pop("CompanyId", UNSET)

        subscription_email = d.pop("SubscriptionEmail", UNSET)

        subscription_phone = d.pop("SubscriptionPhone", UNSET)

        office_phone = d.pop("OfficePhone", UNSET)

        is_locked = d.pop("IsLocked", UNSET)

        image_url = d.pop("ImageUrl", UNSET)

        alias = d.pop("Alias", UNSET)

        title = d.pop("Title", UNSET)

        is_deleted = d.pop("IsDeleted", UNSET)

        def _parse_last_seen_date_utc(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_seen_date_utc_type_0 = isoparse(data)

                return last_seen_date_utc_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_seen_date_utc = _parse_last_seen_date_utc(d.pop("LastSeenDateUtc", UNSET))

        qualer_api_models_service_orders_to_order_assignment_response_model = cls(
            work_item_id=work_item_id,
            employee_id=employee_id,
            company_id=company_id,
            subscription_email=subscription_email,
            subscription_phone=subscription_phone,
            office_phone=office_phone,
            is_locked=is_locked,
            image_url=image_url,
            alias=alias,
            title=title,
            is_deleted=is_deleted,
            last_seen_date_utc=last_seen_date_utc,
        )

        qualer_api_models_service_orders_to_order_assignment_response_model.additional_properties = (
            d
        )
        return qualer_api_models_service_orders_to_order_assignment_response_model

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
