import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.qualer_api_models_service_orders_to_provider_service_order_response_model_timeframe import (
    ServiceOrdersToProviderServiceOrderResponseModelTimeframe,
)
from ..models.service_order_status import ServiceOrderStatus

T = TypeVar("T", bound="ServiceOrdersToProviderServiceOrderResponseModel")


@_attrs_define
class ServiceOrdersToProviderServiceOrderResponseModel:
    """
    Attributes:
        service_order_id (Optional[int]):
        guid (Optional[UUID]):  Example: 00000000-0000-0000-0000-000000000000.
        service_order_number (Optional[int]):
        custom_order_number (Optional[str]):
        due_date (Optional[datetime.datetime]):
        assets (Optional[int]):
        completed_assets (Optional[int]):
        order_status (Optional[ServiceOrderStatus]):
        is_quality_control_fail (Optional[bool]):
        service_private_comments (Optional[str]):
        client_company_id (Optional[int]):
        client_company_name (Optional[str]):
        client_site_name (Optional[str]):
        client_legacy_id (Optional[str]):
        business_from_time (Optional[datetime.datetime]):
        business_to_time (Optional[datetime.datetime]):
        timeframe (Optional[ServiceOrdersToProviderServiceOrderResponseModelTimeframe]):
        site_access_notes (Optional[str]):
        desired_date (Optional[datetime.datetime]):
        deadline_date (Optional[datetime.datetime]):
        request_from_date (Optional[datetime.datetime]):
        request_from_time (Optional[datetime.datetime]):
        request_to_date (Optional[datetime.datetime]):
        request_to_time (Optional[datetime.datetime]):
    """

    service_order_id: Optional[int] = None
    guid: Optional[UUID] = None
    service_order_number: Optional[int] = None
    custom_order_number: Optional[str] = None
    due_date: Optional[datetime.datetime] = None
    assets: Optional[int] = None
    completed_assets: Optional[int] = None
    order_status: Optional[ServiceOrderStatus] = None
    is_quality_control_fail: Optional[bool] = None
    service_private_comments: Optional[str] = None
    client_company_id: Optional[int] = None
    client_company_name: Optional[str] = None
    client_site_name: Optional[str] = None
    client_legacy_id: Optional[str] = None
    business_from_time: Optional[datetime.datetime] = None
    business_to_time: Optional[datetime.datetime] = None
    timeframe: Optional[ServiceOrdersToProviderServiceOrderResponseModelTimeframe] = None
    site_access_notes: Optional[str] = None
    desired_date: Optional[datetime.datetime] = None
    deadline_date: Optional[datetime.datetime] = None
    request_from_date: Optional[datetime.datetime] = None
    request_from_time: Optional[datetime.datetime] = None
    request_to_date: Optional[datetime.datetime] = None
    request_to_time: Optional[datetime.datetime] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_order_id = self.service_order_id
        guid: Optional[str] = None
        if self.guid:
            guid = str(self.guid)
        service_order_number = self.service_order_number
        custom_order_number = self.custom_order_number
        due_date = self.due_date.isoformat() if self.due_date else None
        assets = self.assets
        completed_assets = self.completed_assets
        order_status = self.order_status.value if self.order_status else None
        is_quality_control_fail = self.is_quality_control_fail
        service_private_comments = self.service_private_comments
        client_company_id = self.client_company_id
        client_company_name = self.client_company_name
        client_site_name = self.client_site_name
        client_legacy_id = self.client_legacy_id
        business_from_time = (
            self.business_from_time.isoformat() if self.business_from_time else None
        )
        business_to_time = self.business_to_time.isoformat() if self.business_to_time else None
        timeframe = self.timeframe.value if self.timeframe else None
        site_access_notes = self.site_access_notes
        desired_date = self.desired_date.isoformat() if self.desired_date else None
        deadline_date = self.deadline_date.isoformat() if self.deadline_date else None
        request_from_date = self.request_from_date.isoformat() if self.request_from_date else None
        request_from_time = self.request_from_time.isoformat() if self.request_from_time else None
        request_to_date = self.request_to_date.isoformat() if self.request_to_date else None
        request_to_time = self.request_to_time.isoformat() if self.request_to_time else None
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_id is not None:
            field_dict["ServiceOrderId"] = service_order_id
        if guid is not None:
            field_dict["Guid"] = guid
        if service_order_number is not None:
            field_dict["ServiceOrderNumber"] = service_order_number
        if custom_order_number is not None:
            field_dict["CustomOrderNumber"] = custom_order_number
        if due_date is not None:
            field_dict["DueDate"] = due_date
        if assets is not None:
            field_dict["Assets"] = assets
        if completed_assets is not None:
            field_dict["CompletedAssets"] = completed_assets
        if order_status is not None:
            field_dict["OrderStatus"] = order_status
        if is_quality_control_fail is not None:
            field_dict["IsQualityControlFail"] = is_quality_control_fail
        if service_private_comments is not None:
            field_dict["ServicePrivateComments"] = service_private_comments
        if client_company_id is not None:
            field_dict["ClientCompanyId"] = client_company_id
        if client_company_name is not None:
            field_dict["ClientCompanyName"] = client_company_name
        if client_site_name is not None:
            field_dict["ClientSiteName"] = client_site_name
        if client_legacy_id is not None:
            field_dict["ClientLegacyId"] = client_legacy_id
        if business_from_time is not None:
            field_dict["BusinessFromTime"] = business_from_time
        if business_to_time is not None:
            field_dict["BusinessToTime"] = business_to_time
        if timeframe is not None:
            field_dict["Timeframe"] = timeframe
        if site_access_notes is not None:
            field_dict["SiteAccessNotes"] = site_access_notes
        if desired_date is not None:
            field_dict["DesiredDate"] = desired_date
        if deadline_date is not None:
            field_dict["DeadlineDate"] = deadline_date
        if request_from_date is not None:
            field_dict["RequestFromDate"] = request_from_date
        if request_from_time is not None:
            field_dict["RequestFromTime"] = request_from_time
        if request_to_date is not None:
            field_dict["RequestToDate"] = request_to_date
        if request_to_time is not None:
            field_dict["RequestToTime"] = request_to_time
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_id = d.pop("ServiceOrderId", None)
        _guid = d.pop("Guid", None)
        guid: Optional[UUID]
        if not _guid:
            guid = None
        else:
            guid = UUID(_guid)
        service_order_number = d.pop("ServiceOrderNumber", None)
        custom_order_number = d.pop("CustomOrderNumber", None)

        def _parse_due_date(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_date_type_0 = isoparse(data)
                return due_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        due_date = _parse_due_date(d.pop("DueDate", None))
        assets = d.pop("Assets", None)
        completed_assets = d.pop("CompletedAssets", None)
        _order_status = d.pop("OrderStatus", None)
        order_status: Optional[ServiceOrderStatus]
        if not _order_status:
            order_status = None
        else:
            order_status = ServiceOrderStatus(_order_status)
        is_quality_control_fail = d.pop("IsQualityControlFail", None)
        service_private_comments = d.pop("ServicePrivateComments", None)
        client_company_id = d.pop("ClientCompanyId", None)
        client_company_name = d.pop("ClientCompanyName", None)
        client_site_name = d.pop("ClientSiteName", None)
        client_legacy_id = d.pop("ClientLegacyId", None)

        def _parse_business_from_time(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                business_from_time_type_0 = isoparse(data)
                return business_from_time_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        business_from_time = _parse_business_from_time(d.pop("BusinessFromTime", None))

        def _parse_business_to_time(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                business_to_time_type_0 = isoparse(data)
                return business_to_time_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        business_to_time = _parse_business_to_time(d.pop("BusinessToTime", None))
        _timeframe = d.pop("Timeframe", None)
        timeframe: Optional[ServiceOrdersToProviderServiceOrderResponseModelTimeframe]
        if not _timeframe:
            timeframe = None
        else:
            timeframe = ServiceOrdersToProviderServiceOrderResponseModelTimeframe(_timeframe)
        site_access_notes = d.pop("SiteAccessNotes", None)

        def _parse_desired_date(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                desired_date_type_0 = isoparse(data)
                return desired_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        desired_date = _parse_desired_date(d.pop("DesiredDate", None))

        def _parse_deadline_date(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deadline_date_type_0 = isoparse(data)
                return deadline_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        deadline_date = _parse_deadline_date(d.pop("DeadlineDate", None))

        def _parse_request_from_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                request_from_date_type_0 = isoparse(data)
                return request_from_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        request_from_date = _parse_request_from_date(d.pop("RequestFromDate", None))

        def _parse_request_from_time(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                request_from_time_type_0 = isoparse(data)
                return request_from_time_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        request_from_time = _parse_request_from_time(d.pop("RequestFromTime", None))

        def _parse_request_to_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                request_to_date_type_0 = isoparse(data)
                return request_to_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        request_to_date = _parse_request_to_date(d.pop("RequestToDate", None))

        def _parse_request_to_time(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                request_to_time_type_0 = isoparse(data)
                return request_to_time_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        request_to_time = _parse_request_to_time(d.pop("RequestToTime", None))
        qualer_api_models_service_orders_to_provider_service_order_response_model = cls(
            service_order_id=service_order_id,
            guid=guid,
            service_order_number=service_order_number,
            custom_order_number=custom_order_number,
            due_date=due_date,
            assets=assets,
            completed_assets=completed_assets,
            order_status=order_status,
            is_quality_control_fail=is_quality_control_fail,
            service_private_comments=service_private_comments,
            client_company_id=client_company_id,
            client_company_name=client_company_name,
            client_site_name=client_site_name,
            client_legacy_id=client_legacy_id,
            business_from_time=business_from_time,
            business_to_time=business_to_time,
            timeframe=timeframe,
            site_access_notes=site_access_notes,
            desired_date=desired_date,
            deadline_date=deadline_date,
            request_from_date=request_from_date,
            request_from_time=request_from_time,
            request_to_date=request_to_date,
            request_to_time=request_to_time,
        )
        qualer_api_models_service_orders_to_provider_service_order_response_model.additional_properties = (
            d
        )
        return qualer_api_models_service_orders_to_provider_service_order_response_model

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
