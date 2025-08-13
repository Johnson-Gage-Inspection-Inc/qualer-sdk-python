from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsMaintenancePlansToMaintenanceTaskResponse")


@_attrs_define
class QualerApiModelsMaintenancePlansToMaintenanceTaskResponse:
    """
    Attributes:
        segment_name (Union[None, Unset, str]):
        service_level_id (Union[None, Unset, int]):
        display_order (Union[None, Unset, int]):
        service_notes (Union[None, Unset, str]):
        interval_cycle (Union[None, Unset, str]):
        interval_length (Union[None, Unset, int]):
        on_day (Union[None, Unset, str]):
        on_month (Union[None, Unset, str]):
        on_week_days (Union[None, Unset, str]):
        weekday_of_month (Union[None, Unset, str]):
        color_code (Union[None, Unset, int]):
        service_interval (Union[None, Unset, str]):
        on_segment_id (Union[None, Unset, int]):
        document_number (Union[None, Unset, str]):
        document_section (Union[None, Unset, str]):
        as_found_standard_group_id (Union[None, Unset, int]):
        as_left_standard_group_id (Union[None, Unset, int]):
        task_notes (Union[None, Unset, str]):
        advance_recall_period (Union[None, Unset, str]):
        days_before_due (Union[None, Unset, int]):
        past_due_grace_period (Union[None, Unset, str]):
        days_after_due (Union[None, Unset, int]):
        use_period_in_reports (Union[None, Unset, str]):
        generate_order_automatically (Union[None, Unset, bool]):
        approve_upon_generation (Union[None, Unset, bool]):
        generate_separate (Union[None, Unset, bool]):
    """

    segment_name: Union[None, Unset, str] = UNSET
    service_level_id: Union[None, Unset, int] = UNSET
    display_order: Union[None, Unset, int] = UNSET
    service_notes: Union[None, Unset, str] = UNSET
    interval_cycle: Union[None, Unset, str] = UNSET
    interval_length: Union[None, Unset, int] = UNSET
    on_day: Union[None, Unset, str] = UNSET
    on_month: Union[None, Unset, str] = UNSET
    on_week_days: Union[None, Unset, str] = UNSET
    weekday_of_month: Union[None, Unset, str] = UNSET
    color_code: Union[None, Unset, int] = UNSET
    service_interval: Union[None, Unset, str] = UNSET
    on_segment_id: Union[None, Unset, int] = UNSET
    document_number: Union[None, Unset, str] = UNSET
    document_section: Union[None, Unset, str] = UNSET
    as_found_standard_group_id: Union[None, Unset, int] = UNSET
    as_left_standard_group_id: Union[None, Unset, int] = UNSET
    task_notes: Union[None, Unset, str] = UNSET
    advance_recall_period: Union[None, Unset, str] = UNSET
    days_before_due: Union[None, Unset, int] = UNSET
    past_due_grace_period: Union[None, Unset, str] = UNSET
    days_after_due: Union[None, Unset, int] = UNSET
    use_period_in_reports: Union[None, Unset, str] = UNSET
    generate_order_automatically: Union[None, Unset, bool] = UNSET
    approve_upon_generation: Union[None, Unset, bool] = UNSET
    generate_separate: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        segment_name = self.segment_name

        service_level_id = self.service_level_id

        display_order = self.display_order

        service_notes = self.service_notes

        interval_cycle = self.interval_cycle

        interval_length = self.interval_length

        on_day = self.on_day

        on_month = self.on_month

        on_week_days = self.on_week_days

        weekday_of_month = self.weekday_of_month

        color_code = self.color_code

        service_interval = self.service_interval

        on_segment_id = self.on_segment_id

        document_number = self.document_number

        document_section = self.document_section

        as_found_standard_group_id = self.as_found_standard_group_id

        as_left_standard_group_id = self.as_left_standard_group_id

        task_notes = self.task_notes

        advance_recall_period = self.advance_recall_period

        days_before_due = self.days_before_due

        past_due_grace_period = self.past_due_grace_period

        days_after_due = self.days_after_due

        use_period_in_reports = self.use_period_in_reports

        generate_order_automatically = self.generate_order_automatically

        approve_upon_generation = self.approve_upon_generation

        generate_separate = self.generate_separate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if segment_name is not UNSET:
            field_dict["SegmentName"] = segment_name
        if service_level_id is not UNSET:
            field_dict["ServiceLevelId"] = service_level_id
        if display_order is not UNSET:
            field_dict["DisplayOrder"] = display_order
        if service_notes is not UNSET:
            field_dict["ServiceNotes"] = service_notes
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
        if color_code is not UNSET:
            field_dict["ColorCode"] = color_code
        if service_interval is not UNSET:
            field_dict["ServiceInterval"] = service_interval
        if on_segment_id is not UNSET:
            field_dict["OnSegmentId"] = on_segment_id
        if document_number is not UNSET:
            field_dict["DocumentNumber"] = document_number
        if document_section is not UNSET:
            field_dict["DocumentSection"] = document_section
        if as_found_standard_group_id is not UNSET:
            field_dict["AsFoundStandardGroupId"] = as_found_standard_group_id
        if as_left_standard_group_id is not UNSET:
            field_dict["AsLeftStandardGroupId"] = as_left_standard_group_id
        if task_notes is not UNSET:
            field_dict["TaskNotes"] = task_notes
        if advance_recall_period is not UNSET:
            field_dict["AdvanceRecallPeriod"] = advance_recall_period
        if days_before_due is not UNSET:
            field_dict["DaysBeforeDue"] = days_before_due
        if past_due_grace_period is not UNSET:
            field_dict["PastDueGracePeriod"] = past_due_grace_period
        if days_after_due is not UNSET:
            field_dict["DaysAfterDue"] = days_after_due
        if use_period_in_reports is not UNSET:
            field_dict["UsePeriodInReports"] = use_period_in_reports
        if generate_order_automatically is not UNSET:
            field_dict["GenerateOrderAutomatically"] = generate_order_automatically
        if approve_upon_generation is not UNSET:
            field_dict["ApproveUponGeneration"] = approve_upon_generation
        if generate_separate is not UNSET:
            field_dict["GenerateSeparate"] = generate_separate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        segment_name = d.pop("SegmentName", UNSET)

        service_level_id = d.pop("ServiceLevelId", UNSET)

        display_order = d.pop("DisplayOrder", UNSET)

        service_notes = d.pop("ServiceNotes", UNSET)

        interval_cycle = d.pop("IntervalCycle", UNSET)

        interval_length = d.pop("IntervalLength", UNSET)

        on_day = d.pop("OnDay", UNSET)

        on_month = d.pop("OnMonth", UNSET)

        on_week_days = d.pop("OnWeekDays", UNSET)

        weekday_of_month = d.pop("WeekdayOfMonth", UNSET)

        color_code = d.pop("ColorCode", UNSET)

        service_interval = d.pop("ServiceInterval", UNSET)

        on_segment_id = d.pop("OnSegmentId", UNSET)

        document_number = d.pop("DocumentNumber", UNSET)

        document_section = d.pop("DocumentSection", UNSET)

        as_found_standard_group_id = d.pop("AsFoundStandardGroupId", UNSET)

        as_left_standard_group_id = d.pop("AsLeftStandardGroupId", UNSET)

        task_notes = d.pop("TaskNotes", UNSET)

        advance_recall_period = d.pop("AdvanceRecallPeriod", UNSET)

        days_before_due = d.pop("DaysBeforeDue", UNSET)

        past_due_grace_period = d.pop("PastDueGracePeriod", UNSET)

        days_after_due = d.pop("DaysAfterDue", UNSET)

        use_period_in_reports = d.pop("UsePeriodInReports", UNSET)

        generate_order_automatically = d.pop("GenerateOrderAutomatically", UNSET)

        approve_upon_generation = d.pop("ApproveUponGeneration", UNSET)

        generate_separate = d.pop("GenerateSeparate", UNSET)

        qualer_api_models_maintenance_plans_to_maintenance_task_response = cls(
            segment_name=segment_name,
            service_level_id=service_level_id,
            display_order=display_order,
            service_notes=service_notes,
            interval_cycle=interval_cycle,
            interval_length=interval_length,
            on_day=on_day,
            on_month=on_month,
            on_week_days=on_week_days,
            weekday_of_month=weekday_of_month,
            color_code=color_code,
            service_interval=service_interval,
            on_segment_id=on_segment_id,
            document_number=document_number,
            document_section=document_section,
            as_found_standard_group_id=as_found_standard_group_id,
            as_left_standard_group_id=as_left_standard_group_id,
            task_notes=task_notes,
            advance_recall_period=advance_recall_period,
            days_before_due=days_before_due,
            past_due_grace_period=past_due_grace_period,
            days_after_due=days_after_due,
            use_period_in_reports=use_period_in_reports,
            generate_order_automatically=generate_order_automatically,
            approve_upon_generation=approve_upon_generation,
            generate_separate=generate_separate,
        )

        qualer_api_models_maintenance_plans_to_maintenance_task_response.additional_properties = (
            d
        )
        return qualer_api_models_maintenance_plans_to_maintenance_task_response

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
