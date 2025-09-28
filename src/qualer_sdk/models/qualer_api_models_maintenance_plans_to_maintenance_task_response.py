from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MaintenancePlansToMaintenanceTaskResponse")


@_attrs_define
class MaintenancePlansToMaintenanceTaskResponse:
    """
    Attributes:
        segment_name (Optional[str]):
        service_level_id (Optional[int]):
        display_order (Optional[int]):
        service_notes (Optional[str]):
        interval_cycle (Optional[str]):
        interval_length (Optional[int]):
        on_day (Optional[str]):
        on_month (Optional[str]):
        on_week_days (Optional[str]):
        weekday_of_month (Optional[str]):
        color_code (Optional[int]):
        service_interval (Optional[str]):
        on_segment_id (Optional[int]):
        document_number (Optional[str]):
        document_section (Optional[str]):
        as_found_standard_group_id (Optional[int]):
        as_left_standard_group_id (Optional[int]):
        task_notes (Optional[str]):
        advance_recall_period (Optional[str]):
        days_before_due (Optional[int]):
        past_due_grace_period (Optional[str]):
        days_after_due (Optional[int]):
        use_period_in_reports (Optional[str]):
        generate_order_automatically (Optional[bool]):
        approve_upon_generation (Optional[bool]):
        generate_separate (Optional[bool]):
    """

    segment_name: Optional[str] = None
    service_level_id: Optional[int] = None
    display_order: Optional[int] = None
    service_notes: Optional[str] = None
    interval_cycle: Optional[str] = None
    interval_length: Optional[int] = None
    on_day: Optional[str] = None
    on_month: Optional[str] = None
    on_week_days: Optional[str] = None
    weekday_of_month: Optional[str] = None
    color_code: Optional[int] = None
    service_interval: Optional[str] = None
    on_segment_id: Optional[int] = None
    document_number: Optional[str] = None
    document_section: Optional[str] = None
    as_found_standard_group_id: Optional[int] = None
    as_left_standard_group_id: Optional[int] = None
    task_notes: Optional[str] = None
    advance_recall_period: Optional[str] = None
    days_before_due: Optional[int] = None
    past_due_grace_period: Optional[str] = None
    days_after_due: Optional[int] = None
    use_period_in_reports: Optional[str] = None
    generate_order_automatically: Optional[bool] = None
    approve_upon_generation: Optional[bool] = None
    generate_separate: Optional[bool] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if segment_name is not None:
            field_dict["SegmentName"] = segment_name
        if service_level_id is not None:
            field_dict["ServiceLevelId"] = service_level_id
        if display_order is not None:
            field_dict["DisplayOrder"] = display_order
        if service_notes is not None:
            field_dict["ServiceNotes"] = service_notes
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
        if color_code is not None:
            field_dict["ColorCode"] = color_code
        if service_interval is not None:
            field_dict["ServiceInterval"] = service_interval
        if on_segment_id is not None:
            field_dict["OnSegmentId"] = on_segment_id
        if document_number is not None:
            field_dict["DocumentNumber"] = document_number
        if document_section is not None:
            field_dict["DocumentSection"] = document_section
        if as_found_standard_group_id is not None:
            field_dict["AsFoundStandardGroupId"] = as_found_standard_group_id
        if as_left_standard_group_id is not None:
            field_dict["AsLeftStandardGroupId"] = as_left_standard_group_id
        if task_notes is not None:
            field_dict["TaskNotes"] = task_notes
        if advance_recall_period is not None:
            field_dict["AdvanceRecallPeriod"] = advance_recall_period
        if days_before_due is not None:
            field_dict["DaysBeforeDue"] = days_before_due
        if past_due_grace_period is not None:
            field_dict["PastDueGracePeriod"] = past_due_grace_period
        if days_after_due is not None:
            field_dict["DaysAfterDue"] = days_after_due
        if use_period_in_reports is not None:
            field_dict["UsePeriodInReports"] = use_period_in_reports
        if generate_order_automatically is not None:
            field_dict["GenerateOrderAutomatically"] = generate_order_automatically
        if approve_upon_generation is not None:
            field_dict["ApproveUponGeneration"] = approve_upon_generation
        if generate_separate is not None:
            field_dict["GenerateSeparate"] = generate_separate
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        segment_name = d.pop("SegmentName", None)
        service_level_id = d.pop("ServiceLevelId", None)
        display_order = d.pop("DisplayOrder", None)
        service_notes = d.pop("ServiceNotes", None)
        interval_cycle = d.pop("IntervalCycle", None)
        interval_length = d.pop("IntervalLength", None)
        on_day = d.pop("OnDay", None)
        on_month = d.pop("OnMonth", None)
        on_week_days = d.pop("OnWeekDays", None)
        weekday_of_month = d.pop("WeekdayOfMonth", None)
        color_code = d.pop("ColorCode", None)
        service_interval = d.pop("ServiceInterval", None)
        on_segment_id = d.pop("OnSegmentId", None)
        document_number = d.pop("DocumentNumber", None)
        document_section = d.pop("DocumentSection", None)
        as_found_standard_group_id = d.pop("AsFoundStandardGroupId", None)
        as_left_standard_group_id = d.pop("AsLeftStandardGroupId", None)
        task_notes = d.pop("TaskNotes", None)
        advance_recall_period = d.pop("AdvanceRecallPeriod", None)
        days_before_due = d.pop("DaysBeforeDue", None)
        past_due_grace_period = d.pop("PastDueGracePeriod", None)
        days_after_due = d.pop("DaysAfterDue", None)
        use_period_in_reports = d.pop("UsePeriodInReports", None)
        generate_order_automatically = d.pop("GenerateOrderAutomatically", None)
        approve_upon_generation = d.pop("ApproveUponGeneration", None)
        generate_separate = d.pop("GenerateSeparate", None)
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
        qualer_api_models_maintenance_plans_to_maintenance_task_response.additional_properties = d
        return qualer_api_models_maintenance_plans_to_maintenance_task_response

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
