import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.qualer_api_models_asset_to_asset_service_forecast_model_on_day import (
    QualerApiModelsAssetToAssetServiceForecastModelOnDay,
)
from ..models.qualer_api_models_asset_to_asset_service_forecast_model_on_month import (
    QualerApiModelsAssetToAssetServiceForecastModelOnMonth,
)
from ..models.qualer_api_models_asset_to_asset_service_forecast_model_on_week_days import (
    QualerApiModelsAssetToAssetServiceForecastModelOnWeekDays,
)
from ..models.qualer_api_models_asset_to_asset_service_forecast_model_weekday_of_month import (
    QualerApiModelsAssetToAssetServiceForecastModelWeekdayOfMonth,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsAssetToAssetServiceForecastModel")


@_attrs_define
class QualerApiModelsAssetToAssetServiceForecastModel:
    """
    Attributes:
        company_id (Union[Unset, int]):
        asset_id (Union[Unset, int]):
        site_id (Union[Unset, int]):
        asset_service_record_id (Union[Unset, int]):
        serial_number (Union[Unset, str]):
        asset_user (Union[Unset, str]):
        asset_tag (Union[Unset, str]):
        equipment_id (Union[Unset, str]):
        asset_name (Union[Unset, str]):
        category_name (Union[Unset, str]):
        manufacturer_name (Union[Unset, str]):
        site_name (Union[Unset, str]):
        maintenance_plan_id (Union[Unset, int]):
        maintenance_plan_name (Union[Unset, str]):
        maintenance_task_id (Union[Unset, int]):
        maintenance_task_name (Union[Unset, str]):
        next_service_date (Union[Unset, datetime.datetime]):
        advance_recall_date (Union[Unset, datetime.datetime]):
        grace_period_date (Union[Unset, datetime.datetime]):
        certificate_next_service_date (Union[Unset, datetime.datetime]):
        service_interval (Union[Unset, str]):
        interval_cycle (Union[Unset, str]):
        interval_length (Union[Unset, int]):
        on_day (Union[Unset, QualerApiModelsAssetToAssetServiceForecastModelOnDay]):
        on_month (Union[Unset, QualerApiModelsAssetToAssetServiceForecastModelOnMonth]):
        on_week_days (Union[Unset, QualerApiModelsAssetToAssetServiceForecastModelOnWeekDays]):
        weekday_of_month (Union[Unset, QualerApiModelsAssetToAssetServiceForecastModelWeekdayOfMonth]):
        advance_recall_period (Union[Unset, str]):
        days_before_due (Union[Unset, int]):
        past_due_grace_period (Union[Unset, str]):
        days_after_due (Union[Unset, int]):
    """

    company_id: Union[Unset, int] = UNSET
    asset_id: Union[Unset, int] = UNSET
    site_id: Union[Unset, int] = UNSET
    asset_service_record_id: Union[Unset, int] = UNSET
    serial_number: Union[Unset, str] = UNSET
    asset_user: Union[Unset, str] = UNSET
    asset_tag: Union[Unset, str] = UNSET
    equipment_id: Union[Unset, str] = UNSET
    asset_name: Union[Unset, str] = UNSET
    category_name: Union[Unset, str] = UNSET
    manufacturer_name: Union[Unset, str] = UNSET
    site_name: Union[Unset, str] = UNSET
    maintenance_plan_id: Union[Unset, int] = UNSET
    maintenance_plan_name: Union[Unset, str] = UNSET
    maintenance_task_id: Union[Unset, int] = UNSET
    maintenance_task_name: Union[Unset, str] = UNSET
    next_service_date: Union[Unset, datetime.datetime] = UNSET
    advance_recall_date: Union[Unset, datetime.datetime] = UNSET
    grace_period_date: Union[Unset, datetime.datetime] = UNSET
    certificate_next_service_date: Union[Unset, datetime.datetime] = UNSET
    service_interval: Union[Unset, str] = UNSET
    interval_cycle: Union[Unset, str] = UNSET
    interval_length: Union[Unset, int] = UNSET
    on_day: Union[Unset, QualerApiModelsAssetToAssetServiceForecastModelOnDay] = UNSET
    on_month: Union[Unset, QualerApiModelsAssetToAssetServiceForecastModelOnMonth] = (
        UNSET
    )
    on_week_days: Union[
        Unset, QualerApiModelsAssetToAssetServiceForecastModelOnWeekDays
    ] = UNSET
    weekday_of_month: Union[
        Unset, QualerApiModelsAssetToAssetServiceForecastModelWeekdayOfMonth
    ] = UNSET
    advance_recall_period: Union[Unset, str] = UNSET
    days_before_due: Union[Unset, int] = UNSET
    past_due_grace_period: Union[Unset, str] = UNSET
    days_after_due: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        next_service_date: Union[Unset, str] = UNSET
        if not isinstance(self.next_service_date, Unset):
            next_service_date = self.next_service_date.isoformat()

        advance_recall_date: Union[Unset, str] = UNSET
        if not isinstance(self.advance_recall_date, Unset):
            advance_recall_date = self.advance_recall_date.isoformat()

        grace_period_date: Union[Unset, str] = UNSET
        if not isinstance(self.grace_period_date, Unset):
            grace_period_date = self.grace_period_date.isoformat()

        certificate_next_service_date: Union[Unset, str] = UNSET
        if not isinstance(self.certificate_next_service_date, Unset):
            certificate_next_service_date = (
                self.certificate_next_service_date.isoformat()
            )

        service_interval = self.service_interval

        interval_cycle = self.interval_cycle

        interval_length = self.interval_length

        on_day: Union[Unset, str] = UNSET
        if not isinstance(self.on_day, Unset):
            on_day = self.on_day.value

        on_month: Union[Unset, str] = UNSET
        if not isinstance(self.on_month, Unset):
            on_month = self.on_month.value

        on_week_days: Union[Unset, str] = UNSET
        if not isinstance(self.on_week_days, Unset):
            on_week_days = self.on_week_days.value

        weekday_of_month: Union[Unset, str] = UNSET
        if not isinstance(self.weekday_of_month, Unset):
            weekday_of_month = self.weekday_of_month.value

        advance_recall_period = self.advance_recall_period

        days_before_due = self.days_before_due

        past_due_grace_period = self.past_due_grace_period

        days_after_due = self.days_after_due

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_id is not UNSET:
            field_dict["CompanyId"] = company_id
        if asset_id is not UNSET:
            field_dict["AssetId"] = asset_id
        if site_id is not UNSET:
            field_dict["SiteId"] = site_id
        if asset_service_record_id is not UNSET:
            field_dict["AssetServiceRecordId"] = asset_service_record_id
        if serial_number is not UNSET:
            field_dict["SerialNumber"] = serial_number
        if asset_user is not UNSET:
            field_dict["AssetUser"] = asset_user
        if asset_tag is not UNSET:
            field_dict["AssetTag"] = asset_tag
        if equipment_id is not UNSET:
            field_dict["EquipmentId"] = equipment_id
        if asset_name is not UNSET:
            field_dict["AssetName"] = asset_name
        if category_name is not UNSET:
            field_dict["CategoryName"] = category_name
        if manufacturer_name is not UNSET:
            field_dict["ManufacturerName"] = manufacturer_name
        if site_name is not UNSET:
            field_dict["SiteName"] = site_name
        if maintenance_plan_id is not UNSET:
            field_dict["MaintenancePlanId"] = maintenance_plan_id
        if maintenance_plan_name is not UNSET:
            field_dict["MaintenancePlanName"] = maintenance_plan_name
        if maintenance_task_id is not UNSET:
            field_dict["MaintenanceTaskId"] = maintenance_task_id
        if maintenance_task_name is not UNSET:
            field_dict["MaintenanceTaskName"] = maintenance_task_name
        if next_service_date is not UNSET:
            field_dict["NextServiceDate"] = next_service_date
        if advance_recall_date is not UNSET:
            field_dict["AdvanceRecallDate"] = advance_recall_date
        if grace_period_date is not UNSET:
            field_dict["GracePeriodDate"] = grace_period_date
        if certificate_next_service_date is not UNSET:
            field_dict["CertificateNextServiceDate"] = certificate_next_service_date
        if service_interval is not UNSET:
            field_dict["ServiceInterval"] = service_interval
        if interval_cycle is not UNSET:
            field_dict["IntervalCycle"] = interval_cycle
        if interval_length is not UNSET:
            field_dict["IntervalLength"] = interval_length
        if on_day is not UNSET:
            field_dict["OnDay"] = on_day
        if on_month is not UNSET:
            field_dict["OnMonth"] = on_month
        if on_week_days is not UNSET:
            field_dict["OnWeekDays"] = on_week_days
        if weekday_of_month is not UNSET:
            field_dict["WeekdayOfMonth"] = weekday_of_month
        if advance_recall_period is not UNSET:
            field_dict["AdvanceRecallPeriod"] = advance_recall_period
        if days_before_due is not UNSET:
            field_dict["DaysBeforeDue"] = days_before_due
        if past_due_grace_period is not UNSET:
            field_dict["PastDueGracePeriod"] = past_due_grace_period
        if days_after_due is not UNSET:
            field_dict["DaysAfterDue"] = days_after_due

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_id = d.pop("CompanyId", UNSET)

        asset_id = d.pop("AssetId", UNSET)

        site_id = d.pop("SiteId", UNSET)

        asset_service_record_id = d.pop("AssetServiceRecordId", UNSET)

        serial_number = d.pop("SerialNumber", UNSET)

        asset_user = d.pop("AssetUser", UNSET)

        asset_tag = d.pop("AssetTag", UNSET)

        equipment_id = d.pop("EquipmentId", UNSET)

        asset_name = d.pop("AssetName", UNSET)

        category_name = d.pop("CategoryName", UNSET)

        manufacturer_name = d.pop("ManufacturerName", UNSET)

        site_name = d.pop("SiteName", UNSET)

        maintenance_plan_id = d.pop("MaintenancePlanId", UNSET)

        maintenance_plan_name = d.pop("MaintenancePlanName", UNSET)

        maintenance_task_id = d.pop("MaintenanceTaskId", UNSET)

        maintenance_task_name = d.pop("MaintenanceTaskName", UNSET)

        _next_service_date = d.pop("NextServiceDate", UNSET)
        next_service_date: Union[Unset, datetime.datetime]
        if isinstance(_next_service_date, Unset):
            next_service_date = UNSET
        else:
            next_service_date = isoparse(_next_service_date)

        _advance_recall_date = d.pop("AdvanceRecallDate", UNSET)
        advance_recall_date: Union[Unset, datetime.datetime]
        if isinstance(_advance_recall_date, Unset):
            advance_recall_date = UNSET
        else:
            advance_recall_date = isoparse(_advance_recall_date)

        _grace_period_date = d.pop("GracePeriodDate", UNSET)
        grace_period_date: Union[Unset, datetime.datetime]
        if isinstance(_grace_period_date, Unset):
            grace_period_date = UNSET
        else:
            grace_period_date = isoparse(_grace_period_date)

        _certificate_next_service_date = d.pop("CertificateNextServiceDate", UNSET)
        certificate_next_service_date: Union[Unset, datetime.datetime]
        if isinstance(_certificate_next_service_date, Unset):
            certificate_next_service_date = UNSET
        else:
            certificate_next_service_date = isoparse(_certificate_next_service_date)

        service_interval = d.pop("ServiceInterval", UNSET)

        interval_cycle = d.pop("IntervalCycle", UNSET)

        interval_length = d.pop("IntervalLength", UNSET)

        _on_day = d.pop("OnDay", UNSET)
        on_day: Union[Unset, QualerApiModelsAssetToAssetServiceForecastModelOnDay]
        if isinstance(_on_day, Unset):
            on_day = UNSET
        else:
            on_day = QualerApiModelsAssetToAssetServiceForecastModelOnDay(_on_day)

        _on_month = d.pop("OnMonth", UNSET)
        on_month: Union[Unset, QualerApiModelsAssetToAssetServiceForecastModelOnMonth]
        if isinstance(_on_month, Unset):
            on_month = UNSET
        else:
            on_month = QualerApiModelsAssetToAssetServiceForecastModelOnMonth(_on_month)

        _on_week_days = d.pop("OnWeekDays", UNSET)
        on_week_days: Union[
            Unset, QualerApiModelsAssetToAssetServiceForecastModelOnWeekDays
        ]
        if isinstance(_on_week_days, Unset):
            on_week_days = UNSET
        else:
            on_week_days = QualerApiModelsAssetToAssetServiceForecastModelOnWeekDays(
                _on_week_days
            )

        _weekday_of_month = d.pop("WeekdayOfMonth", UNSET)
        weekday_of_month: Union[
            Unset, QualerApiModelsAssetToAssetServiceForecastModelWeekdayOfMonth
        ]
        if isinstance(_weekday_of_month, Unset):
            weekday_of_month = UNSET
        else:
            weekday_of_month = (
                QualerApiModelsAssetToAssetServiceForecastModelWeekdayOfMonth(
                    _weekday_of_month
                )
            )

        advance_recall_period = d.pop("AdvanceRecallPeriod", UNSET)

        days_before_due = d.pop("DaysBeforeDue", UNSET)

        past_due_grace_period = d.pop("PastDueGracePeriod", UNSET)

        days_after_due = d.pop("DaysAfterDue", UNSET)

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

        qualer_api_models_asset_to_asset_service_forecast_model.additional_properties = (
            d
        )
        return qualer_api_models_asset_to_asset_service_forecast_model

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
