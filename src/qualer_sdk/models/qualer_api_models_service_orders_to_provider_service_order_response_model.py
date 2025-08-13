import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.qualer_api_models_service_orders_to_provider_service_order_response_model_order_status import (
    QualerApiModelsServiceOrdersToProviderServiceOrderResponseModelOrderStatus,
)
from ..models.qualer_api_models_service_orders_to_provider_service_order_response_model_timeframe import (
    QualerApiModelsServiceOrdersToProviderServiceOrderResponseModelTimeframe,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel"
)


@_attrs_define
class QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel:
    """
    Attributes:
        service_order_id (Union[None, Unset, int]):
        guid (Union[None, Unset, UUID]):  Example: 00000000-0000-0000-0000-000000000000.
        service_order_number (Union[None, Unset, int]):
        custom_order_number (Union[None, Unset, str]):
        due_date (Union[None, Unset, datetime.datetime]):
        assets (Union[None, Unset, int]):
        completed_assets (Union[None, Unset, int]):
        order_status (Union[None, Unset, QualerApiModelsServiceOrdersToProviderServiceOrderResponseModelOrderStatus]):
        is_quality_control_fail (Union[None, Unset, bool]):
        service_private_comments (Union[None, Unset, str]):
        client_company_id (Union[None, Unset, int]):
        client_company_name (Union[None, Unset, str]):
        client_site_name (Union[None, Unset, str]):
        client_legacy_id (Union[None, Unset, str]):
        business_from_time (Union[None, Unset, datetime.datetime]):
        business_to_time (Union[None, Unset, datetime.datetime]):
        timeframe (Union[None, Unset, QualerApiModelsServiceOrdersToProviderServiceOrderResponseModelTimeframe]):
        site_access_notes (Union[None, Unset, str]):
        desired_date (Union[None, Unset, datetime.datetime]):
        deadline_date (Union[None, Unset, datetime.datetime]):
        request_from_date (Union[None, Unset, datetime.datetime]):
        request_from_time (Union[None, Unset, datetime.datetime]):
        request_to_date (Union[None, Unset, datetime.datetime]):
        request_to_time (Union[None, Unset, datetime.datetime]):
    """

    service_order_id: Union[None, Unset, int] = UNSET
    guid: Union[None, Unset, UUID] = UNSET
    service_order_number: Union[None, Unset, int] = UNSET
    custom_order_number: Union[None, Unset, str] = UNSET
    due_date: Union[None, Unset, datetime.datetime] = UNSET
    assets: Union[None, Unset, int] = UNSET
    completed_assets: Union[None, Unset, int] = UNSET
    order_status: Union[
        None,
        Unset,
        QualerApiModelsServiceOrdersToProviderServiceOrderResponseModelOrderStatus,
    ] = UNSET
    is_quality_control_fail: Union[None, Unset, bool] = UNSET
    service_private_comments: Union[None, Unset, str] = UNSET
    client_company_id: Union[None, Unset, int] = UNSET
    client_company_name: Union[None, Unset, str] = UNSET
    client_site_name: Union[None, Unset, str] = UNSET
    client_legacy_id: Union[None, Unset, str] = UNSET
    business_from_time: Union[None, Unset, datetime.datetime] = UNSET
    business_to_time: Union[None, Unset, datetime.datetime] = UNSET
    timeframe: Union[
        None,
        Unset,
        QualerApiModelsServiceOrdersToProviderServiceOrderResponseModelTimeframe,
    ] = UNSET
    site_access_notes: Union[None, Unset, str] = UNSET
    desired_date: Union[None, Unset, datetime.datetime] = UNSET
    deadline_date: Union[None, Unset, datetime.datetime] = UNSET
    request_from_date: Union[None, Unset, datetime.datetime] = UNSET
    request_from_time: Union[None, Unset, datetime.datetime] = UNSET
    request_to_date: Union[None, Unset, datetime.datetime] = UNSET
    request_to_time: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_order_id = self.service_order_id

        guid: Union[None, Unset, str] = UNSET
        if self.guid and not isinstance(self.guid, Unset):
            guid = str(self.guid)

        service_order_number = self.service_order_number

        custom_order_number = self.custom_order_number

        due_date: Union[None, Unset, str]
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        elif isinstance(self.due_date, datetime.datetime):
            due_date = self.due_date.isoformat()
        else:
            due_date = self.due_date

        assets = self.assets

        completed_assets = self.completed_assets

        order_status: Union[None, Unset, str] = UNSET
        if self.order_status and not isinstance(self.order_status, Unset):
            order_status = self.order_status.value

        is_quality_control_fail = self.is_quality_control_fail

        service_private_comments = self.service_private_comments

        client_company_id = self.client_company_id

        client_company_name = self.client_company_name

        client_site_name = self.client_site_name

        client_legacy_id = self.client_legacy_id

        business_from_time: Union[None, Unset, str]
        if isinstance(self.business_from_time, Unset):
            business_from_time = UNSET
        elif isinstance(self.business_from_time, datetime.datetime):
            business_from_time = self.business_from_time.isoformat()
        else:
            business_from_time = self.business_from_time

        business_to_time: Union[None, Unset, str]
        if isinstance(self.business_to_time, Unset):
            business_to_time = UNSET
        elif isinstance(self.business_to_time, datetime.datetime):
            business_to_time = self.business_to_time.isoformat()
        else:
            business_to_time = self.business_to_time

        timeframe: Union[None, Unset, str] = UNSET
        if self.timeframe and not isinstance(self.timeframe, Unset):
            timeframe = self.timeframe.value

        site_access_notes = self.site_access_notes

        desired_date: Union[None, Unset, str]
        if isinstance(self.desired_date, Unset):
            desired_date = UNSET
        elif isinstance(self.desired_date, datetime.datetime):
            desired_date = self.desired_date.isoformat()
        else:
            desired_date = self.desired_date

        deadline_date: Union[None, Unset, str]
        if isinstance(self.deadline_date, Unset):
            deadline_date = UNSET
        elif isinstance(self.deadline_date, datetime.datetime):
            deadline_date = self.deadline_date.isoformat()
        else:
            deadline_date = self.deadline_date

        request_from_date: Union[None, Unset, str]
        if isinstance(self.request_from_date, Unset):
            request_from_date = UNSET
        elif isinstance(self.request_from_date, datetime.datetime):
            request_from_date = self.request_from_date.isoformat()
        else:
            request_from_date = self.request_from_date

        request_from_time: Union[None, Unset, str]
        if isinstance(self.request_from_time, Unset):
            request_from_time = UNSET
        elif isinstance(self.request_from_time, datetime.datetime):
            request_from_time = self.request_from_time.isoformat()
        else:
            request_from_time = self.request_from_time

        request_to_date: Union[None, Unset, str]
        if isinstance(self.request_to_date, Unset):
            request_to_date = UNSET
        elif isinstance(self.request_to_date, datetime.datetime):
            request_to_date = self.request_to_date.isoformat()
        else:
            request_to_date = self.request_to_date

        request_to_time: Union[None, Unset, str]
        if isinstance(self.request_to_time, Unset):
            request_to_time = UNSET
        elif isinstance(self.request_to_time, datetime.datetime):
            request_to_time = self.request_to_time.isoformat()
        else:
            request_to_time = self.request_to_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_id is not UNSET:
            field_dict["ServiceOrderId"] = service_order_id
        if guid is not UNSET:
            field_dict["Guid"] = guid
        if service_order_number is not UNSET:
            field_dict["ServiceOrderNumber"] = service_order_number
        if custom_order_number is not UNSET:
            field_dict["CustomOrderNumber"] = custom_order_number
        if due_date is not UNSET:
            field_dict["DueDate"] = due_date
        if assets is not UNSET:
            field_dict["Assets"] = assets
        if completed_assets is not UNSET:
            field_dict["CompletedAssets"] = completed_assets
        if order_status is not UNSET:
            field_dict["OrderStatus"] = order_status
        if is_quality_control_fail is not UNSET:
            field_dict["IsQualityControlFail"] = is_quality_control_fail
        if service_private_comments is not UNSET:
            field_dict["ServicePrivateComments"] = service_private_comments
        if client_company_id is not UNSET:
            field_dict["ClientCompanyId"] = client_company_id
        if client_company_name is not UNSET:
            field_dict["ClientCompanyName"] = client_company_name
        if client_site_name is not UNSET:
            field_dict["ClientSiteName"] = client_site_name
        if client_legacy_id is not UNSET:
            field_dict["ClientLegacyId"] = client_legacy_id
        if business_from_time is not UNSET:
            field_dict["BusinessFromTime"] = business_from_time
        if business_to_time is not UNSET:
            field_dict["BusinessToTime"] = business_to_time
        if timeframe is not UNSET:
            field_dict["Timeframe"] = timeframe
        if site_access_notes is not UNSET:
            field_dict["SiteAccessNotes"] = site_access_notes
        if desired_date is not UNSET:
            field_dict["DesiredDate"] = desired_date
        if deadline_date is not UNSET:
            field_dict["DeadlineDate"] = deadline_date
        if request_from_date is not UNSET:
            field_dict["RequestFromDate"] = request_from_date
        if request_from_time is not UNSET:
            field_dict["RequestFromTime"] = request_from_time
        if request_to_date is not UNSET:
            field_dict["RequestToDate"] = request_to_date
        if request_to_time is not UNSET:
            field_dict["RequestToTime"] = request_to_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_id = d.pop("ServiceOrderId", UNSET)

        _guid = d.pop("Guid", UNSET)
        guid: Union[None, Unset, UUID]
        if isinstance(_guid, Unset):
            guid = UNSET
        else:
            guid = UUID(_guid)

        service_order_number = d.pop("ServiceOrderNumber", UNSET)

        custom_order_number = d.pop("CustomOrderNumber", UNSET)

        def _parse_due_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_date_type_0 = isoparse(data)

                return due_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        due_date = _parse_due_date(d.pop("DueDate", UNSET))

        assets = d.pop("Assets", UNSET)

        completed_assets = d.pop("CompletedAssets", UNSET)

        _order_status = d.pop("OrderStatus", UNSET)
        order_status: Union[
            None,
            Unset,
            QualerApiModelsServiceOrdersToProviderServiceOrderResponseModelOrderStatus,
        ]
        if isinstance(_order_status, Unset):
            order_status = UNSET
        else:
            order_status = QualerApiModelsServiceOrdersToProviderServiceOrderResponseModelOrderStatus(
                _order_status
            )

        is_quality_control_fail = d.pop("IsQualityControlFail", UNSET)

        service_private_comments = d.pop("ServicePrivateComments", UNSET)

        client_company_id = d.pop("ClientCompanyId", UNSET)

        client_company_name = d.pop("ClientCompanyName", UNSET)

        client_site_name = d.pop("ClientSiteName", UNSET)

        client_legacy_id = d.pop("ClientLegacyId", UNSET)

        def _parse_business_from_time(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                business_from_time_type_0 = isoparse(data)

                return business_from_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        business_from_time = _parse_business_from_time(d.pop("BusinessFromTime", UNSET))

        def _parse_business_to_time(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                business_to_time_type_0 = isoparse(data)

                return business_to_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        business_to_time = _parse_business_to_time(d.pop("BusinessToTime", UNSET))

        _timeframe = d.pop("Timeframe", UNSET)
        timeframe: Union[
            None,
            Unset,
            QualerApiModelsServiceOrdersToProviderServiceOrderResponseModelTimeframe,
        ]
        if isinstance(_timeframe, Unset):
            timeframe = UNSET
        else:
            timeframe = QualerApiModelsServiceOrdersToProviderServiceOrderResponseModelTimeframe(
                _timeframe
            )

        site_access_notes = d.pop("SiteAccessNotes", UNSET)

        def _parse_desired_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                desired_date_type_0 = isoparse(data)

                return desired_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        desired_date = _parse_desired_date(d.pop("DesiredDate", UNSET))

        def _parse_deadline_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deadline_date_type_0 = isoparse(data)

                return deadline_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        deadline_date = _parse_deadline_date(d.pop("DeadlineDate", UNSET))

        def _parse_request_from_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                request_from_date_type_0 = isoparse(data)

                return request_from_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        request_from_date = _parse_request_from_date(d.pop("RequestFromDate", UNSET))

        def _parse_request_from_time(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                request_from_time_type_0 = isoparse(data)

                return request_from_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        request_from_time = _parse_request_from_time(d.pop("RequestFromTime", UNSET))

        def _parse_request_to_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                request_to_date_type_0 = isoparse(data)

                return request_to_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        request_to_date = _parse_request_to_date(d.pop("RequestToDate", UNSET))

        def _parse_request_to_time(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                request_to_time_type_0 = isoparse(data)

                return request_to_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        request_to_time = _parse_request_to_time(d.pop("RequestToTime", UNSET))

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
