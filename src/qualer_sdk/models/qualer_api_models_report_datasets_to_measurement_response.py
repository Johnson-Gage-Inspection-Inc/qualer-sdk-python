import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.qualer_api_models_report_datasets_to_measurement_response_double_substitution_sequence import (
    QualerApiModelsReportDatasetsToMeasurementResponseDoubleSubstitutionSequence,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_environment_mask import (
    QualerApiModelsReportDatasetsToMeasurementResponseEnvironmentMask,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_guard_band_logic import (
    QualerApiModelsReportDatasetsToMeasurementResponseGuardBandLogic,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_hysteresis_point import (
    QualerApiModelsReportDatasetsToMeasurementResponseHysteresisPoint,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_measurement_not_taken_result import (
    QualerApiModelsReportDatasetsToMeasurementResponseMeasurementNotTakenResult,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_measurement_point_order import (
    QualerApiModelsReportDatasetsToMeasurementResponseMeasurementPointOrder,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_measurement_type import (
    QualerApiModelsReportDatasetsToMeasurementResponseMeasurementType,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_precision_type import (
    QualerApiModelsReportDatasetsToMeasurementResponsePrecisionType,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_reading_entry_logic import (
    QualerApiModelsReportDatasetsToMeasurementResponseReadingEntryLogic,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_reading_entry_math import (
    QualerApiModelsReportDatasetsToMeasurementResponseReadingEntryMath,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_shipment_status import (
    QualerApiModelsReportDatasetsToMeasurementResponseShipmentStatus,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_specification_mode import (
    QualerApiModelsReportDatasetsToMeasurementResponseSpecificationMode,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_tolerance_mode import (
    QualerApiModelsReportDatasetsToMeasurementResponseToleranceMode,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_tolerance_type import (
    QualerApiModelsReportDatasetsToMeasurementResponseToleranceType,
)
from ..models.qualer_api_models_report_datasets_to_measurement_response_tolerance_unit import (
    QualerApiModelsReportDatasetsToMeasurementResponseToleranceUnit,
)
from ..models.work_status import WorkStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsReportDatasetsToMeasurementResponse")


@_attrs_define
class QualerApiModelsReportDatasetsToMeasurementResponse:
    """
    Attributes:
        is_accredited (Union[None, Unset, bool]):
        service_total (Union[None, Unset, float]):
        repairs_total (Union[None, Unset, float]):
        parts_total (Union[None, Unset, float]):
        parameter_id (Union[None, Unset, int]):
        tool_range_name (Union[None, Unset, str]):
        tool_range_uncertainty (Union[None, Unset, str]):
        primary_tool_last_service_date (Union[None, Unset, datetime.datetime]):
        primary_tool_next_service_date (Union[None, Unset, datetime.datetime]):
        primary_tool_calibrated_by (Union[None, Unset, str]):
        primary_tool_tool_name (Union[None, Unset, str]):
        primary_tool_tool_description (Union[None, Unset, str]):
        primary_tool_tool_type_name (Union[None, Unset, str]):
        primary_tool_manufacturer (Union[None, Unset, str]):
        primary_tool_manufacturer_part_number (Union[None, Unset, str]):
        primary_tool_serial_number (Union[None, Unset, str]):
        secondary_tool_last_service_date (Union[None, Unset, datetime.datetime]):
        secondary_tool_next_service_date (Union[None, Unset, datetime.datetime]):
        secondary_tool_calibrated_by (Union[None, Unset, str]):
        secondary_tool_tool_name (Union[None, Unset, str]):
        secondary_tool_tool_description (Union[None, Unset, str]):
        secondary_tool_tool_type_name (Union[None, Unset, str]):
        secondary_tool_manufacturer (Union[None, Unset, str]):
        secondary_tool_manufacturer_part_number (Union[None, Unset, str]):
        secondary_tool_serial_number (Union[None, Unset, str]):
        measurement_set_name (Union[None, Unset, str]):
        decimal_places (Union[None, Unset, int]):
        significant_figures (Union[None, Unset, int]):
        sd_header (Union[None, Unset, float]):
        cv_header (Union[None, Unset, float]):
        measurement_local_time (Union[None, Unset, datetime.datetime]):
        mean (Union[None, Unset, float]):
        mean_raw (Union[None, Unset, float]):
        mean_decimal_places (Union[None, Unset, int]):
        mean_extended (Union[None, Unset, str]):
        sd (Union[None, Unset, float]):
        sd_raw (Union[None, Unset, float]):
        sd_decimal_places (Union[None, Unset, int]):
        delta (Union[None, Unset, float]):
        range_ (Union[None, Unset, float]):
        sd_extended (Union[None, Unset, str]):
        range_extended (Union[None, Unset, str]):
        delta_extended (Union[None, Unset, str]):
        minimum_measured_value (Union[None, Unset, float]):
        maximum_measured_value (Union[None, Unset, float]):
        min_max_value_extended (Union[None, Unset, str]):
        cv (Union[None, Unset, float]):
        cv_raw (Union[None, Unset, float]):
        cv_decimal_places (Union[None, Unset, int]):
        cv_extended (Union[None, Unset, str]):
        result (Union[None, Unset, int]):
        range_result (Union[None, Unset, bool]):
        delta_result (Union[None, Unset, bool]):
        min_result (Union[None, Unset, bool]):
        max_result (Union[None, Unset, bool]):
        tar_result (Union[None, Unset, bool]):
        tur_result (Union[None, Unset, bool]):
        error_result (Union[None, Unset, bool]):
        sd_result (Union[None, Unset, bool]):
        cv_result (Union[None, Unset, bool]):
        custom_field_result (Union[None, Unset, int]):
        mu (Union[None, Unset, float]):
        mu_raw (Union[None, Unset, float]):
        mu_effective_dof (Union[None, Unset, float]):
        mu_coverage_factor (Union[None, Unset, float]):
        mu_extended (Union[None, Unset, str]):
        cmc (Union[None, Unset, float]):
        cmc_comments (Union[None, Unset, str]):
        tur (Union[None, Unset, float]):
        tur_raw (Union[None, Unset, float]):
        tur_decimal_places (Union[None, Unset, int]):
        tar (Union[None, Unset, float]):
        tar_raw (Union[None, Unset, float]):
        tar_decimal_places (Union[None, Unset, int]):
        guard_band (Union[None, Unset, str]):
        guard_band_logic (Union[None, Unset, QualerApiModelsReportDatasetsToMeasurementResponseGuardBandLogic]):
        uncertainty_budget (Union[None, Unset, str]):
        calculated_uncertainty (Union[None, Unset, float]):
        lock_uncertainty_budget (Union[None, Unset, bool]):
        lab_mu (Union[None, Unset, float]):
        channel (Union[None, Unset, int]):
        measurement_type (Union[None, Unset, QualerApiModelsReportDatasetsToMeasurementResponseMeasurementType]):
        updated_by (Union[None, Unset, str]):
        updated_on (Union[None, Unset, datetime.datetime]):
        error (Union[None, Unset, float]):
        error_extended (Union[None, Unset, str]):
        require_adjustment (Union[None, Unset, bool]):
        adjustment_threshold (Union[None, Unset, float]):
        percent_of_tolerance (Union[None, Unset, float]):
        percent_of_tolerance_extended (Union[None, Unset, str]):
        tol_decimal_places (Union[None, Unset, int]):
        specification_title (Union[None, Unset, str]):
        specification_subtitle (Union[None, Unset, str]):
        specification_group (Union[None, Unset, str]):
        batch_type (Union[None, Unset, int]):
        batch_result (Union[None, Unset, int]):
        is_by_channel (Union[None, Unset, bool]):
        channel_count (Union[None, Unset, int]):
        is_range_accredited (Union[None, Unset, bool]):
        commenced_on (Union[None, Unset, datetime.datetime]):
        commenced_by (Union[None, Unset, str]):
        z_factor (Union[None, Unset, float]):
        air_buoyancy (Union[None, Unset, float]):
        evaporation_rate (Union[None, Unset, float]):
        air_humidity (Union[None, Unset, float]):
        altitude (Union[None, Unset, float]):
        ambient_temperature (Union[None, Unset, float]):
        barometric_pressure (Union[None, Unset, float]):
        light_intensity (Union[None, Unset, float]):
        noise_level (Union[None, Unset, float]):
        ph_level (Union[None, Unset, float]):
        water_conductivity (Union[None, Unset, float]):
        water_temperature (Union[None, Unset, float]):
        solar_radiation (Union[None, Unset, float]):
        wind_speed (Union[None, Unset, float]):
        z_factor_uom (Union[None, Unset, str]):
        air_buoyancy_uom (Union[None, Unset, str]):
        evaporation_rate_uom (Union[None, Unset, str]):
        air_humidity_uom (Union[None, Unset, str]):
        altitude_uom (Union[None, Unset, str]):
        ambient_temperature_uom (Union[None, Unset, str]):
        barometric_pressure_uom (Union[None, Unset, str]):
        light_intensity_uom (Union[None, Unset, str]):
        noise_level_uom (Union[None, Unset, str]):
        ph_level_uom (Union[None, Unset, str]):
        water_conductivity_uom (Union[None, Unset, str]):
        water_temperature_uom (Union[None, Unset, str]):
        solar_radiation_uom (Union[None, Unset, str]):
        wind_speed_uom (Union[None, Unset, str]):
        specification_name (Union[None, Unset, str]):
        parameter_name (Union[None, Unset, str]):
        measurement_set_display_order (Union[None, Unset, int]):
        display_order (Union[None, Unset, int]):
        unit_of_measure (Union[None, Unset, str]):
        display_format (Union[None, Unset, str]):
        precision (Union[None, Unset, float]):
        minimum (Union[None, Unset, float]):
        nominal (Union[None, Unset, float]):
        expected_value (Union[None, Unset, float]):
        expected_value_raw (Union[None, Unset, str]):
        test_value (Union[None, Unset, float]):
        base_value (Union[None, Unset, float]):
        use_expected_value (Union[None, Unset, bool]):
        reading_entry_logic (Union[None, Unset, QualerApiModelsReportDatasetsToMeasurementResponseReadingEntryLogic]):
        reading_entry_math (Union[None, Unset, QualerApiModelsReportDatasetsToMeasurementResponseReadingEntryMath]):
        double_substitution_sequence (Union[None, Unset,
            QualerApiModelsReportDatasetsToMeasurementResponseDoubleSubstitutionSequence]):
        reading_entry_math_string (Union[None, Unset, str]):
        nominal_extended (Union[None, Unset, str]):
        expected_value_extended (Union[None, Unset, str]):
        maximum (Union[None, Unset, float]):
        tolerance_min (Union[None, Unset, float]):
        tolerance_max (Union[None, Unset, float]):
        resolution (Union[None, Unset, float]):
        resolution_count (Union[None, Unset, float]):
        min_max_header (Union[None, Unset, str]):
        accuracy_class (Union[None, Unset, str]):
        accuracy_class_min (Union[None, Unset, float]):
        accuracy_class_max (Union[None, Unset, float]):
        environment_mask (Union[None, Unset, QualerApiModelsReportDatasetsToMeasurementResponseEnvironmentMask]):
        display_name (Union[None, Unset, str]):
        display_part_number (Union[None, Unset, str]):
        part_number (Union[None, Unset, str]):
        vendor_company_id (Union[None, Unset, int]):
        service_order_number (Union[None, Unset, int]):
        custom_order_number (Union[None, Unset, str]):
        completed_by_name (Union[None, Unset, str]):
        completed_on (Union[None, Unset, datetime.datetime]):
        is_limited (Union[None, Unset, bool]):
        vendor_tag (Union[None, Unset, str]):
        vendor_service_notes (Union[None, Unset, str]):
        room (Union[None, Unset, str]):
        segment_name (Union[None, Unset, str]):
        schedule_name (Union[None, Unset, str]):
        next_segment_name (Union[None, Unset, str]):
        certificate_number (Union[None, Unset, str]):
        work_status (Union[None, Unset, WorkStatus]):
        service_type (Union[None, Unset, str]):
        service_level (Union[None, Unset, str]):
        barcode (Union[None, Unset, str]):
        service_comments (Union[None, Unset, str]):
        order_item_number (Union[None, Unset, int]):
        asset_tag (Union[None, Unset, str]):
        asset_user (Union[None, Unset, str]):
        serial_number (Union[None, Unset, str]):
        equipment_id (Union[None, Unset, str]):
        legacy_identifier (Union[None, Unset, str]):
        site_name (Union[None, Unset, str]):
        asset_name (Union[None, Unset, str]):
        asset_description (Union[None, Unset, str]):
        product_name (Union[None, Unset, str]):
        product_description (Union[None, Unset, str]):
        asset_maker (Union[None, Unset, str]):
        station (Union[None, Unset, str]):
        asset_tag_change (Union[None, Unset, str]):
        asset_user_change (Union[None, Unset, str]):
        serial_number_change (Union[None, Unset, str]):
        service_date (Union[None, Unset, datetime.datetime]):
        next_service_date (Union[None, Unset, datetime.datetime]):
        service_order_item_id (Union[None, Unset, int]):
        service_order_id (Union[None, Unset, int]):
        measurement_batch_id (Union[None, Unset, int]):
        measurement_id (Union[None, Unset, int]):
        standard_id (Union[None, Unset, int]):
        tool_id (Union[None, Unset, int]):
        measurement_tool_id (Union[None, Unset, int]):
        measurement_condition_id (Union[None, Unset, int]):
        measurement_point_id (Union[None, Unset, int]):
        measurement_set_id (Union[None, Unset, int]):
        is_hidden (Union[None, Unset, bool]):
        readings (Union[None, Unset, int]):
        tolerance_type (Union[None, Unset, QualerApiModelsReportDatasetsToMeasurementResponseToleranceType]):
        tolerance_type_string (Union[None, Unset, str]):
        precision_type (Union[None, Unset, QualerApiModelsReportDatasetsToMeasurementResponsePrecisionType]):
        specification_mode (Union[None, Unset, QualerApiModelsReportDatasetsToMeasurementResponseSpecificationMode]):
        tolerance_mode (Union[None, Unset, QualerApiModelsReportDatasetsToMeasurementResponseToleranceMode]):
        tolerance_unit (Union[None, Unset, QualerApiModelsReportDatasetsToMeasurementResponseToleranceUnit]):
        tolerance_string (Union[None, Unset, str]):
        po_number (Union[None, Unset, str]):
        secondary_po (Union[None, Unset, str]):
        shipped_date (Union[None, Unset, datetime.datetime]):
        shipment_status (Union[None, Unset, QualerApiModelsReportDatasetsToMeasurementResponseShipmentStatus]):
        shipped_on (Union[None, Unset, datetime.datetime]):
        delivered_on (Union[None, Unset, datetime.datetime]):
        tracking_number (Union[None, Unset, str]):
        payment_terms (Union[None, Unset, int]):
        shipping_method (Union[None, Unset, str]):
        location (Union[None, Unset, str]):
        site_access_notes (Union[None, Unset, str]):
        abbreviated_uom (Union[None, Unset, str]):
        unit_scale_factor (Union[None, Unset, float]):
        measurement_not_taken_result (Union[None, Unset,
            QualerApiModelsReportDatasetsToMeasurementResponseMeasurementNotTakenResult]):
        hide_from_certificate (Union[None, Unset, bool]):
        measurement_not_taken_reason (Union[None, Unset, str]):
        environment_text_1 (Union[None, Unset, str]):
        environment_text_2 (Union[None, Unset, str]):
        environment_text_3 (Union[None, Unset, str]):
        environment_text_4 (Union[None, Unset, str]):
        environment_text_5 (Union[None, Unset, str]):
        environment_text_6 (Union[None, Unset, str]):
        values (Union[None, Unset, str]):
        value_1 (Union[None, Unset, str]):
        value_2 (Union[None, Unset, str]):
        value_3 (Union[None, Unset, str]):
        value_4 (Union[None, Unset, str]):
        value_5 (Union[None, Unset, str]):
        value_6 (Union[None, Unset, str]):
        value_7 (Union[None, Unset, str]):
        value_8 (Union[None, Unset, str]):
        value_9 (Union[None, Unset, str]):
        value_10 (Union[None, Unset, str]):
        value_11 (Union[None, Unset, str]):
        value_12 (Union[None, Unset, str]):
        value_13 (Union[None, Unset, str]):
        value_14 (Union[None, Unset, str]):
        value_15 (Union[None, Unset, str]):
        value_16 (Union[None, Unset, str]):
        value_17 (Union[None, Unset, str]):
        value_18 (Union[None, Unset, str]):
        value_19 (Union[None, Unset, str]):
        value_20 (Union[None, Unset, str]):
        value_21 (Union[None, Unset, str]):
        value_22 (Union[None, Unset, str]):
        value_23 (Union[None, Unset, str]):
        value_24 (Union[None, Unset, str]):
        value_25 (Union[None, Unset, str]):
        value_26 (Union[None, Unset, str]):
        value_27 (Union[None, Unset, str]):
        value_28 (Union[None, Unset, str]):
        value_29 (Union[None, Unset, str]):
        value_30 (Union[None, Unset, str]):
        value_31 (Union[None, Unset, str]):
        value_32 (Union[None, Unset, str]):
        value_33 (Union[None, Unset, str]):
        value_34 (Union[None, Unset, str]):
        value_35 (Union[None, Unset, str]):
        value_36 (Union[None, Unset, str]):
        value_37 (Union[None, Unset, str]):
        value_38 (Union[None, Unset, str]):
        value_39 (Union[None, Unset, str]):
        value_40 (Union[None, Unset, str]):
        raw_value_1 (Union[None, Unset, str]):
        raw_value_2 (Union[None, Unset, str]):
        raw_value_3 (Union[None, Unset, str]):
        raw_value_4 (Union[None, Unset, str]):
        raw_value_5 (Union[None, Unset, str]):
        raw_value_6 (Union[None, Unset, str]):
        raw_value_7 (Union[None, Unset, str]):
        raw_value_8 (Union[None, Unset, str]):
        raw_value_9 (Union[None, Unset, str]):
        raw_value_10 (Union[None, Unset, str]):
        raw_value_11 (Union[None, Unset, str]):
        raw_value_12 (Union[None, Unset, str]):
        raw_value_13 (Union[None, Unset, str]):
        raw_value_14 (Union[None, Unset, str]):
        raw_value_15 (Union[None, Unset, str]):
        raw_value_16 (Union[None, Unset, str]):
        raw_value_17 (Union[None, Unset, str]):
        raw_value_18 (Union[None, Unset, str]):
        raw_value_19 (Union[None, Unset, str]):
        raw_value_20 (Union[None, Unset, str]):
        raw_value_21 (Union[None, Unset, str]):
        raw_value_22 (Union[None, Unset, str]):
        raw_value_23 (Union[None, Unset, str]):
        raw_value_24 (Union[None, Unset, str]):
        raw_value_25 (Union[None, Unset, str]):
        raw_value_26 (Union[None, Unset, str]):
        raw_value_27 (Union[None, Unset, str]):
        raw_value_28 (Union[None, Unset, str]):
        raw_value_29 (Union[None, Unset, str]):
        raw_value_30 (Union[None, Unset, str]):
        raw_value_31 (Union[None, Unset, str]):
        raw_value_32 (Union[None, Unset, str]):
        raw_value_33 (Union[None, Unset, str]):
        raw_value_34 (Union[None, Unset, str]):
        raw_value_35 (Union[None, Unset, str]):
        raw_value_36 (Union[None, Unset, str]):
        raw_value_37 (Union[None, Unset, str]):
        raw_value_38 (Union[None, Unset, str]):
        raw_value_39 (Union[None, Unset, str]):
        raw_value_40 (Union[None, Unset, str]):
        subtitles_to_readings (Union[None, Unset, str]):
        value_subtitle_1 (Union[None, Unset, str]):
        value_subtitle_2 (Union[None, Unset, str]):
        value_subtitle_3 (Union[None, Unset, str]):
        value_subtitle_4 (Union[None, Unset, str]):
        value_subtitle_5 (Union[None, Unset, str]):
        value_subtitle_6 (Union[None, Unset, str]):
        value_subtitle_7 (Union[None, Unset, str]):
        value_subtitle_8 (Union[None, Unset, str]):
        value_subtitle_9 (Union[None, Unset, str]):
        value_subtitle_10 (Union[None, Unset, str]):
        value_subtitle_11 (Union[None, Unset, str]):
        value_subtitle_12 (Union[None, Unset, str]):
        value_subtitle_13 (Union[None, Unset, str]):
        value_subtitle_14 (Union[None, Unset, str]):
        value_subtitle_15 (Union[None, Unset, str]):
        value_subtitle_16 (Union[None, Unset, str]):
        value_subtitle_17 (Union[None, Unset, str]):
        value_subtitle_18 (Union[None, Unset, str]):
        value_subtitle_19 (Union[None, Unset, str]):
        value_subtitle_20 (Union[None, Unset, str]):
        value_subtitle_21 (Union[None, Unset, str]):
        value_subtitle_22 (Union[None, Unset, str]):
        value_subtitle_23 (Union[None, Unset, str]):
        value_subtitle_24 (Union[None, Unset, str]):
        value_subtitle_25 (Union[None, Unset, str]):
        value_subtitle_26 (Union[None, Unset, str]):
        value_subtitle_27 (Union[None, Unset, str]):
        value_subtitle_28 (Union[None, Unset, str]):
        value_subtitle_29 (Union[None, Unset, str]):
        value_subtitle_30 (Union[None, Unset, str]):
        value_subtitle_31 (Union[None, Unset, str]):
        value_subtitle_32 (Union[None, Unset, str]):
        value_subtitle_33 (Union[None, Unset, str]):
        value_subtitle_34 (Union[None, Unset, str]):
        value_subtitle_35 (Union[None, Unset, str]):
        value_subtitle_36 (Union[None, Unset, str]):
        value_subtitle_37 (Union[None, Unset, str]):
        value_subtitle_38 (Union[None, Unset, str]):
        value_subtitle_39 (Union[None, Unset, str]):
        value_subtitle_40 (Union[None, Unset, str]):
        values_decimal_places (Union[None, Unset, int]):
        repeat_measurement_and_calculate_hysteresis (Union[None, Unset, bool]):
        measurement_point_order (Union[None, Unset, QualerApiModelsReportDatasetsToMeasurementResponseMeasurementPointOrder]):
        hysteresis_point (Union[None, Unset, QualerApiModelsReportDatasetsToMeasurementResponseHysteresisPoint]):
        max_hysteresis (Union[None, Unset, float]):
        run (Union[None, Unset, int]):
        direction (Union[None, Unset, int]):
        hysteresis (Union[None, Unset, float]):
        column_mean (Union[None, Unset, str]):
        column_mean_result (Union[None, Unset, str]):
        column_sd (Union[None, Unset, str]):
        column_sd_result (Union[None, Unset, str]):
        column_cv (Union[None, Unset, str]):
        column_cv_result (Union[None, Unset, str]):
        column_range (Union[None, Unset, str]):
        column_range_result (Union[None, Unset, str]):
        column_delta (Union[None, Unset, str]):
        column_delta_result (Union[None, Unset, str]):
        column_result (Union[None, Unset, str]):
    """

    is_accredited: Union[None, Unset, bool] = UNSET
    service_total: Union[None, Unset, float] = UNSET
    repairs_total: Union[None, Unset, float] = UNSET
    parts_total: Union[None, Unset, float] = UNSET
    parameter_id: Union[None, Unset, int] = UNSET
    tool_range_name: Union[None, Unset, str] = UNSET
    tool_range_uncertainty: Union[None, Unset, str] = UNSET
    primary_tool_last_service_date: Union[None, Unset, datetime.datetime] = UNSET
    primary_tool_next_service_date: Union[None, Unset, datetime.datetime] = UNSET
    primary_tool_calibrated_by: Union[None, Unset, str] = UNSET
    primary_tool_tool_name: Union[None, Unset, str] = UNSET
    primary_tool_tool_description: Union[None, Unset, str] = UNSET
    primary_tool_tool_type_name: Union[None, Unset, str] = UNSET
    primary_tool_manufacturer: Union[None, Unset, str] = UNSET
    primary_tool_manufacturer_part_number: Union[None, Unset, str] = UNSET
    primary_tool_serial_number: Union[None, Unset, str] = UNSET
    secondary_tool_last_service_date: Union[None, Unset, datetime.datetime] = UNSET
    secondary_tool_next_service_date: Union[None, Unset, datetime.datetime] = UNSET
    secondary_tool_calibrated_by: Union[None, Unset, str] = UNSET
    secondary_tool_tool_name: Union[None, Unset, str] = UNSET
    secondary_tool_tool_description: Union[None, Unset, str] = UNSET
    secondary_tool_tool_type_name: Union[None, Unset, str] = UNSET
    secondary_tool_manufacturer: Union[None, Unset, str] = UNSET
    secondary_tool_manufacturer_part_number: Union[None, Unset, str] = UNSET
    secondary_tool_serial_number: Union[None, Unset, str] = UNSET
    measurement_set_name: Union[None, Unset, str] = UNSET
    decimal_places: Union[None, Unset, int] = UNSET
    significant_figures: Union[None, Unset, int] = UNSET
    sd_header: Union[None, Unset, float] = UNSET
    cv_header: Union[None, Unset, float] = UNSET
    measurement_local_time: Union[None, Unset, datetime.datetime] = UNSET
    mean: Union[None, Unset, float] = UNSET
    mean_raw: Union[None, Unset, float] = UNSET
    mean_decimal_places: Union[None, Unset, int] = UNSET
    mean_extended: Union[None, Unset, str] = UNSET
    sd: Union[None, Unset, float] = UNSET
    sd_raw: Union[None, Unset, float] = UNSET
    sd_decimal_places: Union[None, Unset, int] = UNSET
    delta: Union[None, Unset, float] = UNSET
    range_: Union[None, Unset, float] = UNSET
    sd_extended: Union[None, Unset, str] = UNSET
    range_extended: Union[None, Unset, str] = UNSET
    delta_extended: Union[None, Unset, str] = UNSET
    minimum_measured_value: Union[None, Unset, float] = UNSET
    maximum_measured_value: Union[None, Unset, float] = UNSET
    min_max_value_extended: Union[None, Unset, str] = UNSET
    cv: Union[None, Unset, float] = UNSET
    cv_raw: Union[None, Unset, float] = UNSET
    cv_decimal_places: Union[None, Unset, int] = UNSET
    cv_extended: Union[None, Unset, str] = UNSET
    result: Union[None, Unset, int] = UNSET
    range_result: Union[None, Unset, bool] = UNSET
    delta_result: Union[None, Unset, bool] = UNSET
    min_result: Union[None, Unset, bool] = UNSET
    max_result: Union[None, Unset, bool] = UNSET
    tar_result: Union[None, Unset, bool] = UNSET
    tur_result: Union[None, Unset, bool] = UNSET
    error_result: Union[None, Unset, bool] = UNSET
    sd_result: Union[None, Unset, bool] = UNSET
    cv_result: Union[None, Unset, bool] = UNSET
    custom_field_result: Union[None, Unset, int] = UNSET
    mu: Union[None, Unset, float] = UNSET
    mu_raw: Union[None, Unset, float] = UNSET
    mu_effective_dof: Union[None, Unset, float] = UNSET
    mu_coverage_factor: Union[None, Unset, float] = UNSET
    mu_extended: Union[None, Unset, str] = UNSET
    cmc: Union[None, Unset, float] = UNSET
    cmc_comments: Union[None, Unset, str] = UNSET
    tur: Union[None, Unset, float] = UNSET
    tur_raw: Union[None, Unset, float] = UNSET
    tur_decimal_places: Union[None, Unset, int] = UNSET
    tar: Union[None, Unset, float] = UNSET
    tar_raw: Union[None, Unset, float] = UNSET
    tar_decimal_places: Union[None, Unset, int] = UNSET
    guard_band: Union[None, Unset, str] = UNSET
    guard_band_logic: Union[
        None, Unset, QualerApiModelsReportDatasetsToMeasurementResponseGuardBandLogic
    ] = UNSET
    uncertainty_budget: Union[None, Unset, str] = UNSET
    calculated_uncertainty: Union[None, Unset, float] = UNSET
    lock_uncertainty_budget: Union[None, Unset, bool] = UNSET
    lab_mu: Union[None, Unset, float] = UNSET
    channel: Union[None, Unset, int] = UNSET
    measurement_type: Union[
        None, Unset, QualerApiModelsReportDatasetsToMeasurementResponseMeasurementType
    ] = UNSET
    updated_by: Union[None, Unset, str] = UNSET
    updated_on: Union[None, Unset, datetime.datetime] = UNSET
    error: Union[None, Unset, float] = UNSET
    error_extended: Union[None, Unset, str] = UNSET
    require_adjustment: Union[None, Unset, bool] = UNSET
    adjustment_threshold: Union[None, Unset, float] = UNSET
    percent_of_tolerance: Union[None, Unset, float] = UNSET
    percent_of_tolerance_extended: Union[None, Unset, str] = UNSET
    tol_decimal_places: Union[None, Unset, int] = UNSET
    specification_title: Union[None, Unset, str] = UNSET
    specification_subtitle: Union[None, Unset, str] = UNSET
    specification_group: Union[None, Unset, str] = UNSET
    batch_type: Union[None, Unset, int] = UNSET
    batch_result: Union[None, Unset, int] = UNSET
    is_by_channel: Union[None, Unset, bool] = UNSET
    channel_count: Union[None, Unset, int] = UNSET
    is_range_accredited: Union[None, Unset, bool] = UNSET
    commenced_on: Union[None, Unset, datetime.datetime] = UNSET
    commenced_by: Union[None, Unset, str] = UNSET
    z_factor: Union[None, Unset, float] = UNSET
    air_buoyancy: Union[None, Unset, float] = UNSET
    evaporation_rate: Union[None, Unset, float] = UNSET
    air_humidity: Union[None, Unset, float] = UNSET
    altitude: Union[None, Unset, float] = UNSET
    ambient_temperature: Union[None, Unset, float] = UNSET
    barometric_pressure: Union[None, Unset, float] = UNSET
    light_intensity: Union[None, Unset, float] = UNSET
    noise_level: Union[None, Unset, float] = UNSET
    ph_level: Union[None, Unset, float] = UNSET
    water_conductivity: Union[None, Unset, float] = UNSET
    water_temperature: Union[None, Unset, float] = UNSET
    solar_radiation: Union[None, Unset, float] = UNSET
    wind_speed: Union[None, Unset, float] = UNSET
    z_factor_uom: Union[None, Unset, str] = UNSET
    air_buoyancy_uom: Union[None, Unset, str] = UNSET
    evaporation_rate_uom: Union[None, Unset, str] = UNSET
    air_humidity_uom: Union[None, Unset, str] = UNSET
    altitude_uom: Union[None, Unset, str] = UNSET
    ambient_temperature_uom: Union[None, Unset, str] = UNSET
    barometric_pressure_uom: Union[None, Unset, str] = UNSET
    light_intensity_uom: Union[None, Unset, str] = UNSET
    noise_level_uom: Union[None, Unset, str] = UNSET
    ph_level_uom: Union[None, Unset, str] = UNSET
    water_conductivity_uom: Union[None, Unset, str] = UNSET
    water_temperature_uom: Union[None, Unset, str] = UNSET
    solar_radiation_uom: Union[None, Unset, str] = UNSET
    wind_speed_uom: Union[None, Unset, str] = UNSET
    specification_name: Union[None, Unset, str] = UNSET
    parameter_name: Union[None, Unset, str] = UNSET
    measurement_set_display_order: Union[None, Unset, int] = UNSET
    display_order: Union[None, Unset, int] = UNSET
    unit_of_measure: Union[None, Unset, str] = UNSET
    display_format: Union[None, Unset, str] = UNSET
    precision: Union[None, Unset, float] = UNSET
    minimum: Union[None, Unset, float] = UNSET
    nominal: Union[None, Unset, float] = UNSET
    expected_value: Union[None, Unset, float] = UNSET
    expected_value_raw: Union[None, Unset, str] = UNSET
    test_value: Union[None, Unset, float] = UNSET
    base_value: Union[None, Unset, float] = UNSET
    use_expected_value: Union[None, Unset, bool] = UNSET
    reading_entry_logic: Union[
        None, Unset, QualerApiModelsReportDatasetsToMeasurementResponseReadingEntryLogic
    ] = UNSET
    reading_entry_math: Union[
        None, Unset, QualerApiModelsReportDatasetsToMeasurementResponseReadingEntryMath
    ] = UNSET
    double_substitution_sequence: Union[
        None,
        Unset,
        QualerApiModelsReportDatasetsToMeasurementResponseDoubleSubstitutionSequence,
    ] = UNSET
    reading_entry_math_string: Union[None, Unset, str] = UNSET
    nominal_extended: Union[None, Unset, str] = UNSET
    expected_value_extended: Union[None, Unset, str] = UNSET
    maximum: Union[None, Unset, float] = UNSET
    tolerance_min: Union[None, Unset, float] = UNSET
    tolerance_max: Union[None, Unset, float] = UNSET
    resolution: Union[None, Unset, float] = UNSET
    resolution_count: Union[None, Unset, float] = UNSET
    min_max_header: Union[None, Unset, str] = UNSET
    accuracy_class: Union[None, Unset, str] = UNSET
    accuracy_class_min: Union[None, Unset, float] = UNSET
    accuracy_class_max: Union[None, Unset, float] = UNSET
    environment_mask: Union[
        None, Unset, QualerApiModelsReportDatasetsToMeasurementResponseEnvironmentMask
    ] = UNSET
    display_name: Union[None, Unset, str] = UNSET
    display_part_number: Union[None, Unset, str] = UNSET
    part_number: Union[None, Unset, str] = UNSET
    vendor_company_id: Union[None, Unset, int] = UNSET
    service_order_number: Union[None, Unset, int] = UNSET
    custom_order_number: Union[None, Unset, str] = UNSET
    completed_by_name: Union[None, Unset, str] = UNSET
    completed_on: Union[None, Unset, datetime.datetime] = UNSET
    is_limited: Union[None, Unset, bool] = UNSET
    vendor_tag: Union[None, Unset, str] = UNSET
    vendor_service_notes: Union[None, Unset, str] = UNSET
    room: Union[None, Unset, str] = UNSET
    segment_name: Union[None, Unset, str] = UNSET
    schedule_name: Union[None, Unset, str] = UNSET
    next_segment_name: Union[None, Unset, str] = UNSET
    certificate_number: Union[None, Unset, str] = UNSET
    work_status: Union[None, Unset, WorkStatus] = UNSET
    service_type: Union[None, Unset, str] = UNSET
    service_level: Union[None, Unset, str] = UNSET
    barcode: Union[None, Unset, str] = UNSET
    service_comments: Union[None, Unset, str] = UNSET
    order_item_number: Union[None, Unset, int] = UNSET
    asset_tag: Union[None, Unset, str] = UNSET
    asset_user: Union[None, Unset, str] = UNSET
    serial_number: Union[None, Unset, str] = UNSET
    equipment_id: Union[None, Unset, str] = UNSET
    legacy_identifier: Union[None, Unset, str] = UNSET
    site_name: Union[None, Unset, str] = UNSET
    asset_name: Union[None, Unset, str] = UNSET
    asset_description: Union[None, Unset, str] = UNSET
    product_name: Union[None, Unset, str] = UNSET
    product_description: Union[None, Unset, str] = UNSET
    asset_maker: Union[None, Unset, str] = UNSET
    station: Union[None, Unset, str] = UNSET
    asset_tag_change: Union[None, Unset, str] = UNSET
    asset_user_change: Union[None, Unset, str] = UNSET
    serial_number_change: Union[None, Unset, str] = UNSET
    service_date: Union[None, Unset, datetime.datetime] = UNSET
    next_service_date: Union[None, Unset, datetime.datetime] = UNSET
    service_order_item_id: Union[None, Unset, int] = UNSET
    service_order_id: Union[None, Unset, int] = UNSET
    measurement_batch_id: Union[None, Unset, int] = UNSET
    measurement_id: Union[None, Unset, int] = UNSET
    standard_id: Union[None, Unset, int] = UNSET
    tool_id: Union[None, Unset, int] = UNSET
    measurement_tool_id: Union[None, Unset, int] = UNSET
    measurement_condition_id: Union[None, Unset, int] = UNSET
    measurement_point_id: Union[None, Unset, int] = UNSET
    measurement_set_id: Union[None, Unset, int] = UNSET
    is_hidden: Union[None, Unset, bool] = UNSET
    readings: Union[None, Unset, int] = UNSET
    tolerance_type: Union[
        None, Unset, QualerApiModelsReportDatasetsToMeasurementResponseToleranceType
    ] = UNSET
    tolerance_type_string: Union[None, Unset, str] = UNSET
    precision_type: Union[
        None, Unset, QualerApiModelsReportDatasetsToMeasurementResponsePrecisionType
    ] = UNSET
    specification_mode: Union[
        None, Unset, QualerApiModelsReportDatasetsToMeasurementResponseSpecificationMode
    ] = UNSET
    tolerance_mode: Union[
        None, Unset, QualerApiModelsReportDatasetsToMeasurementResponseToleranceMode
    ] = UNSET
    tolerance_unit: Union[
        None, Unset, QualerApiModelsReportDatasetsToMeasurementResponseToleranceUnit
    ] = UNSET
    tolerance_string: Union[None, Unset, str] = UNSET
    po_number: Union[None, Unset, str] = UNSET
    secondary_po: Union[None, Unset, str] = UNSET
    shipped_date: Union[None, Unset, datetime.datetime] = UNSET
    shipment_status: Union[
        None, Unset, QualerApiModelsReportDatasetsToMeasurementResponseShipmentStatus
    ] = UNSET
    shipped_on: Union[None, Unset, datetime.datetime] = UNSET
    delivered_on: Union[None, Unset, datetime.datetime] = UNSET
    tracking_number: Union[None, Unset, str] = UNSET
    payment_terms: Union[None, Unset, int] = UNSET
    shipping_method: Union[None, Unset, str] = UNSET
    location: Union[None, Unset, str] = UNSET
    site_access_notes: Union[None, Unset, str] = UNSET
    abbreviated_uom: Union[None, Unset, str] = UNSET
    unit_scale_factor: Union[None, Unset, float] = UNSET
    measurement_not_taken_result: Union[
        None,
        Unset,
        QualerApiModelsReportDatasetsToMeasurementResponseMeasurementNotTakenResult,
    ] = UNSET
    hide_from_certificate: Union[None, Unset, bool] = UNSET
    measurement_not_taken_reason: Union[None, Unset, str] = UNSET
    environment_text_1: Union[None, Unset, str] = UNSET
    environment_text_2: Union[None, Unset, str] = UNSET
    environment_text_3: Union[None, Unset, str] = UNSET
    environment_text_4: Union[None, Unset, str] = UNSET
    environment_text_5: Union[None, Unset, str] = UNSET
    environment_text_6: Union[None, Unset, str] = UNSET
    values: Union[None, Unset, str] = UNSET
    value_1: Union[None, Unset, str] = UNSET
    value_2: Union[None, Unset, str] = UNSET
    value_3: Union[None, Unset, str] = UNSET
    value_4: Union[None, Unset, str] = UNSET
    value_5: Union[None, Unset, str] = UNSET
    value_6: Union[None, Unset, str] = UNSET
    value_7: Union[None, Unset, str] = UNSET
    value_8: Union[None, Unset, str] = UNSET
    value_9: Union[None, Unset, str] = UNSET
    value_10: Union[None, Unset, str] = UNSET
    value_11: Union[None, Unset, str] = UNSET
    value_12: Union[None, Unset, str] = UNSET
    value_13: Union[None, Unset, str] = UNSET
    value_14: Union[None, Unset, str] = UNSET
    value_15: Union[None, Unset, str] = UNSET
    value_16: Union[None, Unset, str] = UNSET
    value_17: Union[None, Unset, str] = UNSET
    value_18: Union[None, Unset, str] = UNSET
    value_19: Union[None, Unset, str] = UNSET
    value_20: Union[None, Unset, str] = UNSET
    value_21: Union[None, Unset, str] = UNSET
    value_22: Union[None, Unset, str] = UNSET
    value_23: Union[None, Unset, str] = UNSET
    value_24: Union[None, Unset, str] = UNSET
    value_25: Union[None, Unset, str] = UNSET
    value_26: Union[None, Unset, str] = UNSET
    value_27: Union[None, Unset, str] = UNSET
    value_28: Union[None, Unset, str] = UNSET
    value_29: Union[None, Unset, str] = UNSET
    value_30: Union[None, Unset, str] = UNSET
    value_31: Union[None, Unset, str] = UNSET
    value_32: Union[None, Unset, str] = UNSET
    value_33: Union[None, Unset, str] = UNSET
    value_34: Union[None, Unset, str] = UNSET
    value_35: Union[None, Unset, str] = UNSET
    value_36: Union[None, Unset, str] = UNSET
    value_37: Union[None, Unset, str] = UNSET
    value_38: Union[None, Unset, str] = UNSET
    value_39: Union[None, Unset, str] = UNSET
    value_40: Union[None, Unset, str] = UNSET
    raw_value_1: Union[None, Unset, str] = UNSET
    raw_value_2: Union[None, Unset, str] = UNSET
    raw_value_3: Union[None, Unset, str] = UNSET
    raw_value_4: Union[None, Unset, str] = UNSET
    raw_value_5: Union[None, Unset, str] = UNSET
    raw_value_6: Union[None, Unset, str] = UNSET
    raw_value_7: Union[None, Unset, str] = UNSET
    raw_value_8: Union[None, Unset, str] = UNSET
    raw_value_9: Union[None, Unset, str] = UNSET
    raw_value_10: Union[None, Unset, str] = UNSET
    raw_value_11: Union[None, Unset, str] = UNSET
    raw_value_12: Union[None, Unset, str] = UNSET
    raw_value_13: Union[None, Unset, str] = UNSET
    raw_value_14: Union[None, Unset, str] = UNSET
    raw_value_15: Union[None, Unset, str] = UNSET
    raw_value_16: Union[None, Unset, str] = UNSET
    raw_value_17: Union[None, Unset, str] = UNSET
    raw_value_18: Union[None, Unset, str] = UNSET
    raw_value_19: Union[None, Unset, str] = UNSET
    raw_value_20: Union[None, Unset, str] = UNSET
    raw_value_21: Union[None, Unset, str] = UNSET
    raw_value_22: Union[None, Unset, str] = UNSET
    raw_value_23: Union[None, Unset, str] = UNSET
    raw_value_24: Union[None, Unset, str] = UNSET
    raw_value_25: Union[None, Unset, str] = UNSET
    raw_value_26: Union[None, Unset, str] = UNSET
    raw_value_27: Union[None, Unset, str] = UNSET
    raw_value_28: Union[None, Unset, str] = UNSET
    raw_value_29: Union[None, Unset, str] = UNSET
    raw_value_30: Union[None, Unset, str] = UNSET
    raw_value_31: Union[None, Unset, str] = UNSET
    raw_value_32: Union[None, Unset, str] = UNSET
    raw_value_33: Union[None, Unset, str] = UNSET
    raw_value_34: Union[None, Unset, str] = UNSET
    raw_value_35: Union[None, Unset, str] = UNSET
    raw_value_36: Union[None, Unset, str] = UNSET
    raw_value_37: Union[None, Unset, str] = UNSET
    raw_value_38: Union[None, Unset, str] = UNSET
    raw_value_39: Union[None, Unset, str] = UNSET
    raw_value_40: Union[None, Unset, str] = UNSET
    subtitles_to_readings: Union[None, Unset, str] = UNSET
    value_subtitle_1: Union[None, Unset, str] = UNSET
    value_subtitle_2: Union[None, Unset, str] = UNSET
    value_subtitle_3: Union[None, Unset, str] = UNSET
    value_subtitle_4: Union[None, Unset, str] = UNSET
    value_subtitle_5: Union[None, Unset, str] = UNSET
    value_subtitle_6: Union[None, Unset, str] = UNSET
    value_subtitle_7: Union[None, Unset, str] = UNSET
    value_subtitle_8: Union[None, Unset, str] = UNSET
    value_subtitle_9: Union[None, Unset, str] = UNSET
    value_subtitle_10: Union[None, Unset, str] = UNSET
    value_subtitle_11: Union[None, Unset, str] = UNSET
    value_subtitle_12: Union[None, Unset, str] = UNSET
    value_subtitle_13: Union[None, Unset, str] = UNSET
    value_subtitle_14: Union[None, Unset, str] = UNSET
    value_subtitle_15: Union[None, Unset, str] = UNSET
    value_subtitle_16: Union[None, Unset, str] = UNSET
    value_subtitle_17: Union[None, Unset, str] = UNSET
    value_subtitle_18: Union[None, Unset, str] = UNSET
    value_subtitle_19: Union[None, Unset, str] = UNSET
    value_subtitle_20: Union[None, Unset, str] = UNSET
    value_subtitle_21: Union[None, Unset, str] = UNSET
    value_subtitle_22: Union[None, Unset, str] = UNSET
    value_subtitle_23: Union[None, Unset, str] = UNSET
    value_subtitle_24: Union[None, Unset, str] = UNSET
    value_subtitle_25: Union[None, Unset, str] = UNSET
    value_subtitle_26: Union[None, Unset, str] = UNSET
    value_subtitle_27: Union[None, Unset, str] = UNSET
    value_subtitle_28: Union[None, Unset, str] = UNSET
    value_subtitle_29: Union[None, Unset, str] = UNSET
    value_subtitle_30: Union[None, Unset, str] = UNSET
    value_subtitle_31: Union[None, Unset, str] = UNSET
    value_subtitle_32: Union[None, Unset, str] = UNSET
    value_subtitle_33: Union[None, Unset, str] = UNSET
    value_subtitle_34: Union[None, Unset, str] = UNSET
    value_subtitle_35: Union[None, Unset, str] = UNSET
    value_subtitle_36: Union[None, Unset, str] = UNSET
    value_subtitle_37: Union[None, Unset, str] = UNSET
    value_subtitle_38: Union[None, Unset, str] = UNSET
    value_subtitle_39: Union[None, Unset, str] = UNSET
    value_subtitle_40: Union[None, Unset, str] = UNSET
    values_decimal_places: Union[None, Unset, int] = UNSET
    repeat_measurement_and_calculate_hysteresis: Union[None, Unset, bool] = UNSET
    measurement_point_order: Union[
        None,
        Unset,
        QualerApiModelsReportDatasetsToMeasurementResponseMeasurementPointOrder,
    ] = UNSET
    hysteresis_point: Union[
        None, Unset, QualerApiModelsReportDatasetsToMeasurementResponseHysteresisPoint
    ] = UNSET
    max_hysteresis: Union[None, Unset, float] = UNSET
    run: Union[None, Unset, int] = UNSET
    direction: Union[None, Unset, int] = UNSET
    hysteresis: Union[None, Unset, float] = UNSET
    column_mean: Union[None, Unset, str] = UNSET
    column_mean_result: Union[None, Unset, str] = UNSET
    column_sd: Union[None, Unset, str] = UNSET
    column_sd_result: Union[None, Unset, str] = UNSET
    column_cv: Union[None, Unset, str] = UNSET
    column_cv_result: Union[None, Unset, str] = UNSET
    column_range: Union[None, Unset, str] = UNSET
    column_range_result: Union[None, Unset, str] = UNSET
    column_delta: Union[None, Unset, str] = UNSET
    column_delta_result: Union[None, Unset, str] = UNSET
    column_result: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_accredited = self.is_accredited

        service_total = self.service_total

        repairs_total = self.repairs_total

        parts_total = self.parts_total

        parameter_id = self.parameter_id

        tool_range_name = self.tool_range_name

        tool_range_uncertainty = self.tool_range_uncertainty

        primary_tool_last_service_date: Union[None, Unset, str]
        if isinstance(self.primary_tool_last_service_date, Unset):
            primary_tool_last_service_date = UNSET
        elif isinstance(self.primary_tool_last_service_date, datetime.datetime):
            primary_tool_last_service_date = (
                self.primary_tool_last_service_date.isoformat()
            )
        else:
            primary_tool_last_service_date = self.primary_tool_last_service_date

        primary_tool_next_service_date: Union[None, Unset, str]
        if isinstance(self.primary_tool_next_service_date, Unset):
            primary_tool_next_service_date = UNSET
        elif isinstance(self.primary_tool_next_service_date, datetime.datetime):
            primary_tool_next_service_date = (
                self.primary_tool_next_service_date.isoformat()
            )
        else:
            primary_tool_next_service_date = self.primary_tool_next_service_date

        primary_tool_calibrated_by = self.primary_tool_calibrated_by

        primary_tool_tool_name = self.primary_tool_tool_name

        primary_tool_tool_description = self.primary_tool_tool_description

        primary_tool_tool_type_name = self.primary_tool_tool_type_name

        primary_tool_manufacturer = self.primary_tool_manufacturer

        primary_tool_manufacturer_part_number = (
            self.primary_tool_manufacturer_part_number
        )

        primary_tool_serial_number = self.primary_tool_serial_number

        secondary_tool_last_service_date: Union[None, Unset, str]
        if isinstance(self.secondary_tool_last_service_date, Unset):
            secondary_tool_last_service_date = UNSET
        elif isinstance(self.secondary_tool_last_service_date, datetime.datetime):
            secondary_tool_last_service_date = (
                self.secondary_tool_last_service_date.isoformat()
            )
        else:
            secondary_tool_last_service_date = self.secondary_tool_last_service_date

        secondary_tool_next_service_date: Union[None, Unset, str]
        if isinstance(self.secondary_tool_next_service_date, Unset):
            secondary_tool_next_service_date = UNSET
        elif isinstance(self.secondary_tool_next_service_date, datetime.datetime):
            secondary_tool_next_service_date = (
                self.secondary_tool_next_service_date.isoformat()
            )
        else:
            secondary_tool_next_service_date = self.secondary_tool_next_service_date

        secondary_tool_calibrated_by = self.secondary_tool_calibrated_by

        secondary_tool_tool_name = self.secondary_tool_tool_name

        secondary_tool_tool_description = self.secondary_tool_tool_description

        secondary_tool_tool_type_name = self.secondary_tool_tool_type_name

        secondary_tool_manufacturer = self.secondary_tool_manufacturer

        secondary_tool_manufacturer_part_number = (
            self.secondary_tool_manufacturer_part_number
        )

        secondary_tool_serial_number = self.secondary_tool_serial_number

        measurement_set_name = self.measurement_set_name

        decimal_places = self.decimal_places

        significant_figures = self.significant_figures

        sd_header = self.sd_header

        cv_header = self.cv_header

        measurement_local_time: Union[None, Unset, str] = UNSET
        if self.measurement_local_time and not isinstance(
            self.measurement_local_time, Unset
        ):
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

        result = self.result

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

        guard_band_logic: Union[None, Unset, str] = UNSET
        if self.guard_band_logic and not isinstance(self.guard_band_logic, Unset):
            guard_band_logic = self.guard_band_logic.value

        uncertainty_budget = self.uncertainty_budget

        calculated_uncertainty = self.calculated_uncertainty

        lock_uncertainty_budget = self.lock_uncertainty_budget

        lab_mu = self.lab_mu

        channel = self.channel

        measurement_type: Union[None, Unset, str] = UNSET
        if self.measurement_type and not isinstance(self.measurement_type, Unset):
            measurement_type = self.measurement_type.value

        updated_by = self.updated_by

        updated_on: Union[None, Unset, str] = UNSET
        if self.updated_on and not isinstance(self.updated_on, Unset):
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

        commenced_on: Union[None, Unset, str] = UNSET
        if self.commenced_on and not isinstance(self.commenced_on, Unset):
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

        reading_entry_logic: Union[None, Unset, str] = UNSET
        if self.reading_entry_logic and not isinstance(self.reading_entry_logic, Unset):
            reading_entry_logic = self.reading_entry_logic.value

        reading_entry_math: Union[None, Unset, str] = UNSET
        if self.reading_entry_math and not isinstance(self.reading_entry_math, Unset):
            reading_entry_math = self.reading_entry_math.value

        double_substitution_sequence: Union[None, Unset, str] = UNSET
        if self.double_substitution_sequence and not isinstance(
            self.double_substitution_sequence, Unset
        ):
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

        environment_mask: Union[None, Unset, str] = UNSET
        if self.environment_mask and not isinstance(self.environment_mask, Unset):
            environment_mask = self.environment_mask.value

        display_name = self.display_name

        display_part_number = self.display_part_number

        part_number = self.part_number

        vendor_company_id = self.vendor_company_id

        service_order_number = self.service_order_number

        custom_order_number = self.custom_order_number

        completed_by_name = self.completed_by_name

        completed_on: Union[None, Unset, str] = UNSET
        if self.completed_on and not isinstance(self.completed_on, Unset):
            completed_on = self.completed_on.isoformat()

        is_limited = self.is_limited

        vendor_tag = self.vendor_tag

        vendor_service_notes = self.vendor_service_notes

        room = self.room

        segment_name = self.segment_name

        schedule_name = self.schedule_name

        next_segment_name = self.next_segment_name

        certificate_number = self.certificate_number

        work_status: Union[None, Unset, int] = UNSET
        if self.work_status and not isinstance(self.work_status, Unset):
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

        service_date: Union[None, Unset, str]
        if isinstance(self.service_date, Unset):
            service_date = UNSET
        elif isinstance(self.service_date, datetime.datetime):
            service_date = self.service_date.isoformat()
        else:
            service_date = self.service_date

        next_service_date: Union[None, Unset, str]
        if isinstance(self.next_service_date, Unset):
            next_service_date = UNSET
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

        tolerance_type: Union[None, Unset, str] = UNSET
        if self.tolerance_type and not isinstance(self.tolerance_type, Unset):
            tolerance_type = self.tolerance_type.value

        tolerance_type_string = self.tolerance_type_string

        precision_type: Union[None, Unset, str] = UNSET
        if self.precision_type and not isinstance(self.precision_type, Unset):
            precision_type = self.precision_type.value

        specification_mode: Union[None, Unset, int] = UNSET
        if self.specification_mode and not isinstance(self.specification_mode, Unset):
            specification_mode = self.specification_mode.value

        tolerance_mode: Union[None, Unset, int] = UNSET
        if self.tolerance_mode and not isinstance(self.tolerance_mode, Unset):
            tolerance_mode = self.tolerance_mode.value

        tolerance_unit: Union[None, Unset, int] = UNSET
        if self.tolerance_unit and not isinstance(self.tolerance_unit, Unset):
            tolerance_unit = self.tolerance_unit.value

        tolerance_string = self.tolerance_string

        po_number = self.po_number

        secondary_po = self.secondary_po

        shipped_date: Union[None, Unset, str]
        if isinstance(self.shipped_date, Unset):
            shipped_date = UNSET
        elif isinstance(self.shipped_date, datetime.datetime):
            shipped_date = self.shipped_date.isoformat()
        else:
            shipped_date = self.shipped_date

        shipment_status: Union[None, Unset, str] = UNSET
        if self.shipment_status and not isinstance(self.shipment_status, Unset):
            shipment_status = self.shipment_status.value

        shipped_on: Union[None, Unset, str] = UNSET
        if self.shipped_on and not isinstance(self.shipped_on, Unset):
            shipped_on = self.shipped_on.isoformat()

        delivered_on: Union[None, Unset, str] = UNSET
        if self.delivered_on and not isinstance(self.delivered_on, Unset):
            delivered_on = self.delivered_on.isoformat()

        tracking_number = self.tracking_number

        payment_terms = self.payment_terms

        shipping_method = self.shipping_method

        location = self.location

        site_access_notes = self.site_access_notes

        abbreviated_uom = self.abbreviated_uom

        unit_scale_factor = self.unit_scale_factor

        measurement_not_taken_result: Union[None, Unset, str] = UNSET
        if self.measurement_not_taken_result and not isinstance(
            self.measurement_not_taken_result, Unset
        ):
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

        measurement_point_order: Union[None, Unset, str] = UNSET
        if self.measurement_point_order and not isinstance(
            self.measurement_point_order, Unset
        ):
            measurement_point_order = self.measurement_point_order.value

        hysteresis_point: Union[None, Unset, str] = UNSET
        if self.hysteresis_point and not isinstance(self.hysteresis_point, Unset):
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_accredited is not UNSET:
            field_dict["IsAccredited"] = is_accredited
        if service_total is not UNSET:
            field_dict["ServiceTotal"] = service_total
        if repairs_total is not UNSET:
            field_dict["RepairsTotal"] = repairs_total
        if parts_total is not UNSET:
            field_dict["PartsTotal"] = parts_total
        if parameter_id is not UNSET:
            field_dict["ParameterId"] = parameter_id
        if tool_range_name is not UNSET:
            field_dict["ToolRangeName"] = tool_range_name
        if tool_range_uncertainty is not UNSET:
            field_dict["ToolRangeUncertainty"] = tool_range_uncertainty
        if primary_tool_last_service_date is not UNSET:
            field_dict["PrimaryToolLastServiceDate"] = primary_tool_last_service_date
        if primary_tool_next_service_date is not UNSET:
            field_dict["PrimaryToolNextServiceDate"] = primary_tool_next_service_date
        if primary_tool_calibrated_by is not UNSET:
            field_dict["PrimaryToolCalibratedBy"] = primary_tool_calibrated_by
        if primary_tool_tool_name is not UNSET:
            field_dict["PrimaryToolToolName"] = primary_tool_tool_name
        if primary_tool_tool_description is not UNSET:
            field_dict["PrimaryToolToolDescription"] = primary_tool_tool_description
        if primary_tool_tool_type_name is not UNSET:
            field_dict["PrimaryToolToolTypeName"] = primary_tool_tool_type_name
        if primary_tool_manufacturer is not UNSET:
            field_dict["PrimaryToolManufacturer"] = primary_tool_manufacturer
        if primary_tool_manufacturer_part_number is not UNSET:
            field_dict["PrimaryToolManufacturerPartNumber"] = (
                primary_tool_manufacturer_part_number
            )
        if primary_tool_serial_number is not UNSET:
            field_dict["PrimaryToolSerialNumber"] = primary_tool_serial_number
        if secondary_tool_last_service_date is not UNSET:
            field_dict["SecondaryToolLastServiceDate"] = (
                secondary_tool_last_service_date
            )
        if secondary_tool_next_service_date is not UNSET:
            field_dict["SecondaryToolNextServiceDate"] = (
                secondary_tool_next_service_date
            )
        if secondary_tool_calibrated_by is not UNSET:
            field_dict["SecondaryToolCalibratedBy"] = secondary_tool_calibrated_by
        if secondary_tool_tool_name is not UNSET:
            field_dict["SecondaryToolToolName"] = secondary_tool_tool_name
        if secondary_tool_tool_description is not UNSET:
            field_dict["SecondaryToolToolDescription"] = secondary_tool_tool_description
        if secondary_tool_tool_type_name is not UNSET:
            field_dict["SecondaryToolToolTypeName"] = secondary_tool_tool_type_name
        if secondary_tool_manufacturer is not UNSET:
            field_dict["SecondaryToolManufacturer"] = secondary_tool_manufacturer
        if secondary_tool_manufacturer_part_number is not UNSET:
            field_dict["SecondaryToolManufacturerPartNumber"] = (
                secondary_tool_manufacturer_part_number
            )
        if secondary_tool_serial_number is not UNSET:
            field_dict["SecondaryToolSerialNumber"] = secondary_tool_serial_number
        if measurement_set_name is not UNSET:
            field_dict["MeasurementSetName"] = measurement_set_name
        if decimal_places is not UNSET:
            field_dict["DecimalPlaces"] = decimal_places
        if significant_figures is not UNSET:
            field_dict["SignificantFigures"] = significant_figures
        if sd_header is not UNSET:
            field_dict["SdHeader"] = sd_header
        if cv_header is not UNSET:
            field_dict["CvHeader"] = cv_header
        if measurement_local_time is not UNSET:
            field_dict["MeasurementLocalTime"] = measurement_local_time
        if mean is not UNSET:
            field_dict["Mean"] = mean
        if mean_raw is not UNSET:
            field_dict["MeanRaw"] = mean_raw
        if mean_decimal_places is not UNSET:
            field_dict["MeanDecimalPlaces"] = mean_decimal_places
        if mean_extended is not UNSET:
            field_dict["MeanExtended"] = mean_extended
        if sd is not UNSET:
            field_dict["Sd"] = sd
        if sd_raw is not UNSET:
            field_dict["SdRaw"] = sd_raw
        if sd_decimal_places is not UNSET:
            field_dict["SDDecimalPlaces"] = sd_decimal_places
        if delta is not UNSET:
            field_dict["Delta"] = delta
        if range_ is not UNSET:
            field_dict["Range"] = range_
        if sd_extended is not UNSET:
            field_dict["SdExtended"] = sd_extended
        if range_extended is not UNSET:
            field_dict["RangeExtended"] = range_extended
        if delta_extended is not UNSET:
            field_dict["DeltaExtended"] = delta_extended
        if minimum_measured_value is not UNSET:
            field_dict["MinimumMeasuredValue"] = minimum_measured_value
        if maximum_measured_value is not UNSET:
            field_dict["MaximumMeasuredValue"] = maximum_measured_value
        if min_max_value_extended is not UNSET:
            field_dict["MinMaxValueExtended"] = min_max_value_extended
        if cv is not UNSET:
            field_dict["Cv"] = cv
        if cv_raw is not UNSET:
            field_dict["CvRaw"] = cv_raw
        if cv_decimal_places is not UNSET:
            field_dict["CVDecimalPlaces"] = cv_decimal_places
        if cv_extended is not UNSET:
            field_dict["CvExtended"] = cv_extended
        if result is not UNSET:
            field_dict["Result"] = result
        if range_result is not UNSET:
            field_dict["RangeResult"] = range_result
        if delta_result is not UNSET:
            field_dict["DeltaResult"] = delta_result
        if min_result is not UNSET:
            field_dict["MinResult"] = min_result
        if max_result is not UNSET:
            field_dict["MaxResult"] = max_result
        if tar_result is not UNSET:
            field_dict["TarResult"] = tar_result
        if tur_result is not UNSET:
            field_dict["TurResult"] = tur_result
        if error_result is not UNSET:
            field_dict["ErrorResult"] = error_result
        if sd_result is not UNSET:
            field_dict["SdResult"] = sd_result
        if cv_result is not UNSET:
            field_dict["CvResult"] = cv_result
        if custom_field_result is not UNSET:
            field_dict["CustomFieldResult"] = custom_field_result
        if mu is not UNSET:
            field_dict["Mu"] = mu
        if mu_raw is not UNSET:
            field_dict["MuRaw"] = mu_raw
        if mu_effective_dof is not UNSET:
            field_dict["MUEffectiveDOF"] = mu_effective_dof
        if mu_coverage_factor is not UNSET:
            field_dict["MUCoverageFactor"] = mu_coverage_factor
        if mu_extended is not UNSET:
            field_dict["MuExtended"] = mu_extended
        if cmc is not UNSET:
            field_dict["Cmc"] = cmc
        if cmc_comments is not UNSET:
            field_dict["CmcComments"] = cmc_comments
        if tur is not UNSET:
            field_dict["Tur"] = tur
        if tur_raw is not UNSET:
            field_dict["TurRaw"] = tur_raw
        if tur_decimal_places is not UNSET:
            field_dict["TURDecimalPlaces"] = tur_decimal_places
        if tar is not UNSET:
            field_dict["Tar"] = tar
        if tar_raw is not UNSET:
            field_dict["TarRaw"] = tar_raw
        if tar_decimal_places is not UNSET:
            field_dict["TARDecimalPlaces"] = tar_decimal_places
        if guard_band is not UNSET:
            field_dict["GuardBand"] = guard_band
        if guard_band_logic is not UNSET:
            field_dict["GuardBandLogic"] = guard_band_logic
        if uncertainty_budget is not UNSET:
            field_dict["UncertaintyBudget"] = uncertainty_budget
        if calculated_uncertainty is not UNSET:
            field_dict["CalculatedUncertainty"] = calculated_uncertainty
        if lock_uncertainty_budget is not UNSET:
            field_dict["LockUncertaintyBudget"] = lock_uncertainty_budget
        if lab_mu is not UNSET:
            field_dict["LabMu"] = lab_mu
        if channel is not UNSET:
            field_dict["Channel"] = channel
        if measurement_type is not UNSET:
            field_dict["MeasurementType"] = measurement_type
        if updated_by is not UNSET:
            field_dict["UpdatedBy"] = updated_by
        if updated_on is not UNSET:
            field_dict["UpdatedOn"] = updated_on
        if error is not UNSET:
            field_dict["Error"] = error
        if error_extended is not UNSET:
            field_dict["ErrorExtended"] = error_extended
        if require_adjustment is not UNSET:
            field_dict["RequireAdjustment"] = require_adjustment
        if adjustment_threshold is not UNSET:
            field_dict["AdjustmentThreshold"] = adjustment_threshold
        if percent_of_tolerance is not UNSET:
            field_dict["PercentOfTolerance"] = percent_of_tolerance
        if percent_of_tolerance_extended is not UNSET:
            field_dict["PercentOfToleranceExtended"] = percent_of_tolerance_extended
        if tol_decimal_places is not UNSET:
            field_dict["TOLDecimalPlaces"] = tol_decimal_places
        if specification_title is not UNSET:
            field_dict["SpecificationTitle"] = specification_title
        if specification_subtitle is not UNSET:
            field_dict["SpecificationSubtitle"] = specification_subtitle
        if specification_group is not UNSET:
            field_dict["SpecificationGroup"] = specification_group
        if batch_type is not UNSET:
            field_dict["BatchType"] = batch_type
        if batch_result is not UNSET:
            field_dict["BatchResult"] = batch_result
        if is_by_channel is not UNSET:
            field_dict["IsByChannel"] = is_by_channel
        if channel_count is not UNSET:
            field_dict["ChannelCount"] = channel_count
        if is_range_accredited is not UNSET:
            field_dict["IsRangeAccredited"] = is_range_accredited
        if commenced_on is not UNSET:
            field_dict["CommencedOn"] = commenced_on
        if commenced_by is not UNSET:
            field_dict["CommencedBy"] = commenced_by
        if z_factor is not UNSET:
            field_dict["ZFactor"] = z_factor
        if air_buoyancy is not UNSET:
            field_dict["AirBuoyancy"] = air_buoyancy
        if evaporation_rate is not UNSET:
            field_dict["EvaporationRate"] = evaporation_rate
        if air_humidity is not UNSET:
            field_dict["AirHumidity"] = air_humidity
        if altitude is not UNSET:
            field_dict["Altitude"] = altitude
        if ambient_temperature is not UNSET:
            field_dict["AmbientTemperature"] = ambient_temperature
        if barometric_pressure is not UNSET:
            field_dict["BarometricPressure"] = barometric_pressure
        if light_intensity is not UNSET:
            field_dict["LightIntensity"] = light_intensity
        if noise_level is not UNSET:
            field_dict["NoiseLevel"] = noise_level
        if ph_level is not UNSET:
            field_dict["PhLevel"] = ph_level
        if water_conductivity is not UNSET:
            field_dict["WaterConductivity"] = water_conductivity
        if water_temperature is not UNSET:
            field_dict["WaterTemperature"] = water_temperature
        if solar_radiation is not UNSET:
            field_dict["SolarRadiation"] = solar_radiation
        if wind_speed is not UNSET:
            field_dict["WindSpeed"] = wind_speed
        if z_factor_uom is not UNSET:
            field_dict["ZFactorUom"] = z_factor_uom
        if air_buoyancy_uom is not UNSET:
            field_dict["AirBuoyancyUom"] = air_buoyancy_uom
        if evaporation_rate_uom is not UNSET:
            field_dict["EvaporationRateUom"] = evaporation_rate_uom
        if air_humidity_uom is not UNSET:
            field_dict["AirHumidityUom"] = air_humidity_uom
        if altitude_uom is not UNSET:
            field_dict["AltitudeUom"] = altitude_uom
        if ambient_temperature_uom is not UNSET:
            field_dict["AmbientTemperatureUom"] = ambient_temperature_uom
        if barometric_pressure_uom is not UNSET:
            field_dict["BarometricPressureUom"] = barometric_pressure_uom
        if light_intensity_uom is not UNSET:
            field_dict["LightIntensityUom"] = light_intensity_uom
        if noise_level_uom is not UNSET:
            field_dict["NoiseLevelUom"] = noise_level_uom
        if ph_level_uom is not UNSET:
            field_dict["PhLevelUom"] = ph_level_uom
        if water_conductivity_uom is not UNSET:
            field_dict["WaterConductivityUom"] = water_conductivity_uom
        if water_temperature_uom is not UNSET:
            field_dict["WaterTemperatureUom"] = water_temperature_uom
        if solar_radiation_uom is not UNSET:
            field_dict["SolarRadiationUom"] = solar_radiation_uom
        if wind_speed_uom is not UNSET:
            field_dict["WindSpeedUom"] = wind_speed_uom
        if specification_name is not UNSET:
            field_dict["SpecificationName"] = specification_name
        if parameter_name is not UNSET:
            field_dict["ParameterName"] = parameter_name
        if measurement_set_display_order is not UNSET:
            field_dict["MeasurementSetDisplayOrder"] = measurement_set_display_order
        if display_order is not UNSET:
            field_dict["DisplayOrder"] = display_order
        if unit_of_measure is not UNSET:
            field_dict["UnitOfMeasure"] = unit_of_measure
        if display_format is not UNSET:
            field_dict["DisplayFormat"] = display_format
        if precision is not UNSET:
            field_dict["Precision"] = precision
        if minimum is not UNSET:
            field_dict["Minimum"] = minimum
        if nominal is not UNSET:
            field_dict["Nominal"] = nominal
        if expected_value is not UNSET:
            field_dict["ExpectedValue"] = expected_value
        if expected_value_raw is not UNSET:
            field_dict["ExpectedValueRaw"] = expected_value_raw
        if test_value is not UNSET:
            field_dict["TestValue"] = test_value
        if base_value is not UNSET:
            field_dict["BaseValue"] = base_value
        if use_expected_value is not UNSET:
            field_dict["UseExpectedValue"] = use_expected_value
        if reading_entry_logic is not UNSET:
            field_dict["ReadingEntryLogic"] = reading_entry_logic
        if reading_entry_math is not UNSET:
            field_dict["ReadingEntryMath"] = reading_entry_math
        if double_substitution_sequence is not UNSET:
            field_dict["DoubleSubstitutionSequence"] = double_substitution_sequence
        if reading_entry_math_string is not UNSET:
            field_dict["ReadingEntryMathString"] = reading_entry_math_string
        if nominal_extended is not UNSET:
            field_dict["NominalExtended"] = nominal_extended
        if expected_value_extended is not UNSET:
            field_dict["ExpectedValueExtended"] = expected_value_extended
        if maximum is not UNSET:
            field_dict["Maximum"] = maximum
        if tolerance_min is not UNSET:
            field_dict["ToleranceMin"] = tolerance_min
        if tolerance_max is not UNSET:
            field_dict["ToleranceMax"] = tolerance_max
        if resolution is not UNSET:
            field_dict["Resolution"] = resolution
        if resolution_count is not UNSET:
            field_dict["ResolutionCount"] = resolution_count
        if min_max_header is not UNSET:
            field_dict["MinMaxHeader"] = min_max_header
        if accuracy_class is not UNSET:
            field_dict["AccuracyClass"] = accuracy_class
        if accuracy_class_min is not UNSET:
            field_dict["AccuracyClassMin"] = accuracy_class_min
        if accuracy_class_max is not UNSET:
            field_dict["AccuracyClassMax"] = accuracy_class_max
        if environment_mask is not UNSET:
            field_dict["EnvironmentMask"] = environment_mask
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if display_part_number is not UNSET:
            field_dict["DisplayPartNumber"] = display_part_number
        if part_number is not UNSET:
            field_dict["PartNumber"] = part_number
        if vendor_company_id is not UNSET:
            field_dict["VendorCompanyId"] = vendor_company_id
        if service_order_number is not UNSET:
            field_dict["ServiceOrderNumber"] = service_order_number
        if custom_order_number is not UNSET:
            field_dict["CustomOrderNumber"] = custom_order_number
        if completed_by_name is not UNSET:
            field_dict["CompletedByName"] = completed_by_name
        if completed_on is not UNSET:
            field_dict["CompletedOn"] = completed_on
        if is_limited is not UNSET:
            field_dict["IsLimited"] = is_limited
        if vendor_tag is not UNSET:
            field_dict["VendorTag"] = vendor_tag
        if vendor_service_notes is not UNSET:
            field_dict["VendorServiceNotes"] = vendor_service_notes
        if room is not UNSET:
            field_dict["Room"] = room
        if segment_name is not UNSET:
            field_dict["SegmentName"] = segment_name
        if schedule_name is not UNSET:
            field_dict["ScheduleName"] = schedule_name
        if next_segment_name is not UNSET:
            field_dict["NextSegmentName"] = next_segment_name
        if certificate_number is not UNSET:
            field_dict["CertificateNumber"] = certificate_number
        if work_status is not UNSET:
            field_dict["WorkStatus"] = work_status
        if service_type is not UNSET:
            field_dict["ServiceType"] = service_type
        if service_level is not UNSET:
            field_dict["ServiceLevel"] = service_level
        if barcode is not UNSET:
            field_dict["Barcode"] = barcode
        if service_comments is not UNSET:
            field_dict["ServiceComments"] = service_comments
        if order_item_number is not UNSET:
            field_dict["OrderItemNumber"] = order_item_number
        if asset_tag is not UNSET:
            field_dict["AssetTag"] = asset_tag
        if asset_user is not UNSET:
            field_dict["AssetUser"] = asset_user
        if serial_number is not UNSET:
            field_dict["SerialNumber"] = serial_number
        if equipment_id is not UNSET:
            field_dict["EquipmentId"] = equipment_id
        if legacy_identifier is not UNSET:
            field_dict["LegacyIdentifier"] = legacy_identifier
        if site_name is not UNSET:
            field_dict["SiteName"] = site_name
        if asset_name is not UNSET:
            field_dict["AssetName"] = asset_name
        if asset_description is not UNSET:
            field_dict["AssetDescription"] = asset_description
        if product_name is not UNSET:
            field_dict["ProductName"] = product_name
        if product_description is not UNSET:
            field_dict["ProductDescription"] = product_description
        if asset_maker is not UNSET:
            field_dict["AssetMaker"] = asset_maker
        if station is not UNSET:
            field_dict["Station"] = station
        if asset_tag_change is not UNSET:
            field_dict["AssetTagChange"] = asset_tag_change
        if asset_user_change is not UNSET:
            field_dict["AssetUserChange"] = asset_user_change
        if serial_number_change is not UNSET:
            field_dict["SerialNumberChange"] = serial_number_change
        if service_date is not UNSET:
            field_dict["ServiceDate"] = service_date
        if next_service_date is not UNSET:
            field_dict["NextServiceDate"] = next_service_date
        if service_order_item_id is not UNSET:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if service_order_id is not UNSET:
            field_dict["ServiceOrderId"] = service_order_id
        if measurement_batch_id is not UNSET:
            field_dict["MeasurementBatchId"] = measurement_batch_id
        if measurement_id is not UNSET:
            field_dict["MeasurementId"] = measurement_id
        if standard_id is not UNSET:
            field_dict["StandardId"] = standard_id
        if tool_id is not UNSET:
            field_dict["ToolId"] = tool_id
        if measurement_tool_id is not UNSET:
            field_dict["MeasurementToolId"] = measurement_tool_id
        if measurement_condition_id is not UNSET:
            field_dict["MeasurementConditionId"] = measurement_condition_id
        if measurement_point_id is not UNSET:
            field_dict["MeasurementPointId"] = measurement_point_id
        if measurement_set_id is not UNSET:
            field_dict["MeasurementSetId"] = measurement_set_id
        if is_hidden is not UNSET:
            field_dict["IsHidden"] = is_hidden
        if readings is not UNSET:
            field_dict["Readings"] = readings
        if tolerance_type is not UNSET:
            field_dict["ToleranceType"] = tolerance_type
        if tolerance_type_string is not UNSET:
            field_dict["ToleranceTypeString"] = tolerance_type_string
        if precision_type is not UNSET:
            field_dict["PrecisionType"] = precision_type
        if specification_mode is not UNSET:
            field_dict["SpecificationMode"] = specification_mode
        if tolerance_mode is not UNSET:
            field_dict["ToleranceMode"] = tolerance_mode
        if tolerance_unit is not UNSET:
            field_dict["ToleranceUnit"] = tolerance_unit
        if tolerance_string is not UNSET:
            field_dict["ToleranceString"] = tolerance_string
        if po_number is not UNSET:
            field_dict["PoNumber"] = po_number
        if secondary_po is not UNSET:
            field_dict["SecondaryPo"] = secondary_po
        if shipped_date is not UNSET:
            field_dict["ShippedDate"] = shipped_date
        if shipment_status is not UNSET:
            field_dict["ShipmentStatus"] = shipment_status
        if shipped_on is not UNSET:
            field_dict["ShippedOn"] = shipped_on
        if delivered_on is not UNSET:
            field_dict["DeliveredOn"] = delivered_on
        if tracking_number is not UNSET:
            field_dict["TrackingNumber"] = tracking_number
        if payment_terms is not UNSET:
            field_dict["PaymentTerms"] = payment_terms
        if shipping_method is not UNSET:
            field_dict["ShippingMethod"] = shipping_method
        if location is not UNSET:
            field_dict["Location"] = location
        if site_access_notes is not UNSET:
            field_dict["SiteAccessNotes"] = site_access_notes
        if abbreviated_uom is not UNSET:
            field_dict["AbbreviatedUOM"] = abbreviated_uom
        if unit_scale_factor is not UNSET:
            field_dict["UnitScaleFactor"] = unit_scale_factor
        if measurement_not_taken_result is not UNSET:
            field_dict["MeasurementNotTakenResult"] = measurement_not_taken_result
        if hide_from_certificate is not UNSET:
            field_dict["HideFromCertificate"] = hide_from_certificate
        if measurement_not_taken_reason is not UNSET:
            field_dict["MeasurementNotTakenReason"] = measurement_not_taken_reason
        if environment_text_1 is not UNSET:
            field_dict["EnvironmentText1"] = environment_text_1
        if environment_text_2 is not UNSET:
            field_dict["EnvironmentText2"] = environment_text_2
        if environment_text_3 is not UNSET:
            field_dict["EnvironmentText3"] = environment_text_3
        if environment_text_4 is not UNSET:
            field_dict["EnvironmentText4"] = environment_text_4
        if environment_text_5 is not UNSET:
            field_dict["EnvironmentText5"] = environment_text_5
        if environment_text_6 is not UNSET:
            field_dict["EnvironmentText6"] = environment_text_6
        if values is not UNSET:
            field_dict["Values"] = values
        if value_1 is not UNSET:
            field_dict["Value1"] = value_1
        if value_2 is not UNSET:
            field_dict["Value2"] = value_2
        if value_3 is not UNSET:
            field_dict["Value3"] = value_3
        if value_4 is not UNSET:
            field_dict["Value4"] = value_4
        if value_5 is not UNSET:
            field_dict["Value5"] = value_5
        if value_6 is not UNSET:
            field_dict["Value6"] = value_6
        if value_7 is not UNSET:
            field_dict["Value7"] = value_7
        if value_8 is not UNSET:
            field_dict["Value8"] = value_8
        if value_9 is not UNSET:
            field_dict["Value9"] = value_9
        if value_10 is not UNSET:
            field_dict["Value10"] = value_10
        if value_11 is not UNSET:
            field_dict["Value11"] = value_11
        if value_12 is not UNSET:
            field_dict["Value12"] = value_12
        if value_13 is not UNSET:
            field_dict["Value13"] = value_13
        if value_14 is not UNSET:
            field_dict["Value14"] = value_14
        if value_15 is not UNSET:
            field_dict["Value15"] = value_15
        if value_16 is not UNSET:
            field_dict["Value16"] = value_16
        if value_17 is not UNSET:
            field_dict["Value17"] = value_17
        if value_18 is not UNSET:
            field_dict["Value18"] = value_18
        if value_19 is not UNSET:
            field_dict["Value19"] = value_19
        if value_20 is not UNSET:
            field_dict["Value20"] = value_20
        if value_21 is not UNSET:
            field_dict["Value21"] = value_21
        if value_22 is not UNSET:
            field_dict["Value22"] = value_22
        if value_23 is not UNSET:
            field_dict["Value23"] = value_23
        if value_24 is not UNSET:
            field_dict["Value24"] = value_24
        if value_25 is not UNSET:
            field_dict["Value25"] = value_25
        if value_26 is not UNSET:
            field_dict["Value26"] = value_26
        if value_27 is not UNSET:
            field_dict["Value27"] = value_27
        if value_28 is not UNSET:
            field_dict["Value28"] = value_28
        if value_29 is not UNSET:
            field_dict["Value29"] = value_29
        if value_30 is not UNSET:
            field_dict["Value30"] = value_30
        if value_31 is not UNSET:
            field_dict["Value31"] = value_31
        if value_32 is not UNSET:
            field_dict["Value32"] = value_32
        if value_33 is not UNSET:
            field_dict["Value33"] = value_33
        if value_34 is not UNSET:
            field_dict["Value34"] = value_34
        if value_35 is not UNSET:
            field_dict["Value35"] = value_35
        if value_36 is not UNSET:
            field_dict["Value36"] = value_36
        if value_37 is not UNSET:
            field_dict["Value37"] = value_37
        if value_38 is not UNSET:
            field_dict["Value38"] = value_38
        if value_39 is not UNSET:
            field_dict["Value39"] = value_39
        if value_40 is not UNSET:
            field_dict["Value40"] = value_40
        if raw_value_1 is not UNSET:
            field_dict["RawValue1"] = raw_value_1
        if raw_value_2 is not UNSET:
            field_dict["RawValue2"] = raw_value_2
        if raw_value_3 is not UNSET:
            field_dict["RawValue3"] = raw_value_3
        if raw_value_4 is not UNSET:
            field_dict["RawValue4"] = raw_value_4
        if raw_value_5 is not UNSET:
            field_dict["RawValue5"] = raw_value_5
        if raw_value_6 is not UNSET:
            field_dict["RawValue6"] = raw_value_6
        if raw_value_7 is not UNSET:
            field_dict["RawValue7"] = raw_value_7
        if raw_value_8 is not UNSET:
            field_dict["RawValue8"] = raw_value_8
        if raw_value_9 is not UNSET:
            field_dict["RawValue9"] = raw_value_9
        if raw_value_10 is not UNSET:
            field_dict["RawValue10"] = raw_value_10
        if raw_value_11 is not UNSET:
            field_dict["RawValue11"] = raw_value_11
        if raw_value_12 is not UNSET:
            field_dict["RawValue12"] = raw_value_12
        if raw_value_13 is not UNSET:
            field_dict["RawValue13"] = raw_value_13
        if raw_value_14 is not UNSET:
            field_dict["RawValue14"] = raw_value_14
        if raw_value_15 is not UNSET:
            field_dict["RawValue15"] = raw_value_15
        if raw_value_16 is not UNSET:
            field_dict["RawValue16"] = raw_value_16
        if raw_value_17 is not UNSET:
            field_dict["RawValue17"] = raw_value_17
        if raw_value_18 is not UNSET:
            field_dict["RawValue18"] = raw_value_18
        if raw_value_19 is not UNSET:
            field_dict["RawValue19"] = raw_value_19
        if raw_value_20 is not UNSET:
            field_dict["RawValue20"] = raw_value_20
        if raw_value_21 is not UNSET:
            field_dict["RawValue21"] = raw_value_21
        if raw_value_22 is not UNSET:
            field_dict["RawValue22"] = raw_value_22
        if raw_value_23 is not UNSET:
            field_dict["RawValue23"] = raw_value_23
        if raw_value_24 is not UNSET:
            field_dict["RawValue24"] = raw_value_24
        if raw_value_25 is not UNSET:
            field_dict["RawValue25"] = raw_value_25
        if raw_value_26 is not UNSET:
            field_dict["RawValue26"] = raw_value_26
        if raw_value_27 is not UNSET:
            field_dict["RawValue27"] = raw_value_27
        if raw_value_28 is not UNSET:
            field_dict["RawValue28"] = raw_value_28
        if raw_value_29 is not UNSET:
            field_dict["RawValue29"] = raw_value_29
        if raw_value_30 is not UNSET:
            field_dict["RawValue30"] = raw_value_30
        if raw_value_31 is not UNSET:
            field_dict["RawValue31"] = raw_value_31
        if raw_value_32 is not UNSET:
            field_dict["RawValue32"] = raw_value_32
        if raw_value_33 is not UNSET:
            field_dict["RawValue33"] = raw_value_33
        if raw_value_34 is not UNSET:
            field_dict["RawValue34"] = raw_value_34
        if raw_value_35 is not UNSET:
            field_dict["RawValue35"] = raw_value_35
        if raw_value_36 is not UNSET:
            field_dict["RawValue36"] = raw_value_36
        if raw_value_37 is not UNSET:
            field_dict["RawValue37"] = raw_value_37
        if raw_value_38 is not UNSET:
            field_dict["RawValue38"] = raw_value_38
        if raw_value_39 is not UNSET:
            field_dict["RawValue39"] = raw_value_39
        if raw_value_40 is not UNSET:
            field_dict["RawValue40"] = raw_value_40
        if subtitles_to_readings is not UNSET:
            field_dict["SubtitlesToReadings"] = subtitles_to_readings
        if value_subtitle_1 is not UNSET:
            field_dict["ValueSubtitle1"] = value_subtitle_1
        if value_subtitle_2 is not UNSET:
            field_dict["ValueSubtitle2"] = value_subtitle_2
        if value_subtitle_3 is not UNSET:
            field_dict["ValueSubtitle3"] = value_subtitle_3
        if value_subtitle_4 is not UNSET:
            field_dict["ValueSubtitle4"] = value_subtitle_4
        if value_subtitle_5 is not UNSET:
            field_dict["ValueSubtitle5"] = value_subtitle_5
        if value_subtitle_6 is not UNSET:
            field_dict["ValueSubtitle6"] = value_subtitle_6
        if value_subtitle_7 is not UNSET:
            field_dict["ValueSubtitle7"] = value_subtitle_7
        if value_subtitle_8 is not UNSET:
            field_dict["ValueSubtitle8"] = value_subtitle_8
        if value_subtitle_9 is not UNSET:
            field_dict["ValueSubtitle9"] = value_subtitle_9
        if value_subtitle_10 is not UNSET:
            field_dict["ValueSubtitle10"] = value_subtitle_10
        if value_subtitle_11 is not UNSET:
            field_dict["ValueSubtitle11"] = value_subtitle_11
        if value_subtitle_12 is not UNSET:
            field_dict["ValueSubtitle12"] = value_subtitle_12
        if value_subtitle_13 is not UNSET:
            field_dict["ValueSubtitle13"] = value_subtitle_13
        if value_subtitle_14 is not UNSET:
            field_dict["ValueSubtitle14"] = value_subtitle_14
        if value_subtitle_15 is not UNSET:
            field_dict["ValueSubtitle15"] = value_subtitle_15
        if value_subtitle_16 is not UNSET:
            field_dict["ValueSubtitle16"] = value_subtitle_16
        if value_subtitle_17 is not UNSET:
            field_dict["ValueSubtitle17"] = value_subtitle_17
        if value_subtitle_18 is not UNSET:
            field_dict["ValueSubtitle18"] = value_subtitle_18
        if value_subtitle_19 is not UNSET:
            field_dict["ValueSubtitle19"] = value_subtitle_19
        if value_subtitle_20 is not UNSET:
            field_dict["ValueSubtitle20"] = value_subtitle_20
        if value_subtitle_21 is not UNSET:
            field_dict["ValueSubtitle21"] = value_subtitle_21
        if value_subtitle_22 is not UNSET:
            field_dict["ValueSubtitle22"] = value_subtitle_22
        if value_subtitle_23 is not UNSET:
            field_dict["ValueSubtitle23"] = value_subtitle_23
        if value_subtitle_24 is not UNSET:
            field_dict["ValueSubtitle24"] = value_subtitle_24
        if value_subtitle_25 is not UNSET:
            field_dict["ValueSubtitle25"] = value_subtitle_25
        if value_subtitle_26 is not UNSET:
            field_dict["ValueSubtitle26"] = value_subtitle_26
        if value_subtitle_27 is not UNSET:
            field_dict["ValueSubtitle27"] = value_subtitle_27
        if value_subtitle_28 is not UNSET:
            field_dict["ValueSubtitle28"] = value_subtitle_28
        if value_subtitle_29 is not UNSET:
            field_dict["ValueSubtitle29"] = value_subtitle_29
        if value_subtitle_30 is not UNSET:
            field_dict["ValueSubtitle30"] = value_subtitle_30
        if value_subtitle_31 is not UNSET:
            field_dict["ValueSubtitle31"] = value_subtitle_31
        if value_subtitle_32 is not UNSET:
            field_dict["ValueSubtitle32"] = value_subtitle_32
        if value_subtitle_33 is not UNSET:
            field_dict["ValueSubtitle33"] = value_subtitle_33
        if value_subtitle_34 is not UNSET:
            field_dict["ValueSubtitle34"] = value_subtitle_34
        if value_subtitle_35 is not UNSET:
            field_dict["ValueSubtitle35"] = value_subtitle_35
        if value_subtitle_36 is not UNSET:
            field_dict["ValueSubtitle36"] = value_subtitle_36
        if value_subtitle_37 is not UNSET:
            field_dict["ValueSubtitle37"] = value_subtitle_37
        if value_subtitle_38 is not UNSET:
            field_dict["ValueSubtitle38"] = value_subtitle_38
        if value_subtitle_39 is not UNSET:
            field_dict["ValueSubtitle39"] = value_subtitle_39
        if value_subtitle_40 is not UNSET:
            field_dict["ValueSubtitle40"] = value_subtitle_40
        if values_decimal_places is not UNSET:
            field_dict["ValuesDecimalPlaces"] = values_decimal_places
        if repeat_measurement_and_calculate_hysteresis is not UNSET:
            field_dict["RepeatMeasurementAndCalculateHysteresis"] = (
                repeat_measurement_and_calculate_hysteresis
            )
        if measurement_point_order is not UNSET:
            field_dict["MeasurementPointOrder"] = measurement_point_order
        if hysteresis_point is not UNSET:
            field_dict["HysteresisPoint"] = hysteresis_point
        if max_hysteresis is not UNSET:
            field_dict["MaxHysteresis"] = max_hysteresis
        if run is not UNSET:
            field_dict["Run"] = run
        if direction is not UNSET:
            field_dict["Direction"] = direction
        if hysteresis is not UNSET:
            field_dict["Hysteresis"] = hysteresis
        if column_mean is not UNSET:
            field_dict["ColumnMean"] = column_mean
        if column_mean_result is not UNSET:
            field_dict["ColumnMeanResult"] = column_mean_result
        if column_sd is not UNSET:
            field_dict["ColumnSD"] = column_sd
        if column_sd_result is not UNSET:
            field_dict["ColumnSDResult"] = column_sd_result
        if column_cv is not UNSET:
            field_dict["ColumnCV"] = column_cv
        if column_cv_result is not UNSET:
            field_dict["ColumnCVResult"] = column_cv_result
        if column_range is not UNSET:
            field_dict["ColumnRange"] = column_range
        if column_range_result is not UNSET:
            field_dict["ColumnRangeResult"] = column_range_result
        if column_delta is not UNSET:
            field_dict["ColumnDelta"] = column_delta
        if column_delta_result is not UNSET:
            field_dict["ColumnDeltaResult"] = column_delta_result
        if column_result is not UNSET:
            field_dict["ColumnResult"] = column_result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_accredited = d.pop("IsAccredited", UNSET)

        service_total = d.pop("ServiceTotal", UNSET)

        repairs_total = d.pop("RepairsTotal", UNSET)

        parts_total = d.pop("PartsTotal", UNSET)

        parameter_id = d.pop("ParameterId", UNSET)

        tool_range_name = d.pop("ToolRangeName", UNSET)

        tool_range_uncertainty = d.pop("ToolRangeUncertainty", UNSET)

        def _parse_primary_tool_last_service_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                primary_tool_last_service_date_type_0 = isoparse(data)

                return primary_tool_last_service_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        primary_tool_last_service_date = _parse_primary_tool_last_service_date(
            d.pop("PrimaryToolLastServiceDate", UNSET)
        )

        def _parse_primary_tool_next_service_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                primary_tool_next_service_date_type_0 = isoparse(data)

                return primary_tool_next_service_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        primary_tool_next_service_date = _parse_primary_tool_next_service_date(
            d.pop("PrimaryToolNextServiceDate", UNSET)
        )

        primary_tool_calibrated_by = d.pop("PrimaryToolCalibratedBy", UNSET)

        primary_tool_tool_name = d.pop("PrimaryToolToolName", UNSET)

        primary_tool_tool_description = d.pop("PrimaryToolToolDescription", UNSET)

        primary_tool_tool_type_name = d.pop("PrimaryToolToolTypeName", UNSET)

        primary_tool_manufacturer = d.pop("PrimaryToolManufacturer", UNSET)

        primary_tool_manufacturer_part_number = d.pop(
            "PrimaryToolManufacturerPartNumber", UNSET
        )

        primary_tool_serial_number = d.pop("PrimaryToolSerialNumber", UNSET)

        def _parse_secondary_tool_last_service_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                secondary_tool_last_service_date_type_0 = isoparse(data)

                return secondary_tool_last_service_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        secondary_tool_last_service_date = _parse_secondary_tool_last_service_date(
            d.pop("SecondaryToolLastServiceDate", UNSET)
        )

        def _parse_secondary_tool_next_service_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                secondary_tool_next_service_date_type_0 = isoparse(data)

                return secondary_tool_next_service_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        secondary_tool_next_service_date = _parse_secondary_tool_next_service_date(
            d.pop("SecondaryToolNextServiceDate", UNSET)
        )

        secondary_tool_calibrated_by = d.pop("SecondaryToolCalibratedBy", UNSET)

        secondary_tool_tool_name = d.pop("SecondaryToolToolName", UNSET)

        secondary_tool_tool_description = d.pop("SecondaryToolToolDescription", UNSET)

        secondary_tool_tool_type_name = d.pop("SecondaryToolToolTypeName", UNSET)

        secondary_tool_manufacturer = d.pop("SecondaryToolManufacturer", UNSET)

        secondary_tool_manufacturer_part_number = d.pop(
            "SecondaryToolManufacturerPartNumber", UNSET
        )

        secondary_tool_serial_number = d.pop("SecondaryToolSerialNumber", UNSET)

        measurement_set_name = d.pop("MeasurementSetName", UNSET)

        decimal_places = d.pop("DecimalPlaces", UNSET)

        significant_figures = d.pop("SignificantFigures", UNSET)

        sd_header = d.pop("SdHeader", UNSET)

        cv_header = d.pop("CvHeader", UNSET)

        _measurement_local_time = d.pop("MeasurementLocalTime", UNSET)
        measurement_local_time: Union[None, Unset, datetime.datetime]
        if isinstance(_measurement_local_time, Unset):
            measurement_local_time = UNSET
        else:
            measurement_local_time = isoparse(_measurement_local_time)

        mean = d.pop("Mean", UNSET)

        mean_raw = d.pop("MeanRaw", UNSET)

        mean_decimal_places = d.pop("MeanDecimalPlaces", UNSET)

        mean_extended = d.pop("MeanExtended", UNSET)

        sd = d.pop("Sd", UNSET)

        sd_raw = d.pop("SdRaw", UNSET)

        sd_decimal_places = d.pop("SDDecimalPlaces", UNSET)

        delta = d.pop("Delta", UNSET)

        range_ = d.pop("Range", UNSET)

        sd_extended = d.pop("SdExtended", UNSET)

        range_extended = d.pop("RangeExtended", UNSET)

        delta_extended = d.pop("DeltaExtended", UNSET)

        minimum_measured_value = d.pop("MinimumMeasuredValue", UNSET)

        maximum_measured_value = d.pop("MaximumMeasuredValue", UNSET)

        min_max_value_extended = d.pop("MinMaxValueExtended", UNSET)

        cv = d.pop("Cv", UNSET)

        cv_raw = d.pop("CvRaw", UNSET)

        cv_decimal_places = d.pop("CVDecimalPlaces", UNSET)

        cv_extended = d.pop("CvExtended", UNSET)

        result = d.pop("Result", UNSET)

        range_result = d.pop("RangeResult", UNSET)

        delta_result = d.pop("DeltaResult", UNSET)

        min_result = d.pop("MinResult", UNSET)

        max_result = d.pop("MaxResult", UNSET)

        tar_result = d.pop("TarResult", UNSET)

        tur_result = d.pop("TurResult", UNSET)

        error_result = d.pop("ErrorResult", UNSET)

        sd_result = d.pop("SdResult", UNSET)

        cv_result = d.pop("CvResult", UNSET)

        custom_field_result = d.pop("CustomFieldResult", UNSET)

        mu = d.pop("Mu", UNSET)

        mu_raw = d.pop("MuRaw", UNSET)

        mu_effective_dof = d.pop("MUEffectiveDOF", UNSET)

        mu_coverage_factor = d.pop("MUCoverageFactor", UNSET)

        mu_extended = d.pop("MuExtended", UNSET)

        cmc = d.pop("Cmc", UNSET)

        cmc_comments = d.pop("CmcComments", UNSET)

        tur = d.pop("Tur", UNSET)

        tur_raw = d.pop("TurRaw", UNSET)

        tur_decimal_places = d.pop("TURDecimalPlaces", UNSET)

        tar = d.pop("Tar", UNSET)

        tar_raw = d.pop("TarRaw", UNSET)

        tar_decimal_places = d.pop("TARDecimalPlaces", UNSET)

        guard_band = d.pop("GuardBand", UNSET)

        _guard_band_logic = d.pop("GuardBandLogic", UNSET)
        guard_band_logic: Union[
            None,
            Unset,
            QualerApiModelsReportDatasetsToMeasurementResponseGuardBandLogic,
        ]
        if isinstance(_guard_band_logic, Unset):
            guard_band_logic = UNSET
        else:
            guard_band_logic = (
                QualerApiModelsReportDatasetsToMeasurementResponseGuardBandLogic(
                    _guard_band_logic
                )
            )

        uncertainty_budget = d.pop("UncertaintyBudget", UNSET)

        calculated_uncertainty = d.pop("CalculatedUncertainty", UNSET)

        lock_uncertainty_budget = d.pop("LockUncertaintyBudget", UNSET)

        lab_mu = d.pop("LabMu", UNSET)

        channel = d.pop("Channel", UNSET)

        _measurement_type = d.pop("MeasurementType", UNSET)
        measurement_type: Union[
            None,
            Unset,
            QualerApiModelsReportDatasetsToMeasurementResponseMeasurementType,
        ]
        if isinstance(_measurement_type, Unset):
            measurement_type = UNSET
        else:
            measurement_type = (
                QualerApiModelsReportDatasetsToMeasurementResponseMeasurementType(
                    _measurement_type
                )
            )

        updated_by = d.pop("UpdatedBy", UNSET)

        _updated_on = d.pop("UpdatedOn", UNSET)
        updated_on: Union[None, Unset, datetime.datetime]
        if isinstance(_updated_on, Unset):
            updated_on = UNSET
        else:
            updated_on = isoparse(_updated_on)

        error = d.pop("Error", UNSET)

        error_extended = d.pop("ErrorExtended", UNSET)

        require_adjustment = d.pop("RequireAdjustment", UNSET)

        adjustment_threshold = d.pop("AdjustmentThreshold", UNSET)

        percent_of_tolerance = d.pop("PercentOfTolerance", UNSET)

        percent_of_tolerance_extended = d.pop("PercentOfToleranceExtended", UNSET)

        tol_decimal_places = d.pop("TOLDecimalPlaces", UNSET)

        specification_title = d.pop("SpecificationTitle", UNSET)

        specification_subtitle = d.pop("SpecificationSubtitle", UNSET)

        specification_group = d.pop("SpecificationGroup", UNSET)

        batch_type = d.pop("BatchType", UNSET)

        batch_result = d.pop("BatchResult", UNSET)

        is_by_channel = d.pop("IsByChannel", UNSET)

        channel_count = d.pop("ChannelCount", UNSET)

        is_range_accredited = d.pop("IsRangeAccredited", UNSET)

        _commenced_on = d.pop("CommencedOn", UNSET)
        commenced_on: Union[None, Unset, datetime.datetime]
        if isinstance(_commenced_on, Unset):
            commenced_on = UNSET
        else:
            commenced_on = isoparse(_commenced_on)

        commenced_by = d.pop("CommencedBy", UNSET)

        z_factor = d.pop("ZFactor", UNSET)

        air_buoyancy = d.pop("AirBuoyancy", UNSET)

        evaporation_rate = d.pop("EvaporationRate", UNSET)

        air_humidity = d.pop("AirHumidity", UNSET)

        altitude = d.pop("Altitude", UNSET)

        ambient_temperature = d.pop("AmbientTemperature", UNSET)

        barometric_pressure = d.pop("BarometricPressure", UNSET)

        light_intensity = d.pop("LightIntensity", UNSET)

        noise_level = d.pop("NoiseLevel", UNSET)

        ph_level = d.pop("PhLevel", UNSET)

        water_conductivity = d.pop("WaterConductivity", UNSET)

        water_temperature = d.pop("WaterTemperature", UNSET)

        solar_radiation = d.pop("SolarRadiation", UNSET)

        wind_speed = d.pop("WindSpeed", UNSET)

        z_factor_uom = d.pop("ZFactorUom", UNSET)

        air_buoyancy_uom = d.pop("AirBuoyancyUom", UNSET)

        evaporation_rate_uom = d.pop("EvaporationRateUom", UNSET)

        air_humidity_uom = d.pop("AirHumidityUom", UNSET)

        altitude_uom = d.pop("AltitudeUom", UNSET)

        ambient_temperature_uom = d.pop("AmbientTemperatureUom", UNSET)

        barometric_pressure_uom = d.pop("BarometricPressureUom", UNSET)

        light_intensity_uom = d.pop("LightIntensityUom", UNSET)

        noise_level_uom = d.pop("NoiseLevelUom", UNSET)

        ph_level_uom = d.pop("PhLevelUom", UNSET)

        water_conductivity_uom = d.pop("WaterConductivityUom", UNSET)

        water_temperature_uom = d.pop("WaterTemperatureUom", UNSET)

        solar_radiation_uom = d.pop("SolarRadiationUom", UNSET)

        wind_speed_uom = d.pop("WindSpeedUom", UNSET)

        specification_name = d.pop("SpecificationName", UNSET)

        parameter_name = d.pop("ParameterName", UNSET)

        measurement_set_display_order = d.pop("MeasurementSetDisplayOrder", UNSET)

        display_order = d.pop("DisplayOrder", UNSET)

        unit_of_measure = d.pop("UnitOfMeasure", UNSET)

        display_format = d.pop("DisplayFormat", UNSET)

        precision = d.pop("Precision", UNSET)

        minimum = d.pop("Minimum", UNSET)

        nominal = d.pop("Nominal", UNSET)

        expected_value = d.pop("ExpectedValue", UNSET)

        expected_value_raw = d.pop("ExpectedValueRaw", UNSET)

        test_value = d.pop("TestValue", UNSET)

        base_value = d.pop("BaseValue", UNSET)

        use_expected_value = d.pop("UseExpectedValue", UNSET)

        _reading_entry_logic = d.pop("ReadingEntryLogic", UNSET)
        reading_entry_logic: Union[
            None,
            Unset,
            QualerApiModelsReportDatasetsToMeasurementResponseReadingEntryLogic,
        ]
        if isinstance(_reading_entry_logic, Unset):
            reading_entry_logic = UNSET
        else:
            reading_entry_logic = (
                QualerApiModelsReportDatasetsToMeasurementResponseReadingEntryLogic(
                    _reading_entry_logic
                )
            )

        _reading_entry_math = d.pop("ReadingEntryMath", UNSET)
        reading_entry_math: Union[
            None,
            Unset,
            QualerApiModelsReportDatasetsToMeasurementResponseReadingEntryMath,
        ]
        if isinstance(_reading_entry_math, Unset):
            reading_entry_math = UNSET
        else:
            reading_entry_math = (
                QualerApiModelsReportDatasetsToMeasurementResponseReadingEntryMath(
                    _reading_entry_math
                )
            )

        _double_substitution_sequence = d.pop("DoubleSubstitutionSequence", UNSET)
        double_substitution_sequence: Union[
            None,
            Unset,
            QualerApiModelsReportDatasetsToMeasurementResponseDoubleSubstitutionSequence,
        ]
        if isinstance(_double_substitution_sequence, Unset):
            double_substitution_sequence = UNSET
        else:
            double_substitution_sequence = QualerApiModelsReportDatasetsToMeasurementResponseDoubleSubstitutionSequence(
                _double_substitution_sequence
            )

        reading_entry_math_string = d.pop("ReadingEntryMathString", UNSET)

        nominal_extended = d.pop("NominalExtended", UNSET)

        expected_value_extended = d.pop("ExpectedValueExtended", UNSET)

        maximum = d.pop("Maximum", UNSET)

        tolerance_min = d.pop("ToleranceMin", UNSET)

        tolerance_max = d.pop("ToleranceMax", UNSET)

        resolution = d.pop("Resolution", UNSET)

        resolution_count = d.pop("ResolutionCount", UNSET)

        min_max_header = d.pop("MinMaxHeader", UNSET)

        accuracy_class = d.pop("AccuracyClass", UNSET)

        accuracy_class_min = d.pop("AccuracyClassMin", UNSET)

        accuracy_class_max = d.pop("AccuracyClassMax", UNSET)

        _environment_mask = d.pop("EnvironmentMask", UNSET)
        environment_mask: Union[
            None,
            Unset,
            QualerApiModelsReportDatasetsToMeasurementResponseEnvironmentMask,
        ]
        if isinstance(_environment_mask, Unset):
            environment_mask = UNSET
        else:
            environment_mask = (
                QualerApiModelsReportDatasetsToMeasurementResponseEnvironmentMask(
                    _environment_mask
                )
            )

        display_name = d.pop("DisplayName", UNSET)

        display_part_number = d.pop("DisplayPartNumber", UNSET)

        part_number = d.pop("PartNumber", UNSET)

        vendor_company_id = d.pop("VendorCompanyId", UNSET)

        service_order_number = d.pop("ServiceOrderNumber", UNSET)

        custom_order_number = d.pop("CustomOrderNumber", UNSET)

        completed_by_name = d.pop("CompletedByName", UNSET)

        _completed_on = d.pop("CompletedOn", UNSET)
        completed_on: Union[None, Unset, datetime.datetime]
        if isinstance(_completed_on, Unset):
            completed_on = UNSET
        else:
            completed_on = isoparse(_completed_on)

        is_limited = d.pop("IsLimited", UNSET)

        vendor_tag = d.pop("VendorTag", UNSET)

        vendor_service_notes = d.pop("VendorServiceNotes", UNSET)

        room = d.pop("Room", UNSET)

        segment_name = d.pop("SegmentName", UNSET)

        schedule_name = d.pop("ScheduleName", UNSET)

        next_segment_name = d.pop("NextSegmentName", UNSET)

        certificate_number = d.pop("CertificateNumber", UNSET)

        _work_status = d.pop("WorkStatus", UNSET)
        work_status: Union[None, Unset, WorkStatus]
        if isinstance(_work_status, Unset):
            work_status = UNSET
        elif _work_status is None:
            work_status = None
        else:
            work_status = WorkStatus(_work_status)

        service_type = d.pop("ServiceType", UNSET)

        service_level = d.pop("ServiceLevel", UNSET)

        barcode = d.pop("Barcode", UNSET)

        service_comments = d.pop("ServiceComments", UNSET)

        order_item_number = d.pop("OrderItemNumber", UNSET)

        asset_tag = d.pop("AssetTag", UNSET)

        asset_user = d.pop("AssetUser", UNSET)

        serial_number = d.pop("SerialNumber", UNSET)

        equipment_id = d.pop("EquipmentId", UNSET)

        legacy_identifier = d.pop("LegacyIdentifier", UNSET)

        site_name = d.pop("SiteName", UNSET)

        asset_name = d.pop("AssetName", UNSET)

        asset_description = d.pop("AssetDescription", UNSET)

        product_name = d.pop("ProductName", UNSET)

        product_description = d.pop("ProductDescription", UNSET)

        asset_maker = d.pop("AssetMaker", UNSET)

        station = d.pop("Station", UNSET)

        asset_tag_change = d.pop("AssetTagChange", UNSET)

        asset_user_change = d.pop("AssetUserChange", UNSET)

        serial_number_change = d.pop("SerialNumberChange", UNSET)

        def _parse_service_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                service_date_type_0 = isoparse(data)

                return service_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        service_date = _parse_service_date(d.pop("ServiceDate", UNSET))

        def _parse_next_service_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_service_date_type_0 = isoparse(data)

                return next_service_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        next_service_date = _parse_next_service_date(d.pop("NextServiceDate", UNSET))

        service_order_item_id = d.pop("ServiceOrderItemId", UNSET)

        service_order_id = d.pop("ServiceOrderId", UNSET)

        measurement_batch_id = d.pop("MeasurementBatchId", UNSET)

        measurement_id = d.pop("MeasurementId", UNSET)

        standard_id = d.pop("StandardId", UNSET)

        tool_id = d.pop("ToolId", UNSET)

        measurement_tool_id = d.pop("MeasurementToolId", UNSET)

        measurement_condition_id = d.pop("MeasurementConditionId", UNSET)

        measurement_point_id = d.pop("MeasurementPointId", UNSET)

        measurement_set_id = d.pop("MeasurementSetId", UNSET)

        is_hidden = d.pop("IsHidden", UNSET)

        readings = d.pop("Readings", UNSET)

        _tolerance_type = d.pop("ToleranceType", UNSET)
        tolerance_type: Union[
            None, Unset, QualerApiModelsReportDatasetsToMeasurementResponseToleranceType
        ]
        if isinstance(_tolerance_type, Unset):
            tolerance_type = UNSET
        else:
            tolerance_type = (
                QualerApiModelsReportDatasetsToMeasurementResponseToleranceType(
                    _tolerance_type
                )
            )

        tolerance_type_string = d.pop("ToleranceTypeString", UNSET)

        _precision_type = d.pop("PrecisionType", UNSET)
        precision_type: Union[
            None, Unset, QualerApiModelsReportDatasetsToMeasurementResponsePrecisionType
        ]
        if isinstance(_precision_type, Unset):
            precision_type = UNSET
        else:
            precision_type = (
                QualerApiModelsReportDatasetsToMeasurementResponsePrecisionType(
                    _precision_type
                )
            )

        _specification_mode = d.pop("SpecificationMode", UNSET)
        specification_mode: Union[
            None,
            Unset,
            QualerApiModelsReportDatasetsToMeasurementResponseSpecificationMode,
        ]
        if isinstance(_specification_mode, Unset):
            specification_mode = UNSET
        else:
            specification_mode = (
                QualerApiModelsReportDatasetsToMeasurementResponseSpecificationMode(
                    _specification_mode
                )
            )

        _tolerance_mode = d.pop("ToleranceMode", UNSET)
        tolerance_mode: Union[
            None, Unset, QualerApiModelsReportDatasetsToMeasurementResponseToleranceMode
        ]
        if isinstance(_tolerance_mode, Unset):
            tolerance_mode = UNSET
        else:
            tolerance_mode = (
                QualerApiModelsReportDatasetsToMeasurementResponseToleranceMode(
                    _tolerance_mode
                )
            )

        _tolerance_unit = d.pop("ToleranceUnit", UNSET)
        tolerance_unit: Union[
            None, Unset, QualerApiModelsReportDatasetsToMeasurementResponseToleranceUnit
        ]
        if isinstance(_tolerance_unit, Unset):
            tolerance_unit = UNSET
        else:
            tolerance_unit = (
                QualerApiModelsReportDatasetsToMeasurementResponseToleranceUnit(
                    _tolerance_unit
                )
            )

        tolerance_string = d.pop("ToleranceString", UNSET)

        po_number = d.pop("PoNumber", UNSET)

        secondary_po = d.pop("SecondaryPo", UNSET)

        def _parse_shipped_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shipped_date_type_0 = isoparse(data)

                return shipped_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        shipped_date = _parse_shipped_date(d.pop("ShippedDate", UNSET))

        _shipment_status = d.pop("ShipmentStatus", UNSET)
        shipment_status: Union[
            None,
            Unset,
            QualerApiModelsReportDatasetsToMeasurementResponseShipmentStatus,
        ]
        if isinstance(_shipment_status, Unset):
            shipment_status = UNSET
        else:
            shipment_status = (
                QualerApiModelsReportDatasetsToMeasurementResponseShipmentStatus(
                    _shipment_status
                )
            )

        _shipped_on = d.pop("ShippedOn", UNSET)
        shipped_on: Union[None, Unset, datetime.datetime]
        if isinstance(_shipped_on, Unset):
            shipped_on = UNSET
        else:
            shipped_on = isoparse(_shipped_on)

        _delivered_on = d.pop("DeliveredOn", UNSET)
        delivered_on: Union[None, Unset, datetime.datetime]
        if isinstance(_delivered_on, Unset):
            delivered_on = UNSET
        else:
            delivered_on = isoparse(_delivered_on)

        tracking_number = d.pop("TrackingNumber", UNSET)

        payment_terms = d.pop("PaymentTerms", UNSET)

        shipping_method = d.pop("ShippingMethod", UNSET)

        location = d.pop("Location", UNSET)

        site_access_notes = d.pop("SiteAccessNotes", UNSET)

        abbreviated_uom = d.pop("AbbreviatedUOM", UNSET)

        unit_scale_factor = d.pop("UnitScaleFactor", UNSET)

        _measurement_not_taken_result = d.pop("MeasurementNotTakenResult", UNSET)
        measurement_not_taken_result: Union[
            None,
            Unset,
            QualerApiModelsReportDatasetsToMeasurementResponseMeasurementNotTakenResult,
        ]
        if isinstance(_measurement_not_taken_result, Unset):
            measurement_not_taken_result = UNSET
        else:
            measurement_not_taken_result = QualerApiModelsReportDatasetsToMeasurementResponseMeasurementNotTakenResult(
                _measurement_not_taken_result
            )

        hide_from_certificate = d.pop("HideFromCertificate", UNSET)

        measurement_not_taken_reason = d.pop("MeasurementNotTakenReason", UNSET)

        environment_text_1 = d.pop("EnvironmentText1", UNSET)

        environment_text_2 = d.pop("EnvironmentText2", UNSET)

        environment_text_3 = d.pop("EnvironmentText3", UNSET)

        environment_text_4 = d.pop("EnvironmentText4", UNSET)

        environment_text_5 = d.pop("EnvironmentText5", UNSET)

        environment_text_6 = d.pop("EnvironmentText6", UNSET)

        values = d.pop("Values", UNSET)

        value_1 = d.pop("Value1", UNSET)

        value_2 = d.pop("Value2", UNSET)

        value_3 = d.pop("Value3", UNSET)

        value_4 = d.pop("Value4", UNSET)

        value_5 = d.pop("Value5", UNSET)

        value_6 = d.pop("Value6", UNSET)

        value_7 = d.pop("Value7", UNSET)

        value_8 = d.pop("Value8", UNSET)

        value_9 = d.pop("Value9", UNSET)

        value_10 = d.pop("Value10", UNSET)

        value_11 = d.pop("Value11", UNSET)

        value_12 = d.pop("Value12", UNSET)

        value_13 = d.pop("Value13", UNSET)

        value_14 = d.pop("Value14", UNSET)

        value_15 = d.pop("Value15", UNSET)

        value_16 = d.pop("Value16", UNSET)

        value_17 = d.pop("Value17", UNSET)

        value_18 = d.pop("Value18", UNSET)

        value_19 = d.pop("Value19", UNSET)

        value_20 = d.pop("Value20", UNSET)

        value_21 = d.pop("Value21", UNSET)

        value_22 = d.pop("Value22", UNSET)

        value_23 = d.pop("Value23", UNSET)

        value_24 = d.pop("Value24", UNSET)

        value_25 = d.pop("Value25", UNSET)

        value_26 = d.pop("Value26", UNSET)

        value_27 = d.pop("Value27", UNSET)

        value_28 = d.pop("Value28", UNSET)

        value_29 = d.pop("Value29", UNSET)

        value_30 = d.pop("Value30", UNSET)

        value_31 = d.pop("Value31", UNSET)

        value_32 = d.pop("Value32", UNSET)

        value_33 = d.pop("Value33", UNSET)

        value_34 = d.pop("Value34", UNSET)

        value_35 = d.pop("Value35", UNSET)

        value_36 = d.pop("Value36", UNSET)

        value_37 = d.pop("Value37", UNSET)

        value_38 = d.pop("Value38", UNSET)

        value_39 = d.pop("Value39", UNSET)

        value_40 = d.pop("Value40", UNSET)

        raw_value_1 = d.pop("RawValue1", UNSET)

        raw_value_2 = d.pop("RawValue2", UNSET)

        raw_value_3 = d.pop("RawValue3", UNSET)

        raw_value_4 = d.pop("RawValue4", UNSET)

        raw_value_5 = d.pop("RawValue5", UNSET)

        raw_value_6 = d.pop("RawValue6", UNSET)

        raw_value_7 = d.pop("RawValue7", UNSET)

        raw_value_8 = d.pop("RawValue8", UNSET)

        raw_value_9 = d.pop("RawValue9", UNSET)

        raw_value_10 = d.pop("RawValue10", UNSET)

        raw_value_11 = d.pop("RawValue11", UNSET)

        raw_value_12 = d.pop("RawValue12", UNSET)

        raw_value_13 = d.pop("RawValue13", UNSET)

        raw_value_14 = d.pop("RawValue14", UNSET)

        raw_value_15 = d.pop("RawValue15", UNSET)

        raw_value_16 = d.pop("RawValue16", UNSET)

        raw_value_17 = d.pop("RawValue17", UNSET)

        raw_value_18 = d.pop("RawValue18", UNSET)

        raw_value_19 = d.pop("RawValue19", UNSET)

        raw_value_20 = d.pop("RawValue20", UNSET)

        raw_value_21 = d.pop("RawValue21", UNSET)

        raw_value_22 = d.pop("RawValue22", UNSET)

        raw_value_23 = d.pop("RawValue23", UNSET)

        raw_value_24 = d.pop("RawValue24", UNSET)

        raw_value_25 = d.pop("RawValue25", UNSET)

        raw_value_26 = d.pop("RawValue26", UNSET)

        raw_value_27 = d.pop("RawValue27", UNSET)

        raw_value_28 = d.pop("RawValue28", UNSET)

        raw_value_29 = d.pop("RawValue29", UNSET)

        raw_value_30 = d.pop("RawValue30", UNSET)

        raw_value_31 = d.pop("RawValue31", UNSET)

        raw_value_32 = d.pop("RawValue32", UNSET)

        raw_value_33 = d.pop("RawValue33", UNSET)

        raw_value_34 = d.pop("RawValue34", UNSET)

        raw_value_35 = d.pop("RawValue35", UNSET)

        raw_value_36 = d.pop("RawValue36", UNSET)

        raw_value_37 = d.pop("RawValue37", UNSET)

        raw_value_38 = d.pop("RawValue38", UNSET)

        raw_value_39 = d.pop("RawValue39", UNSET)

        raw_value_40 = d.pop("RawValue40", UNSET)

        subtitles_to_readings = d.pop("SubtitlesToReadings", UNSET)

        value_subtitle_1 = d.pop("ValueSubtitle1", UNSET)

        value_subtitle_2 = d.pop("ValueSubtitle2", UNSET)

        value_subtitle_3 = d.pop("ValueSubtitle3", UNSET)

        value_subtitle_4 = d.pop("ValueSubtitle4", UNSET)

        value_subtitle_5 = d.pop("ValueSubtitle5", UNSET)

        value_subtitle_6 = d.pop("ValueSubtitle6", UNSET)

        value_subtitle_7 = d.pop("ValueSubtitle7", UNSET)

        value_subtitle_8 = d.pop("ValueSubtitle8", UNSET)

        value_subtitle_9 = d.pop("ValueSubtitle9", UNSET)

        value_subtitle_10 = d.pop("ValueSubtitle10", UNSET)

        value_subtitle_11 = d.pop("ValueSubtitle11", UNSET)

        value_subtitle_12 = d.pop("ValueSubtitle12", UNSET)

        value_subtitle_13 = d.pop("ValueSubtitle13", UNSET)

        value_subtitle_14 = d.pop("ValueSubtitle14", UNSET)

        value_subtitle_15 = d.pop("ValueSubtitle15", UNSET)

        value_subtitle_16 = d.pop("ValueSubtitle16", UNSET)

        value_subtitle_17 = d.pop("ValueSubtitle17", UNSET)

        value_subtitle_18 = d.pop("ValueSubtitle18", UNSET)

        value_subtitle_19 = d.pop("ValueSubtitle19", UNSET)

        value_subtitle_20 = d.pop("ValueSubtitle20", UNSET)

        value_subtitle_21 = d.pop("ValueSubtitle21", UNSET)

        value_subtitle_22 = d.pop("ValueSubtitle22", UNSET)

        value_subtitle_23 = d.pop("ValueSubtitle23", UNSET)

        value_subtitle_24 = d.pop("ValueSubtitle24", UNSET)

        value_subtitle_25 = d.pop("ValueSubtitle25", UNSET)

        value_subtitle_26 = d.pop("ValueSubtitle26", UNSET)

        value_subtitle_27 = d.pop("ValueSubtitle27", UNSET)

        value_subtitle_28 = d.pop("ValueSubtitle28", UNSET)

        value_subtitle_29 = d.pop("ValueSubtitle29", UNSET)

        value_subtitle_30 = d.pop("ValueSubtitle30", UNSET)

        value_subtitle_31 = d.pop("ValueSubtitle31", UNSET)

        value_subtitle_32 = d.pop("ValueSubtitle32", UNSET)

        value_subtitle_33 = d.pop("ValueSubtitle33", UNSET)

        value_subtitle_34 = d.pop("ValueSubtitle34", UNSET)

        value_subtitle_35 = d.pop("ValueSubtitle35", UNSET)

        value_subtitle_36 = d.pop("ValueSubtitle36", UNSET)

        value_subtitle_37 = d.pop("ValueSubtitle37", UNSET)

        value_subtitle_38 = d.pop("ValueSubtitle38", UNSET)

        value_subtitle_39 = d.pop("ValueSubtitle39", UNSET)

        value_subtitle_40 = d.pop("ValueSubtitle40", UNSET)

        values_decimal_places = d.pop("ValuesDecimalPlaces", UNSET)

        repeat_measurement_and_calculate_hysteresis = d.pop(
            "RepeatMeasurementAndCalculateHysteresis", UNSET
        )

        _measurement_point_order = d.pop("MeasurementPointOrder", UNSET)
        measurement_point_order: Union[
            None,
            Unset,
            QualerApiModelsReportDatasetsToMeasurementResponseMeasurementPointOrder,
        ]
        if isinstance(_measurement_point_order, Unset):
            measurement_point_order = UNSET
        else:
            measurement_point_order = (
                QualerApiModelsReportDatasetsToMeasurementResponseMeasurementPointOrder(
                    _measurement_point_order
                )
            )

        _hysteresis_point = d.pop("HysteresisPoint", UNSET)
        hysteresis_point: Union[
            None,
            Unset,
            QualerApiModelsReportDatasetsToMeasurementResponseHysteresisPoint,
        ]
        if isinstance(_hysteresis_point, Unset):
            hysteresis_point = UNSET
        else:
            hysteresis_point = (
                QualerApiModelsReportDatasetsToMeasurementResponseHysteresisPoint(
                    _hysteresis_point
                )
            )

        max_hysteresis = d.pop("MaxHysteresis", UNSET)

        run = d.pop("Run", UNSET)

        direction = d.pop("Direction", UNSET)

        hysteresis = d.pop("Hysteresis", UNSET)

        column_mean = d.pop("ColumnMean", UNSET)

        column_mean_result = d.pop("ColumnMeanResult", UNSET)

        column_sd = d.pop("ColumnSD", UNSET)

        column_sd_result = d.pop("ColumnSDResult", UNSET)

        column_cv = d.pop("ColumnCV", UNSET)

        column_cv_result = d.pop("ColumnCVResult", UNSET)

        column_range = d.pop("ColumnRange", UNSET)

        column_range_result = d.pop("ColumnRangeResult", UNSET)

        column_delta = d.pop("ColumnDelta", UNSET)

        column_delta_result = d.pop("ColumnDeltaResult", UNSET)

        column_result = d.pop("ColumnResult", UNSET)

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

        qualer_api_models_report_datasets_to_measurement_response.additional_properties = (
            d
        )
        return qualer_api_models_report_datasets_to_measurement_response

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
