import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.qualer_api_models_report_datasets_to_measurement_all_response_as_found_guard_band_logic import (
    QualerApiModelsReportDatasetsToMeasurementAllResponseAsFoundGuardBandLogic,
)
from ..models.qualer_api_models_report_datasets_to_measurement_all_response_as_found_measurement_not_taken_result import (
    QualerApiModelsReportDatasetsToMeasurementAllResponseAsFoundMeasurementNotTakenResult,
)
from ..models.qualer_api_models_report_datasets_to_measurement_all_response_as_found_measurement_type import (
    QualerApiModelsReportDatasetsToMeasurementAllResponseAsFoundMeasurementType,
)
from ..models.qualer_api_models_report_datasets_to_measurement_all_response_as_found_precision_type import (
    QualerApiModelsReportDatasetsToMeasurementAllResponseAsFoundPrecisionType,
)
from ..models.qualer_api_models_report_datasets_to_measurement_all_response_as_found_reading_entry_math import (
    QualerApiModelsReportDatasetsToMeasurementAllResponseAsFoundReadingEntryMath,
)
from ..models.qualer_api_models_report_datasets_to_measurement_all_response_as_left_guard_band_logic import (
    QualerApiModelsReportDatasetsToMeasurementAllResponseAsLeftGuardBandLogic,
)
from ..models.qualer_api_models_report_datasets_to_measurement_all_response_as_left_measurement_not_taken_result import (
    QualerApiModelsReportDatasetsToMeasurementAllResponseAsLeftMeasurementNotTakenResult,
)
from ..models.qualer_api_models_report_datasets_to_measurement_all_response_as_left_measurement_type import (
    QualerApiModelsReportDatasetsToMeasurementAllResponseAsLeftMeasurementType,
)
from ..models.qualer_api_models_report_datasets_to_measurement_all_response_as_left_precision_type import (
    QualerApiModelsReportDatasetsToMeasurementAllResponseAsLeftPrecisionType,
)
from ..models.qualer_api_models_report_datasets_to_measurement_all_response_as_left_reading_entry_math import (
    QualerApiModelsReportDatasetsToMeasurementAllResponseAsLeftReadingEntryMath,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsReportDatasetsToMeasurementAllResponse")


@_attrs_define
class QualerApiModelsReportDatasetsToMeasurementAllResponse:
    """
    Attributes:
        barcode (Union[Unset, str]):
        display_name (Union[Unset, str]):
        display_part_number (Union[Unset, str]):
        part_number (Union[Unset, str]):
        vendor_company_id (Union[Unset, int]):
        service_order_number (Union[Unset, int]):
        completed_by_name (Union[Unset, str]):
        completed_on (Union[Unset, datetime.datetime]):
        is_limited (Union[Unset, bool]):
        vendor_tag (Union[Unset, str]):
        room (Union[Unset, str]):
        segment_name (Union[Unset, str]):
        schedule_name (Union[Unset, str]):
        next_segment_name (Union[Unset, str]):
        certificate_number (Union[Unset, str]):
        work_status (Union[Unset, int]):
        service_type (Union[Unset, str]):
        service_level (Union[Unset, str]):
        service_comments (Union[Unset, str]):
        order_item_number (Union[Unset, int]):
        service_total (Union[Unset, float]):
        repairs_total (Union[Unset, float]):
        parts_total (Union[Unset, float]):
        asset_tag (Union[Unset, str]):
        asset_user (Union[Unset, str]):
        serial_number (Union[Unset, str]):
        equipment_id (Union[Unset, str]):
        legacy_identifier (Union[Unset, str]):
        asset_name (Union[Unset, str]):
        asset_description (Union[Unset, str]):
        product_name (Union[Unset, str]):
        product_description (Union[Unset, str]):
        asset_maker (Union[Unset, str]):
        asset_tag_change (Union[Unset, str]):
        asset_user_change (Union[Unset, str]):
        serial_number_change (Union[Unset, str]):
        service_date (Union[None, Unset, datetime.datetime]):
        next_service_date (Union[None, Unset, datetime.datetime]):
        service_order_item_id (Union[Unset, int]):
        site_name (Union[Unset, str]):
        po_number (Union[Unset, str]):
        shipped_date (Union[None, Unset, datetime.datetime]):
        tracking_number (Union[Unset, str]):
        payment_terms (Union[Unset, int]):
        shipping_method (Union[Unset, str]):
        location (Union[Unset, str]):
        site_access_notes (Union[Unset, str]):
        as_left_decimal_places (Union[Unset, int]):
        as_left_measurement_set_name (Union[Unset, str]):
        as_left_measurement_set_id (Union[Unset, int]):
        as_left_adjustment_threshold (Union[Unset, float]):
        as_left_mean_extended (Union[Unset, str]):
        as_left_sd_extended (Union[Unset, str]):
        as_left_range_extended (Union[Unset, str]):
        as_left_delta_extended (Union[Unset, str]):
        as_left_cv_extended (Union[Unset, str]):
        as_left_nominal_extended (Union[Unset, str]):
        as_left_min_max_header (Union[Unset, str]):
        as_left_accuracy_class (Union[Unset, str]):
        as_left_accuracy_class_min (Union[Unset, float]):
        as_left_accuracy_class_max (Union[Unset, float]):
        as_left_minimum_measured_value (Union[Unset, float]):
        as_left_maxi_mum_measured_value (Union[Unset, float]):
        as_left_min_max_value_extended (Union[Unset, str]):
        as_left_tool_range_name (Union[Unset, str]):
        as_left_tool_range_uncertainty (Union[Unset, str]):
        as_left_primary_tool_last_service_date (Union[None, Unset, datetime.datetime]):
        as_left_primary_tool_next_service_date (Union[None, Unset, datetime.datetime]):
        as_left_primary_tool_calibrated_by (Union[Unset, str]):
        as_left_primary_tool_tool_name (Union[Unset, str]):
        as_left_primary_tool_tool_description (Union[Unset, str]):
        as_left_primary_tool_tool_type_name (Union[Unset, str]):
        as_left_primary_tool_manufacturer (Union[Unset, str]):
        as_left_primary_tool_manufacturer_part_number (Union[Unset, str]):
        as_left_primary_tool_serial_number (Union[Unset, str]):
        as_found_measurement_set_name (Union[Unset, str]):
        as_found_measurement_set_id (Union[Unset, int]):
        as_found_adjustment_threshold (Union[Unset, float]):
        as_found_decimal_places (Union[Unset, int]):
        as_found_mean_extended (Union[Unset, str]):
        as_found_sd_extended (Union[Unset, str]):
        as_found_range_extended (Union[Unset, str]):
        as_found_delta_extended (Union[Unset, str]):
        as_found_cv_extended (Union[Unset, str]):
        as_found_nominal_extended (Union[Unset, str]):
        as_found_min_max_header (Union[Unset, str]):
        as_found_accuracy_class (Union[Unset, str]):
        as_found_accuracy_class_min (Union[Unset, float]):
        as_found_accuracy_class_max (Union[Unset, float]):
        as_found_minimum_measured_value (Union[Unset, float]):
        as_found_maxi_mum_measured_value (Union[Unset, float]):
        as_found_min_max_value_extended (Union[Unset, str]):
        as_found_tool_range_name (Union[Unset, str]):
        as_found_tool_range_uncertainty (Union[Unset, str]):
        as_found_primary_tool_last_service_date (Union[None, Unset, datetime.datetime]):
        as_found_primary_tool_next_service_date (Union[None, Unset, datetime.datetime]):
        as_found_primary_tool_calibrated_by (Union[Unset, str]):
        as_found_primary_tool_tool_name (Union[Unset, str]):
        as_found_primary_tool_tool_description (Union[Unset, str]):
        as_found_primary_tool_tool_type_name (Union[Unset, str]):
        as_found_primary_tool_manufacturer (Union[Unset, str]):
        as_found_primary_tool_manufacturer_part_number (Union[Unset, str]):
        as_found_primary_tool_serial_number (Union[Unset, str]):
        as_left_secondary_tool_last_service_date (Union[None, Unset, datetime.datetime]):
        as_left_secondary_tool_next_service_date (Union[None, Unset, datetime.datetime]):
        as_left_secondary_tool_calibrated_by (Union[Unset, str]):
        as_left_secondary_tool_tool_name (Union[Unset, str]):
        as_left_secondary_tool_tool_description (Union[Unset, str]):
        as_left_secondary_tool_tool_type_name (Union[Unset, str]):
        as_left_secondary_tool_manufacturer (Union[Unset, str]):
        as_left_secondary_tool_manufacturer_part_number (Union[Unset, str]):
        as_left_secondary_tool_serial_number (Union[Unset, str]):
        as_found_secondary_tool_last_service_date (Union[None, Unset, datetime.datetime]):
        as_found_secondary_tool_next_service_date (Union[None, Unset, datetime.datetime]):
        as_found_secondary_tool_calibrated_by (Union[Unset, str]):
        as_found_secondary_tool_tool_name (Union[Unset, str]):
        as_found_secondary_tool_tool_description (Union[Unset, str]):
        as_found_secondary_tool_tool_type_name (Union[Unset, str]):
        as_found_secondary_tool_manufacturer (Union[Unset, str]):
        as_found_secondary_tool_manufacturer_part_number (Union[Unset, str]):
        as_found_secondary_tool_serial_number (Union[Unset, str]):
        as_found_measurement_not_taken_result (Union[Unset,
            QualerApiModelsReportDatasetsToMeasurementAllResponseAsFoundMeasurementNotTakenResult]):
        as_found_hide_from_certificate (Union[Unset, bool]):
        as_found_measurement_not_taken_reason (Union[Unset, str]):
        as_left_values (Union[Unset, str]):
        as_left_is_accredited (Union[Unset, bool]):
        as_left_is_range_accredited (Union[Unset, bool]):
        as_found_values (Union[Unset, str]):
        as_found_is_accredited (Union[Unset, bool]):
        as_found_is_range_accredited (Union[Unset, bool]):
        as_found_parameter_id (Union[Unset, int]):
        as_found_sd_header (Union[Unset, float]):
        as_found_cv_header (Union[Unset, float]):
        as_found_measurement_local_time (Union[None, Unset, datetime.datetime]):
        as_found_tur (Union[Unset, float]):
        as_found_tur_raw (Union[Unset, float]):
        as_left_tur (Union[Unset, float]):
        as_left_tur_raw (Union[Unset, float]):
        as_found_tar (Union[Unset, float]):
        as_found_tar_raw (Union[Unset, float]):
        as_left_tar (Union[Unset, float]):
        as_left_tar_raw (Union[Unset, float]):
        as_found_guard_band (Union[Unset, str]):
        as_left_guard_band (Union[Unset, str]):
        as_found_guard_band_logic (Union[Unset,
            QualerApiModelsReportDatasetsToMeasurementAllResponseAsFoundGuardBandLogic]):
        as_left_guard_band_logic (Union[Unset,
            QualerApiModelsReportDatasetsToMeasurementAllResponseAsLeftGuardBandLogic]):
        as_found_error (Union[Unset, float]):
        as_found_error_extended (Union[Unset, str]):
        as_left_error (Union[Unset, float]):
        as_left_error_extended (Union[Unset, str]):
        as_found_percent_of_tolerance (Union[Unset, float]):
        as_found_percent_of_tolerance_extended (Union[Unset, str]):
        as_left_percent_of_tolerance (Union[Unset, float]):
        as_left_percent_of_tolerance_extended (Union[Unset, str]):
        as_found_tolerance_maximum (Union[Unset, float]):
        as_found_tolerance_minimum (Union[Unset, float]):
        as_found_tolerance_type (Union[Unset, int]):
        as_found_tolerance_mode (Union[Unset, int]):
        as_found_tolerance_string (Union[Unset, str]):
        as_left_tolerance_maximum (Union[Unset, float]):
        as_left_tolerance_minimum (Union[Unset, float]):
        as_left_tolerance_type (Union[Unset, int]):
        as_left_tolerance_mode (Union[Unset, int]):
        as_left_tolerance_string (Union[Unset, str]):
        as_found_max_hysteresis (Union[Unset, float]):
        as_found_run (Union[Unset, int]):
        as_found_direction (Union[Unset, int]):
        as_found_hysteresis (Union[Unset, float]):
        as_left_max_hysteresis (Union[Unset, float]):
        as_left_run (Union[Unset, int]):
        as_left_direction (Union[Unset, int]):
        as_left_hysteresis (Union[Unset, float]):
        as_found_reading_entry_math (Union[Unset,
            QualerApiModelsReportDatasetsToMeasurementAllResponseAsFoundReadingEntryMath]):
        as_found_reading_entry_math_string (Union[Unset, str]):
        as_found_value_1 (Union[Unset, str]):
        as_found_value_2 (Union[Unset, str]):
        as_found_value_3 (Union[Unset, str]):
        as_found_value_4 (Union[Unset, str]):
        as_found_value_5 (Union[Unset, str]):
        as_found_value_6 (Union[Unset, str]):
        as_found_value_7 (Union[Unset, str]):
        as_found_value_8 (Union[Unset, str]):
        as_found_value_9 (Union[Unset, str]):
        as_found_value_10 (Union[Unset, str]):
        as_found_value_11 (Union[Unset, str]):
        as_found_value_12 (Union[Unset, str]):
        as_found_value_13 (Union[Unset, str]):
        as_found_value_14 (Union[Unset, str]):
        as_found_value_15 (Union[Unset, str]):
        as_found_value_16 (Union[Unset, str]):
        as_found_value_17 (Union[Unset, str]):
        as_found_value_18 (Union[Unset, str]):
        as_found_value_19 (Union[Unset, str]):
        as_found_value_20 (Union[Unset, str]):
        as_found_value_21 (Union[Unset, str]):
        as_found_value_22 (Union[Unset, str]):
        as_found_value_23 (Union[Unset, str]):
        as_found_value_24 (Union[Unset, str]):
        as_found_value_25 (Union[Unset, str]):
        as_found_value_26 (Union[Unset, str]):
        as_found_value_27 (Union[Unset, str]):
        as_found_value_28 (Union[Unset, str]):
        as_found_value_29 (Union[Unset, str]):
        as_found_value_30 (Union[Unset, str]):
        as_found_value_31 (Union[Unset, str]):
        as_found_value_32 (Union[Unset, str]):
        as_found_value_33 (Union[Unset, str]):
        as_found_value_34 (Union[Unset, str]):
        as_found_value_35 (Union[Unset, str]):
        as_found_value_36 (Union[Unset, str]):
        as_found_value_37 (Union[Unset, str]):
        as_found_value_38 (Union[Unset, str]):
        as_found_value_39 (Union[Unset, str]):
        as_found_value_40 (Union[Unset, str]):
        as_found_raw_value_1 (Union[Unset, str]):
        as_found_raw_value_2 (Union[Unset, str]):
        as_found_raw_value_3 (Union[Unset, str]):
        as_found_raw_value_4 (Union[Unset, str]):
        as_found_raw_value_5 (Union[Unset, str]):
        as_found_raw_value_6 (Union[Unset, str]):
        as_found_raw_value_7 (Union[Unset, str]):
        as_found_raw_value_8 (Union[Unset, str]):
        as_found_raw_value_9 (Union[Unset, str]):
        as_found_raw_value_10 (Union[Unset, str]):
        as_found_raw_value_11 (Union[Unset, str]):
        as_found_raw_value_12 (Union[Unset, str]):
        as_found_raw_value_13 (Union[Unset, str]):
        as_found_raw_value_14 (Union[Unset, str]):
        as_found_raw_value_15 (Union[Unset, str]):
        as_found_raw_value_16 (Union[Unset, str]):
        as_found_raw_value_17 (Union[Unset, str]):
        as_found_raw_value_18 (Union[Unset, str]):
        as_found_raw_value_19 (Union[Unset, str]):
        as_found_raw_value_20 (Union[Unset, str]):
        as_found_raw_value_21 (Union[Unset, str]):
        as_found_raw_value_22 (Union[Unset, str]):
        as_found_raw_value_23 (Union[Unset, str]):
        as_found_raw_value_24 (Union[Unset, str]):
        as_found_raw_value_25 (Union[Unset, str]):
        as_found_raw_value_26 (Union[Unset, str]):
        as_found_raw_value_27 (Union[Unset, str]):
        as_found_raw_value_28 (Union[Unset, str]):
        as_found_raw_value_29 (Union[Unset, str]):
        as_found_raw_value_30 (Union[Unset, str]):
        as_found_raw_value_31 (Union[Unset, str]):
        as_found_raw_value_32 (Union[Unset, str]):
        as_found_raw_value_33 (Union[Unset, str]):
        as_found_raw_value_34 (Union[Unset, str]):
        as_found_raw_value_35 (Union[Unset, str]):
        as_found_raw_value_36 (Union[Unset, str]):
        as_found_raw_value_37 (Union[Unset, str]):
        as_found_raw_value_38 (Union[Unset, str]):
        as_found_raw_value_39 (Union[Unset, str]):
        as_found_raw_value_40 (Union[Unset, str]):
        as_found_value_subtitle_1 (Union[Unset, str]):
        as_found_value_subtitle_2 (Union[Unset, str]):
        as_found_value_subtitle_3 (Union[Unset, str]):
        as_found_value_subtitle_4 (Union[Unset, str]):
        as_found_value_subtitle_5 (Union[Unset, str]):
        as_found_value_subtitle_6 (Union[Unset, str]):
        as_found_value_subtitle_7 (Union[Unset, str]):
        as_found_value_subtitle_8 (Union[Unset, str]):
        as_found_value_subtitle_9 (Union[Unset, str]):
        as_found_value_subtitle_10 (Union[Unset, str]):
        as_found_value_subtitle_11 (Union[Unset, str]):
        as_found_value_subtitle_12 (Union[Unset, str]):
        as_found_value_subtitle_13 (Union[Unset, str]):
        as_found_value_subtitle_14 (Union[Unset, str]):
        as_found_value_subtitle_15 (Union[Unset, str]):
        as_found_value_subtitle_16 (Union[Unset, str]):
        as_found_value_subtitle_17 (Union[Unset, str]):
        as_found_value_subtitle_18 (Union[Unset, str]):
        as_found_value_subtitle_19 (Union[Unset, str]):
        as_found_value_subtitle_20 (Union[Unset, str]):
        as_found_value_subtitle_21 (Union[Unset, str]):
        as_found_value_subtitle_22 (Union[Unset, str]):
        as_found_value_subtitle_23 (Union[Unset, str]):
        as_found_value_subtitle_24 (Union[Unset, str]):
        as_found_value_subtitle_25 (Union[Unset, str]):
        as_found_value_subtitle_26 (Union[Unset, str]):
        as_found_value_subtitle_27 (Union[Unset, str]):
        as_found_value_subtitle_28 (Union[Unset, str]):
        as_found_value_subtitle_29 (Union[Unset, str]):
        as_found_value_subtitle_30 (Union[Unset, str]):
        as_found_value_subtitle_31 (Union[Unset, str]):
        as_found_value_subtitle_32 (Union[Unset, str]):
        as_found_value_subtitle_33 (Union[Unset, str]):
        as_found_value_subtitle_34 (Union[Unset, str]):
        as_found_value_subtitle_35 (Union[Unset, str]):
        as_found_value_subtitle_36 (Union[Unset, str]):
        as_found_value_subtitle_37 (Union[Unset, str]):
        as_found_value_subtitle_38 (Union[Unset, str]):
        as_found_value_subtitle_39 (Union[Unset, str]):
        as_found_value_subtitle_40 (Union[Unset, str]):
        as_found_mean (Union[Unset, float]):
        as_found_mean_raw (Union[Unset, float]):
        as_found_sd (Union[Unset, float]):
        as_found_sd_raw (Union[Unset, float]):
        as_found_delta (Union[Unset, float]):
        as_found_range (Union[Unset, float]):
        as_found_cv (Union[Unset, float]):
        as_found_cv_raw (Union[Unset, float]):
        as_found_result (Union[Unset, int]):
        as_found_range_result (Union[Unset, bool]):
        as_found_delta_result (Union[Unset, bool]):
        as_found_min_result (Union[Unset, bool]):
        as_found_max_result (Union[Unset, bool]):
        as_found_tar_result (Union[Unset, bool]):
        as_found_tur_result (Union[Unset, bool]):
        as_found_error_result (Union[Unset, bool]):
        as_found_sd_result (Union[Unset, bool]):
        as_found_cv_result (Union[Unset, bool]):
        as_found_custom_field_result (Union[Unset, int]):
        as_found_mu (Union[Unset, float]):
        as_found_mu_raw (Union[Unset, float]):
        as_found_mu_effective_dof (Union[Unset, float]):
        as_found_mu_coverage_factor (Union[Unset, float]):
        as_found_cmc (Union[Unset, float]):
        as_found_cmc_comments (Union[Unset, str]):
        as_found_calculated_uncertainty (Union[Unset, float]):
        as_found_lab_mu (Union[Unset, float]):
        as_found_uncertainty_budget (Union[Unset, str]):
        as_found_mu_extended (Union[Unset, str]):
        as_found_channel (Union[Unset, int]):
        as_found_measurement_type (Union[Unset,
            QualerApiModelsReportDatasetsToMeasurementAllResponseAsFoundMeasurementType]):
        as_found_updated_by (Union[Unset, str]):
        as_found_updated_on (Union[None, Unset, datetime.datetime]):
        as_left_abbreviated_uom (Union[Unset, str]):
        as_left_unit_scale_factor (Union[Unset, float]):
        as_found_specification_title (Union[Unset, str]):
        as_found_specification_subtitle (Union[Unset, str]):
        as_found_specification_group (Union[Unset, str]):
        as_found_batch_type (Union[Unset, int]):
        as_found_batch_result (Union[Unset, int]):
        as_found_is_by_channel (Union[Unset, bool]):
        as_found_channel_count (Union[Unset, int]):
        as_found_commenced_on (Union[Unset, datetime.datetime]):
        as_found_commenced_by (Union[Unset, str]):
        as_found_z_factor (Union[Unset, float]):
        as_found_air_buoyancy (Union[Unset, float]):
        as_found_evaporation_rate (Union[Unset, float]):
        as_found_ambient_temperature (Union[Unset, float]):
        as_found_air_humidity (Union[Unset, float]):
        as_found_barometric_pressure (Union[Unset, float]):
        as_found_altitude (Union[Unset, float]):
        as_found_wind_speed (Union[Unset, float]):
        as_found_solar_radiation (Union[Unset, float]):
        as_found_light_intensity (Union[Unset, float]):
        as_found_noise_level (Union[Unset, float]):
        as_found_ph_level (Union[Unset, float]):
        as_found_water_conductivity (Union[Unset, float]):
        as_found_water_temperature (Union[Unset, float]):
        as_found_z_factor_uom (Union[Unset, str]):
        as_found_air_buoyancy_uom (Union[Unset, str]):
        as_found_evaporation_rate_uom (Union[Unset, str]):
        as_found_ambient_temperature_uom (Union[Unset, str]):
        as_found_air_humidity_uom (Union[Unset, str]):
        as_found_barometric_pressure_uom (Union[Unset, str]):
        as_found_altitude_uom (Union[Unset, str]):
        as_found_wind_speed_uom (Union[Unset, str]):
        as_found_solar_radiation_uom (Union[Unset, str]):
        as_found_light_intensity_uom (Union[Unset, str]):
        as_found_noise_level_uom (Union[Unset, str]):
        as_found_ph_level_uom (Union[Unset, str]):
        as_found_water_conductivity_uom (Union[Unset, str]):
        as_found_water_temperature_uom (Union[Unset, str]):
        as_found_abbreviated_uom (Union[Unset, str]):
        as_found_unit_scale_factor (Union[Unset, float]):
        as_found_specification_name (Union[Unset, str]):
        as_found_parameter_name (Union[Unset, str]):
        as_found_display_order (Union[Unset, int]):
        as_found_unit_of_measure (Union[Unset, str]):
        as_found_display_format (Union[Unset, str]):
        as_found_precision (Union[Unset, float]):
        as_found_precision_type (Union[Unset,
            QualerApiModelsReportDatasetsToMeasurementAllResponseAsFoundPrecisionType]):
        as_found_minimum (Union[Unset, float]):
        as_found_nominal (Union[Unset, float]):
        as_found_expected_value (Union[Unset, float]):
        as_found_expected_value_raw (Union[Unset, str]):
        as_found_test_value (Union[Unset, float]):
        as_found_base_value (Union[Unset, float]):
        as_found_maxi_mum (Union[Unset, float]):
        as_found_resolution (Union[Unset, float]):
        as_found_resolution_count (Union[Unset, int]):
        as_found_measurement_batch_id (Union[Unset, int]):
        as_found_measurement_id (Union[Unset, int]):
        as_found_standard_id (Union[Unset, int]):
        as_found_tool_id (Union[Unset, int]):
        as_found_measurement_condition_id (Union[Unset, int]):
        as_found_measurement_point_id (Union[Unset, int]):
        as_left_parameter_id (Union[Unset, int]):
        as_left_sd_header (Union[Unset, float]):
        as_left_cv_header (Union[Unset, float]):
        as_left_measurement_local_time (Union[None, Unset, datetime.datetime]):
        as_left_reading_entry_math (Union[Unset,
            QualerApiModelsReportDatasetsToMeasurementAllResponseAsLeftReadingEntryMath]):
        as_left_reading_entry_math_string (Union[Unset, str]):
        as_left_value_1 (Union[Unset, str]):
        as_left_value_2 (Union[Unset, str]):
        as_left_value_3 (Union[Unset, str]):
        as_left_value_4 (Union[Unset, str]):
        as_left_value_5 (Union[Unset, str]):
        as_left_value_6 (Union[Unset, str]):
        as_left_value_7 (Union[Unset, str]):
        as_left_value_8 (Union[Unset, str]):
        as_left_value_9 (Union[Unset, str]):
        as_left_value_10 (Union[Unset, str]):
        as_left_value_11 (Union[Unset, str]):
        as_left_value_12 (Union[Unset, str]):
        as_left_value_13 (Union[Unset, str]):
        as_left_value_14 (Union[Unset, str]):
        as_left_value_15 (Union[Unset, str]):
        as_left_value_16 (Union[Unset, str]):
        as_left_value_17 (Union[Unset, str]):
        as_left_value_18 (Union[Unset, str]):
        as_left_value_19 (Union[Unset, str]):
        as_left_value_20 (Union[Unset, str]):
        as_left_value_21 (Union[Unset, str]):
        as_left_value_22 (Union[Unset, str]):
        as_left_value_23 (Union[Unset, str]):
        as_left_value_24 (Union[Unset, str]):
        as_left_value_25 (Union[Unset, str]):
        as_left_value_26 (Union[Unset, str]):
        as_left_value_27 (Union[Unset, str]):
        as_left_value_28 (Union[Unset, str]):
        as_left_value_29 (Union[Unset, str]):
        as_left_value_30 (Union[Unset, str]):
        as_left_value_31 (Union[Unset, str]):
        as_left_value_32 (Union[Unset, str]):
        as_left_value_33 (Union[Unset, str]):
        as_left_value_34 (Union[Unset, str]):
        as_left_value_35 (Union[Unset, str]):
        as_left_value_36 (Union[Unset, str]):
        as_left_value_37 (Union[Unset, str]):
        as_left_value_38 (Union[Unset, str]):
        as_left_value_39 (Union[Unset, str]):
        as_left_value_40 (Union[Unset, str]):
        as_left_raw_value_1 (Union[Unset, str]):
        as_left_raw_value_2 (Union[Unset, str]):
        as_left_raw_value_3 (Union[Unset, str]):
        as_left_raw_value_4 (Union[Unset, str]):
        as_left_raw_value_5 (Union[Unset, str]):
        as_left_raw_value_6 (Union[Unset, str]):
        as_left_raw_value_7 (Union[Unset, str]):
        as_left_raw_value_8 (Union[Unset, str]):
        as_left_raw_value_9 (Union[Unset, str]):
        as_left_raw_value_10 (Union[Unset, str]):
        as_left_raw_value_11 (Union[Unset, str]):
        as_left_raw_value_12 (Union[Unset, str]):
        as_left_raw_value_13 (Union[Unset, str]):
        as_left_raw_value_14 (Union[Unset, str]):
        as_left_raw_value_15 (Union[Unset, str]):
        as_left_raw_value_16 (Union[Unset, str]):
        as_left_raw_value_17 (Union[Unset, str]):
        as_left_raw_value_18 (Union[Unset, str]):
        as_left_raw_value_19 (Union[Unset, str]):
        as_left_raw_value_20 (Union[Unset, str]):
        as_left_raw_value_21 (Union[Unset, str]):
        as_left_raw_value_22 (Union[Unset, str]):
        as_left_raw_value_23 (Union[Unset, str]):
        as_left_raw_value_24 (Union[Unset, str]):
        as_left_raw_value_25 (Union[Unset, str]):
        as_left_raw_value_26 (Union[Unset, str]):
        as_left_raw_value_27 (Union[Unset, str]):
        as_left_raw_value_28 (Union[Unset, str]):
        as_left_raw_value_29 (Union[Unset, str]):
        as_left_raw_value_30 (Union[Unset, str]):
        as_left_raw_value_31 (Union[Unset, str]):
        as_left_raw_value_32 (Union[Unset, str]):
        as_left_raw_value_33 (Union[Unset, str]):
        as_left_raw_value_34 (Union[Unset, str]):
        as_left_raw_value_35 (Union[Unset, str]):
        as_left_raw_value_36 (Union[Unset, str]):
        as_left_raw_value_37 (Union[Unset, str]):
        as_left_raw_value_38 (Union[Unset, str]):
        as_left_raw_value_39 (Union[Unset, str]):
        as_left_raw_value_40 (Union[Unset, str]):
        as_left_value_subtitle_1 (Union[Unset, str]):
        as_left_value_subtitle_2 (Union[Unset, str]):
        as_left_value_subtitle_3 (Union[Unset, str]):
        as_left_value_subtitle_4 (Union[Unset, str]):
        as_left_value_subtitle_5 (Union[Unset, str]):
        as_left_value_subtitle_6 (Union[Unset, str]):
        as_left_value_subtitle_7 (Union[Unset, str]):
        as_left_value_subtitle_8 (Union[Unset, str]):
        as_left_value_subtitle_9 (Union[Unset, str]):
        as_left_value_subtitle_10 (Union[Unset, str]):
        as_left_value_subtitle_11 (Union[Unset, str]):
        as_left_value_subtitle_12 (Union[Unset, str]):
        as_left_value_subtitle_13 (Union[Unset, str]):
        as_left_value_subtitle_14 (Union[Unset, str]):
        as_left_value_subtitle_15 (Union[Unset, str]):
        as_left_value_subtitle_16 (Union[Unset, str]):
        as_left_value_subtitle_17 (Union[Unset, str]):
        as_left_value_subtitle_18 (Union[Unset, str]):
        as_left_value_subtitle_19 (Union[Unset, str]):
        as_left_value_subtitle_20 (Union[Unset, str]):
        as_left_value_subtitle_21 (Union[Unset, str]):
        as_left_value_subtitle_22 (Union[Unset, str]):
        as_left_value_subtitle_23 (Union[Unset, str]):
        as_left_value_subtitle_24 (Union[Unset, str]):
        as_left_value_subtitle_25 (Union[Unset, str]):
        as_left_value_subtitle_26 (Union[Unset, str]):
        as_left_value_subtitle_27 (Union[Unset, str]):
        as_left_value_subtitle_28 (Union[Unset, str]):
        as_left_value_subtitle_29 (Union[Unset, str]):
        as_left_value_subtitle_30 (Union[Unset, str]):
        as_left_value_subtitle_31 (Union[Unset, str]):
        as_left_value_subtitle_32 (Union[Unset, str]):
        as_left_value_subtitle_33 (Union[Unset, str]):
        as_left_value_subtitle_34 (Union[Unset, str]):
        as_left_value_subtitle_35 (Union[Unset, str]):
        as_left_value_subtitle_36 (Union[Unset, str]):
        as_left_value_subtitle_37 (Union[Unset, str]):
        as_left_value_subtitle_38 (Union[Unset, str]):
        as_left_value_subtitle_39 (Union[Unset, str]):
        as_left_value_subtitle_40 (Union[Unset, str]):
        as_left_mean (Union[Unset, float]):
        as_left_mean_raw (Union[Unset, float]):
        as_left_sd (Union[Unset, float]):
        as_left_sd_raw (Union[Unset, float]):
        as_left_cv (Union[Unset, float]):
        as_left_cv_raw (Union[Unset, float]):
        as_left_delta (Union[Unset, float]):
        as_left_range (Union[Unset, float]):
        as_left_result (Union[None, Unset, int]):
        as_left_range_result (Union[Unset, bool]):
        as_left_delta_result (Union[Unset, bool]):
        as_left_min_result (Union[Unset, bool]):
        as_left_max_result (Union[Unset, bool]):
        as_left_tar_result (Union[Unset, bool]):
        as_left_tur_result (Union[Unset, bool]):
        as_left_error_result (Union[Unset, bool]):
        as_left_sd_result (Union[Unset, bool]):
        as_left_cv_result (Union[Unset, bool]):
        as_left_custom_field_result (Union[Unset, int]):
        as_left_mu (Union[Unset, float]):
        as_left_mu_raw (Union[Unset, float]):
        as_left_mu_effective_dof (Union[Unset, float]):
        as_left_mu_coverage_factor (Union[Unset, float]):
        as_left_cmc (Union[Unset, float]):
        as_left_cmc_comments (Union[Unset, str]):
        as_left_calculated_uncertainty (Union[Unset, float]):
        as_left_lab_mu (Union[Unset, float]):
        as_left_uncertainty_budget (Union[Unset, str]):
        as_left_mu_extended (Union[Unset, str]):
        as_left_channel (Union[Unset, int]):
        as_left_measurement_type (Union[Unset,
            QualerApiModelsReportDatasetsToMeasurementAllResponseAsLeftMeasurementType]):
        as_left_updated_by (Union[Unset, str]):
        as_left_updated_on (Union[None, Unset, datetime.datetime]):
        as_left_specification_title (Union[Unset, str]):
        as_left_specification_subtitle (Union[Unset, str]):
        as_left_specification_group (Union[Unset, str]):
        as_left_batch_type (Union[Unset, int]):
        as_left_batch_result (Union[Unset, int]):
        as_left_is_by_channel (Union[Unset, bool]):
        as_left_channel_count (Union[Unset, int]):
        as_left_commenced_on (Union[Unset, datetime.datetime]):
        as_left_commenced_by (Union[Unset, str]):
        as_left_z_factor (Union[Unset, float]):
        as_left_air_buoyancy (Union[Unset, float]):
        as_left_evaporation_rate (Union[Unset, float]):
        as_left_ambient_temperature (Union[Unset, float]):
        as_left_air_humidity (Union[Unset, float]):
        as_left_barometric_pressure (Union[Unset, float]):
        as_left_altitude (Union[Unset, float]):
        as_left_wind_speed (Union[Unset, float]):
        as_left_solar_radiation (Union[Unset, float]):
        as_left_light_intensity (Union[Unset, float]):
        as_left_noise_level (Union[Unset, float]):
        as_left_ph_level (Union[Unset, float]):
        as_left_water_conductivity (Union[Unset, float]):
        as_left_water_temperature (Union[Unset, float]):
        as_left_z_factor_uom (Union[Unset, str]):
        as_left_air_buoyancy_uom (Union[Unset, str]):
        as_left_evaporation_rate_uom (Union[Unset, str]):
        as_left_ambient_temperature_uom (Union[Unset, str]):
        as_left_air_humidity_uom (Union[Unset, str]):
        as_left_barometric_pressure_uom (Union[Unset, str]):
        as_left_altitude_uom (Union[Unset, str]):
        as_left_wind_speed_uom (Union[Unset, str]):
        as_left_solar_radiation_uom (Union[Unset, str]):
        as_left_light_intensity_uom (Union[Unset, str]):
        as_left_noise_level_uom (Union[Unset, str]):
        as_left_ph_level_uom (Union[Unset, str]):
        as_left_water_conductivity_uom (Union[Unset, str]):
        as_left_water_temperature_uom (Union[Unset, str]):
        as_left_specification_name (Union[Unset, str]):
        as_left_parameter_name (Union[Unset, str]):
        as_left_display_order (Union[Unset, int]):
        as_left_unit_of_measure (Union[Unset, str]):
        as_left_display_format (Union[Unset, str]):
        as_left_precision (Union[Unset, float]):
        as_left_precision_type (Union[Unset, QualerApiModelsReportDatasetsToMeasurementAllResponseAsLeftPrecisionType]):
        as_left_minimum (Union[Unset, float]):
        as_left_nominal (Union[Unset, float]):
        as_left_expected_value (Union[Unset, float]):
        as_left_expected_value_raw (Union[Unset, str]):
        as_left_test_value (Union[Unset, float]):
        as_left_base_value (Union[Unset, float]):
        as_left_maxi_mum (Union[Unset, float]):
        as_left_resolution (Union[Unset, float]):
        as_left_resolution_count (Union[Unset, int]):
        as_left_measurement_not_taken_result (Union[Unset,
            QualerApiModelsReportDatasetsToMeasurementAllResponseAsLeftMeasurementNotTakenResult]):
        as_left_hide_from_certificate (Union[Unset, bool]):
        as_left_measurement_not_taken_reason (Union[Unset, str]):
        as_left_measurement_batch_id (Union[Unset, int]):
        as_left_measurement_id (Union[Unset, int]):
        as_left_standard_id (Union[Unset, int]):
        as_left_tool_id (Union[Unset, int]):
        as_left_measurement_condition_id (Union[Unset, int]):
        as_left_measurement_point_id (Union[Unset, int]):
    """

    barcode: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_part_number: Union[Unset, str] = UNSET
    part_number: Union[Unset, str] = UNSET
    vendor_company_id: Union[Unset, int] = UNSET
    service_order_number: Union[Unset, int] = UNSET
    completed_by_name: Union[Unset, str] = UNSET
    completed_on: Union[Unset, datetime.datetime] = UNSET
    is_limited: Union[Unset, bool] = UNSET
    vendor_tag: Union[Unset, str] = UNSET
    room: Union[Unset, str] = UNSET
    segment_name: Union[Unset, str] = UNSET
    schedule_name: Union[Unset, str] = UNSET
    next_segment_name: Union[Unset, str] = UNSET
    certificate_number: Union[Unset, str] = UNSET
    work_status: Union[None, Unset, int] = UNSET
    service_type: Union[Unset, str] = UNSET
    service_level: Union[Unset, str] = UNSET
    service_comments: Union[Unset, str] = UNSET
    order_item_number: Union[Unset, int] = UNSET
    service_total: Union[Unset, float] = UNSET
    repairs_total: Union[Unset, float] = UNSET
    parts_total: Union[Unset, float] = UNSET
    asset_tag: Union[Unset, str] = UNSET
    asset_user: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    equipment_id: Union[Unset, str] = UNSET
    legacy_identifier: Union[Unset, str] = UNSET
    asset_name: Union[Unset, str] = UNSET
    asset_description: Union[Unset, str] = UNSET
    product_name: Union[Unset, str] = UNSET
    product_description: Union[Unset, str] = UNSET
    asset_maker: Union[Unset, str] = UNSET
    asset_tag_change: Union[Unset, str] = UNSET
    asset_user_change: Union[Unset, str] = UNSET
    serial_number_change: Union[Unset, str] = UNSET
    service_date: Union[None, Unset, datetime.datetime] = UNSET
    next_service_date: Union[None, Unset, datetime.datetime] = UNSET
    service_order_item_id: Union[Unset, int] = UNSET
    site_name: Union[Unset, str] = UNSET
    po_number: Union[Unset, str] = UNSET
    shipped_date: Union[None, Unset, datetime.datetime] = UNSET
    tracking_number: Union[Unset, str] = UNSET
    payment_terms: Union[Unset, int] = UNSET
    shipping_method: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    site_access_notes: Union[Unset, str] = UNSET
    as_left_decimal_places: Union[Unset, int] = UNSET
    as_left_measurement_set_name: Union[Unset, str] = UNSET
    as_left_measurement_set_id: Union[Unset, int] = UNSET
    as_left_adjustment_threshold: Union[Unset, float] = UNSET
    as_left_mean_extended: Union[Unset, str] = UNSET
    as_left_sd_extended: Union[Unset, str] = UNSET
    as_left_range_extended: Union[Unset, str] = UNSET
    as_left_delta_extended: Union[Unset, str] = UNSET
    as_left_cv_extended: Union[Unset, str] = UNSET
    as_left_nominal_extended: Union[Unset, str] = UNSET
    as_left_min_max_header: Union[Unset, str] = UNSET
    as_left_accuracy_class: Union[Unset, str] = UNSET
    as_left_accuracy_class_min: Union[Unset, float] = UNSET
    as_left_accuracy_class_max: Union[Unset, float] = UNSET
    as_left_minimum_measured_value: Union[Unset, float] = UNSET
    as_left_maxi_mum_measured_value: Union[Unset, float] = UNSET
    as_left_min_max_value_extended: Union[Unset, str] = UNSET
    as_left_tool_range_name: Union[Unset, str] = UNSET
    as_left_tool_range_uncertainty: Union[Unset, str] = UNSET
    as_left_primary_tool_last_service_date: Union[None, Unset, datetime.datetime] = (
        UNSET
    )
    as_left_primary_tool_next_service_date: Union[None, Unset, datetime.datetime] = (
        UNSET
    )
    as_left_primary_tool_calibrated_by: Union[Unset, str] = UNSET
    as_left_primary_tool_tool_name: Union[Unset, str] = UNSET
    as_left_primary_tool_tool_description: Union[Unset, str] = UNSET
    as_left_primary_tool_tool_type_name: Union[Unset, str] = UNSET
    as_left_primary_tool_manufacturer: Union[Unset, str] = UNSET
    as_left_primary_tool_manufacturer_part_number: Union[Unset, str] = UNSET
    as_left_primary_tool_serial_number: Union[Unset, str] = UNSET
    as_found_measurement_set_name: Union[Unset, str] = UNSET
    as_found_measurement_set_id: Union[Unset, int] = UNSET
    as_found_adjustment_threshold: Union[Unset, float] = UNSET
    as_found_decimal_places: Union[Unset, int] = UNSET
    as_found_mean_extended: Union[Unset, str] = UNSET
    as_found_sd_extended: Union[Unset, str] = UNSET
    as_found_range_extended: Union[Unset, str] = UNSET
    as_found_delta_extended: Union[Unset, str] = UNSET
    as_found_cv_extended: Union[Unset, str] = UNSET
    as_found_nominal_extended: Union[Unset, str] = UNSET
    as_found_min_max_header: Union[Unset, str] = UNSET
    as_found_accuracy_class: Union[Unset, str] = UNSET
    as_found_accuracy_class_min: Union[Unset, float] = UNSET
    as_found_accuracy_class_max: Union[Unset, float] = UNSET
    as_found_minimum_measured_value: Union[Unset, float] = UNSET
    as_found_maxi_mum_measured_value: Union[Unset, float] = UNSET
    as_found_min_max_value_extended: Union[Unset, str] = UNSET
    as_found_tool_range_name: Union[Unset, str] = UNSET
    as_found_tool_range_uncertainty: Union[Unset, str] = UNSET
    as_found_primary_tool_last_service_date: Union[None, Unset, datetime.datetime] = (
        UNSET
    )
    as_found_primary_tool_next_service_date: Union[None, Unset, datetime.datetime] = (
        UNSET
    )
    as_found_primary_tool_calibrated_by: Union[Unset, str] = UNSET
    as_found_primary_tool_tool_name: Union[Unset, str] = UNSET
    as_found_primary_tool_tool_description: Union[Unset, str] = UNSET
    as_found_primary_tool_tool_type_name: Union[Unset, str] = UNSET
    as_found_primary_tool_manufacturer: Union[Unset, str] = UNSET
    as_found_primary_tool_manufacturer_part_number: Union[Unset, str] = UNSET
    as_found_primary_tool_serial_number: Union[Unset, str] = UNSET
    as_left_secondary_tool_last_service_date: Union[None, Unset, datetime.datetime] = (
        UNSET
    )
    as_left_secondary_tool_next_service_date: Union[None, Unset, datetime.datetime] = (
        UNSET
    )
    as_left_secondary_tool_calibrated_by: Union[Unset, str] = UNSET
    as_left_secondary_tool_tool_name: Union[Unset, str] = UNSET
    as_left_secondary_tool_tool_description: Union[Unset, str] = UNSET
    as_left_secondary_tool_tool_type_name: Union[Unset, str] = UNSET
    as_left_secondary_tool_manufacturer: Union[Unset, str] = UNSET
    as_left_secondary_tool_manufacturer_part_number: Union[Unset, str] = UNSET
    as_left_secondary_tool_serial_number: Union[Unset, str] = UNSET
    as_found_secondary_tool_last_service_date: Union[None, Unset, datetime.datetime] = (
        UNSET
    )
    as_found_secondary_tool_next_service_date: Union[None, Unset, datetime.datetime] = (
        UNSET
    )
    as_found_secondary_tool_calibrated_by: Union[Unset, str] = UNSET
    as_found_secondary_tool_tool_name: Union[Unset, str] = UNSET
    as_found_secondary_tool_tool_description: Union[Unset, str] = UNSET
    as_found_secondary_tool_tool_type_name: Union[Unset, str] = UNSET
    as_found_secondary_tool_manufacturer: Union[Unset, str] = UNSET
    as_found_secondary_tool_manufacturer_part_number: Union[Unset, str] = UNSET
    as_found_secondary_tool_serial_number: Union[Unset, str] = UNSET
    as_found_measurement_not_taken_result: Union[
        Unset,
        QualerApiModelsReportDatasetsToMeasurementAllResponseAsFoundMeasurementNotTakenResult,
    ] = UNSET
    as_found_hide_from_certificate: Union[Unset, bool] = UNSET
    as_found_measurement_not_taken_reason: Union[Unset, str] = UNSET
    as_left_values: Union[Unset, str] = UNSET
    as_left_is_accredited: Union[Unset, bool] = UNSET
    as_left_is_range_accredited: Union[Unset, bool] = UNSET
    as_found_values: Union[Unset, str] = UNSET
    as_found_is_accredited: Union[Unset, bool] = UNSET
    as_found_is_range_accredited: Union[Unset, bool] = UNSET
    as_found_parameter_id: Union[Unset, int] = UNSET
    as_found_sd_header: Union[Unset, float] = UNSET
    as_found_cv_header: Union[Unset, float] = UNSET
    as_found_measurement_local_time: Union[None, Unset, datetime.datetime] = UNSET
    as_found_tur: Union[Unset, float] = UNSET
    as_found_tur_raw: Union[Unset, float] = UNSET
    as_left_tur: Union[Unset, float] = UNSET
    as_left_tur_raw: Union[Unset, float] = UNSET
    as_found_tar: Union[Unset, float] = UNSET
    as_found_tar_raw: Union[Unset, float] = UNSET
    as_left_tar: Union[Unset, float] = UNSET
    as_left_tar_raw: Union[Unset, float] = UNSET
    as_found_guard_band: Union[Unset, str] = UNSET
    as_left_guard_band: Union[Unset, str] = UNSET
    as_found_guard_band_logic: Union[
        Unset,
        QualerApiModelsReportDatasetsToMeasurementAllResponseAsFoundGuardBandLogic,
    ] = UNSET
    as_left_guard_band_logic: Union[
        Unset, QualerApiModelsReportDatasetsToMeasurementAllResponseAsLeftGuardBandLogic
    ] = UNSET
    as_found_error: Union[Unset, float] = UNSET
    as_found_error_extended: Union[Unset, str] = UNSET
    as_left_error: Union[Unset, float] = UNSET
    as_left_error_extended: Union[Unset, str] = UNSET
    as_found_percent_of_tolerance: Union[Unset, float] = UNSET
    as_found_percent_of_tolerance_extended: Union[Unset, str] = UNSET
    as_left_percent_of_tolerance: Union[Unset, float] = UNSET
    as_left_percent_of_tolerance_extended: Union[Unset, str] = UNSET
    as_found_tolerance_maximum: Union[Unset, float] = UNSET
    as_found_tolerance_minimum: Union[Unset, float] = UNSET
    as_found_tolerance_type: Union[Unset, int] = UNSET
    as_found_tolerance_mode: Union[Unset, int] = UNSET
    as_found_tolerance_string: Union[Unset, str] = UNSET
    as_left_tolerance_maximum: Union[Unset, float] = UNSET
    as_left_tolerance_minimum: Union[Unset, float] = UNSET
    as_left_tolerance_type: Union[Unset, int] = UNSET
    as_left_tolerance_mode: Union[Unset, int] = UNSET
    as_left_tolerance_string: Union[Unset, str] = UNSET
    as_found_max_hysteresis: Union[Unset, float] = UNSET
    as_found_run: Union[Unset, int] = UNSET
    as_found_direction: Union[Unset, int] = UNSET
    as_found_hysteresis: Union[Unset, float] = UNSET
    as_left_max_hysteresis: Union[Unset, float] = UNSET
    as_left_run: Union[Unset, int] = UNSET
    as_left_direction: Union[Unset, int] = UNSET
    as_left_hysteresis: Union[Unset, float] = UNSET
    as_found_reading_entry_math: Union[
        Unset,
        QualerApiModelsReportDatasetsToMeasurementAllResponseAsFoundReadingEntryMath,
    ] = UNSET
    as_found_reading_entry_math_string: Union[Unset, str] = UNSET
    as_found_value_1: Union[Unset, str] = UNSET
    as_found_value_2: Union[Unset, str] = UNSET
    as_found_value_3: Union[Unset, str] = UNSET
    as_found_value_4: Union[Unset, str] = UNSET
    as_found_value_5: Union[Unset, str] = UNSET
    as_found_value_6: Union[Unset, str] = UNSET
    as_found_value_7: Union[Unset, str] = UNSET
    as_found_value_8: Union[Unset, str] = UNSET
    as_found_value_9: Union[Unset, str] = UNSET
    as_found_value_10: Union[Unset, str] = UNSET
    as_found_value_11: Union[Unset, str] = UNSET
    as_found_value_12: Union[Unset, str] = UNSET
    as_found_value_13: Union[Unset, str] = UNSET
    as_found_value_14: Union[Unset, str] = UNSET
    as_found_value_15: Union[Unset, str] = UNSET
    as_found_value_16: Union[Unset, str] = UNSET
    as_found_value_17: Union[Unset, str] = UNSET
    as_found_value_18: Union[Unset, str] = UNSET
    as_found_value_19: Union[Unset, str] = UNSET
    as_found_value_20: Union[Unset, str] = UNSET
    as_found_value_21: Union[Unset, str] = UNSET
    as_found_value_22: Union[Unset, str] = UNSET
    as_found_value_23: Union[Unset, str] = UNSET
    as_found_value_24: Union[Unset, str] = UNSET
    as_found_value_25: Union[Unset, str] = UNSET
    as_found_value_26: Union[Unset, str] = UNSET
    as_found_value_27: Union[Unset, str] = UNSET
    as_found_value_28: Union[Unset, str] = UNSET
    as_found_value_29: Union[Unset, str] = UNSET
    as_found_value_30: Union[Unset, str] = UNSET
    as_found_value_31: Union[Unset, str] = UNSET
    as_found_value_32: Union[Unset, str] = UNSET
    as_found_value_33: Union[Unset, str] = UNSET
    as_found_value_34: Union[Unset, str] = UNSET
    as_found_value_35: Union[Unset, str] = UNSET
    as_found_value_36: Union[Unset, str] = UNSET
    as_found_value_37: Union[Unset, str] = UNSET
    as_found_value_38: Union[Unset, str] = UNSET
    as_found_value_39: Union[Unset, str] = UNSET
    as_found_value_40: Union[Unset, str] = UNSET
    as_found_raw_value_1: Union[Unset, str] = UNSET
    as_found_raw_value_2: Union[Unset, str] = UNSET
    as_found_raw_value_3: Union[Unset, str] = UNSET
    as_found_raw_value_4: Union[Unset, str] = UNSET
    as_found_raw_value_5: Union[Unset, str] = UNSET
    as_found_raw_value_6: Union[Unset, str] = UNSET
    as_found_raw_value_7: Union[Unset, str] = UNSET
    as_found_raw_value_8: Union[Unset, str] = UNSET
    as_found_raw_value_9: Union[Unset, str] = UNSET
    as_found_raw_value_10: Union[Unset, str] = UNSET
    as_found_raw_value_11: Union[Unset, str] = UNSET
    as_found_raw_value_12: Union[Unset, str] = UNSET
    as_found_raw_value_13: Union[Unset, str] = UNSET
    as_found_raw_value_14: Union[Unset, str] = UNSET
    as_found_raw_value_15: Union[Unset, str] = UNSET
    as_found_raw_value_16: Union[Unset, str] = UNSET
    as_found_raw_value_17: Union[Unset, str] = UNSET
    as_found_raw_value_18: Union[Unset, str] = UNSET
    as_found_raw_value_19: Union[Unset, str] = UNSET
    as_found_raw_value_20: Union[Unset, str] = UNSET
    as_found_raw_value_21: Union[Unset, str] = UNSET
    as_found_raw_value_22: Union[Unset, str] = UNSET
    as_found_raw_value_23: Union[Unset, str] = UNSET
    as_found_raw_value_24: Union[Unset, str] = UNSET
    as_found_raw_value_25: Union[Unset, str] = UNSET
    as_found_raw_value_26: Union[Unset, str] = UNSET
    as_found_raw_value_27: Union[Unset, str] = UNSET
    as_found_raw_value_28: Union[Unset, str] = UNSET
    as_found_raw_value_29: Union[Unset, str] = UNSET
    as_found_raw_value_30: Union[Unset, str] = UNSET
    as_found_raw_value_31: Union[Unset, str] = UNSET
    as_found_raw_value_32: Union[Unset, str] = UNSET
    as_found_raw_value_33: Union[Unset, str] = UNSET
    as_found_raw_value_34: Union[Unset, str] = UNSET
    as_found_raw_value_35: Union[Unset, str] = UNSET
    as_found_raw_value_36: Union[Unset, str] = UNSET
    as_found_raw_value_37: Union[Unset, str] = UNSET
    as_found_raw_value_38: Union[Unset, str] = UNSET
    as_found_raw_value_39: Union[Unset, str] = UNSET
    as_found_raw_value_40: Union[Unset, str] = UNSET
    as_found_value_subtitle_1: Union[Unset, str] = UNSET
    as_found_value_subtitle_2: Union[Unset, str] = UNSET
    as_found_value_subtitle_3: Union[Unset, str] = UNSET
    as_found_value_subtitle_4: Union[Unset, str] = UNSET
    as_found_value_subtitle_5: Union[Unset, str] = UNSET
    as_found_value_subtitle_6: Union[Unset, str] = UNSET
    as_found_value_subtitle_7: Union[Unset, str] = UNSET
    as_found_value_subtitle_8: Union[Unset, str] = UNSET
    as_found_value_subtitle_9: Union[Unset, str] = UNSET
    as_found_value_subtitle_10: Union[Unset, str] = UNSET
    as_found_value_subtitle_11: Union[Unset, str] = UNSET
    as_found_value_subtitle_12: Union[Unset, str] = UNSET
    as_found_value_subtitle_13: Union[Unset, str] = UNSET
    as_found_value_subtitle_14: Union[Unset, str] = UNSET
    as_found_value_subtitle_15: Union[Unset, str] = UNSET
    as_found_value_subtitle_16: Union[Unset, str] = UNSET
    as_found_value_subtitle_17: Union[Unset, str] = UNSET
    as_found_value_subtitle_18: Union[Unset, str] = UNSET
    as_found_value_subtitle_19: Union[Unset, str] = UNSET
    as_found_value_subtitle_20: Union[Unset, str] = UNSET
    as_found_value_subtitle_21: Union[Unset, str] = UNSET
    as_found_value_subtitle_22: Union[Unset, str] = UNSET
    as_found_value_subtitle_23: Union[Unset, str] = UNSET
    as_found_value_subtitle_24: Union[Unset, str] = UNSET
    as_found_value_subtitle_25: Union[Unset, str] = UNSET
    as_found_value_subtitle_26: Union[Unset, str] = UNSET
    as_found_value_subtitle_27: Union[Unset, str] = UNSET
    as_found_value_subtitle_28: Union[Unset, str] = UNSET
    as_found_value_subtitle_29: Union[Unset, str] = UNSET
    as_found_value_subtitle_30: Union[Unset, str] = UNSET
    as_found_value_subtitle_31: Union[Unset, str] = UNSET
    as_found_value_subtitle_32: Union[Unset, str] = UNSET
    as_found_value_subtitle_33: Union[Unset, str] = UNSET
    as_found_value_subtitle_34: Union[Unset, str] = UNSET
    as_found_value_subtitle_35: Union[Unset, str] = UNSET
    as_found_value_subtitle_36: Union[Unset, str] = UNSET
    as_found_value_subtitle_37: Union[Unset, str] = UNSET
    as_found_value_subtitle_38: Union[Unset, str] = UNSET
    as_found_value_subtitle_39: Union[Unset, str] = UNSET
    as_found_value_subtitle_40: Union[Unset, str] = UNSET
    as_found_mean: Union[Unset, float] = UNSET
    as_found_mean_raw: Union[Unset, float] = UNSET
    as_found_sd: Union[Unset, float] = UNSET
    as_found_sd_raw: Union[Unset, float] = UNSET
    as_found_delta: Union[Unset, float] = UNSET
    as_found_range: Union[Unset, float] = UNSET
    as_found_cv: Union[Unset, float] = UNSET
    as_found_cv_raw: Union[Unset, float] = UNSET
    as_found_result: Union[None, Unset, int] = UNSET
    as_found_range_result: Union[Unset, bool] = UNSET
    as_found_delta_result: Union[Unset, bool] = UNSET
    as_found_min_result: Union[Unset, bool] = UNSET
    as_found_max_result: Union[Unset, bool] = UNSET
    as_found_tar_result: Union[Unset, bool] = UNSET
    as_found_tur_result: Union[Unset, bool] = UNSET
    as_found_error_result: Union[Unset, bool] = UNSET
    as_found_sd_result: Union[Unset, bool] = UNSET
    as_found_cv_result: Union[Unset, bool] = UNSET
    as_found_custom_field_result: Union[Unset, int] = UNSET
    as_found_mu: Union[Unset, float] = UNSET
    as_found_mu_raw: Union[Unset, float] = UNSET
    as_found_mu_effective_dof: Union[Unset, float] = UNSET
    as_found_mu_coverage_factor: Union[Unset, float] = UNSET
    as_found_cmc: Union[Unset, float] = UNSET
    as_found_cmc_comments: Union[Unset, str] = UNSET
    as_found_calculated_uncertainty: Union[Unset, float] = UNSET
    as_found_lab_mu: Union[Unset, float] = UNSET
    as_found_uncertainty_budget: Union[Unset, str] = UNSET
    as_found_mu_extended: Union[Unset, str] = UNSET
    as_found_channel: Union[Unset, int] = UNSET
    as_found_measurement_type: Union[
        Unset,
        QualerApiModelsReportDatasetsToMeasurementAllResponseAsFoundMeasurementType,
    ] = UNSET
    as_found_updated_by: Union[Unset, str] = UNSET
    as_found_updated_on: Union[None, Unset, datetime.datetime] = UNSET
    as_left_abbreviated_uom: Union[Unset, str] = UNSET
    as_left_unit_scale_factor: Union[Unset, float] = UNSET
    as_found_specification_title: Union[Unset, str] = UNSET
    as_found_specification_subtitle: Union[Unset, str] = UNSET
    as_found_specification_group: Union[Unset, str] = UNSET
    as_found_batch_type: Union[Unset, int] = UNSET
    as_found_batch_result: Union[Unset, int] = UNSET
    as_found_is_by_channel: Union[Unset, bool] = UNSET
    as_found_channel_count: Union[Unset, int] = UNSET
    as_found_commenced_on: Union[Unset, datetime.datetime] = UNSET
    as_found_commenced_by: Union[Unset, str] = UNSET
    as_found_z_factor: Union[Unset, float] = UNSET
    as_found_air_buoyancy: Union[Unset, float] = UNSET
    as_found_evaporation_rate: Union[Unset, float] = UNSET
    as_found_ambient_temperature: Union[Unset, float] = UNSET
    as_found_air_humidity: Union[Unset, float] = UNSET
    as_found_barometric_pressure: Union[Unset, float] = UNSET
    as_found_altitude: Union[Unset, float] = UNSET
    as_found_wind_speed: Union[Unset, float] = UNSET
    as_found_solar_radiation: Union[Unset, float] = UNSET
    as_found_light_intensity: Union[Unset, float] = UNSET
    as_found_noise_level: Union[Unset, float] = UNSET
    as_found_ph_level: Union[Unset, float] = UNSET
    as_found_water_conductivity: Union[Unset, float] = UNSET
    as_found_water_temperature: Union[Unset, float] = UNSET
    as_found_z_factor_uom: Union[Unset, str] = UNSET
    as_found_air_buoyancy_uom: Union[Unset, str] = UNSET
    as_found_evaporation_rate_uom: Union[Unset, str] = UNSET
    as_found_ambient_temperature_uom: Union[Unset, str] = UNSET
    as_found_air_humidity_uom: Union[Unset, str] = UNSET
    as_found_barometric_pressure_uom: Union[Unset, str] = UNSET
    as_found_altitude_uom: Union[Unset, str] = UNSET
    as_found_wind_speed_uom: Union[Unset, str] = UNSET
    as_found_solar_radiation_uom: Union[Unset, str] = UNSET
    as_found_light_intensity_uom: Union[Unset, str] = UNSET
    as_found_noise_level_uom: Union[Unset, str] = UNSET
    as_found_ph_level_uom: Union[Unset, str] = UNSET
    as_found_water_conductivity_uom: Union[Unset, str] = UNSET
    as_found_water_temperature_uom: Union[Unset, str] = UNSET
    as_found_abbreviated_uom: Union[Unset, str] = UNSET
    as_found_unit_scale_factor: Union[Unset, float] = UNSET
    as_found_specification_name: Union[Unset, str] = UNSET
    as_found_parameter_name: Union[Unset, str] = UNSET
    as_found_display_order: Union[Unset, int] = UNSET
    as_found_unit_of_measure: Union[Unset, str] = UNSET
    as_found_display_format: Union[Unset, str] = UNSET
    as_found_precision: Union[Unset, float] = UNSET
    as_found_precision_type: Union[
        Unset, QualerApiModelsReportDatasetsToMeasurementAllResponseAsFoundPrecisionType
    ] = UNSET
    as_found_minimum: Union[Unset, float] = UNSET
    as_found_nominal: Union[Unset, float] = UNSET
    as_found_expected_value: Union[Unset, float] = UNSET
    as_found_expected_value_raw: Union[Unset, str] = UNSET
    as_found_test_value: Union[Unset, float] = UNSET
    as_found_base_value: Union[Unset, float] = UNSET
    as_found_maxi_mum: Union[Unset, float] = UNSET
    as_found_resolution: Union[Unset, float] = UNSET
    as_found_resolution_count: Union[Unset, int] = UNSET
    as_found_measurement_batch_id: Union[Unset, int] = UNSET
    as_found_measurement_id: Union[Unset, int] = UNSET
    as_found_standard_id: Union[Unset, int] = UNSET
    as_found_tool_id: Union[Unset, int] = UNSET
    as_found_measurement_condition_id: Union[Unset, int] = UNSET
    as_found_measurement_point_id: Union[Unset, int] = UNSET
    as_left_parameter_id: Union[Unset, int] = UNSET
    as_left_sd_header: Union[Unset, float] = UNSET
    as_left_cv_header: Union[Unset, float] = UNSET
    as_left_measurement_local_time: Union[None, Unset, datetime.datetime] = UNSET
    as_left_reading_entry_math: Union[
        Unset,
        QualerApiModelsReportDatasetsToMeasurementAllResponseAsLeftReadingEntryMath,
    ] = UNSET
    as_left_reading_entry_math_string: Union[Unset, str] = UNSET
    as_left_value_1: Union[Unset, str] = UNSET
    as_left_value_2: Union[Unset, str] = UNSET
    as_left_value_3: Union[Unset, str] = UNSET
    as_left_value_4: Union[Unset, str] = UNSET
    as_left_value_5: Union[Unset, str] = UNSET
    as_left_value_6: Union[Unset, str] = UNSET
    as_left_value_7: Union[Unset, str] = UNSET
    as_left_value_8: Union[Unset, str] = UNSET
    as_left_value_9: Union[Unset, str] = UNSET
    as_left_value_10: Union[Unset, str] = UNSET
    as_left_value_11: Union[Unset, str] = UNSET
    as_left_value_12: Union[Unset, str] = UNSET
    as_left_value_13: Union[Unset, str] = UNSET
    as_left_value_14: Union[Unset, str] = UNSET
    as_left_value_15: Union[Unset, str] = UNSET
    as_left_value_16: Union[Unset, str] = UNSET
    as_left_value_17: Union[Unset, str] = UNSET
    as_left_value_18: Union[Unset, str] = UNSET
    as_left_value_19: Union[Unset, str] = UNSET
    as_left_value_20: Union[Unset, str] = UNSET
    as_left_value_21: Union[Unset, str] = UNSET
    as_left_value_22: Union[Unset, str] = UNSET
    as_left_value_23: Union[Unset, str] = UNSET
    as_left_value_24: Union[Unset, str] = UNSET
    as_left_value_25: Union[Unset, str] = UNSET
    as_left_value_26: Union[Unset, str] = UNSET
    as_left_value_27: Union[Unset, str] = UNSET
    as_left_value_28: Union[Unset, str] = UNSET
    as_left_value_29: Union[Unset, str] = UNSET
    as_left_value_30: Union[Unset, str] = UNSET
    as_left_value_31: Union[Unset, str] = UNSET
    as_left_value_32: Union[Unset, str] = UNSET
    as_left_value_33: Union[Unset, str] = UNSET
    as_left_value_34: Union[Unset, str] = UNSET
    as_left_value_35: Union[Unset, str] = UNSET
    as_left_value_36: Union[Unset, str] = UNSET
    as_left_value_37: Union[Unset, str] = UNSET
    as_left_value_38: Union[Unset, str] = UNSET
    as_left_value_39: Union[Unset, str] = UNSET
    as_left_value_40: Union[Unset, str] = UNSET
    as_left_raw_value_1: Union[Unset, str] = UNSET
    as_left_raw_value_2: Union[Unset, str] = UNSET
    as_left_raw_value_3: Union[Unset, str] = UNSET
    as_left_raw_value_4: Union[Unset, str] = UNSET
    as_left_raw_value_5: Union[Unset, str] = UNSET
    as_left_raw_value_6: Union[Unset, str] = UNSET
    as_left_raw_value_7: Union[Unset, str] = UNSET
    as_left_raw_value_8: Union[Unset, str] = UNSET
    as_left_raw_value_9: Union[Unset, str] = UNSET
    as_left_raw_value_10: Union[Unset, str] = UNSET
    as_left_raw_value_11: Union[Unset, str] = UNSET
    as_left_raw_value_12: Union[Unset, str] = UNSET
    as_left_raw_value_13: Union[Unset, str] = UNSET
    as_left_raw_value_14: Union[Unset, str] = UNSET
    as_left_raw_value_15: Union[Unset, str] = UNSET
    as_left_raw_value_16: Union[Unset, str] = UNSET
    as_left_raw_value_17: Union[Unset, str] = UNSET
    as_left_raw_value_18: Union[Unset, str] = UNSET
    as_left_raw_value_19: Union[Unset, str] = UNSET
    as_left_raw_value_20: Union[Unset, str] = UNSET
    as_left_raw_value_21: Union[Unset, str] = UNSET
    as_left_raw_value_22: Union[Unset, str] = UNSET
    as_left_raw_value_23: Union[Unset, str] = UNSET
    as_left_raw_value_24: Union[Unset, str] = UNSET
    as_left_raw_value_25: Union[Unset, str] = UNSET
    as_left_raw_value_26: Union[Unset, str] = UNSET
    as_left_raw_value_27: Union[Unset, str] = UNSET
    as_left_raw_value_28: Union[Unset, str] = UNSET
    as_left_raw_value_29: Union[Unset, str] = UNSET
    as_left_raw_value_30: Union[Unset, str] = UNSET
    as_left_raw_value_31: Union[Unset, str] = UNSET
    as_left_raw_value_32: Union[Unset, str] = UNSET
    as_left_raw_value_33: Union[Unset, str] = UNSET
    as_left_raw_value_34: Union[Unset, str] = UNSET
    as_left_raw_value_35: Union[Unset, str] = UNSET
    as_left_raw_value_36: Union[Unset, str] = UNSET
    as_left_raw_value_37: Union[Unset, str] = UNSET
    as_left_raw_value_38: Union[Unset, str] = UNSET
    as_left_raw_value_39: Union[Unset, str] = UNSET
    as_left_raw_value_40: Union[Unset, str] = UNSET
    as_left_value_subtitle_1: Union[Unset, str] = UNSET
    as_left_value_subtitle_2: Union[Unset, str] = UNSET
    as_left_value_subtitle_3: Union[Unset, str] = UNSET
    as_left_value_subtitle_4: Union[Unset, str] = UNSET
    as_left_value_subtitle_5: Union[Unset, str] = UNSET
    as_left_value_subtitle_6: Union[Unset, str] = UNSET
    as_left_value_subtitle_7: Union[Unset, str] = UNSET
    as_left_value_subtitle_8: Union[Unset, str] = UNSET
    as_left_value_subtitle_9: Union[Unset, str] = UNSET
    as_left_value_subtitle_10: Union[Unset, str] = UNSET
    as_left_value_subtitle_11: Union[Unset, str] = UNSET
    as_left_value_subtitle_12: Union[Unset, str] = UNSET
    as_left_value_subtitle_13: Union[Unset, str] = UNSET
    as_left_value_subtitle_14: Union[Unset, str] = UNSET
    as_left_value_subtitle_15: Union[Unset, str] = UNSET
    as_left_value_subtitle_16: Union[Unset, str] = UNSET
    as_left_value_subtitle_17: Union[Unset, str] = UNSET
    as_left_value_subtitle_18: Union[Unset, str] = UNSET
    as_left_value_subtitle_19: Union[Unset, str] = UNSET
    as_left_value_subtitle_20: Union[Unset, str] = UNSET
    as_left_value_subtitle_21: Union[Unset, str] = UNSET
    as_left_value_subtitle_22: Union[Unset, str] = UNSET
    as_left_value_subtitle_23: Union[Unset, str] = UNSET
    as_left_value_subtitle_24: Union[Unset, str] = UNSET
    as_left_value_subtitle_25: Union[Unset, str] = UNSET
    as_left_value_subtitle_26: Union[Unset, str] = UNSET
    as_left_value_subtitle_27: Union[Unset, str] = UNSET
    as_left_value_subtitle_28: Union[Unset, str] = UNSET
    as_left_value_subtitle_29: Union[Unset, str] = UNSET
    as_left_value_subtitle_30: Union[Unset, str] = UNSET
    as_left_value_subtitle_31: Union[Unset, str] = UNSET
    as_left_value_subtitle_32: Union[Unset, str] = UNSET
    as_left_value_subtitle_33: Union[Unset, str] = UNSET
    as_left_value_subtitle_34: Union[Unset, str] = UNSET
    as_left_value_subtitle_35: Union[Unset, str] = UNSET
    as_left_value_subtitle_36: Union[Unset, str] = UNSET
    as_left_value_subtitle_37: Union[Unset, str] = UNSET
    as_left_value_subtitle_38: Union[Unset, str] = UNSET
    as_left_value_subtitle_39: Union[Unset, str] = UNSET
    as_left_value_subtitle_40: Union[Unset, str] = UNSET
    as_left_mean: Union[Unset, float] = UNSET
    as_left_mean_raw: Union[Unset, float] = UNSET
    as_left_sd: Union[Unset, float] = UNSET
    as_left_sd_raw: Union[Unset, float] = UNSET
    as_left_cv: Union[Unset, float] = UNSET
    as_left_cv_raw: Union[Unset, float] = UNSET
    as_left_delta: Union[Unset, float] = UNSET
    as_left_range: Union[Unset, float] = UNSET
    as_left_result: Union[None, Unset, int] = UNSET
    as_left_range_result: Union[Unset, bool] = UNSET
    as_left_delta_result: Union[Unset, bool] = UNSET
    as_left_min_result: Union[Unset, bool] = UNSET
    as_left_max_result: Union[Unset, bool] = UNSET
    as_left_tar_result: Union[Unset, bool] = UNSET
    as_left_tur_result: Union[Unset, bool] = UNSET
    as_left_error_result: Union[Unset, bool] = UNSET
    as_left_sd_result: Union[Unset, bool] = UNSET
    as_left_cv_result: Union[Unset, bool] = UNSET
    as_left_custom_field_result: Union[Unset, int] = UNSET
    as_left_mu: Union[Unset, float] = UNSET
    as_left_mu_raw: Union[Unset, float] = UNSET
    as_left_mu_effective_dof: Union[Unset, float] = UNSET
    as_left_mu_coverage_factor: Union[Unset, float] = UNSET
    as_left_cmc: Union[Unset, float] = UNSET
    as_left_cmc_comments: Union[Unset, str] = UNSET
    as_left_calculated_uncertainty: Union[Unset, float] = UNSET
    as_left_lab_mu: Union[Unset, float] = UNSET
    as_left_uncertainty_budget: Union[Unset, str] = UNSET
    as_left_mu_extended: Union[Unset, str] = UNSET
    as_left_channel: Union[Unset, int] = UNSET
    as_left_measurement_type: Union[
        Unset,
        QualerApiModelsReportDatasetsToMeasurementAllResponseAsLeftMeasurementType,
    ] = UNSET
    as_left_updated_by: Union[Unset, str] = UNSET
    as_left_updated_on: Union[None, Unset, datetime.datetime] = UNSET
    as_left_specification_title: Union[Unset, str] = UNSET
    as_left_specification_subtitle: Union[Unset, str] = UNSET
    as_left_specification_group: Union[Unset, str] = UNSET
    as_left_batch_type: Union[Unset, int] = UNSET
    as_left_batch_result: Union[Unset, int] = UNSET
    as_left_is_by_channel: Union[Unset, bool] = UNSET
    as_left_channel_count: Union[Unset, int] = UNSET
    as_left_commenced_on: Union[Unset, datetime.datetime] = UNSET
    as_left_commenced_by: Union[Unset, str] = UNSET
    as_left_z_factor: Union[Unset, float] = UNSET
    as_left_air_buoyancy: Union[Unset, float] = UNSET
    as_left_evaporation_rate: Union[Unset, float] = UNSET
    as_left_ambient_temperature: Union[Unset, float] = UNSET
    as_left_air_humidity: Union[Unset, float] = UNSET
    as_left_barometric_pressure: Union[Unset, float] = UNSET
    as_left_altitude: Union[Unset, float] = UNSET
    as_left_wind_speed: Union[Unset, float] = UNSET
    as_left_solar_radiation: Union[Unset, float] = UNSET
    as_left_light_intensity: Union[Unset, float] = UNSET
    as_left_noise_level: Union[Unset, float] = UNSET
    as_left_ph_level: Union[Unset, float] = UNSET
    as_left_water_conductivity: Union[Unset, float] = UNSET
    as_left_water_temperature: Union[Unset, float] = UNSET
    as_left_z_factor_uom: Union[Unset, str] = UNSET
    as_left_air_buoyancy_uom: Union[Unset, str] = UNSET
    as_left_evaporation_rate_uom: Union[Unset, str] = UNSET
    as_left_ambient_temperature_uom: Union[Unset, str] = UNSET
    as_left_air_humidity_uom: Union[Unset, str] = UNSET
    as_left_barometric_pressure_uom: Union[Unset, str] = UNSET
    as_left_altitude_uom: Union[Unset, str] = UNSET
    as_left_wind_speed_uom: Union[Unset, str] = UNSET
    as_left_solar_radiation_uom: Union[Unset, str] = UNSET
    as_left_light_intensity_uom: Union[Unset, str] = UNSET
    as_left_noise_level_uom: Union[Unset, str] = UNSET
    as_left_ph_level_uom: Union[Unset, str] = UNSET
    as_left_water_conductivity_uom: Union[Unset, str] = UNSET
    as_left_water_temperature_uom: Union[Unset, str] = UNSET
    as_left_specification_name: Union[Unset, str] = UNSET
    as_left_parameter_name: Union[Unset, str] = UNSET
    as_left_display_order: Union[Unset, int] = UNSET
    as_left_unit_of_measure: Union[Unset, str] = UNSET
    as_left_display_format: Union[Unset, str] = UNSET
    as_left_precision: Union[Unset, float] = UNSET
    as_left_precision_type: Union[
        Unset, QualerApiModelsReportDatasetsToMeasurementAllResponseAsLeftPrecisionType
    ] = UNSET
    as_left_minimum: Union[Unset, float] = UNSET
    as_left_nominal: Union[Unset, float] = UNSET
    as_left_expected_value: Union[Unset, float] = UNSET
    as_left_expected_value_raw: Union[Unset, str] = UNSET
    as_left_test_value: Union[Unset, float] = UNSET
    as_left_base_value: Union[Unset, float] = UNSET
    as_left_maxi_mum: Union[Unset, float] = UNSET
    as_left_resolution: Union[Unset, float] = UNSET
    as_left_resolution_count: Union[Unset, int] = UNSET
    as_left_measurement_not_taken_result: Union[
        Unset,
        QualerApiModelsReportDatasetsToMeasurementAllResponseAsLeftMeasurementNotTakenResult,
    ] = UNSET
    as_left_hide_from_certificate: Union[Unset, bool] = UNSET
    as_left_measurement_not_taken_reason: Union[Unset, str] = UNSET
    as_left_measurement_batch_id: Union[Unset, int] = UNSET
    as_left_measurement_id: Union[Unset, int] = UNSET
    as_left_standard_id: Union[Unset, int] = UNSET
    as_left_tool_id: Union[Unset, int] = UNSET
    as_left_measurement_condition_id: Union[Unset, int] = UNSET
    as_left_measurement_point_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        barcode = self.barcode

        display_name = self.display_name

        display_part_number = self.display_part_number

        part_number = self.part_number

        vendor_company_id = self.vendor_company_id

        service_order_number = self.service_order_number

        completed_by_name = self.completed_by_name

        completed_on: Union[Unset, str] = UNSET
        if not isinstance(self.completed_on, Unset):
            completed_on = self.completed_on.isoformat()

        is_limited = self.is_limited

        vendor_tag = self.vendor_tag

        room = self.room

        segment_name = self.segment_name

        schedule_name = self.schedule_name

        next_segment_name = self.next_segment_name

        certificate_number = self.certificate_number

        work_status: Union[None, Unset, str]

        if isinstance(self.work_status, Unset):

            work_status = UNSET

        else:

            work_status = self.work_status
        service_type = self.service_type

        service_level = self.service_level

        service_comments = self.service_comments

        order_item_number = self.order_item_number

        service_total = self.service_total

        repairs_total = self.repairs_total

        parts_total = self.parts_total

        asset_tag = self.asset_tag

        asset_user = self.asset_user

        serial_number = self.serial_number

        equipment_id = self.equipment_id

        legacy_identifier = self.legacy_identifier

        asset_name = self.asset_name

        asset_description = self.asset_description

        product_name = self.product_name

        product_description = self.product_description

        asset_maker = self.asset_maker

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

        site_name = self.site_name

        po_number = self.po_number

        shipped_date: Union[None, Unset, str]
        if isinstance(self.shipped_date, Unset):
            shipped_date = UNSET
        elif isinstance(self.shipped_date, datetime.datetime):
            shipped_date = self.shipped_date.isoformat()
        else:
            shipped_date = self.shipped_date

        tracking_number = self.tracking_number

        payment_terms = self.payment_terms

        shipping_method = self.shipping_method

        location = self.location

        site_access_notes = self.site_access_notes

        as_left_decimal_places = self.as_left_decimal_places

        as_left_measurement_set_name = self.as_left_measurement_set_name

        as_left_measurement_set_id = self.as_left_measurement_set_id

        as_left_adjustment_threshold = self.as_left_adjustment_threshold

        as_left_mean_extended = self.as_left_mean_extended

        as_left_sd_extended = self.as_left_sd_extended

        as_left_range_extended = self.as_left_range_extended

        as_left_delta_extended = self.as_left_delta_extended

        as_left_cv_extended = self.as_left_cv_extended

        as_left_nominal_extended = self.as_left_nominal_extended

        as_left_min_max_header = self.as_left_min_max_header

        as_left_accuracy_class = self.as_left_accuracy_class

        as_left_accuracy_class_min = self.as_left_accuracy_class_min

        as_left_accuracy_class_max = self.as_left_accuracy_class_max

        as_left_minimum_measured_value = self.as_left_minimum_measured_value

        as_left_maxi_mum_measured_value = self.as_left_maxi_mum_measured_value

        as_left_min_max_value_extended = self.as_left_min_max_value_extended

        as_left_tool_range_name = self.as_left_tool_range_name

        as_left_tool_range_uncertainty = self.as_left_tool_range_uncertainty

        as_left_primary_tool_last_service_date: Union[None, Unset, str]
        if isinstance(self.as_left_primary_tool_last_service_date, Unset):
            as_left_primary_tool_last_service_date = UNSET
        elif isinstance(self.as_left_primary_tool_last_service_date, datetime.datetime):
            as_left_primary_tool_last_service_date = (
                self.as_left_primary_tool_last_service_date.isoformat()
            )
        else:
            as_left_primary_tool_last_service_date = (
                self.as_left_primary_tool_last_service_date
            )

        as_left_primary_tool_next_service_date: Union[None, Unset, str]
        if isinstance(self.as_left_primary_tool_next_service_date, Unset):
            as_left_primary_tool_next_service_date = UNSET
        elif isinstance(self.as_left_primary_tool_next_service_date, datetime.datetime):
            as_left_primary_tool_next_service_date = (
                self.as_left_primary_tool_next_service_date.isoformat()
            )
        else:
            as_left_primary_tool_next_service_date = (
                self.as_left_primary_tool_next_service_date
            )

        as_left_primary_tool_calibrated_by = self.as_left_primary_tool_calibrated_by

        as_left_primary_tool_tool_name = self.as_left_primary_tool_tool_name

        as_left_primary_tool_tool_description = (
            self.as_left_primary_tool_tool_description
        )

        as_left_primary_tool_tool_type_name = self.as_left_primary_tool_tool_type_name

        as_left_primary_tool_manufacturer = self.as_left_primary_tool_manufacturer

        as_left_primary_tool_manufacturer_part_number = (
            self.as_left_primary_tool_manufacturer_part_number
        )

        as_left_primary_tool_serial_number = self.as_left_primary_tool_serial_number

        as_found_measurement_set_name = self.as_found_measurement_set_name

        as_found_measurement_set_id = self.as_found_measurement_set_id

        as_found_adjustment_threshold = self.as_found_adjustment_threshold

        as_found_decimal_places = self.as_found_decimal_places

        as_found_mean_extended = self.as_found_mean_extended

        as_found_sd_extended = self.as_found_sd_extended

        as_found_range_extended = self.as_found_range_extended

        as_found_delta_extended = self.as_found_delta_extended

        as_found_cv_extended = self.as_found_cv_extended

        as_found_nominal_extended = self.as_found_nominal_extended

        as_found_min_max_header = self.as_found_min_max_header

        as_found_accuracy_class = self.as_found_accuracy_class

        as_found_accuracy_class_min = self.as_found_accuracy_class_min

        as_found_accuracy_class_max = self.as_found_accuracy_class_max

        as_found_minimum_measured_value = self.as_found_minimum_measured_value

        as_found_maxi_mum_measured_value = self.as_found_maxi_mum_measured_value

        as_found_min_max_value_extended = self.as_found_min_max_value_extended

        as_found_tool_range_name = self.as_found_tool_range_name

        as_found_tool_range_uncertainty = self.as_found_tool_range_uncertainty

        as_found_primary_tool_last_service_date: Union[None, Unset, str]
        if isinstance(self.as_found_primary_tool_last_service_date, Unset):
            as_found_primary_tool_last_service_date = UNSET
        elif isinstance(
            self.as_found_primary_tool_last_service_date, datetime.datetime
        ):
            as_found_primary_tool_last_service_date = (
                self.as_found_primary_tool_last_service_date.isoformat()
            )
        else:
            as_found_primary_tool_last_service_date = (
                self.as_found_primary_tool_last_service_date
            )

        as_found_primary_tool_next_service_date: Union[None, Unset, str]
        if isinstance(self.as_found_primary_tool_next_service_date, Unset):
            as_found_primary_tool_next_service_date = UNSET
        elif isinstance(
            self.as_found_primary_tool_next_service_date, datetime.datetime
        ):
            as_found_primary_tool_next_service_date = (
                self.as_found_primary_tool_next_service_date.isoformat()
            )
        else:
            as_found_primary_tool_next_service_date = (
                self.as_found_primary_tool_next_service_date
            )

        as_found_primary_tool_calibrated_by = self.as_found_primary_tool_calibrated_by

        as_found_primary_tool_tool_name = self.as_found_primary_tool_tool_name

        as_found_primary_tool_tool_description = (
            self.as_found_primary_tool_tool_description
        )

        as_found_primary_tool_tool_type_name = self.as_found_primary_tool_tool_type_name

        as_found_primary_tool_manufacturer = self.as_found_primary_tool_manufacturer

        as_found_primary_tool_manufacturer_part_number = (
            self.as_found_primary_tool_manufacturer_part_number
        )

        as_found_primary_tool_serial_number = self.as_found_primary_tool_serial_number

        as_left_secondary_tool_last_service_date: Union[None, Unset, str]
        if isinstance(self.as_left_secondary_tool_last_service_date, Unset):
            as_left_secondary_tool_last_service_date = UNSET
        elif isinstance(
            self.as_left_secondary_tool_last_service_date, datetime.datetime
        ):
            as_left_secondary_tool_last_service_date = (
                self.as_left_secondary_tool_last_service_date.isoformat()
            )
        else:
            as_left_secondary_tool_last_service_date = (
                self.as_left_secondary_tool_last_service_date
            )

        as_left_secondary_tool_next_service_date: Union[None, Unset, str]
        if isinstance(self.as_left_secondary_tool_next_service_date, Unset):
            as_left_secondary_tool_next_service_date = UNSET
        elif isinstance(
            self.as_left_secondary_tool_next_service_date, datetime.datetime
        ):
            as_left_secondary_tool_next_service_date = (
                self.as_left_secondary_tool_next_service_date.isoformat()
            )
        else:
            as_left_secondary_tool_next_service_date = (
                self.as_left_secondary_tool_next_service_date
            )

        as_left_secondary_tool_calibrated_by = self.as_left_secondary_tool_calibrated_by

        as_left_secondary_tool_tool_name = self.as_left_secondary_tool_tool_name

        as_left_secondary_tool_tool_description = (
            self.as_left_secondary_tool_tool_description
        )

        as_left_secondary_tool_tool_type_name = (
            self.as_left_secondary_tool_tool_type_name
        )

        as_left_secondary_tool_manufacturer = self.as_left_secondary_tool_manufacturer

        as_left_secondary_tool_manufacturer_part_number = (
            self.as_left_secondary_tool_manufacturer_part_number
        )

        as_left_secondary_tool_serial_number = self.as_left_secondary_tool_serial_number

        as_found_secondary_tool_last_service_date: Union[None, Unset, str]
        if isinstance(self.as_found_secondary_tool_last_service_date, Unset):
            as_found_secondary_tool_last_service_date = UNSET
        elif isinstance(
            self.as_found_secondary_tool_last_service_date, datetime.datetime
        ):
            as_found_secondary_tool_last_service_date = (
                self.as_found_secondary_tool_last_service_date.isoformat()
            )
        else:
            as_found_secondary_tool_last_service_date = (
                self.as_found_secondary_tool_last_service_date
            )

        as_found_secondary_tool_next_service_date: Union[None, Unset, str]
        if isinstance(self.as_found_secondary_tool_next_service_date, Unset):
            as_found_secondary_tool_next_service_date = UNSET
        elif isinstance(
            self.as_found_secondary_tool_next_service_date, datetime.datetime
        ):
            as_found_secondary_tool_next_service_date = (
                self.as_found_secondary_tool_next_service_date.isoformat()
            )
        else:
            as_found_secondary_tool_next_service_date = (
                self.as_found_secondary_tool_next_service_date
            )

        as_found_secondary_tool_calibrated_by = (
            self.as_found_secondary_tool_calibrated_by
        )

        as_found_secondary_tool_tool_name = self.as_found_secondary_tool_tool_name

        as_found_secondary_tool_tool_description = (
            self.as_found_secondary_tool_tool_description
        )

        as_found_secondary_tool_tool_type_name = (
            self.as_found_secondary_tool_tool_type_name
        )

        as_found_secondary_tool_manufacturer = self.as_found_secondary_tool_manufacturer

        as_found_secondary_tool_manufacturer_part_number = (
            self.as_found_secondary_tool_manufacturer_part_number
        )

        as_found_secondary_tool_serial_number = (
            self.as_found_secondary_tool_serial_number
        )

        as_found_measurement_not_taken_result: Union[None, Unset, int] = UNSET
        if not isinstance(self.as_found_measurement_not_taken_result, Unset):
            as_found_measurement_not_taken_result = (
                self.as_found_measurement_not_taken_result.value
            )

        as_found_hide_from_certificate = self.as_found_hide_from_certificate

        as_found_measurement_not_taken_reason = (
            self.as_found_measurement_not_taken_reason
        )

        as_left_values = self.as_left_values

        as_left_is_accredited = self.as_left_is_accredited

        as_left_is_range_accredited = self.as_left_is_range_accredited

        as_found_values = self.as_found_values

        as_found_is_accredited = self.as_found_is_accredited

        as_found_is_range_accredited = self.as_found_is_range_accredited

        as_found_parameter_id = self.as_found_parameter_id

        as_found_sd_header = self.as_found_sd_header

        as_found_cv_header = self.as_found_cv_header

        as_found_measurement_local_time: Union[None, Unset, str]
        if isinstance(self.as_found_measurement_local_time, Unset):
            as_found_measurement_local_time = UNSET
        elif isinstance(self.as_found_measurement_local_time, datetime.datetime):
            as_found_measurement_local_time = (
                self.as_found_measurement_local_time.isoformat()
            )
        else:
            as_found_measurement_local_time = self.as_found_measurement_local_time

        as_found_tur = self.as_found_tur

        as_found_tur_raw = self.as_found_tur_raw

        as_left_tur = self.as_left_tur

        as_left_tur_raw = self.as_left_tur_raw

        as_found_tar = self.as_found_tar

        as_found_tar_raw = self.as_found_tar_raw

        as_left_tar = self.as_left_tar

        as_left_tar_raw = self.as_left_tar_raw

        as_found_guard_band = self.as_found_guard_band

        as_left_guard_band = self.as_left_guard_band

        as_found_guard_band_logic: Union[Unset, int] = UNSET
        if not isinstance(self.as_found_guard_band_logic, Unset):
            as_found_guard_band_logic = self.as_found_guard_band_logic.value

        as_left_guard_band_logic: Union[Unset, int] = UNSET
        if not isinstance(self.as_left_guard_band_logic, Unset):
            as_left_guard_band_logic = self.as_left_guard_band_logic.value

        as_found_error = self.as_found_error

        as_found_error_extended = self.as_found_error_extended

        as_left_error = self.as_left_error

        as_left_error_extended = self.as_left_error_extended

        as_found_percent_of_tolerance = self.as_found_percent_of_tolerance

        as_found_percent_of_tolerance_extended = (
            self.as_found_percent_of_tolerance_extended
        )

        as_left_percent_of_tolerance = self.as_left_percent_of_tolerance

        as_left_percent_of_tolerance_extended = (
            self.as_left_percent_of_tolerance_extended
        )

        as_found_tolerance_maximum = self.as_found_tolerance_maximum

        as_found_tolerance_minimum = self.as_found_tolerance_minimum

        as_found_tolerance_type = self.as_found_tolerance_type

        as_found_tolerance_mode = self.as_found_tolerance_mode

        as_found_tolerance_string = self.as_found_tolerance_string

        as_left_tolerance_maximum = self.as_left_tolerance_maximum

        as_left_tolerance_minimum = self.as_left_tolerance_minimum

        as_left_tolerance_type = self.as_left_tolerance_type

        as_left_tolerance_mode = self.as_left_tolerance_mode

        as_left_tolerance_string = self.as_left_tolerance_string

        as_found_max_hysteresis = self.as_found_max_hysteresis

        as_found_run = self.as_found_run

        as_found_direction = self.as_found_direction

        as_found_hysteresis = self.as_found_hysteresis

        as_left_max_hysteresis = self.as_left_max_hysteresis

        as_left_run = self.as_left_run

        as_left_direction = self.as_left_direction

        as_left_hysteresis = self.as_left_hysteresis

        as_found_reading_entry_math: Union[Unset, str] = UNSET
        if not isinstance(self.as_found_reading_entry_math, Unset):
            as_found_reading_entry_math = self.as_found_reading_entry_math.value

        as_found_reading_entry_math_string = self.as_found_reading_entry_math_string

        as_found_value_1 = self.as_found_value_1

        as_found_value_2 = self.as_found_value_2

        as_found_value_3 = self.as_found_value_3

        as_found_value_4 = self.as_found_value_4

        as_found_value_5 = self.as_found_value_5

        as_found_value_6 = self.as_found_value_6

        as_found_value_7 = self.as_found_value_7

        as_found_value_8 = self.as_found_value_8

        as_found_value_9 = self.as_found_value_9

        as_found_value_10 = self.as_found_value_10

        as_found_value_11 = self.as_found_value_11

        as_found_value_12 = self.as_found_value_12

        as_found_value_13 = self.as_found_value_13

        as_found_value_14 = self.as_found_value_14

        as_found_value_15 = self.as_found_value_15

        as_found_value_16 = self.as_found_value_16

        as_found_value_17 = self.as_found_value_17

        as_found_value_18 = self.as_found_value_18

        as_found_value_19 = self.as_found_value_19

        as_found_value_20 = self.as_found_value_20

        as_found_value_21 = self.as_found_value_21

        as_found_value_22 = self.as_found_value_22

        as_found_value_23 = self.as_found_value_23

        as_found_value_24 = self.as_found_value_24

        as_found_value_25 = self.as_found_value_25

        as_found_value_26 = self.as_found_value_26

        as_found_value_27 = self.as_found_value_27

        as_found_value_28 = self.as_found_value_28

        as_found_value_29 = self.as_found_value_29

        as_found_value_30 = self.as_found_value_30

        as_found_value_31 = self.as_found_value_31

        as_found_value_32 = self.as_found_value_32

        as_found_value_33 = self.as_found_value_33

        as_found_value_34 = self.as_found_value_34

        as_found_value_35 = self.as_found_value_35

        as_found_value_36 = self.as_found_value_36

        as_found_value_37 = self.as_found_value_37

        as_found_value_38 = self.as_found_value_38

        as_found_value_39 = self.as_found_value_39

        as_found_value_40 = self.as_found_value_40

        as_found_raw_value_1 = self.as_found_raw_value_1

        as_found_raw_value_2 = self.as_found_raw_value_2

        as_found_raw_value_3 = self.as_found_raw_value_3

        as_found_raw_value_4 = self.as_found_raw_value_4

        as_found_raw_value_5 = self.as_found_raw_value_5

        as_found_raw_value_6 = self.as_found_raw_value_6

        as_found_raw_value_7 = self.as_found_raw_value_7

        as_found_raw_value_8 = self.as_found_raw_value_8

        as_found_raw_value_9 = self.as_found_raw_value_9

        as_found_raw_value_10 = self.as_found_raw_value_10

        as_found_raw_value_11 = self.as_found_raw_value_11

        as_found_raw_value_12 = self.as_found_raw_value_12

        as_found_raw_value_13 = self.as_found_raw_value_13

        as_found_raw_value_14 = self.as_found_raw_value_14

        as_found_raw_value_15 = self.as_found_raw_value_15

        as_found_raw_value_16 = self.as_found_raw_value_16

        as_found_raw_value_17 = self.as_found_raw_value_17

        as_found_raw_value_18 = self.as_found_raw_value_18

        as_found_raw_value_19 = self.as_found_raw_value_19

        as_found_raw_value_20 = self.as_found_raw_value_20

        as_found_raw_value_21 = self.as_found_raw_value_21

        as_found_raw_value_22 = self.as_found_raw_value_22

        as_found_raw_value_23 = self.as_found_raw_value_23

        as_found_raw_value_24 = self.as_found_raw_value_24

        as_found_raw_value_25 = self.as_found_raw_value_25

        as_found_raw_value_26 = self.as_found_raw_value_26

        as_found_raw_value_27 = self.as_found_raw_value_27

        as_found_raw_value_28 = self.as_found_raw_value_28

        as_found_raw_value_29 = self.as_found_raw_value_29

        as_found_raw_value_30 = self.as_found_raw_value_30

        as_found_raw_value_31 = self.as_found_raw_value_31

        as_found_raw_value_32 = self.as_found_raw_value_32

        as_found_raw_value_33 = self.as_found_raw_value_33

        as_found_raw_value_34 = self.as_found_raw_value_34

        as_found_raw_value_35 = self.as_found_raw_value_35

        as_found_raw_value_36 = self.as_found_raw_value_36

        as_found_raw_value_37 = self.as_found_raw_value_37

        as_found_raw_value_38 = self.as_found_raw_value_38

        as_found_raw_value_39 = self.as_found_raw_value_39

        as_found_raw_value_40 = self.as_found_raw_value_40

        as_found_value_subtitle_1 = self.as_found_value_subtitle_1

        as_found_value_subtitle_2 = self.as_found_value_subtitle_2

        as_found_value_subtitle_3 = self.as_found_value_subtitle_3

        as_found_value_subtitle_4 = self.as_found_value_subtitle_4

        as_found_value_subtitle_5 = self.as_found_value_subtitle_5

        as_found_value_subtitle_6 = self.as_found_value_subtitle_6

        as_found_value_subtitle_7 = self.as_found_value_subtitle_7

        as_found_value_subtitle_8 = self.as_found_value_subtitle_8

        as_found_value_subtitle_9 = self.as_found_value_subtitle_9

        as_found_value_subtitle_10 = self.as_found_value_subtitle_10

        as_found_value_subtitle_11 = self.as_found_value_subtitle_11

        as_found_value_subtitle_12 = self.as_found_value_subtitle_12

        as_found_value_subtitle_13 = self.as_found_value_subtitle_13

        as_found_value_subtitle_14 = self.as_found_value_subtitle_14

        as_found_value_subtitle_15 = self.as_found_value_subtitle_15

        as_found_value_subtitle_16 = self.as_found_value_subtitle_16

        as_found_value_subtitle_17 = self.as_found_value_subtitle_17

        as_found_value_subtitle_18 = self.as_found_value_subtitle_18

        as_found_value_subtitle_19 = self.as_found_value_subtitle_19

        as_found_value_subtitle_20 = self.as_found_value_subtitle_20

        as_found_value_subtitle_21 = self.as_found_value_subtitle_21

        as_found_value_subtitle_22 = self.as_found_value_subtitle_22

        as_found_value_subtitle_23 = self.as_found_value_subtitle_23

        as_found_value_subtitle_24 = self.as_found_value_subtitle_24

        as_found_value_subtitle_25 = self.as_found_value_subtitle_25

        as_found_value_subtitle_26 = self.as_found_value_subtitle_26

        as_found_value_subtitle_27 = self.as_found_value_subtitle_27

        as_found_value_subtitle_28 = self.as_found_value_subtitle_28

        as_found_value_subtitle_29 = self.as_found_value_subtitle_29

        as_found_value_subtitle_30 = self.as_found_value_subtitle_30

        as_found_value_subtitle_31 = self.as_found_value_subtitle_31

        as_found_value_subtitle_32 = self.as_found_value_subtitle_32

        as_found_value_subtitle_33 = self.as_found_value_subtitle_33

        as_found_value_subtitle_34 = self.as_found_value_subtitle_34

        as_found_value_subtitle_35 = self.as_found_value_subtitle_35

        as_found_value_subtitle_36 = self.as_found_value_subtitle_36

        as_found_value_subtitle_37 = self.as_found_value_subtitle_37

        as_found_value_subtitle_38 = self.as_found_value_subtitle_38

        as_found_value_subtitle_39 = self.as_found_value_subtitle_39

        as_found_value_subtitle_40 = self.as_found_value_subtitle_40

        as_found_mean = self.as_found_mean

        as_found_mean_raw = self.as_found_mean_raw

        as_found_sd = self.as_found_sd

        as_found_sd_raw = self.as_found_sd_raw

        as_found_delta = self.as_found_delta

        as_found_range = self.as_found_range

        as_found_cv = self.as_found_cv

        as_found_cv_raw = self.as_found_cv_raw

        as_found_result: Union[None, Unset, str]

        if isinstance(self.as_found_result, Unset):

            as_found_result = UNSET

        else:

            as_found_result = self.as_found_result
        as_found_range_result = self.as_found_range_result

        as_found_delta_result = self.as_found_delta_result

        as_found_min_result = self.as_found_min_result

        as_found_max_result = self.as_found_max_result

        as_found_tar_result = self.as_found_tar_result

        as_found_tur_result = self.as_found_tur_result

        as_found_error_result = self.as_found_error_result

        as_found_sd_result = self.as_found_sd_result

        as_found_cv_result = self.as_found_cv_result

        as_found_custom_field_result = self.as_found_custom_field_result

        as_found_mu = self.as_found_mu

        as_found_mu_raw = self.as_found_mu_raw

        as_found_mu_effective_dof = self.as_found_mu_effective_dof

        as_found_mu_coverage_factor = self.as_found_mu_coverage_factor

        as_found_cmc = self.as_found_cmc

        as_found_cmc_comments = self.as_found_cmc_comments

        as_found_calculated_uncertainty = self.as_found_calculated_uncertainty

        as_found_lab_mu = self.as_found_lab_mu

        as_found_uncertainty_budget = self.as_found_uncertainty_budget

        as_found_mu_extended = self.as_found_mu_extended

        as_found_channel = self.as_found_channel

        as_found_measurement_type: Union[Unset, int] = UNSET
        if not isinstance(self.as_found_measurement_type, Unset):
            as_found_measurement_type = self.as_found_measurement_type.value

        as_found_updated_by = self.as_found_updated_by

        as_found_updated_on: Union[None, Unset, str]
        if isinstance(self.as_found_updated_on, Unset):
            as_found_updated_on = UNSET
        elif isinstance(self.as_found_updated_on, datetime.datetime):
            as_found_updated_on = self.as_found_updated_on.isoformat()
        else:
            as_found_updated_on = self.as_found_updated_on

        as_left_abbreviated_uom = self.as_left_abbreviated_uom

        as_left_unit_scale_factor = self.as_left_unit_scale_factor

        as_found_specification_title = self.as_found_specification_title

        as_found_specification_subtitle = self.as_found_specification_subtitle

        as_found_specification_group = self.as_found_specification_group

        as_found_batch_type = self.as_found_batch_type

        as_found_batch_result = self.as_found_batch_result

        as_found_is_by_channel = self.as_found_is_by_channel

        as_found_channel_count = self.as_found_channel_count

        as_found_commenced_on: Union[Unset, str] = UNSET
        if not isinstance(self.as_found_commenced_on, Unset):
            as_found_commenced_on = self.as_found_commenced_on.isoformat()

        as_found_commenced_by = self.as_found_commenced_by

        as_found_z_factor = self.as_found_z_factor

        as_found_air_buoyancy = self.as_found_air_buoyancy

        as_found_evaporation_rate = self.as_found_evaporation_rate

        as_found_ambient_temperature = self.as_found_ambient_temperature

        as_found_air_humidity = self.as_found_air_humidity

        as_found_barometric_pressure = self.as_found_barometric_pressure

        as_found_altitude = self.as_found_altitude

        as_found_wind_speed = self.as_found_wind_speed

        as_found_solar_radiation = self.as_found_solar_radiation

        as_found_light_intensity = self.as_found_light_intensity

        as_found_noise_level = self.as_found_noise_level

        as_found_ph_level = self.as_found_ph_level

        as_found_water_conductivity = self.as_found_water_conductivity

        as_found_water_temperature = self.as_found_water_temperature

        as_found_z_factor_uom = self.as_found_z_factor_uom

        as_found_air_buoyancy_uom = self.as_found_air_buoyancy_uom

        as_found_evaporation_rate_uom = self.as_found_evaporation_rate_uom

        as_found_ambient_temperature_uom = self.as_found_ambient_temperature_uom

        as_found_air_humidity_uom = self.as_found_air_humidity_uom

        as_found_barometric_pressure_uom = self.as_found_barometric_pressure_uom

        as_found_altitude_uom = self.as_found_altitude_uom

        as_found_wind_speed_uom = self.as_found_wind_speed_uom

        as_found_solar_radiation_uom = self.as_found_solar_radiation_uom

        as_found_light_intensity_uom = self.as_found_light_intensity_uom

        as_found_noise_level_uom = self.as_found_noise_level_uom

        as_found_ph_level_uom = self.as_found_ph_level_uom

        as_found_water_conductivity_uom = self.as_found_water_conductivity_uom

        as_found_water_temperature_uom = self.as_found_water_temperature_uom

        as_found_abbreviated_uom = self.as_found_abbreviated_uom

        as_found_unit_scale_factor = self.as_found_unit_scale_factor

        as_found_specification_name = self.as_found_specification_name

        as_found_parameter_name = self.as_found_parameter_name

        as_found_display_order = self.as_found_display_order

        as_found_unit_of_measure = self.as_found_unit_of_measure

        as_found_display_format = self.as_found_display_format

        as_found_precision = self.as_found_precision

        as_found_precision_type: Union[Unset, str] = UNSET
        if not isinstance(self.as_found_precision_type, Unset):
            as_found_precision_type = self.as_found_precision_type.value

        as_found_minimum = self.as_found_minimum

        as_found_nominal = self.as_found_nominal

        as_found_expected_value = self.as_found_expected_value

        as_found_expected_value_raw = self.as_found_expected_value_raw

        as_found_test_value = self.as_found_test_value

        as_found_base_value = self.as_found_base_value

        as_found_maxi_mum = self.as_found_maxi_mum

        as_found_resolution = self.as_found_resolution

        as_found_resolution_count = self.as_found_resolution_count

        as_found_measurement_batch_id = self.as_found_measurement_batch_id

        as_found_measurement_id = self.as_found_measurement_id

        as_found_standard_id = self.as_found_standard_id

        as_found_tool_id = self.as_found_tool_id

        as_found_measurement_condition_id = self.as_found_measurement_condition_id

        as_found_measurement_point_id = self.as_found_measurement_point_id

        as_left_parameter_id = self.as_left_parameter_id

        as_left_sd_header = self.as_left_sd_header

        as_left_cv_header = self.as_left_cv_header

        as_left_measurement_local_time: Union[None, Unset, str]
        if isinstance(self.as_left_measurement_local_time, Unset):
            as_left_measurement_local_time = UNSET
        elif isinstance(self.as_left_measurement_local_time, datetime.datetime):
            as_left_measurement_local_time = (
                self.as_left_measurement_local_time.isoformat()
            )
        else:
            as_left_measurement_local_time = self.as_left_measurement_local_time

        as_left_reading_entry_math: Union[Unset, str] = UNSET
        if not isinstance(self.as_left_reading_entry_math, Unset):
            as_left_reading_entry_math = self.as_left_reading_entry_math.value

        as_left_reading_entry_math_string = self.as_left_reading_entry_math_string

        as_left_value_1 = self.as_left_value_1

        as_left_value_2 = self.as_left_value_2

        as_left_value_3 = self.as_left_value_3

        as_left_value_4 = self.as_left_value_4

        as_left_value_5 = self.as_left_value_5

        as_left_value_6 = self.as_left_value_6

        as_left_value_7 = self.as_left_value_7

        as_left_value_8 = self.as_left_value_8

        as_left_value_9 = self.as_left_value_9

        as_left_value_10 = self.as_left_value_10

        as_left_value_11 = self.as_left_value_11

        as_left_value_12 = self.as_left_value_12

        as_left_value_13 = self.as_left_value_13

        as_left_value_14 = self.as_left_value_14

        as_left_value_15 = self.as_left_value_15

        as_left_value_16 = self.as_left_value_16

        as_left_value_17 = self.as_left_value_17

        as_left_value_18 = self.as_left_value_18

        as_left_value_19 = self.as_left_value_19

        as_left_value_20 = self.as_left_value_20

        as_left_value_21 = self.as_left_value_21

        as_left_value_22 = self.as_left_value_22

        as_left_value_23 = self.as_left_value_23

        as_left_value_24 = self.as_left_value_24

        as_left_value_25 = self.as_left_value_25

        as_left_value_26 = self.as_left_value_26

        as_left_value_27 = self.as_left_value_27

        as_left_value_28 = self.as_left_value_28

        as_left_value_29 = self.as_left_value_29

        as_left_value_30 = self.as_left_value_30

        as_left_value_31 = self.as_left_value_31

        as_left_value_32 = self.as_left_value_32

        as_left_value_33 = self.as_left_value_33

        as_left_value_34 = self.as_left_value_34

        as_left_value_35 = self.as_left_value_35

        as_left_value_36 = self.as_left_value_36

        as_left_value_37 = self.as_left_value_37

        as_left_value_38 = self.as_left_value_38

        as_left_value_39 = self.as_left_value_39

        as_left_value_40 = self.as_left_value_40

        as_left_raw_value_1 = self.as_left_raw_value_1

        as_left_raw_value_2 = self.as_left_raw_value_2

        as_left_raw_value_3 = self.as_left_raw_value_3

        as_left_raw_value_4 = self.as_left_raw_value_4

        as_left_raw_value_5 = self.as_left_raw_value_5

        as_left_raw_value_6 = self.as_left_raw_value_6

        as_left_raw_value_7 = self.as_left_raw_value_7

        as_left_raw_value_8 = self.as_left_raw_value_8

        as_left_raw_value_9 = self.as_left_raw_value_9

        as_left_raw_value_10 = self.as_left_raw_value_10

        as_left_raw_value_11 = self.as_left_raw_value_11

        as_left_raw_value_12 = self.as_left_raw_value_12

        as_left_raw_value_13 = self.as_left_raw_value_13

        as_left_raw_value_14 = self.as_left_raw_value_14

        as_left_raw_value_15 = self.as_left_raw_value_15

        as_left_raw_value_16 = self.as_left_raw_value_16

        as_left_raw_value_17 = self.as_left_raw_value_17

        as_left_raw_value_18 = self.as_left_raw_value_18

        as_left_raw_value_19 = self.as_left_raw_value_19

        as_left_raw_value_20 = self.as_left_raw_value_20

        as_left_raw_value_21 = self.as_left_raw_value_21

        as_left_raw_value_22 = self.as_left_raw_value_22

        as_left_raw_value_23 = self.as_left_raw_value_23

        as_left_raw_value_24 = self.as_left_raw_value_24

        as_left_raw_value_25 = self.as_left_raw_value_25

        as_left_raw_value_26 = self.as_left_raw_value_26

        as_left_raw_value_27 = self.as_left_raw_value_27

        as_left_raw_value_28 = self.as_left_raw_value_28

        as_left_raw_value_29 = self.as_left_raw_value_29

        as_left_raw_value_30 = self.as_left_raw_value_30

        as_left_raw_value_31 = self.as_left_raw_value_31

        as_left_raw_value_32 = self.as_left_raw_value_32

        as_left_raw_value_33 = self.as_left_raw_value_33

        as_left_raw_value_34 = self.as_left_raw_value_34

        as_left_raw_value_35 = self.as_left_raw_value_35

        as_left_raw_value_36 = self.as_left_raw_value_36

        as_left_raw_value_37 = self.as_left_raw_value_37

        as_left_raw_value_38 = self.as_left_raw_value_38

        as_left_raw_value_39 = self.as_left_raw_value_39

        as_left_raw_value_40 = self.as_left_raw_value_40

        as_left_value_subtitle_1 = self.as_left_value_subtitle_1

        as_left_value_subtitle_2 = self.as_left_value_subtitle_2

        as_left_value_subtitle_3 = self.as_left_value_subtitle_3

        as_left_value_subtitle_4 = self.as_left_value_subtitle_4

        as_left_value_subtitle_5 = self.as_left_value_subtitle_5

        as_left_value_subtitle_6 = self.as_left_value_subtitle_6

        as_left_value_subtitle_7 = self.as_left_value_subtitle_7

        as_left_value_subtitle_8 = self.as_left_value_subtitle_8

        as_left_value_subtitle_9 = self.as_left_value_subtitle_9

        as_left_value_subtitle_10 = self.as_left_value_subtitle_10

        as_left_value_subtitle_11 = self.as_left_value_subtitle_11

        as_left_value_subtitle_12 = self.as_left_value_subtitle_12

        as_left_value_subtitle_13 = self.as_left_value_subtitle_13

        as_left_value_subtitle_14 = self.as_left_value_subtitle_14

        as_left_value_subtitle_15 = self.as_left_value_subtitle_15

        as_left_value_subtitle_16 = self.as_left_value_subtitle_16

        as_left_value_subtitle_17 = self.as_left_value_subtitle_17

        as_left_value_subtitle_18 = self.as_left_value_subtitle_18

        as_left_value_subtitle_19 = self.as_left_value_subtitle_19

        as_left_value_subtitle_20 = self.as_left_value_subtitle_20

        as_left_value_subtitle_21 = self.as_left_value_subtitle_21

        as_left_value_subtitle_22 = self.as_left_value_subtitle_22

        as_left_value_subtitle_23 = self.as_left_value_subtitle_23

        as_left_value_subtitle_24 = self.as_left_value_subtitle_24

        as_left_value_subtitle_25 = self.as_left_value_subtitle_25

        as_left_value_subtitle_26 = self.as_left_value_subtitle_26

        as_left_value_subtitle_27 = self.as_left_value_subtitle_27

        as_left_value_subtitle_28 = self.as_left_value_subtitle_28

        as_left_value_subtitle_29 = self.as_left_value_subtitle_29

        as_left_value_subtitle_30 = self.as_left_value_subtitle_30

        as_left_value_subtitle_31 = self.as_left_value_subtitle_31

        as_left_value_subtitle_32 = self.as_left_value_subtitle_32

        as_left_value_subtitle_33 = self.as_left_value_subtitle_33

        as_left_value_subtitle_34 = self.as_left_value_subtitle_34

        as_left_value_subtitle_35 = self.as_left_value_subtitle_35

        as_left_value_subtitle_36 = self.as_left_value_subtitle_36

        as_left_value_subtitle_37 = self.as_left_value_subtitle_37

        as_left_value_subtitle_38 = self.as_left_value_subtitle_38

        as_left_value_subtitle_39 = self.as_left_value_subtitle_39

        as_left_value_subtitle_40 = self.as_left_value_subtitle_40

        as_left_mean = self.as_left_mean

        as_left_mean_raw = self.as_left_mean_raw

        as_left_sd = self.as_left_sd

        as_left_sd_raw = self.as_left_sd_raw

        as_left_cv = self.as_left_cv

        as_left_cv_raw = self.as_left_cv_raw

        as_left_delta = self.as_left_delta

        as_left_range = self.as_left_range

        as_left_result: Union[None, Unset, int]
        if isinstance(self.as_left_result, Unset):
            as_left_result = UNSET
        else:
            as_left_result: Union[None, Unset, str]

            if isinstance(self.as_left_result, Unset):

                as_left_result = UNSET

            else:

                as_left_result = self.as_left_result
        as_left_range_result = self.as_left_range_result

        as_left_delta_result = self.as_left_delta_result

        as_left_min_result = self.as_left_min_result

        as_left_max_result = self.as_left_max_result

        as_left_tar_result = self.as_left_tar_result

        as_left_tur_result = self.as_left_tur_result

        as_left_error_result = self.as_left_error_result

        as_left_sd_result = self.as_left_sd_result

        as_left_cv_result = self.as_left_cv_result

        as_left_custom_field_result = self.as_left_custom_field_result

        as_left_mu = self.as_left_mu

        as_left_mu_raw = self.as_left_mu_raw

        as_left_mu_effective_dof = self.as_left_mu_effective_dof

        as_left_mu_coverage_factor = self.as_left_mu_coverage_factor

        as_left_cmc = self.as_left_cmc

        as_left_cmc_comments = self.as_left_cmc_comments

        as_left_calculated_uncertainty = self.as_left_calculated_uncertainty

        as_left_lab_mu = self.as_left_lab_mu

        as_left_uncertainty_budget = self.as_left_uncertainty_budget

        as_left_mu_extended = self.as_left_mu_extended

        as_left_channel = self.as_left_channel

        as_left_measurement_type: Union[Unset, int] = UNSET
        if not isinstance(self.as_left_measurement_type, Unset):
            as_left_measurement_type = self.as_left_measurement_type.value

        as_left_updated_by = self.as_left_updated_by

        as_left_updated_on: Union[None, Unset, str]
        if isinstance(self.as_left_updated_on, Unset):
            as_left_updated_on = UNSET
        elif isinstance(self.as_left_updated_on, datetime.datetime):
            as_left_updated_on = self.as_left_updated_on.isoformat()
        else:
            as_left_updated_on = self.as_left_updated_on

        as_left_specification_title = self.as_left_specification_title

        as_left_specification_subtitle = self.as_left_specification_subtitle

        as_left_specification_group = self.as_left_specification_group

        as_left_batch_type = self.as_left_batch_type

        as_left_batch_result = self.as_left_batch_result

        as_left_is_by_channel = self.as_left_is_by_channel

        as_left_channel_count = self.as_left_channel_count

        as_left_commenced_on: Union[Unset, str] = UNSET
        if not isinstance(self.as_left_commenced_on, Unset):
            as_left_commenced_on = self.as_left_commenced_on.isoformat()

        as_left_commenced_by = self.as_left_commenced_by

        as_left_z_factor = self.as_left_z_factor

        as_left_air_buoyancy = self.as_left_air_buoyancy

        as_left_evaporation_rate = self.as_left_evaporation_rate

        as_left_ambient_temperature = self.as_left_ambient_temperature

        as_left_air_humidity = self.as_left_air_humidity

        as_left_barometric_pressure = self.as_left_barometric_pressure

        as_left_altitude = self.as_left_altitude

        as_left_wind_speed = self.as_left_wind_speed

        as_left_solar_radiation = self.as_left_solar_radiation

        as_left_light_intensity = self.as_left_light_intensity

        as_left_noise_level = self.as_left_noise_level

        as_left_ph_level = self.as_left_ph_level

        as_left_water_conductivity = self.as_left_water_conductivity

        as_left_water_temperature = self.as_left_water_temperature

        as_left_z_factor_uom = self.as_left_z_factor_uom

        as_left_air_buoyancy_uom = self.as_left_air_buoyancy_uom

        as_left_evaporation_rate_uom = self.as_left_evaporation_rate_uom

        as_left_ambient_temperature_uom = self.as_left_ambient_temperature_uom

        as_left_air_humidity_uom = self.as_left_air_humidity_uom

        as_left_barometric_pressure_uom = self.as_left_barometric_pressure_uom

        as_left_altitude_uom = self.as_left_altitude_uom

        as_left_wind_speed_uom = self.as_left_wind_speed_uom

        as_left_solar_radiation_uom = self.as_left_solar_radiation_uom

        as_left_light_intensity_uom = self.as_left_light_intensity_uom

        as_left_noise_level_uom = self.as_left_noise_level_uom

        as_left_ph_level_uom = self.as_left_ph_level_uom

        as_left_water_conductivity_uom = self.as_left_water_conductivity_uom

        as_left_water_temperature_uom = self.as_left_water_temperature_uom

        as_left_specification_name = self.as_left_specification_name

        as_left_parameter_name = self.as_left_parameter_name

        as_left_display_order = self.as_left_display_order

        as_left_unit_of_measure = self.as_left_unit_of_measure

        as_left_display_format = self.as_left_display_format

        as_left_precision = self.as_left_precision

        as_left_precision_type: Union[Unset, str] = UNSET
        if not isinstance(self.as_left_precision_type, Unset):
            as_left_precision_type = self.as_left_precision_type.value

        as_left_minimum = self.as_left_minimum

        as_left_nominal = self.as_left_nominal

        as_left_expected_value = self.as_left_expected_value

        as_left_expected_value_raw = self.as_left_expected_value_raw

        as_left_test_value = self.as_left_test_value

        as_left_base_value = self.as_left_base_value

        as_left_maxi_mum = self.as_left_maxi_mum

        as_left_resolution = self.as_left_resolution

        as_left_resolution_count = self.as_left_resolution_count

        as_left_measurement_not_taken_result: Union[Unset, str] = UNSET
        if not isinstance(self.as_left_measurement_not_taken_result, Unset):
            as_left_measurement_not_taken_result = (
                self.as_left_measurement_not_taken_result.value
            )

        as_left_hide_from_certificate = self.as_left_hide_from_certificate

        as_left_measurement_not_taken_reason = self.as_left_measurement_not_taken_reason

        as_left_measurement_batch_id = self.as_left_measurement_batch_id

        as_left_measurement_id = self.as_left_measurement_id

        as_left_standard_id = self.as_left_standard_id

        as_left_tool_id = self.as_left_tool_id

        as_left_measurement_condition_id = self.as_left_measurement_condition_id

        as_left_measurement_point_id = self.as_left_measurement_point_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if barcode is not UNSET:
            field_dict["Barcode"] = barcode
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
        if completed_by_name is not UNSET:
            field_dict["CompletedByName"] = completed_by_name
        if completed_on is not UNSET:
            field_dict["CompletedOn"] = completed_on
        if is_limited is not UNSET:
            field_dict["IsLimited"] = is_limited
        if vendor_tag is not UNSET:
            field_dict["VendorTag"] = vendor_tag
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
        if service_comments is not UNSET:
            field_dict["ServiceComments"] = service_comments
        if order_item_number is not UNSET:
            field_dict["OrderItemNumber"] = order_item_number
        if service_total is not UNSET:
            field_dict["ServiceTotal"] = service_total
        if repairs_total is not UNSET:
            field_dict["RepairsTotal"] = repairs_total
        if parts_total is not UNSET:
            field_dict["PartsTotal"] = parts_total
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
        if site_name is not UNSET:
            field_dict["SiteName"] = site_name
        if po_number is not UNSET:
            field_dict["PoNumber"] = po_number
        if shipped_date is not UNSET:
            field_dict["ShippedDate"] = shipped_date
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
        if as_left_decimal_places is not UNSET:
            field_dict["AsLeftDecimalPlaces"] = as_left_decimal_places
        if as_left_measurement_set_name is not UNSET:
            field_dict["AsLeftMeasurementSetName"] = as_left_measurement_set_name
        if as_left_measurement_set_id is not UNSET:
            field_dict["AsLeftMeasurementSetId"] = as_left_measurement_set_id
        if as_left_adjustment_threshold is not UNSET:
            field_dict["AsLeftAdjustmentThreshold"] = as_left_adjustment_threshold
        if as_left_mean_extended is not UNSET:
            field_dict["AsLeftMeanExtended"] = as_left_mean_extended
        if as_left_sd_extended is not UNSET:
            field_dict["AsLeftSdExtended"] = as_left_sd_extended
        if as_left_range_extended is not UNSET:
            field_dict["AsLeftRangeExtended"] = as_left_range_extended
        if as_left_delta_extended is not UNSET:
            field_dict["AsLeftDeltaExtended"] = as_left_delta_extended
        if as_left_cv_extended is not UNSET:
            field_dict["AsLeftCvExtended"] = as_left_cv_extended
        if as_left_nominal_extended is not UNSET:
            field_dict["AsLeftNominalExtended"] = as_left_nominal_extended
        if as_left_min_max_header is not UNSET:
            field_dict["AsLeftMinMaxHeader"] = as_left_min_max_header
        if as_left_accuracy_class is not UNSET:
            field_dict["AsLeftAccuracyClass"] = as_left_accuracy_class
        if as_left_accuracy_class_min is not UNSET:
            field_dict["AsLeftAccuracyClassMin"] = as_left_accuracy_class_min
        if as_left_accuracy_class_max is not UNSET:
            field_dict["AsLeftAccuracyClassMax"] = as_left_accuracy_class_max
        if as_left_minimum_measured_value is not UNSET:
            field_dict["AsLeftMinimumMeasuredValue"] = as_left_minimum_measured_value
        if as_left_maxi_mum_measured_value is not UNSET:
            field_dict["AsLeftMaxiMumMeasuredValue"] = as_left_maxi_mum_measured_value
        if as_left_min_max_value_extended is not UNSET:
            field_dict["AsLeftMinMaxValueExtended"] = as_left_min_max_value_extended
        if as_left_tool_range_name is not UNSET:
            field_dict["AsLeftToolRangeName"] = as_left_tool_range_name
        if as_left_tool_range_uncertainty is not UNSET:
            field_dict["AsLeftToolRangeUncertainty"] = as_left_tool_range_uncertainty
        if as_left_primary_tool_last_service_date is not UNSET:
            field_dict["AsLeftPrimaryToolLastServiceDate"] = (
                as_left_primary_tool_last_service_date
            )
        if as_left_primary_tool_next_service_date is not UNSET:
            field_dict["AsLeftPrimaryToolNextServiceDate"] = (
                as_left_primary_tool_next_service_date
            )
        if as_left_primary_tool_calibrated_by is not UNSET:
            field_dict["AsLeftPrimaryToolCalibratedBy"] = (
                as_left_primary_tool_calibrated_by
            )
        if as_left_primary_tool_tool_name is not UNSET:
            field_dict["AsLeftPrimaryToolToolName"] = as_left_primary_tool_tool_name
        if as_left_primary_tool_tool_description is not UNSET:
            field_dict["AsLeftPrimaryToolToolDescription"] = (
                as_left_primary_tool_tool_description
            )
        if as_left_primary_tool_tool_type_name is not UNSET:
            field_dict["AsLeftPrimaryToolToolTypeName"] = (
                as_left_primary_tool_tool_type_name
            )
        if as_left_primary_tool_manufacturer is not UNSET:
            field_dict["AsLeftPrimaryToolManufacturer"] = (
                as_left_primary_tool_manufacturer
            )
        if as_left_primary_tool_manufacturer_part_number is not UNSET:
            field_dict["AsLeftPrimaryToolManufacturerPartNumber"] = (
                as_left_primary_tool_manufacturer_part_number
            )
        if as_left_primary_tool_serial_number is not UNSET:
            field_dict["AsLeftPrimaryToolSerialNumber"] = (
                as_left_primary_tool_serial_number
            )
        if as_found_measurement_set_name is not UNSET:
            field_dict["AsFoundMeasurementSetName"] = as_found_measurement_set_name
        if as_found_measurement_set_id is not UNSET:
            field_dict["AsFoundMeasurementSetId"] = as_found_measurement_set_id
        if as_found_adjustment_threshold is not UNSET:
            field_dict["AsFoundAdjustmentThreshold"] = as_found_adjustment_threshold
        if as_found_decimal_places is not UNSET:
            field_dict["AsFoundDecimalPlaces"] = as_found_decimal_places
        if as_found_mean_extended is not UNSET:
            field_dict["AsFoundMeanExtended"] = as_found_mean_extended
        if as_found_sd_extended is not UNSET:
            field_dict["AsFoundSdExtended"] = as_found_sd_extended
        if as_found_range_extended is not UNSET:
            field_dict["AsFoundRangeExtended"] = as_found_range_extended
        if as_found_delta_extended is not UNSET:
            field_dict["AsFoundDeltaExtended"] = as_found_delta_extended
        if as_found_cv_extended is not UNSET:
            field_dict["AsFoundCvExtended"] = as_found_cv_extended
        if as_found_nominal_extended is not UNSET:
            field_dict["AsFoundNominalExtended"] = as_found_nominal_extended
        if as_found_min_max_header is not UNSET:
            field_dict["AsFoundMinMaxHeader"] = as_found_min_max_header
        if as_found_accuracy_class is not UNSET:
            field_dict["AsFoundAccuracyClass"] = as_found_accuracy_class
        if as_found_accuracy_class_min is not UNSET:
            field_dict["AsFoundAccuracyClassMin"] = as_found_accuracy_class_min
        if as_found_accuracy_class_max is not UNSET:
            field_dict["AsFoundAccuracyClassMax"] = as_found_accuracy_class_max
        if as_found_minimum_measured_value is not UNSET:
            field_dict["AsFoundMinimumMeasuredValue"] = as_found_minimum_measured_value
        if as_found_maxi_mum_measured_value is not UNSET:
            field_dict["AsFoundMaxiMumMeasuredValue"] = as_found_maxi_mum_measured_value
        if as_found_min_max_value_extended is not UNSET:
            field_dict["AsFoundMinMaxValueExtended"] = as_found_min_max_value_extended
        if as_found_tool_range_name is not UNSET:
            field_dict["AsFoundToolRangeName"] = as_found_tool_range_name
        if as_found_tool_range_uncertainty is not UNSET:
            field_dict["AsFoundToolRangeUncertainty"] = as_found_tool_range_uncertainty
        if as_found_primary_tool_last_service_date is not UNSET:
            field_dict["AsFoundPrimaryToolLastServiceDate"] = (
                as_found_primary_tool_last_service_date
            )
        if as_found_primary_tool_next_service_date is not UNSET:
            field_dict["AsFoundPrimaryToolNextServiceDate"] = (
                as_found_primary_tool_next_service_date
            )
        if as_found_primary_tool_calibrated_by is not UNSET:
            field_dict["AsFoundPrimaryToolCalibratedBy"] = (
                as_found_primary_tool_calibrated_by
            )
        if as_found_primary_tool_tool_name is not UNSET:
            field_dict["AsFoundPrimaryToolToolName"] = as_found_primary_tool_tool_name
        if as_found_primary_tool_tool_description is not UNSET:
            field_dict["AsFoundPrimaryToolToolDescription"] = (
                as_found_primary_tool_tool_description
            )
        if as_found_primary_tool_tool_type_name is not UNSET:
            field_dict["AsFoundPrimaryToolToolTypeName"] = (
                as_found_primary_tool_tool_type_name
            )
        if as_found_primary_tool_manufacturer is not UNSET:
            field_dict["AsFoundPrimaryToolManufacturer"] = (
                as_found_primary_tool_manufacturer
            )
        if as_found_primary_tool_manufacturer_part_number is not UNSET:
            field_dict["AsFoundPrimaryToolManufacturerPartNumber"] = (
                as_found_primary_tool_manufacturer_part_number
            )
        if as_found_primary_tool_serial_number is not UNSET:
            field_dict["AsFoundPrimaryToolSerialNumber"] = (
                as_found_primary_tool_serial_number
            )
        if as_left_secondary_tool_last_service_date is not UNSET:
            field_dict["AsLeftSecondaryToolLastServiceDate"] = (
                as_left_secondary_tool_last_service_date
            )
        if as_left_secondary_tool_next_service_date is not UNSET:
            field_dict["AsLeftSecondaryToolNextServiceDate"] = (
                as_left_secondary_tool_next_service_date
            )
        if as_left_secondary_tool_calibrated_by is not UNSET:
            field_dict["AsLeftSecondaryToolCalibratedBy"] = (
                as_left_secondary_tool_calibrated_by
            )
        if as_left_secondary_tool_tool_name is not UNSET:
            field_dict["AsLeftSecondaryToolToolName"] = as_left_secondary_tool_tool_name
        if as_left_secondary_tool_tool_description is not UNSET:
            field_dict["AsLeftSecondaryToolToolDescription"] = (
                as_left_secondary_tool_tool_description
            )
        if as_left_secondary_tool_tool_type_name is not UNSET:
            field_dict["AsLeftSecondaryToolToolTypeName"] = (
                as_left_secondary_tool_tool_type_name
            )
        if as_left_secondary_tool_manufacturer is not UNSET:
            field_dict["AsLeftSecondaryToolManufacturer"] = (
                as_left_secondary_tool_manufacturer
            )
        if as_left_secondary_tool_manufacturer_part_number is not UNSET:
            field_dict["AsLeftSecondaryToolManufacturerPartNumber"] = (
                as_left_secondary_tool_manufacturer_part_number
            )
        if as_left_secondary_tool_serial_number is not UNSET:
            field_dict["AsLeftSecondaryToolSerialNumber"] = (
                as_left_secondary_tool_serial_number
            )
        if as_found_secondary_tool_last_service_date is not UNSET:
            field_dict["AsFoundSecondaryToolLastServiceDate"] = (
                as_found_secondary_tool_last_service_date
            )
        if as_found_secondary_tool_next_service_date is not UNSET:
            field_dict["AsFoundSecondaryToolNextServiceDate"] = (
                as_found_secondary_tool_next_service_date
            )
        if as_found_secondary_tool_calibrated_by is not UNSET:
            field_dict["AsFoundSecondaryToolCalibratedBy"] = (
                as_found_secondary_tool_calibrated_by
            )
        if as_found_secondary_tool_tool_name is not UNSET:
            field_dict["AsFoundSecondaryToolToolName"] = (
                as_found_secondary_tool_tool_name
            )
        if as_found_secondary_tool_tool_description is not UNSET:
            field_dict["AsFoundSecondaryToolToolDescription"] = (
                as_found_secondary_tool_tool_description
            )
        if as_found_secondary_tool_tool_type_name is not UNSET:
            field_dict["AsFoundSecondaryToolToolTypeName"] = (
                as_found_secondary_tool_tool_type_name
            )
        if as_found_secondary_tool_manufacturer is not UNSET:
            field_dict["AsFoundSecondaryToolManufacturer"] = (
                as_found_secondary_tool_manufacturer
            )
        if as_found_secondary_tool_manufacturer_part_number is not UNSET:
            field_dict["AsFoundSecondaryToolManufacturerPartNumber"] = (
                as_found_secondary_tool_manufacturer_part_number
            )
        if as_found_secondary_tool_serial_number is not UNSET:
            field_dict["AsFoundSecondaryToolSerialNumber"] = (
                as_found_secondary_tool_serial_number
            )
        if as_found_measurement_not_taken_result is not UNSET:
            field_dict["AsFoundMeasurementNotTakenResult"] = (
                as_found_measurement_not_taken_result
            )
        if as_found_hide_from_certificate is not UNSET:
            field_dict["AsFoundHideFromCertificate"] = as_found_hide_from_certificate
        if as_found_measurement_not_taken_reason is not UNSET:
            field_dict["AsFoundMeasurementNotTakenReason"] = (
                as_found_measurement_not_taken_reason
            )
        if as_left_values is not UNSET:
            field_dict["AsLeftValues"] = as_left_values
        if as_left_is_accredited is not UNSET:
            field_dict["AsLeftIsAccredited"] = as_left_is_accredited
        if as_left_is_range_accredited is not UNSET:
            field_dict["AsLeftIsRangeAccredited"] = as_left_is_range_accredited
        if as_found_values is not UNSET:
            field_dict["AsFoundValues"] = as_found_values
        if as_found_is_accredited is not UNSET:
            field_dict["AsFoundIsAccredited"] = as_found_is_accredited
        if as_found_is_range_accredited is not UNSET:
            field_dict["AsFoundIsRangeAccredited"] = as_found_is_range_accredited
        if as_found_parameter_id is not UNSET:
            field_dict["AsFoundParameterId"] = as_found_parameter_id
        if as_found_sd_header is not UNSET:
            field_dict["AsFoundSdHeader"] = as_found_sd_header
        if as_found_cv_header is not UNSET:
            field_dict["AsFoundCvHeader"] = as_found_cv_header
        if as_found_measurement_local_time is not UNSET:
            field_dict["AsFoundMeasurementLocalTime"] = as_found_measurement_local_time
        if as_found_tur is not UNSET:
            field_dict["AsFoundTur"] = as_found_tur
        if as_found_tur_raw is not UNSET:
            field_dict["AsFoundTurRaw"] = as_found_tur_raw
        if as_left_tur is not UNSET:
            field_dict["AsLeftTur"] = as_left_tur
        if as_left_tur_raw is not UNSET:
            field_dict["AsLeftTurRaw"] = as_left_tur_raw
        if as_found_tar is not UNSET:
            field_dict["AsFoundTar"] = as_found_tar
        if as_found_tar_raw is not UNSET:
            field_dict["AsFoundTarRaw"] = as_found_tar_raw
        if as_left_tar is not UNSET:
            field_dict["AsLeftTar"] = as_left_tar
        if as_left_tar_raw is not UNSET:
            field_dict["AsLeftTarRaw"] = as_left_tar_raw
        if as_found_guard_band is not UNSET:
            field_dict["AsFoundGuardBand"] = as_found_guard_band
        if as_left_guard_band is not UNSET:
            field_dict["AsLeftGuardBand"] = as_left_guard_band
        if as_found_guard_band_logic is not UNSET:
            field_dict["AsFoundGuardBandLogic"] = as_found_guard_band_logic
        if as_left_guard_band_logic is not UNSET:
            field_dict["AsLeftGuardBandLogic"] = as_left_guard_band_logic
        if as_found_error is not UNSET:
            field_dict["AsFoundError"] = as_found_error
        if as_found_error_extended is not UNSET:
            field_dict["AsFoundErrorExtended"] = as_found_error_extended
        if as_left_error is not UNSET:
            field_dict["AsLeftError"] = as_left_error
        if as_left_error_extended is not UNSET:
            field_dict["AsLeftErrorExtended"] = as_left_error_extended
        if as_found_percent_of_tolerance is not UNSET:
            field_dict["AsFoundPercentOfTolerance"] = as_found_percent_of_tolerance
        if as_found_percent_of_tolerance_extended is not UNSET:
            field_dict["AsFoundPercentOfToleranceExtended"] = (
                as_found_percent_of_tolerance_extended
            )
        if as_left_percent_of_tolerance is not UNSET:
            field_dict["AsLeftPercentOfTolerance"] = as_left_percent_of_tolerance
        if as_left_percent_of_tolerance_extended is not UNSET:
            field_dict["AsLeftPercentOfToleranceExtended"] = (
                as_left_percent_of_tolerance_extended
            )
        if as_found_tolerance_maximum is not UNSET:
            field_dict["AsFoundToleranceMaximum"] = as_found_tolerance_maximum
        if as_found_tolerance_minimum is not UNSET:
            field_dict["AsFoundToleranceMinimum"] = as_found_tolerance_minimum
        if as_found_tolerance_type is not UNSET:
            field_dict["AsFoundToleranceType"] = as_found_tolerance_type
        if as_found_tolerance_mode is not UNSET:
            field_dict["AsFoundToleranceMode"] = as_found_tolerance_mode
        if as_found_tolerance_string is not UNSET:
            field_dict["AsFoundToleranceString"] = as_found_tolerance_string
        if as_left_tolerance_maximum is not UNSET:
            field_dict["AsLeftToleranceMaximum"] = as_left_tolerance_maximum
        if as_left_tolerance_minimum is not UNSET:
            field_dict["AsLeftToleranceMinimum"] = as_left_tolerance_minimum
        if as_left_tolerance_type is not UNSET:
            field_dict["AsLeftToleranceType"] = as_left_tolerance_type
        if as_left_tolerance_mode is not UNSET:
            field_dict["AsLeftToleranceMode"] = as_left_tolerance_mode
        if as_left_tolerance_string is not UNSET:
            field_dict["AsLeftToleranceString"] = as_left_tolerance_string
        if as_found_max_hysteresis is not UNSET:
            field_dict["AsFoundMaxHysteresis"] = as_found_max_hysteresis
        if as_found_run is not UNSET:
            field_dict["AsFoundRun"] = as_found_run
        if as_found_direction is not UNSET:
            field_dict["AsFoundDirection"] = as_found_direction
        if as_found_hysteresis is not UNSET:
            field_dict["AsFoundHysteresis"] = as_found_hysteresis
        if as_left_max_hysteresis is not UNSET:
            field_dict["AsLeftMaxHysteresis"] = as_left_max_hysteresis
        if as_left_run is not UNSET:
            field_dict["AsLeftRun"] = as_left_run
        if as_left_direction is not UNSET:
            field_dict["AsLeftDirection"] = as_left_direction
        if as_left_hysteresis is not UNSET:
            field_dict["AsLeftHysteresis"] = as_left_hysteresis
        if as_found_reading_entry_math is not UNSET:
            field_dict["AsFoundReadingEntryMath"] = as_found_reading_entry_math
        if as_found_reading_entry_math_string is not UNSET:
            field_dict["AsFoundReadingEntryMathString"] = (
                as_found_reading_entry_math_string
            )
        if as_found_value_1 is not UNSET:
            field_dict["AsFoundValue1"] = as_found_value_1
        if as_found_value_2 is not UNSET:
            field_dict["AsFoundValue2"] = as_found_value_2
        if as_found_value_3 is not UNSET:
            field_dict["AsFoundValue3"] = as_found_value_3
        if as_found_value_4 is not UNSET:
            field_dict["AsFoundValue4"] = as_found_value_4
        if as_found_value_5 is not UNSET:
            field_dict["AsFoundValue5"] = as_found_value_5
        if as_found_value_6 is not UNSET:
            field_dict["AsFoundValue6"] = as_found_value_6
        if as_found_value_7 is not UNSET:
            field_dict["AsFoundValue7"] = as_found_value_7
        if as_found_value_8 is not UNSET:
            field_dict["AsFoundValue8"] = as_found_value_8
        if as_found_value_9 is not UNSET:
            field_dict["AsFoundValue9"] = as_found_value_9
        if as_found_value_10 is not UNSET:
            field_dict["AsFoundValue10"] = as_found_value_10
        if as_found_value_11 is not UNSET:
            field_dict["AsFoundValue11"] = as_found_value_11
        if as_found_value_12 is not UNSET:
            field_dict["AsFoundValue12"] = as_found_value_12
        if as_found_value_13 is not UNSET:
            field_dict["AsFoundValue13"] = as_found_value_13
        if as_found_value_14 is not UNSET:
            field_dict["AsFoundValue14"] = as_found_value_14
        if as_found_value_15 is not UNSET:
            field_dict["AsFoundValue15"] = as_found_value_15
        if as_found_value_16 is not UNSET:
            field_dict["AsFoundValue16"] = as_found_value_16
        if as_found_value_17 is not UNSET:
            field_dict["AsFoundValue17"] = as_found_value_17
        if as_found_value_18 is not UNSET:
            field_dict["AsFoundValue18"] = as_found_value_18
        if as_found_value_19 is not UNSET:
            field_dict["AsFoundValue19"] = as_found_value_19
        if as_found_value_20 is not UNSET:
            field_dict["AsFoundValue20"] = as_found_value_20
        if as_found_value_21 is not UNSET:
            field_dict["AsFoundValue21"] = as_found_value_21
        if as_found_value_22 is not UNSET:
            field_dict["AsFoundValue22"] = as_found_value_22
        if as_found_value_23 is not UNSET:
            field_dict["AsFoundValue23"] = as_found_value_23
        if as_found_value_24 is not UNSET:
            field_dict["AsFoundValue24"] = as_found_value_24
        if as_found_value_25 is not UNSET:
            field_dict["AsFoundValue25"] = as_found_value_25
        if as_found_value_26 is not UNSET:
            field_dict["AsFoundValue26"] = as_found_value_26
        if as_found_value_27 is not UNSET:
            field_dict["AsFoundValue27"] = as_found_value_27
        if as_found_value_28 is not UNSET:
            field_dict["AsFoundValue28"] = as_found_value_28
        if as_found_value_29 is not UNSET:
            field_dict["AsFoundValue29"] = as_found_value_29
        if as_found_value_30 is not UNSET:
            field_dict["AsFoundValue30"] = as_found_value_30
        if as_found_value_31 is not UNSET:
            field_dict["AsFoundValue31"] = as_found_value_31
        if as_found_value_32 is not UNSET:
            field_dict["AsFoundValue32"] = as_found_value_32
        if as_found_value_33 is not UNSET:
            field_dict["AsFoundValue33"] = as_found_value_33
        if as_found_value_34 is not UNSET:
            field_dict["AsFoundValue34"] = as_found_value_34
        if as_found_value_35 is not UNSET:
            field_dict["AsFoundValue35"] = as_found_value_35
        if as_found_value_36 is not UNSET:
            field_dict["AsFoundValue36"] = as_found_value_36
        if as_found_value_37 is not UNSET:
            field_dict["AsFoundValue37"] = as_found_value_37
        if as_found_value_38 is not UNSET:
            field_dict["AsFoundValue38"] = as_found_value_38
        if as_found_value_39 is not UNSET:
            field_dict["AsFoundValue39"] = as_found_value_39
        if as_found_value_40 is not UNSET:
            field_dict["AsFoundValue40"] = as_found_value_40
        if as_found_raw_value_1 is not UNSET:
            field_dict["AsFoundRawValue1"] = as_found_raw_value_1
        if as_found_raw_value_2 is not UNSET:
            field_dict["AsFoundRawValue2"] = as_found_raw_value_2
        if as_found_raw_value_3 is not UNSET:
            field_dict["AsFoundRawValue3"] = as_found_raw_value_3
        if as_found_raw_value_4 is not UNSET:
            field_dict["AsFoundRawValue4"] = as_found_raw_value_4
        if as_found_raw_value_5 is not UNSET:
            field_dict["AsFoundRawValue5"] = as_found_raw_value_5
        if as_found_raw_value_6 is not UNSET:
            field_dict["AsFoundRawValue6"] = as_found_raw_value_6
        if as_found_raw_value_7 is not UNSET:
            field_dict["AsFoundRawValue7"] = as_found_raw_value_7
        if as_found_raw_value_8 is not UNSET:
            field_dict["AsFoundRawValue8"] = as_found_raw_value_8
        if as_found_raw_value_9 is not UNSET:
            field_dict["AsFoundRawValue9"] = as_found_raw_value_9
        if as_found_raw_value_10 is not UNSET:
            field_dict["AsFoundRawValue10"] = as_found_raw_value_10
        if as_found_raw_value_11 is not UNSET:
            field_dict["AsFoundRawValue11"] = as_found_raw_value_11
        if as_found_raw_value_12 is not UNSET:
            field_dict["AsFoundRawValue12"] = as_found_raw_value_12
        if as_found_raw_value_13 is not UNSET:
            field_dict["AsFoundRawValue13"] = as_found_raw_value_13
        if as_found_raw_value_14 is not UNSET:
            field_dict["AsFoundRawValue14"] = as_found_raw_value_14
        if as_found_raw_value_15 is not UNSET:
            field_dict["AsFoundRawValue15"] = as_found_raw_value_15
        if as_found_raw_value_16 is not UNSET:
            field_dict["AsFoundRawValue16"] = as_found_raw_value_16
        if as_found_raw_value_17 is not UNSET:
            field_dict["AsFoundRawValue17"] = as_found_raw_value_17
        if as_found_raw_value_18 is not UNSET:
            field_dict["AsFoundRawValue18"] = as_found_raw_value_18
        if as_found_raw_value_19 is not UNSET:
            field_dict["AsFoundRawValue19"] = as_found_raw_value_19
        if as_found_raw_value_20 is not UNSET:
            field_dict["AsFoundRawValue20"] = as_found_raw_value_20
        if as_found_raw_value_21 is not UNSET:
            field_dict["AsFoundRawValue21"] = as_found_raw_value_21
        if as_found_raw_value_22 is not UNSET:
            field_dict["AsFoundRawValue22"] = as_found_raw_value_22
        if as_found_raw_value_23 is not UNSET:
            field_dict["AsFoundRawValue23"] = as_found_raw_value_23
        if as_found_raw_value_24 is not UNSET:
            field_dict["AsFoundRawValue24"] = as_found_raw_value_24
        if as_found_raw_value_25 is not UNSET:
            field_dict["AsFoundRawValue25"] = as_found_raw_value_25
        if as_found_raw_value_26 is not UNSET:
            field_dict["AsFoundRawValue26"] = as_found_raw_value_26
        if as_found_raw_value_27 is not UNSET:
            field_dict["AsFoundRawValue27"] = as_found_raw_value_27
        if as_found_raw_value_28 is not UNSET:
            field_dict["AsFoundRawValue28"] = as_found_raw_value_28
        if as_found_raw_value_29 is not UNSET:
            field_dict["AsFoundRawValue29"] = as_found_raw_value_29
        if as_found_raw_value_30 is not UNSET:
            field_dict["AsFoundRawValue30"] = as_found_raw_value_30
        if as_found_raw_value_31 is not UNSET:
            field_dict["AsFoundRawValue31"] = as_found_raw_value_31
        if as_found_raw_value_32 is not UNSET:
            field_dict["AsFoundRawValue32"] = as_found_raw_value_32
        if as_found_raw_value_33 is not UNSET:
            field_dict["AsFoundRawValue33"] = as_found_raw_value_33
        if as_found_raw_value_34 is not UNSET:
            field_dict["AsFoundRawValue34"] = as_found_raw_value_34
        if as_found_raw_value_35 is not UNSET:
            field_dict["AsFoundRawValue35"] = as_found_raw_value_35
        if as_found_raw_value_36 is not UNSET:
            field_dict["AsFoundRawValue36"] = as_found_raw_value_36
        if as_found_raw_value_37 is not UNSET:
            field_dict["AsFoundRawValue37"] = as_found_raw_value_37
        if as_found_raw_value_38 is not UNSET:
            field_dict["AsFoundRawValue38"] = as_found_raw_value_38
        if as_found_raw_value_39 is not UNSET:
            field_dict["AsFoundRawValue39"] = as_found_raw_value_39
        if as_found_raw_value_40 is not UNSET:
            field_dict["AsFoundRawValue40"] = as_found_raw_value_40
        if as_found_value_subtitle_1 is not UNSET:
            field_dict["AsFoundValueSubtitle1"] = as_found_value_subtitle_1
        if as_found_value_subtitle_2 is not UNSET:
            field_dict["AsFoundValueSubtitle2"] = as_found_value_subtitle_2
        if as_found_value_subtitle_3 is not UNSET:
            field_dict["AsFoundValueSubtitle3"] = as_found_value_subtitle_3
        if as_found_value_subtitle_4 is not UNSET:
            field_dict["AsFoundValueSubtitle4"] = as_found_value_subtitle_4
        if as_found_value_subtitle_5 is not UNSET:
            field_dict["AsFoundValueSubtitle5"] = as_found_value_subtitle_5
        if as_found_value_subtitle_6 is not UNSET:
            field_dict["AsFoundValueSubtitle6"] = as_found_value_subtitle_6
        if as_found_value_subtitle_7 is not UNSET:
            field_dict["AsFoundValueSubtitle7"] = as_found_value_subtitle_7
        if as_found_value_subtitle_8 is not UNSET:
            field_dict["AsFoundValueSubtitle8"] = as_found_value_subtitle_8
        if as_found_value_subtitle_9 is not UNSET:
            field_dict["AsFoundValueSubtitle9"] = as_found_value_subtitle_9
        if as_found_value_subtitle_10 is not UNSET:
            field_dict["AsFoundValueSubtitle10"] = as_found_value_subtitle_10
        if as_found_value_subtitle_11 is not UNSET:
            field_dict["AsFoundValueSubtitle11"] = as_found_value_subtitle_11
        if as_found_value_subtitle_12 is not UNSET:
            field_dict["AsFoundValueSubtitle12"] = as_found_value_subtitle_12
        if as_found_value_subtitle_13 is not UNSET:
            field_dict["AsFoundValueSubtitle13"] = as_found_value_subtitle_13
        if as_found_value_subtitle_14 is not UNSET:
            field_dict["AsFoundValueSubtitle14"] = as_found_value_subtitle_14
        if as_found_value_subtitle_15 is not UNSET:
            field_dict["AsFoundValueSubtitle15"] = as_found_value_subtitle_15
        if as_found_value_subtitle_16 is not UNSET:
            field_dict["AsFoundValueSubtitle16"] = as_found_value_subtitle_16
        if as_found_value_subtitle_17 is not UNSET:
            field_dict["AsFoundValueSubtitle17"] = as_found_value_subtitle_17
        if as_found_value_subtitle_18 is not UNSET:
            field_dict["AsFoundValueSubtitle18"] = as_found_value_subtitle_18
        if as_found_value_subtitle_19 is not UNSET:
            field_dict["AsFoundValueSubtitle19"] = as_found_value_subtitle_19
        if as_found_value_subtitle_20 is not UNSET:
            field_dict["AsFoundValueSubtitle20"] = as_found_value_subtitle_20
        if as_found_value_subtitle_21 is not UNSET:
            field_dict["AsFoundValueSubtitle21"] = as_found_value_subtitle_21
        if as_found_value_subtitle_22 is not UNSET:
            field_dict["AsFoundValueSubtitle22"] = as_found_value_subtitle_22
        if as_found_value_subtitle_23 is not UNSET:
            field_dict["AsFoundValueSubtitle23"] = as_found_value_subtitle_23
        if as_found_value_subtitle_24 is not UNSET:
            field_dict["AsFoundValueSubtitle24"] = as_found_value_subtitle_24
        if as_found_value_subtitle_25 is not UNSET:
            field_dict["AsFoundValueSubtitle25"] = as_found_value_subtitle_25
        if as_found_value_subtitle_26 is not UNSET:
            field_dict["AsFoundValueSubtitle26"] = as_found_value_subtitle_26
        if as_found_value_subtitle_27 is not UNSET:
            field_dict["AsFoundValueSubtitle27"] = as_found_value_subtitle_27
        if as_found_value_subtitle_28 is not UNSET:
            field_dict["AsFoundValueSubtitle28"] = as_found_value_subtitle_28
        if as_found_value_subtitle_29 is not UNSET:
            field_dict["AsFoundValueSubtitle29"] = as_found_value_subtitle_29
        if as_found_value_subtitle_30 is not UNSET:
            field_dict["AsFoundValueSubtitle30"] = as_found_value_subtitle_30
        if as_found_value_subtitle_31 is not UNSET:
            field_dict["AsFoundValueSubtitle31"] = as_found_value_subtitle_31
        if as_found_value_subtitle_32 is not UNSET:
            field_dict["AsFoundValueSubtitle32"] = as_found_value_subtitle_32
        if as_found_value_subtitle_33 is not UNSET:
            field_dict["AsFoundValueSubtitle33"] = as_found_value_subtitle_33
        if as_found_value_subtitle_34 is not UNSET:
            field_dict["AsFoundValueSubtitle34"] = as_found_value_subtitle_34
        if as_found_value_subtitle_35 is not UNSET:
            field_dict["AsFoundValueSubtitle35"] = as_found_value_subtitle_35
        if as_found_value_subtitle_36 is not UNSET:
            field_dict["AsFoundValueSubtitle36"] = as_found_value_subtitle_36
        if as_found_value_subtitle_37 is not UNSET:
            field_dict["AsFoundValueSubtitle37"] = as_found_value_subtitle_37
        if as_found_value_subtitle_38 is not UNSET:
            field_dict["AsFoundValueSubtitle38"] = as_found_value_subtitle_38
        if as_found_value_subtitle_39 is not UNSET:
            field_dict["AsFoundValueSubtitle39"] = as_found_value_subtitle_39
        if as_found_value_subtitle_40 is not UNSET:
            field_dict["AsFoundValueSubtitle40"] = as_found_value_subtitle_40
        if as_found_mean is not UNSET:
            field_dict["AsFoundMean"] = as_found_mean
        if as_found_mean_raw is not UNSET:
            field_dict["AsFoundMeanRaw"] = as_found_mean_raw
        if as_found_sd is not UNSET:
            field_dict["AsFoundSd"] = as_found_sd
        if as_found_sd_raw is not UNSET:
            field_dict["AsFoundSdRaw"] = as_found_sd_raw
        if as_found_delta is not UNSET:
            field_dict["AsFoundDelta"] = as_found_delta
        if as_found_range is not UNSET:
            field_dict["AsFoundRange"] = as_found_range
        if as_found_cv is not UNSET:
            field_dict["AsFoundCv"] = as_found_cv
        if as_found_cv_raw is not UNSET:
            field_dict["AsFoundCvRaw"] = as_found_cv_raw
        if as_found_result is not UNSET:
            field_dict["AsFoundResult"] = as_found_result
        if as_found_range_result is not UNSET:
            field_dict["AsFoundRangeResult"] = as_found_range_result
        if as_found_delta_result is not UNSET:
            field_dict["AsFoundDeltaResult"] = as_found_delta_result
        if as_found_min_result is not UNSET:
            field_dict["AsFoundMinResult"] = as_found_min_result
        if as_found_max_result is not UNSET:
            field_dict["AsFoundMaxResult"] = as_found_max_result
        if as_found_tar_result is not UNSET:
            field_dict["AsFoundTarResult"] = as_found_tar_result
        if as_found_tur_result is not UNSET:
            field_dict["AsFoundTurResult"] = as_found_tur_result
        if as_found_error_result is not UNSET:
            field_dict["AsFoundErrorResult"] = as_found_error_result
        if as_found_sd_result is not UNSET:
            field_dict["AsFoundSdResult"] = as_found_sd_result
        if as_found_cv_result is not UNSET:
            field_dict["AsFoundCvResult"] = as_found_cv_result
        if as_found_custom_field_result is not UNSET:
            field_dict["AsFoundCustomFieldResult"] = as_found_custom_field_result
        if as_found_mu is not UNSET:
            field_dict["AsFoundMu"] = as_found_mu
        if as_found_mu_raw is not UNSET:
            field_dict["AsFoundMuRaw"] = as_found_mu_raw
        if as_found_mu_effective_dof is not UNSET:
            field_dict["AsFoundMuEffectiveDOF"] = as_found_mu_effective_dof
        if as_found_mu_coverage_factor is not UNSET:
            field_dict["AsFoundMUCoverageFactor"] = as_found_mu_coverage_factor
        if as_found_cmc is not UNSET:
            field_dict["AsFoundCmc"] = as_found_cmc
        if as_found_cmc_comments is not UNSET:
            field_dict["AsFoundCmcComments"] = as_found_cmc_comments
        if as_found_calculated_uncertainty is not UNSET:
            field_dict["AsFoundCalculatedUncertainty"] = as_found_calculated_uncertainty
        if as_found_lab_mu is not UNSET:
            field_dict["AsFoundLabMu"] = as_found_lab_mu
        if as_found_uncertainty_budget is not UNSET:
            field_dict["AsFoundUncertaintyBudget"] = as_found_uncertainty_budget
        if as_found_mu_extended is not UNSET:
            field_dict["AsFoundMuExtended"] = as_found_mu_extended
        if as_found_channel is not UNSET:
            field_dict["AsFoundChannel"] = as_found_channel
        if as_found_measurement_type is not UNSET:
            field_dict["AsFoundMeasurementType"] = as_found_measurement_type
        if as_found_updated_by is not UNSET:
            field_dict["AsFoundUpdatedBy"] = as_found_updated_by
        if as_found_updated_on is not UNSET:
            field_dict["AsFoundUpdatedOn"] = as_found_updated_on
        if as_left_abbreviated_uom is not UNSET:
            field_dict["AsLeftAbbreviatedUOM"] = as_left_abbreviated_uom
        if as_left_unit_scale_factor is not UNSET:
            field_dict["AsLeftUnitScaleFactor"] = as_left_unit_scale_factor
        if as_found_specification_title is not UNSET:
            field_dict["AsFoundSpecificationTitle"] = as_found_specification_title
        if as_found_specification_subtitle is not UNSET:
            field_dict["AsFoundSpecificationSubtitle"] = as_found_specification_subtitle
        if as_found_specification_group is not UNSET:
            field_dict["AsFoundSpecificationGroup"] = as_found_specification_group
        if as_found_batch_type is not UNSET:
            field_dict["AsFoundBatchType"] = as_found_batch_type
        if as_found_batch_result is not UNSET:
            field_dict["AsFoundBatchResult"] = as_found_batch_result
        if as_found_is_by_channel is not UNSET:
            field_dict["AsFoundIsByChannel"] = as_found_is_by_channel
        if as_found_channel_count is not UNSET:
            field_dict["AsFoundChannelCount"] = as_found_channel_count
        if as_found_commenced_on is not UNSET:
            field_dict["AsFoundCommencedOn"] = as_found_commenced_on
        if as_found_commenced_by is not UNSET:
            field_dict["AsFoundCommencedBy"] = as_found_commenced_by
        if as_found_z_factor is not UNSET:
            field_dict["AsFoundZFactor"] = as_found_z_factor
        if as_found_air_buoyancy is not UNSET:
            field_dict["AsFoundAirBuoyancy"] = as_found_air_buoyancy
        if as_found_evaporation_rate is not UNSET:
            field_dict["AsFoundEvaporationRate"] = as_found_evaporation_rate
        if as_found_ambient_temperature is not UNSET:
            field_dict["AsFoundAmbientTemperature"] = as_found_ambient_temperature
        if as_found_air_humidity is not UNSET:
            field_dict["AsFoundAirHumidity"] = as_found_air_humidity
        if as_found_barometric_pressure is not UNSET:
            field_dict["AsFoundBarometricPressure"] = as_found_barometric_pressure
        if as_found_altitude is not UNSET:
            field_dict["AsFoundAltitude"] = as_found_altitude
        if as_found_wind_speed is not UNSET:
            field_dict["AsFoundWindSpeed"] = as_found_wind_speed
        if as_found_solar_radiation is not UNSET:
            field_dict["AsFoundSolarRadiation"] = as_found_solar_radiation
        if as_found_light_intensity is not UNSET:
            field_dict["AsFoundLightIntensity"] = as_found_light_intensity
        if as_found_noise_level is not UNSET:
            field_dict["AsFoundNoiseLevel"] = as_found_noise_level
        if as_found_ph_level is not UNSET:
            field_dict["AsFoundPhLevel"] = as_found_ph_level
        if as_found_water_conductivity is not UNSET:
            field_dict["AsFoundWaterConductivity"] = as_found_water_conductivity
        if as_found_water_temperature is not UNSET:
            field_dict["AsFoundWaterTemperature"] = as_found_water_temperature
        if as_found_z_factor_uom is not UNSET:
            field_dict["AsFoundZFactorUom"] = as_found_z_factor_uom
        if as_found_air_buoyancy_uom is not UNSET:
            field_dict["AsFoundAirBuoyancyUom"] = as_found_air_buoyancy_uom
        if as_found_evaporation_rate_uom is not UNSET:
            field_dict["AsFoundEvaporationRateUom"] = as_found_evaporation_rate_uom
        if as_found_ambient_temperature_uom is not UNSET:
            field_dict["AsFoundAmbientTemperatureUom"] = (
                as_found_ambient_temperature_uom
            )
        if as_found_air_humidity_uom is not UNSET:
            field_dict["AsFoundAirHumidityUom"] = as_found_air_humidity_uom
        if as_found_barometric_pressure_uom is not UNSET:
            field_dict["AsFoundBarometricPressureUom"] = (
                as_found_barometric_pressure_uom
            )
        if as_found_altitude_uom is not UNSET:
            field_dict["AsFoundAltitudeUom"] = as_found_altitude_uom
        if as_found_wind_speed_uom is not UNSET:
            field_dict["AsFoundWindSpeedUom"] = as_found_wind_speed_uom
        if as_found_solar_radiation_uom is not UNSET:
            field_dict["AsFoundSolarRadiationUom"] = as_found_solar_radiation_uom
        if as_found_light_intensity_uom is not UNSET:
            field_dict["AsFoundLightIntensityUom"] = as_found_light_intensity_uom
        if as_found_noise_level_uom is not UNSET:
            field_dict["AsFoundNoiseLevelUom"] = as_found_noise_level_uom
        if as_found_ph_level_uom is not UNSET:
            field_dict["AsFoundPhLevelUom"] = as_found_ph_level_uom
        if as_found_water_conductivity_uom is not UNSET:
            field_dict["AsFoundWaterConductivityUom"] = as_found_water_conductivity_uom
        if as_found_water_temperature_uom is not UNSET:
            field_dict["AsFoundWaterTemperatureUom"] = as_found_water_temperature_uom
        if as_found_abbreviated_uom is not UNSET:
            field_dict["AsFoundAbbreviatedUOM"] = as_found_abbreviated_uom
        if as_found_unit_scale_factor is not UNSET:
            field_dict["AsFoundUnitScaleFactor"] = as_found_unit_scale_factor
        if as_found_specification_name is not UNSET:
            field_dict["AsFoundSpecificationName"] = as_found_specification_name
        if as_found_parameter_name is not UNSET:
            field_dict["AsFoundParameterName"] = as_found_parameter_name
        if as_found_display_order is not UNSET:
            field_dict["AsFoundDisplayOrder"] = as_found_display_order
        if as_found_unit_of_measure is not UNSET:
            field_dict["AsFoundUnitOfMeasure"] = as_found_unit_of_measure
        if as_found_display_format is not UNSET:
            field_dict["AsFoundDisplayFormat"] = as_found_display_format
        if as_found_precision is not UNSET:
            field_dict["AsFoundPrecision"] = as_found_precision
        if as_found_precision_type is not UNSET:
            field_dict["AsFoundPrecisionType"] = as_found_precision_type
        if as_found_minimum is not UNSET:
            field_dict["AsFoundMinimum"] = as_found_minimum
        if as_found_nominal is not UNSET:
            field_dict["AsFoundNominal"] = as_found_nominal
        if as_found_expected_value is not UNSET:
            field_dict["AsFoundExpectedValue"] = as_found_expected_value
        if as_found_expected_value_raw is not UNSET:
            field_dict["AsFoundExpectedValueRaw"] = as_found_expected_value_raw
        if as_found_test_value is not UNSET:
            field_dict["AsFoundTestValue"] = as_found_test_value
        if as_found_base_value is not UNSET:
            field_dict["AsFoundBaseValue"] = as_found_base_value
        if as_found_maxi_mum is not UNSET:
            field_dict["AsFoundMaxiMum"] = as_found_maxi_mum
        if as_found_resolution is not UNSET:
            field_dict["AsFoundResolution"] = as_found_resolution
        if as_found_resolution_count is not UNSET:
            field_dict["AsFoundResolutionCount"] = as_found_resolution_count
        if as_found_measurement_batch_id is not UNSET:
            field_dict["AsFoundMeasurementBatchId"] = as_found_measurement_batch_id
        if as_found_measurement_id is not UNSET:
            field_dict["AsFoundMeasurementId"] = as_found_measurement_id
        if as_found_standard_id is not UNSET:
            field_dict["AsFoundStandardId"] = as_found_standard_id
        if as_found_tool_id is not UNSET:
            field_dict["AsFoundToolId"] = as_found_tool_id
        if as_found_measurement_condition_id is not UNSET:
            field_dict["AsFoundMeasurementConditionId"] = (
                as_found_measurement_condition_id
            )
        if as_found_measurement_point_id is not UNSET:
            field_dict["AsFoundMeasurementPointId"] = as_found_measurement_point_id
        if as_left_parameter_id is not UNSET:
            field_dict["AsLeftParameterId"] = as_left_parameter_id
        if as_left_sd_header is not UNSET:
            field_dict["AsLeftSdHeader"] = as_left_sd_header
        if as_left_cv_header is not UNSET:
            field_dict["AsLeftCvHeader"] = as_left_cv_header
        if as_left_measurement_local_time is not UNSET:
            field_dict["AsLeftMeasurementLocalTime"] = as_left_measurement_local_time
        if as_left_reading_entry_math is not UNSET:
            field_dict["AsLeftReadingEntryMath"] = as_left_reading_entry_math
        if as_left_reading_entry_math_string is not UNSET:
            field_dict["AsLeftReadingEntryMathString"] = (
                as_left_reading_entry_math_string
            )
        if as_left_value_1 is not UNSET:
            field_dict["AsLeftValue1"] = as_left_value_1
        if as_left_value_2 is not UNSET:
            field_dict["AsLeftValue2"] = as_left_value_2
        if as_left_value_3 is not UNSET:
            field_dict["AsLeftValue3"] = as_left_value_3
        if as_left_value_4 is not UNSET:
            field_dict["AsLeftValue4"] = as_left_value_4
        if as_left_value_5 is not UNSET:
            field_dict["AsLeftValue5"] = as_left_value_5
        if as_left_value_6 is not UNSET:
            field_dict["AsLeftValue6"] = as_left_value_6
        if as_left_value_7 is not UNSET:
            field_dict["AsLeftValue7"] = as_left_value_7
        if as_left_value_8 is not UNSET:
            field_dict["AsLeftValue8"] = as_left_value_8
        if as_left_value_9 is not UNSET:
            field_dict["AsLeftValue9"] = as_left_value_9
        if as_left_value_10 is not UNSET:
            field_dict["AsLeftValue10"] = as_left_value_10
        if as_left_value_11 is not UNSET:
            field_dict["AsLeftValue11"] = as_left_value_11
        if as_left_value_12 is not UNSET:
            field_dict["AsLeftValue12"] = as_left_value_12
        if as_left_value_13 is not UNSET:
            field_dict["AsLeftValue13"] = as_left_value_13
        if as_left_value_14 is not UNSET:
            field_dict["AsLeftValue14"] = as_left_value_14
        if as_left_value_15 is not UNSET:
            field_dict["AsLeftValue15"] = as_left_value_15
        if as_left_value_16 is not UNSET:
            field_dict["AsLeftValue16"] = as_left_value_16
        if as_left_value_17 is not UNSET:
            field_dict["AsLeftValue17"] = as_left_value_17
        if as_left_value_18 is not UNSET:
            field_dict["AsLeftValue18"] = as_left_value_18
        if as_left_value_19 is not UNSET:
            field_dict["AsLeftValue19"] = as_left_value_19
        if as_left_value_20 is not UNSET:
            field_dict["AsLeftValue20"] = as_left_value_20
        if as_left_value_21 is not UNSET:
            field_dict["AsLeftValue21"] = as_left_value_21
        if as_left_value_22 is not UNSET:
            field_dict["AsLeftValue22"] = as_left_value_22
        if as_left_value_23 is not UNSET:
            field_dict["AsLeftValue23"] = as_left_value_23
        if as_left_value_24 is not UNSET:
            field_dict["AsLeftValue24"] = as_left_value_24
        if as_left_value_25 is not UNSET:
            field_dict["AsLeftValue25"] = as_left_value_25
        if as_left_value_26 is not UNSET:
            field_dict["AsLeftValue26"] = as_left_value_26
        if as_left_value_27 is not UNSET:
            field_dict["AsLeftValue27"] = as_left_value_27
        if as_left_value_28 is not UNSET:
            field_dict["AsLeftValue28"] = as_left_value_28
        if as_left_value_29 is not UNSET:
            field_dict["AsLeftValue29"] = as_left_value_29
        if as_left_value_30 is not UNSET:
            field_dict["AsLeftValue30"] = as_left_value_30
        if as_left_value_31 is not UNSET:
            field_dict["AsLeftValue31"] = as_left_value_31
        if as_left_value_32 is not UNSET:
            field_dict["AsLeftValue32"] = as_left_value_32
        if as_left_value_33 is not UNSET:
            field_dict["AsLeftValue33"] = as_left_value_33
        if as_left_value_34 is not UNSET:
            field_dict["AsLeftValue34"] = as_left_value_34
        if as_left_value_35 is not UNSET:
            field_dict["AsLeftValue35"] = as_left_value_35
        if as_left_value_36 is not UNSET:
            field_dict["AsLeftValue36"] = as_left_value_36
        if as_left_value_37 is not UNSET:
            field_dict["AsLeftValue37"] = as_left_value_37
        if as_left_value_38 is not UNSET:
            field_dict["AsLeftValue38"] = as_left_value_38
        if as_left_value_39 is not UNSET:
            field_dict["AsLeftValue39"] = as_left_value_39
        if as_left_value_40 is not UNSET:
            field_dict["AsLeftValue40"] = as_left_value_40
        if as_left_raw_value_1 is not UNSET:
            field_dict["AsLeftRawValue1"] = as_left_raw_value_1
        if as_left_raw_value_2 is not UNSET:
            field_dict["AsLeftRawValue2"] = as_left_raw_value_2
        if as_left_raw_value_3 is not UNSET:
            field_dict["AsLeftRawValue3"] = as_left_raw_value_3
        if as_left_raw_value_4 is not UNSET:
            field_dict["AsLeftRawValue4"] = as_left_raw_value_4
        if as_left_raw_value_5 is not UNSET:
            field_dict["AsLeftRawValue5"] = as_left_raw_value_5
        if as_left_raw_value_6 is not UNSET:
            field_dict["AsLeftRawValue6"] = as_left_raw_value_6
        if as_left_raw_value_7 is not UNSET:
            field_dict["AsLeftRawValue7"] = as_left_raw_value_7
        if as_left_raw_value_8 is not UNSET:
            field_dict["AsLeftRawValue8"] = as_left_raw_value_8
        if as_left_raw_value_9 is not UNSET:
            field_dict["AsLeftRawValue9"] = as_left_raw_value_9
        if as_left_raw_value_10 is not UNSET:
            field_dict["AsLeftRawValue10"] = as_left_raw_value_10
        if as_left_raw_value_11 is not UNSET:
            field_dict["AsLeftRawValue11"] = as_left_raw_value_11
        if as_left_raw_value_12 is not UNSET:
            field_dict["AsLeftRawValue12"] = as_left_raw_value_12
        if as_left_raw_value_13 is not UNSET:
            field_dict["AsLeftRawValue13"] = as_left_raw_value_13
        if as_left_raw_value_14 is not UNSET:
            field_dict["AsLeftRawValue14"] = as_left_raw_value_14
        if as_left_raw_value_15 is not UNSET:
            field_dict["AsLeftRawValue15"] = as_left_raw_value_15
        if as_left_raw_value_16 is not UNSET:
            field_dict["AsLeftRawValue16"] = as_left_raw_value_16
        if as_left_raw_value_17 is not UNSET:
            field_dict["AsLeftRawValue17"] = as_left_raw_value_17
        if as_left_raw_value_18 is not UNSET:
            field_dict["AsLeftRawValue18"] = as_left_raw_value_18
        if as_left_raw_value_19 is not UNSET:
            field_dict["AsLeftRawValue19"] = as_left_raw_value_19
        if as_left_raw_value_20 is not UNSET:
            field_dict["AsLeftRawValue20"] = as_left_raw_value_20
        if as_left_raw_value_21 is not UNSET:
            field_dict["AsLeftRawValue21"] = as_left_raw_value_21
        if as_left_raw_value_22 is not UNSET:
            field_dict["AsLeftRawValue22"] = as_left_raw_value_22
        if as_left_raw_value_23 is not UNSET:
            field_dict["AsLeftRawValue23"] = as_left_raw_value_23
        if as_left_raw_value_24 is not UNSET:
            field_dict["AsLeftRawValue24"] = as_left_raw_value_24
        if as_left_raw_value_25 is not UNSET:
            field_dict["AsLeftRawValue25"] = as_left_raw_value_25
        if as_left_raw_value_26 is not UNSET:
            field_dict["AsLeftRawValue26"] = as_left_raw_value_26
        if as_left_raw_value_27 is not UNSET:
            field_dict["AsLeftRawValue27"] = as_left_raw_value_27
        if as_left_raw_value_28 is not UNSET:
            field_dict["AsLeftRawValue28"] = as_left_raw_value_28
        if as_left_raw_value_29 is not UNSET:
            field_dict["AsLeftRawValue29"] = as_left_raw_value_29
        if as_left_raw_value_30 is not UNSET:
            field_dict["AsLeftRawValue30"] = as_left_raw_value_30
        if as_left_raw_value_31 is not UNSET:
            field_dict["AsLeftRawValue31"] = as_left_raw_value_31
        if as_left_raw_value_32 is not UNSET:
            field_dict["AsLeftRawValue32"] = as_left_raw_value_32
        if as_left_raw_value_33 is not UNSET:
            field_dict["AsLeftRawValue33"] = as_left_raw_value_33
        if as_left_raw_value_34 is not UNSET:
            field_dict["AsLeftRawValue34"] = as_left_raw_value_34
        if as_left_raw_value_35 is not UNSET:
            field_dict["AsLeftRawValue35"] = as_left_raw_value_35
        if as_left_raw_value_36 is not UNSET:
            field_dict["AsLeftRawValue36"] = as_left_raw_value_36
        if as_left_raw_value_37 is not UNSET:
            field_dict["AsLeftRawValue37"] = as_left_raw_value_37
        if as_left_raw_value_38 is not UNSET:
            field_dict["AsLeftRawValue38"] = as_left_raw_value_38
        if as_left_raw_value_39 is not UNSET:
            field_dict["AsLeftRawValue39"] = as_left_raw_value_39
        if as_left_raw_value_40 is not UNSET:
            field_dict["AsLeftRawValue40"] = as_left_raw_value_40
        if as_left_value_subtitle_1 is not UNSET:
            field_dict["AsLeftValueSubtitle1"] = as_left_value_subtitle_1
        if as_left_value_subtitle_2 is not UNSET:
            field_dict["AsLeftValueSubtitle2"] = as_left_value_subtitle_2
        if as_left_value_subtitle_3 is not UNSET:
            field_dict["AsLeftValueSubtitle3"] = as_left_value_subtitle_3
        if as_left_value_subtitle_4 is not UNSET:
            field_dict["AsLeftValueSubtitle4"] = as_left_value_subtitle_4
        if as_left_value_subtitle_5 is not UNSET:
            field_dict["AsLeftValueSubtitle5"] = as_left_value_subtitle_5
        if as_left_value_subtitle_6 is not UNSET:
            field_dict["AsLeftValueSubtitle6"] = as_left_value_subtitle_6
        if as_left_value_subtitle_7 is not UNSET:
            field_dict["AsLeftValueSubtitle7"] = as_left_value_subtitle_7
        if as_left_value_subtitle_8 is not UNSET:
            field_dict["AsLeftValueSubtitle8"] = as_left_value_subtitle_8
        if as_left_value_subtitle_9 is not UNSET:
            field_dict["AsLeftValueSubtitle9"] = as_left_value_subtitle_9
        if as_left_value_subtitle_10 is not UNSET:
            field_dict["AsLeftValueSubtitle10"] = as_left_value_subtitle_10
        if as_left_value_subtitle_11 is not UNSET:
            field_dict["AsLeftValueSubtitle11"] = as_left_value_subtitle_11
        if as_left_value_subtitle_12 is not UNSET:
            field_dict["AsLeftValueSubtitle12"] = as_left_value_subtitle_12
        if as_left_value_subtitle_13 is not UNSET:
            field_dict["AsLeftValueSubtitle13"] = as_left_value_subtitle_13
        if as_left_value_subtitle_14 is not UNSET:
            field_dict["AsLeftValueSubtitle14"] = as_left_value_subtitle_14
        if as_left_value_subtitle_15 is not UNSET:
            field_dict["AsLeftValueSubtitle15"] = as_left_value_subtitle_15
        if as_left_value_subtitle_16 is not UNSET:
            field_dict["AsLeftValueSubtitle16"] = as_left_value_subtitle_16
        if as_left_value_subtitle_17 is not UNSET:
            field_dict["AsLeftValueSubtitle17"] = as_left_value_subtitle_17
        if as_left_value_subtitle_18 is not UNSET:
            field_dict["AsLeftValueSubtitle18"] = as_left_value_subtitle_18
        if as_left_value_subtitle_19 is not UNSET:
            field_dict["AsLeftValueSubtitle19"] = as_left_value_subtitle_19
        if as_left_value_subtitle_20 is not UNSET:
            field_dict["AsLeftValueSubtitle20"] = as_left_value_subtitle_20
        if as_left_value_subtitle_21 is not UNSET:
            field_dict["AsLeftValueSubtitle21"] = as_left_value_subtitle_21
        if as_left_value_subtitle_22 is not UNSET:
            field_dict["AsLeftValueSubtitle22"] = as_left_value_subtitle_22
        if as_left_value_subtitle_23 is not UNSET:
            field_dict["AsLeftValueSubtitle23"] = as_left_value_subtitle_23
        if as_left_value_subtitle_24 is not UNSET:
            field_dict["AsLeftValueSubtitle24"] = as_left_value_subtitle_24
        if as_left_value_subtitle_25 is not UNSET:
            field_dict["AsLeftValueSubtitle25"] = as_left_value_subtitle_25
        if as_left_value_subtitle_26 is not UNSET:
            field_dict["AsLeftValueSubtitle26"] = as_left_value_subtitle_26
        if as_left_value_subtitle_27 is not UNSET:
            field_dict["AsLeftValueSubtitle27"] = as_left_value_subtitle_27
        if as_left_value_subtitle_28 is not UNSET:
            field_dict["AsLeftValueSubtitle28"] = as_left_value_subtitle_28
        if as_left_value_subtitle_29 is not UNSET:
            field_dict["AsLeftValueSubtitle29"] = as_left_value_subtitle_29
        if as_left_value_subtitle_30 is not UNSET:
            field_dict["AsLeftValueSubtitle30"] = as_left_value_subtitle_30
        if as_left_value_subtitle_31 is not UNSET:
            field_dict["AsLeftValueSubtitle31"] = as_left_value_subtitle_31
        if as_left_value_subtitle_32 is not UNSET:
            field_dict["AsLeftValueSubtitle32"] = as_left_value_subtitle_32
        if as_left_value_subtitle_33 is not UNSET:
            field_dict["AsLeftValueSubtitle33"] = as_left_value_subtitle_33
        if as_left_value_subtitle_34 is not UNSET:
            field_dict["AsLeftValueSubtitle34"] = as_left_value_subtitle_34
        if as_left_value_subtitle_35 is not UNSET:
            field_dict["AsLeftValueSubtitle35"] = as_left_value_subtitle_35
        if as_left_value_subtitle_36 is not UNSET:
            field_dict["AsLeftValueSubtitle36"] = as_left_value_subtitle_36
        if as_left_value_subtitle_37 is not UNSET:
            field_dict["AsLeftValueSubtitle37"] = as_left_value_subtitle_37
        if as_left_value_subtitle_38 is not UNSET:
            field_dict["AsLeftValueSubtitle38"] = as_left_value_subtitle_38
        if as_left_value_subtitle_39 is not UNSET:
            field_dict["AsLeftValueSubtitle39"] = as_left_value_subtitle_39
        if as_left_value_subtitle_40 is not UNSET:
            field_dict["AsLeftValueSubtitle40"] = as_left_value_subtitle_40
        if as_left_mean is not UNSET:
            field_dict["AsLeftMean"] = as_left_mean
        if as_left_mean_raw is not UNSET:
            field_dict["AsLeftMeanRaw"] = as_left_mean_raw
        if as_left_sd is not UNSET:
            field_dict["AsLeftSd"] = as_left_sd
        if as_left_sd_raw is not UNSET:
            field_dict["AsLeftSdRaw"] = as_left_sd_raw
        if as_left_cv is not UNSET:
            field_dict["AsLeftCv"] = as_left_cv
        if as_left_cv_raw is not UNSET:
            field_dict["AsLeftCvRaw"] = as_left_cv_raw
        if as_left_delta is not UNSET:
            field_dict["AsLeftDelta"] = as_left_delta
        if as_left_range is not UNSET:
            field_dict["AsLeftRange"] = as_left_range
        if as_left_result is not UNSET:
            field_dict["AsLeftResult"] = as_left_result
        if as_left_range_result is not UNSET:
            field_dict["AsLeftRangeResult"] = as_left_range_result
        if as_left_delta_result is not UNSET:
            field_dict["AsLeftDeltaResult"] = as_left_delta_result
        if as_left_min_result is not UNSET:
            field_dict["AsLeftMinResult"] = as_left_min_result
        if as_left_max_result is not UNSET:
            field_dict["AsLeftMaxResult"] = as_left_max_result
        if as_left_tar_result is not UNSET:
            field_dict["AsLeftTarResult"] = as_left_tar_result
        if as_left_tur_result is not UNSET:
            field_dict["AsLeftTurResult"] = as_left_tur_result
        if as_left_error_result is not UNSET:
            field_dict["AsLeftErrorResult"] = as_left_error_result
        if as_left_sd_result is not UNSET:
            field_dict["AsLeftSdResult"] = as_left_sd_result
        if as_left_cv_result is not UNSET:
            field_dict["AsLeftCvResult"] = as_left_cv_result
        if as_left_custom_field_result is not UNSET:
            field_dict["AsLeftCustomFieldResult"] = as_left_custom_field_result
        if as_left_mu is not UNSET:
            field_dict["AsLeftMu"] = as_left_mu
        if as_left_mu_raw is not UNSET:
            field_dict["AsLeftMuRaw"] = as_left_mu_raw
        if as_left_mu_effective_dof is not UNSET:
            field_dict["AsLeftMUEffectiveDOF"] = as_left_mu_effective_dof
        if as_left_mu_coverage_factor is not UNSET:
            field_dict["AsLeftMUCoverageFactor"] = as_left_mu_coverage_factor
        if as_left_cmc is not UNSET:
            field_dict["AsLeftCmc"] = as_left_cmc
        if as_left_cmc_comments is not UNSET:
            field_dict["AsLeftCmcComments"] = as_left_cmc_comments
        if as_left_calculated_uncertainty is not UNSET:
            field_dict["AsLeftCalculatedUncertainty"] = as_left_calculated_uncertainty
        if as_left_lab_mu is not UNSET:
            field_dict["AsLeftLabMu"] = as_left_lab_mu
        if as_left_uncertainty_budget is not UNSET:
            field_dict["AsLeftUncertaintyBudget"] = as_left_uncertainty_budget
        if as_left_mu_extended is not UNSET:
            field_dict["AsLeftMuExtended"] = as_left_mu_extended
        if as_left_channel is not UNSET:
            field_dict["AsLeftChannel"] = as_left_channel
        if as_left_measurement_type is not UNSET:
            field_dict["AsLeftMeasurementType"] = as_left_measurement_type
        if as_left_updated_by is not UNSET:
            field_dict["AsLeftUpdatedBy"] = as_left_updated_by
        if as_left_updated_on is not UNSET:
            field_dict["AsLeftUpdatedOn"] = as_left_updated_on
        if as_left_specification_title is not UNSET:
            field_dict["AsLeftSpecificationTitle"] = as_left_specification_title
        if as_left_specification_subtitle is not UNSET:
            field_dict["AsLeftSpecificationSubtitle"] = as_left_specification_subtitle
        if as_left_specification_group is not UNSET:
            field_dict["AsLeftSpecificationGroup"] = as_left_specification_group
        if as_left_batch_type is not UNSET:
            field_dict["AsLeftBatchType"] = as_left_batch_type
        if as_left_batch_result is not UNSET:
            field_dict["AsLeftBatchResult"] = as_left_batch_result
        if as_left_is_by_channel is not UNSET:
            field_dict["AsLeftIsByChannel"] = as_left_is_by_channel
        if as_left_channel_count is not UNSET:
            field_dict["AsLeftChannelCount"] = as_left_channel_count
        if as_left_commenced_on is not UNSET:
            field_dict["AsLeftCommencedOn"] = as_left_commenced_on
        if as_left_commenced_by is not UNSET:
            field_dict["AsLeftCommencedBy"] = as_left_commenced_by
        if as_left_z_factor is not UNSET:
            field_dict["AsLeftZFactor"] = as_left_z_factor
        if as_left_air_buoyancy is not UNSET:
            field_dict["AsLeftAirBuoyancy"] = as_left_air_buoyancy
        if as_left_evaporation_rate is not UNSET:
            field_dict["AsLeftEvaporationRate"] = as_left_evaporation_rate
        if as_left_ambient_temperature is not UNSET:
            field_dict["AsLeftAmbientTemperature"] = as_left_ambient_temperature
        if as_left_air_humidity is not UNSET:
            field_dict["AsLeftAirHumidity"] = as_left_air_humidity
        if as_left_barometric_pressure is not UNSET:
            field_dict["AsLeftBarometricPressure"] = as_left_barometric_pressure
        if as_left_altitude is not UNSET:
            field_dict["AsLeftAltitude"] = as_left_altitude
        if as_left_wind_speed is not UNSET:
            field_dict["AsLeftWindSpeed"] = as_left_wind_speed
        if as_left_solar_radiation is not UNSET:
            field_dict["AsLeftSolarRadiation"] = as_left_solar_radiation
        if as_left_light_intensity is not UNSET:
            field_dict["AsLeftLightIntensity"] = as_left_light_intensity
        if as_left_noise_level is not UNSET:
            field_dict["AsLeftNoiseLevel"] = as_left_noise_level
        if as_left_ph_level is not UNSET:
            field_dict["AsLeftPhLevel"] = as_left_ph_level
        if as_left_water_conductivity is not UNSET:
            field_dict["AsLeftWaterConductivity"] = as_left_water_conductivity
        if as_left_water_temperature is not UNSET:
            field_dict["AsLeftWaterTemperature"] = as_left_water_temperature
        if as_left_z_factor_uom is not UNSET:
            field_dict["AsLeftZFactorUom"] = as_left_z_factor_uom
        if as_left_air_buoyancy_uom is not UNSET:
            field_dict["AsLeftAirBuoyancyUom"] = as_left_air_buoyancy_uom
        if as_left_evaporation_rate_uom is not UNSET:
            field_dict["AsLeftEvaporationRateUom"] = as_left_evaporation_rate_uom
        if as_left_ambient_temperature_uom is not UNSET:
            field_dict["AsLeftAmbientTemperatureUom"] = as_left_ambient_temperature_uom
        if as_left_air_humidity_uom is not UNSET:
            field_dict["AsLeftAirHumidityUom"] = as_left_air_humidity_uom
        if as_left_barometric_pressure_uom is not UNSET:
            field_dict["AsLeftBarometricPressureUom"] = as_left_barometric_pressure_uom
        if as_left_altitude_uom is not UNSET:
            field_dict["AsLeftAltitudeUom"] = as_left_altitude_uom
        if as_left_wind_speed_uom is not UNSET:
            field_dict["AsLeftWindSpeedUom"] = as_left_wind_speed_uom
        if as_left_solar_radiation_uom is not UNSET:
            field_dict["AsLeftSolarRadiationUom"] = as_left_solar_radiation_uom
        if as_left_light_intensity_uom is not UNSET:
            field_dict["AsLeftLightIntensityUom"] = as_left_light_intensity_uom
        if as_left_noise_level_uom is not UNSET:
            field_dict["AsLeftNoiseLevelUom"] = as_left_noise_level_uom
        if as_left_ph_level_uom is not UNSET:
            field_dict["AsLeftPhLevelUom"] = as_left_ph_level_uom
        if as_left_water_conductivity_uom is not UNSET:
            field_dict["AsLeftWaterConductivityUom"] = as_left_water_conductivity_uom
        if as_left_water_temperature_uom is not UNSET:
            field_dict["AsLeftWaterTemperatureUom"] = as_left_water_temperature_uom
        if as_left_specification_name is not UNSET:
            field_dict["AsLeftSpecificationName"] = as_left_specification_name
        if as_left_parameter_name is not UNSET:
            field_dict["AsLeftParameterName"] = as_left_parameter_name
        if as_left_display_order is not UNSET:
            field_dict["AsLeftDisplayOrder"] = as_left_display_order
        if as_left_unit_of_measure is not UNSET:
            field_dict["AsLeftUnitOfMeasure"] = as_left_unit_of_measure
        if as_left_display_format is not UNSET:
            field_dict["AsLeftDisplayFormat"] = as_left_display_format
        if as_left_precision is not UNSET:
            field_dict["AsLeftPrecision"] = as_left_precision
        if as_left_precision_type is not UNSET:
            field_dict["AsLeftPrecisionType"] = as_left_precision_type
        if as_left_minimum is not UNSET:
            field_dict["AsLeftMinimum"] = as_left_minimum
        if as_left_nominal is not UNSET:
            field_dict["AsLeftNominal"] = as_left_nominal
        if as_left_expected_value is not UNSET:
            field_dict["AsLeftExpectedValue"] = as_left_expected_value
        if as_left_expected_value_raw is not UNSET:
            field_dict["AsLeftExpectedValueRaw"] = as_left_expected_value_raw
        if as_left_test_value is not UNSET:
            field_dict["AsLeftTestValue"] = as_left_test_value
        if as_left_base_value is not UNSET:
            field_dict["AsLeftBaseValue"] = as_left_base_value
        if as_left_maxi_mum is not UNSET:
            field_dict["AsLeftMaxiMum"] = as_left_maxi_mum
        if as_left_resolution is not UNSET:
            field_dict["AsLeftResolution"] = as_left_resolution
        if as_left_resolution_count is not UNSET:
            field_dict["AsLeftResolutionCount"] = as_left_resolution_count
        if as_left_measurement_not_taken_result is not UNSET:
            field_dict["AsLeftMeasurementNotTakenResult"] = (
                as_left_measurement_not_taken_result
            )
        if as_left_hide_from_certificate is not UNSET:
            field_dict["AsLeftHideFromCertificate"] = as_left_hide_from_certificate
        if as_left_measurement_not_taken_reason is not UNSET:
            field_dict["AsLeftMeasurementNotTakenReason"] = (
                as_left_measurement_not_taken_reason
            )
        if as_left_measurement_batch_id is not UNSET:
            field_dict["AsLeftMeasurementBatchId"] = as_left_measurement_batch_id
        if as_left_measurement_id is not UNSET:
            field_dict["AsLeftMeasurementId"] = as_left_measurement_id
        if as_left_standard_id is not UNSET:
            field_dict["AsLeftStandardId"] = as_left_standard_id
        if as_left_tool_id is not UNSET:
            field_dict["AsLeftToolId"] = as_left_tool_id
        if as_left_measurement_condition_id is not UNSET:
            field_dict["AsLeftMeasurementConditionId"] = (
                as_left_measurement_condition_id
            )
        if as_left_measurement_point_id is not UNSET:
            field_dict["AsLeftMeasurementPointId"] = as_left_measurement_point_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        barcode = d.pop("Barcode", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        display_part_number = d.pop("DisplayPartNumber", UNSET)

        part_number = d.pop("PartNumber", UNSET)

        vendor_company_id = d.pop("VendorCompanyId", UNSET)

        service_order_number = d.pop("ServiceOrderNumber", UNSET)

        completed_by_name = d.pop("CompletedByName", UNSET)

        _completed_on = d.pop("CompletedOn", UNSET)
        completed_on: Union[Unset, datetime.datetime]
        if isinstance(_completed_on, Unset):
            completed_on = UNSET
        else:
            if _completed_on is None:

                completed_on = None

            else:

                completed_on = isoparse(_completed_on)

        is_limited = d.pop("IsLimited", UNSET)

        vendor_tag = d.pop("VendorTag", UNSET)

        room = d.pop("Room", UNSET)

        segment_name = d.pop("SegmentName", UNSET)

        schedule_name = d.pop("ScheduleName", UNSET)

        next_segment_name = d.pop("NextSegmentName", UNSET)

        certificate_number = d.pop("CertificateNumber", UNSET)

        work_status = d.pop("WorkStatus", UNSET)

        service_type = d.pop("ServiceType", UNSET)

        service_level = d.pop("ServiceLevel", UNSET)

        service_comments = d.pop("ServiceComments", UNSET)

        order_item_number = d.pop("OrderItemNumber", UNSET)

        service_total = d.pop("ServiceTotal", UNSET)

        repairs_total = d.pop("RepairsTotal", UNSET)

        parts_total = d.pop("PartsTotal", UNSET)

        asset_tag = d.pop("AssetTag", UNSET)

        asset_user = d.pop("AssetUser", UNSET)

        serial_number = d.pop("SerialNumber", UNSET)

        equipment_id = d.pop("EquipmentId", UNSET)

        legacy_identifier = d.pop("LegacyIdentifier", UNSET)

        asset_name = d.pop("AssetName", UNSET)

        asset_description = d.pop("AssetDescription", UNSET)

        product_name = d.pop("ProductName", UNSET)

        product_description = d.pop("ProductDescription", UNSET)

        asset_maker = d.pop("AssetMaker", UNSET)

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

        site_name = d.pop("SiteName", UNSET)

        po_number = d.pop("PoNumber", UNSET)

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

        tracking_number = d.pop("TrackingNumber", UNSET)

        payment_terms = d.pop("PaymentTerms", UNSET)

        shipping_method = d.pop("ShippingMethod", UNSET)

        location = d.pop("Location", UNSET)

        site_access_notes = d.pop("SiteAccessNotes", UNSET)

        as_left_decimal_places = d.pop("AsLeftDecimalPlaces", UNSET)

        as_left_measurement_set_name = d.pop("AsLeftMeasurementSetName", UNSET)

        as_left_measurement_set_id = d.pop("AsLeftMeasurementSetId", UNSET)

        as_left_adjustment_threshold = d.pop("AsLeftAdjustmentThreshold", UNSET)

        as_left_mean_extended = d.pop("AsLeftMeanExtended", UNSET)

        as_left_sd_extended = d.pop("AsLeftSdExtended", UNSET)

        as_left_range_extended = d.pop("AsLeftRangeExtended", UNSET)

        as_left_delta_extended = d.pop("AsLeftDeltaExtended", UNSET)

        as_left_cv_extended = d.pop("AsLeftCvExtended", UNSET)

        as_left_nominal_extended = d.pop("AsLeftNominalExtended", UNSET)

        as_left_min_max_header = d.pop("AsLeftMinMaxHeader", UNSET)

        as_left_accuracy_class = d.pop("AsLeftAccuracyClass", UNSET)

        as_left_accuracy_class_min = d.pop("AsLeftAccuracyClassMin", UNSET)

        as_left_accuracy_class_max = d.pop("AsLeftAccuracyClassMax", UNSET)

        as_left_minimum_measured_value = d.pop("AsLeftMinimumMeasuredValue", UNSET)

        as_left_maxi_mum_measured_value = d.pop("AsLeftMaxiMumMeasuredValue", UNSET)

        as_left_min_max_value_extended = d.pop("AsLeftMinMaxValueExtended", UNSET)

        as_left_tool_range_name = d.pop("AsLeftToolRangeName", UNSET)

        as_left_tool_range_uncertainty = d.pop("AsLeftToolRangeUncertainty", UNSET)

        def _parse_as_left_primary_tool_last_service_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_left_primary_tool_last_service_date_type_0 = isoparse(data)

                return as_left_primary_tool_last_service_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        as_left_primary_tool_last_service_date = (
            _parse_as_left_primary_tool_last_service_date(
                d.pop("AsLeftPrimaryToolLastServiceDate", UNSET)
            )
        )

        def _parse_as_left_primary_tool_next_service_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_left_primary_tool_next_service_date_type_0 = isoparse(data)

                return as_left_primary_tool_next_service_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        as_left_primary_tool_next_service_date = (
            _parse_as_left_primary_tool_next_service_date(
                d.pop("AsLeftPrimaryToolNextServiceDate", UNSET)
            )
        )

        as_left_primary_tool_calibrated_by = d.pop(
            "AsLeftPrimaryToolCalibratedBy", UNSET
        )

        as_left_primary_tool_tool_name = d.pop("AsLeftPrimaryToolToolName", UNSET)

        as_left_primary_tool_tool_description = d.pop(
            "AsLeftPrimaryToolToolDescription", UNSET
        )

        as_left_primary_tool_tool_type_name = d.pop(
            "AsLeftPrimaryToolToolTypeName", UNSET
        )

        as_left_primary_tool_manufacturer = d.pop(
            "AsLeftPrimaryToolManufacturer", UNSET
        )

        as_left_primary_tool_manufacturer_part_number = d.pop(
            "AsLeftPrimaryToolManufacturerPartNumber", UNSET
        )

        as_left_primary_tool_serial_number = d.pop(
            "AsLeftPrimaryToolSerialNumber", UNSET
        )

        as_found_measurement_set_name = d.pop("AsFoundMeasurementSetName", UNSET)

        as_found_measurement_set_id = d.pop("AsFoundMeasurementSetId", UNSET)

        as_found_adjustment_threshold = d.pop("AsFoundAdjustmentThreshold", UNSET)

        as_found_decimal_places = d.pop("AsFoundDecimalPlaces", UNSET)

        as_found_mean_extended = d.pop("AsFoundMeanExtended", UNSET)

        as_found_sd_extended = d.pop("AsFoundSdExtended", UNSET)

        as_found_range_extended = d.pop("AsFoundRangeExtended", UNSET)

        as_found_delta_extended = d.pop("AsFoundDeltaExtended", UNSET)

        as_found_cv_extended = d.pop("AsFoundCvExtended", UNSET)

        as_found_nominal_extended = d.pop("AsFoundNominalExtended", UNSET)

        as_found_min_max_header = d.pop("AsFoundMinMaxHeader", UNSET)

        as_found_accuracy_class = d.pop("AsFoundAccuracyClass", UNSET)

        as_found_accuracy_class_min = d.pop("AsFoundAccuracyClassMin", UNSET)

        as_found_accuracy_class_max = d.pop("AsFoundAccuracyClassMax", UNSET)

        as_found_minimum_measured_value = d.pop("AsFoundMinimumMeasuredValue", UNSET)

        as_found_maxi_mum_measured_value = d.pop("AsFoundMaxiMumMeasuredValue", UNSET)

        as_found_min_max_value_extended = d.pop("AsFoundMinMaxValueExtended", UNSET)

        as_found_tool_range_name = d.pop("AsFoundToolRangeName", UNSET)

        as_found_tool_range_uncertainty = d.pop("AsFoundToolRangeUncertainty", UNSET)

        def _parse_as_found_primary_tool_last_service_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_found_primary_tool_last_service_date_type_0 = isoparse(data)

                return as_found_primary_tool_last_service_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        as_found_primary_tool_last_service_date = (
            _parse_as_found_primary_tool_last_service_date(
                d.pop("AsFoundPrimaryToolLastServiceDate", UNSET)
            )
        )

        def _parse_as_found_primary_tool_next_service_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_found_primary_tool_next_service_date_type_0 = isoparse(data)

                return as_found_primary_tool_next_service_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        as_found_primary_tool_next_service_date = (
            _parse_as_found_primary_tool_next_service_date(
                d.pop("AsFoundPrimaryToolNextServiceDate", UNSET)
            )
        )

        as_found_primary_tool_calibrated_by = d.pop(
            "AsFoundPrimaryToolCalibratedBy", UNSET
        )

        as_found_primary_tool_tool_name = d.pop("AsFoundPrimaryToolToolName", UNSET)

        as_found_primary_tool_tool_description = d.pop(
            "AsFoundPrimaryToolToolDescription", UNSET
        )

        as_found_primary_tool_tool_type_name = d.pop(
            "AsFoundPrimaryToolToolTypeName", UNSET
        )

        as_found_primary_tool_manufacturer = d.pop(
            "AsFoundPrimaryToolManufacturer", UNSET
        )

        as_found_primary_tool_manufacturer_part_number = d.pop(
            "AsFoundPrimaryToolManufacturerPartNumber", UNSET
        )

        as_found_primary_tool_serial_number = d.pop(
            "AsFoundPrimaryToolSerialNumber", UNSET
        )

        def _parse_as_left_secondary_tool_last_service_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_left_secondary_tool_last_service_date_type_0 = isoparse(data)

                return as_left_secondary_tool_last_service_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        as_left_secondary_tool_last_service_date = (
            _parse_as_left_secondary_tool_last_service_date(
                d.pop("AsLeftSecondaryToolLastServiceDate", UNSET)
            )
        )

        def _parse_as_left_secondary_tool_next_service_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_left_secondary_tool_next_service_date_type_0 = isoparse(data)

                return as_left_secondary_tool_next_service_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        as_left_secondary_tool_next_service_date = (
            _parse_as_left_secondary_tool_next_service_date(
                d.pop("AsLeftSecondaryToolNextServiceDate", UNSET)
            )
        )

        as_left_secondary_tool_calibrated_by = d.pop(
            "AsLeftSecondaryToolCalibratedBy", UNSET
        )

        as_left_secondary_tool_tool_name = d.pop("AsLeftSecondaryToolToolName", UNSET)

        as_left_secondary_tool_tool_description = d.pop(
            "AsLeftSecondaryToolToolDescription", UNSET
        )

        as_left_secondary_tool_tool_type_name = d.pop(
            "AsLeftSecondaryToolToolTypeName", UNSET
        )

        as_left_secondary_tool_manufacturer = d.pop(
            "AsLeftSecondaryToolManufacturer", UNSET
        )

        as_left_secondary_tool_manufacturer_part_number = d.pop(
            "AsLeftSecondaryToolManufacturerPartNumber", UNSET
        )

        as_left_secondary_tool_serial_number = d.pop(
            "AsLeftSecondaryToolSerialNumber", UNSET
        )

        def _parse_as_found_secondary_tool_last_service_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_found_secondary_tool_last_service_date_type_0 = isoparse(data)

                return as_found_secondary_tool_last_service_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        as_found_secondary_tool_last_service_date = (
            _parse_as_found_secondary_tool_last_service_date(
                d.pop("AsFoundSecondaryToolLastServiceDate", UNSET)
            )
        )

        def _parse_as_found_secondary_tool_next_service_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_found_secondary_tool_next_service_date_type_0 = isoparse(data)

                return as_found_secondary_tool_next_service_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        as_found_secondary_tool_next_service_date = (
            _parse_as_found_secondary_tool_next_service_date(
                d.pop("AsFoundSecondaryToolNextServiceDate", UNSET)
            )
        )

        as_found_secondary_tool_calibrated_by = d.pop(
            "AsFoundSecondaryToolCalibratedBy", UNSET
        )

        as_found_secondary_tool_tool_name = d.pop("AsFoundSecondaryToolToolName", UNSET)

        as_found_secondary_tool_tool_description = d.pop(
            "AsFoundSecondaryToolToolDescription", UNSET
        )

        as_found_secondary_tool_tool_type_name = d.pop(
            "AsFoundSecondaryToolToolTypeName", UNSET
        )

        as_found_secondary_tool_manufacturer = d.pop(
            "AsFoundSecondaryToolManufacturer", UNSET
        )

        as_found_secondary_tool_manufacturer_part_number = d.pop(
            "AsFoundSecondaryToolManufacturerPartNumber", UNSET
        )

        as_found_secondary_tool_serial_number = d.pop(
            "AsFoundSecondaryToolSerialNumber", UNSET
        )

        _as_found_measurement_not_taken_result = d.pop(
            "AsFoundMeasurementNotTakenResult", UNSET
        )
        as_found_measurement_not_taken_result: Union[
            Unset,
            QualerApiModelsReportDatasetsToMeasurementAllResponseAsFoundMeasurementNotTakenResult,
        ]
        if isinstance(_as_found_measurement_not_taken_result, Unset):
            as_found_measurement_not_taken_result = UNSET
        else:
            as_found_measurement_not_taken_result = QualerApiModelsReportDatasetsToMeasurementAllResponseAsFoundMeasurementNotTakenResult(
                _as_found_measurement_not_taken_result
            )

        as_found_hide_from_certificate = d.pop("AsFoundHideFromCertificate", UNSET)

        as_found_measurement_not_taken_reason = d.pop(
            "AsFoundMeasurementNotTakenReason", UNSET
        )

        as_left_values = d.pop("AsLeftValues", UNSET)

        as_left_is_accredited = d.pop("AsLeftIsAccredited", UNSET)

        as_left_is_range_accredited = d.pop("AsLeftIsRangeAccredited", UNSET)

        as_found_values = d.pop("AsFoundValues", UNSET)

        as_found_is_accredited = d.pop("AsFoundIsAccredited", UNSET)

        as_found_is_range_accredited = d.pop("AsFoundIsRangeAccredited", UNSET)

        as_found_parameter_id = d.pop("AsFoundParameterId", UNSET)

        as_found_sd_header = d.pop("AsFoundSdHeader", UNSET)

        as_found_cv_header = d.pop("AsFoundCvHeader", UNSET)

        def _parse_as_found_measurement_local_time(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_found_measurement_local_time_type_0 = isoparse(data)

                return as_found_measurement_local_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        as_found_measurement_local_time = _parse_as_found_measurement_local_time(
            d.pop("AsFoundMeasurementLocalTime", UNSET)
        )

        as_found_tur = d.pop("AsFoundTur", UNSET)

        as_found_tur_raw = d.pop("AsFoundTurRaw", UNSET)

        as_left_tur = d.pop("AsLeftTur", UNSET)

        as_left_tur_raw = d.pop("AsLeftTurRaw", UNSET)

        as_found_tar = d.pop("AsFoundTar", UNSET)

        as_found_tar_raw = d.pop("AsFoundTarRaw", UNSET)

        as_left_tar = d.pop("AsLeftTar", UNSET)

        as_left_tar_raw = d.pop("AsLeftTarRaw", UNSET)

        as_found_guard_band = d.pop("AsFoundGuardBand", UNSET)

        as_left_guard_band = d.pop("AsLeftGuardBand", UNSET)

        _as_found_guard_band_logic = d.pop("AsFoundGuardBandLogic", UNSET)
        as_found_guard_band_logic: Union[
            Unset,
            QualerApiModelsReportDatasetsToMeasurementAllResponseAsFoundGuardBandLogic,
        ]
        if isinstance(_as_found_guard_band_logic, Unset):
            as_found_guard_band_logic = UNSET
        else:
            as_found_guard_band_logic = QualerApiModelsReportDatasetsToMeasurementAllResponseAsFoundGuardBandLogic(
                _as_found_guard_band_logic
            )

        _as_left_guard_band_logic = d.pop("AsLeftGuardBandLogic", UNSET)
        as_left_guard_band_logic: Union[
            Unset,
            QualerApiModelsReportDatasetsToMeasurementAllResponseAsLeftGuardBandLogic,
        ]
        if isinstance(_as_left_guard_band_logic, Unset):
            as_left_guard_band_logic = UNSET
        else:
            as_left_guard_band_logic = QualerApiModelsReportDatasetsToMeasurementAllResponseAsLeftGuardBandLogic(
                _as_left_guard_band_logic
            )

        as_found_error = d.pop("AsFoundError", UNSET)

        as_found_error_extended = d.pop("AsFoundErrorExtended", UNSET)

        as_left_error = d.pop("AsLeftError", UNSET)

        as_left_error_extended = d.pop("AsLeftErrorExtended", UNSET)

        as_found_percent_of_tolerance = d.pop("AsFoundPercentOfTolerance", UNSET)

        as_found_percent_of_tolerance_extended = d.pop(
            "AsFoundPercentOfToleranceExtended", UNSET
        )

        as_left_percent_of_tolerance = d.pop("AsLeftPercentOfTolerance", UNSET)

        as_left_percent_of_tolerance_extended = d.pop(
            "AsLeftPercentOfToleranceExtended", UNSET
        )

        as_found_tolerance_maximum = d.pop("AsFoundToleranceMaximum", UNSET)

        as_found_tolerance_minimum = d.pop("AsFoundToleranceMinimum", UNSET)

        as_found_tolerance_type = d.pop("AsFoundToleranceType", UNSET)

        as_found_tolerance_mode = d.pop("AsFoundToleranceMode", UNSET)

        as_found_tolerance_string = d.pop("AsFoundToleranceString", UNSET)

        as_left_tolerance_maximum = d.pop("AsLeftToleranceMaximum", UNSET)

        as_left_tolerance_minimum = d.pop("AsLeftToleranceMinimum", UNSET)

        as_left_tolerance_type = d.pop("AsLeftToleranceType", UNSET)

        as_left_tolerance_mode = d.pop("AsLeftToleranceMode", UNSET)

        as_left_tolerance_string = d.pop("AsLeftToleranceString", UNSET)

        as_found_max_hysteresis = d.pop("AsFoundMaxHysteresis", UNSET)

        as_found_run = d.pop("AsFoundRun", UNSET)

        as_found_direction = d.pop("AsFoundDirection", UNSET)

        as_found_hysteresis = d.pop("AsFoundHysteresis", UNSET)

        as_left_max_hysteresis = d.pop("AsLeftMaxHysteresis", UNSET)

        as_left_run = d.pop("AsLeftRun", UNSET)

        as_left_direction = d.pop("AsLeftDirection", UNSET)

        as_left_hysteresis = d.pop("AsLeftHysteresis", UNSET)

        _as_found_reading_entry_math = d.pop("AsFoundReadingEntryMath", UNSET)
        as_found_reading_entry_math: Union[
            Unset,
            QualerApiModelsReportDatasetsToMeasurementAllResponseAsFoundReadingEntryMath,
        ]
        if isinstance(_as_found_reading_entry_math, Unset):
            as_found_reading_entry_math = UNSET
        else:
            as_found_reading_entry_math = QualerApiModelsReportDatasetsToMeasurementAllResponseAsFoundReadingEntryMath(
                _as_found_reading_entry_math
            )

        as_found_reading_entry_math_string = d.pop(
            "AsFoundReadingEntryMathString", UNSET
        )

        as_found_value_1 = d.pop("AsFoundValue1", UNSET)

        as_found_value_2 = d.pop("AsFoundValue2", UNSET)

        as_found_value_3 = d.pop("AsFoundValue3", UNSET)

        as_found_value_4 = d.pop("AsFoundValue4", UNSET)

        as_found_value_5 = d.pop("AsFoundValue5", UNSET)

        as_found_value_6 = d.pop("AsFoundValue6", UNSET)

        as_found_value_7 = d.pop("AsFoundValue7", UNSET)

        as_found_value_8 = d.pop("AsFoundValue8", UNSET)

        as_found_value_9 = d.pop("AsFoundValue9", UNSET)

        as_found_value_10 = d.pop("AsFoundValue10", UNSET)

        as_found_value_11 = d.pop("AsFoundValue11", UNSET)

        as_found_value_12 = d.pop("AsFoundValue12", UNSET)

        as_found_value_13 = d.pop("AsFoundValue13", UNSET)

        as_found_value_14 = d.pop("AsFoundValue14", UNSET)

        as_found_value_15 = d.pop("AsFoundValue15", UNSET)

        as_found_value_16 = d.pop("AsFoundValue16", UNSET)

        as_found_value_17 = d.pop("AsFoundValue17", UNSET)

        as_found_value_18 = d.pop("AsFoundValue18", UNSET)

        as_found_value_19 = d.pop("AsFoundValue19", UNSET)

        as_found_value_20 = d.pop("AsFoundValue20", UNSET)

        as_found_value_21 = d.pop("AsFoundValue21", UNSET)

        as_found_value_22 = d.pop("AsFoundValue22", UNSET)

        as_found_value_23 = d.pop("AsFoundValue23", UNSET)

        as_found_value_24 = d.pop("AsFoundValue24", UNSET)

        as_found_value_25 = d.pop("AsFoundValue25", UNSET)

        as_found_value_26 = d.pop("AsFoundValue26", UNSET)

        as_found_value_27 = d.pop("AsFoundValue27", UNSET)

        as_found_value_28 = d.pop("AsFoundValue28", UNSET)

        as_found_value_29 = d.pop("AsFoundValue29", UNSET)

        as_found_value_30 = d.pop("AsFoundValue30", UNSET)

        as_found_value_31 = d.pop("AsFoundValue31", UNSET)

        as_found_value_32 = d.pop("AsFoundValue32", UNSET)

        as_found_value_33 = d.pop("AsFoundValue33", UNSET)

        as_found_value_34 = d.pop("AsFoundValue34", UNSET)

        as_found_value_35 = d.pop("AsFoundValue35", UNSET)

        as_found_value_36 = d.pop("AsFoundValue36", UNSET)

        as_found_value_37 = d.pop("AsFoundValue37", UNSET)

        as_found_value_38 = d.pop("AsFoundValue38", UNSET)

        as_found_value_39 = d.pop("AsFoundValue39", UNSET)

        as_found_value_40 = d.pop("AsFoundValue40", UNSET)

        as_found_raw_value_1 = d.pop("AsFoundRawValue1", UNSET)

        as_found_raw_value_2 = d.pop("AsFoundRawValue2", UNSET)

        as_found_raw_value_3 = d.pop("AsFoundRawValue3", UNSET)

        as_found_raw_value_4 = d.pop("AsFoundRawValue4", UNSET)

        as_found_raw_value_5 = d.pop("AsFoundRawValue5", UNSET)

        as_found_raw_value_6 = d.pop("AsFoundRawValue6", UNSET)

        as_found_raw_value_7 = d.pop("AsFoundRawValue7", UNSET)

        as_found_raw_value_8 = d.pop("AsFoundRawValue8", UNSET)

        as_found_raw_value_9 = d.pop("AsFoundRawValue9", UNSET)

        as_found_raw_value_10 = d.pop("AsFoundRawValue10", UNSET)

        as_found_raw_value_11 = d.pop("AsFoundRawValue11", UNSET)

        as_found_raw_value_12 = d.pop("AsFoundRawValue12", UNSET)

        as_found_raw_value_13 = d.pop("AsFoundRawValue13", UNSET)

        as_found_raw_value_14 = d.pop("AsFoundRawValue14", UNSET)

        as_found_raw_value_15 = d.pop("AsFoundRawValue15", UNSET)

        as_found_raw_value_16 = d.pop("AsFoundRawValue16", UNSET)

        as_found_raw_value_17 = d.pop("AsFoundRawValue17", UNSET)

        as_found_raw_value_18 = d.pop("AsFoundRawValue18", UNSET)

        as_found_raw_value_19 = d.pop("AsFoundRawValue19", UNSET)

        as_found_raw_value_20 = d.pop("AsFoundRawValue20", UNSET)

        as_found_raw_value_21 = d.pop("AsFoundRawValue21", UNSET)

        as_found_raw_value_22 = d.pop("AsFoundRawValue22", UNSET)

        as_found_raw_value_23 = d.pop("AsFoundRawValue23", UNSET)

        as_found_raw_value_24 = d.pop("AsFoundRawValue24", UNSET)

        as_found_raw_value_25 = d.pop("AsFoundRawValue25", UNSET)

        as_found_raw_value_26 = d.pop("AsFoundRawValue26", UNSET)

        as_found_raw_value_27 = d.pop("AsFoundRawValue27", UNSET)

        as_found_raw_value_28 = d.pop("AsFoundRawValue28", UNSET)

        as_found_raw_value_29 = d.pop("AsFoundRawValue29", UNSET)

        as_found_raw_value_30 = d.pop("AsFoundRawValue30", UNSET)

        as_found_raw_value_31 = d.pop("AsFoundRawValue31", UNSET)

        as_found_raw_value_32 = d.pop("AsFoundRawValue32", UNSET)

        as_found_raw_value_33 = d.pop("AsFoundRawValue33", UNSET)

        as_found_raw_value_34 = d.pop("AsFoundRawValue34", UNSET)

        as_found_raw_value_35 = d.pop("AsFoundRawValue35", UNSET)

        as_found_raw_value_36 = d.pop("AsFoundRawValue36", UNSET)

        as_found_raw_value_37 = d.pop("AsFoundRawValue37", UNSET)

        as_found_raw_value_38 = d.pop("AsFoundRawValue38", UNSET)

        as_found_raw_value_39 = d.pop("AsFoundRawValue39", UNSET)

        as_found_raw_value_40 = d.pop("AsFoundRawValue40", UNSET)

        as_found_value_subtitle_1 = d.pop("AsFoundValueSubtitle1", UNSET)

        as_found_value_subtitle_2 = d.pop("AsFoundValueSubtitle2", UNSET)

        as_found_value_subtitle_3 = d.pop("AsFoundValueSubtitle3", UNSET)

        as_found_value_subtitle_4 = d.pop("AsFoundValueSubtitle4", UNSET)

        as_found_value_subtitle_5 = d.pop("AsFoundValueSubtitle5", UNSET)

        as_found_value_subtitle_6 = d.pop("AsFoundValueSubtitle6", UNSET)

        as_found_value_subtitle_7 = d.pop("AsFoundValueSubtitle7", UNSET)

        as_found_value_subtitle_8 = d.pop("AsFoundValueSubtitle8", UNSET)

        as_found_value_subtitle_9 = d.pop("AsFoundValueSubtitle9", UNSET)

        as_found_value_subtitle_10 = d.pop("AsFoundValueSubtitle10", UNSET)

        as_found_value_subtitle_11 = d.pop("AsFoundValueSubtitle11", UNSET)

        as_found_value_subtitle_12 = d.pop("AsFoundValueSubtitle12", UNSET)

        as_found_value_subtitle_13 = d.pop("AsFoundValueSubtitle13", UNSET)

        as_found_value_subtitle_14 = d.pop("AsFoundValueSubtitle14", UNSET)

        as_found_value_subtitle_15 = d.pop("AsFoundValueSubtitle15", UNSET)

        as_found_value_subtitle_16 = d.pop("AsFoundValueSubtitle16", UNSET)

        as_found_value_subtitle_17 = d.pop("AsFoundValueSubtitle17", UNSET)

        as_found_value_subtitle_18 = d.pop("AsFoundValueSubtitle18", UNSET)

        as_found_value_subtitle_19 = d.pop("AsFoundValueSubtitle19", UNSET)

        as_found_value_subtitle_20 = d.pop("AsFoundValueSubtitle20", UNSET)

        as_found_value_subtitle_21 = d.pop("AsFoundValueSubtitle21", UNSET)

        as_found_value_subtitle_22 = d.pop("AsFoundValueSubtitle22", UNSET)

        as_found_value_subtitle_23 = d.pop("AsFoundValueSubtitle23", UNSET)

        as_found_value_subtitle_24 = d.pop("AsFoundValueSubtitle24", UNSET)

        as_found_value_subtitle_25 = d.pop("AsFoundValueSubtitle25", UNSET)

        as_found_value_subtitle_26 = d.pop("AsFoundValueSubtitle26", UNSET)

        as_found_value_subtitle_27 = d.pop("AsFoundValueSubtitle27", UNSET)

        as_found_value_subtitle_28 = d.pop("AsFoundValueSubtitle28", UNSET)

        as_found_value_subtitle_29 = d.pop("AsFoundValueSubtitle29", UNSET)

        as_found_value_subtitle_30 = d.pop("AsFoundValueSubtitle30", UNSET)

        as_found_value_subtitle_31 = d.pop("AsFoundValueSubtitle31", UNSET)

        as_found_value_subtitle_32 = d.pop("AsFoundValueSubtitle32", UNSET)

        as_found_value_subtitle_33 = d.pop("AsFoundValueSubtitle33", UNSET)

        as_found_value_subtitle_34 = d.pop("AsFoundValueSubtitle34", UNSET)

        as_found_value_subtitle_35 = d.pop("AsFoundValueSubtitle35", UNSET)

        as_found_value_subtitle_36 = d.pop("AsFoundValueSubtitle36", UNSET)

        as_found_value_subtitle_37 = d.pop("AsFoundValueSubtitle37", UNSET)

        as_found_value_subtitle_38 = d.pop("AsFoundValueSubtitle38", UNSET)

        as_found_value_subtitle_39 = d.pop("AsFoundValueSubtitle39", UNSET)

        as_found_value_subtitle_40 = d.pop("AsFoundValueSubtitle40", UNSET)

        as_found_mean = d.pop("AsFoundMean", UNSET)

        as_found_mean_raw = d.pop("AsFoundMeanRaw", UNSET)

        as_found_sd = d.pop("AsFoundSd", UNSET)

        as_found_sd_raw = d.pop("AsFoundSdRaw", UNSET)

        as_found_delta = d.pop("AsFoundDelta", UNSET)

        as_found_range = d.pop("AsFoundRange", UNSET)

        as_found_cv = d.pop("AsFoundCv", UNSET)

        as_found_cv_raw = d.pop("AsFoundCvRaw", UNSET)

        as_found_result = d.pop("AsFoundResult", UNSET)

        as_found_range_result = d.pop("AsFoundRangeResult", UNSET)

        as_found_delta_result = d.pop("AsFoundDeltaResult", UNSET)

        as_found_min_result = d.pop("AsFoundMinResult", UNSET)

        as_found_max_result = d.pop("AsFoundMaxResult", UNSET)

        as_found_tar_result = d.pop("AsFoundTarResult", UNSET)

        as_found_tur_result = d.pop("AsFoundTurResult", UNSET)

        as_found_error_result = d.pop("AsFoundErrorResult", UNSET)

        as_found_sd_result = d.pop("AsFoundSdResult", UNSET)

        as_found_cv_result = d.pop("AsFoundCvResult", UNSET)

        as_found_custom_field_result = d.pop("AsFoundCustomFieldResult", UNSET)

        as_found_mu = d.pop("AsFoundMu", UNSET)

        as_found_mu_raw = d.pop("AsFoundMuRaw", UNSET)

        as_found_mu_effective_dof = d.pop("AsFoundMuEffectiveDOF", UNSET)

        as_found_mu_coverage_factor = d.pop("AsFoundMUCoverageFactor", UNSET)

        as_found_cmc = d.pop("AsFoundCmc", UNSET)

        as_found_cmc_comments = d.pop("AsFoundCmcComments", UNSET)

        as_found_calculated_uncertainty = d.pop("AsFoundCalculatedUncertainty", UNSET)

        as_found_lab_mu = d.pop("AsFoundLabMu", UNSET)

        as_found_uncertainty_budget = d.pop("AsFoundUncertaintyBudget", UNSET)

        as_found_mu_extended = d.pop("AsFoundMuExtended", UNSET)

        as_found_channel = d.pop("AsFoundChannel", UNSET)

        _as_found_measurement_type = d.pop("AsFoundMeasurementType", UNSET)
        as_found_measurement_type: Union[
            Unset,
            QualerApiModelsReportDatasetsToMeasurementAllResponseAsFoundMeasurementType,
        ]
        if isinstance(_as_found_measurement_type, Unset):
            as_found_measurement_type = UNSET
        else:
            as_found_measurement_type = QualerApiModelsReportDatasetsToMeasurementAllResponseAsFoundMeasurementType(
                _as_found_measurement_type
            )

        as_found_updated_by = d.pop("AsFoundUpdatedBy", UNSET)

        def _parse_as_found_updated_on(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_found_updated_on_type_0 = isoparse(data)

                return as_found_updated_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        as_found_updated_on = _parse_as_found_updated_on(
            d.pop("AsFoundUpdatedOn", UNSET)
        )

        as_left_abbreviated_uom = d.pop("AsLeftAbbreviatedUOM", UNSET)

        as_left_unit_scale_factor = d.pop("AsLeftUnitScaleFactor", UNSET)

        as_found_specification_title = d.pop("AsFoundSpecificationTitle", UNSET)

        as_found_specification_subtitle = d.pop("AsFoundSpecificationSubtitle", UNSET)

        as_found_specification_group = d.pop("AsFoundSpecificationGroup", UNSET)

        as_found_batch_type = d.pop("AsFoundBatchType", UNSET)

        as_found_batch_result = d.pop("AsFoundBatchResult", UNSET)

        as_found_is_by_channel = d.pop("AsFoundIsByChannel", UNSET)

        as_found_channel_count = d.pop("AsFoundChannelCount", UNSET)

        _as_found_commenced_on = d.pop("AsFoundCommencedOn", UNSET)
        as_found_commenced_on: Union[Unset, datetime.datetime]
        if isinstance(_as_found_commenced_on, Unset):
            as_found_commenced_on = UNSET
        else:
            if _as_found_commenced_on is None:

                as_found_commenced_on = None

            else:

                as_found_commenced_on = isoparse(_as_found_commenced_on)

        as_found_commenced_by = d.pop("AsFoundCommencedBy", UNSET)

        as_found_z_factor = d.pop("AsFoundZFactor", UNSET)

        as_found_air_buoyancy = d.pop("AsFoundAirBuoyancy", UNSET)

        as_found_evaporation_rate = d.pop("AsFoundEvaporationRate", UNSET)

        as_found_ambient_temperature = d.pop("AsFoundAmbientTemperature", UNSET)

        as_found_air_humidity = d.pop("AsFoundAirHumidity", UNSET)

        as_found_barometric_pressure = d.pop("AsFoundBarometricPressure", UNSET)

        as_found_altitude = d.pop("AsFoundAltitude", UNSET)

        as_found_wind_speed = d.pop("AsFoundWindSpeed", UNSET)

        as_found_solar_radiation = d.pop("AsFoundSolarRadiation", UNSET)

        as_found_light_intensity = d.pop("AsFoundLightIntensity", UNSET)

        as_found_noise_level = d.pop("AsFoundNoiseLevel", UNSET)

        as_found_ph_level = d.pop("AsFoundPhLevel", UNSET)

        as_found_water_conductivity = d.pop("AsFoundWaterConductivity", UNSET)

        as_found_water_temperature = d.pop("AsFoundWaterTemperature", UNSET)

        as_found_z_factor_uom = d.pop("AsFoundZFactorUom", UNSET)

        as_found_air_buoyancy_uom = d.pop("AsFoundAirBuoyancyUom", UNSET)

        as_found_evaporation_rate_uom = d.pop("AsFoundEvaporationRateUom", UNSET)

        as_found_ambient_temperature_uom = d.pop("AsFoundAmbientTemperatureUom", UNSET)

        as_found_air_humidity_uom = d.pop("AsFoundAirHumidityUom", UNSET)

        as_found_barometric_pressure_uom = d.pop("AsFoundBarometricPressureUom", UNSET)

        as_found_altitude_uom = d.pop("AsFoundAltitudeUom", UNSET)

        as_found_wind_speed_uom = d.pop("AsFoundWindSpeedUom", UNSET)

        as_found_solar_radiation_uom = d.pop("AsFoundSolarRadiationUom", UNSET)

        as_found_light_intensity_uom = d.pop("AsFoundLightIntensityUom", UNSET)

        as_found_noise_level_uom = d.pop("AsFoundNoiseLevelUom", UNSET)

        as_found_ph_level_uom = d.pop("AsFoundPhLevelUom", UNSET)

        as_found_water_conductivity_uom = d.pop("AsFoundWaterConductivityUom", UNSET)

        as_found_water_temperature_uom = d.pop("AsFoundWaterTemperatureUom", UNSET)

        as_found_abbreviated_uom = d.pop("AsFoundAbbreviatedUOM", UNSET)

        as_found_unit_scale_factor = d.pop("AsFoundUnitScaleFactor", UNSET)

        as_found_specification_name = d.pop("AsFoundSpecificationName", UNSET)

        as_found_parameter_name = d.pop("AsFoundParameterName", UNSET)

        as_found_display_order = d.pop("AsFoundDisplayOrder", UNSET)

        as_found_unit_of_measure = d.pop("AsFoundUnitOfMeasure", UNSET)

        as_found_display_format = d.pop("AsFoundDisplayFormat", UNSET)

        as_found_precision = d.pop("AsFoundPrecision", UNSET)

        _as_found_precision_type = d.pop("AsFoundPrecisionType", UNSET)
        as_found_precision_type: Union[
            Unset,
            QualerApiModelsReportDatasetsToMeasurementAllResponseAsFoundPrecisionType,
        ]
        if isinstance(_as_found_precision_type, Unset):
            as_found_precision_type = UNSET
        else:
            as_found_precision_type = QualerApiModelsReportDatasetsToMeasurementAllResponseAsFoundPrecisionType(
                _as_found_precision_type
            )

        as_found_minimum = d.pop("AsFoundMinimum", UNSET)

        as_found_nominal = d.pop("AsFoundNominal", UNSET)

        as_found_expected_value = d.pop("AsFoundExpectedValue", UNSET)

        as_found_expected_value_raw = d.pop("AsFoundExpectedValueRaw", UNSET)

        as_found_test_value = d.pop("AsFoundTestValue", UNSET)

        as_found_base_value = d.pop("AsFoundBaseValue", UNSET)

        as_found_maxi_mum = d.pop("AsFoundMaxiMum", UNSET)

        as_found_resolution = d.pop("AsFoundResolution", UNSET)

        as_found_resolution_count = d.pop("AsFoundResolutionCount", UNSET)

        as_found_measurement_batch_id = d.pop("AsFoundMeasurementBatchId", UNSET)

        as_found_measurement_id = d.pop("AsFoundMeasurementId", UNSET)

        as_found_standard_id = d.pop("AsFoundStandardId", UNSET)

        as_found_tool_id = d.pop("AsFoundToolId", UNSET)

        as_found_measurement_condition_id = d.pop(
            "AsFoundMeasurementConditionId", UNSET
        )

        as_found_measurement_point_id = d.pop("AsFoundMeasurementPointId", UNSET)

        as_left_parameter_id = d.pop("AsLeftParameterId", UNSET)

        as_left_sd_header = d.pop("AsLeftSdHeader", UNSET)

        as_left_cv_header = d.pop("AsLeftCvHeader", UNSET)

        def _parse_as_left_measurement_local_time(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_left_measurement_local_time_type_0 = isoparse(data)

                return as_left_measurement_local_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        as_left_measurement_local_time = _parse_as_left_measurement_local_time(
            d.pop("AsLeftMeasurementLocalTime", UNSET)
        )

        _as_left_reading_entry_math = d.pop("AsLeftReadingEntryMath", UNSET)
        as_left_reading_entry_math: Union[
            Unset,
            QualerApiModelsReportDatasetsToMeasurementAllResponseAsLeftReadingEntryMath,
        ]
        if isinstance(_as_left_reading_entry_math, Unset):
            as_left_reading_entry_math = UNSET
        else:
            as_left_reading_entry_math = QualerApiModelsReportDatasetsToMeasurementAllResponseAsLeftReadingEntryMath(
                _as_left_reading_entry_math
            )

        as_left_reading_entry_math_string = d.pop("AsLeftReadingEntryMathString", UNSET)

        as_left_value_1 = d.pop("AsLeftValue1", UNSET)

        as_left_value_2 = d.pop("AsLeftValue2", UNSET)

        as_left_value_3 = d.pop("AsLeftValue3", UNSET)

        as_left_value_4 = d.pop("AsLeftValue4", UNSET)

        as_left_value_5 = d.pop("AsLeftValue5", UNSET)

        as_left_value_6 = d.pop("AsLeftValue6", UNSET)

        as_left_value_7 = d.pop("AsLeftValue7", UNSET)

        as_left_value_8 = d.pop("AsLeftValue8", UNSET)

        as_left_value_9 = d.pop("AsLeftValue9", UNSET)

        as_left_value_10 = d.pop("AsLeftValue10", UNSET)

        as_left_value_11 = d.pop("AsLeftValue11", UNSET)

        as_left_value_12 = d.pop("AsLeftValue12", UNSET)

        as_left_value_13 = d.pop("AsLeftValue13", UNSET)

        as_left_value_14 = d.pop("AsLeftValue14", UNSET)

        as_left_value_15 = d.pop("AsLeftValue15", UNSET)

        as_left_value_16 = d.pop("AsLeftValue16", UNSET)

        as_left_value_17 = d.pop("AsLeftValue17", UNSET)

        as_left_value_18 = d.pop("AsLeftValue18", UNSET)

        as_left_value_19 = d.pop("AsLeftValue19", UNSET)

        as_left_value_20 = d.pop("AsLeftValue20", UNSET)

        as_left_value_21 = d.pop("AsLeftValue21", UNSET)

        as_left_value_22 = d.pop("AsLeftValue22", UNSET)

        as_left_value_23 = d.pop("AsLeftValue23", UNSET)

        as_left_value_24 = d.pop("AsLeftValue24", UNSET)

        as_left_value_25 = d.pop("AsLeftValue25", UNSET)

        as_left_value_26 = d.pop("AsLeftValue26", UNSET)

        as_left_value_27 = d.pop("AsLeftValue27", UNSET)

        as_left_value_28 = d.pop("AsLeftValue28", UNSET)

        as_left_value_29 = d.pop("AsLeftValue29", UNSET)

        as_left_value_30 = d.pop("AsLeftValue30", UNSET)

        as_left_value_31 = d.pop("AsLeftValue31", UNSET)

        as_left_value_32 = d.pop("AsLeftValue32", UNSET)

        as_left_value_33 = d.pop("AsLeftValue33", UNSET)

        as_left_value_34 = d.pop("AsLeftValue34", UNSET)

        as_left_value_35 = d.pop("AsLeftValue35", UNSET)

        as_left_value_36 = d.pop("AsLeftValue36", UNSET)

        as_left_value_37 = d.pop("AsLeftValue37", UNSET)

        as_left_value_38 = d.pop("AsLeftValue38", UNSET)

        as_left_value_39 = d.pop("AsLeftValue39", UNSET)

        as_left_value_40 = d.pop("AsLeftValue40", UNSET)

        as_left_raw_value_1 = d.pop("AsLeftRawValue1", UNSET)

        as_left_raw_value_2 = d.pop("AsLeftRawValue2", UNSET)

        as_left_raw_value_3 = d.pop("AsLeftRawValue3", UNSET)

        as_left_raw_value_4 = d.pop("AsLeftRawValue4", UNSET)

        as_left_raw_value_5 = d.pop("AsLeftRawValue5", UNSET)

        as_left_raw_value_6 = d.pop("AsLeftRawValue6", UNSET)

        as_left_raw_value_7 = d.pop("AsLeftRawValue7", UNSET)

        as_left_raw_value_8 = d.pop("AsLeftRawValue8", UNSET)

        as_left_raw_value_9 = d.pop("AsLeftRawValue9", UNSET)

        as_left_raw_value_10 = d.pop("AsLeftRawValue10", UNSET)

        as_left_raw_value_11 = d.pop("AsLeftRawValue11", UNSET)

        as_left_raw_value_12 = d.pop("AsLeftRawValue12", UNSET)

        as_left_raw_value_13 = d.pop("AsLeftRawValue13", UNSET)

        as_left_raw_value_14 = d.pop("AsLeftRawValue14", UNSET)

        as_left_raw_value_15 = d.pop("AsLeftRawValue15", UNSET)

        as_left_raw_value_16 = d.pop("AsLeftRawValue16", UNSET)

        as_left_raw_value_17 = d.pop("AsLeftRawValue17", UNSET)

        as_left_raw_value_18 = d.pop("AsLeftRawValue18", UNSET)

        as_left_raw_value_19 = d.pop("AsLeftRawValue19", UNSET)

        as_left_raw_value_20 = d.pop("AsLeftRawValue20", UNSET)

        as_left_raw_value_21 = d.pop("AsLeftRawValue21", UNSET)

        as_left_raw_value_22 = d.pop("AsLeftRawValue22", UNSET)

        as_left_raw_value_23 = d.pop("AsLeftRawValue23", UNSET)

        as_left_raw_value_24 = d.pop("AsLeftRawValue24", UNSET)

        as_left_raw_value_25 = d.pop("AsLeftRawValue25", UNSET)

        as_left_raw_value_26 = d.pop("AsLeftRawValue26", UNSET)

        as_left_raw_value_27 = d.pop("AsLeftRawValue27", UNSET)

        as_left_raw_value_28 = d.pop("AsLeftRawValue28", UNSET)

        as_left_raw_value_29 = d.pop("AsLeftRawValue29", UNSET)

        as_left_raw_value_30 = d.pop("AsLeftRawValue30", UNSET)

        as_left_raw_value_31 = d.pop("AsLeftRawValue31", UNSET)

        as_left_raw_value_32 = d.pop("AsLeftRawValue32", UNSET)

        as_left_raw_value_33 = d.pop("AsLeftRawValue33", UNSET)

        as_left_raw_value_34 = d.pop("AsLeftRawValue34", UNSET)

        as_left_raw_value_35 = d.pop("AsLeftRawValue35", UNSET)

        as_left_raw_value_36 = d.pop("AsLeftRawValue36", UNSET)

        as_left_raw_value_37 = d.pop("AsLeftRawValue37", UNSET)

        as_left_raw_value_38 = d.pop("AsLeftRawValue38", UNSET)

        as_left_raw_value_39 = d.pop("AsLeftRawValue39", UNSET)

        as_left_raw_value_40 = d.pop("AsLeftRawValue40", UNSET)

        as_left_value_subtitle_1 = d.pop("AsLeftValueSubtitle1", UNSET)

        as_left_value_subtitle_2 = d.pop("AsLeftValueSubtitle2", UNSET)

        as_left_value_subtitle_3 = d.pop("AsLeftValueSubtitle3", UNSET)

        as_left_value_subtitle_4 = d.pop("AsLeftValueSubtitle4", UNSET)

        as_left_value_subtitle_5 = d.pop("AsLeftValueSubtitle5", UNSET)

        as_left_value_subtitle_6 = d.pop("AsLeftValueSubtitle6", UNSET)

        as_left_value_subtitle_7 = d.pop("AsLeftValueSubtitle7", UNSET)

        as_left_value_subtitle_8 = d.pop("AsLeftValueSubtitle8", UNSET)

        as_left_value_subtitle_9 = d.pop("AsLeftValueSubtitle9", UNSET)

        as_left_value_subtitle_10 = d.pop("AsLeftValueSubtitle10", UNSET)

        as_left_value_subtitle_11 = d.pop("AsLeftValueSubtitle11", UNSET)

        as_left_value_subtitle_12 = d.pop("AsLeftValueSubtitle12", UNSET)

        as_left_value_subtitle_13 = d.pop("AsLeftValueSubtitle13", UNSET)

        as_left_value_subtitle_14 = d.pop("AsLeftValueSubtitle14", UNSET)

        as_left_value_subtitle_15 = d.pop("AsLeftValueSubtitle15", UNSET)

        as_left_value_subtitle_16 = d.pop("AsLeftValueSubtitle16", UNSET)

        as_left_value_subtitle_17 = d.pop("AsLeftValueSubtitle17", UNSET)

        as_left_value_subtitle_18 = d.pop("AsLeftValueSubtitle18", UNSET)

        as_left_value_subtitle_19 = d.pop("AsLeftValueSubtitle19", UNSET)

        as_left_value_subtitle_20 = d.pop("AsLeftValueSubtitle20", UNSET)

        as_left_value_subtitle_21 = d.pop("AsLeftValueSubtitle21", UNSET)

        as_left_value_subtitle_22 = d.pop("AsLeftValueSubtitle22", UNSET)

        as_left_value_subtitle_23 = d.pop("AsLeftValueSubtitle23", UNSET)

        as_left_value_subtitle_24 = d.pop("AsLeftValueSubtitle24", UNSET)

        as_left_value_subtitle_25 = d.pop("AsLeftValueSubtitle25", UNSET)

        as_left_value_subtitle_26 = d.pop("AsLeftValueSubtitle26", UNSET)

        as_left_value_subtitle_27 = d.pop("AsLeftValueSubtitle27", UNSET)

        as_left_value_subtitle_28 = d.pop("AsLeftValueSubtitle28", UNSET)

        as_left_value_subtitle_29 = d.pop("AsLeftValueSubtitle29", UNSET)

        as_left_value_subtitle_30 = d.pop("AsLeftValueSubtitle30", UNSET)

        as_left_value_subtitle_31 = d.pop("AsLeftValueSubtitle31", UNSET)

        as_left_value_subtitle_32 = d.pop("AsLeftValueSubtitle32", UNSET)

        as_left_value_subtitle_33 = d.pop("AsLeftValueSubtitle33", UNSET)

        as_left_value_subtitle_34 = d.pop("AsLeftValueSubtitle34", UNSET)

        as_left_value_subtitle_35 = d.pop("AsLeftValueSubtitle35", UNSET)

        as_left_value_subtitle_36 = d.pop("AsLeftValueSubtitle36", UNSET)

        as_left_value_subtitle_37 = d.pop("AsLeftValueSubtitle37", UNSET)

        as_left_value_subtitle_38 = d.pop("AsLeftValueSubtitle38", UNSET)

        as_left_value_subtitle_39 = d.pop("AsLeftValueSubtitle39", UNSET)

        as_left_value_subtitle_40 = d.pop("AsLeftValueSubtitle40", UNSET)

        as_left_mean = d.pop("AsLeftMean", UNSET)

        as_left_mean_raw = d.pop("AsLeftMeanRaw", UNSET)

        as_left_sd = d.pop("AsLeftSd", UNSET)

        as_left_sd_raw = d.pop("AsLeftSdRaw", UNSET)

        as_left_cv = d.pop("AsLeftCv", UNSET)

        as_left_cv_raw = d.pop("AsLeftCvRaw", UNSET)

        as_left_delta = d.pop("AsLeftDelta", UNSET)

        as_left_range = d.pop("AsLeftRange", UNSET)

        def _parse_as_left_result(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        as_left_result = _parse_as_left_result(d.pop("AsLeftResult", UNSET))

        as_left_range_result = d.pop("AsLeftRangeResult", UNSET)

        as_left_delta_result = d.pop("AsLeftDeltaResult", UNSET)

        as_left_min_result = d.pop("AsLeftMinResult", UNSET)

        as_left_max_result = d.pop("AsLeftMaxResult", UNSET)

        as_left_tar_result = d.pop("AsLeftTarResult", UNSET)

        as_left_tur_result = d.pop("AsLeftTurResult", UNSET)

        as_left_error_result = d.pop("AsLeftErrorResult", UNSET)

        as_left_sd_result = d.pop("AsLeftSdResult", UNSET)

        as_left_cv_result = d.pop("AsLeftCvResult", UNSET)

        as_left_custom_field_result = d.pop("AsLeftCustomFieldResult", UNSET)

        as_left_mu = d.pop("AsLeftMu", UNSET)

        as_left_mu_raw = d.pop("AsLeftMuRaw", UNSET)

        as_left_mu_effective_dof = d.pop("AsLeftMUEffectiveDOF", UNSET)

        as_left_mu_coverage_factor = d.pop("AsLeftMUCoverageFactor", UNSET)

        as_left_cmc = d.pop("AsLeftCmc", UNSET)

        as_left_cmc_comments = d.pop("AsLeftCmcComments", UNSET)

        as_left_calculated_uncertainty = d.pop("AsLeftCalculatedUncertainty", UNSET)

        as_left_lab_mu = d.pop("AsLeftLabMu", UNSET)

        as_left_uncertainty_budget = d.pop("AsLeftUncertaintyBudget", UNSET)

        as_left_mu_extended = d.pop("AsLeftMuExtended", UNSET)

        as_left_channel = d.pop("AsLeftChannel", UNSET)

        _as_left_measurement_type = d.pop("AsLeftMeasurementType", UNSET)
        as_left_measurement_type: Union[
            Unset,
            QualerApiModelsReportDatasetsToMeasurementAllResponseAsLeftMeasurementType,
        ]
        if isinstance(_as_left_measurement_type, Unset):
            as_left_measurement_type = UNSET
        else:
            as_left_measurement_type = QualerApiModelsReportDatasetsToMeasurementAllResponseAsLeftMeasurementType(
                _as_left_measurement_type
            )

        as_left_updated_by = d.pop("AsLeftUpdatedBy", UNSET)

        def _parse_as_left_updated_on(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_left_updated_on_type_0 = isoparse(data)

                return as_left_updated_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        as_left_updated_on = _parse_as_left_updated_on(d.pop("AsLeftUpdatedOn", UNSET))

        as_left_specification_title = d.pop("AsLeftSpecificationTitle", UNSET)

        as_left_specification_subtitle = d.pop("AsLeftSpecificationSubtitle", UNSET)

        as_left_specification_group = d.pop("AsLeftSpecificationGroup", UNSET)

        as_left_batch_type = d.pop("AsLeftBatchType", UNSET)

        as_left_batch_result = d.pop("AsLeftBatchResult", UNSET)

        as_left_is_by_channel = d.pop("AsLeftIsByChannel", UNSET)

        as_left_channel_count = d.pop("AsLeftChannelCount", UNSET)

        _as_left_commenced_on = d.pop("AsLeftCommencedOn", UNSET)
        as_left_commenced_on: Union[Unset, datetime.datetime]
        if isinstance(_as_left_commenced_on, Unset):
            as_left_commenced_on = UNSET
        else:
            if _as_left_commenced_on is None:

                as_left_commenced_on = None

            else:

                as_left_commenced_on = isoparse(_as_left_commenced_on)

        as_left_commenced_by = d.pop("AsLeftCommencedBy", UNSET)

        as_left_z_factor = d.pop("AsLeftZFactor", UNSET)

        as_left_air_buoyancy = d.pop("AsLeftAirBuoyancy", UNSET)

        as_left_evaporation_rate = d.pop("AsLeftEvaporationRate", UNSET)

        as_left_ambient_temperature = d.pop("AsLeftAmbientTemperature", UNSET)

        as_left_air_humidity = d.pop("AsLeftAirHumidity", UNSET)

        as_left_barometric_pressure = d.pop("AsLeftBarometricPressure", UNSET)

        as_left_altitude = d.pop("AsLeftAltitude", UNSET)

        as_left_wind_speed = d.pop("AsLeftWindSpeed", UNSET)

        as_left_solar_radiation = d.pop("AsLeftSolarRadiation", UNSET)

        as_left_light_intensity = d.pop("AsLeftLightIntensity", UNSET)

        as_left_noise_level = d.pop("AsLeftNoiseLevel", UNSET)

        as_left_ph_level = d.pop("AsLeftPhLevel", UNSET)

        as_left_water_conductivity = d.pop("AsLeftWaterConductivity", UNSET)

        as_left_water_temperature = d.pop("AsLeftWaterTemperature", UNSET)

        as_left_z_factor_uom = d.pop("AsLeftZFactorUom", UNSET)

        as_left_air_buoyancy_uom = d.pop("AsLeftAirBuoyancyUom", UNSET)

        as_left_evaporation_rate_uom = d.pop("AsLeftEvaporationRateUom", UNSET)

        as_left_ambient_temperature_uom = d.pop("AsLeftAmbientTemperatureUom", UNSET)

        as_left_air_humidity_uom = d.pop("AsLeftAirHumidityUom", UNSET)

        as_left_barometric_pressure_uom = d.pop("AsLeftBarometricPressureUom", UNSET)

        as_left_altitude_uom = d.pop("AsLeftAltitudeUom", UNSET)

        as_left_wind_speed_uom = d.pop("AsLeftWindSpeedUom", UNSET)

        as_left_solar_radiation_uom = d.pop("AsLeftSolarRadiationUom", UNSET)

        as_left_light_intensity_uom = d.pop("AsLeftLightIntensityUom", UNSET)

        as_left_noise_level_uom = d.pop("AsLeftNoiseLevelUom", UNSET)

        as_left_ph_level_uom = d.pop("AsLeftPhLevelUom", UNSET)

        as_left_water_conductivity_uom = d.pop("AsLeftWaterConductivityUom", UNSET)

        as_left_water_temperature_uom = d.pop("AsLeftWaterTemperatureUom", UNSET)

        as_left_specification_name = d.pop("AsLeftSpecificationName", UNSET)

        as_left_parameter_name = d.pop("AsLeftParameterName", UNSET)

        as_left_display_order = d.pop("AsLeftDisplayOrder", UNSET)

        as_left_unit_of_measure = d.pop("AsLeftUnitOfMeasure", UNSET)

        as_left_display_format = d.pop("AsLeftDisplayFormat", UNSET)

        as_left_precision = d.pop("AsLeftPrecision", UNSET)

        _as_left_precision_type = d.pop("AsLeftPrecisionType", UNSET)
        as_left_precision_type: Union[
            Unset,
            QualerApiModelsReportDatasetsToMeasurementAllResponseAsLeftPrecisionType,
        ]
        if isinstance(_as_left_precision_type, Unset):
            as_left_precision_type = UNSET
        else:
            as_left_precision_type = QualerApiModelsReportDatasetsToMeasurementAllResponseAsLeftPrecisionType(
                _as_left_precision_type
            )

        as_left_minimum = d.pop("AsLeftMinimum", UNSET)

        as_left_nominal = d.pop("AsLeftNominal", UNSET)

        as_left_expected_value = d.pop("AsLeftExpectedValue", UNSET)

        as_left_expected_value_raw = d.pop("AsLeftExpectedValueRaw", UNSET)

        as_left_test_value = d.pop("AsLeftTestValue", UNSET)

        as_left_base_value = d.pop("AsLeftBaseValue", UNSET)

        as_left_maxi_mum = d.pop("AsLeftMaxiMum", UNSET)

        as_left_resolution = d.pop("AsLeftResolution", UNSET)

        as_left_resolution_count = d.pop("AsLeftResolutionCount", UNSET)

        _as_left_measurement_not_taken_result = d.pop(
            "AsLeftMeasurementNotTakenResult", UNSET
        )
        as_left_measurement_not_taken_result: Union[
            Unset,
            QualerApiModelsReportDatasetsToMeasurementAllResponseAsLeftMeasurementNotTakenResult,
        ]
        if isinstance(_as_left_measurement_not_taken_result, Unset):
            as_left_measurement_not_taken_result = UNSET
        else:
            as_left_measurement_not_taken_result = QualerApiModelsReportDatasetsToMeasurementAllResponseAsLeftMeasurementNotTakenResult(
                _as_left_measurement_not_taken_result
            )

        as_left_hide_from_certificate = d.pop("AsLeftHideFromCertificate", UNSET)

        as_left_measurement_not_taken_reason = d.pop(
            "AsLeftMeasurementNotTakenReason", UNSET
        )

        as_left_measurement_batch_id = d.pop("AsLeftMeasurementBatchId", UNSET)

        as_left_measurement_id = d.pop("AsLeftMeasurementId", UNSET)

        as_left_standard_id = d.pop("AsLeftStandardId", UNSET)

        as_left_tool_id = d.pop("AsLeftToolId", UNSET)

        as_left_measurement_condition_id = d.pop("AsLeftMeasurementConditionId", UNSET)

        as_left_measurement_point_id = d.pop("AsLeftMeasurementPointId", UNSET)

        qualer_api_models_report_datasets_to_measurement_all_response = cls(
            barcode=barcode,
            display_name=display_name,
            display_part_number=display_part_number,
            part_number=part_number,
            vendor_company_id=vendor_company_id,
            service_order_number=service_order_number,
            completed_by_name=completed_by_name,
            completed_on=completed_on,
            is_limited=is_limited,
            vendor_tag=vendor_tag,
            room=room,
            segment_name=segment_name,
            schedule_name=schedule_name,
            next_segment_name=next_segment_name,
            certificate_number=certificate_number,
            work_status=work_status,
            service_type=service_type,
            service_level=service_level,
            service_comments=service_comments,
            order_item_number=order_item_number,
            service_total=service_total,
            repairs_total=repairs_total,
            parts_total=parts_total,
            asset_tag=asset_tag,
            asset_user=asset_user,
            serial_number=serial_number,
            equipment_id=equipment_id,
            legacy_identifier=legacy_identifier,
            asset_name=asset_name,
            asset_description=asset_description,
            product_name=product_name,
            product_description=product_description,
            asset_maker=asset_maker,
            asset_tag_change=asset_tag_change,
            asset_user_change=asset_user_change,
            serial_number_change=serial_number_change,
            service_date=service_date,
            next_service_date=next_service_date,
            service_order_item_id=service_order_item_id,
            site_name=site_name,
            po_number=po_number,
            shipped_date=shipped_date,
            tracking_number=tracking_number,
            payment_terms=payment_terms,
            shipping_method=shipping_method,
            location=location,
            site_access_notes=site_access_notes,
            as_left_decimal_places=as_left_decimal_places,
            as_left_measurement_set_name=as_left_measurement_set_name,
            as_left_measurement_set_id=as_left_measurement_set_id,
            as_left_adjustment_threshold=as_left_adjustment_threshold,
            as_left_mean_extended=as_left_mean_extended,
            as_left_sd_extended=as_left_sd_extended,
            as_left_range_extended=as_left_range_extended,
            as_left_delta_extended=as_left_delta_extended,
            as_left_cv_extended=as_left_cv_extended,
            as_left_nominal_extended=as_left_nominal_extended,
            as_left_min_max_header=as_left_min_max_header,
            as_left_accuracy_class=as_left_accuracy_class,
            as_left_accuracy_class_min=as_left_accuracy_class_min,
            as_left_accuracy_class_max=as_left_accuracy_class_max,
            as_left_minimum_measured_value=as_left_minimum_measured_value,
            as_left_maxi_mum_measured_value=as_left_maxi_mum_measured_value,
            as_left_min_max_value_extended=as_left_min_max_value_extended,
            as_left_tool_range_name=as_left_tool_range_name,
            as_left_tool_range_uncertainty=as_left_tool_range_uncertainty,
            as_left_primary_tool_last_service_date=as_left_primary_tool_last_service_date,
            as_left_primary_tool_next_service_date=as_left_primary_tool_next_service_date,
            as_left_primary_tool_calibrated_by=as_left_primary_tool_calibrated_by,
            as_left_primary_tool_tool_name=as_left_primary_tool_tool_name,
            as_left_primary_tool_tool_description=as_left_primary_tool_tool_description,
            as_left_primary_tool_tool_type_name=as_left_primary_tool_tool_type_name,
            as_left_primary_tool_manufacturer=as_left_primary_tool_manufacturer,
            as_left_primary_tool_manufacturer_part_number=as_left_primary_tool_manufacturer_part_number,
            as_left_primary_tool_serial_number=as_left_primary_tool_serial_number,
            as_found_measurement_set_name=as_found_measurement_set_name,
            as_found_measurement_set_id=as_found_measurement_set_id,
            as_found_adjustment_threshold=as_found_adjustment_threshold,
            as_found_decimal_places=as_found_decimal_places,
            as_found_mean_extended=as_found_mean_extended,
            as_found_sd_extended=as_found_sd_extended,
            as_found_range_extended=as_found_range_extended,
            as_found_delta_extended=as_found_delta_extended,
            as_found_cv_extended=as_found_cv_extended,
            as_found_nominal_extended=as_found_nominal_extended,
            as_found_min_max_header=as_found_min_max_header,
            as_found_accuracy_class=as_found_accuracy_class,
            as_found_accuracy_class_min=as_found_accuracy_class_min,
            as_found_accuracy_class_max=as_found_accuracy_class_max,
            as_found_minimum_measured_value=as_found_minimum_measured_value,
            as_found_maxi_mum_measured_value=as_found_maxi_mum_measured_value,
            as_found_min_max_value_extended=as_found_min_max_value_extended,
            as_found_tool_range_name=as_found_tool_range_name,
            as_found_tool_range_uncertainty=as_found_tool_range_uncertainty,
            as_found_primary_tool_last_service_date=as_found_primary_tool_last_service_date,
            as_found_primary_tool_next_service_date=as_found_primary_tool_next_service_date,
            as_found_primary_tool_calibrated_by=as_found_primary_tool_calibrated_by,
            as_found_primary_tool_tool_name=as_found_primary_tool_tool_name,
            as_found_primary_tool_tool_description=as_found_primary_tool_tool_description,
            as_found_primary_tool_tool_type_name=as_found_primary_tool_tool_type_name,
            as_found_primary_tool_manufacturer=as_found_primary_tool_manufacturer,
            as_found_primary_tool_manufacturer_part_number=as_found_primary_tool_manufacturer_part_number,
            as_found_primary_tool_serial_number=as_found_primary_tool_serial_number,
            as_left_secondary_tool_last_service_date=as_left_secondary_tool_last_service_date,
            as_left_secondary_tool_next_service_date=as_left_secondary_tool_next_service_date,
            as_left_secondary_tool_calibrated_by=as_left_secondary_tool_calibrated_by,
            as_left_secondary_tool_tool_name=as_left_secondary_tool_tool_name,
            as_left_secondary_tool_tool_description=as_left_secondary_tool_tool_description,
            as_left_secondary_tool_tool_type_name=as_left_secondary_tool_tool_type_name,
            as_left_secondary_tool_manufacturer=as_left_secondary_tool_manufacturer,
            as_left_secondary_tool_manufacturer_part_number=as_left_secondary_tool_manufacturer_part_number,
            as_left_secondary_tool_serial_number=as_left_secondary_tool_serial_number,
            as_found_secondary_tool_last_service_date=as_found_secondary_tool_last_service_date,
            as_found_secondary_tool_next_service_date=as_found_secondary_tool_next_service_date,
            as_found_secondary_tool_calibrated_by=as_found_secondary_tool_calibrated_by,
            as_found_secondary_tool_tool_name=as_found_secondary_tool_tool_name,
            as_found_secondary_tool_tool_description=as_found_secondary_tool_tool_description,
            as_found_secondary_tool_tool_type_name=as_found_secondary_tool_tool_type_name,
            as_found_secondary_tool_manufacturer=as_found_secondary_tool_manufacturer,
            as_found_secondary_tool_manufacturer_part_number=as_found_secondary_tool_manufacturer_part_number,
            as_found_secondary_tool_serial_number=as_found_secondary_tool_serial_number,
            as_found_measurement_not_taken_result=as_found_measurement_not_taken_result,
            as_found_hide_from_certificate=as_found_hide_from_certificate,
            as_found_measurement_not_taken_reason=as_found_measurement_not_taken_reason,
            as_left_values=as_left_values,
            as_left_is_accredited=as_left_is_accredited,
            as_left_is_range_accredited=as_left_is_range_accredited,
            as_found_values=as_found_values,
            as_found_is_accredited=as_found_is_accredited,
            as_found_is_range_accredited=as_found_is_range_accredited,
            as_found_parameter_id=as_found_parameter_id,
            as_found_sd_header=as_found_sd_header,
            as_found_cv_header=as_found_cv_header,
            as_found_measurement_local_time=as_found_measurement_local_time,
            as_found_tur=as_found_tur,
            as_found_tur_raw=as_found_tur_raw,
            as_left_tur=as_left_tur,
            as_left_tur_raw=as_left_tur_raw,
            as_found_tar=as_found_tar,
            as_found_tar_raw=as_found_tar_raw,
            as_left_tar=as_left_tar,
            as_left_tar_raw=as_left_tar_raw,
            as_found_guard_band=as_found_guard_band,
            as_left_guard_band=as_left_guard_band,
            as_found_guard_band_logic=as_found_guard_band_logic,
            as_left_guard_band_logic=as_left_guard_band_logic,
            as_found_error=as_found_error,
            as_found_error_extended=as_found_error_extended,
            as_left_error=as_left_error,
            as_left_error_extended=as_left_error_extended,
            as_found_percent_of_tolerance=as_found_percent_of_tolerance,
            as_found_percent_of_tolerance_extended=as_found_percent_of_tolerance_extended,
            as_left_percent_of_tolerance=as_left_percent_of_tolerance,
            as_left_percent_of_tolerance_extended=as_left_percent_of_tolerance_extended,
            as_found_tolerance_maximum=as_found_tolerance_maximum,
            as_found_tolerance_minimum=as_found_tolerance_minimum,
            as_found_tolerance_type=as_found_tolerance_type,
            as_found_tolerance_mode=as_found_tolerance_mode,
            as_found_tolerance_string=as_found_tolerance_string,
            as_left_tolerance_maximum=as_left_tolerance_maximum,
            as_left_tolerance_minimum=as_left_tolerance_minimum,
            as_left_tolerance_type=as_left_tolerance_type,
            as_left_tolerance_mode=as_left_tolerance_mode,
            as_left_tolerance_string=as_left_tolerance_string,
            as_found_max_hysteresis=as_found_max_hysteresis,
            as_found_run=as_found_run,
            as_found_direction=as_found_direction,
            as_found_hysteresis=as_found_hysteresis,
            as_left_max_hysteresis=as_left_max_hysteresis,
            as_left_run=as_left_run,
            as_left_direction=as_left_direction,
            as_left_hysteresis=as_left_hysteresis,
            as_found_reading_entry_math=as_found_reading_entry_math,
            as_found_reading_entry_math_string=as_found_reading_entry_math_string,
            as_found_value_1=as_found_value_1,
            as_found_value_2=as_found_value_2,
            as_found_value_3=as_found_value_3,
            as_found_value_4=as_found_value_4,
            as_found_value_5=as_found_value_5,
            as_found_value_6=as_found_value_6,
            as_found_value_7=as_found_value_7,
            as_found_value_8=as_found_value_8,
            as_found_value_9=as_found_value_9,
            as_found_value_10=as_found_value_10,
            as_found_value_11=as_found_value_11,
            as_found_value_12=as_found_value_12,
            as_found_value_13=as_found_value_13,
            as_found_value_14=as_found_value_14,
            as_found_value_15=as_found_value_15,
            as_found_value_16=as_found_value_16,
            as_found_value_17=as_found_value_17,
            as_found_value_18=as_found_value_18,
            as_found_value_19=as_found_value_19,
            as_found_value_20=as_found_value_20,
            as_found_value_21=as_found_value_21,
            as_found_value_22=as_found_value_22,
            as_found_value_23=as_found_value_23,
            as_found_value_24=as_found_value_24,
            as_found_value_25=as_found_value_25,
            as_found_value_26=as_found_value_26,
            as_found_value_27=as_found_value_27,
            as_found_value_28=as_found_value_28,
            as_found_value_29=as_found_value_29,
            as_found_value_30=as_found_value_30,
            as_found_value_31=as_found_value_31,
            as_found_value_32=as_found_value_32,
            as_found_value_33=as_found_value_33,
            as_found_value_34=as_found_value_34,
            as_found_value_35=as_found_value_35,
            as_found_value_36=as_found_value_36,
            as_found_value_37=as_found_value_37,
            as_found_value_38=as_found_value_38,
            as_found_value_39=as_found_value_39,
            as_found_value_40=as_found_value_40,
            as_found_raw_value_1=as_found_raw_value_1,
            as_found_raw_value_2=as_found_raw_value_2,
            as_found_raw_value_3=as_found_raw_value_3,
            as_found_raw_value_4=as_found_raw_value_4,
            as_found_raw_value_5=as_found_raw_value_5,
            as_found_raw_value_6=as_found_raw_value_6,
            as_found_raw_value_7=as_found_raw_value_7,
            as_found_raw_value_8=as_found_raw_value_8,
            as_found_raw_value_9=as_found_raw_value_9,
            as_found_raw_value_10=as_found_raw_value_10,
            as_found_raw_value_11=as_found_raw_value_11,
            as_found_raw_value_12=as_found_raw_value_12,
            as_found_raw_value_13=as_found_raw_value_13,
            as_found_raw_value_14=as_found_raw_value_14,
            as_found_raw_value_15=as_found_raw_value_15,
            as_found_raw_value_16=as_found_raw_value_16,
            as_found_raw_value_17=as_found_raw_value_17,
            as_found_raw_value_18=as_found_raw_value_18,
            as_found_raw_value_19=as_found_raw_value_19,
            as_found_raw_value_20=as_found_raw_value_20,
            as_found_raw_value_21=as_found_raw_value_21,
            as_found_raw_value_22=as_found_raw_value_22,
            as_found_raw_value_23=as_found_raw_value_23,
            as_found_raw_value_24=as_found_raw_value_24,
            as_found_raw_value_25=as_found_raw_value_25,
            as_found_raw_value_26=as_found_raw_value_26,
            as_found_raw_value_27=as_found_raw_value_27,
            as_found_raw_value_28=as_found_raw_value_28,
            as_found_raw_value_29=as_found_raw_value_29,
            as_found_raw_value_30=as_found_raw_value_30,
            as_found_raw_value_31=as_found_raw_value_31,
            as_found_raw_value_32=as_found_raw_value_32,
            as_found_raw_value_33=as_found_raw_value_33,
            as_found_raw_value_34=as_found_raw_value_34,
            as_found_raw_value_35=as_found_raw_value_35,
            as_found_raw_value_36=as_found_raw_value_36,
            as_found_raw_value_37=as_found_raw_value_37,
            as_found_raw_value_38=as_found_raw_value_38,
            as_found_raw_value_39=as_found_raw_value_39,
            as_found_raw_value_40=as_found_raw_value_40,
            as_found_value_subtitle_1=as_found_value_subtitle_1,
            as_found_value_subtitle_2=as_found_value_subtitle_2,
            as_found_value_subtitle_3=as_found_value_subtitle_3,
            as_found_value_subtitle_4=as_found_value_subtitle_4,
            as_found_value_subtitle_5=as_found_value_subtitle_5,
            as_found_value_subtitle_6=as_found_value_subtitle_6,
            as_found_value_subtitle_7=as_found_value_subtitle_7,
            as_found_value_subtitle_8=as_found_value_subtitle_8,
            as_found_value_subtitle_9=as_found_value_subtitle_9,
            as_found_value_subtitle_10=as_found_value_subtitle_10,
            as_found_value_subtitle_11=as_found_value_subtitle_11,
            as_found_value_subtitle_12=as_found_value_subtitle_12,
            as_found_value_subtitle_13=as_found_value_subtitle_13,
            as_found_value_subtitle_14=as_found_value_subtitle_14,
            as_found_value_subtitle_15=as_found_value_subtitle_15,
            as_found_value_subtitle_16=as_found_value_subtitle_16,
            as_found_value_subtitle_17=as_found_value_subtitle_17,
            as_found_value_subtitle_18=as_found_value_subtitle_18,
            as_found_value_subtitle_19=as_found_value_subtitle_19,
            as_found_value_subtitle_20=as_found_value_subtitle_20,
            as_found_value_subtitle_21=as_found_value_subtitle_21,
            as_found_value_subtitle_22=as_found_value_subtitle_22,
            as_found_value_subtitle_23=as_found_value_subtitle_23,
            as_found_value_subtitle_24=as_found_value_subtitle_24,
            as_found_value_subtitle_25=as_found_value_subtitle_25,
            as_found_value_subtitle_26=as_found_value_subtitle_26,
            as_found_value_subtitle_27=as_found_value_subtitle_27,
            as_found_value_subtitle_28=as_found_value_subtitle_28,
            as_found_value_subtitle_29=as_found_value_subtitle_29,
            as_found_value_subtitle_30=as_found_value_subtitle_30,
            as_found_value_subtitle_31=as_found_value_subtitle_31,
            as_found_value_subtitle_32=as_found_value_subtitle_32,
            as_found_value_subtitle_33=as_found_value_subtitle_33,
            as_found_value_subtitle_34=as_found_value_subtitle_34,
            as_found_value_subtitle_35=as_found_value_subtitle_35,
            as_found_value_subtitle_36=as_found_value_subtitle_36,
            as_found_value_subtitle_37=as_found_value_subtitle_37,
            as_found_value_subtitle_38=as_found_value_subtitle_38,
            as_found_value_subtitle_39=as_found_value_subtitle_39,
            as_found_value_subtitle_40=as_found_value_subtitle_40,
            as_found_mean=as_found_mean,
            as_found_mean_raw=as_found_mean_raw,
            as_found_sd=as_found_sd,
            as_found_sd_raw=as_found_sd_raw,
            as_found_delta=as_found_delta,
            as_found_range=as_found_range,
            as_found_cv=as_found_cv,
            as_found_cv_raw=as_found_cv_raw,
            as_found_result=as_found_result,
            as_found_range_result=as_found_range_result,
            as_found_delta_result=as_found_delta_result,
            as_found_min_result=as_found_min_result,
            as_found_max_result=as_found_max_result,
            as_found_tar_result=as_found_tar_result,
            as_found_tur_result=as_found_tur_result,
            as_found_error_result=as_found_error_result,
            as_found_sd_result=as_found_sd_result,
            as_found_cv_result=as_found_cv_result,
            as_found_custom_field_result=as_found_custom_field_result,
            as_found_mu=as_found_mu,
            as_found_mu_raw=as_found_mu_raw,
            as_found_mu_effective_dof=as_found_mu_effective_dof,
            as_found_mu_coverage_factor=as_found_mu_coverage_factor,
            as_found_cmc=as_found_cmc,
            as_found_cmc_comments=as_found_cmc_comments,
            as_found_calculated_uncertainty=as_found_calculated_uncertainty,
            as_found_lab_mu=as_found_lab_mu,
            as_found_uncertainty_budget=as_found_uncertainty_budget,
            as_found_mu_extended=as_found_mu_extended,
            as_found_channel=as_found_channel,
            as_found_measurement_type=as_found_measurement_type,
            as_found_updated_by=as_found_updated_by,
            as_found_updated_on=as_found_updated_on,
            as_left_abbreviated_uom=as_left_abbreviated_uom,
            as_left_unit_scale_factor=as_left_unit_scale_factor,
            as_found_specification_title=as_found_specification_title,
            as_found_specification_subtitle=as_found_specification_subtitle,
            as_found_specification_group=as_found_specification_group,
            as_found_batch_type=as_found_batch_type,
            as_found_batch_result=as_found_batch_result,
            as_found_is_by_channel=as_found_is_by_channel,
            as_found_channel_count=as_found_channel_count,
            as_found_commenced_on=as_found_commenced_on,
            as_found_commenced_by=as_found_commenced_by,
            as_found_z_factor=as_found_z_factor,
            as_found_air_buoyancy=as_found_air_buoyancy,
            as_found_evaporation_rate=as_found_evaporation_rate,
            as_found_ambient_temperature=as_found_ambient_temperature,
            as_found_air_humidity=as_found_air_humidity,
            as_found_barometric_pressure=as_found_barometric_pressure,
            as_found_altitude=as_found_altitude,
            as_found_wind_speed=as_found_wind_speed,
            as_found_solar_radiation=as_found_solar_radiation,
            as_found_light_intensity=as_found_light_intensity,
            as_found_noise_level=as_found_noise_level,
            as_found_ph_level=as_found_ph_level,
            as_found_water_conductivity=as_found_water_conductivity,
            as_found_water_temperature=as_found_water_temperature,
            as_found_z_factor_uom=as_found_z_factor_uom,
            as_found_air_buoyancy_uom=as_found_air_buoyancy_uom,
            as_found_evaporation_rate_uom=as_found_evaporation_rate_uom,
            as_found_ambient_temperature_uom=as_found_ambient_temperature_uom,
            as_found_air_humidity_uom=as_found_air_humidity_uom,
            as_found_barometric_pressure_uom=as_found_barometric_pressure_uom,
            as_found_altitude_uom=as_found_altitude_uom,
            as_found_wind_speed_uom=as_found_wind_speed_uom,
            as_found_solar_radiation_uom=as_found_solar_radiation_uom,
            as_found_light_intensity_uom=as_found_light_intensity_uom,
            as_found_noise_level_uom=as_found_noise_level_uom,
            as_found_ph_level_uom=as_found_ph_level_uom,
            as_found_water_conductivity_uom=as_found_water_conductivity_uom,
            as_found_water_temperature_uom=as_found_water_temperature_uom,
            as_found_abbreviated_uom=as_found_abbreviated_uom,
            as_found_unit_scale_factor=as_found_unit_scale_factor,
            as_found_specification_name=as_found_specification_name,
            as_found_parameter_name=as_found_parameter_name,
            as_found_display_order=as_found_display_order,
            as_found_unit_of_measure=as_found_unit_of_measure,
            as_found_display_format=as_found_display_format,
            as_found_precision=as_found_precision,
            as_found_precision_type=as_found_precision_type,
            as_found_minimum=as_found_minimum,
            as_found_nominal=as_found_nominal,
            as_found_expected_value=as_found_expected_value,
            as_found_expected_value_raw=as_found_expected_value_raw,
            as_found_test_value=as_found_test_value,
            as_found_base_value=as_found_base_value,
            as_found_maxi_mum=as_found_maxi_mum,
            as_found_resolution=as_found_resolution,
            as_found_resolution_count=as_found_resolution_count,
            as_found_measurement_batch_id=as_found_measurement_batch_id,
            as_found_measurement_id=as_found_measurement_id,
            as_found_standard_id=as_found_standard_id,
            as_found_tool_id=as_found_tool_id,
            as_found_measurement_condition_id=as_found_measurement_condition_id,
            as_found_measurement_point_id=as_found_measurement_point_id,
            as_left_parameter_id=as_left_parameter_id,
            as_left_sd_header=as_left_sd_header,
            as_left_cv_header=as_left_cv_header,
            as_left_measurement_local_time=as_left_measurement_local_time,
            as_left_reading_entry_math=as_left_reading_entry_math,
            as_left_reading_entry_math_string=as_left_reading_entry_math_string,
            as_left_value_1=as_left_value_1,
            as_left_value_2=as_left_value_2,
            as_left_value_3=as_left_value_3,
            as_left_value_4=as_left_value_4,
            as_left_value_5=as_left_value_5,
            as_left_value_6=as_left_value_6,
            as_left_value_7=as_left_value_7,
            as_left_value_8=as_left_value_8,
            as_left_value_9=as_left_value_9,
            as_left_value_10=as_left_value_10,
            as_left_value_11=as_left_value_11,
            as_left_value_12=as_left_value_12,
            as_left_value_13=as_left_value_13,
            as_left_value_14=as_left_value_14,
            as_left_value_15=as_left_value_15,
            as_left_value_16=as_left_value_16,
            as_left_value_17=as_left_value_17,
            as_left_value_18=as_left_value_18,
            as_left_value_19=as_left_value_19,
            as_left_value_20=as_left_value_20,
            as_left_value_21=as_left_value_21,
            as_left_value_22=as_left_value_22,
            as_left_value_23=as_left_value_23,
            as_left_value_24=as_left_value_24,
            as_left_value_25=as_left_value_25,
            as_left_value_26=as_left_value_26,
            as_left_value_27=as_left_value_27,
            as_left_value_28=as_left_value_28,
            as_left_value_29=as_left_value_29,
            as_left_value_30=as_left_value_30,
            as_left_value_31=as_left_value_31,
            as_left_value_32=as_left_value_32,
            as_left_value_33=as_left_value_33,
            as_left_value_34=as_left_value_34,
            as_left_value_35=as_left_value_35,
            as_left_value_36=as_left_value_36,
            as_left_value_37=as_left_value_37,
            as_left_value_38=as_left_value_38,
            as_left_value_39=as_left_value_39,
            as_left_value_40=as_left_value_40,
            as_left_raw_value_1=as_left_raw_value_1,
            as_left_raw_value_2=as_left_raw_value_2,
            as_left_raw_value_3=as_left_raw_value_3,
            as_left_raw_value_4=as_left_raw_value_4,
            as_left_raw_value_5=as_left_raw_value_5,
            as_left_raw_value_6=as_left_raw_value_6,
            as_left_raw_value_7=as_left_raw_value_7,
            as_left_raw_value_8=as_left_raw_value_8,
            as_left_raw_value_9=as_left_raw_value_9,
            as_left_raw_value_10=as_left_raw_value_10,
            as_left_raw_value_11=as_left_raw_value_11,
            as_left_raw_value_12=as_left_raw_value_12,
            as_left_raw_value_13=as_left_raw_value_13,
            as_left_raw_value_14=as_left_raw_value_14,
            as_left_raw_value_15=as_left_raw_value_15,
            as_left_raw_value_16=as_left_raw_value_16,
            as_left_raw_value_17=as_left_raw_value_17,
            as_left_raw_value_18=as_left_raw_value_18,
            as_left_raw_value_19=as_left_raw_value_19,
            as_left_raw_value_20=as_left_raw_value_20,
            as_left_raw_value_21=as_left_raw_value_21,
            as_left_raw_value_22=as_left_raw_value_22,
            as_left_raw_value_23=as_left_raw_value_23,
            as_left_raw_value_24=as_left_raw_value_24,
            as_left_raw_value_25=as_left_raw_value_25,
            as_left_raw_value_26=as_left_raw_value_26,
            as_left_raw_value_27=as_left_raw_value_27,
            as_left_raw_value_28=as_left_raw_value_28,
            as_left_raw_value_29=as_left_raw_value_29,
            as_left_raw_value_30=as_left_raw_value_30,
            as_left_raw_value_31=as_left_raw_value_31,
            as_left_raw_value_32=as_left_raw_value_32,
            as_left_raw_value_33=as_left_raw_value_33,
            as_left_raw_value_34=as_left_raw_value_34,
            as_left_raw_value_35=as_left_raw_value_35,
            as_left_raw_value_36=as_left_raw_value_36,
            as_left_raw_value_37=as_left_raw_value_37,
            as_left_raw_value_38=as_left_raw_value_38,
            as_left_raw_value_39=as_left_raw_value_39,
            as_left_raw_value_40=as_left_raw_value_40,
            as_left_value_subtitle_1=as_left_value_subtitle_1,
            as_left_value_subtitle_2=as_left_value_subtitle_2,
            as_left_value_subtitle_3=as_left_value_subtitle_3,
            as_left_value_subtitle_4=as_left_value_subtitle_4,
            as_left_value_subtitle_5=as_left_value_subtitle_5,
            as_left_value_subtitle_6=as_left_value_subtitle_6,
            as_left_value_subtitle_7=as_left_value_subtitle_7,
            as_left_value_subtitle_8=as_left_value_subtitle_8,
            as_left_value_subtitle_9=as_left_value_subtitle_9,
            as_left_value_subtitle_10=as_left_value_subtitle_10,
            as_left_value_subtitle_11=as_left_value_subtitle_11,
            as_left_value_subtitle_12=as_left_value_subtitle_12,
            as_left_value_subtitle_13=as_left_value_subtitle_13,
            as_left_value_subtitle_14=as_left_value_subtitle_14,
            as_left_value_subtitle_15=as_left_value_subtitle_15,
            as_left_value_subtitle_16=as_left_value_subtitle_16,
            as_left_value_subtitle_17=as_left_value_subtitle_17,
            as_left_value_subtitle_18=as_left_value_subtitle_18,
            as_left_value_subtitle_19=as_left_value_subtitle_19,
            as_left_value_subtitle_20=as_left_value_subtitle_20,
            as_left_value_subtitle_21=as_left_value_subtitle_21,
            as_left_value_subtitle_22=as_left_value_subtitle_22,
            as_left_value_subtitle_23=as_left_value_subtitle_23,
            as_left_value_subtitle_24=as_left_value_subtitle_24,
            as_left_value_subtitle_25=as_left_value_subtitle_25,
            as_left_value_subtitle_26=as_left_value_subtitle_26,
            as_left_value_subtitle_27=as_left_value_subtitle_27,
            as_left_value_subtitle_28=as_left_value_subtitle_28,
            as_left_value_subtitle_29=as_left_value_subtitle_29,
            as_left_value_subtitle_30=as_left_value_subtitle_30,
            as_left_value_subtitle_31=as_left_value_subtitle_31,
            as_left_value_subtitle_32=as_left_value_subtitle_32,
            as_left_value_subtitle_33=as_left_value_subtitle_33,
            as_left_value_subtitle_34=as_left_value_subtitle_34,
            as_left_value_subtitle_35=as_left_value_subtitle_35,
            as_left_value_subtitle_36=as_left_value_subtitle_36,
            as_left_value_subtitle_37=as_left_value_subtitle_37,
            as_left_value_subtitle_38=as_left_value_subtitle_38,
            as_left_value_subtitle_39=as_left_value_subtitle_39,
            as_left_value_subtitle_40=as_left_value_subtitle_40,
            as_left_mean=as_left_mean,
            as_left_mean_raw=as_left_mean_raw,
            as_left_sd=as_left_sd,
            as_left_sd_raw=as_left_sd_raw,
            as_left_cv=as_left_cv,
            as_left_cv_raw=as_left_cv_raw,
            as_left_delta=as_left_delta,
            as_left_range=as_left_range,
            as_left_result=as_left_result,
            as_left_range_result=as_left_range_result,
            as_left_delta_result=as_left_delta_result,
            as_left_min_result=as_left_min_result,
            as_left_max_result=as_left_max_result,
            as_left_tar_result=as_left_tar_result,
            as_left_tur_result=as_left_tur_result,
            as_left_error_result=as_left_error_result,
            as_left_sd_result=as_left_sd_result,
            as_left_cv_result=as_left_cv_result,
            as_left_custom_field_result=as_left_custom_field_result,
            as_left_mu=as_left_mu,
            as_left_mu_raw=as_left_mu_raw,
            as_left_mu_effective_dof=as_left_mu_effective_dof,
            as_left_mu_coverage_factor=as_left_mu_coverage_factor,
            as_left_cmc=as_left_cmc,
            as_left_cmc_comments=as_left_cmc_comments,
            as_left_calculated_uncertainty=as_left_calculated_uncertainty,
            as_left_lab_mu=as_left_lab_mu,
            as_left_uncertainty_budget=as_left_uncertainty_budget,
            as_left_mu_extended=as_left_mu_extended,
            as_left_channel=as_left_channel,
            as_left_measurement_type=as_left_measurement_type,
            as_left_updated_by=as_left_updated_by,
            as_left_updated_on=as_left_updated_on,
            as_left_specification_title=as_left_specification_title,
            as_left_specification_subtitle=as_left_specification_subtitle,
            as_left_specification_group=as_left_specification_group,
            as_left_batch_type=as_left_batch_type,
            as_left_batch_result=as_left_batch_result,
            as_left_is_by_channel=as_left_is_by_channel,
            as_left_channel_count=as_left_channel_count,
            as_left_commenced_on=as_left_commenced_on,
            as_left_commenced_by=as_left_commenced_by,
            as_left_z_factor=as_left_z_factor,
            as_left_air_buoyancy=as_left_air_buoyancy,
            as_left_evaporation_rate=as_left_evaporation_rate,
            as_left_ambient_temperature=as_left_ambient_temperature,
            as_left_air_humidity=as_left_air_humidity,
            as_left_barometric_pressure=as_left_barometric_pressure,
            as_left_altitude=as_left_altitude,
            as_left_wind_speed=as_left_wind_speed,
            as_left_solar_radiation=as_left_solar_radiation,
            as_left_light_intensity=as_left_light_intensity,
            as_left_noise_level=as_left_noise_level,
            as_left_ph_level=as_left_ph_level,
            as_left_water_conductivity=as_left_water_conductivity,
            as_left_water_temperature=as_left_water_temperature,
            as_left_z_factor_uom=as_left_z_factor_uom,
            as_left_air_buoyancy_uom=as_left_air_buoyancy_uom,
            as_left_evaporation_rate_uom=as_left_evaporation_rate_uom,
            as_left_ambient_temperature_uom=as_left_ambient_temperature_uom,
            as_left_air_humidity_uom=as_left_air_humidity_uom,
            as_left_barometric_pressure_uom=as_left_barometric_pressure_uom,
            as_left_altitude_uom=as_left_altitude_uom,
            as_left_wind_speed_uom=as_left_wind_speed_uom,
            as_left_solar_radiation_uom=as_left_solar_radiation_uom,
            as_left_light_intensity_uom=as_left_light_intensity_uom,
            as_left_noise_level_uom=as_left_noise_level_uom,
            as_left_ph_level_uom=as_left_ph_level_uom,
            as_left_water_conductivity_uom=as_left_water_conductivity_uom,
            as_left_water_temperature_uom=as_left_water_temperature_uom,
            as_left_specification_name=as_left_specification_name,
            as_left_parameter_name=as_left_parameter_name,
            as_left_display_order=as_left_display_order,
            as_left_unit_of_measure=as_left_unit_of_measure,
            as_left_display_format=as_left_display_format,
            as_left_precision=as_left_precision,
            as_left_precision_type=as_left_precision_type,
            as_left_minimum=as_left_minimum,
            as_left_nominal=as_left_nominal,
            as_left_expected_value=as_left_expected_value,
            as_left_expected_value_raw=as_left_expected_value_raw,
            as_left_test_value=as_left_test_value,
            as_left_base_value=as_left_base_value,
            as_left_maxi_mum=as_left_maxi_mum,
            as_left_resolution=as_left_resolution,
            as_left_resolution_count=as_left_resolution_count,
            as_left_measurement_not_taken_result=as_left_measurement_not_taken_result,
            as_left_hide_from_certificate=as_left_hide_from_certificate,
            as_left_measurement_not_taken_reason=as_left_measurement_not_taken_reason,
            as_left_measurement_batch_id=as_left_measurement_batch_id,
            as_left_measurement_id=as_left_measurement_id,
            as_left_standard_id=as_left_standard_id,
            as_left_tool_id=as_left_tool_id,
            as_left_measurement_condition_id=as_left_measurement_condition_id,
            as_left_measurement_point_id=as_left_measurement_point_id,
        )

        qualer_api_models_report_datasets_to_measurement_all_response.additional_properties = (
            d
        )
        return qualer_api_models_report_datasets_to_measurement_all_response

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
