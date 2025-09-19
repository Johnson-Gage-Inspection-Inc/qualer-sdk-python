import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.qualer_api_models_report_datasets_to_measurement_response_double_substitution_sequence import (
    ReportDatasetsToMeasurementResponseDoubleSubstitutionSequence,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_environment_mask import (
    ReportDatasetsToMeasurementResponseEnvironmentMask,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_guard_band_logic import (
    ReportDatasetsToMeasurementResponseGuardBandLogic,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_hysteresis_point import (
    ReportDatasetsToMeasurementResponseHysteresisPoint,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_measurement_not_taken_result import (
    ReportDatasetsToMeasurementResponseMeasurementNotTakenResult,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_measurement_point_order import (
    ReportDatasetsToMeasurementResponseMeasurementPointOrder,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_measurement_type import (
    ReportDatasetsToMeasurementResponseMeasurementType,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_precision_type import (
    ReportDatasetsToMeasurementResponsePrecisionType,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_reading_entry_logic import (
    ReportDatasetsToMeasurementResponseReadingEntryLogic,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_reading_entry_math import (
    ReportDatasetsToMeasurementResponseReadingEntryMath,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_shipment_status import (
    ReportDatasetsToMeasurementResponseShipmentStatus,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_specification_mode import (
    ReportDatasetsToMeasurementResponseSpecificationMode,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_tolerance_mode import (
    ReportDatasetsToMeasurementResponseToleranceMode,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_tolerance_type import (
    ReportDatasetsToMeasurementResponseToleranceType,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_tolerance_unit import (
    ReportDatasetsToMeasurementResponseToleranceUnit,
)
from ..models.service_result_status import ServiceResultStatus
from ..models.work_status import WorkStatus

T = TypeVar("T", bound="ReportDatasetsToMeasurementResponse")


@_attrs_define
class ReportDatasetsToMeasurementResponse:
    """
    Attributes:
        is_accredited (Optional[bool]):
        service_total (Optional[float]):
        repairs_total (Optional[float]):
        parts_total (Optional[float]):
        parameter_id (Optional[int]):
        tool_range_name (Optional[str]):
        tool_range_uncertainty (Optional[str]):
        primary_tool_last_service_date (Optional[datetime.datetime]):
        primary_tool_next_service_date (Optional[datetime.datetime]):
        primary_tool_calibrated_by (Optional[str]):
        primary_tool_tool_name (Optional[str]):
        primary_tool_tool_description (Optional[str]):
        primary_tool_tool_type_name (Optional[str]):
        primary_tool_manufacturer (Optional[str]):
        primary_tool_manufacturer_part_number (Optional[str]):
        primary_tool_serial_number (Optional[str]):
        secondary_tool_last_service_date (Optional[datetime.datetime]):
        secondary_tool_next_service_date (Optional[datetime.datetime]):
        secondary_tool_calibrated_by (Optional[str]):
        secondary_tool_tool_name (Optional[str]):
        secondary_tool_tool_description (Optional[str]):
        secondary_tool_tool_type_name (Optional[str]):
        secondary_tool_manufacturer (Optional[str]):
        secondary_tool_manufacturer_part_number (Optional[str]):
        secondary_tool_serial_number (Optional[str]):
        measurement_set_name (Optional[str]):
        decimal_places (Optional[int]):
        significant_figures (Optional[int]):
        sd_header (Optional[float]):
        cv_header (Optional[float]):
        measurement_local_time (Optional[datetime.datetime]):
        mean (Optional[float]):
        mean_raw (Optional[float]):
        mean_decimal_places (Optional[int]):
        mean_extended (Optional[str]):
        sd (Optional[float]):
        sd_raw (Optional[float]):
        sd_decimal_places (Optional[int]):
        delta (Optional[float]):
        range_ (Optional[float]):
        sd_extended (Optional[str]):
        range_extended (Optional[str]):
        delta_extended (Optional[str]):
        minimum_measured_value (Optional[float]):
        maximum_measured_value (Optional[float]):
        min_max_value_extended (Optional[str]):
        cv (Optional[float]):
        cv_raw (Optional[float]):
        cv_decimal_places (Optional[int]):
        cv_extended (Optional[str]):
        result (Optional[ServiceResultStatus]):
        range_result (Optional[bool]):
        delta_result (Optional[bool]):
        min_result (Optional[bool]):
        max_result (Optional[bool]):
        tar_result (Optional[bool]):
        tur_result (Optional[bool]):
        error_result (Optional[bool]):
        sd_result (Optional[bool]):
        cv_result (Optional[bool]):
        custom_field_result (Optional[int]):
        mu (Optional[float]):
        mu_raw (Optional[float]):
        mu_effective_dof (Optional[float]):
        mu_coverage_factor (Optional[float]):
        mu_extended (Optional[str]):
        cmc (Optional[float]):
        cmc_comments (Optional[str]):
        tur (Optional[float]):
        tur_raw (Optional[float]):
        tur_decimal_places (Optional[int]):
        tar (Optional[float]):
        tar_raw (Optional[float]):
        tar_decimal_places (Optional[int]):
        guard_band (Optional[str]):
        guard_band_logic (Optional[ReportDatasetsToMeasurementResponseGuardBandLogic]):
        uncertainty_budget (Optional[str]):
        calculated_uncertainty (Optional[float]):
        lock_uncertainty_budget (Optional[bool]):
        lab_mu (Optional[float]):
        channel (Optional[int]):
        measurement_type (Optional[ReportDatasetsToMeasurementResponseMeasurementType]):
        updated_by (Optional[str]):
        updated_on (Optional[datetime.datetime]):
        error (Optional[float]):
        error_extended (Optional[str]):
        require_adjustment (Optional[bool]):
        adjustment_threshold (Optional[float]):
        percent_of_tolerance (Optional[float]):
        percent_of_tolerance_extended (Optional[str]):
        tol_decimal_places (Optional[int]):
        specification_title (Optional[str]):
        specification_subtitle (Optional[str]):
        specification_group (Optional[str]):
        batch_type (Optional[int]):
        batch_result (Optional[int]):
        is_by_channel (Optional[bool]):
        channel_count (Optional[int]):
        is_range_accredited (Optional[bool]):
        commenced_on (Optional[datetime.datetime]):
        commenced_by (Optional[str]):
        z_factor (Optional[float]):
        air_buoyancy (Optional[float]):
        evaporation_rate (Optional[float]):
        air_humidity (Optional[float]):
        altitude (Optional[float]):
        ambient_temperature (Optional[float]):
        barometric_pressure (Optional[float]):
        light_intensity (Optional[float]):
        noise_level (Optional[float]):
        ph_level (Optional[float]):
        water_conductivity (Optional[float]):
        water_temperature (Optional[float]):
        solar_radiation (Optional[float]):
        wind_speed (Optional[float]):
        z_factor_uom (Optional[str]):
        air_buoyancy_uom (Optional[str]):
        evaporation_rate_uom (Optional[str]):
        air_humidity_uom (Optional[str]):
        altitude_uom (Optional[str]):
        ambient_temperature_uom (Optional[str]):
        barometric_pressure_uom (Optional[str]):
        light_intensity_uom (Optional[str]):
        noise_level_uom (Optional[str]):
        ph_level_uom (Optional[str]):
        water_conductivity_uom (Optional[str]):
        water_temperature_uom (Optional[str]):
        solar_radiation_uom (Optional[str]):
        wind_speed_uom (Optional[str]):
        specification_name (Optional[str]):
        parameter_name (Optional[str]):
        measurement_set_display_order (Optional[int]):
        display_order (Optional[int]):
        unit_of_measure (Optional[str]):
        display_format (Optional[str]):
        precision (Optional[float]):
        minimum (Optional[float]):
        nominal (Optional[float]):
        expected_value (Optional[float]):
        expected_value_raw (Optional[str]):
        test_value (Optional[float]):
        base_value (Optional[float]):
        use_expected_value (Optional[bool]):
        reading_entry_logic (Optional[ReportDatasetsToMeasurementResponseReadingEntryLogic]):
        reading_entry_math (Optional[ReportDatasetsToMeasurementResponseReadingEntryMath]):
        double_substitution_sequence (Optional[ReportDatasetsToMeasurementResponseDoubleSubstitutionSequence]):
        reading_entry_math_string (Optional[str]):
        nominal_extended (Optional[str]):
        expected_value_extended (Optional[str]):
        maximum (Optional[float]):
        tolerance_min (Optional[float]):
        tolerance_max (Optional[float]):
        resolution (Optional[float]):
        resolution_count (Optional[float]):
        min_max_header (Optional[str]):
        accuracy_class (Optional[str]):
        accuracy_class_min (Optional[float]):
        accuracy_class_max (Optional[float]):
        environment_mask (Optional[ReportDatasetsToMeasurementResponseEnvironmentMask]):
        display_name (Optional[str]):
        display_part_number (Optional[str]):
        part_number (Optional[str]):
        vendor_company_id (Optional[int]):
        service_order_number (Optional[int]):
        custom_order_number (Optional[str]):
        completed_by_name (Optional[str]):
        completed_on (Optional[datetime.datetime]):
        is_limited (Optional[bool]):
        vendor_tag (Optional[str]):
        vendor_service_notes (Optional[str]):
        room (Optional[str]):
        segment_name (Optional[str]):
        schedule_name (Optional[str]):
        next_segment_name (Optional[str]):
        certificate_number (Optional[str]):
        work_status (Optional[WorkStatus]):
        service_type (Optional[str]):
        service_level (Optional[str]):
        barcode (Optional[str]):
        service_comments (Optional[str]):
        order_item_number (Optional[int]):
        asset_tag (Optional[str]):
        asset_user (Optional[str]):
        serial_number (Optional[str]):
        equipment_id (Optional[str]):
        legacy_identifier (Optional[str]):
        site_name (Optional[str]):
        asset_name (Optional[str]):
        asset_description (Optional[str]):
        product_name (Optional[str]):
        product_description (Optional[str]):
        asset_maker (Optional[str]):
        station (Optional[str]):
        asset_tag_change (Optional[str]):
        asset_user_change (Optional[str]):
        serial_number_change (Optional[str]):
        service_date (Optional[datetime.datetime]):
        next_service_date (Optional[datetime.datetime]):
        service_order_item_id (Optional[int]):
        service_order_id (Optional[int]):
        measurement_batch_id (Optional[int]):
        measurement_id (Optional[int]):
        standard_id (Optional[int]):
        tool_id (Optional[int]):
        measurement_tool_id (Optional[int]):
        measurement_condition_id (Optional[int]):
        measurement_point_id (Optional[int]):
        measurement_set_id (Optional[int]):
        is_hidden (Optional[bool]):
        readings (Optional[int]):
        tolerance_type (Optional[ReportDatasetsToMeasurementResponseToleranceType]):
        tolerance_type_string (Optional[str]):
        precision_type (Optional[ReportDatasetsToMeasurementResponsePrecisionType]):
        specification_mode (Optional[ReportDatasetsToMeasurementResponseSpecificationMode]):
        tolerance_mode (Optional[ReportDatasetsToMeasurementResponseToleranceMode]):
        tolerance_unit (Optional[ReportDatasetsToMeasurementResponseToleranceUnit]):
        tolerance_string (Optional[str]):
        po_number (Optional[str]):
        secondary_po (Optional[str]):
        shipped_date (Optional[datetime.datetime]):
        shipment_status (Optional[ReportDatasetsToMeasurementResponseShipmentStatus]):
        shipped_on (Optional[datetime.datetime]):
        delivered_on (Optional[datetime.datetime]):
        tracking_number (Optional[str]):
        payment_terms (Optional[int]):
        shipping_method (Optional[str]):
        location (Optional[str]):
        site_access_notes (Optional[str]):
        abbreviated_uom (Optional[str]):
        unit_scale_factor (Optional[float]):
        measurement_not_taken_result (Optional[ReportDatasetsToMeasurementResponseMeasurementNotTakenResult]):
        hide_from_certificate (Optional[bool]):
        measurement_not_taken_reason (Optional[str]):
        environment_text_1 (Optional[str]):
        environment_text_2 (Optional[str]):
        environment_text_3 (Optional[str]):
        environment_text_4 (Optional[str]):
        environment_text_5 (Optional[str]):
        environment_text_6 (Optional[str]):
        values (Optional[str]):
        value_1 (Optional[str]):
        value_2 (Optional[str]):
        value_3 (Optional[str]):
        value_4 (Optional[str]):
        value_5 (Optional[str]):
        value_6 (Optional[str]):
        value_7 (Optional[str]):
        value_8 (Optional[str]):
        value_9 (Optional[str]):
        value_10 (Optional[str]):
        value_11 (Optional[str]):
        value_12 (Optional[str]):
        value_13 (Optional[str]):
        value_14 (Optional[str]):
        value_15 (Optional[str]):
        value_16 (Optional[str]):
        value_17 (Optional[str]):
        value_18 (Optional[str]):
        value_19 (Optional[str]):
        value_20 (Optional[str]):
        value_21 (Optional[str]):
        value_22 (Optional[str]):
        value_23 (Optional[str]):
        value_24 (Optional[str]):
        value_25 (Optional[str]):
        value_26 (Optional[str]):
        value_27 (Optional[str]):
        value_28 (Optional[str]):
        value_29 (Optional[str]):
        value_30 (Optional[str]):
        value_31 (Optional[str]):
        value_32 (Optional[str]):
        value_33 (Optional[str]):
        value_34 (Optional[str]):
        value_35 (Optional[str]):
        value_36 (Optional[str]):
        value_37 (Optional[str]):
        value_38 (Optional[str]):
        value_39 (Optional[str]):
        value_40 (Optional[str]):
        raw_value_1 (Optional[str]):
        raw_value_2 (Optional[str]):
        raw_value_3 (Optional[str]):
        raw_value_4 (Optional[str]):
        raw_value_5 (Optional[str]):
        raw_value_6 (Optional[str]):
        raw_value_7 (Optional[str]):
        raw_value_8 (Optional[str]):
        raw_value_9 (Optional[str]):
        raw_value_10 (Optional[str]):
        raw_value_11 (Optional[str]):
        raw_value_12 (Optional[str]):
        raw_value_13 (Optional[str]):
        raw_value_14 (Optional[str]):
        raw_value_15 (Optional[str]):
        raw_value_16 (Optional[str]):
        raw_value_17 (Optional[str]):
        raw_value_18 (Optional[str]):
        raw_value_19 (Optional[str]):
        raw_value_20 (Optional[str]):
        raw_value_21 (Optional[str]):
        raw_value_22 (Optional[str]):
        raw_value_23 (Optional[str]):
        raw_value_24 (Optional[str]):
        raw_value_25 (Optional[str]):
        raw_value_26 (Optional[str]):
        raw_value_27 (Optional[str]):
        raw_value_28 (Optional[str]):
        raw_value_29 (Optional[str]):
        raw_value_30 (Optional[str]):
        raw_value_31 (Optional[str]):
        raw_value_32 (Optional[str]):
        raw_value_33 (Optional[str]):
        raw_value_34 (Optional[str]):
        raw_value_35 (Optional[str]):
        raw_value_36 (Optional[str]):
        raw_value_37 (Optional[str]):
        raw_value_38 (Optional[str]):
        raw_value_39 (Optional[str]):
        raw_value_40 (Optional[str]):
        subtitles_to_readings (Optional[str]):
        value_subtitle_1 (Optional[str]):
        value_subtitle_2 (Optional[str]):
        value_subtitle_3 (Optional[str]):
        value_subtitle_4 (Optional[str]):
        value_subtitle_5 (Optional[str]):
        value_subtitle_6 (Optional[str]):
        value_subtitle_7 (Optional[str]):
        value_subtitle_8 (Optional[str]):
        value_subtitle_9 (Optional[str]):
        value_subtitle_10 (Optional[str]):
        value_subtitle_11 (Optional[str]):
        value_subtitle_12 (Optional[str]):
        value_subtitle_13 (Optional[str]):
        value_subtitle_14 (Optional[str]):
        value_subtitle_15 (Optional[str]):
        value_subtitle_16 (Optional[str]):
        value_subtitle_17 (Optional[str]):
        value_subtitle_18 (Optional[str]):
        value_subtitle_19 (Optional[str]):
        value_subtitle_20 (Optional[str]):
        value_subtitle_21 (Optional[str]):
        value_subtitle_22 (Optional[str]):
        value_subtitle_23 (Optional[str]):
        value_subtitle_24 (Optional[str]):
        value_subtitle_25 (Optional[str]):
        value_subtitle_26 (Optional[str]):
        value_subtitle_27 (Optional[str]):
        value_subtitle_28 (Optional[str]):
        value_subtitle_29 (Optional[str]):
        value_subtitle_30 (Optional[str]):
        value_subtitle_31 (Optional[str]):
        value_subtitle_32 (Optional[str]):
        value_subtitle_33 (Optional[str]):
        value_subtitle_34 (Optional[str]):
        value_subtitle_35 (Optional[str]):
        value_subtitle_36 (Optional[str]):
        value_subtitle_37 (Optional[str]):
        value_subtitle_38 (Optional[str]):
        value_subtitle_39 (Optional[str]):
        value_subtitle_40 (Optional[str]):
        values_decimal_places (Optional[int]):
        repeat_measurement_and_calculate_hysteresis (Optional[bool]):
        measurement_point_order (Optional[ReportDatasetsToMeasurementResponseMeasurementPointOrder]):
        hysteresis_point (Optional[ReportDatasetsToMeasurementResponseHysteresisPoint]):
        max_hysteresis (Optional[float]):
        run (Optional[int]):
        direction (Optional[int]):
        hysteresis (Optional[float]):
        column_mean (Optional[str]):
        column_mean_result (Optional[str]):
        column_sd (Optional[str]):
        column_sd_result (Optional[str]):
        column_cv (Optional[str]):
        column_cv_result (Optional[str]):
        column_range (Optional[str]):
        column_range_result (Optional[str]):
        column_delta (Optional[str]):
        column_delta_result (Optional[str]):
        column_result (Optional[str]):
    """

    is_accredited: Optional[bool] = None
    service_total: Optional[float] = None
    repairs_total: Optional[float] = None
    parts_total: Optional[float] = None
    parameter_id: Optional[int] = None
    tool_range_name: Optional[str] = None
    tool_range_uncertainty: Optional[str] = None
    primary_tool_last_service_date: Optional[datetime.datetime] = None
    primary_tool_next_service_date: Optional[datetime.datetime] = None
    primary_tool_calibrated_by: Optional[str] = None
    primary_tool_tool_name: Optional[str] = None
    primary_tool_tool_description: Optional[str] = None
    primary_tool_tool_type_name: Optional[str] = None
    primary_tool_manufacturer: Optional[str] = None
    primary_tool_manufacturer_part_number: Optional[str] = None
    primary_tool_serial_number: Optional[str] = None
    secondary_tool_last_service_date: Optional[datetime.datetime] = None
    secondary_tool_next_service_date: Optional[datetime.datetime] = None
    secondary_tool_calibrated_by: Optional[str] = None
    secondary_tool_tool_name: Optional[str] = None
    secondary_tool_tool_description: Optional[str] = None
    secondary_tool_tool_type_name: Optional[str] = None
    secondary_tool_manufacturer: Optional[str] = None
    secondary_tool_manufacturer_part_number: Optional[str] = None
    secondary_tool_serial_number: Optional[str] = None
    measurement_set_name: Optional[str] = None
    decimal_places: Optional[int] = None
    significant_figures: Optional[int] = None
    sd_header: Optional[float] = None
    cv_header: Optional[float] = None
    measurement_local_time: Optional[datetime.datetime] = None
    mean: Optional[float] = None
    mean_raw: Optional[float] = None
    mean_decimal_places: Optional[int] = None
    mean_extended: Optional[str] = None
    sd: Optional[float] = None
    sd_raw: Optional[float] = None
    sd_decimal_places: Optional[int] = None
    delta: Optional[float] = None
    range_: Optional[float] = None
    sd_extended: Optional[str] = None
    range_extended: Optional[str] = None
    delta_extended: Optional[str] = None
    minimum_measured_value: Optional[float] = None
    maximum_measured_value: Optional[float] = None
    min_max_value_extended: Optional[str] = None
    cv: Optional[float] = None
    cv_raw: Optional[float] = None
    cv_decimal_places: Optional[int] = None
    cv_extended: Optional[str] = None
    result: Optional[ServiceResultStatus] = None
    range_result: Optional[bool] = None
    delta_result: Optional[bool] = None
    min_result: Optional[bool] = None
    max_result: Optional[bool] = None
    tar_result: Optional[bool] = None
    tur_result: Optional[bool] = None
    error_result: Optional[bool] = None
    sd_result: Optional[bool] = None
    cv_result: Optional[bool] = None
    custom_field_result: Optional[int] = None
    mu: Optional[float] = None
    mu_raw: Optional[float] = None
    mu_effective_dof: Optional[float] = None
    mu_coverage_factor: Optional[float] = None
    mu_extended: Optional[str] = None
    cmc: Optional[float] = None
    cmc_comments: Optional[str] = None
    tur: Optional[float] = None
    tur_raw: Optional[float] = None
    tur_decimal_places: Optional[int] = None
    tar: Optional[float] = None
    tar_raw: Optional[float] = None
    tar_decimal_places: Optional[int] = None
    guard_band: Optional[str] = None
    guard_band_logic: Optional[ReportDatasetsToMeasurementResponseGuardBandLogic] = None
    uncertainty_budget: Optional[str] = None
    calculated_uncertainty: Optional[float] = None
    lock_uncertainty_budget: Optional[bool] = None
    lab_mu: Optional[float] = None
    channel: Optional[int] = None
    measurement_type: Optional[ReportDatasetsToMeasurementResponseMeasurementType] = None
    updated_by: Optional[str] = None
    updated_on: Optional[datetime.datetime] = None
    error: Optional[float] = None
    error_extended: Optional[str] = None
    require_adjustment: Optional[bool] = None
    adjustment_threshold: Optional[float] = None
    percent_of_tolerance: Optional[float] = None
    percent_of_tolerance_extended: Optional[str] = None
    tol_decimal_places: Optional[int] = None
    specification_title: Optional[str] = None
    specification_subtitle: Optional[str] = None
    specification_group: Optional[str] = None
    batch_type: Optional[int] = None
    batch_result: Optional[int] = None
    is_by_channel: Optional[bool] = None
    channel_count: Optional[int] = None
    is_range_accredited: Optional[bool] = None
    commenced_on: Optional[datetime.datetime] = None
    commenced_by: Optional[str] = None
    z_factor: Optional[float] = None
    air_buoyancy: Optional[float] = None
    evaporation_rate: Optional[float] = None
    air_humidity: Optional[float] = None
    altitude: Optional[float] = None
    ambient_temperature: Optional[float] = None
    barometric_pressure: Optional[float] = None
    light_intensity: Optional[float] = None
    noise_level: Optional[float] = None
    ph_level: Optional[float] = None
    water_conductivity: Optional[float] = None
    water_temperature: Optional[float] = None
    solar_radiation: Optional[float] = None
    wind_speed: Optional[float] = None
    z_factor_uom: Optional[str] = None
    air_buoyancy_uom: Optional[str] = None
    evaporation_rate_uom: Optional[str] = None
    air_humidity_uom: Optional[str] = None
    altitude_uom: Optional[str] = None
    ambient_temperature_uom: Optional[str] = None
    barometric_pressure_uom: Optional[str] = None
    light_intensity_uom: Optional[str] = None
    noise_level_uom: Optional[str] = None
    ph_level_uom: Optional[str] = None
    water_conductivity_uom: Optional[str] = None
    water_temperature_uom: Optional[str] = None
    solar_radiation_uom: Optional[str] = None
    wind_speed_uom: Optional[str] = None
    specification_name: Optional[str] = None
    parameter_name: Optional[str] = None
    measurement_set_display_order: Optional[int] = None
    display_order: Optional[int] = None
    unit_of_measure: Optional[str] = None
    display_format: Optional[str] = None
    precision: Optional[float] = None
    minimum: Optional[float] = None
    nominal: Optional[float] = None
    expected_value: Optional[float] = None
    expected_value_raw: Optional[str] = None
    test_value: Optional[float] = None
    base_value: Optional[float] = None
    use_expected_value: Optional[bool] = None
    reading_entry_logic: Optional[ReportDatasetsToMeasurementResponseReadingEntryLogic] = None
    reading_entry_math: Optional[ReportDatasetsToMeasurementResponseReadingEntryMath] = None
    double_substitution_sequence: Optional[
        ReportDatasetsToMeasurementResponseDoubleSubstitutionSequence
    ] = None
    reading_entry_math_string: Optional[str] = None
    nominal_extended: Optional[str] = None
    expected_value_extended: Optional[str] = None
    maximum: Optional[float] = None
    tolerance_min: Optional[float] = None
    tolerance_max: Optional[float] = None
    resolution: Optional[float] = None
    resolution_count: Optional[float] = None
    min_max_header: Optional[str] = None
    accuracy_class: Optional[str] = None
    accuracy_class_min: Optional[float] = None
    accuracy_class_max: Optional[float] = None
    environment_mask: Optional[ReportDatasetsToMeasurementResponseEnvironmentMask] = None
    display_name: Optional[str] = None
    display_part_number: Optional[str] = None
    part_number: Optional[str] = None
    vendor_company_id: Optional[int] = None
    service_order_number: Optional[int] = None
    custom_order_number: Optional[str] = None
    completed_by_name: Optional[str] = None
    completed_on: Optional[datetime.datetime] = None
    is_limited: Optional[bool] = None
    vendor_tag: Optional[str] = None
    vendor_service_notes: Optional[str] = None
    room: Optional[str] = None
    segment_name: Optional[str] = None
    schedule_name: Optional[str] = None
    next_segment_name: Optional[str] = None
    certificate_number: Optional[str] = None
    work_status: Optional[WorkStatus] = None
    service_type: Optional[str] = None
    service_level: Optional[str] = None
    barcode: Optional[str] = None
    service_comments: Optional[str] = None
    order_item_number: Optional[int] = None
    asset_tag: Optional[str] = None
    asset_user: Optional[str] = None
    serial_number: Optional[str] = None
    equipment_id: Optional[str] = None
    legacy_identifier: Optional[str] = None
    site_name: Optional[str] = None
    asset_name: Optional[str] = None
    asset_description: Optional[str] = None
    product_name: Optional[str] = None
    product_description: Optional[str] = None
    asset_maker: Optional[str] = None
    station: Optional[str] = None
    asset_tag_change: Optional[str] = None
    asset_user_change: Optional[str] = None
    serial_number_change: Optional[str] = None
    service_date: Optional[datetime.datetime] = None
    next_service_date: Optional[datetime.datetime] = None
    service_order_item_id: Optional[int] = None
    service_order_id: Optional[int] = None
    measurement_batch_id: Optional[int] = None
    measurement_id: Optional[int] = None
    standard_id: Optional[int] = None
    tool_id: Optional[int] = None
    measurement_tool_id: Optional[int] = None
    measurement_condition_id: Optional[int] = None
    measurement_point_id: Optional[int] = None
    measurement_set_id: Optional[int] = None
    is_hidden: Optional[bool] = None
    readings: Optional[int] = None
    tolerance_type: Optional["ReportDatasetsToMeasurementResponseToleranceType"] = None
    tolerance_type_string: Optional[str] = None
    precision_type: Optional["ReportDatasetsToMeasurementResponsePrecisionType"] = None
    specification_mode: Optional[ReportDatasetsToMeasurementResponseSpecificationMode] = None
    tolerance_mode: Optional["ReportDatasetsToMeasurementResponseToleranceMode"] = None
    tolerance_unit: Optional["ReportDatasetsToMeasurementResponseToleranceUnit"] = None
    tolerance_string: Optional[str] = None
    po_number: Optional[str] = None
    secondary_po: Optional[str] = None
    shipped_date: Optional[datetime.datetime] = None
    shipment_status: Optional[ReportDatasetsToMeasurementResponseShipmentStatus] = None
    shipped_on: Optional[datetime.datetime] = None
    delivered_on: Optional[datetime.datetime] = None
    tracking_number: Optional[str] = None
    payment_terms: Optional[int] = None
    shipping_method: Optional[str] = None
    location: Optional[str] = None
    site_access_notes: Optional[str] = None
    abbreviated_uom: Optional[str] = None
    unit_scale_factor: Optional[float] = None
    measurement_not_taken_result: Optional[
        ReportDatasetsToMeasurementResponseMeasurementNotTakenResult
    ] = None
    hide_from_certificate: Optional[bool] = None
    measurement_not_taken_reason: Optional[str] = None
    environment_text_1: Optional[str] = None
    environment_text_2: Optional[str] = None
    environment_text_3: Optional[str] = None
    environment_text_4: Optional[str] = None
    environment_text_5: Optional[str] = None
    environment_text_6: Optional[str] = None
    values: Optional[str] = None
    value_1: Optional[str] = None
    value_2: Optional[str] = None
    value_3: Optional[str] = None
    value_4: Optional[str] = None
    value_5: Optional[str] = None
    value_6: Optional[str] = None
    value_7: Optional[str] = None
    value_8: Optional[str] = None
    value_9: Optional[str] = None
    value_10: Optional[str] = None
    value_11: Optional[str] = None
    value_12: Optional[str] = None
    value_13: Optional[str] = None
    value_14: Optional[str] = None
    value_15: Optional[str] = None
    value_16: Optional[str] = None
    value_17: Optional[str] = None
    value_18: Optional[str] = None
    value_19: Optional[str] = None
    value_20: Optional[str] = None
    value_21: Optional[str] = None
    value_22: Optional[str] = None
    value_23: Optional[str] = None
    value_24: Optional[str] = None
    value_25: Optional[str] = None
    value_26: Optional[str] = None
    value_27: Optional[str] = None
    value_28: Optional[str] = None
    value_29: Optional[str] = None
    value_30: Optional[str] = None
    value_31: Optional[str] = None
    value_32: Optional[str] = None
    value_33: Optional[str] = None
    value_34: Optional[str] = None
    value_35: Optional[str] = None
    value_36: Optional[str] = None
    value_37: Optional[str] = None
    value_38: Optional[str] = None
    value_39: Optional[str] = None
    value_40: Optional[str] = None
    raw_value_1: Optional[str] = None
    raw_value_2: Optional[str] = None
    raw_value_3: Optional[str] = None
    raw_value_4: Optional[str] = None
    raw_value_5: Optional[str] = None
    raw_value_6: Optional[str] = None
    raw_value_7: Optional[str] = None
    raw_value_8: Optional[str] = None
    raw_value_9: Optional[str] = None
    raw_value_10: Optional[str] = None
    raw_value_11: Optional[str] = None
    raw_value_12: Optional[str] = None
    raw_value_13: Optional[str] = None
    raw_value_14: Optional[str] = None
    raw_value_15: Optional[str] = None
    raw_value_16: Optional[str] = None
    raw_value_17: Optional[str] = None
    raw_value_18: Optional[str] = None
    raw_value_19: Optional[str] = None
    raw_value_20: Optional[str] = None
    raw_value_21: Optional[str] = None
    raw_value_22: Optional[str] = None
    raw_value_23: Optional[str] = None
    raw_value_24: Optional[str] = None
    raw_value_25: Optional[str] = None
    raw_value_26: Optional[str] = None
    raw_value_27: Optional[str] = None
    raw_value_28: Optional[str] = None
    raw_value_29: Optional[str] = None
    raw_value_30: Optional[str] = None
    raw_value_31: Optional[str] = None
    raw_value_32: Optional[str] = None
    raw_value_33: Optional[str] = None
    raw_value_34: Optional[str] = None
    raw_value_35: Optional[str] = None
    raw_value_36: Optional[str] = None
    raw_value_37: Optional[str] = None
    raw_value_38: Optional[str] = None
    raw_value_39: Optional[str] = None
    raw_value_40: Optional[str] = None
    subtitles_to_readings: Optional[str] = None
    value_subtitle_1: Optional[str] = None
    value_subtitle_2: Optional[str] = None
    value_subtitle_3: Optional[str] = None
    value_subtitle_4: Optional[str] = None
    value_subtitle_5: Optional[str] = None
    value_subtitle_6: Optional[str] = None
    value_subtitle_7: Optional[str] = None
    value_subtitle_8: Optional[str] = None
    value_subtitle_9: Optional[str] = None
    value_subtitle_10: Optional[str] = None
    value_subtitle_11: Optional[str] = None
    value_subtitle_12: Optional[str] = None
    value_subtitle_13: Optional[str] = None
    value_subtitle_14: Optional[str] = None
    value_subtitle_15: Optional[str] = None
    value_subtitle_16: Optional[str] = None
    value_subtitle_17: Optional[str] = None
    value_subtitle_18: Optional[str] = None
    value_subtitle_19: Optional[str] = None
    value_subtitle_20: Optional[str] = None
    value_subtitle_21: Optional[str] = None
    value_subtitle_22: Optional[str] = None
    value_subtitle_23: Optional[str] = None
    value_subtitle_24: Optional[str] = None
    value_subtitle_25: Optional[str] = None
    value_subtitle_26: Optional[str] = None
    value_subtitle_27: Optional[str] = None
    value_subtitle_28: Optional[str] = None
    value_subtitle_29: Optional[str] = None
    value_subtitle_30: Optional[str] = None
    value_subtitle_31: Optional[str] = None
    value_subtitle_32: Optional[str] = None
    value_subtitle_33: Optional[str] = None
    value_subtitle_34: Optional[str] = None
    value_subtitle_35: Optional[str] = None
    value_subtitle_36: Optional[str] = None
    value_subtitle_37: Optional[str] = None
    value_subtitle_38: Optional[str] = None
    value_subtitle_39: Optional[str] = None
    value_subtitle_40: Optional[str] = None
    values_decimal_places: Optional[int] = None
    repeat_measurement_and_calculate_hysteresis: Optional[bool] = None
    measurement_point_order: Optional[ReportDatasetsToMeasurementResponseMeasurementPointOrder] = (
        None
    )
    hysteresis_point: Optional[ReportDatasetsToMeasurementResponseHysteresisPoint] = None
    max_hysteresis: Optional[float] = None
    run: Optional[int] = None
    direction: Optional[int] = None
    hysteresis: Optional[float] = None
    column_mean: Optional[str] = None
    column_mean_result: Optional[str] = None
    column_sd: Optional[str] = None
    column_sd_result: Optional[str] = None
    column_cv: Optional[str] = None
    column_cv_result: Optional[str] = None
    column_range: Optional[str] = None
    column_range_result: Optional[str] = None
    column_delta: Optional[str] = None
    column_delta_result: Optional[str] = None
    column_result: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_accredited = self.is_accredited

        service_total = self.service_total

        repairs_total = self.repairs_total

        parts_total = self.parts_total

        parameter_id = self.parameter_id

        tool_range_name = self.tool_range_name

        tool_range_uncertainty = self.tool_range_uncertainty

        primary_tool_last_service_date: Optional[str]
        if not self.primary_tool_last_service_date:
            primary_tool_last_service_date = None
        elif isinstance(self.primary_tool_last_service_date, datetime.datetime):
            primary_tool_last_service_date = self.primary_tool_last_service_date.isoformat()
        else:
            primary_tool_last_service_date = self.primary_tool_last_service_date

        primary_tool_next_service_date: Optional[str]
        if not self.primary_tool_next_service_date:
            primary_tool_next_service_date = None
        elif isinstance(self.primary_tool_next_service_date, datetime.datetime):
            primary_tool_next_service_date = self.primary_tool_next_service_date.isoformat()
        else:
            primary_tool_next_service_date = self.primary_tool_next_service_date

        primary_tool_calibrated_by = self.primary_tool_calibrated_by

        primary_tool_tool_name = self.primary_tool_tool_name

        primary_tool_tool_description = self.primary_tool_tool_description

        primary_tool_tool_type_name = self.primary_tool_tool_type_name

        primary_tool_manufacturer = self.primary_tool_manufacturer

        primary_tool_manufacturer_part_number = self.primary_tool_manufacturer_part_number

        primary_tool_serial_number = self.primary_tool_serial_number

        secondary_tool_last_service_date: Optional[str]
        if not self.secondary_tool_last_service_date:
            secondary_tool_last_service_date = None
        elif isinstance(self.secondary_tool_last_service_date, datetime.datetime):
            secondary_tool_last_service_date = self.secondary_tool_last_service_date.isoformat()
        else:
            secondary_tool_last_service_date = self.secondary_tool_last_service_date

        secondary_tool_next_service_date: Optional[str]
        if not self.secondary_tool_next_service_date:
            secondary_tool_next_service_date = None
        elif isinstance(self.secondary_tool_next_service_date, datetime.datetime):
            secondary_tool_next_service_date = self.secondary_tool_next_service_date.isoformat()
        else:
            secondary_tool_next_service_date = self.secondary_tool_next_service_date

        secondary_tool_calibrated_by = self.secondary_tool_calibrated_by

        secondary_tool_tool_name = self.secondary_tool_tool_name

        secondary_tool_tool_description = self.secondary_tool_tool_description

        secondary_tool_tool_type_name = self.secondary_tool_tool_type_name

        secondary_tool_manufacturer = self.secondary_tool_manufacturer

        secondary_tool_manufacturer_part_number = self.secondary_tool_manufacturer_part_number

        secondary_tool_serial_number = self.secondary_tool_serial_number

        measurement_set_name = self.measurement_set_name

        decimal_places = self.decimal_places

        significant_figures = self.significant_figures

        sd_header = self.sd_header

        cv_header = self.cv_header

        measurement_local_time: Optional[str] = None
        if self.measurement_local_time:
            measurement_local_time = self.measurement_local_time.isoformat()

        mean = self.mean

        mean_raw = self.mean_raw

        mean_decimal_places = self.mean_decimal_places

        mean_extended = self.mean_extended

        sd = self.sd

        sd_raw = self.sd_raw

        sd_decimal_places = self.sd_decimal_places

        delta = self.delta

        range_ = self.range_

        sd_extended = self.sd_extended

        range_extended = self.range_extended

        delta_extended = self.delta_extended

        minimum_measured_value = self.minimum_measured_value

        maximum_measured_value = self.maximum_measured_value

        min_max_value_extended = self.min_max_value_extended

        cv = self.cv

        cv_raw = self.cv_raw

        cv_decimal_places = self.cv_decimal_places

        cv_extended = self.cv_extended

        result: Optional[int] = None
        if self.result:
            result = self.result.value

        range_result = self.range_result

        delta_result = self.delta_result

        min_result = self.min_result

        max_result = self.max_result

        tar_result = self.tar_result

        tur_result = self.tur_result

        error_result = self.error_result

        sd_result = self.sd_result

        cv_result = self.cv_result

        custom_field_result = self.custom_field_result

        mu = self.mu

        mu_raw = self.mu_raw

        mu_effective_dof = self.mu_effective_dof

        mu_coverage_factor = self.mu_coverage_factor

        mu_extended = self.mu_extended

        cmc = self.cmc

        cmc_comments = self.cmc_comments

        tur = self.tur

        tur_raw = self.tur_raw

        tur_decimal_places = self.tur_decimal_places

        tar = self.tar

        tar_raw = self.tar_raw

        tar_decimal_places = self.tar_decimal_places

        guard_band = self.guard_band

        guard_band_logic: Optional[str] = None
        if self.guard_band_logic:
            guard_band_logic = self.guard_band_logic.value

        uncertainty_budget = self.uncertainty_budget

        calculated_uncertainty = self.calculated_uncertainty

        lock_uncertainty_budget = self.lock_uncertainty_budget

        lab_mu = self.lab_mu

        channel = self.channel

        measurement_type: Optional[str] = None
        if self.measurement_type:
            measurement_type = self.measurement_type.value

        updated_by = self.updated_by

        updated_on: Optional[str] = None
        if self.updated_on:
            updated_on = self.updated_on.isoformat()

        error = self.error

        error_extended = self.error_extended

        require_adjustment = self.require_adjustment

        adjustment_threshold = self.adjustment_threshold

        percent_of_tolerance = self.percent_of_tolerance

        percent_of_tolerance_extended = self.percent_of_tolerance_extended

        tol_decimal_places = self.tol_decimal_places

        specification_title = self.specification_title

        specification_subtitle = self.specification_subtitle

        specification_group = self.specification_group

        batch_type = self.batch_type

        batch_result = self.batch_result

        is_by_channel = self.is_by_channel

        channel_count = self.channel_count

        is_range_accredited = self.is_range_accredited

        commenced_on: Optional[str] = None
        if self.commenced_on:
            commenced_on = self.commenced_on.isoformat()

        commenced_by = self.commenced_by

        z_factor = self.z_factor

        air_buoyancy = self.air_buoyancy

        evaporation_rate = self.evaporation_rate

        air_humidity = self.air_humidity

        altitude = self.altitude

        ambient_temperature = self.ambient_temperature

        barometric_pressure = self.barometric_pressure

        light_intensity = self.light_intensity

        noise_level = self.noise_level

        ph_level = self.ph_level

        water_conductivity = self.water_conductivity

        water_temperature = self.water_temperature

        solar_radiation = self.solar_radiation

        wind_speed = self.wind_speed

        z_factor_uom = self.z_factor_uom

        air_buoyancy_uom = self.air_buoyancy_uom

        evaporation_rate_uom = self.evaporation_rate_uom

        air_humidity_uom = self.air_humidity_uom

        altitude_uom = self.altitude_uom

        ambient_temperature_uom = self.ambient_temperature_uom

        barometric_pressure_uom = self.barometric_pressure_uom

        light_intensity_uom = self.light_intensity_uom

        noise_level_uom = self.noise_level_uom

        ph_level_uom = self.ph_level_uom

        water_conductivity_uom = self.water_conductivity_uom

        water_temperature_uom = self.water_temperature_uom

        solar_radiation_uom = self.solar_radiation_uom

        wind_speed_uom = self.wind_speed_uom

        specification_name = self.specification_name

        parameter_name = self.parameter_name

        measurement_set_display_order = self.measurement_set_display_order

        display_order = self.display_order

        unit_of_measure = self.unit_of_measure

        display_format = self.display_format

        precision = self.precision

        minimum = self.minimum

        nominal = self.nominal

        expected_value = self.expected_value

        expected_value_raw = self.expected_value_raw

        test_value = self.test_value

        base_value = self.base_value

        use_expected_value = self.use_expected_value

        reading_entry_logic: Optional[str] = None
        if self.reading_entry_logic:
            reading_entry_logic = self.reading_entry_logic.value

        reading_entry_math: Optional[str] = None
        if self.reading_entry_math:
            reading_entry_math = self.reading_entry_math.value

        double_substitution_sequence: Optional[str] = None
        if self.double_substitution_sequence:
            double_substitution_sequence = self.double_substitution_sequence.value

        reading_entry_math_string = self.reading_entry_math_string

        nominal_extended = self.nominal_extended

        expected_value_extended = self.expected_value_extended

        maximum = self.maximum

        tolerance_min = self.tolerance_min

        tolerance_max = self.tolerance_max

        resolution = self.resolution

        resolution_count = self.resolution_count

        min_max_header = self.min_max_header

        accuracy_class = self.accuracy_class

        accuracy_class_min = self.accuracy_class_min

        accuracy_class_max = self.accuracy_class_max

        environment_mask: Optional[str] = None
        if self.environment_mask:
            environment_mask = self.environment_mask.value

        display_name = self.display_name

        display_part_number = self.display_part_number

        part_number = self.part_number

        vendor_company_id = self.vendor_company_id

        service_order_number = self.service_order_number

        custom_order_number = self.custom_order_number

        completed_by_name = self.completed_by_name

        completed_on: Optional[str] = None
        if self.completed_on:
            completed_on = self.completed_on.isoformat()

        is_limited = self.is_limited

        vendor_tag = self.vendor_tag

        vendor_service_notes = self.vendor_service_notes

        room = self.room

        segment_name = self.segment_name

        schedule_name = self.schedule_name

        next_segment_name = self.next_segment_name

        certificate_number = self.certificate_number

        work_status: Optional[int] = None
        if self.work_status:
            work_status = self.work_status.value

        service_type = self.service_type

        service_level = self.service_level

        barcode = self.barcode

        service_comments = self.service_comments

        order_item_number = self.order_item_number

        asset_tag = self.asset_tag

        asset_user = self.asset_user

        serial_number = self.serial_number

        equipment_id = self.equipment_id

        legacy_identifier = self.legacy_identifier

        site_name = self.site_name

        asset_name = self.asset_name

        asset_description = self.asset_description

        product_name = self.product_name

        product_description = self.product_description

        asset_maker = self.asset_maker

        station = self.station

        asset_tag_change = self.asset_tag_change

        asset_user_change = self.asset_user_change

        serial_number_change = self.serial_number_change

        service_date: Optional[str]
        if not self.service_date:
            service_date = None
        elif isinstance(self.service_date, datetime.datetime):
            service_date = self.service_date.isoformat()
        else:
            service_date = self.service_date

        next_service_date: Optional[str]
        if not self.next_service_date:
            next_service_date = None
        elif isinstance(self.next_service_date, datetime.datetime):
            next_service_date = self.next_service_date.isoformat()
        else:
            next_service_date = self.next_service_date

        service_order_item_id = self.service_order_item_id

        service_order_id = self.service_order_id

        measurement_batch_id = self.measurement_batch_id

        measurement_id = self.measurement_id

        standard_id = self.standard_id

        tool_id = self.tool_id

        measurement_tool_id = self.measurement_tool_id

        measurement_condition_id = self.measurement_condition_id

        measurement_point_id = self.measurement_point_id

        measurement_set_id = self.measurement_set_id

        is_hidden = self.is_hidden

        readings = self.readings

        tolerance_type: Optional[str] = None
        if self.tolerance_type:
            tolerance_type = self.tolerance_type.value

        tolerance_type_string = self.tolerance_type_string

        precision_type: Optional[str] = None
        if self.precision_type:
            precision_type = self.precision_type.value

        specification_mode: Optional[int] = None
        if self.specification_mode:
            specification_mode = self.specification_mode.value

        tolerance_mode: Optional[int] = None
        if self.tolerance_mode:
            tolerance_mode = self.tolerance_mode.value

        tolerance_unit: Optional[int] = None
        if self.tolerance_unit:
            tolerance_unit = self.tolerance_unit.value

        tolerance_string = self.tolerance_string

        po_number = self.po_number

        secondary_po = self.secondary_po

        shipped_date: Optional[str]
        if not self.shipped_date:
            shipped_date = None
        elif isinstance(self.shipped_date, datetime.datetime):
            shipped_date = self.shipped_date.isoformat()
        else:
            shipped_date = self.shipped_date

        shipment_status: Optional[str] = None
        if self.shipment_status:
            shipment_status = self.shipment_status.value

        shipped_on: Optional[str] = None
        if self.shipped_on:
            shipped_on = self.shipped_on.isoformat()

        delivered_on: Optional[str] = None
        if self.delivered_on:
            delivered_on = self.delivered_on.isoformat()

        tracking_number = self.tracking_number

        payment_terms = self.payment_terms

        shipping_method = self.shipping_method

        location = self.location

        site_access_notes = self.site_access_notes

        abbreviated_uom = self.abbreviated_uom

        unit_scale_factor = self.unit_scale_factor

        measurement_not_taken_result: Optional[str] = None
        if self.measurement_not_taken_result:
            measurement_not_taken_result = self.measurement_not_taken_result.value

        hide_from_certificate = self.hide_from_certificate

        measurement_not_taken_reason = self.measurement_not_taken_reason

        environment_text_1 = self.environment_text_1

        environment_text_2 = self.environment_text_2

        environment_text_3 = self.environment_text_3

        environment_text_4 = self.environment_text_4

        environment_text_5 = self.environment_text_5

        environment_text_6 = self.environment_text_6

        values = self.values

        value_1 = self.value_1

        value_2 = self.value_2

        value_3 = self.value_3

        value_4 = self.value_4

        value_5 = self.value_5

        value_6 = self.value_6

        value_7 = self.value_7

        value_8 = self.value_8

        value_9 = self.value_9

        value_10 = self.value_10

        value_11 = self.value_11

        value_12 = self.value_12

        value_13 = self.value_13

        value_14 = self.value_14

        value_15 = self.value_15

        value_16 = self.value_16

        value_17 = self.value_17

        value_18 = self.value_18

        value_19 = self.value_19

        value_20 = self.value_20

        value_21 = self.value_21

        value_22 = self.value_22

        value_23 = self.value_23

        value_24 = self.value_24

        value_25 = self.value_25

        value_26 = self.value_26

        value_27 = self.value_27

        value_28 = self.value_28

        value_29 = self.value_29

        value_30 = self.value_30

        value_31 = self.value_31

        value_32 = self.value_32

        value_33 = self.value_33

        value_34 = self.value_34

        value_35 = self.value_35

        value_36 = self.value_36

        value_37 = self.value_37

        value_38 = self.value_38

        value_39 = self.value_39

        value_40 = self.value_40

        raw_value_1 = self.raw_value_1

        raw_value_2 = self.raw_value_2

        raw_value_3 = self.raw_value_3

        raw_value_4 = self.raw_value_4

        raw_value_5 = self.raw_value_5

        raw_value_6 = self.raw_value_6

        raw_value_7 = self.raw_value_7

        raw_value_8 = self.raw_value_8

        raw_value_9 = self.raw_value_9

        raw_value_10 = self.raw_value_10

        raw_value_11 = self.raw_value_11

        raw_value_12 = self.raw_value_12

        raw_value_13 = self.raw_value_13

        raw_value_14 = self.raw_value_14

        raw_value_15 = self.raw_value_15

        raw_value_16 = self.raw_value_16

        raw_value_17 = self.raw_value_17

        raw_value_18 = self.raw_value_18

        raw_value_19 = self.raw_value_19

        raw_value_20 = self.raw_value_20

        raw_value_21 = self.raw_value_21

        raw_value_22 = self.raw_value_22

        raw_value_23 = self.raw_value_23

        raw_value_24 = self.raw_value_24

        raw_value_25 = self.raw_value_25

        raw_value_26 = self.raw_value_26

        raw_value_27 = self.raw_value_27

        raw_value_28 = self.raw_value_28

        raw_value_29 = self.raw_value_29

        raw_value_30 = self.raw_value_30

        raw_value_31 = self.raw_value_31

        raw_value_32 = self.raw_value_32

        raw_value_33 = self.raw_value_33

        raw_value_34 = self.raw_value_34

        raw_value_35 = self.raw_value_35

        raw_value_36 = self.raw_value_36

        raw_value_37 = self.raw_value_37

        raw_value_38 = self.raw_value_38

        raw_value_39 = self.raw_value_39

        raw_value_40 = self.raw_value_40

        subtitles_to_readings = self.subtitles_to_readings

        value_subtitle_1 = self.value_subtitle_1

        value_subtitle_2 = self.value_subtitle_2

        value_subtitle_3 = self.value_subtitle_3

        value_subtitle_4 = self.value_subtitle_4

        value_subtitle_5 = self.value_subtitle_5

        value_subtitle_6 = self.value_subtitle_6

        value_subtitle_7 = self.value_subtitle_7

        value_subtitle_8 = self.value_subtitle_8

        value_subtitle_9 = self.value_subtitle_9

        value_subtitle_10 = self.value_subtitle_10

        value_subtitle_11 = self.value_subtitle_11

        value_subtitle_12 = self.value_subtitle_12

        value_subtitle_13 = self.value_subtitle_13

        value_subtitle_14 = self.value_subtitle_14

        value_subtitle_15 = self.value_subtitle_15

        value_subtitle_16 = self.value_subtitle_16

        value_subtitle_17 = self.value_subtitle_17

        value_subtitle_18 = self.value_subtitle_18

        value_subtitle_19 = self.value_subtitle_19

        value_subtitle_20 = self.value_subtitle_20

        value_subtitle_21 = self.value_subtitle_21

        value_subtitle_22 = self.value_subtitle_22

        value_subtitle_23 = self.value_subtitle_23

        value_subtitle_24 = self.value_subtitle_24

        value_subtitle_25 = self.value_subtitle_25

        value_subtitle_26 = self.value_subtitle_26

        value_subtitle_27 = self.value_subtitle_27

        value_subtitle_28 = self.value_subtitle_28

        value_subtitle_29 = self.value_subtitle_29

        value_subtitle_30 = self.value_subtitle_30

        value_subtitle_31 = self.value_subtitle_31

        value_subtitle_32 = self.value_subtitle_32

        value_subtitle_33 = self.value_subtitle_33

        value_subtitle_34 = self.value_subtitle_34

        value_subtitle_35 = self.value_subtitle_35

        value_subtitle_36 = self.value_subtitle_36

        value_subtitle_37 = self.value_subtitle_37

        value_subtitle_38 = self.value_subtitle_38

        value_subtitle_39 = self.value_subtitle_39

        value_subtitle_40 = self.value_subtitle_40

        values_decimal_places = self.values_decimal_places

        repeat_measurement_and_calculate_hysteresis = (
            self.repeat_measurement_and_calculate_hysteresis
        )

        measurement_point_order: Optional[str] = None
        if self.measurement_point_order:
            measurement_point_order = self.measurement_point_order.value

        hysteresis_point: Optional[str] = None
        if self.hysteresis_point:
            hysteresis_point = self.hysteresis_point.value

        max_hysteresis = self.max_hysteresis

        run = self.run

        direction = self.direction

        hysteresis = self.hysteresis

        column_mean = self.column_mean

        column_mean_result = self.column_mean_result

        column_sd = self.column_sd

        column_sd_result = self.column_sd_result

        column_cv = self.column_cv

        column_cv_result = self.column_cv_result

        column_range = self.column_range

        column_range_result = self.column_range_result

        column_delta = self.column_delta

        column_delta_result = self.column_delta_result

        column_result = self.column_result

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_accredited is not None:
            field_dict["IsAccredited"] = is_accredited
        if service_total is not None:
            field_dict["ServiceTotal"] = service_total
        if repairs_total is not None:
            field_dict["RepairsTotal"] = repairs_total
        if parts_total is not None:
            field_dict["PartsTotal"] = parts_total
        if parameter_id is not None:
            field_dict["ParameterId"] = parameter_id
        if tool_range_name is not None:
            field_dict["ToolRangeName"] = tool_range_name
        if tool_range_uncertainty is not None:
            field_dict["ToolRangeUncertainty"] = tool_range_uncertainty
        if primary_tool_last_service_date is not None:
            field_dict["PrimaryToolLastServiceDate"] = primary_tool_last_service_date
        if primary_tool_next_service_date is not None:
            field_dict["PrimaryToolNextServiceDate"] = primary_tool_next_service_date
        if primary_tool_calibrated_by is not None:
            field_dict["PrimaryToolCalibratedBy"] = primary_tool_calibrated_by
        if primary_tool_tool_name is not None:
            field_dict["PrimaryToolToolName"] = primary_tool_tool_name
        if primary_tool_tool_description is not None:
            field_dict["PrimaryToolToolDescription"] = primary_tool_tool_description
        if primary_tool_tool_type_name is not None:
            field_dict["PrimaryToolToolTypeName"] = primary_tool_tool_type_name
        if primary_tool_manufacturer is not None:
            field_dict["PrimaryToolManufacturer"] = primary_tool_manufacturer
        if primary_tool_manufacturer_part_number is not None:
            field_dict["PrimaryToolManufacturerPartNumber"] = primary_tool_manufacturer_part_number
        if primary_tool_serial_number is not None:
            field_dict["PrimaryToolSerialNumber"] = primary_tool_serial_number
        if secondary_tool_last_service_date is not None:
            field_dict["SecondaryToolLastServiceDate"] = secondary_tool_last_service_date
        if secondary_tool_next_service_date is not None:
            field_dict["SecondaryToolNextServiceDate"] = secondary_tool_next_service_date
        if secondary_tool_calibrated_by is not None:
            field_dict["SecondaryToolCalibratedBy"] = secondary_tool_calibrated_by
        if secondary_tool_tool_name is not None:
            field_dict["SecondaryToolToolName"] = secondary_tool_tool_name
        if secondary_tool_tool_description is not None:
            field_dict["SecondaryToolToolDescription"] = secondary_tool_tool_description
        if secondary_tool_tool_type_name is not None:
            field_dict["SecondaryToolToolTypeName"] = secondary_tool_tool_type_name
        if secondary_tool_manufacturer is not None:
            field_dict["SecondaryToolManufacturer"] = secondary_tool_manufacturer
        if secondary_tool_manufacturer_part_number is not None:
            field_dict["SecondaryToolManufacturerPartNumber"] = (
                secondary_tool_manufacturer_part_number
            )
        if secondary_tool_serial_number is not None:
            field_dict["SecondaryToolSerialNumber"] = secondary_tool_serial_number
        if measurement_set_name is not None:
            field_dict["MeasurementSetName"] = measurement_set_name
        if decimal_places is not None:
            field_dict["DecimalPlaces"] = decimal_places
        if significant_figures is not None:
            field_dict["SignificantFigures"] = significant_figures
        if sd_header is not None:
            field_dict["SdHeader"] = sd_header
        if cv_header is not None:
            field_dict["CvHeader"] = cv_header
        if measurement_local_time is not None:
            field_dict["MeasurementLocalTime"] = measurement_local_time
        if mean is not None:
            field_dict["Mean"] = mean
        if mean_raw is not None:
            field_dict["MeanRaw"] = mean_raw
        if mean_decimal_places is not None:
            field_dict["MeanDecimalPlaces"] = mean_decimal_places
        if mean_extended is not None:
            field_dict["MeanExtended"] = mean_extended
        if sd is not None:
            field_dict["Sd"] = sd
        if sd_raw is not None:
            field_dict["SdRaw"] = sd_raw
        if sd_decimal_places is not None:
            field_dict["SDDecimalPlaces"] = sd_decimal_places
        if delta is not None:
            field_dict["Delta"] = delta
        if range_ is not None:
            field_dict["Range"] = range_
        if sd_extended is not None:
            field_dict["SdExtended"] = sd_extended
        if range_extended is not None:
            field_dict["RangeExtended"] = range_extended
        if delta_extended is not None:
            field_dict["DeltaExtended"] = delta_extended
        if minimum_measured_value is not None:
            field_dict["MinimumMeasuredValue"] = minimum_measured_value
        if maximum_measured_value is not None:
            field_dict["MaximumMeasuredValue"] = maximum_measured_value
        if min_max_value_extended is not None:
            field_dict["MinMaxValueExtended"] = min_max_value_extended
        if cv is not None:
            field_dict["Cv"] = cv
        if cv_raw is not None:
            field_dict["CvRaw"] = cv_raw
        if cv_decimal_places is not None:
            field_dict["CVDecimalPlaces"] = cv_decimal_places
        if cv_extended is not None:
            field_dict["CvExtended"] = cv_extended
        if result is not None:
            field_dict["Result"] = result
        if range_result is not None:
            field_dict["RangeResult"] = range_result
        if delta_result is not None:
            field_dict["DeltaResult"] = delta_result
        if min_result is not None:
            field_dict["MinResult"] = min_result
        if max_result is not None:
            field_dict["MaxResult"] = max_result
        if tar_result is not None:
            field_dict["TarResult"] = tar_result
        if tur_result is not None:
            field_dict["TurResult"] = tur_result
        if error_result is not None:
            field_dict["ErrorResult"] = error_result
        if sd_result is not None:
            field_dict["SdResult"] = sd_result
        if cv_result is not None:
            field_dict["CvResult"] = cv_result
        if custom_field_result is not None:
            field_dict["CustomFieldResult"] = custom_field_result
        if mu is not None:
            field_dict["Mu"] = mu
        if mu_raw is not None:
            field_dict["MuRaw"] = mu_raw
        if mu_effective_dof is not None:
            field_dict["MUEffectiveDOF"] = mu_effective_dof
        if mu_coverage_factor is not None:
            field_dict["MUCoverageFactor"] = mu_coverage_factor
        if mu_extended is not None:
            field_dict["MuExtended"] = mu_extended
        if cmc is not None:
            field_dict["Cmc"] = cmc
        if cmc_comments is not None:
            field_dict["CmcComments"] = cmc_comments
        if tur is not None:
            field_dict["Tur"] = tur
        if tur_raw is not None:
            field_dict["TurRaw"] = tur_raw
        if tur_decimal_places is not None:
            field_dict["TURDecimalPlaces"] = tur_decimal_places
        if tar is not None:
            field_dict["Tar"] = tar
        if tar_raw is not None:
            field_dict["TarRaw"] = tar_raw
        if tar_decimal_places is not None:
            field_dict["TARDecimalPlaces"] = tar_decimal_places
        if guard_band is not None:
            field_dict["GuardBand"] = guard_band
        if guard_band_logic is not None:
            field_dict["GuardBandLogic"] = guard_band_logic
        if uncertainty_budget is not None:
            field_dict["UncertaintyBudget"] = uncertainty_budget
        if calculated_uncertainty is not None:
            field_dict["CalculatedUncertainty"] = calculated_uncertainty
        if lock_uncertainty_budget is not None:
            field_dict["LockUncertaintyBudget"] = lock_uncertainty_budget
        if lab_mu is not None:
            field_dict["LabMu"] = lab_mu
        if channel is not None:
            field_dict["Channel"] = channel
        if measurement_type is not None:
            field_dict["MeasurementType"] = measurement_type
        if updated_by is not None:
            field_dict["UpdatedBy"] = updated_by
        if updated_on is not None:
            field_dict["UpdatedOn"] = updated_on
        if error is not None:
            field_dict["Error"] = error
        if error_extended is not None:
            field_dict["ErrorExtended"] = error_extended
        if require_adjustment is not None:
            field_dict["RequireAdjustment"] = require_adjustment
        if adjustment_threshold is not None:
            field_dict["AdjustmentThreshold"] = adjustment_threshold
        if percent_of_tolerance is not None:
            field_dict["PercentOfTolerance"] = percent_of_tolerance
        if percent_of_tolerance_extended is not None:
            field_dict["PercentOfToleranceExtended"] = percent_of_tolerance_extended
        if tol_decimal_places is not None:
            field_dict["TOLDecimalPlaces"] = tol_decimal_places
        if specification_title is not None:
            field_dict["SpecificationTitle"] = specification_title
        if specification_subtitle is not None:
            field_dict["SpecificationSubtitle"] = specification_subtitle
        if specification_group is not None:
            field_dict["SpecificationGroup"] = specification_group
        if batch_type is not None:
            field_dict["BatchType"] = batch_type
        if batch_result is not None:
            field_dict["BatchResult"] = batch_result
        if is_by_channel is not None:
            field_dict["IsByChannel"] = is_by_channel
        if channel_count is not None:
            field_dict["ChannelCount"] = channel_count
        if is_range_accredited is not None:
            field_dict["IsRangeAccredited"] = is_range_accredited
        if commenced_on is not None:
            field_dict["CommencedOn"] = commenced_on
        if commenced_by is not None:
            field_dict["CommencedBy"] = commenced_by
        if z_factor is not None:
            field_dict["ZFactor"] = z_factor
        if air_buoyancy is not None:
            field_dict["AirBuoyancy"] = air_buoyancy
        if evaporation_rate is not None:
            field_dict["EvaporationRate"] = evaporation_rate
        if air_humidity is not None:
            field_dict["AirHumidity"] = air_humidity
        if altitude is not None:
            field_dict["Altitude"] = altitude
        if ambient_temperature is not None:
            field_dict["AmbientTemperature"] = ambient_temperature
        if barometric_pressure is not None:
            field_dict["BarometricPressure"] = barometric_pressure
        if light_intensity is not None:
            field_dict["LightIntensity"] = light_intensity
        if noise_level is not None:
            field_dict["NoiseLevel"] = noise_level
        if ph_level is not None:
            field_dict["PhLevel"] = ph_level
        if water_conductivity is not None:
            field_dict["WaterConductivity"] = water_conductivity
        if water_temperature is not None:
            field_dict["WaterTemperature"] = water_temperature
        if solar_radiation is not None:
            field_dict["SolarRadiation"] = solar_radiation
        if wind_speed is not None:
            field_dict["WindSpeed"] = wind_speed
        if z_factor_uom is not None:
            field_dict["ZFactorUom"] = z_factor_uom
        if air_buoyancy_uom is not None:
            field_dict["AirBuoyancyUom"] = air_buoyancy_uom
        if evaporation_rate_uom is not None:
            field_dict["EvaporationRateUom"] = evaporation_rate_uom
        if air_humidity_uom is not None:
            field_dict["AirHumidityUom"] = air_humidity_uom
        if altitude_uom is not None:
            field_dict["AltitudeUom"] = altitude_uom
        if ambient_temperature_uom is not None:
            field_dict["AmbientTemperatureUom"] = ambient_temperature_uom
        if barometric_pressure_uom is not None:
            field_dict["BarometricPressureUom"] = barometric_pressure_uom
        if light_intensity_uom is not None:
            field_dict["LightIntensityUom"] = light_intensity_uom
        if noise_level_uom is not None:
            field_dict["NoiseLevelUom"] = noise_level_uom
        if ph_level_uom is not None:
            field_dict["PhLevelUom"] = ph_level_uom
        if water_conductivity_uom is not None:
            field_dict["WaterConductivityUom"] = water_conductivity_uom
        if water_temperature_uom is not None:
            field_dict["WaterTemperatureUom"] = water_temperature_uom
        if solar_radiation_uom is not None:
            field_dict["SolarRadiationUom"] = solar_radiation_uom
        if wind_speed_uom is not None:
            field_dict["WindSpeedUom"] = wind_speed_uom
        if specification_name is not None:
            field_dict["SpecificationName"] = specification_name
        if parameter_name is not None:
            field_dict["ParameterName"] = parameter_name
        if measurement_set_display_order is not None:
            field_dict["MeasurementSetDisplayOrder"] = measurement_set_display_order
        if display_order is not None:
            field_dict["DisplayOrder"] = display_order
        if unit_of_measure is not None:
            field_dict["UnitOfMeasure"] = unit_of_measure
        if display_format is not None:
            field_dict["DisplayFormat"] = display_format
        if precision is not None:
            field_dict["Precision"] = precision
        if minimum is not None:
            field_dict["Minimum"] = minimum
        if nominal is not None:
            field_dict["Nominal"] = nominal
        if expected_value is not None:
            field_dict["ExpectedValue"] = expected_value
        if expected_value_raw is not None:
            field_dict["ExpectedValueRaw"] = expected_value_raw
        if test_value is not None:
            field_dict["TestValue"] = test_value
        if base_value is not None:
            field_dict["BaseValue"] = base_value
        if use_expected_value is not None:
            field_dict["UseExpectedValue"] = use_expected_value
        if reading_entry_logic is not None:
            field_dict["ReadingEntryLogic"] = reading_entry_logic
        if reading_entry_math is not None:
            field_dict["ReadingEntryMath"] = reading_entry_math
        if double_substitution_sequence is not None:
            field_dict["DoubleSubstitutionSequence"] = double_substitution_sequence
        if reading_entry_math_string is not None:
            field_dict["ReadingEntryMathString"] = reading_entry_math_string
        if nominal_extended is not None:
            field_dict["NominalExtended"] = nominal_extended
        if expected_value_extended is not None:
            field_dict["ExpectedValueExtended"] = expected_value_extended
        if maximum is not None:
            field_dict["Maximum"] = maximum
        if tolerance_min is not None:
            field_dict["ToleranceMin"] = tolerance_min
        if tolerance_max is not None:
            field_dict["ToleranceMax"] = tolerance_max
        if resolution is not None:
            field_dict["Resolution"] = resolution
        if resolution_count is not None:
            field_dict["ResolutionCount"] = resolution_count
        if min_max_header is not None:
            field_dict["MinMaxHeader"] = min_max_header
        if accuracy_class is not None:
            field_dict["AccuracyClass"] = accuracy_class
        if accuracy_class_min is not None:
            field_dict["AccuracyClassMin"] = accuracy_class_min
        if accuracy_class_max is not None:
            field_dict["AccuracyClassMax"] = accuracy_class_max
        if environment_mask is not None:
            field_dict["EnvironmentMask"] = environment_mask
        if display_name is not None:
            field_dict["DisplayName"] = display_name
        if display_part_number is not None:
            field_dict["DisplayPartNumber"] = display_part_number
        if part_number is not None:
            field_dict["PartNumber"] = part_number
        if vendor_company_id is not None:
            field_dict["VendorCompanyId"] = vendor_company_id
        if service_order_number is not None:
            field_dict["ServiceOrderNumber"] = service_order_number
        if custom_order_number is not None:
            field_dict["CustomOrderNumber"] = custom_order_number
        if completed_by_name is not None:
            field_dict["CompletedByName"] = completed_by_name
        if completed_on is not None:
            field_dict["CompletedOn"] = completed_on
        if is_limited is not None:
            field_dict["IsLimited"] = is_limited
        if vendor_tag is not None:
            field_dict["VendorTag"] = vendor_tag
        if vendor_service_notes is not None:
            field_dict["VendorServiceNotes"] = vendor_service_notes
        if room is not None:
            field_dict["Room"] = room
        if segment_name is not None:
            field_dict["SegmentName"] = segment_name
        if schedule_name is not None:
            field_dict["ScheduleName"] = schedule_name
        if next_segment_name is not None:
            field_dict["NextSegmentName"] = next_segment_name
        if certificate_number is not None:
            field_dict["CertificateNumber"] = certificate_number
        if work_status is not None:
            field_dict["WorkStatus"] = work_status
        if service_type is not None:
            field_dict["ServiceType"] = service_type
        if service_level is not None:
            field_dict["ServiceLevel"] = service_level
        if barcode is not None:
            field_dict["Barcode"] = barcode
        if service_comments is not None:
            field_dict["ServiceComments"] = service_comments
        if order_item_number is not None:
            field_dict["OrderItemNumber"] = order_item_number
        if asset_tag is not None:
            field_dict["AssetTag"] = asset_tag
        if asset_user is not None:
            field_dict["AssetUser"] = asset_user
        if serial_number is not None:
            field_dict["SerialNumber"] = serial_number
        if equipment_id is not None:
            field_dict["EquipmentId"] = equipment_id
        if legacy_identifier is not None:
            field_dict["LegacyIdentifier"] = legacy_identifier
        if site_name is not None:
            field_dict["SiteName"] = site_name
        if asset_name is not None:
            field_dict["AssetName"] = asset_name
        if asset_description is not None:
            field_dict["AssetDescription"] = asset_description
        if product_name is not None:
            field_dict["ProductName"] = product_name
        if product_description is not None:
            field_dict["ProductDescription"] = product_description
        if asset_maker is not None:
            field_dict["AssetMaker"] = asset_maker
        if station is not None:
            field_dict["Station"] = station
        if asset_tag_change is not None:
            field_dict["AssetTagChange"] = asset_tag_change
        if asset_user_change is not None:
            field_dict["AssetUserChange"] = asset_user_change
        if serial_number_change is not None:
            field_dict["SerialNumberChange"] = serial_number_change
        if service_date is not None:
            field_dict["ServiceDate"] = service_date
        if next_service_date is not None:
            field_dict["NextServiceDate"] = next_service_date
        if service_order_item_id is not None:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if service_order_id is not None:
            field_dict["ServiceOrderId"] = service_order_id
        if measurement_batch_id is not None:
            field_dict["MeasurementBatchId"] = measurement_batch_id
        if measurement_id is not None:
            field_dict["MeasurementId"] = measurement_id
        if standard_id is not None:
            field_dict["StandardId"] = standard_id
        if tool_id is not None:
            field_dict["ToolId"] = tool_id
        if measurement_tool_id is not None:
            field_dict["MeasurementToolId"] = measurement_tool_id
        if measurement_condition_id is not None:
            field_dict["MeasurementConditionId"] = measurement_condition_id
        if measurement_point_id is not None:
            field_dict["MeasurementPointId"] = measurement_point_id
        if measurement_set_id is not None:
            field_dict["MeasurementSetId"] = measurement_set_id
        if is_hidden is not None:
            field_dict["IsHidden"] = is_hidden
        if readings is not None:
            field_dict["Readings"] = readings
        if tolerance_type is not None:
            field_dict["ToleranceType"] = tolerance_type
        if tolerance_type_string is not None:
            field_dict["ToleranceTypeString"] = tolerance_type_string
        if precision_type is not None:
            field_dict["PrecisionType"] = precision_type
        if specification_mode is not None:
            field_dict["SpecificationMode"] = specification_mode
        if tolerance_mode is not None:
            field_dict["ToleranceMode"] = tolerance_mode
        if tolerance_unit is not None:
            field_dict["ToleranceUnit"] = tolerance_unit
        if tolerance_string is not None:
            field_dict["ToleranceString"] = tolerance_string
        if po_number is not None:
            field_dict["PoNumber"] = po_number
        if secondary_po is not None:
            field_dict["SecondaryPo"] = secondary_po
        if shipped_date is not None:
            field_dict["ShippedDate"] = shipped_date
        if shipment_status is not None:
            field_dict["ShipmentStatus"] = shipment_status
        if shipped_on is not None:
            field_dict["ShippedOn"] = shipped_on
        if delivered_on is not None:
            field_dict["DeliveredOn"] = delivered_on
        if tracking_number is not None:
            field_dict["TrackingNumber"] = tracking_number
        if payment_terms is not None:
            field_dict["PaymentTerms"] = payment_terms
        if shipping_method is not None:
            field_dict["ShippingMethod"] = shipping_method
        if location is not None:
            field_dict["Location"] = location
        if site_access_notes is not None:
            field_dict["SiteAccessNotes"] = site_access_notes
        if abbreviated_uom is not None:
            field_dict["AbbreviatedUOM"] = abbreviated_uom
        if unit_scale_factor is not None:
            field_dict["UnitScaleFactor"] = unit_scale_factor
        if measurement_not_taken_result is not None:
            field_dict["MeasurementNotTakenResult"] = measurement_not_taken_result
        if hide_from_certificate is not None:
            field_dict["HideFromCertificate"] = hide_from_certificate
        if measurement_not_taken_reason is not None:
            field_dict["MeasurementNotTakenReason"] = measurement_not_taken_reason
        if environment_text_1 is not None:
            field_dict["EnvironmentText1"] = environment_text_1
        if environment_text_2 is not None:
            field_dict["EnvironmentText2"] = environment_text_2
        if environment_text_3 is not None:
            field_dict["EnvironmentText3"] = environment_text_3
        if environment_text_4 is not None:
            field_dict["EnvironmentText4"] = environment_text_4
        if environment_text_5 is not None:
            field_dict["EnvironmentText5"] = environment_text_5
        if environment_text_6 is not None:
            field_dict["EnvironmentText6"] = environment_text_6
        if values is not None:
            field_dict["Values"] = values
        if value_1 is not None:
            field_dict["Value1"] = value_1
        if value_2 is not None:
            field_dict["Value2"] = value_2
        if value_3 is not None:
            field_dict["Value3"] = value_3
        if value_4 is not None:
            field_dict["Value4"] = value_4
        if value_5 is not None:
            field_dict["Value5"] = value_5
        if value_6 is not None:
            field_dict["Value6"] = value_6
        if value_7 is not None:
            field_dict["Value7"] = value_7
        if value_8 is not None:
            field_dict["Value8"] = value_8
        if value_9 is not None:
            field_dict["Value9"] = value_9
        if value_10 is not None:
            field_dict["Value10"] = value_10
        if value_11 is not None:
            field_dict["Value11"] = value_11
        if value_12 is not None:
            field_dict["Value12"] = value_12
        if value_13 is not None:
            field_dict["Value13"] = value_13
        if value_14 is not None:
            field_dict["Value14"] = value_14
        if value_15 is not None:
            field_dict["Value15"] = value_15
        if value_16 is not None:
            field_dict["Value16"] = value_16
        if value_17 is not None:
            field_dict["Value17"] = value_17
        if value_18 is not None:
            field_dict["Value18"] = value_18
        if value_19 is not None:
            field_dict["Value19"] = value_19
        if value_20 is not None:
            field_dict["Value20"] = value_20
        if value_21 is not None:
            field_dict["Value21"] = value_21
        if value_22 is not None:
            field_dict["Value22"] = value_22
        if value_23 is not None:
            field_dict["Value23"] = value_23
        if value_24 is not None:
            field_dict["Value24"] = value_24
        if value_25 is not None:
            field_dict["Value25"] = value_25
        if value_26 is not None:
            field_dict["Value26"] = value_26
        if value_27 is not None:
            field_dict["Value27"] = value_27
        if value_28 is not None:
            field_dict["Value28"] = value_28
        if value_29 is not None:
            field_dict["Value29"] = value_29
        if value_30 is not None:
            field_dict["Value30"] = value_30
        if value_31 is not None:
            field_dict["Value31"] = value_31
        if value_32 is not None:
            field_dict["Value32"] = value_32
        if value_33 is not None:
            field_dict["Value33"] = value_33
        if value_34 is not None:
            field_dict["Value34"] = value_34
        if value_35 is not None:
            field_dict["Value35"] = value_35
        if value_36 is not None:
            field_dict["Value36"] = value_36
        if value_37 is not None:
            field_dict["Value37"] = value_37
        if value_38 is not None:
            field_dict["Value38"] = value_38
        if value_39 is not None:
            field_dict["Value39"] = value_39
        if value_40 is not None:
            field_dict["Value40"] = value_40
        if raw_value_1 is not None:
            field_dict["RawValue1"] = raw_value_1
        if raw_value_2 is not None:
            field_dict["RawValue2"] = raw_value_2
        if raw_value_3 is not None:
            field_dict["RawValue3"] = raw_value_3
        if raw_value_4 is not None:
            field_dict["RawValue4"] = raw_value_4
        if raw_value_5 is not None:
            field_dict["RawValue5"] = raw_value_5
        if raw_value_6 is not None:
            field_dict["RawValue6"] = raw_value_6
        if raw_value_7 is not None:
            field_dict["RawValue7"] = raw_value_7
        if raw_value_8 is not None:
            field_dict["RawValue8"] = raw_value_8
        if raw_value_9 is not None:
            field_dict["RawValue9"] = raw_value_9
        if raw_value_10 is not None:
            field_dict["RawValue10"] = raw_value_10
        if raw_value_11 is not None:
            field_dict["RawValue11"] = raw_value_11
        if raw_value_12 is not None:
            field_dict["RawValue12"] = raw_value_12
        if raw_value_13 is not None:
            field_dict["RawValue13"] = raw_value_13
        if raw_value_14 is not None:
            field_dict["RawValue14"] = raw_value_14
        if raw_value_15 is not None:
            field_dict["RawValue15"] = raw_value_15
        if raw_value_16 is not None:
            field_dict["RawValue16"] = raw_value_16
        if raw_value_17 is not None:
            field_dict["RawValue17"] = raw_value_17
        if raw_value_18 is not None:
            field_dict["RawValue18"] = raw_value_18
        if raw_value_19 is not None:
            field_dict["RawValue19"] = raw_value_19
        if raw_value_20 is not None:
            field_dict["RawValue20"] = raw_value_20
        if raw_value_21 is not None:
            field_dict["RawValue21"] = raw_value_21
        if raw_value_22 is not None:
            field_dict["RawValue22"] = raw_value_22
        if raw_value_23 is not None:
            field_dict["RawValue23"] = raw_value_23
        if raw_value_24 is not None:
            field_dict["RawValue24"] = raw_value_24
        if raw_value_25 is not None:
            field_dict["RawValue25"] = raw_value_25
        if raw_value_26 is not None:
            field_dict["RawValue26"] = raw_value_26
        if raw_value_27 is not None:
            field_dict["RawValue27"] = raw_value_27
        if raw_value_28 is not None:
            field_dict["RawValue28"] = raw_value_28
        if raw_value_29 is not None:
            field_dict["RawValue29"] = raw_value_29
        if raw_value_30 is not None:
            field_dict["RawValue30"] = raw_value_30
        if raw_value_31 is not None:
            field_dict["RawValue31"] = raw_value_31
        if raw_value_32 is not None:
            field_dict["RawValue32"] = raw_value_32
        if raw_value_33 is not None:
            field_dict["RawValue33"] = raw_value_33
        if raw_value_34 is not None:
            field_dict["RawValue34"] = raw_value_34
        if raw_value_35 is not None:
            field_dict["RawValue35"] = raw_value_35
        if raw_value_36 is not None:
            field_dict["RawValue36"] = raw_value_36
        if raw_value_37 is not None:
            field_dict["RawValue37"] = raw_value_37
        if raw_value_38 is not None:
            field_dict["RawValue38"] = raw_value_38
        if raw_value_39 is not None:
            field_dict["RawValue39"] = raw_value_39
        if raw_value_40 is not None:
            field_dict["RawValue40"] = raw_value_40
        if subtitles_to_readings is not None:
            field_dict["SubtitlesToReadings"] = subtitles_to_readings
        if value_subtitle_1 is not None:
            field_dict["ValueSubtitle1"] = value_subtitle_1
        if value_subtitle_2 is not None:
            field_dict["ValueSubtitle2"] = value_subtitle_2
        if value_subtitle_3 is not None:
            field_dict["ValueSubtitle3"] = value_subtitle_3
        if value_subtitle_4 is not None:
            field_dict["ValueSubtitle4"] = value_subtitle_4
        if value_subtitle_5 is not None:
            field_dict["ValueSubtitle5"] = value_subtitle_5
        if value_subtitle_6 is not None:
            field_dict["ValueSubtitle6"] = value_subtitle_6
        if value_subtitle_7 is not None:
            field_dict["ValueSubtitle7"] = value_subtitle_7
        if value_subtitle_8 is not None:
            field_dict["ValueSubtitle8"] = value_subtitle_8
        if value_subtitle_9 is not None:
            field_dict["ValueSubtitle9"] = value_subtitle_9
        if value_subtitle_10 is not None:
            field_dict["ValueSubtitle10"] = value_subtitle_10
        if value_subtitle_11 is not None:
            field_dict["ValueSubtitle11"] = value_subtitle_11
        if value_subtitle_12 is not None:
            field_dict["ValueSubtitle12"] = value_subtitle_12
        if value_subtitle_13 is not None:
            field_dict["ValueSubtitle13"] = value_subtitle_13
        if value_subtitle_14 is not None:
            field_dict["ValueSubtitle14"] = value_subtitle_14
        if value_subtitle_15 is not None:
            field_dict["ValueSubtitle15"] = value_subtitle_15
        if value_subtitle_16 is not None:
            field_dict["ValueSubtitle16"] = value_subtitle_16
        if value_subtitle_17 is not None:
            field_dict["ValueSubtitle17"] = value_subtitle_17
        if value_subtitle_18 is not None:
            field_dict["ValueSubtitle18"] = value_subtitle_18
        if value_subtitle_19 is not None:
            field_dict["ValueSubtitle19"] = value_subtitle_19
        if value_subtitle_20 is not None:
            field_dict["ValueSubtitle20"] = value_subtitle_20
        if value_subtitle_21 is not None:
            field_dict["ValueSubtitle21"] = value_subtitle_21
        if value_subtitle_22 is not None:
            field_dict["ValueSubtitle22"] = value_subtitle_22
        if value_subtitle_23 is not None:
            field_dict["ValueSubtitle23"] = value_subtitle_23
        if value_subtitle_24 is not None:
            field_dict["ValueSubtitle24"] = value_subtitle_24
        if value_subtitle_25 is not None:
            field_dict["ValueSubtitle25"] = value_subtitle_25
        if value_subtitle_26 is not None:
            field_dict["ValueSubtitle26"] = value_subtitle_26
        if value_subtitle_27 is not None:
            field_dict["ValueSubtitle27"] = value_subtitle_27
        if value_subtitle_28 is not None:
            field_dict["ValueSubtitle28"] = value_subtitle_28
        if value_subtitle_29 is not None:
            field_dict["ValueSubtitle29"] = value_subtitle_29
        if value_subtitle_30 is not None:
            field_dict["ValueSubtitle30"] = value_subtitle_30
        if value_subtitle_31 is not None:
            field_dict["ValueSubtitle31"] = value_subtitle_31
        if value_subtitle_32 is not None:
            field_dict["ValueSubtitle32"] = value_subtitle_32
        if value_subtitle_33 is not None:
            field_dict["ValueSubtitle33"] = value_subtitle_33
        if value_subtitle_34 is not None:
            field_dict["ValueSubtitle34"] = value_subtitle_34
        if value_subtitle_35 is not None:
            field_dict["ValueSubtitle35"] = value_subtitle_35
        if value_subtitle_36 is not None:
            field_dict["ValueSubtitle36"] = value_subtitle_36
        if value_subtitle_37 is not None:
            field_dict["ValueSubtitle37"] = value_subtitle_37
        if value_subtitle_38 is not None:
            field_dict["ValueSubtitle38"] = value_subtitle_38
        if value_subtitle_39 is not None:
            field_dict["ValueSubtitle39"] = value_subtitle_39
        if value_subtitle_40 is not None:
            field_dict["ValueSubtitle40"] = value_subtitle_40
        if values_decimal_places is not None:
            field_dict["ValuesDecimalPlaces"] = values_decimal_places
        if repeat_measurement_and_calculate_hysteresis is not None:
            field_dict["RepeatMeasurementAndCalculateHysteresis"] = (
                repeat_measurement_and_calculate_hysteresis
            )
        if measurement_point_order is not None:
            field_dict["MeasurementPointOrder"] = measurement_point_order
        if hysteresis_point is not None:
            field_dict["HysteresisPoint"] = hysteresis_point
        if max_hysteresis is not None:
            field_dict["MaxHysteresis"] = max_hysteresis
        if run is not None:
            field_dict["Run"] = run
        if direction is not None:
            field_dict["Direction"] = direction
        if hysteresis is not None:
            field_dict["Hysteresis"] = hysteresis
        if column_mean is not None:
            field_dict["ColumnMean"] = column_mean
        if column_mean_result is not None:
            field_dict["ColumnMeanResult"] = column_mean_result
        if column_sd is not None:
            field_dict["ColumnSD"] = column_sd
        if column_sd_result is not None:
            field_dict["ColumnSDResult"] = column_sd_result
        if column_cv is not None:
            field_dict["ColumnCV"] = column_cv
        if column_cv_result is not None:
            field_dict["ColumnCVResult"] = column_cv_result
        if column_range is not None:
            field_dict["ColumnRange"] = column_range
        if column_range_result is not None:
            field_dict["ColumnRangeResult"] = column_range_result
        if column_delta is not None:
            field_dict["ColumnDelta"] = column_delta
        if column_delta_result is not None:
            field_dict["ColumnDeltaResult"] = column_delta_result
        if column_result is not None:
            field_dict["ColumnResult"] = column_result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_accredited = d.pop("IsAccredited", None)

        service_total = d.pop("ServiceTotal", None)

        repairs_total = d.pop("RepairsTotal", None)

        parts_total = d.pop("PartsTotal", None)

        parameter_id = d.pop("ParameterId", None)

        tool_range_name = d.pop("ToolRangeName", None)

        tool_range_uncertainty = d.pop("ToolRangeUncertainty", None)

        def _parse_primary_tool_last_service_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                primary_tool_last_service_date_type_0 = isoparse(data)

                return primary_tool_last_service_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        primary_tool_last_service_date = _parse_primary_tool_last_service_date(
            d.pop("PrimaryToolLastServiceDate", None)
        )

        def _parse_primary_tool_next_service_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                primary_tool_next_service_date_type_0 = isoparse(data)

                return primary_tool_next_service_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        primary_tool_next_service_date = _parse_primary_tool_next_service_date(
            d.pop("PrimaryToolNextServiceDate", None)
        )

        primary_tool_calibrated_by = d.pop("PrimaryToolCalibratedBy", None)

        primary_tool_tool_name = d.pop("PrimaryToolToolName", None)

        primary_tool_tool_description = d.pop("PrimaryToolToolDescription", None)

        primary_tool_tool_type_name = d.pop("PrimaryToolToolTypeName", None)

        primary_tool_manufacturer = d.pop("PrimaryToolManufacturer", None)

        primary_tool_manufacturer_part_number = d.pop("PrimaryToolManufacturerPartNumber", None)

        primary_tool_serial_number = d.pop("PrimaryToolSerialNumber", None)

        def _parse_secondary_tool_last_service_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                secondary_tool_last_service_date_type_0 = isoparse(data)

                return secondary_tool_last_service_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        secondary_tool_last_service_date = _parse_secondary_tool_last_service_date(
            d.pop("SecondaryToolLastServiceDate", None)
        )

        def _parse_secondary_tool_next_service_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                secondary_tool_next_service_date_type_0 = isoparse(data)

                return secondary_tool_next_service_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        secondary_tool_next_service_date = _parse_secondary_tool_next_service_date(
            d.pop("SecondaryToolNextServiceDate", None)
        )

        secondary_tool_calibrated_by = d.pop("SecondaryToolCalibratedBy", None)

        secondary_tool_tool_name = d.pop("SecondaryToolToolName", None)

        secondary_tool_tool_description = d.pop("SecondaryToolToolDescription", None)

        secondary_tool_tool_type_name = d.pop("SecondaryToolToolTypeName", None)

        secondary_tool_manufacturer = d.pop("SecondaryToolManufacturer", None)

        secondary_tool_manufacturer_part_number = d.pop("SecondaryToolManufacturerPartNumber", None)

        secondary_tool_serial_number = d.pop("SecondaryToolSerialNumber", None)

        measurement_set_name = d.pop("MeasurementSetName", None)

        decimal_places = d.pop("DecimalPlaces", None)

        significant_figures = d.pop("SignificantFigures", None)

        sd_header = d.pop("SdHeader", None)

        cv_header = d.pop("CvHeader", None)

        _measurement_local_time = d.pop("MeasurementLocalTime", None)
        measurement_local_time: Optional[datetime.datetime]
        if not _measurement_local_time:
            measurement_local_time = None
        else:
            measurement_local_time = isoparse(_measurement_local_time)

        mean = d.pop("Mean", None)

        mean_raw = d.pop("MeanRaw", None)

        mean_decimal_places = d.pop("MeanDecimalPlaces", None)

        mean_extended = d.pop("MeanExtended", None)

        sd = d.pop("Sd", None)

        sd_raw = d.pop("SdRaw", None)

        sd_decimal_places = d.pop("SDDecimalPlaces", None)

        delta = d.pop("Delta", None)

        range_ = d.pop("Range", None)

        sd_extended = d.pop("SdExtended", None)

        range_extended = d.pop("RangeExtended", None)

        delta_extended = d.pop("DeltaExtended", None)

        minimum_measured_value = d.pop("MinimumMeasuredValue", None)

        maximum_measured_value = d.pop("MaximumMeasuredValue", None)

        min_max_value_extended = d.pop("MinMaxValueExtended", None)

        cv = d.pop("Cv", None)

        cv_raw = d.pop("CvRaw", None)

        cv_decimal_places = d.pop("CVDecimalPlaces", None)

        cv_extended = d.pop("CvExtended", None)

        _result = d.pop("Result", None)
        result: Optional[ServiceResultStatus]
        if not _result:
            result = None
        else:
            result = ServiceResultStatus(_result)

        range_result = d.pop("RangeResult", None)

        delta_result = d.pop("DeltaResult", None)

        min_result = d.pop("MinResult", None)

        max_result = d.pop("MaxResult", None)

        tar_result = d.pop("TarResult", None)

        tur_result = d.pop("TurResult", None)

        error_result = d.pop("ErrorResult", None)

        sd_result = d.pop("SdResult", None)

        cv_result = d.pop("CvResult", None)

        custom_field_result = d.pop("CustomFieldResult", None)

        mu = d.pop("Mu", None)

        mu_raw = d.pop("MuRaw", None)

        mu_effective_dof = d.pop("MUEffectiveDOF", None)

        mu_coverage_factor = d.pop("MUCoverageFactor", None)

        mu_extended = d.pop("MuExtended", None)

        cmc = d.pop("Cmc", None)

        cmc_comments = d.pop("CmcComments", None)

        tur = d.pop("Tur", None)

        tur_raw = d.pop("TurRaw", None)

        tur_decimal_places = d.pop("TURDecimalPlaces", None)

        tar = d.pop("Tar", None)

        tar_raw = d.pop("TarRaw", None)

        tar_decimal_places = d.pop("TARDecimalPlaces", None)

        guard_band = d.pop("GuardBand", None)

        _guard_band_logic = d.pop("GuardBandLogic", None)
        guard_band_logic: Optional[ReportDatasetsToMeasurementResponseGuardBandLogic]
        if not _guard_band_logic:
            guard_band_logic = None
        elif _guard_band_logic is None:
            guard_band_logic = None
        else:
            guard_band_logic = ReportDatasetsToMeasurementResponseGuardBandLogic(_guard_band_logic)

        uncertainty_budget = d.pop("UncertaintyBudget", None)

        calculated_uncertainty = d.pop("CalculatedUncertainty", None)

        lock_uncertainty_budget = d.pop("LockUncertaintyBudget", None)

        lab_mu = d.pop("LabMu", None)

        channel = d.pop("Channel", None)

        _measurement_type = d.pop("MeasurementType", None)
        measurement_type: Optional[ReportDatasetsToMeasurementResponseMeasurementType]
        if not _measurement_type:
            measurement_type = None
        elif _measurement_type is None:
            measurement_type = None
        else:
            # Handle both integer and string values for MeasurementType
            if isinstance(_measurement_type, int):
                # Map integer values to string values
                measurement_type_mapping = {
                    0: "Data",
                    1: "Cumulative",
                }
                string_value = measurement_type_mapping.get(_measurement_type)
                if string_value:
                    measurement_type = ReportDatasetsToMeasurementResponseMeasurementType(
                        string_value
                    )
                else:
                    # Unknown integer value, set to None
                    measurement_type = None
            else:
                # Handle string values normally
                measurement_type = ReportDatasetsToMeasurementResponseMeasurementType(
                    _measurement_type
                )

        updated_by = d.pop("UpdatedBy", None)

        _updated_on = d.pop("UpdatedOn", None)
        updated_on: Optional[datetime.datetime]
        if not _updated_on:
            updated_on = None
        else:
            updated_on = isoparse(_updated_on)

        error = d.pop("Error", None)

        error_extended = d.pop("ErrorExtended", None)

        require_adjustment = d.pop("RequireAdjustment", None)

        adjustment_threshold = d.pop("AdjustmentThreshold", None)

        percent_of_tolerance = d.pop("PercentOfTolerance", None)

        percent_of_tolerance_extended = d.pop("PercentOfToleranceExtended", None)

        tol_decimal_places = d.pop("TOLDecimalPlaces", None)

        specification_title = d.pop("SpecificationTitle", None)

        specification_subtitle = d.pop("SpecificationSubtitle", None)

        specification_group = d.pop("SpecificationGroup", None)

        batch_type = d.pop("BatchType", None)

        batch_result = d.pop("BatchResult", None)

        is_by_channel = d.pop("IsByChannel", None)

        channel_count = d.pop("ChannelCount", None)

        is_range_accredited = d.pop("IsRangeAccredited", None)

        _commenced_on = d.pop("CommencedOn", None)
        commenced_on: Optional[datetime.datetime]
        if not _commenced_on:
            commenced_on = None
        elif _commenced_on is None:
            commenced_on = None
        else:
            commenced_on = isoparse(_commenced_on)

        commenced_by = d.pop("CommencedBy", None)

        z_factor = d.pop("ZFactor", None)

        air_buoyancy = d.pop("AirBuoyancy", None)

        evaporation_rate = d.pop("EvaporationRate", None)

        air_humidity = d.pop("AirHumidity", None)

        altitude = d.pop("Altitude", None)

        ambient_temperature = d.pop("AmbientTemperature", None)

        barometric_pressure = d.pop("BarometricPressure", None)

        light_intensity = d.pop("LightIntensity", None)

        noise_level = d.pop("NoiseLevel", None)

        ph_level = d.pop("PhLevel", None)

        water_conductivity = d.pop("WaterConductivity", None)

        water_temperature = d.pop("WaterTemperature", None)

        solar_radiation = d.pop("SolarRadiation", None)

        wind_speed = d.pop("WindSpeed", None)

        z_factor_uom = d.pop("ZFactorUom", None)

        air_buoyancy_uom = d.pop("AirBuoyancyUom", None)

        evaporation_rate_uom = d.pop("EvaporationRateUom", None)

        air_humidity_uom = d.pop("AirHumidityUom", None)

        altitude_uom = d.pop("AltitudeUom", None)

        ambient_temperature_uom = d.pop("AmbientTemperatureUom", None)

        barometric_pressure_uom = d.pop("BarometricPressureUom", None)

        light_intensity_uom = d.pop("LightIntensityUom", None)

        noise_level_uom = d.pop("NoiseLevelUom", None)

        ph_level_uom = d.pop("PhLevelUom", None)

        water_conductivity_uom = d.pop("WaterConductivityUom", None)

        water_temperature_uom = d.pop("WaterTemperatureUom", None)

        solar_radiation_uom = d.pop("SolarRadiationUom", None)

        wind_speed_uom = d.pop("WindSpeedUom", None)

        specification_name = d.pop("SpecificationName", None)

        parameter_name = d.pop("ParameterName", None)

        measurement_set_display_order = d.pop("MeasurementSetDisplayOrder", None)

        display_order = d.pop("DisplayOrder", None)

        unit_of_measure = d.pop("UnitOfMeasure", None)

        display_format = d.pop("DisplayFormat", None)

        precision = d.pop("Precision", None)

        minimum = d.pop("Minimum", None)

        nominal = d.pop("Nominal", None)

        expected_value = d.pop("ExpectedValue", None)

        expected_value_raw = d.pop("ExpectedValueRaw", None)

        test_value = d.pop("TestValue", None)

        base_value = d.pop("BaseValue", None)

        use_expected_value = d.pop("UseExpectedValue", None)

        _reading_entry_logic = d.pop("ReadingEntryLogic", None)
        reading_entry_logic: Optional[ReportDatasetsToMeasurementResponseReadingEntryLogic]
        if not _reading_entry_logic:
            reading_entry_logic = None
        elif _reading_entry_logic is None:
            reading_entry_logic = None
        else:
            # Handle both integer and string values for ReadingEntryLogic
            if isinstance(_reading_entry_logic, int):
                # Map integer values to string values
                reading_entry_logic_mapping = {
                    0: "SingleValue",
                    1: "TwoValues",
                    2: "TwoValuesAndResult",
                    3: "DoubleSubstitution",
                    4: "MeasuredValueConversion",
                    5: "MeasuredValueConversionDisplay",
                }
                string_value = reading_entry_logic_mapping.get(_reading_entry_logic)
                if string_value:
                    reading_entry_logic = ReportDatasetsToMeasurementResponseReadingEntryLogic(
                        string_value
                    )
                else:
                    # Unknown integer value, set to None
                    reading_entry_logic = None
            else:
                # Handle string values normally
                reading_entry_logic = ReportDatasetsToMeasurementResponseReadingEntryLogic(
                    _reading_entry_logic
                )

        _reading_entry_math = d.pop("ReadingEntryMath", None)
        reading_entry_math: Optional[ReportDatasetsToMeasurementResponseReadingEntryMath]
        if not _reading_entry_math:
            reading_entry_math = None
        elif _reading_entry_math is None:
            reading_entry_math = None
        else:
            # Handle both integer and string values for ReadingEntryMath
            if isinstance(_reading_entry_math, int):
                # Map integer values to string values
                reading_entry_math_mapping = {
                    0: "Addition",
                    1: "Subtraction",
                    2: "Multiplication",
                    3: "Division",
                    4: "Average",
                    5: "Difference",
                    6: "ReverseSubtraction",
                    7: "Maximum",
                    8: "Minimum",
                }
                string_value = reading_entry_math_mapping.get(_reading_entry_math)
                if string_value:
                    reading_entry_math = ReportDatasetsToMeasurementResponseReadingEntryMath(
                        string_value
                    )
                else:
                    # Unknown integer value, set to None
                    reading_entry_math = None
            else:
                # Handle string values normally
                reading_entry_math = ReportDatasetsToMeasurementResponseReadingEntryMath(
                    _reading_entry_math
                )

        _double_substitution_sequence = d.pop("DoubleSubstitutionSequence", None)
        double_substitution_sequence: Optional[
            ReportDatasetsToMeasurementResponseDoubleSubstitutionSequence
        ]
        if not _double_substitution_sequence:
            double_substitution_sequence = None
        elif _double_substitution_sequence is None:
            double_substitution_sequence = None
        else:
            # Handle both integer and string values for DoubleSubstitutionSequence
            if isinstance(_double_substitution_sequence, int):
                # Map integer values to string values
                double_substitution_sequence_mapping = {
                    0: "StandardTested",
                    1: "TestedStandard",
                    2: "ZeroStandard",
                }
                string_value = double_substitution_sequence_mapping.get(
                    _double_substitution_sequence
                )
                if string_value:
                    double_substitution_sequence = (
                        ReportDatasetsToMeasurementResponseDoubleSubstitutionSequence(string_value)
                    )
                else:
                    # Unknown integer value, set to None
                    double_substitution_sequence = None
            else:
                # Handle string values normally
                double_substitution_sequence = (
                    ReportDatasetsToMeasurementResponseDoubleSubstitutionSequence(
                        _double_substitution_sequence
                    )
                )

        reading_entry_math_string = d.pop("ReadingEntryMathString", None)

        nominal_extended = d.pop("NominalExtended", None)

        expected_value_extended = d.pop("ExpectedValueExtended", None)

        maximum = d.pop("Maximum", None)

        tolerance_min = d.pop("ToleranceMin", None)

        tolerance_max = d.pop("ToleranceMax", None)

        resolution = d.pop("Resolution", None)

        resolution_count = d.pop("ResolutionCount", None)

        min_max_header = d.pop("MinMaxHeader", None)

        accuracy_class = d.pop("AccuracyClass", None)

        accuracy_class_min = d.pop("AccuracyClassMin", None)

        accuracy_class_max = d.pop("AccuracyClassMax", None)

        _environment_mask = d.pop("EnvironmentMask", None)
        environment_mask: Optional[ReportDatasetsToMeasurementResponseEnvironmentMask]
        if not _environment_mask:
            environment_mask = None
        elif _environment_mask is None:
            environment_mask = None
        else:
            # Handle both integer and string values for EnvironmentMask
            if isinstance(_environment_mask, int):
                # Map integer values to string values (this might be a flag enum)
                environment_mask_mapping = {
                    0: "ZFactor",
                    1: "AirBuoyancy",
                    2: "EvaporationRate",
                    3: "AirHumidity",
                    4: "Altitude",
                    5: "AmbientTemperature",
                    6: "BarometricPressure",
                    7: "LightIntensity",
                    8: "NoiseLevel",
                    9: "PhLevel",
                    10: "WaterConductivity",
                    11: "WaterTemperature",
                    12: "SolarRadiation",
                    13: "WindSpeed",
                }
                string_value = environment_mask_mapping.get(_environment_mask)
                if string_value:
                    environment_mask = ReportDatasetsToMeasurementResponseEnvironmentMask(
                        string_value
                    )
                else:
                    # Unknown integer value, set to None
                    environment_mask = None
            else:
                # Handle string values normally
                environment_mask = ReportDatasetsToMeasurementResponseEnvironmentMask(
                    _environment_mask
                )

        display_name = d.pop("DisplayName", None)

        display_part_number = d.pop("DisplayPartNumber", None)

        part_number = d.pop("PartNumber", None)

        vendor_company_id = d.pop("VendorCompanyId", None)

        service_order_number = d.pop("ServiceOrderNumber", None)

        custom_order_number = d.pop("CustomOrderNumber", None)

        completed_by_name = d.pop("CompletedByName", None)

        _completed_on = d.pop("CompletedOn", None)
        completed_on: Optional[datetime.datetime]
        if not _completed_on:
            completed_on = None
        elif _completed_on is None:
            completed_on = None
        else:
            completed_on = isoparse(_completed_on)

        is_limited = d.pop("IsLimited", None)

        vendor_tag = d.pop("VendorTag", None)

        vendor_service_notes = d.pop("VendorServiceNotes", None)

        room = d.pop("Room", None)

        segment_name = d.pop("SegmentName", None)

        schedule_name = d.pop("ScheduleName", None)

        next_segment_name = d.pop("NextSegmentName", None)

        certificate_number = d.pop("CertificateNumber", None)

        _work_status = d.pop("WorkStatus", None)
        work_status: Optional[WorkStatus]
        if not _work_status:
            work_status = None
        elif _work_status is None:
            work_status = None
        else:
            work_status = WorkStatus(_work_status)

        service_type = d.pop("ServiceType", None)

        service_level = d.pop("ServiceLevel", None)

        barcode = d.pop("Barcode", None)

        service_comments = d.pop("ServiceComments", None)

        order_item_number = d.pop("OrderItemNumber", None)

        asset_tag = d.pop("AssetTag", None)

        asset_user = d.pop("AssetUser", None)

        serial_number = d.pop("SerialNumber", None)

        equipment_id = d.pop("EquipmentId", None)

        legacy_identifier = d.pop("LegacyIdentifier", None)

        site_name = d.pop("SiteName", None)

        asset_name = d.pop("AssetName", None)

        asset_description = d.pop("AssetDescription", None)

        product_name = d.pop("ProductName", None)

        product_description = d.pop("ProductDescription", None)

        asset_maker = d.pop("AssetMaker", None)

        station = d.pop("Station", None)

        asset_tag_change = d.pop("AssetTagChange", None)

        asset_user_change = d.pop("AssetUserChange", None)

        serial_number_change = d.pop("SerialNumberChange", None)

        def _parse_service_date(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                service_date_type_0 = isoparse(data)

                return service_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        service_date = _parse_service_date(d.pop("ServiceDate", None))

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

        service_order_item_id = d.pop("ServiceOrderItemId", None)

        service_order_id = d.pop("ServiceOrderId", None)

        measurement_batch_id = d.pop("MeasurementBatchId", None)

        measurement_id = d.pop("MeasurementId", None)

        standard_id = d.pop("StandardId", None)

        tool_id = d.pop("ToolId", None)

        measurement_tool_id = d.pop("MeasurementToolId", None)

        measurement_condition_id = d.pop("MeasurementConditionId", None)

        measurement_point_id = d.pop("MeasurementPointId", None)

        measurement_set_id = d.pop("MeasurementSetId", None)

        is_hidden = d.pop("IsHidden", None)

        readings = d.pop("Readings", None)

        _tolerance_type = d.pop("ToleranceType", None)
        tolerance_type: Optional[ReportDatasetsToMeasurementResponseToleranceType]
        if not _tolerance_type:
            tolerance_type = None
        elif _tolerance_type is None:
            tolerance_type = None
        else:
            # Handle both integer and string values for ToleranceType
            if isinstance(_tolerance_type, int):
                # Map integer values to string values
                tolerance_type_mapping = {
                    0: "Offset",
                    1: "Percentage",
                    2: "Range",
                    3: "Function",
                    4: "PercentagePlus",
                    5: "Ppm",
                    6: "PpmPlus",
                }
                string_value = tolerance_type_mapping.get(_tolerance_type)
                if string_value:
                    tolerance_type = ReportDatasetsToMeasurementResponseToleranceType(string_value)
                else:
                    # Unknown integer value, set to None
                    tolerance_type = None
            else:
                # Handle string values normally
                tolerance_type = ReportDatasetsToMeasurementResponseToleranceType(_tolerance_type)

        tolerance_type_string = d.pop("ToleranceTypeString", None)

        _precision_type = d.pop("PrecisionType", None)
        precision_type: Optional[ReportDatasetsToMeasurementResponsePrecisionType]
        if not _precision_type:
            precision_type = None
        elif _precision_type is None:
            precision_type = None
        else:
            # Handle both integer and string values for PrecisionType
            if isinstance(_precision_type, int):
                # Map integer values to string values
                precision_type_mapping = {
                    0: "UnitOfMeasure",
                    1: "Percentage",
                    2: "Readability",
                }
                string_value = precision_type_mapping.get(_precision_type)
                if string_value:
                    precision_type = ReportDatasetsToMeasurementResponsePrecisionType(string_value)
                else:
                    # Unknown integer value, set to None
                    precision_type = None
            else:
                # Handle string values normally
                precision_type = ReportDatasetsToMeasurementResponsePrecisionType(_precision_type)

        _specification_mode = d.pop("SpecificationMode", None)
        specification_mode: Optional[ReportDatasetsToMeasurementResponseSpecificationMode]
        if not _specification_mode:
            specification_mode = None
        else:
            specification_mode = ReportDatasetsToMeasurementResponseSpecificationMode(
                _specification_mode
            )

        _tolerance_mode = d.pop("ToleranceMode", None)
        tolerance_mode: Optional[ReportDatasetsToMeasurementResponseToleranceMode]
        if not _tolerance_mode:
            tolerance_mode = None
        else:
            tolerance_mode = ReportDatasetsToMeasurementResponseToleranceMode(_tolerance_mode)

        _tolerance_unit = d.pop("ToleranceUnit", None)
        tolerance_unit: Optional[ReportDatasetsToMeasurementResponseToleranceUnit]
        if not _tolerance_unit:
            tolerance_unit = None
        else:
            tolerance_unit = ReportDatasetsToMeasurementResponseToleranceUnit(_tolerance_unit)

        tolerance_string = d.pop("ToleranceString", None)

        po_number = d.pop("PoNumber", None)

        secondary_po = d.pop("SecondaryPo", None)

        def _parse_shipped_date(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shipped_date_type_0 = isoparse(data)

                return shipped_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        shipped_date = _parse_shipped_date(d.pop("ShippedDate", None))

        _shipment_status = d.pop("ShipmentStatus", None)
        shipment_status: Optional[ReportDatasetsToMeasurementResponseShipmentStatus]
        if not _shipment_status:
            shipment_status = None
        elif _shipment_status is None:
            shipment_status = None
        else:
            # Handle both integer and string values for ShipmentStatus
            try:
                if isinstance(_shipment_status, int):
                    # Convert integer to string to preserve the information
                    _shipment_status = str(_shipment_status)
                shipment_status = ReportDatasetsToMeasurementResponseShipmentStatus(
                    _shipment_status
                )
            except ValueError:
                # If the value is not a valid enum value, preserve it as a string attribute
                # This preserves the information while allowing the object to be created
                shipment_status = None
                # TODO: Consider logging this unknown value: _shipment_status

        _shipped_on = d.pop("ShippedOn", None)
        shipped_on: Optional[datetime.datetime]
        if not _shipped_on:
            shipped_on = None
        elif _shipped_on is None:
            shipped_on = None
        else:
            shipped_on = isoparse(_shipped_on)

        _delivered_on = d.pop("DeliveredOn", None)
        delivered_on: Optional[datetime.datetime]
        if not _delivered_on:
            delivered_on = None
        elif _delivered_on is None:
            delivered_on = None
        else:
            delivered_on = isoparse(_delivered_on)

        tracking_number = d.pop("TrackingNumber", None)

        payment_terms = d.pop("PaymentTerms", None)

        shipping_method = d.pop("ShippingMethod", None)

        location = d.pop("Location", None)

        site_access_notes = d.pop("SiteAccessNotes", None)

        abbreviated_uom = d.pop("AbbreviatedUOM", None)

        unit_scale_factor = d.pop("UnitScaleFactor", None)

        _measurement_not_taken_result = d.pop("MeasurementNotTakenResult", None)
        measurement_not_taken_result: Optional[
            ReportDatasetsToMeasurementResponseMeasurementNotTakenResult
        ]
        if not _measurement_not_taken_result:
            measurement_not_taken_result = None
        elif _measurement_not_taken_result is None:
            measurement_not_taken_result = None
        else:
            # Handle integer to string mapping for MeasurementNotTakenResult enum
            if isinstance(_measurement_not_taken_result, int):
                int_to_str_map = {0: "Fail", 1: "Pass", 2: "Limited"}
                _measurement_not_taken_result = int_to_str_map.get(
                    _measurement_not_taken_result, str(_measurement_not_taken_result)
                )

            try:
                measurement_not_taken_result = (
                    ReportDatasetsToMeasurementResponseMeasurementNotTakenResult(
                        _measurement_not_taken_result
                    )
                )
            except ValueError:
                # If the value is not recognized, use None as fallback
                measurement_not_taken_result = None

        hide_from_certificate = d.pop("HideFromCertificate", None)

        measurement_not_taken_reason = d.pop("MeasurementNotTakenReason", None)

        environment_text_1 = d.pop("EnvironmentText1", None)

        environment_text_2 = d.pop("EnvironmentText2", None)

        environment_text_3 = d.pop("EnvironmentText3", None)

        environment_text_4 = d.pop("EnvironmentText4", None)

        environment_text_5 = d.pop("EnvironmentText5", None)

        environment_text_6 = d.pop("EnvironmentText6", None)

        values = d.pop("Values", None)

        value_1 = d.pop("Value1", None)

        value_2 = d.pop("Value2", None)

        value_3 = d.pop("Value3", None)

        value_4 = d.pop("Value4", None)

        value_5 = d.pop("Value5", None)

        value_6 = d.pop("Value6", None)

        value_7 = d.pop("Value7", None)

        value_8 = d.pop("Value8", None)

        value_9 = d.pop("Value9", None)

        value_10 = d.pop("Value10", None)

        value_11 = d.pop("Value11", None)

        value_12 = d.pop("Value12", None)

        value_13 = d.pop("Value13", None)

        value_14 = d.pop("Value14", None)

        value_15 = d.pop("Value15", None)

        value_16 = d.pop("Value16", None)

        value_17 = d.pop("Value17", None)

        value_18 = d.pop("Value18", None)

        value_19 = d.pop("Value19", None)

        value_20 = d.pop("Value20", None)

        value_21 = d.pop("Value21", None)

        value_22 = d.pop("Value22", None)

        value_23 = d.pop("Value23", None)

        value_24 = d.pop("Value24", None)

        value_25 = d.pop("Value25", None)

        value_26 = d.pop("Value26", None)

        value_27 = d.pop("Value27", None)

        value_28 = d.pop("Value28", None)

        value_29 = d.pop("Value29", None)

        value_30 = d.pop("Value30", None)

        value_31 = d.pop("Value31", None)

        value_32 = d.pop("Value32", None)

        value_33 = d.pop("Value33", None)

        value_34 = d.pop("Value34", None)

        value_35 = d.pop("Value35", None)

        value_36 = d.pop("Value36", None)

        value_37 = d.pop("Value37", None)

        value_38 = d.pop("Value38", None)

        value_39 = d.pop("Value39", None)

        value_40 = d.pop("Value40", None)

        raw_value_1 = d.pop("RawValue1", None)

        raw_value_2 = d.pop("RawValue2", None)

        raw_value_3 = d.pop("RawValue3", None)

        raw_value_4 = d.pop("RawValue4", None)

        raw_value_5 = d.pop("RawValue5", None)

        raw_value_6 = d.pop("RawValue6", None)

        raw_value_7 = d.pop("RawValue7", None)

        raw_value_8 = d.pop("RawValue8", None)

        raw_value_9 = d.pop("RawValue9", None)

        raw_value_10 = d.pop("RawValue10", None)

        raw_value_11 = d.pop("RawValue11", None)

        raw_value_12 = d.pop("RawValue12", None)

        raw_value_13 = d.pop("RawValue13", None)

        raw_value_14 = d.pop("RawValue14", None)

        raw_value_15 = d.pop("RawValue15", None)

        raw_value_16 = d.pop("RawValue16", None)

        raw_value_17 = d.pop("RawValue17", None)

        raw_value_18 = d.pop("RawValue18", None)

        raw_value_19 = d.pop("RawValue19", None)

        raw_value_20 = d.pop("RawValue20", None)

        raw_value_21 = d.pop("RawValue21", None)

        raw_value_22 = d.pop("RawValue22", None)

        raw_value_23 = d.pop("RawValue23", None)

        raw_value_24 = d.pop("RawValue24", None)

        raw_value_25 = d.pop("RawValue25", None)

        raw_value_26 = d.pop("RawValue26", None)

        raw_value_27 = d.pop("RawValue27", None)

        raw_value_28 = d.pop("RawValue28", None)

        raw_value_29 = d.pop("RawValue29", None)

        raw_value_30 = d.pop("RawValue30", None)

        raw_value_31 = d.pop("RawValue31", None)

        raw_value_32 = d.pop("RawValue32", None)

        raw_value_33 = d.pop("RawValue33", None)

        raw_value_34 = d.pop("RawValue34", None)

        raw_value_35 = d.pop("RawValue35", None)

        raw_value_36 = d.pop("RawValue36", None)

        raw_value_37 = d.pop("RawValue37", None)

        raw_value_38 = d.pop("RawValue38", None)

        raw_value_39 = d.pop("RawValue39", None)

        raw_value_40 = d.pop("RawValue40", None)

        subtitles_to_readings = d.pop("SubtitlesToReadings", None)

        value_subtitle_1 = d.pop("ValueSubtitle1", None)

        value_subtitle_2 = d.pop("ValueSubtitle2", None)

        value_subtitle_3 = d.pop("ValueSubtitle3", None)

        value_subtitle_4 = d.pop("ValueSubtitle4", None)

        value_subtitle_5 = d.pop("ValueSubtitle5", None)

        value_subtitle_6 = d.pop("ValueSubtitle6", None)

        value_subtitle_7 = d.pop("ValueSubtitle7", None)

        value_subtitle_8 = d.pop("ValueSubtitle8", None)

        value_subtitle_9 = d.pop("ValueSubtitle9", None)

        value_subtitle_10 = d.pop("ValueSubtitle10", None)

        value_subtitle_11 = d.pop("ValueSubtitle11", None)

        value_subtitle_12 = d.pop("ValueSubtitle12", None)

        value_subtitle_13 = d.pop("ValueSubtitle13", None)

        value_subtitle_14 = d.pop("ValueSubtitle14", None)

        value_subtitle_15 = d.pop("ValueSubtitle15", None)

        value_subtitle_16 = d.pop("ValueSubtitle16", None)

        value_subtitle_17 = d.pop("ValueSubtitle17", None)

        value_subtitle_18 = d.pop("ValueSubtitle18", None)

        value_subtitle_19 = d.pop("ValueSubtitle19", None)

        value_subtitle_20 = d.pop("ValueSubtitle20", None)

        value_subtitle_21 = d.pop("ValueSubtitle21", None)

        value_subtitle_22 = d.pop("ValueSubtitle22", None)

        value_subtitle_23 = d.pop("ValueSubtitle23", None)

        value_subtitle_24 = d.pop("ValueSubtitle24", None)

        value_subtitle_25 = d.pop("ValueSubtitle25", None)

        value_subtitle_26 = d.pop("ValueSubtitle26", None)

        value_subtitle_27 = d.pop("ValueSubtitle27", None)

        value_subtitle_28 = d.pop("ValueSubtitle28", None)

        value_subtitle_29 = d.pop("ValueSubtitle29", None)

        value_subtitle_30 = d.pop("ValueSubtitle30", None)

        value_subtitle_31 = d.pop("ValueSubtitle31", None)

        value_subtitle_32 = d.pop("ValueSubtitle32", None)

        value_subtitle_33 = d.pop("ValueSubtitle33", None)

        value_subtitle_34 = d.pop("ValueSubtitle34", None)

        value_subtitle_35 = d.pop("ValueSubtitle35", None)

        value_subtitle_36 = d.pop("ValueSubtitle36", None)

        value_subtitle_37 = d.pop("ValueSubtitle37", None)

        value_subtitle_38 = d.pop("ValueSubtitle38", None)

        value_subtitle_39 = d.pop("ValueSubtitle39", None)

        value_subtitle_40 = d.pop("ValueSubtitle40", None)

        values_decimal_places = d.pop("ValuesDecimalPlaces", None)

        repeat_measurement_and_calculate_hysteresis = d.pop(
            "RepeatMeasurementAndCalculateHysteresis", None
        )

        _measurement_point_order = d.pop("MeasurementPointOrder", None)
        measurement_point_order: Optional[ReportDatasetsToMeasurementResponseMeasurementPointOrder]
        if not _measurement_point_order:
            measurement_point_order = None
        elif _measurement_point_order is None:
            measurement_point_order = None
        else:
            # Handle integer to string mapping
            if isinstance(_measurement_point_order, int):
                measurement_point_order_map = {
                    0: "AscendingDescending",
                    1: "AsEntered",
                    2: "DescendingAscending",
                    3: "ZeroAscendingDescending",
                    4: "ZeroDescendingAscending",
                }
                _measurement_point_order = measurement_point_order_map.get(
                    _measurement_point_order, _measurement_point_order
                )
            measurement_point_order = ReportDatasetsToMeasurementResponseMeasurementPointOrder(
                _measurement_point_order
            )

        _hysteresis_point = d.pop("HysteresisPoint", None)
        hysteresis_point: Optional[ReportDatasetsToMeasurementResponseHysteresisPoint]
        if not _hysteresis_point:
            hysteresis_point = None
        elif _hysteresis_point is None:
            hysteresis_point = None
        else:
            # Handle integer to string mapping
            if isinstance(_hysteresis_point, int):
                hysteresis_point_map = {0: "First", 1: "None", 2: "Second", 3: "Zero"}
                _hysteresis_point = hysteresis_point_map.get(_hysteresis_point, _hysteresis_point)
            hysteresis_point = ReportDatasetsToMeasurementResponseHysteresisPoint(_hysteresis_point)

        max_hysteresis = d.pop("MaxHysteresis", None)

        run = d.pop("Run", None)

        direction = d.pop("Direction", None)

        hysteresis = d.pop("Hysteresis", None)

        column_mean = d.pop("ColumnMean", None)

        column_mean_result = d.pop("ColumnMeanResult", None)

        column_sd = d.pop("ColumnSD", None)

        column_sd_result = d.pop("ColumnSDResult", None)

        column_cv = d.pop("ColumnCV", None)

        column_cv_result = d.pop("ColumnCVResult", None)

        column_range = d.pop("ColumnRange", None)

        column_range_result = d.pop("ColumnRangeResult", None)

        column_delta = d.pop("ColumnDelta", None)

        column_delta_result = d.pop("ColumnDeltaResult", None)

        column_result = d.pop("ColumnResult", None)

        qualer_api_models_report_datasets_to_measurement_response = cls(
            is_accredited=is_accredited,
            service_total=service_total,
            repairs_total=repairs_total,
            parts_total=parts_total,
            parameter_id=parameter_id,
            tool_range_name=tool_range_name,
            tool_range_uncertainty=tool_range_uncertainty,
            primary_tool_last_service_date=primary_tool_last_service_date,
            primary_tool_next_service_date=primary_tool_next_service_date,
            primary_tool_calibrated_by=primary_tool_calibrated_by,
            primary_tool_tool_name=primary_tool_tool_name,
            primary_tool_tool_description=primary_tool_tool_description,
            primary_tool_tool_type_name=primary_tool_tool_type_name,
            primary_tool_manufacturer=primary_tool_manufacturer,
            primary_tool_manufacturer_part_number=primary_tool_manufacturer_part_number,
            primary_tool_serial_number=primary_tool_serial_number,
            secondary_tool_last_service_date=secondary_tool_last_service_date,
            secondary_tool_next_service_date=secondary_tool_next_service_date,
            secondary_tool_calibrated_by=secondary_tool_calibrated_by,
            secondary_tool_tool_name=secondary_tool_tool_name,
            secondary_tool_tool_description=secondary_tool_tool_description,
            secondary_tool_tool_type_name=secondary_tool_tool_type_name,
            secondary_tool_manufacturer=secondary_tool_manufacturer,
            secondary_tool_manufacturer_part_number=secondary_tool_manufacturer_part_number,
            secondary_tool_serial_number=secondary_tool_serial_number,
            measurement_set_name=measurement_set_name,
            decimal_places=decimal_places,
            significant_figures=significant_figures,
            sd_header=sd_header,
            cv_header=cv_header,
            measurement_local_time=measurement_local_time,
            mean=mean,
            mean_raw=mean_raw,
            mean_decimal_places=mean_decimal_places,
            mean_extended=mean_extended,
            sd=sd,
            sd_raw=sd_raw,
            sd_decimal_places=sd_decimal_places,
            delta=delta,
            range_=range_,
            sd_extended=sd_extended,
            range_extended=range_extended,
            delta_extended=delta_extended,
            minimum_measured_value=minimum_measured_value,
            maximum_measured_value=maximum_measured_value,
            min_max_value_extended=min_max_value_extended,
            cv=cv,
            cv_raw=cv_raw,
            cv_decimal_places=cv_decimal_places,
            cv_extended=cv_extended,
            result=result,
            range_result=range_result,
            delta_result=delta_result,
            min_result=min_result,
            max_result=max_result,
            tar_result=tar_result,
            tur_result=tur_result,
            error_result=error_result,
            sd_result=sd_result,
            cv_result=cv_result,
            custom_field_result=custom_field_result,
            mu=mu,
            mu_raw=mu_raw,
            mu_effective_dof=mu_effective_dof,
            mu_coverage_factor=mu_coverage_factor,
            mu_extended=mu_extended,
            cmc=cmc,
            cmc_comments=cmc_comments,
            tur=tur,
            tur_raw=tur_raw,
            tur_decimal_places=tur_decimal_places,
            tar=tar,
            tar_raw=tar_raw,
            tar_decimal_places=tar_decimal_places,
            guard_band=guard_band,
            guard_band_logic=guard_band_logic,
            uncertainty_budget=uncertainty_budget,
            calculated_uncertainty=calculated_uncertainty,
            lock_uncertainty_budget=lock_uncertainty_budget,
            lab_mu=lab_mu,
            channel=channel,
            measurement_type=measurement_type,
            updated_by=updated_by,
            updated_on=updated_on,
            error=error,
            error_extended=error_extended,
            require_adjustment=require_adjustment,
            adjustment_threshold=adjustment_threshold,
            percent_of_tolerance=percent_of_tolerance,
            percent_of_tolerance_extended=percent_of_tolerance_extended,
            tol_decimal_places=tol_decimal_places,
            specification_title=specification_title,
            specification_subtitle=specification_subtitle,
            specification_group=specification_group,
            batch_type=batch_type,
            batch_result=batch_result,
            is_by_channel=is_by_channel,
            channel_count=channel_count,
            is_range_accredited=is_range_accredited,
            commenced_on=commenced_on,
            commenced_by=commenced_by,
            z_factor=z_factor,
            air_buoyancy=air_buoyancy,
            evaporation_rate=evaporation_rate,
            air_humidity=air_humidity,
            altitude=altitude,
            ambient_temperature=ambient_temperature,
            barometric_pressure=barometric_pressure,
            light_intensity=light_intensity,
            noise_level=noise_level,
            ph_level=ph_level,
            water_conductivity=water_conductivity,
            water_temperature=water_temperature,
            solar_radiation=solar_radiation,
            wind_speed=wind_speed,
            z_factor_uom=z_factor_uom,
            air_buoyancy_uom=air_buoyancy_uom,
            evaporation_rate_uom=evaporation_rate_uom,
            air_humidity_uom=air_humidity_uom,
            altitude_uom=altitude_uom,
            ambient_temperature_uom=ambient_temperature_uom,
            barometric_pressure_uom=barometric_pressure_uom,
            light_intensity_uom=light_intensity_uom,
            noise_level_uom=noise_level_uom,
            ph_level_uom=ph_level_uom,
            water_conductivity_uom=water_conductivity_uom,
            water_temperature_uom=water_temperature_uom,
            solar_radiation_uom=solar_radiation_uom,
            wind_speed_uom=wind_speed_uom,
            specification_name=specification_name,
            parameter_name=parameter_name,
            measurement_set_display_order=measurement_set_display_order,
            display_order=display_order,
            unit_of_measure=unit_of_measure,
            display_format=display_format,
            precision=precision,
            minimum=minimum,
            nominal=nominal,
            expected_value=expected_value,
            expected_value_raw=expected_value_raw,
            test_value=test_value,
            base_value=base_value,
            use_expected_value=use_expected_value,
            reading_entry_logic=reading_entry_logic,
            reading_entry_math=reading_entry_math,
            double_substitution_sequence=double_substitution_sequence,
            reading_entry_math_string=reading_entry_math_string,
            nominal_extended=nominal_extended,
            expected_value_extended=expected_value_extended,
            maximum=maximum,
            tolerance_min=tolerance_min,
            tolerance_max=tolerance_max,
            resolution=resolution,
            resolution_count=resolution_count,
            min_max_header=min_max_header,
            accuracy_class=accuracy_class,
            accuracy_class_min=accuracy_class_min,
            accuracy_class_max=accuracy_class_max,
            environment_mask=environment_mask,
            display_name=display_name,
            display_part_number=display_part_number,
            part_number=part_number,
            vendor_company_id=vendor_company_id,
            service_order_number=service_order_number,
            custom_order_number=custom_order_number,
            completed_by_name=completed_by_name,
            completed_on=completed_on,
            is_limited=is_limited,
            vendor_tag=vendor_tag,
            vendor_service_notes=vendor_service_notes,
            room=room,
            segment_name=segment_name,
            schedule_name=schedule_name,
            next_segment_name=next_segment_name,
            certificate_number=certificate_number,
            work_status=work_status,
            service_type=service_type,
            service_level=service_level,
            barcode=barcode,
            service_comments=service_comments,
            order_item_number=order_item_number,
            asset_tag=asset_tag,
            asset_user=asset_user,
            serial_number=serial_number,
            equipment_id=equipment_id,
            legacy_identifier=legacy_identifier,
            site_name=site_name,
            asset_name=asset_name,
            asset_description=asset_description,
            product_name=product_name,
            product_description=product_description,
            asset_maker=asset_maker,
            station=station,
            asset_tag_change=asset_tag_change,
            asset_user_change=asset_user_change,
            serial_number_change=serial_number_change,
            service_date=service_date,
            next_service_date=next_service_date,
            service_order_item_id=service_order_item_id,
            service_order_id=service_order_id,
            measurement_batch_id=measurement_batch_id,
            measurement_id=measurement_id,
            standard_id=standard_id,
            tool_id=tool_id,
            measurement_tool_id=measurement_tool_id,
            measurement_condition_id=measurement_condition_id,
            measurement_point_id=measurement_point_id,
            measurement_set_id=measurement_set_id,
            is_hidden=is_hidden,
            readings=readings,
            tolerance_type=tolerance_type,
            tolerance_type_string=tolerance_type_string,
            precision_type=precision_type,
            specification_mode=specification_mode,
            tolerance_mode=tolerance_mode,
            tolerance_unit=tolerance_unit,
            tolerance_string=tolerance_string,
            po_number=po_number,
            secondary_po=secondary_po,
            shipped_date=shipped_date,
            shipment_status=shipment_status,
            shipped_on=shipped_on,
            delivered_on=delivered_on,
            tracking_number=tracking_number,
            payment_terms=payment_terms,
            shipping_method=shipping_method,
            location=location,
            site_access_notes=site_access_notes,
            abbreviated_uom=abbreviated_uom,
            unit_scale_factor=unit_scale_factor,
            measurement_not_taken_result=measurement_not_taken_result,
            hide_from_certificate=hide_from_certificate,
            measurement_not_taken_reason=measurement_not_taken_reason,
            environment_text_1=environment_text_1,
            environment_text_2=environment_text_2,
            environment_text_3=environment_text_3,
            environment_text_4=environment_text_4,
            environment_text_5=environment_text_5,
            environment_text_6=environment_text_6,
            values=values,
            value_1=value_1,
            value_2=value_2,
            value_3=value_3,
            value_4=value_4,
            value_5=value_5,
            value_6=value_6,
            value_7=value_7,
            value_8=value_8,
            value_9=value_9,
            value_10=value_10,
            value_11=value_11,
            value_12=value_12,
            value_13=value_13,
            value_14=value_14,
            value_15=value_15,
            value_16=value_16,
            value_17=value_17,
            value_18=value_18,
            value_19=value_19,
            value_20=value_20,
            value_21=value_21,
            value_22=value_22,
            value_23=value_23,
            value_24=value_24,
            value_25=value_25,
            value_26=value_26,
            value_27=value_27,
            value_28=value_28,
            value_29=value_29,
            value_30=value_30,
            value_31=value_31,
            value_32=value_32,
            value_33=value_33,
            value_34=value_34,
            value_35=value_35,
            value_36=value_36,
            value_37=value_37,
            value_38=value_38,
            value_39=value_39,
            value_40=value_40,
            raw_value_1=raw_value_1,
            raw_value_2=raw_value_2,
            raw_value_3=raw_value_3,
            raw_value_4=raw_value_4,
            raw_value_5=raw_value_5,
            raw_value_6=raw_value_6,
            raw_value_7=raw_value_7,
            raw_value_8=raw_value_8,
            raw_value_9=raw_value_9,
            raw_value_10=raw_value_10,
            raw_value_11=raw_value_11,
            raw_value_12=raw_value_12,
            raw_value_13=raw_value_13,
            raw_value_14=raw_value_14,
            raw_value_15=raw_value_15,
            raw_value_16=raw_value_16,
            raw_value_17=raw_value_17,
            raw_value_18=raw_value_18,
            raw_value_19=raw_value_19,
            raw_value_20=raw_value_20,
            raw_value_21=raw_value_21,
            raw_value_22=raw_value_22,
            raw_value_23=raw_value_23,
            raw_value_24=raw_value_24,
            raw_value_25=raw_value_25,
            raw_value_26=raw_value_26,
            raw_value_27=raw_value_27,
            raw_value_28=raw_value_28,
            raw_value_29=raw_value_29,
            raw_value_30=raw_value_30,
            raw_value_31=raw_value_31,
            raw_value_32=raw_value_32,
            raw_value_33=raw_value_33,
            raw_value_34=raw_value_34,
            raw_value_35=raw_value_35,
            raw_value_36=raw_value_36,
            raw_value_37=raw_value_37,
            raw_value_38=raw_value_38,
            raw_value_39=raw_value_39,
            raw_value_40=raw_value_40,
            subtitles_to_readings=subtitles_to_readings,
            value_subtitle_1=value_subtitle_1,
            value_subtitle_2=value_subtitle_2,
            value_subtitle_3=value_subtitle_3,
            value_subtitle_4=value_subtitle_4,
            value_subtitle_5=value_subtitle_5,
            value_subtitle_6=value_subtitle_6,
            value_subtitle_7=value_subtitle_7,
            value_subtitle_8=value_subtitle_8,
            value_subtitle_9=value_subtitle_9,
            value_subtitle_10=value_subtitle_10,
            value_subtitle_11=value_subtitle_11,
            value_subtitle_12=value_subtitle_12,
            value_subtitle_13=value_subtitle_13,
            value_subtitle_14=value_subtitle_14,
            value_subtitle_15=value_subtitle_15,
            value_subtitle_16=value_subtitle_16,
            value_subtitle_17=value_subtitle_17,
            value_subtitle_18=value_subtitle_18,
            value_subtitle_19=value_subtitle_19,
            value_subtitle_20=value_subtitle_20,
            value_subtitle_21=value_subtitle_21,
            value_subtitle_22=value_subtitle_22,
            value_subtitle_23=value_subtitle_23,
            value_subtitle_24=value_subtitle_24,
            value_subtitle_25=value_subtitle_25,
            value_subtitle_26=value_subtitle_26,
            value_subtitle_27=value_subtitle_27,
            value_subtitle_28=value_subtitle_28,
            value_subtitle_29=value_subtitle_29,
            value_subtitle_30=value_subtitle_30,
            value_subtitle_31=value_subtitle_31,
            value_subtitle_32=value_subtitle_32,
            value_subtitle_33=value_subtitle_33,
            value_subtitle_34=value_subtitle_34,
            value_subtitle_35=value_subtitle_35,
            value_subtitle_36=value_subtitle_36,
            value_subtitle_37=value_subtitle_37,
            value_subtitle_38=value_subtitle_38,
            value_subtitle_39=value_subtitle_39,
            value_subtitle_40=value_subtitle_40,
            values_decimal_places=values_decimal_places,
            repeat_measurement_and_calculate_hysteresis=repeat_measurement_and_calculate_hysteresis,
            measurement_point_order=measurement_point_order,
            hysteresis_point=hysteresis_point,
            max_hysteresis=max_hysteresis,
            run=run,
            direction=direction,
            hysteresis=hysteresis,
            column_mean=column_mean,
            column_mean_result=column_mean_result,
            column_sd=column_sd,
            column_sd_result=column_sd_result,
            column_cv=column_cv,
            column_cv_result=column_cv_result,
            column_range=column_range,
            column_range_result=column_range_result,
            column_delta=column_delta,
            column_delta_result=column_delta_result,
            column_result=column_result,
        )

        qualer_api_models_report_datasets_to_measurement_response.additional_properties = d
        return qualer_api_models_report_datasets_to_measurement_response

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
