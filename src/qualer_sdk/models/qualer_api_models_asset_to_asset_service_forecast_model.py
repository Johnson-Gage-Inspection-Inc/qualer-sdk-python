import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="AssetToAssetServiceForecastModel")


def _isoformat_if_datetime(value: Any) -> Any:
    return value.isoformat() if isinstance(value, datetime.datetime) else value


@_attrs_define
class AssetToAssetServiceForecastModel:
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
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if self.company_id is not None:
            field_dict["CompanyId"] = self.company_id
        if self.asset_id is not None:
            field_dict["AssetId"] = self.asset_id
        if self.site_id is not None:
            field_dict["SiteId"] = self.site_id
        if self.asset_service_record_id is not None:
            field_dict["AssetServiceRecordId"] = self.asset_service_record_id
        if self.serial_number is not None:
            field_dict["SerialNumber"] = self.serial_number
        if self.asset_user is not None:
            field_dict["AssetUser"] = self.asset_user
        if self.asset_tag is not None:
            field_dict["AssetTag"] = self.asset_tag
        if self.equipment_id is not None:
            field_dict["EquipmentId"] = self.equipment_id
        if self.asset_name is not None:
            field_dict["AssetName"] = self.asset_name
        if self.category_name is not None:
            field_dict["CategoryName"] = self.category_name
        if self.manufacturer_name is not None:
            field_dict["ManufacturerName"] = self.manufacturer_name
        if self.site_name is not None:
            field_dict["SiteName"] = self.site_name
        if self.maintenance_plan_id is not None:
            field_dict["MaintenancePlanId"] = self.maintenance_plan_id
        if self.maintenance_plan_name is not None:
            field_dict["MaintenancePlanName"] = self.maintenance_plan_name
        if self.maintenance_task_id is not None:
            field_dict["MaintenanceTaskId"] = self.maintenance_task_id
        if self.maintenance_task_name is not None:
            field_dict["MaintenanceTaskName"] = self.maintenance_task_name
        if self.next_service_date is not None:
            field_dict["NextServiceDate"] = _isoformat_if_datetime(self.next_service_date)
        if self.advance_recall_date is not None:
            field_dict["AdvanceRecallDate"] = _isoformat_if_datetime(self.advance_recall_date)
        if self.grace_period_date is not None:
            field_dict["GracePeriodDate"] = _isoformat_if_datetime(self.grace_period_date)
        if self.certificate_next_service_date is not None:
            field_dict["CertificateNextServiceDate"] = _isoformat_if_datetime(
                self.certificate_next_service_date
            )
        if self.service_interval is not None:
            field_dict["ServiceInterval"] = self.service_interval
        if self.interval_cycle is not None:
            field_dict["IntervalCycle"] = self.interval_cycle
        if self.interval_length is not None:
            field_dict["IntervalLength"] = self.interval_length
        if self.on_day is not None:
            field_dict["OnDay"] = self.on_day
        if self.on_month is not None:
            field_dict["OnMonth"] = self.on_month
        if self.on_week_days is not None:
            field_dict["OnWeekDays"] = self.on_week_days
        if self.weekday_of_month is not None:
            field_dict["WeekdayOfMonth"] = self.weekday_of_month
        if self.advance_recall_period is not None:
            field_dict["AdvanceRecallPeriod"] = self.advance_recall_period
        if self.days_before_due is not None:
            field_dict["DaysBeforeDue"] = self.days_before_due
        if self.past_due_grace_period is not None:
            field_dict["PastDueGracePeriod"] = self.past_due_grace_period
        if self.days_after_due is not None:
            field_dict["DaysAfterDue"] = self.days_after_due
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
            except Exception:
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
            except Exception:
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
            except Exception:
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
            except Exception:
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
