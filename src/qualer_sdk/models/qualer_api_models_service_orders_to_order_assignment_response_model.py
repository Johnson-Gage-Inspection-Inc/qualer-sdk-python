import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ServiceOrdersToOrderAssignmentResponseModel")


@_attrs_define
class ServiceOrdersToOrderAssignmentResponseModel:
    """
    Attributes:
        work_item_id (Optional[int]):
        employee_id (Optional[int]):
        company_id (Optional[int]):
        subscription_email (Optional[str]):
        subscription_phone (Optional[str]):
        office_phone (Optional[str]):
        is_locked (Optional[bool]):
        image_url (Optional[str]):
        alias (Optional[str]):
        title (Optional[str]):
        is_deleted (Optional[bool]):
        last_seen_date_utc (Optional[datetime.datetime]):
    """

    work_item_id: Optional[int] = None
    employee_id: Optional[int] = None
    company_id: Optional[int] = None
    subscription_email: Optional[str] = None
    subscription_phone: Optional[str] = None
    office_phone: Optional[str] = None
    is_locked: Optional[bool] = None
    image_url: Optional[str] = None
    alias: Optional[str] = None
    title: Optional[str] = None
    is_deleted: Optional[bool] = None
    last_seen_date_utc: Optional[datetime.datetime] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
        last_seen_date_utc = (
            self.last_seen_date_utc.isoformat() if self.last_seen_date_utc else None
        )
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if work_item_id is not None:
            field_dict["WorkItemId"] = work_item_id
        if employee_id is not None:
            field_dict["EmployeeId"] = employee_id
        if company_id is not None:
            field_dict["CompanyId"] = company_id
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
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        work_item_id = d.pop("WorkItemId", None)
        employee_id = d.pop("EmployeeId", None)
        company_id = d.pop("CompanyId", None)
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
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        last_seen_date_utc = _parse_last_seen_date_utc(d.pop("LastSeenDateUtc", None))
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
