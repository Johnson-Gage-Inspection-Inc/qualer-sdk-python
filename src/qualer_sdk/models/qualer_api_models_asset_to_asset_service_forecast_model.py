import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="QualerApiModelsAssetToAssetServiceForecastModel")


@_attrs_define
class QualerApiModelsAssetToAssetServiceForecastModel:
    """
    Attributes:
        company_id (Optional[int]):
        asset_id (Optional[int]):
        site_id (Optional[int]):
        asset_service_record_id (Optional[int]):
        serial_number (Optional[str]):
        asset_user (Optional[str]):
        asset_tag (Optional[str]):
        equipment_id (Optional[str]):
        asset_name (Optional[str]):
        category_name (Optional[str]):
        manufacturer_name (Optional[str]):
        site_name (Optional[str]):
        maintenance_plan_id (Optional[int]):
        maintenance_plan_name (Optional[str]):
        maintenance_task_id (Optional[int]):
        maintenance_task_name (Optional[str]):
        next_service_date (Optional[datetime.datetime]):
        advance_recall_date (Optional[datetime.datetime]):
        grace_period_date (Optional[datetime.datetime]):
        certificate_next_service_date (Optional[datetime.datetime]):
        service_interval (Optional[str]):
        interval_cycle (Optional[str]):
        interval_length (Optional[int]):
        on_day (Optional[int]):
        on_month (Optional[int]):
        on_week_days (Optional[int]):
        weekday_of_month (Optional[int]):
        advance_recall_period (Optional[str]):
        days_before_due (Optional[int]):
        past_due_grace_period (Optional[str]):
        days_after_due (Optional[int]):
    """

    company_id: Optional[int] = None
    asset_id: Optional[int] = None
    site_id: Optional[int] = None
    asset_service_record_id: Optional[int] = None
    serial_number: Optional[str] = None
    asset_user: Optional[str] = None
    asset_tag: Optional[str] = None
    equipment_id: Optional[str] = None
    asset_name: Optional[str] = None
    category_name: Optional[str] = None
    manufacturer_name: Optional[str] = None
    site_name: Optional[str] = None
    maintenance_plan_id: Optional[int] = None
    maintenance_plan_name: Optional[str] = None
    maintenance_task_id: Optional[int] = None
    maintenance_task_name: Optional[str] = None
    next_service_date: Optional[datetime.datetime] = None
    advance_recall_date: Optional[datetime.datetime] = None
    grace_period_date: Optional[datetime.datetime] = None
    certificate_next_service_date: Optional[datetime.datetime] = None
    service_interval: Optional[str] = None
    interval_cycle: Optional[str] = None
    interval_length: Optional[int] = None
    on_day: Optional[int] = None
    on_month: Optional[int] = None
    on_week_days: Optional[int] = None
    weekday_of_month: Optional[int] = None
    advance_recall_period: Optional[str] = None
    days_before_due: Optional[int] = None
    past_due_grace_period: Optional[str] = None
    days_after_due: Optional[int] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        company_id = self.company_id

        asset_id = self.asset_id

        site_id = self.site_id

        asset_service_record_id = self.asset_service_record_id

        serial_number = self.serial_number

        asset_user = self.asset_user

        asset_tag = self.asset_tag

        equipment_id = self.equipment_id

        asset_name = self.asset_name

        category_name = self.category_name

        manufacturer_name = self.manufacturer_name

        site_name = self.site_name

        maintenance_plan_id = self.maintenance_plan_id

        maintenance_plan_name = self.maintenance_plan_name

        maintenance_task_id = self.maintenance_task_id

        maintenance_task_name = self.maintenance_task_name

        next_service_date: Optional[str]
        if not self.next_service_date:
            next_service_date = None
        elif isinstance(self.next_service_date, datetime.datetime):
            next_service_date = self.next_service_date.isoformat()
        else:
            next_service_date = self.next_service_date

        advance_recall_date: Optional[str]
        if not self.advance_recall_date:
            advance_recall_date = None
        elif isinstance(self.advance_recall_date, datetime.datetime):
            advance_recall_date = self.advance_recall_date.isoformat()
        else:
            advance_recall_date = self.advance_recall_date

        grace_period_date: Optional[str]
        if not self.grace_period_date:
            grace_period_date = None
        elif isinstance(self.grace_period_date, datetime.datetime):
            grace_period_date = self.grace_period_date.isoformat()
        else:
            grace_period_date = self.grace_period_date

        certificate_next_service_date: Optional[str]
        if not self.certificate_next_service_date:
            certificate_next_service_date = None
        elif isinstance(self.certificate_next_service_date, datetime.datetime):
            certificate_next_service_date = self.certificate_next_service_date.isoformat()
        else:
            certificate_next_service_date = self.certificate_next_service_date

        service_interval = self.service_interval

        interval_cycle = self.interval_cycle

        interval_length = self.interval_length

        on_day = self.on_day

        on_month = self.on_month

        on_week_days = self.on_week_days

        weekday_of_month = self.weekday_of_month

        advance_recall_period = self.advance_recall_period

        days_before_due = self.days_before_due

        past_due_grace_period = self.past_due_grace_period

        days_after_due = self.days_after_due

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_id is not None:
            field_dict["CompanyId"] = company_id
        if asset_id is not None:
            field_dict["AssetId"] = asset_id
        if site_id is not None:
            field_dict["SiteId"] = site_id
        if asset_service_record_id is not None:
            field_dict["AssetServiceRecordId"] = asset_service_record_id
        if serial_number is not None:
            field_dict["SerialNumber"] = serial_number
        if asset_user is not None:
            field_dict["AssetUser"] = asset_user
        if asset_tag is not None:
            field_dict["AssetTag"] = asset_tag
        if equipment_id is not None:
            field_dict["EquipmentId"] = equipment_id
        if asset_name is not None:
            field_dict["AssetName"] = asset_name
        if category_name is not None:
            field_dict["CategoryName"] = category_name
        if manufacturer_name is not None:
            field_dict["ManufacturerName"] = manufacturer_name
        if site_name is not None:
            field_dict["SiteName"] = site_name
        if maintenance_plan_id is not None:
            field_dict["MaintenancePlanId"] = maintenance_plan_id
        if maintenance_plan_name is not None:
            field_dict["MaintenancePlanName"] = maintenance_plan_name
        if maintenance_task_id is not None:
            field_dict["MaintenanceTaskId"] = maintenance_task_id
        if maintenance_task_name is not None:
            field_dict["MaintenanceTaskName"] = maintenance_task_name
        if next_service_date is not None:
            field_dict["NextServiceDate"] = next_service_date
        if advance_recall_date is not None:
            field_dict["AdvanceRecallDate"] = advance_recall_date
        if grace_period_date is not None:
            field_dict["GracePeriodDate"] = grace_period_date
        if certificate_next_service_date is not None:
            field_dict["CertificateNextServiceDate"] = certificate_next_service_date
        if service_interval is not None:
            field_dict["ServiceInterval"] = service_interval
        if interval_cycle is not None:
            field_dict["IntervalCycle"] = interval_cycle
        if interval_length is not None:
            field_dict["IntervalLength"] = interval_length
        if on_day is not None:
            field_dict["OnDay"] = on_day
        if on_month is not None:
            field_dict["OnMonth"] = on_month
        if on_week_days is not None:
            field_dict["OnWeekDays"] = on_week_days
        if weekday_of_month is not None:
            field_dict["WeekdayOfMonth"] = weekday_of_month
        if advance_recall_period is not None:
            field_dict["AdvanceRecallPeriod"] = advance_recall_period
        if days_before_due is not None:
            field_dict["DaysBeforeDue"] = days_before_due
        if past_due_grace_period is not None:
            field_dict["PastDueGracePeriod"] = past_due_grace_period
        if days_after_due is not None:
            field_dict["DaysAfterDue"] = days_after_due

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_id = d.pop("CompanyId", None)

        asset_id = d.pop("AssetId", None)

        site_id = d.pop("SiteId", None)

        asset_service_record_id = d.pop("AssetServiceRecordId", None)

        serial_number = d.pop("SerialNumber", None)

        asset_user = d.pop("AssetUser", None)

        asset_tag = d.pop("AssetTag", None)

        equipment_id = d.pop("EquipmentId", None)

        asset_name = d.pop("AssetName", None)

        category_name = d.pop("CategoryName", None)

        manufacturer_name = d.pop("ManufacturerName", None)

        site_name = d.pop("SiteName", None)

        maintenance_plan_id = d.pop("MaintenancePlanId", None)

        maintenance_plan_name = d.pop("MaintenancePlanName", None)

        maintenance_task_id = d.pop("MaintenanceTaskId", None)

        maintenance_task_name = d.pop("MaintenanceTaskName", None)

        def _parse_next_service_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_service_date_type_0 = isoparse(data)

                return next_service_date_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        next_service_date = _parse_next_service_date(d.pop("NextServiceDate", None))

        def _parse_advance_recall_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                advance_recall_date_type_0 = isoparse(data)

                return advance_recall_date_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        advance_recall_date = _parse_advance_recall_date(d.pop("AdvanceRecallDate", None))

        def _parse_grace_period_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                grace_period_date_type_0 = isoparse(data)

                return grace_period_date_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        grace_period_date = _parse_grace_period_date(d.pop("GracePeriodDate", None))

        def _parse_certificate_next_service_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                certificate_next_service_date_type_0 = isoparse(data)

                return certificate_next_service_date_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        certificate_next_service_date = _parse_certificate_next_service_date(
            d.pop("CertificateNextServiceDate", None)
        )

        service_interval = d.pop("ServiceInterval", None)

        interval_cycle = d.pop("IntervalCycle", None)

        interval_length = d.pop("IntervalLength", None)

        on_day = d.pop("OnDay", None)

        on_month = d.pop("OnMonth", None)

        on_week_days = d.pop("OnWeekDays", None)

        weekday_of_month = d.pop("WeekdayOfMonth", None)

        advance_recall_period = d.pop("AdvanceRecallPeriod", None)

        days_before_due = d.pop("DaysBeforeDue", None)

        past_due_grace_period = d.pop("PastDueGracePeriod", None)

        days_after_due = d.pop("DaysAfterDue", None)

        qualer_api_models_asset_to_asset_service_forecast_model = cls(
            company_id=company_id,
            asset_id=asset_id,
            site_id=site_id,
            asset_service_record_id=asset_service_record_id,
            serial_number=serial_number,
            asset_user=asset_user,
            asset_tag=asset_tag,
            equipment_id=equipment_id,
            asset_name=asset_name,
            category_name=category_name,
            manufacturer_name=manufacturer_name,
            site_name=site_name,
            maintenance_plan_id=maintenance_plan_id,
            maintenance_plan_name=maintenance_plan_name,
            maintenance_task_id=maintenance_task_id,
            maintenance_task_name=maintenance_task_name,
            next_service_date=next_service_date,
            advance_recall_date=advance_recall_date,
            grace_period_date=grace_period_date,
            certificate_next_service_date=certificate_next_service_date,
            service_interval=service_interval,
            interval_cycle=interval_cycle,
            interval_length=interval_length,
            on_day=on_day,
            on_month=on_month,
            on_week_days=on_week_days,
            weekday_of_month=weekday_of_month,
            advance_recall_period=advance_recall_period,
            days_before_due=days_before_due,
            past_due_grace_period=past_due_grace_period,
            days_after_due=days_after_due,
        )

        qualer_api_models_asset_to_asset_service_forecast_model.additional_properties = d
        return qualer_api_models_asset_to_asset_service_forecast_model

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
