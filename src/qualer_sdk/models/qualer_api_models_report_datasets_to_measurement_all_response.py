import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.qualer_api_models_report_datasets_to_measurement_all_response_as_found_guard_band_logic import (
    ReportDatasetsToMeasurementAllResponseAsFoundGuardBandLogic,
)
from ..models.qualer_api_models_report_datasets_to_measurement_all_response_as_found_measurement_not_taken_result import (
    ReportDatasetsToMeasurementAllResponseAsFoundMeasurementNotTakenResult,
)
from ..models.qualer_api_models_report_datasets_to_measurement_all_response_as_found_measurement_type import (
    ReportDatasetsToMeasurementAllResponseAsFoundMeasurementType,
)
from ..models.qualer_api_models_report_datasets_to_measurement_all_response_as_found_precision_type import (
    ReportDatasetsToMeasurementAllResponseAsFoundPrecisionType,
)
from ..models.qualer_api_models_report_datasets_to_measurement_all_response_as_found_reading_entry_math import (
    ReportDatasetsToMeasurementAllResponseAsFoundReadingEntryMath,
)
from ..models.qualer_api_models_report_datasets_to_measurement_all_response_as_left_guard_band_logic import (
    ReportDatasetsToMeasurementAllResponseAsLeftGuardBandLogic,
)
from ..models.qualer_api_models_report_datasets_to_measurement_all_response_as_left_measurement_not_taken_result import (
    ReportDatasetsToMeasurementAllResponseAsLeftMeasurementNotTakenResult,
)
from ..models.qualer_api_models_report_datasets_to_measurement_all_response_as_left_measurement_type import (
    ReportDatasetsToMeasurementAllResponseAsLeftMeasurementType,
)
from ..models.qualer_api_models_report_datasets_to_measurement_all_response_as_left_precision_type import (
    ReportDatasetsToMeasurementAllResponseAsLeftPrecisionType,
)
from ..models.qualer_api_models_report_datasets_to_measurement_all_response_as_left_reading_entry_math import (
    ReportDatasetsToMeasurementAllResponseAsLeftReadingEntryMath,
)
from ..models.work_status import WorkStatus

T = TypeVar("T", bound="ReportDatasetsToMeasurementAllResponse")


@_attrs_define
class ReportDatasetsToMeasurementAllResponse:
    barcode: Optional[str] = None
    display_name: Optional[str] = None
    display_part_number: Optional[str] = None
    part_number: Optional[str] = None
    vendor_company_id: Optional[int] = None
    service_order_number: Optional[int] = None
    completed_by_name: Optional[str] = None
    completed_on: Optional[datetime.datetime] = None
    is_limited: Optional[bool] = None
    vendor_tag: Optional[str] = None
    room: Optional[str] = None
    segment_name: Optional[str] = None
    schedule_name: Optional[str] = None
    next_segment_name: Optional[str] = None
    certificate_number: Optional[str] = None
    work_status: Optional[WorkStatus] = None
    service_type: Optional[str] = None
    service_level: Optional[str] = None
    service_comments: Optional[str] = None
    order_item_number: Optional[int] = None
    service_total: Optional[float] = None
    repairs_total: Optional[float] = None
    parts_total: Optional[float] = None
    asset_tag: Optional[str] = None
    asset_user: Optional[str] = None
    serial_number: Optional[str] = None
    equipment_id: Optional[str] = None
    legacy_identifier: Optional[str] = None
    asset_name: Optional[str] = None
    asset_description: Optional[str] = None
    product_name: Optional[str] = None
    product_description: Optional[str] = None
    asset_maker: Optional[str] = None
    asset_tag_change: Optional[str] = None
    asset_user_change: Optional[str] = None
    serial_number_change: Optional[str] = None
    service_date: Optional[datetime.datetime] = None
    next_service_date: Optional[datetime.datetime] = None
    service_order_item_id: Optional[int] = None
    site_name: Optional[str] = None
    po_number: Optional[str] = None
    shipped_date: Optional[datetime.datetime] = None
    tracking_number: Optional[str] = None
    payment_terms: Optional[int] = None
    shipping_method: Optional[str] = None
    location: Optional[str] = None
    site_access_notes: Optional[str] = None
    as_left_decimal_places: Optional[int] = None
    as_left_measurement_set_name: Optional[str] = None
    as_left_measurement_set_id: Optional[int] = None
    as_left_adjustment_threshold: Optional[float] = None
    as_left_mean_extended: Optional[str] = None
    as_left_sd_extended: Optional[str] = None
    as_left_range_extended: Optional[str] = None
    as_left_delta_extended: Optional[str] = None
    as_left_cv_extended: Optional[str] = None
    as_left_nominal_extended: Optional[str] = None
    as_left_min_max_header: Optional[str] = None
    as_left_accuracy_class: Optional[str] = None
    as_left_accuracy_class_min: Optional[float] = None
    as_left_accuracy_class_max: Optional[float] = None
    as_left_minimum_measured_value: Optional[float] = None
    as_left_maxi_mum_measured_value: Optional[float] = None
    as_left_min_max_value_extended: Optional[str] = None
    as_left_tool_range_name: Optional[str] = None
    as_left_tool_range_uncertainty: Optional[str] = None
    as_left_primary_tool_last_service_date: Optional[datetime.datetime] = None
    as_left_primary_tool_next_service_date: Optional[datetime.datetime] = None
    as_left_primary_tool_calibrated_by: Optional[str] = None
    as_left_primary_tool_tool_name: Optional[str] = None
    as_left_primary_tool_tool_description: Optional[str] = None
    as_left_primary_tool_tool_type_name: Optional[str] = None
    as_left_primary_tool_manufacturer: Optional[str] = None
    as_left_primary_tool_manufacturer_part_number: Optional[str] = None
    as_left_primary_tool_serial_number: Optional[str] = None
    as_found_measurement_set_name: Optional[str] = None
    as_found_measurement_set_id: Optional[int] = None
    as_found_adjustment_threshold: Optional[float] = None
    as_found_decimal_places: Optional[int] = None
    as_found_mean_extended: Optional[str] = None
    as_found_sd_extended: Optional[str] = None
    as_found_range_extended: Optional[str] = None
    as_found_delta_extended: Optional[str] = None
    as_found_cv_extended: Optional[str] = None
    as_found_nominal_extended: Optional[str] = None
    as_found_min_max_header: Optional[str] = None
    as_found_accuracy_class: Optional[str] = None
    as_found_accuracy_class_min: Optional[float] = None
    as_found_accuracy_class_max: Optional[float] = None
    as_found_minimum_measured_value: Optional[float] = None
    as_found_maxi_mum_measured_value: Optional[float] = None
    as_found_min_max_value_extended: Optional[str] = None
    as_found_tool_range_name: Optional[str] = None
    as_found_tool_range_uncertainty: Optional[str] = None
    as_found_primary_tool_last_service_date: Optional[datetime.datetime] = None
    as_found_primary_tool_next_service_date: Optional[datetime.datetime] = None
    as_found_primary_tool_calibrated_by: Optional[str] = None
    as_found_primary_tool_tool_name: Optional[str] = None
    as_found_primary_tool_tool_description: Optional[str] = None
    as_found_primary_tool_tool_type_name: Optional[str] = None
    as_found_primary_tool_manufacturer: Optional[str] = None
    as_found_primary_tool_manufacturer_part_number: Optional[str] = None
    as_found_primary_tool_serial_number: Optional[str] = None
    as_left_secondary_tool_last_service_date: Optional[datetime.datetime] = None
    as_left_secondary_tool_next_service_date: Optional[datetime.datetime] = None
    as_left_secondary_tool_calibrated_by: Optional[str] = None
    as_left_secondary_tool_tool_name: Optional[str] = None
    as_left_secondary_tool_tool_description: Optional[str] = None
    as_left_secondary_tool_tool_type_name: Optional[str] = None
    as_left_secondary_tool_manufacturer: Optional[str] = None
    as_left_secondary_tool_manufacturer_part_number: Optional[str] = None
    as_left_secondary_tool_serial_number: Optional[str] = None
    as_found_secondary_tool_last_service_date: Optional[datetime.datetime] = None
    as_found_secondary_tool_next_service_date: Optional[datetime.datetime] = None
    as_found_secondary_tool_calibrated_by: Optional[str] = None
    as_found_secondary_tool_tool_name: Optional[str] = None
    as_found_secondary_tool_tool_description: Optional[str] = None
    as_found_secondary_tool_tool_type_name: Optional[str] = None
    as_found_secondary_tool_manufacturer: Optional[str] = None
    as_found_secondary_tool_manufacturer_part_number: Optional[str] = None
    as_found_secondary_tool_serial_number: Optional[str] = None
    as_found_measurement_not_taken_result: Optional[
        ReportDatasetsToMeasurementAllResponseAsFoundMeasurementNotTakenResult
    ] = None
    as_found_hide_from_certificate: Optional[bool] = None
    as_found_measurement_not_taken_reason: Optional[str] = None
    as_left_values: Optional[str] = None
    as_left_is_accredited: Optional[bool] = None
    as_left_is_range_accredited: Optional[bool] = None
    as_found_values: Optional[str] = None
    as_found_is_accredited: Optional[bool] = None
    as_found_is_range_accredited: Optional[bool] = None
    as_found_parameter_id: Optional[int] = None
    as_found_sd_header: Optional[float] = None
    as_found_cv_header: Optional[float] = None
    as_found_measurement_local_time: Optional[datetime.datetime] = None
    as_found_tur: Optional[float] = None
    as_found_tur_raw: Optional[float] = None
    as_left_tur: Optional[float] = None
    as_left_tur_raw: Optional[float] = None
    as_found_tar: Optional[float] = None
    as_found_tar_raw: Optional[float] = None
    as_left_tar: Optional[float] = None
    as_left_tar_raw: Optional[float] = None
    as_found_guard_band: Optional[str] = None
    as_left_guard_band: Optional[str] = None
    as_found_guard_band_logic: Optional[
        ReportDatasetsToMeasurementAllResponseAsFoundGuardBandLogic
    ] = None
    as_left_guard_band_logic: Optional[
        ReportDatasetsToMeasurementAllResponseAsLeftGuardBandLogic
    ] = None
    as_found_error: Optional[float] = None
    as_found_error_extended: Optional[str] = None
    as_left_error: Optional[float] = None
    as_left_error_extended: Optional[str] = None
    as_found_percent_of_tolerance: Optional[float] = None
    as_found_percent_of_tolerance_extended: Optional[str] = None
    as_left_percent_of_tolerance: Optional[float] = None
    as_left_percent_of_tolerance_extended: Optional[str] = None
    as_found_tolerance_maximum: Optional[float] = None
    as_found_tolerance_minimum: Optional[float] = None
    as_found_tolerance_type: Optional[int] = None
    as_found_tolerance_mode: Optional[int] = None
    as_found_tolerance_string: Optional[str] = None
    as_left_tolerance_maximum: Optional[float] = None
    as_left_tolerance_minimum: Optional[float] = None
    as_left_tolerance_type: Optional[int] = None
    as_left_tolerance_mode: Optional[int] = None
    as_left_tolerance_string: Optional[str] = None
    as_found_max_hysteresis: Optional[float] = None
    as_found_run: Optional[int] = None
    as_found_direction: Optional[int] = None
    as_found_hysteresis: Optional[float] = None
    as_left_max_hysteresis: Optional[float] = None
    as_left_run: Optional[int] = None
    as_left_direction: Optional[int] = None
    as_left_hysteresis: Optional[float] = None
    as_found_reading_entry_math: Optional[
        ReportDatasetsToMeasurementAllResponseAsFoundReadingEntryMath
    ] = None
    as_found_reading_entry_math_string: Optional[str] = None
    as_found_value_1: Optional[str] = None
    as_found_value_2: Optional[str] = None
    as_found_value_3: Optional[str] = None
    as_found_value_4: Optional[str] = None
    as_found_value_5: Optional[str] = None
    as_found_value_6: Optional[str] = None
    as_found_value_7: Optional[str] = None
    as_found_value_8: Optional[str] = None
    as_found_value_9: Optional[str] = None
    as_found_value_10: Optional[str] = None
    as_found_value_11: Optional[str] = None
    as_found_value_12: Optional[str] = None
    as_found_value_13: Optional[str] = None
    as_found_value_14: Optional[str] = None
    as_found_value_15: Optional[str] = None
    as_found_value_16: Optional[str] = None
    as_found_value_17: Optional[str] = None
    as_found_value_18: Optional[str] = None
    as_found_value_19: Optional[str] = None
    as_found_value_20: Optional[str] = None
    as_found_value_21: Optional[str] = None
    as_found_value_22: Optional[str] = None
    as_found_value_23: Optional[str] = None
    as_found_value_24: Optional[str] = None
    as_found_value_25: Optional[str] = None
    as_found_value_26: Optional[str] = None
    as_found_value_27: Optional[str] = None
    as_found_value_28: Optional[str] = None
    as_found_value_29: Optional[str] = None
    as_found_value_30: Optional[str] = None
    as_found_value_31: Optional[str] = None
    as_found_value_32: Optional[str] = None
    as_found_value_33: Optional[str] = None
    as_found_value_34: Optional[str] = None
    as_found_value_35: Optional[str] = None
    as_found_value_36: Optional[str] = None
    as_found_value_37: Optional[str] = None
    as_found_value_38: Optional[str] = None
    as_found_value_39: Optional[str] = None
    as_found_value_40: Optional[str] = None
    as_found_raw_value_1: Optional[str] = None
    as_found_raw_value_2: Optional[str] = None
    as_found_raw_value_3: Optional[str] = None
    as_found_raw_value_4: Optional[str] = None
    as_found_raw_value_5: Optional[str] = None
    as_found_raw_value_6: Optional[str] = None
    as_found_raw_value_7: Optional[str] = None
    as_found_raw_value_8: Optional[str] = None
    as_found_raw_value_9: Optional[str] = None
    as_found_raw_value_10: Optional[str] = None
    as_found_raw_value_11: Optional[str] = None
    as_found_raw_value_12: Optional[str] = None
    as_found_raw_value_13: Optional[str] = None
    as_found_raw_value_14: Optional[str] = None
    as_found_raw_value_15: Optional[str] = None
    as_found_raw_value_16: Optional[str] = None
    as_found_raw_value_17: Optional[str] = None
    as_found_raw_value_18: Optional[str] = None
    as_found_raw_value_19: Optional[str] = None
    as_found_raw_value_20: Optional[str] = None
    as_found_raw_value_21: Optional[str] = None
    as_found_raw_value_22: Optional[str] = None
    as_found_raw_value_23: Optional[str] = None
    as_found_raw_value_24: Optional[str] = None
    as_found_raw_value_25: Optional[str] = None
    as_found_raw_value_26: Optional[str] = None
    as_found_raw_value_27: Optional[str] = None
    as_found_raw_value_28: Optional[str] = None
    as_found_raw_value_29: Optional[str] = None
    as_found_raw_value_30: Optional[str] = None
    as_found_raw_value_31: Optional[str] = None
    as_found_raw_value_32: Optional[str] = None
    as_found_raw_value_33: Optional[str] = None
    as_found_raw_value_34: Optional[str] = None
    as_found_raw_value_35: Optional[str] = None
    as_found_raw_value_36: Optional[str] = None
    as_found_raw_value_37: Optional[str] = None
    as_found_raw_value_38: Optional[str] = None
    as_found_raw_value_39: Optional[str] = None
    as_found_raw_value_40: Optional[str] = None
    as_found_value_subtitle_1: Optional[str] = None
    as_found_value_subtitle_2: Optional[str] = None
    as_found_value_subtitle_3: Optional[str] = None
    as_found_value_subtitle_4: Optional[str] = None
    as_found_value_subtitle_5: Optional[str] = None
    as_found_value_subtitle_6: Optional[str] = None
    as_found_value_subtitle_7: Optional[str] = None
    as_found_value_subtitle_8: Optional[str] = None
    as_found_value_subtitle_9: Optional[str] = None
    as_found_value_subtitle_10: Optional[str] = None
    as_found_value_subtitle_11: Optional[str] = None
    as_found_value_subtitle_12: Optional[str] = None
    as_found_value_subtitle_13: Optional[str] = None
    as_found_value_subtitle_14: Optional[str] = None
    as_found_value_subtitle_15: Optional[str] = None
    as_found_value_subtitle_16: Optional[str] = None
    as_found_value_subtitle_17: Optional[str] = None
    as_found_value_subtitle_18: Optional[str] = None
    as_found_value_subtitle_19: Optional[str] = None
    as_found_value_subtitle_20: Optional[str] = None
    as_found_value_subtitle_21: Optional[str] = None
    as_found_value_subtitle_22: Optional[str] = None
    as_found_value_subtitle_23: Optional[str] = None
    as_found_value_subtitle_24: Optional[str] = None
    as_found_value_subtitle_25: Optional[str] = None
    as_found_value_subtitle_26: Optional[str] = None
    as_found_value_subtitle_27: Optional[str] = None
    as_found_value_subtitle_28: Optional[str] = None
    as_found_value_subtitle_29: Optional[str] = None
    as_found_value_subtitle_30: Optional[str] = None
    as_found_value_subtitle_31: Optional[str] = None
    as_found_value_subtitle_32: Optional[str] = None
    as_found_value_subtitle_33: Optional[str] = None
    as_found_value_subtitle_34: Optional[str] = None
    as_found_value_subtitle_35: Optional[str] = None
    as_found_value_subtitle_36: Optional[str] = None
    as_found_value_subtitle_37: Optional[str] = None
    as_found_value_subtitle_38: Optional[str] = None
    as_found_value_subtitle_39: Optional[str] = None
    as_found_value_subtitle_40: Optional[str] = None
    as_found_mean: Optional[float] = None
    as_found_mean_raw: Optional[float] = None
    as_found_sd: Optional[float] = None
    as_found_sd_raw: Optional[float] = None
    as_found_delta: Optional[float] = None
    as_found_range: Optional[float] = None
    as_found_cv: Optional[float] = None
    as_found_cv_raw: Optional[float] = None
    as_found_result: Optional[int] = None
    as_found_range_result: Optional[bool] = None
    as_found_delta_result: Optional[bool] = None
    as_found_min_result: Optional[bool] = None
    as_found_max_result: Optional[bool] = None
    as_found_tar_result: Optional[bool] = None
    as_found_tur_result: Optional[bool] = None
    as_found_error_result: Optional[bool] = None
    as_found_sd_result: Optional[bool] = None
    as_found_cv_result: Optional[bool] = None
    as_found_custom_field_result: Optional[int] = None
    as_found_mu: Optional[float] = None
    as_found_mu_raw: Optional[float] = None
    as_found_mu_effective_dof: Optional[float] = None
    as_found_mu_coverage_factor: Optional[float] = None
    as_found_cmc: Optional[float] = None
    as_found_cmc_comments: Optional[str] = None
    as_found_calculated_uncertainty: Optional[float] = None
    as_found_lab_mu: Optional[float] = None
    as_found_uncertainty_budget: Optional[str] = None
    as_found_mu_extended: Optional[str] = None
    as_found_channel: Optional[int] = None
    as_found_measurement_type: Optional[
        ReportDatasetsToMeasurementAllResponseAsFoundMeasurementType
    ] = None
    as_found_updated_by: Optional[str] = None
    as_found_updated_on: Optional[datetime.datetime] = None
    as_left_abbreviated_uom: Optional[str] = None
    as_left_unit_scale_factor: Optional[float] = None
    as_found_specification_title: Optional[str] = None
    as_found_specification_subtitle: Optional[str] = None
    as_found_specification_group: Optional[str] = None
    as_found_batch_type: Optional[int] = None
    as_found_batch_result: Optional[int] = None
    as_found_is_by_channel: Optional[bool] = None
    as_found_channel_count: Optional[int] = None
    as_found_commenced_on: Optional[datetime.datetime] = None
    as_found_commenced_by: Optional[str] = None
    as_found_z_factor: Optional[float] = None
    as_found_air_buoyancy: Optional[float] = None
    as_found_evaporation_rate: Optional[float] = None
    as_found_ambient_temperature: Optional[float] = None
    as_found_air_humidity: Optional[float] = None
    as_found_barometric_pressure: Optional[float] = None
    as_found_altitude: Optional[float] = None
    as_found_wind_speed: Optional[float] = None
    as_found_solar_radiation: Optional[float] = None
    as_found_light_intensity: Optional[float] = None
    as_found_noise_level: Optional[float] = None
    as_found_ph_level: Optional[float] = None
    as_found_water_conductivity: Optional[float] = None
    as_found_water_temperature: Optional[float] = None
    as_found_z_factor_uom: Optional[str] = None
    as_found_air_buoyancy_uom: Optional[str] = None
    as_found_evaporation_rate_uom: Optional[str] = None
    as_found_ambient_temperature_uom: Optional[str] = None
    as_found_air_humidity_uom: Optional[str] = None
    as_found_barometric_pressure_uom: Optional[str] = None
    as_found_altitude_uom: Optional[str] = None
    as_found_wind_speed_uom: Optional[str] = None
    as_found_solar_radiation_uom: Optional[str] = None
    as_found_light_intensity_uom: Optional[str] = None
    as_found_noise_level_uom: Optional[str] = None
    as_found_ph_level_uom: Optional[str] = None
    as_found_water_conductivity_uom: Optional[str] = None
    as_found_water_temperature_uom: Optional[str] = None
    as_found_abbreviated_uom: Optional[str] = None
    as_found_unit_scale_factor: Optional[float] = None
    as_found_specification_name: Optional[str] = None
    as_found_parameter_name: Optional[str] = None
    as_found_display_order: Optional[int] = None
    as_found_unit_of_measure: Optional[str] = None
    as_found_display_format: Optional[str] = None
    as_found_precision: Optional[float] = None
    as_found_precision_type: Optional[
        ReportDatasetsToMeasurementAllResponseAsFoundPrecisionType
    ] = None
    as_found_minimum: Optional[float] = None
    as_found_nominal: Optional[float] = None
    as_found_expected_value: Optional[float] = None
    as_found_expected_value_raw: Optional[str] = None
    as_found_test_value: Optional[float] = None
    as_found_base_value: Optional[float] = None
    as_found_maxi_mum: Optional[float] = None
    as_found_resolution: Optional[float] = None
    as_found_resolution_count: Optional[int] = None
    as_found_measurement_batch_id: Optional[int] = None
    as_found_measurement_id: Optional[int] = None
    as_found_standard_id: Optional[int] = None
    as_found_tool_id: Optional[int] = None
    as_found_measurement_condition_id: Optional[int] = None
    as_found_measurement_point_id: Optional[int] = None
    as_left_parameter_id: Optional[int] = None
    as_left_sd_header: Optional[float] = None
    as_left_cv_header: Optional[float] = None
    as_left_measurement_local_time: Optional[datetime.datetime] = None
    as_left_reading_entry_math: Optional[
        ReportDatasetsToMeasurementAllResponseAsLeftReadingEntryMath
    ] = None
    as_left_reading_entry_math_string: Optional[str] = None
    as_left_value_1: Optional[str] = None
    as_left_value_2: Optional[str] = None
    as_left_value_3: Optional[str] = None
    as_left_value_4: Optional[str] = None
    as_left_value_5: Optional[str] = None
    as_left_value_6: Optional[str] = None
    as_left_value_7: Optional[str] = None
    as_left_value_8: Optional[str] = None
    as_left_value_9: Optional[str] = None
    as_left_value_10: Optional[str] = None
    as_left_value_11: Optional[str] = None
    as_left_value_12: Optional[str] = None
    as_left_value_13: Optional[str] = None
    as_left_value_14: Optional[str] = None
    as_left_value_15: Optional[str] = None
    as_left_value_16: Optional[str] = None
    as_left_value_17: Optional[str] = None
    as_left_value_18: Optional[str] = None
    as_left_value_19: Optional[str] = None
    as_left_value_20: Optional[str] = None
    as_left_value_21: Optional[str] = None
    as_left_value_22: Optional[str] = None
    as_left_value_23: Optional[str] = None
    as_left_value_24: Optional[str] = None
    as_left_value_25: Optional[str] = None
    as_left_value_26: Optional[str] = None
    as_left_value_27: Optional[str] = None
    as_left_value_28: Optional[str] = None
    as_left_value_29: Optional[str] = None
    as_left_value_30: Optional[str] = None
    as_left_value_31: Optional[str] = None
    as_left_value_32: Optional[str] = None
    as_left_value_33: Optional[str] = None
    as_left_value_34: Optional[str] = None
    as_left_value_35: Optional[str] = None
    as_left_value_36: Optional[str] = None
    as_left_value_37: Optional[str] = None
    as_left_value_38: Optional[str] = None
    as_left_value_39: Optional[str] = None
    as_left_value_40: Optional[str] = None
    as_left_raw_value_1: Optional[str] = None
    as_left_raw_value_2: Optional[str] = None
    as_left_raw_value_3: Optional[str] = None
    as_left_raw_value_4: Optional[str] = None
    as_left_raw_value_5: Optional[str] = None
    as_left_raw_value_6: Optional[str] = None
    as_left_raw_value_7: Optional[str] = None
    as_left_raw_value_8: Optional[str] = None
    as_left_raw_value_9: Optional[str] = None
    as_left_raw_value_10: Optional[str] = None
    as_left_raw_value_11: Optional[str] = None
    as_left_raw_value_12: Optional[str] = None
    as_left_raw_value_13: Optional[str] = None
    as_left_raw_value_14: Optional[str] = None
    as_left_raw_value_15: Optional[str] = None
    as_left_raw_value_16: Optional[str] = None
    as_left_raw_value_17: Optional[str] = None
    as_left_raw_value_18: Optional[str] = None
    as_left_raw_value_19: Optional[str] = None
    as_left_raw_value_20: Optional[str] = None
    as_left_raw_value_21: Optional[str] = None
    as_left_raw_value_22: Optional[str] = None
    as_left_raw_value_23: Optional[str] = None
    as_left_raw_value_24: Optional[str] = None
    as_left_raw_value_25: Optional[str] = None
    as_left_raw_value_26: Optional[str] = None
    as_left_raw_value_27: Optional[str] = None
    as_left_raw_value_28: Optional[str] = None
    as_left_raw_value_29: Optional[str] = None
    as_left_raw_value_30: Optional[str] = None
    as_left_raw_value_31: Optional[str] = None
    as_left_raw_value_32: Optional[str] = None
    as_left_raw_value_33: Optional[str] = None
    as_left_raw_value_34: Optional[str] = None
    as_left_raw_value_35: Optional[str] = None
    as_left_raw_value_36: Optional[str] = None
    as_left_raw_value_37: Optional[str] = None
    as_left_raw_value_38: Optional[str] = None
    as_left_raw_value_39: Optional[str] = None
    as_left_raw_value_40: Optional[str] = None
    as_left_value_subtitle_1: Optional[str] = None
    as_left_value_subtitle_2: Optional[str] = None
    as_left_value_subtitle_3: Optional[str] = None
    as_left_value_subtitle_4: Optional[str] = None
    as_left_value_subtitle_5: Optional[str] = None
    as_left_value_subtitle_6: Optional[str] = None
    as_left_value_subtitle_7: Optional[str] = None
    as_left_value_subtitle_8: Optional[str] = None
    as_left_value_subtitle_9: Optional[str] = None
    as_left_value_subtitle_10: Optional[str] = None
    as_left_value_subtitle_11: Optional[str] = None
    as_left_value_subtitle_12: Optional[str] = None
    as_left_value_subtitle_13: Optional[str] = None
    as_left_value_subtitle_14: Optional[str] = None
    as_left_value_subtitle_15: Optional[str] = None
    as_left_value_subtitle_16: Optional[str] = None
    as_left_value_subtitle_17: Optional[str] = None
    as_left_value_subtitle_18: Optional[str] = None
    as_left_value_subtitle_19: Optional[str] = None
    as_left_value_subtitle_20: Optional[str] = None
    as_left_value_subtitle_21: Optional[str] = None
    as_left_value_subtitle_22: Optional[str] = None
    as_left_value_subtitle_23: Optional[str] = None
    as_left_value_subtitle_24: Optional[str] = None
    as_left_value_subtitle_25: Optional[str] = None
    as_left_value_subtitle_26: Optional[str] = None
    as_left_value_subtitle_27: Optional[str] = None
    as_left_value_subtitle_28: Optional[str] = None
    as_left_value_subtitle_29: Optional[str] = None
    as_left_value_subtitle_30: Optional[str] = None
    as_left_value_subtitle_31: Optional[str] = None
    as_left_value_subtitle_32: Optional[str] = None
    as_left_value_subtitle_33: Optional[str] = None
    as_left_value_subtitle_34: Optional[str] = None
    as_left_value_subtitle_35: Optional[str] = None
    as_left_value_subtitle_36: Optional[str] = None
    as_left_value_subtitle_37: Optional[str] = None
    as_left_value_subtitle_38: Optional[str] = None
    as_left_value_subtitle_39: Optional[str] = None
    as_left_value_subtitle_40: Optional[str] = None
    as_left_mean: Optional[float] = None
    as_left_mean_raw: Optional[float] = None
    as_left_sd: Optional[float] = None
    as_left_sd_raw: Optional[float] = None
    as_left_cv: Optional[float] = None
    as_left_cv_raw: Optional[float] = None
    as_left_delta: Optional[float] = None
    as_left_range: Optional[float] = None
    as_left_result: Optional[int] = None
    as_left_range_result: Optional[bool] = None
    as_left_delta_result: Optional[bool] = None
    as_left_min_result: Optional[bool] = None
    as_left_max_result: Optional[bool] = None
    as_left_tar_result: Optional[bool] = None
    as_left_tur_result: Optional[bool] = None
    as_left_error_result: Optional[bool] = None
    as_left_sd_result: Optional[bool] = None
    as_left_cv_result: Optional[bool] = None
    as_left_custom_field_result: Optional[int] = None
    as_left_mu: Optional[float] = None
    as_left_mu_raw: Optional[float] = None
    as_left_mu_effective_dof: Optional[float] = None
    as_left_mu_coverage_factor: Optional[float] = None
    as_left_cmc: Optional[float] = None
    as_left_cmc_comments: Optional[str] = None
    as_left_calculated_uncertainty: Optional[float] = None
    as_left_lab_mu: Optional[float] = None
    as_left_uncertainty_budget: Optional[str] = None
    as_left_mu_extended: Optional[str] = None
    as_left_channel: Optional[int] = None
    as_left_measurement_type: Optional[
        ReportDatasetsToMeasurementAllResponseAsLeftMeasurementType
    ] = None
    as_left_updated_by: Optional[str] = None
    as_left_updated_on: Optional[datetime.datetime] = None
    as_left_specification_title: Optional[str] = None
    as_left_specification_subtitle: Optional[str] = None
    as_left_specification_group: Optional[str] = None
    as_left_batch_type: Optional[int] = None
    as_left_batch_result: Optional[int] = None
    as_left_is_by_channel: Optional[bool] = None
    as_left_channel_count: Optional[int] = None
    as_left_commenced_on: Optional[datetime.datetime] = None
    as_left_commenced_by: Optional[str] = None
    as_left_z_factor: Optional[float] = None
    as_left_air_buoyancy: Optional[float] = None
    as_left_evaporation_rate: Optional[float] = None
    as_left_ambient_temperature: Optional[float] = None
    as_left_air_humidity: Optional[float] = None
    as_left_barometric_pressure: Optional[float] = None
    as_left_altitude: Optional[float] = None
    as_left_wind_speed: Optional[float] = None
    as_left_solar_radiation: Optional[float] = None
    as_left_light_intensity: Optional[float] = None
    as_left_noise_level: Optional[float] = None
    as_left_ph_level: Optional[float] = None
    as_left_water_conductivity: Optional[float] = None
    as_left_water_temperature: Optional[float] = None
    as_left_z_factor_uom: Optional[str] = None
    as_left_air_buoyancy_uom: Optional[str] = None
    as_left_evaporation_rate_uom: Optional[str] = None
    as_left_ambient_temperature_uom: Optional[str] = None
    as_left_air_humidity_uom: Optional[str] = None
    as_left_barometric_pressure_uom: Optional[str] = None
    as_left_altitude_uom: Optional[str] = None
    as_left_wind_speed_uom: Optional[str] = None
    as_left_solar_radiation_uom: Optional[str] = None
    as_left_light_intensity_uom: Optional[str] = None
    as_left_noise_level_uom: Optional[str] = None
    as_left_ph_level_uom: Optional[str] = None
    as_left_water_conductivity_uom: Optional[str] = None
    as_left_water_temperature_uom: Optional[str] = None
    as_left_specification_name: Optional[str] = None
    as_left_parameter_name: Optional[str] = None
    as_left_display_order: Optional[int] = None
    as_left_unit_of_measure: Optional[str] = None
    as_left_display_format: Optional[str] = None
    as_left_precision: Optional[float] = None
    as_left_precision_type: Optional[ReportDatasetsToMeasurementAllResponseAsLeftPrecisionType] = (
        None
    )
    as_left_minimum: Optional[float] = None
    as_left_nominal: Optional[float] = None
    as_left_expected_value: Optional[float] = None
    as_left_expected_value_raw: Optional[str] = None
    as_left_test_value: Optional[float] = None
    as_left_base_value: Optional[float] = None
    as_left_maxi_mum: Optional[float] = None
    as_left_resolution: Optional[float] = None
    as_left_resolution_count: Optional[int] = None
    as_left_measurement_not_taken_result: Optional[
        ReportDatasetsToMeasurementAllResponseAsLeftMeasurementNotTakenResult
    ] = None
    as_left_hide_from_certificate: Optional[bool] = None
    as_left_measurement_not_taken_reason: Optional[str] = None
    as_left_measurement_batch_id: Optional[int] = None
    as_left_measurement_id: Optional[int] = None
    as_left_standard_id: Optional[int] = None
    as_left_tool_id: Optional[int] = None
    as_left_measurement_condition_id: Optional[int] = None
    as_left_measurement_point_id: Optional[int] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        barcode = self.barcode
        display_name = self.display_name
        display_part_number = self.display_part_number
        part_number = self.part_number
        vendor_company_id = self.vendor_company_id
        service_order_number = self.service_order_number
        completed_by_name = self.completed_by_name
        completed_on: Optional[str] = None
        if self.completed_on is not None:
            completed_on = self.completed_on.isoformat()
        is_limited = self.is_limited
        vendor_tag = self.vendor_tag
        room = self.room
        segment_name = self.segment_name
        schedule_name = self.schedule_name
        next_segment_name = self.next_segment_name
        certificate_number = self.certificate_number
        work_status: Optional[int] = None
        if self.work_status is not None:
            work_status = self.work_status.value
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
        service_date: Optional[str]
        if self.service_date is None:
            service_date = None
        elif isinstance(self.service_date, datetime.datetime):
            service_date = self.service_date.isoformat()
        else:
            service_date = self.service_date
        next_service_date: Optional[str]
        if self.next_service_date is None:
            next_service_date = None
        elif isinstance(self.next_service_date, datetime.datetime):
            next_service_date = self.next_service_date.isoformat()
        else:
            next_service_date = self.next_service_date
        service_order_item_id = self.service_order_item_id
        site_name = self.site_name
        po_number = self.po_number
        shipped_date: Optional[str]
        if self.shipped_date is None:
            shipped_date = None
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
        as_left_primary_tool_last_service_date: Optional[str]
        if not self.as_left_primary_tool_last_service_date:
            as_left_primary_tool_last_service_date = None
        elif isinstance(self.as_left_primary_tool_last_service_date, datetime.datetime):
            as_left_primary_tool_last_service_date = (
                self.as_left_primary_tool_last_service_date.isoformat()
            )
        else:
            as_left_primary_tool_last_service_date = self.as_left_primary_tool_last_service_date
        as_left_primary_tool_next_service_date: Optional[str]
        if not self.as_left_primary_tool_next_service_date:
            as_left_primary_tool_next_service_date = None
        elif isinstance(self.as_left_primary_tool_next_service_date, datetime.datetime):
            as_left_primary_tool_next_service_date = (
                self.as_left_primary_tool_next_service_date.isoformat()
            )
        else:
            as_left_primary_tool_next_service_date = self.as_left_primary_tool_next_service_date
        as_left_primary_tool_calibrated_by = self.as_left_primary_tool_calibrated_by
        as_left_primary_tool_tool_name = self.as_left_primary_tool_tool_name
        as_left_primary_tool_tool_description = self.as_left_primary_tool_tool_description
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
        as_found_primary_tool_last_service_date: Optional[str]
        if not self.as_found_primary_tool_last_service_date:
            as_found_primary_tool_last_service_date = None
        elif isinstance(self.as_found_primary_tool_last_service_date, datetime.datetime):
            as_found_primary_tool_last_service_date = (
                self.as_found_primary_tool_last_service_date.isoformat()
            )
        else:
            as_found_primary_tool_last_service_date = self.as_found_primary_tool_last_service_date
        as_found_primary_tool_next_service_date: Optional[str]
        if not self.as_found_primary_tool_next_service_date:
            as_found_primary_tool_next_service_date = None
        elif isinstance(self.as_found_primary_tool_next_service_date, datetime.datetime):
            as_found_primary_tool_next_service_date = (
                self.as_found_primary_tool_next_service_date.isoformat()
            )
        else:
            as_found_primary_tool_next_service_date = self.as_found_primary_tool_next_service_date
        as_found_primary_tool_calibrated_by = self.as_found_primary_tool_calibrated_by
        as_found_primary_tool_tool_name = self.as_found_primary_tool_tool_name
        as_found_primary_tool_tool_description = self.as_found_primary_tool_tool_description
        as_found_primary_tool_tool_type_name = self.as_found_primary_tool_tool_type_name
        as_found_primary_tool_manufacturer = self.as_found_primary_tool_manufacturer
        as_found_primary_tool_manufacturer_part_number = (
            self.as_found_primary_tool_manufacturer_part_number
        )
        as_found_primary_tool_serial_number = self.as_found_primary_tool_serial_number
        as_left_secondary_tool_last_service_date: Optional[str]
        if not self.as_left_secondary_tool_last_service_date:
            as_left_secondary_tool_last_service_date = None
        elif isinstance(self.as_left_secondary_tool_last_service_date, datetime.datetime):
            as_left_secondary_tool_last_service_date = (
                self.as_left_secondary_tool_last_service_date.isoformat()
            )
        else:
            as_left_secondary_tool_last_service_date = self.as_left_secondary_tool_last_service_date
        as_left_secondary_tool_next_service_date: Optional[str]
        if not self.as_left_secondary_tool_next_service_date:
            as_left_secondary_tool_next_service_date = None
        elif isinstance(self.as_left_secondary_tool_next_service_date, datetime.datetime):
            as_left_secondary_tool_next_service_date = (
                self.as_left_secondary_tool_next_service_date.isoformat()
            )
        else:
            as_left_secondary_tool_next_service_date = self.as_left_secondary_tool_next_service_date
        as_left_secondary_tool_calibrated_by = self.as_left_secondary_tool_calibrated_by
        as_left_secondary_tool_tool_name = self.as_left_secondary_tool_tool_name
        as_left_secondary_tool_tool_description = self.as_left_secondary_tool_tool_description
        as_left_secondary_tool_tool_type_name = self.as_left_secondary_tool_tool_type_name
        as_left_secondary_tool_manufacturer = self.as_left_secondary_tool_manufacturer
        as_left_secondary_tool_manufacturer_part_number = (
            self.as_left_secondary_tool_manufacturer_part_number
        )
        as_left_secondary_tool_serial_number = self.as_left_secondary_tool_serial_number
        as_found_secondary_tool_last_service_date: Optional[str]
        if not self.as_found_secondary_tool_last_service_date:
            as_found_secondary_tool_last_service_date = None
        elif isinstance(self.as_found_secondary_tool_last_service_date, datetime.datetime):
            as_found_secondary_tool_last_service_date = (
                self.as_found_secondary_tool_last_service_date.isoformat()
            )
        else:
            as_found_secondary_tool_last_service_date = (
                self.as_found_secondary_tool_last_service_date
            )
        as_found_secondary_tool_next_service_date: Optional[str]
        if not self.as_found_secondary_tool_next_service_date:
            as_found_secondary_tool_next_service_date = None
        elif isinstance(self.as_found_secondary_tool_next_service_date, datetime.datetime):
            as_found_secondary_tool_next_service_date = (
                self.as_found_secondary_tool_next_service_date.isoformat()
            )
        else:
            as_found_secondary_tool_next_service_date = (
                self.as_found_secondary_tool_next_service_date
            )
        as_found_secondary_tool_calibrated_by = self.as_found_secondary_tool_calibrated_by
        as_found_secondary_tool_tool_name = self.as_found_secondary_tool_tool_name
        as_found_secondary_tool_tool_description = self.as_found_secondary_tool_tool_description
        as_found_secondary_tool_tool_type_name = self.as_found_secondary_tool_tool_type_name
        as_found_secondary_tool_manufacturer = self.as_found_secondary_tool_manufacturer
        as_found_secondary_tool_manufacturer_part_number = (
            self.as_found_secondary_tool_manufacturer_part_number
        )
        as_found_secondary_tool_serial_number = self.as_found_secondary_tool_serial_number
        as_found_measurement_not_taken_result: Optional[str] = None
        if self.as_found_measurement_not_taken_result is not None:
            as_found_measurement_not_taken_result = self.as_found_measurement_not_taken_result.value
        as_found_hide_from_certificate = self.as_found_hide_from_certificate
        as_found_measurement_not_taken_reason = self.as_found_measurement_not_taken_reason
        as_left_values = self.as_left_values
        as_left_is_accredited = self.as_left_is_accredited
        as_left_is_range_accredited = self.as_left_is_range_accredited
        as_found_values = self.as_found_values
        as_found_is_accredited = self.as_found_is_accredited
        as_found_is_range_accredited = self.as_found_is_range_accredited
        as_found_parameter_id = self.as_found_parameter_id
        as_found_sd_header = self.as_found_sd_header
        as_found_cv_header = self.as_found_cv_header
        as_found_measurement_local_time: Optional[str] = None
        if self.as_found_measurement_local_time is not None:
            as_found_measurement_local_time = self.as_found_measurement_local_time.isoformat()
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
        as_found_guard_band_logic: Optional[str] = None
        if self.as_found_guard_band_logic is not None:
            as_found_guard_band_logic = self.as_found_guard_band_logic.value
        as_left_guard_band_logic: Optional[str] = None
        if self.as_left_guard_band_logic is not None:
            as_left_guard_band_logic = self.as_left_guard_band_logic.value
        as_found_error = self.as_found_error
        as_found_error_extended = self.as_found_error_extended
        as_left_error = self.as_left_error
        as_left_error_extended = self.as_left_error_extended
        as_found_percent_of_tolerance = self.as_found_percent_of_tolerance
        as_found_percent_of_tolerance_extended = self.as_found_percent_of_tolerance_extended
        as_left_percent_of_tolerance = self.as_left_percent_of_tolerance
        as_left_percent_of_tolerance_extended = self.as_left_percent_of_tolerance_extended
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
        as_found_reading_entry_math: Optional[str] = None
        if self.as_found_reading_entry_math is not None:
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
        as_found_result: Optional[str]
        if not self.as_found_result:
            as_found_result = None
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
        as_found_measurement_type: Optional[str] = None
        if self.as_found_measurement_type is not None:
            as_found_measurement_type = self.as_found_measurement_type.value
        as_found_updated_by = self.as_found_updated_by
        as_found_updated_on: Optional[str] = None
        if self.as_found_updated_on:
            as_found_updated_on = self.as_found_updated_on.isoformat()
        as_left_abbreviated_uom = self.as_left_abbreviated_uom
        as_left_unit_scale_factor = self.as_left_unit_scale_factor
        as_found_specification_title = self.as_found_specification_title
        as_found_specification_subtitle = self.as_found_specification_subtitle
        as_found_specification_group = self.as_found_specification_group
        as_found_batch_type = self.as_found_batch_type
        as_found_batch_result = self.as_found_batch_result
        as_found_is_by_channel = self.as_found_is_by_channel
        as_found_channel_count = self.as_found_channel_count
        as_found_commenced_on: Optional[str] = None
        if self.as_found_commenced_on is not None:
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
        as_found_precision_type: Optional[str] = None
        if self.as_found_precision_type is not None:
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
        as_left_measurement_local_time: Optional[str] = None
        if self.as_left_measurement_local_time is not None:
            as_left_measurement_local_time = self.as_left_measurement_local_time.isoformat()
        as_left_reading_entry_math: Optional[str] = None
        if self.as_left_reading_entry_math is not None:
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
        # serialize as_left_result without shadowing type annotations
        if self.as_left_result is None:
            as_left_result = None
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
        as_left_measurement_type: Optional[str] = None
        if self.as_left_measurement_type is not None:
            as_left_measurement_type = self.as_left_measurement_type.value
        as_left_updated_by = self.as_left_updated_by
        as_left_updated_on: Optional[str] = None
        if self.as_left_updated_on:
            as_left_updated_on = self.as_left_updated_on.isoformat()
        as_left_specification_title = self.as_left_specification_title
        as_left_specification_subtitle = self.as_left_specification_subtitle
        as_left_specification_group = self.as_left_specification_group
        as_left_batch_type = self.as_left_batch_type
        as_left_batch_result = self.as_left_batch_result
        as_left_is_by_channel = self.as_left_is_by_channel
        as_left_channel_count = self.as_left_channel_count
        as_left_commenced_on: Optional[str] = None
        if self.as_left_commenced_on is not None:
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
        as_left_precision_type: Optional[str] = None
        if self.as_left_precision_type is not None:
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
        as_left_measurement_not_taken_result: Optional[str] = None
        if self.as_left_measurement_not_taken_result is not None:
            as_left_measurement_not_taken_result = self.as_left_measurement_not_taken_result.value
        as_left_hide_from_certificate = self.as_left_hide_from_certificate
        as_left_measurement_not_taken_reason = self.as_left_measurement_not_taken_reason
        as_left_measurement_batch_id = self.as_left_measurement_batch_id
        as_left_measurement_id = self.as_left_measurement_id
        as_left_standard_id = self.as_left_standard_id
        as_left_tool_id = self.as_left_tool_id
        as_left_measurement_condition_id = self.as_left_measurement_condition_id
        as_left_measurement_point_id = self.as_left_measurement_point_id
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if barcode is not None:
            field_dict["Barcode"] = barcode
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
        if completed_by_name is not None:
            field_dict["CompletedByName"] = completed_by_name
        if completed_on is not None:
            field_dict["CompletedOn"] = completed_on
        if is_limited is not None:
            field_dict["IsLimited"] = is_limited
        if vendor_tag is not None:
            field_dict["VendorTag"] = vendor_tag
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
        if service_comments is not None:
            field_dict["ServiceComments"] = service_comments
        if order_item_number is not None:
            field_dict["OrderItemNumber"] = order_item_number
        if service_total is not None:
            field_dict["ServiceTotal"] = service_total
        if repairs_total is not None:
            field_dict["RepairsTotal"] = repairs_total
        if parts_total is not None:
            field_dict["PartsTotal"] = parts_total
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
        if site_name is not None:
            field_dict["SiteName"] = site_name
        if po_number is not None:
            field_dict["PoNumber"] = po_number
        if shipped_date is not None:
            field_dict["ShippedDate"] = shipped_date
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
        if as_left_decimal_places is not None:
            field_dict["AsLeftDecimalPlaces"] = as_left_decimal_places
        if as_left_measurement_set_name is not None:
            field_dict["AsLeftMeasurementSetName"] = as_left_measurement_set_name
        if as_left_measurement_set_id is not None:
            field_dict["AsLeftMeasurementSetId"] = as_left_measurement_set_id
        if as_left_adjustment_threshold is not None:
            field_dict["AsLeftAdjustmentThreshold"] = as_left_adjustment_threshold
        if as_left_mean_extended is not None:
            field_dict["AsLeftMeanExtended"] = as_left_mean_extended
        if as_left_sd_extended is not None:
            field_dict["AsLeftSdExtended"] = as_left_sd_extended
        if as_left_range_extended is not None:
            field_dict["AsLeftRangeExtended"] = as_left_range_extended
        if as_left_delta_extended is not None:
            field_dict["AsLeftDeltaExtended"] = as_left_delta_extended
        if as_left_cv_extended is not None:
            field_dict["AsLeftCvExtended"] = as_left_cv_extended
        if as_left_nominal_extended is not None:
            field_dict["AsLeftNominalExtended"] = as_left_nominal_extended
        if as_left_min_max_header is not None:
            field_dict["AsLeftMinMaxHeader"] = as_left_min_max_header
        if as_left_accuracy_class is not None:
            field_dict["AsLeftAccuracyClass"] = as_left_accuracy_class
        if as_left_accuracy_class_min is not None:
            field_dict["AsLeftAccuracyClassMin"] = as_left_accuracy_class_min
        if as_left_accuracy_class_max is not None:
            field_dict["AsLeftAccuracyClassMax"] = as_left_accuracy_class_max
        if as_left_minimum_measured_value is not None:
            field_dict["AsLeftMinimumMeasuredValue"] = as_left_minimum_measured_value
        if as_left_maxi_mum_measured_value is not None:
            field_dict["AsLeftMaxiMumMeasuredValue"] = as_left_maxi_mum_measured_value
        if as_left_min_max_value_extended is not None:
            field_dict["AsLeftMinMaxValueExtended"] = as_left_min_max_value_extended
        if as_left_tool_range_name is not None:
            field_dict["AsLeftToolRangeName"] = as_left_tool_range_name
        if as_left_tool_range_uncertainty is not None:
            field_dict["AsLeftToolRangeUncertainty"] = as_left_tool_range_uncertainty
        if as_left_primary_tool_last_service_date is not None:
            field_dict["AsLeftPrimaryToolLastServiceDate"] = as_left_primary_tool_last_service_date
        if as_left_primary_tool_next_service_date is not None:
            field_dict["AsLeftPrimaryToolNextServiceDate"] = as_left_primary_tool_next_service_date
        if as_left_primary_tool_calibrated_by is not None:
            field_dict["AsLeftPrimaryToolCalibratedBy"] = as_left_primary_tool_calibrated_by
        if as_left_primary_tool_tool_name is not None:
            field_dict["AsLeftPrimaryToolToolName"] = as_left_primary_tool_tool_name
        if as_left_primary_tool_tool_description is not None:
            field_dict["AsLeftPrimaryToolToolDescription"] = as_left_primary_tool_tool_description
        if as_left_primary_tool_tool_type_name is not None:
            field_dict["AsLeftPrimaryToolToolTypeName"] = as_left_primary_tool_tool_type_name
        if as_left_primary_tool_manufacturer is not None:
            field_dict["AsLeftPrimaryToolManufacturer"] = as_left_primary_tool_manufacturer
        if as_left_primary_tool_manufacturer_part_number is not None:
            field_dict["AsLeftPrimaryToolManufacturerPartNumber"] = (
                as_left_primary_tool_manufacturer_part_number
            )
        if as_left_primary_tool_serial_number is not None:
            field_dict["AsLeftPrimaryToolSerialNumber"] = as_left_primary_tool_serial_number
        if as_found_measurement_set_name is not None:
            field_dict["AsFoundMeasurementSetName"] = as_found_measurement_set_name
        if as_found_measurement_set_id is not None:
            field_dict["AsFoundMeasurementSetId"] = as_found_measurement_set_id
        if as_found_adjustment_threshold is not None:
            field_dict["AsFoundAdjustmentThreshold"] = as_found_adjustment_threshold
        if as_found_decimal_places is not None:
            field_dict["AsFoundDecimalPlaces"] = as_found_decimal_places
        if as_found_mean_extended is not None:
            field_dict["AsFoundMeanExtended"] = as_found_mean_extended
        if as_found_sd_extended is not None:
            field_dict["AsFoundSdExtended"] = as_found_sd_extended
        if as_found_range_extended is not None:
            field_dict["AsFoundRangeExtended"] = as_found_range_extended
        if as_found_delta_extended is not None:
            field_dict["AsFoundDeltaExtended"] = as_found_delta_extended
        if as_found_cv_extended is not None:
            field_dict["AsFoundCvExtended"] = as_found_cv_extended
        if as_found_nominal_extended is not None:
            field_dict["AsFoundNominalExtended"] = as_found_nominal_extended
        if as_found_min_max_header is not None:
            field_dict["AsFoundMinMaxHeader"] = as_found_min_max_header
        if as_found_accuracy_class is not None:
            field_dict["AsFoundAccuracyClass"] = as_found_accuracy_class
        if as_found_accuracy_class_min is not None:
            field_dict["AsFoundAccuracyClassMin"] = as_found_accuracy_class_min
        if as_found_accuracy_class_max is not None:
            field_dict["AsFoundAccuracyClassMax"] = as_found_accuracy_class_max
        if as_found_minimum_measured_value is not None:
            field_dict["AsFoundMinimumMeasuredValue"] = as_found_minimum_measured_value
        if as_found_maxi_mum_measured_value is not None:
            field_dict["AsFoundMaxiMumMeasuredValue"] = as_found_maxi_mum_measured_value
        if as_found_min_max_value_extended is not None:
            field_dict["AsFoundMinMaxValueExtended"] = as_found_min_max_value_extended
        if as_found_tool_range_name is not None:
            field_dict["AsFoundToolRangeName"] = as_found_tool_range_name
        if as_found_tool_range_uncertainty is not None:
            field_dict["AsFoundToolRangeUncertainty"] = as_found_tool_range_uncertainty
        if as_found_primary_tool_last_service_date is not None:
            field_dict["AsFoundPrimaryToolLastServiceDate"] = (
                as_found_primary_tool_last_service_date
            )
        if as_found_primary_tool_next_service_date is not None:
            field_dict["AsFoundPrimaryToolNextServiceDate"] = (
                as_found_primary_tool_next_service_date
            )
        if as_found_primary_tool_calibrated_by is not None:
            field_dict["AsFoundPrimaryToolCalibratedBy"] = as_found_primary_tool_calibrated_by
        if as_found_primary_tool_tool_name is not None:
            field_dict["AsFoundPrimaryToolToolName"] = as_found_primary_tool_tool_name
        if as_found_primary_tool_tool_description is not None:
            field_dict["AsFoundPrimaryToolToolDescription"] = as_found_primary_tool_tool_description
        if as_found_primary_tool_tool_type_name is not None:
            field_dict["AsFoundPrimaryToolToolTypeName"] = as_found_primary_tool_tool_type_name
        if as_found_primary_tool_manufacturer is not None:
            field_dict["AsFoundPrimaryToolManufacturer"] = as_found_primary_tool_manufacturer
        if as_found_primary_tool_manufacturer_part_number is not None:
            field_dict["AsFoundPrimaryToolManufacturerPartNumber"] = (
                as_found_primary_tool_manufacturer_part_number
            )
        if as_found_primary_tool_serial_number is not None:
            field_dict["AsFoundPrimaryToolSerialNumber"] = as_found_primary_tool_serial_number
        if as_left_secondary_tool_last_service_date is not None:
            field_dict["AsLeftSecondaryToolLastServiceDate"] = (
                as_left_secondary_tool_last_service_date
            )
        if as_left_secondary_tool_next_service_date is not None:
            field_dict["AsLeftSecondaryToolNextServiceDate"] = (
                as_left_secondary_tool_next_service_date
            )
        if as_left_secondary_tool_calibrated_by is not None:
            field_dict["AsLeftSecondaryToolCalibratedBy"] = as_left_secondary_tool_calibrated_by
        if as_left_secondary_tool_tool_name is not None:
            field_dict["AsLeftSecondaryToolToolName"] = as_left_secondary_tool_tool_name
        if as_left_secondary_tool_tool_description is not None:
            field_dict["AsLeftSecondaryToolToolDescription"] = (
                as_left_secondary_tool_tool_description
            )
        if as_left_secondary_tool_tool_type_name is not None:
            field_dict["AsLeftSecondaryToolToolTypeName"] = as_left_secondary_tool_tool_type_name
        if as_left_secondary_tool_manufacturer is not None:
            field_dict["AsLeftSecondaryToolManufacturer"] = as_left_secondary_tool_manufacturer
        if as_left_secondary_tool_manufacturer_part_number is not None:
            field_dict["AsLeftSecondaryToolManufacturerPartNumber"] = (
                as_left_secondary_tool_manufacturer_part_number
            )
        if as_left_secondary_tool_serial_number is not None:
            field_dict["AsLeftSecondaryToolSerialNumber"] = as_left_secondary_tool_serial_number
        if as_found_secondary_tool_last_service_date is not None:
            field_dict["AsFoundSecondaryToolLastServiceDate"] = (
                as_found_secondary_tool_last_service_date
            )
        if as_found_secondary_tool_next_service_date is not None:
            field_dict["AsFoundSecondaryToolNextServiceDate"] = (
                as_found_secondary_tool_next_service_date
            )
        if as_found_secondary_tool_calibrated_by is not None:
            field_dict["AsFoundSecondaryToolCalibratedBy"] = as_found_secondary_tool_calibrated_by
        if as_found_secondary_tool_tool_name is not None:
            field_dict["AsFoundSecondaryToolToolName"] = as_found_secondary_tool_tool_name
        if as_found_secondary_tool_tool_description is not None:
            field_dict["AsFoundSecondaryToolToolDescription"] = (
                as_found_secondary_tool_tool_description
            )
        if as_found_secondary_tool_tool_type_name is not None:
            field_dict["AsFoundSecondaryToolToolTypeName"] = as_found_secondary_tool_tool_type_name
        if as_found_secondary_tool_manufacturer is not None:
            field_dict["AsFoundSecondaryToolManufacturer"] = as_found_secondary_tool_manufacturer
        if as_found_secondary_tool_manufacturer_part_number is not None:
            field_dict["AsFoundSecondaryToolManufacturerPartNumber"] = (
                as_found_secondary_tool_manufacturer_part_number
            )
        if as_found_secondary_tool_serial_number is not None:
            field_dict["AsFoundSecondaryToolSerialNumber"] = as_found_secondary_tool_serial_number
        if as_found_measurement_not_taken_result is not None:
            field_dict["AsFoundMeasurementNotTakenResult"] = as_found_measurement_not_taken_result
        if as_found_hide_from_certificate is not None:
            field_dict["AsFoundHideFromCertificate"] = as_found_hide_from_certificate
        if as_found_measurement_not_taken_reason is not None:
            field_dict["AsFoundMeasurementNotTakenReason"] = as_found_measurement_not_taken_reason
        if as_left_values is not None:
            field_dict["AsLeftValues"] = as_left_values
        if as_left_is_accredited is not None:
            field_dict["AsLeftIsAccredited"] = as_left_is_accredited
        if as_left_is_range_accredited is not None:
            field_dict["AsLeftIsRangeAccredited"] = as_left_is_range_accredited
        if as_found_values is not None:
            field_dict["AsFoundValues"] = as_found_values
        if as_found_is_accredited is not None:
            field_dict["AsFoundIsAccredited"] = as_found_is_accredited
        if as_found_is_range_accredited is not None:
            field_dict["AsFoundIsRangeAccredited"] = as_found_is_range_accredited
        if as_found_parameter_id is not None:
            field_dict["AsFoundParameterId"] = as_found_parameter_id
        if as_found_sd_header is not None:
            field_dict["AsFoundSdHeader"] = as_found_sd_header
        if as_found_cv_header is not None:
            field_dict["AsFoundCvHeader"] = as_found_cv_header
        if as_found_measurement_local_time is not None:
            field_dict["AsFoundMeasurementLocalTime"] = as_found_measurement_local_time
        if as_found_tur is not None:
            field_dict["AsFoundTur"] = as_found_tur
        if as_found_tur_raw is not None:
            field_dict["AsFoundTurRaw"] = as_found_tur_raw
        if as_left_tur is not None:
            field_dict["AsLeftTur"] = as_left_tur
        if as_left_tur_raw is not None:
            field_dict["AsLeftTurRaw"] = as_left_tur_raw
        if as_found_tar is not None:
            field_dict["AsFoundTar"] = as_found_tar
        if as_found_tar_raw is not None:
            field_dict["AsFoundTarRaw"] = as_found_tar_raw
        if as_left_tar is not None:
            field_dict["AsLeftTar"] = as_left_tar
        if as_left_tar_raw is not None:
            field_dict["AsLeftTarRaw"] = as_left_tar_raw
        if as_found_guard_band is not None:
            field_dict["AsFoundGuardBand"] = as_found_guard_band
        if as_left_guard_band is not None:
            field_dict["AsLeftGuardBand"] = as_left_guard_band
        if as_found_guard_band_logic is not None:
            field_dict["AsFoundGuardBandLogic"] = as_found_guard_band_logic
        if as_left_guard_band_logic is not None:
            field_dict["AsLeftGuardBandLogic"] = as_left_guard_band_logic
        if as_found_error is not None:
            field_dict["AsFoundError"] = as_found_error
        if as_found_error_extended is not None:
            field_dict["AsFoundErrorExtended"] = as_found_error_extended
        if as_left_error is not None:
            field_dict["AsLeftError"] = as_left_error
        if as_left_error_extended is not None:
            field_dict["AsLeftErrorExtended"] = as_left_error_extended
        if as_found_percent_of_tolerance is not None:
            field_dict["AsFoundPercentOfTolerance"] = as_found_percent_of_tolerance
        if as_found_percent_of_tolerance_extended is not None:
            field_dict["AsFoundPercentOfToleranceExtended"] = as_found_percent_of_tolerance_extended
        if as_left_percent_of_tolerance is not None:
            field_dict["AsLeftPercentOfTolerance"] = as_left_percent_of_tolerance
        if as_left_percent_of_tolerance_extended is not None:
            field_dict["AsLeftPercentOfToleranceExtended"] = as_left_percent_of_tolerance_extended
        if as_found_tolerance_maximum is not None:
            field_dict["AsFoundToleranceMaximum"] = as_found_tolerance_maximum
        if as_found_tolerance_minimum is not None:
            field_dict["AsFoundToleranceMinimum"] = as_found_tolerance_minimum
        if as_found_tolerance_type is not None:
            field_dict["AsFoundToleranceType"] = as_found_tolerance_type
        if as_found_tolerance_mode is not None:
            field_dict["AsFoundToleranceMode"] = as_found_tolerance_mode
        if as_found_tolerance_string is not None:
            field_dict["AsFoundToleranceString"] = as_found_tolerance_string
        if as_left_tolerance_maximum is not None:
            field_dict["AsLeftToleranceMaximum"] = as_left_tolerance_maximum
        if as_left_tolerance_minimum is not None:
            field_dict["AsLeftToleranceMinimum"] = as_left_tolerance_minimum
        if as_left_tolerance_type is not None:
            field_dict["AsLeftToleranceType"] = as_left_tolerance_type
        if as_left_tolerance_mode is not None:
            field_dict["AsLeftToleranceMode"] = as_left_tolerance_mode
        if as_left_tolerance_string is not None:
            field_dict["AsLeftToleranceString"] = as_left_tolerance_string
        if as_found_max_hysteresis is not None:
            field_dict["AsFoundMaxHysteresis"] = as_found_max_hysteresis
        if as_found_run is not None:
            field_dict["AsFoundRun"] = as_found_run
        if as_found_direction is not None:
            field_dict["AsFoundDirection"] = as_found_direction
        if as_found_hysteresis is not None:
            field_dict["AsFoundHysteresis"] = as_found_hysteresis
        if as_left_max_hysteresis is not None:
            field_dict["AsLeftMaxHysteresis"] = as_left_max_hysteresis
        if as_left_run is not None:
            field_dict["AsLeftRun"] = as_left_run
        if as_left_direction is not None:
            field_dict["AsLeftDirection"] = as_left_direction
        if as_left_hysteresis is not None:
            field_dict["AsLeftHysteresis"] = as_left_hysteresis
        if as_found_reading_entry_math is not None:
            field_dict["AsFoundReadingEntryMath"] = as_found_reading_entry_math
        if as_found_reading_entry_math_string is not None:
            field_dict["AsFoundReadingEntryMathString"] = as_found_reading_entry_math_string
        if as_found_value_1 is not None:
            field_dict["AsFoundValue1"] = as_found_value_1
        if as_found_value_2 is not None:
            field_dict["AsFoundValue2"] = as_found_value_2
        if as_found_value_3 is not None:
            field_dict["AsFoundValue3"] = as_found_value_3
        if as_found_value_4 is not None:
            field_dict["AsFoundValue4"] = as_found_value_4
        if as_found_value_5 is not None:
            field_dict["AsFoundValue5"] = as_found_value_5
        if as_found_value_6 is not None:
            field_dict["AsFoundValue6"] = as_found_value_6
        if as_found_value_7 is not None:
            field_dict["AsFoundValue7"] = as_found_value_7
        if as_found_value_8 is not None:
            field_dict["AsFoundValue8"] = as_found_value_8
        if as_found_value_9 is not None:
            field_dict["AsFoundValue9"] = as_found_value_9
        if as_found_value_10 is not None:
            field_dict["AsFoundValue10"] = as_found_value_10
        if as_found_value_11 is not None:
            field_dict["AsFoundValue11"] = as_found_value_11
        if as_found_value_12 is not None:
            field_dict["AsFoundValue12"] = as_found_value_12
        if as_found_value_13 is not None:
            field_dict["AsFoundValue13"] = as_found_value_13
        if as_found_value_14 is not None:
            field_dict["AsFoundValue14"] = as_found_value_14
        if as_found_value_15 is not None:
            field_dict["AsFoundValue15"] = as_found_value_15
        if as_found_value_16 is not None:
            field_dict["AsFoundValue16"] = as_found_value_16
        if as_found_value_17 is not None:
            field_dict["AsFoundValue17"] = as_found_value_17
        if as_found_value_18 is not None:
            field_dict["AsFoundValue18"] = as_found_value_18
        if as_found_value_19 is not None:
            field_dict["AsFoundValue19"] = as_found_value_19
        if as_found_value_20 is not None:
            field_dict["AsFoundValue20"] = as_found_value_20
        if as_found_value_21 is not None:
            field_dict["AsFoundValue21"] = as_found_value_21
        if as_found_value_22 is not None:
            field_dict["AsFoundValue22"] = as_found_value_22
        if as_found_value_23 is not None:
            field_dict["AsFoundValue23"] = as_found_value_23
        if as_found_value_24 is not None:
            field_dict["AsFoundValue24"] = as_found_value_24
        if as_found_value_25 is not None:
            field_dict["AsFoundValue25"] = as_found_value_25
        if as_found_value_26 is not None:
            field_dict["AsFoundValue26"] = as_found_value_26
        if as_found_value_27 is not None:
            field_dict["AsFoundValue27"] = as_found_value_27
        if as_found_value_28 is not None:
            field_dict["AsFoundValue28"] = as_found_value_28
        if as_found_value_29 is not None:
            field_dict["AsFoundValue29"] = as_found_value_29
        if as_found_value_30 is not None:
            field_dict["AsFoundValue30"] = as_found_value_30
        if as_found_value_31 is not None:
            field_dict["AsFoundValue31"] = as_found_value_31
        if as_found_value_32 is not None:
            field_dict["AsFoundValue32"] = as_found_value_32
        if as_found_value_33 is not None:
            field_dict["AsFoundValue33"] = as_found_value_33
        if as_found_value_34 is not None:
            field_dict["AsFoundValue34"] = as_found_value_34
        if as_found_value_35 is not None:
            field_dict["AsFoundValue35"] = as_found_value_35
        if as_found_value_36 is not None:
            field_dict["AsFoundValue36"] = as_found_value_36
        if as_found_value_37 is not None:
            field_dict["AsFoundValue37"] = as_found_value_37
        if as_found_value_38 is not None:
            field_dict["AsFoundValue38"] = as_found_value_38
        if as_found_value_39 is not None:
            field_dict["AsFoundValue39"] = as_found_value_39
        if as_found_value_40 is not None:
            field_dict["AsFoundValue40"] = as_found_value_40
        if as_found_raw_value_1 is not None:
            field_dict["AsFoundRawValue1"] = as_found_raw_value_1
        if as_found_raw_value_2 is not None:
            field_dict["AsFoundRawValue2"] = as_found_raw_value_2
        if as_found_raw_value_3 is not None:
            field_dict["AsFoundRawValue3"] = as_found_raw_value_3
        if as_found_raw_value_4 is not None:
            field_dict["AsFoundRawValue4"] = as_found_raw_value_4
        if as_found_raw_value_5 is not None:
            field_dict["AsFoundRawValue5"] = as_found_raw_value_5
        if as_found_raw_value_6 is not None:
            field_dict["AsFoundRawValue6"] = as_found_raw_value_6
        if as_found_raw_value_7 is not None:
            field_dict["AsFoundRawValue7"] = as_found_raw_value_7
        if as_found_raw_value_8 is not None:
            field_dict["AsFoundRawValue8"] = as_found_raw_value_8
        if as_found_raw_value_9 is not None:
            field_dict["AsFoundRawValue9"] = as_found_raw_value_9
        if as_found_raw_value_10 is not None:
            field_dict["AsFoundRawValue10"] = as_found_raw_value_10
        if as_found_raw_value_11 is not None:
            field_dict["AsFoundRawValue11"] = as_found_raw_value_11
        if as_found_raw_value_12 is not None:
            field_dict["AsFoundRawValue12"] = as_found_raw_value_12
        if as_found_raw_value_13 is not None:
            field_dict["AsFoundRawValue13"] = as_found_raw_value_13
        if as_found_raw_value_14 is not None:
            field_dict["AsFoundRawValue14"] = as_found_raw_value_14
        if as_found_raw_value_15 is not None:
            field_dict["AsFoundRawValue15"] = as_found_raw_value_15
        if as_found_raw_value_16 is not None:
            field_dict["AsFoundRawValue16"] = as_found_raw_value_16
        if as_found_raw_value_17 is not None:
            field_dict["AsFoundRawValue17"] = as_found_raw_value_17
        if as_found_raw_value_18 is not None:
            field_dict["AsFoundRawValue18"] = as_found_raw_value_18
        if as_found_raw_value_19 is not None:
            field_dict["AsFoundRawValue19"] = as_found_raw_value_19
        if as_found_raw_value_20 is not None:
            field_dict["AsFoundRawValue20"] = as_found_raw_value_20
        if as_found_raw_value_21 is not None:
            field_dict["AsFoundRawValue21"] = as_found_raw_value_21
        if as_found_raw_value_22 is not None:
            field_dict["AsFoundRawValue22"] = as_found_raw_value_22
        if as_found_raw_value_23 is not None:
            field_dict["AsFoundRawValue23"] = as_found_raw_value_23
        if as_found_raw_value_24 is not None:
            field_dict["AsFoundRawValue24"] = as_found_raw_value_24
        if as_found_raw_value_25 is not None:
            field_dict["AsFoundRawValue25"] = as_found_raw_value_25
        if as_found_raw_value_26 is not None:
            field_dict["AsFoundRawValue26"] = as_found_raw_value_26
        if as_found_raw_value_27 is not None:
            field_dict["AsFoundRawValue27"] = as_found_raw_value_27
        if as_found_raw_value_28 is not None:
            field_dict["AsFoundRawValue28"] = as_found_raw_value_28
        if as_found_raw_value_29 is not None:
            field_dict["AsFoundRawValue29"] = as_found_raw_value_29
        if as_found_raw_value_30 is not None:
            field_dict["AsFoundRawValue30"] = as_found_raw_value_30
        if as_found_raw_value_31 is not None:
            field_dict["AsFoundRawValue31"] = as_found_raw_value_31
        if as_found_raw_value_32 is not None:
            field_dict["AsFoundRawValue32"] = as_found_raw_value_32
        if as_found_raw_value_33 is not None:
            field_dict["AsFoundRawValue33"] = as_found_raw_value_33
        if as_found_raw_value_34 is not None:
            field_dict["AsFoundRawValue34"] = as_found_raw_value_34
        if as_found_raw_value_35 is not None:
            field_dict["AsFoundRawValue35"] = as_found_raw_value_35
        if as_found_raw_value_36 is not None:
            field_dict["AsFoundRawValue36"] = as_found_raw_value_36
        if as_found_raw_value_37 is not None:
            field_dict["AsFoundRawValue37"] = as_found_raw_value_37
        if as_found_raw_value_38 is not None:
            field_dict["AsFoundRawValue38"] = as_found_raw_value_38
        if as_found_raw_value_39 is not None:
            field_dict["AsFoundRawValue39"] = as_found_raw_value_39
        if as_found_raw_value_40 is not None:
            field_dict["AsFoundRawValue40"] = as_found_raw_value_40
        if as_found_value_subtitle_1 is not None:
            field_dict["AsFoundValueSubtitle1"] = as_found_value_subtitle_1
        if as_found_value_subtitle_2 is not None:
            field_dict["AsFoundValueSubtitle2"] = as_found_value_subtitle_2
        if as_found_value_subtitle_3 is not None:
            field_dict["AsFoundValueSubtitle3"] = as_found_value_subtitle_3
        if as_found_value_subtitle_4 is not None:
            field_dict["AsFoundValueSubtitle4"] = as_found_value_subtitle_4
        if as_found_value_subtitle_5 is not None:
            field_dict["AsFoundValueSubtitle5"] = as_found_value_subtitle_5
        if as_found_value_subtitle_6 is not None:
            field_dict["AsFoundValueSubtitle6"] = as_found_value_subtitle_6
        if as_found_value_subtitle_7 is not None:
            field_dict["AsFoundValueSubtitle7"] = as_found_value_subtitle_7
        if as_found_value_subtitle_8 is not None:
            field_dict["AsFoundValueSubtitle8"] = as_found_value_subtitle_8
        if as_found_value_subtitle_9 is not None:
            field_dict["AsFoundValueSubtitle9"] = as_found_value_subtitle_9
        if as_found_value_subtitle_10 is not None:
            field_dict["AsFoundValueSubtitle10"] = as_found_value_subtitle_10
        if as_found_value_subtitle_11 is not None:
            field_dict["AsFoundValueSubtitle11"] = as_found_value_subtitle_11
        if as_found_value_subtitle_12 is not None:
            field_dict["AsFoundValueSubtitle12"] = as_found_value_subtitle_12
        if as_found_value_subtitle_13 is not None:
            field_dict["AsFoundValueSubtitle13"] = as_found_value_subtitle_13
        if as_found_value_subtitle_14 is not None:
            field_dict["AsFoundValueSubtitle14"] = as_found_value_subtitle_14
        if as_found_value_subtitle_15 is not None:
            field_dict["AsFoundValueSubtitle15"] = as_found_value_subtitle_15
        if as_found_value_subtitle_16 is not None:
            field_dict["AsFoundValueSubtitle16"] = as_found_value_subtitle_16
        if as_found_value_subtitle_17 is not None:
            field_dict["AsFoundValueSubtitle17"] = as_found_value_subtitle_17
        if as_found_value_subtitle_18 is not None:
            field_dict["AsFoundValueSubtitle18"] = as_found_value_subtitle_18
        if as_found_value_subtitle_19 is not None:
            field_dict["AsFoundValueSubtitle19"] = as_found_value_subtitle_19
        if as_found_value_subtitle_20 is not None:
            field_dict["AsFoundValueSubtitle20"] = as_found_value_subtitle_20
        if as_found_value_subtitle_21 is not None:
            field_dict["AsFoundValueSubtitle21"] = as_found_value_subtitle_21
        if as_found_value_subtitle_22 is not None:
            field_dict["AsFoundValueSubtitle22"] = as_found_value_subtitle_22
        if as_found_value_subtitle_23 is not None:
            field_dict["AsFoundValueSubtitle23"] = as_found_value_subtitle_23
        if as_found_value_subtitle_24 is not None:
            field_dict["AsFoundValueSubtitle24"] = as_found_value_subtitle_24
        if as_found_value_subtitle_25 is not None:
            field_dict["AsFoundValueSubtitle25"] = as_found_value_subtitle_25
        if as_found_value_subtitle_26 is not None:
            field_dict["AsFoundValueSubtitle26"] = as_found_value_subtitle_26
        if as_found_value_subtitle_27 is not None:
            field_dict["AsFoundValueSubtitle27"] = as_found_value_subtitle_27
        if as_found_value_subtitle_28 is not None:
            field_dict["AsFoundValueSubtitle28"] = as_found_value_subtitle_28
        if as_found_value_subtitle_29 is not None:
            field_dict["AsFoundValueSubtitle29"] = as_found_value_subtitle_29
        if as_found_value_subtitle_30 is not None:
            field_dict["AsFoundValueSubtitle30"] = as_found_value_subtitle_30
        if as_found_value_subtitle_31 is not None:
            field_dict["AsFoundValueSubtitle31"] = as_found_value_subtitle_31
        if as_found_value_subtitle_32 is not None:
            field_dict["AsFoundValueSubtitle32"] = as_found_value_subtitle_32
        if as_found_value_subtitle_33 is not None:
            field_dict["AsFoundValueSubtitle33"] = as_found_value_subtitle_33
        if as_found_value_subtitle_34 is not None:
            field_dict["AsFoundValueSubtitle34"] = as_found_value_subtitle_34
        if as_found_value_subtitle_35 is not None:
            field_dict["AsFoundValueSubtitle35"] = as_found_value_subtitle_35
        if as_found_value_subtitle_36 is not None:
            field_dict["AsFoundValueSubtitle36"] = as_found_value_subtitle_36
        if as_found_value_subtitle_37 is not None:
            field_dict["AsFoundValueSubtitle37"] = as_found_value_subtitle_37
        if as_found_value_subtitle_38 is not None:
            field_dict["AsFoundValueSubtitle38"] = as_found_value_subtitle_38
        if as_found_value_subtitle_39 is not None:
            field_dict["AsFoundValueSubtitle39"] = as_found_value_subtitle_39
        if as_found_value_subtitle_40 is not None:
            field_dict["AsFoundValueSubtitle40"] = as_found_value_subtitle_40
        if as_found_mean is not None:
            field_dict["AsFoundMean"] = as_found_mean
        if as_found_mean_raw is not None:
            field_dict["AsFoundMeanRaw"] = as_found_mean_raw
        if as_found_sd is not None:
            field_dict["AsFoundSd"] = as_found_sd
        if as_found_sd_raw is not None:
            field_dict["AsFoundSdRaw"] = as_found_sd_raw
        if as_found_delta is not None:
            field_dict["AsFoundDelta"] = as_found_delta
        if as_found_range is not None:
            field_dict["AsFoundRange"] = as_found_range
        if as_found_cv is not None:
            field_dict["AsFoundCv"] = as_found_cv
        if as_found_cv_raw is not None:
            field_dict["AsFoundCvRaw"] = as_found_cv_raw
        if as_found_result is not None:
            field_dict["AsFoundResult"] = as_found_result
        if as_found_range_result is not None:
            field_dict["AsFoundRangeResult"] = as_found_range_result
        if as_found_delta_result is not None:
            field_dict["AsFoundDeltaResult"] = as_found_delta_result
        if as_found_min_result is not None:
            field_dict["AsFoundMinResult"] = as_found_min_result
        if as_found_max_result is not None:
            field_dict["AsFoundMaxResult"] = as_found_max_result
        if as_found_tar_result is not None:
            field_dict["AsFoundTarResult"] = as_found_tar_result
        if as_found_tur_result is not None:
            field_dict["AsFoundTurResult"] = as_found_tur_result
        if as_found_error_result is not None:
            field_dict["AsFoundErrorResult"] = as_found_error_result
        if as_found_sd_result is not None:
            field_dict["AsFoundSdResult"] = as_found_sd_result
        if as_found_cv_result is not None:
            field_dict["AsFoundCvResult"] = as_found_cv_result
        if as_found_custom_field_result is not None:
            field_dict["AsFoundCustomFieldResult"] = as_found_custom_field_result
        if as_found_mu is not None:
            field_dict["AsFoundMu"] = as_found_mu
        if as_found_mu_raw is not None:
            field_dict["AsFoundMuRaw"] = as_found_mu_raw
        if as_found_mu_effective_dof is not None:
            field_dict["AsFoundMuEffectiveDOF"] = as_found_mu_effective_dof
        if as_found_mu_coverage_factor is not None:
            field_dict["AsFoundMUCoverageFactor"] = as_found_mu_coverage_factor
        if as_found_cmc is not None:
            field_dict["AsFoundCmc"] = as_found_cmc
        if as_found_cmc_comments is not None:
            field_dict["AsFoundCmcComments"] = as_found_cmc_comments
        if as_found_calculated_uncertainty is not None:
            field_dict["AsFoundCalculatedUncertainty"] = as_found_calculated_uncertainty
        if as_found_lab_mu is not None:
            field_dict["AsFoundLabMu"] = as_found_lab_mu
        if as_found_uncertainty_budget is not None:
            field_dict["AsFoundUncertaintyBudget"] = as_found_uncertainty_budget
        if as_found_mu_extended is not None:
            field_dict["AsFoundMuExtended"] = as_found_mu_extended
        if as_found_channel is not None:
            field_dict["AsFoundChannel"] = as_found_channel
        if as_found_measurement_type is not None:
            field_dict["AsFoundMeasurementType"] = as_found_measurement_type
        if as_found_updated_by is not None:
            field_dict["AsFoundUpdatedBy"] = as_found_updated_by
        if as_found_updated_on is not None:
            field_dict["AsFoundUpdatedOn"] = as_found_updated_on
        if as_left_abbreviated_uom is not None:
            field_dict["AsLeftAbbreviatedUOM"] = as_left_abbreviated_uom
        if as_left_unit_scale_factor is not None:
            field_dict["AsLeftUnitScaleFactor"] = as_left_unit_scale_factor
        if as_found_specification_title is not None:
            field_dict["AsFoundSpecificationTitle"] = as_found_specification_title
        if as_found_specification_subtitle is not None:
            field_dict["AsFoundSpecificationSubtitle"] = as_found_specification_subtitle
        if as_found_specification_group is not None:
            field_dict["AsFoundSpecificationGroup"] = as_found_specification_group
        if as_found_batch_type is not None:
            field_dict["AsFoundBatchType"] = as_found_batch_type
        if as_found_batch_result is not None:
            field_dict["AsFoundBatchResult"] = as_found_batch_result
        if as_found_is_by_channel is not None:
            field_dict["AsFoundIsByChannel"] = as_found_is_by_channel
        if as_found_channel_count is not None:
            field_dict["AsFoundChannelCount"] = as_found_channel_count
        if as_found_commenced_on is not None:
            field_dict["AsFoundCommencedOn"] = as_found_commenced_on
        if as_found_commenced_by is not None:
            field_dict["AsFoundCommencedBy"] = as_found_commenced_by
        if as_found_z_factor is not None:
            field_dict["AsFoundZFactor"] = as_found_z_factor
        if as_found_air_buoyancy is not None:
            field_dict["AsFoundAirBuoyancy"] = as_found_air_buoyancy
        if as_found_evaporation_rate is not None:
            field_dict["AsFoundEvaporationRate"] = as_found_evaporation_rate
        if as_found_ambient_temperature is not None:
            field_dict["AsFoundAmbientTemperature"] = as_found_ambient_temperature
        if as_found_air_humidity is not None:
            field_dict["AsFoundAirHumidity"] = as_found_air_humidity
        if as_found_barometric_pressure is not None:
            field_dict["AsFoundBarometricPressure"] = as_found_barometric_pressure
        if as_found_altitude is not None:
            field_dict["AsFoundAltitude"] = as_found_altitude
        if as_found_wind_speed is not None:
            field_dict["AsFoundWindSpeed"] = as_found_wind_speed
        if as_found_solar_radiation is not None:
            field_dict["AsFoundSolarRadiation"] = as_found_solar_radiation
        if as_found_light_intensity is not None:
            field_dict["AsFoundLightIntensity"] = as_found_light_intensity
        if as_found_noise_level is not None:
            field_dict["AsFoundNoiseLevel"] = as_found_noise_level
        if as_found_ph_level is not None:
            field_dict["AsFoundPhLevel"] = as_found_ph_level
        if as_found_water_conductivity is not None:
            field_dict["AsFoundWaterConductivity"] = as_found_water_conductivity
        if as_found_water_temperature is not None:
            field_dict["AsFoundWaterTemperature"] = as_found_water_temperature
        if as_found_z_factor_uom is not None:
            field_dict["AsFoundZFactorUom"] = as_found_z_factor_uom
        if as_found_air_buoyancy_uom is not None:
            field_dict["AsFoundAirBuoyancyUom"] = as_found_air_buoyancy_uom
        if as_found_evaporation_rate_uom is not None:
            field_dict["AsFoundEvaporationRateUom"] = as_found_evaporation_rate_uom
        if as_found_ambient_temperature_uom is not None:
            field_dict["AsFoundAmbientTemperatureUom"] = as_found_ambient_temperature_uom
        if as_found_air_humidity_uom is not None:
            field_dict["AsFoundAirHumidityUom"] = as_found_air_humidity_uom
        if as_found_barometric_pressure_uom is not None:
            field_dict["AsFoundBarometricPressureUom"] = as_found_barometric_pressure_uom
        if as_found_altitude_uom is not None:
            field_dict["AsFoundAltitudeUom"] = as_found_altitude_uom
        if as_found_wind_speed_uom is not None:
            field_dict["AsFoundWindSpeedUom"] = as_found_wind_speed_uom
        if as_found_solar_radiation_uom is not None:
            field_dict["AsFoundSolarRadiationUom"] = as_found_solar_radiation_uom
        if as_found_light_intensity_uom is not None:
            field_dict["AsFoundLightIntensityUom"] = as_found_light_intensity_uom
        if as_found_noise_level_uom is not None:
            field_dict["AsFoundNoiseLevelUom"] = as_found_noise_level_uom
        if as_found_ph_level_uom is not None:
            field_dict["AsFoundPhLevelUom"] = as_found_ph_level_uom
        if as_found_water_conductivity_uom is not None:
            field_dict["AsFoundWaterConductivityUom"] = as_found_water_conductivity_uom
        if as_found_water_temperature_uom is not None:
            field_dict["AsFoundWaterTemperatureUom"] = as_found_water_temperature_uom
        if as_found_abbreviated_uom is not None:
            field_dict["AsFoundAbbreviatedUOM"] = as_found_abbreviated_uom
        if as_found_unit_scale_factor is not None:
            field_dict["AsFoundUnitScaleFactor"] = as_found_unit_scale_factor
        if as_found_specification_name is not None:
            field_dict["AsFoundSpecificationName"] = as_found_specification_name
        if as_found_parameter_name is not None:
            field_dict["AsFoundParameterName"] = as_found_parameter_name
        if as_found_display_order is not None:
            field_dict["AsFoundDisplayOrder"] = as_found_display_order
        if as_found_unit_of_measure is not None:
            field_dict["AsFoundUnitOfMeasure"] = as_found_unit_of_measure
        if as_found_display_format is not None:
            field_dict["AsFoundDisplayFormat"] = as_found_display_format
        if as_found_precision is not None:
            field_dict["AsFoundPrecision"] = as_found_precision
        if as_found_precision_type is not None:
            field_dict["AsFoundPrecisionType"] = as_found_precision_type
        if as_found_minimum is not None:
            field_dict["AsFoundMinimum"] = as_found_minimum
        if as_found_nominal is not None:
            field_dict["AsFoundNominal"] = as_found_nominal
        if as_found_expected_value is not None:
            field_dict["AsFoundExpectedValue"] = as_found_expected_value
        if as_found_expected_value_raw is not None:
            field_dict["AsFoundExpectedValueRaw"] = as_found_expected_value_raw
        if as_found_test_value is not None:
            field_dict["AsFoundTestValue"] = as_found_test_value
        if as_found_base_value is not None:
            field_dict["AsFoundBaseValue"] = as_found_base_value
        if as_found_maxi_mum is not None:
            field_dict["AsFoundMaxiMum"] = as_found_maxi_mum
        if as_found_resolution is not None:
            field_dict["AsFoundResolution"] = as_found_resolution
        if as_found_resolution_count is not None:
            field_dict["AsFoundResolutionCount"] = as_found_resolution_count
        if as_found_measurement_batch_id is not None:
            field_dict["AsFoundMeasurementBatchId"] = as_found_measurement_batch_id
        if as_found_measurement_id is not None:
            field_dict["AsFoundMeasurementId"] = as_found_measurement_id
        if as_found_standard_id is not None:
            field_dict["AsFoundStandardId"] = as_found_standard_id
        if as_found_tool_id is not None:
            field_dict["AsFoundToolId"] = as_found_tool_id
        if as_found_measurement_condition_id is not None:
            field_dict["AsFoundMeasurementConditionId"] = as_found_measurement_condition_id
        if as_found_measurement_point_id is not None:
            field_dict["AsFoundMeasurementPointId"] = as_found_measurement_point_id
        if as_left_parameter_id is not None:
            field_dict["AsLeftParameterId"] = as_left_parameter_id
        if as_left_sd_header is not None:
            field_dict["AsLeftSdHeader"] = as_left_sd_header
        if as_left_cv_header is not None:
            field_dict["AsLeftCvHeader"] = as_left_cv_header
        if as_left_measurement_local_time is not None:
            field_dict["AsLeftMeasurementLocalTime"] = as_left_measurement_local_time
        if as_left_reading_entry_math is not None:
            field_dict["AsLeftReadingEntryMath"] = as_left_reading_entry_math
        if as_left_reading_entry_math_string is not None:
            field_dict["AsLeftReadingEntryMathString"] = as_left_reading_entry_math_string
        if as_left_value_1 is not None:
            field_dict["AsLeftValue1"] = as_left_value_1
        if as_left_value_2 is not None:
            field_dict["AsLeftValue2"] = as_left_value_2
        if as_left_value_3 is not None:
            field_dict["AsLeftValue3"] = as_left_value_3
        if as_left_value_4 is not None:
            field_dict["AsLeftValue4"] = as_left_value_4
        if as_left_value_5 is not None:
            field_dict["AsLeftValue5"] = as_left_value_5
        if as_left_value_6 is not None:
            field_dict["AsLeftValue6"] = as_left_value_6
        if as_left_value_7 is not None:
            field_dict["AsLeftValue7"] = as_left_value_7
        if as_left_value_8 is not None:
            field_dict["AsLeftValue8"] = as_left_value_8
        if as_left_value_9 is not None:
            field_dict["AsLeftValue9"] = as_left_value_9
        if as_left_value_10 is not None:
            field_dict["AsLeftValue10"] = as_left_value_10
        if as_left_value_11 is not None:
            field_dict["AsLeftValue11"] = as_left_value_11
        if as_left_value_12 is not None:
            field_dict["AsLeftValue12"] = as_left_value_12
        if as_left_value_13 is not None:
            field_dict["AsLeftValue13"] = as_left_value_13
        if as_left_value_14 is not None:
            field_dict["AsLeftValue14"] = as_left_value_14
        if as_left_value_15 is not None:
            field_dict["AsLeftValue15"] = as_left_value_15
        if as_left_value_16 is not None:
            field_dict["AsLeftValue16"] = as_left_value_16
        if as_left_value_17 is not None:
            field_dict["AsLeftValue17"] = as_left_value_17
        if as_left_value_18 is not None:
            field_dict["AsLeftValue18"] = as_left_value_18
        if as_left_value_19 is not None:
            field_dict["AsLeftValue19"] = as_left_value_19
        if as_left_value_20 is not None:
            field_dict["AsLeftValue20"] = as_left_value_20
        if as_left_value_21 is not None:
            field_dict["AsLeftValue21"] = as_left_value_21
        if as_left_value_22 is not None:
            field_dict["AsLeftValue22"] = as_left_value_22
        if as_left_value_23 is not None:
            field_dict["AsLeftValue23"] = as_left_value_23
        if as_left_value_24 is not None:
            field_dict["AsLeftValue24"] = as_left_value_24
        if as_left_value_25 is not None:
            field_dict["AsLeftValue25"] = as_left_value_25
        if as_left_value_26 is not None:
            field_dict["AsLeftValue26"] = as_left_value_26
        if as_left_value_27 is not None:
            field_dict["AsLeftValue27"] = as_left_value_27
        if as_left_value_28 is not None:
            field_dict["AsLeftValue28"] = as_left_value_28
        if as_left_value_29 is not None:
            field_dict["AsLeftValue29"] = as_left_value_29
        if as_left_value_30 is not None:
            field_dict["AsLeftValue30"] = as_left_value_30
        if as_left_value_31 is not None:
            field_dict["AsLeftValue31"] = as_left_value_31
        if as_left_value_32 is not None:
            field_dict["AsLeftValue32"] = as_left_value_32
        if as_left_value_33 is not None:
            field_dict["AsLeftValue33"] = as_left_value_33
        if as_left_value_34 is not None:
            field_dict["AsLeftValue34"] = as_left_value_34
        if as_left_value_35 is not None:
            field_dict["AsLeftValue35"] = as_left_value_35
        if as_left_value_36 is not None:
            field_dict["AsLeftValue36"] = as_left_value_36
        if as_left_value_37 is not None:
            field_dict["AsLeftValue37"] = as_left_value_37
        if as_left_value_38 is not None:
            field_dict["AsLeftValue38"] = as_left_value_38
        if as_left_value_39 is not None:
            field_dict["AsLeftValue39"] = as_left_value_39
        if as_left_value_40 is not None:
            field_dict["AsLeftValue40"] = as_left_value_40
        if as_left_raw_value_1 is not None:
            field_dict["AsLeftRawValue1"] = as_left_raw_value_1
        if as_left_raw_value_2 is not None:
            field_dict["AsLeftRawValue2"] = as_left_raw_value_2
        if as_left_raw_value_3 is not None:
            field_dict["AsLeftRawValue3"] = as_left_raw_value_3
        if as_left_raw_value_4 is not None:
            field_dict["AsLeftRawValue4"] = as_left_raw_value_4
        if as_left_raw_value_5 is not None:
            field_dict["AsLeftRawValue5"] = as_left_raw_value_5
        if as_left_raw_value_6 is not None:
            field_dict["AsLeftRawValue6"] = as_left_raw_value_6
        if as_left_raw_value_7 is not None:
            field_dict["AsLeftRawValue7"] = as_left_raw_value_7
        if as_left_raw_value_8 is not None:
            field_dict["AsLeftRawValue8"] = as_left_raw_value_8
        if as_left_raw_value_9 is not None:
            field_dict["AsLeftRawValue9"] = as_left_raw_value_9
        if as_left_raw_value_10 is not None:
            field_dict["AsLeftRawValue10"] = as_left_raw_value_10
        if as_left_raw_value_11 is not None:
            field_dict["AsLeftRawValue11"] = as_left_raw_value_11
        if as_left_raw_value_12 is not None:
            field_dict["AsLeftRawValue12"] = as_left_raw_value_12
        if as_left_raw_value_13 is not None:
            field_dict["AsLeftRawValue13"] = as_left_raw_value_13
        if as_left_raw_value_14 is not None:
            field_dict["AsLeftRawValue14"] = as_left_raw_value_14
        if as_left_raw_value_15 is not None:
            field_dict["AsLeftRawValue15"] = as_left_raw_value_15
        if as_left_raw_value_16 is not None:
            field_dict["AsLeftRawValue16"] = as_left_raw_value_16
        if as_left_raw_value_17 is not None:
            field_dict["AsLeftRawValue17"] = as_left_raw_value_17
        if as_left_raw_value_18 is not None:
            field_dict["AsLeftRawValue18"] = as_left_raw_value_18
        if as_left_raw_value_19 is not None:
            field_dict["AsLeftRawValue19"] = as_left_raw_value_19
        if as_left_raw_value_20 is not None:
            field_dict["AsLeftRawValue20"] = as_left_raw_value_20
        if as_left_raw_value_21 is not None:
            field_dict["AsLeftRawValue21"] = as_left_raw_value_21
        if as_left_raw_value_22 is not None:
            field_dict["AsLeftRawValue22"] = as_left_raw_value_22
        if as_left_raw_value_23 is not None:
            field_dict["AsLeftRawValue23"] = as_left_raw_value_23
        if as_left_raw_value_24 is not None:
            field_dict["AsLeftRawValue24"] = as_left_raw_value_24
        if as_left_raw_value_25 is not None:
            field_dict["AsLeftRawValue25"] = as_left_raw_value_25
        if as_left_raw_value_26 is not None:
            field_dict["AsLeftRawValue26"] = as_left_raw_value_26
        if as_left_raw_value_27 is not None:
            field_dict["AsLeftRawValue27"] = as_left_raw_value_27
        if as_left_raw_value_28 is not None:
            field_dict["AsLeftRawValue28"] = as_left_raw_value_28
        if as_left_raw_value_29 is not None:
            field_dict["AsLeftRawValue29"] = as_left_raw_value_29
        if as_left_raw_value_30 is not None:
            field_dict["AsLeftRawValue30"] = as_left_raw_value_30
        if as_left_raw_value_31 is not None:
            field_dict["AsLeftRawValue31"] = as_left_raw_value_31
        if as_left_raw_value_32 is not None:
            field_dict["AsLeftRawValue32"] = as_left_raw_value_32
        if as_left_raw_value_33 is not None:
            field_dict["AsLeftRawValue33"] = as_left_raw_value_33
        if as_left_raw_value_34 is not None:
            field_dict["AsLeftRawValue34"] = as_left_raw_value_34
        if as_left_raw_value_35 is not None:
            field_dict["AsLeftRawValue35"] = as_left_raw_value_35
        if as_left_raw_value_36 is not None:
            field_dict["AsLeftRawValue36"] = as_left_raw_value_36
        if as_left_raw_value_37 is not None:
            field_dict["AsLeftRawValue37"] = as_left_raw_value_37
        if as_left_raw_value_38 is not None:
            field_dict["AsLeftRawValue38"] = as_left_raw_value_38
        if as_left_raw_value_39 is not None:
            field_dict["AsLeftRawValue39"] = as_left_raw_value_39
        if as_left_raw_value_40 is not None:
            field_dict["AsLeftRawValue40"] = as_left_raw_value_40
        if as_left_value_subtitle_1 is not None:
            field_dict["AsLeftValueSubtitle1"] = as_left_value_subtitle_1
        if as_left_value_subtitle_2 is not None:
            field_dict["AsLeftValueSubtitle2"] = as_left_value_subtitle_2
        if as_left_value_subtitle_3 is not None:
            field_dict["AsLeftValueSubtitle3"] = as_left_value_subtitle_3
        if as_left_value_subtitle_4 is not None:
            field_dict["AsLeftValueSubtitle4"] = as_left_value_subtitle_4
        if as_left_value_subtitle_5 is not None:
            field_dict["AsLeftValueSubtitle5"] = as_left_value_subtitle_5
        if as_left_value_subtitle_6 is not None:
            field_dict["AsLeftValueSubtitle6"] = as_left_value_subtitle_6
        if as_left_value_subtitle_7 is not None:
            field_dict["AsLeftValueSubtitle7"] = as_left_value_subtitle_7
        if as_left_value_subtitle_8 is not None:
            field_dict["AsLeftValueSubtitle8"] = as_left_value_subtitle_8
        if as_left_value_subtitle_9 is not None:
            field_dict["AsLeftValueSubtitle9"] = as_left_value_subtitle_9
        if as_left_value_subtitle_10 is not None:
            field_dict["AsLeftValueSubtitle10"] = as_left_value_subtitle_10
        if as_left_value_subtitle_11 is not None:
            field_dict["AsLeftValueSubtitle11"] = as_left_value_subtitle_11
        if as_left_value_subtitle_12 is not None:
            field_dict["AsLeftValueSubtitle12"] = as_left_value_subtitle_12
        if as_left_value_subtitle_13 is not None:
            field_dict["AsLeftValueSubtitle13"] = as_left_value_subtitle_13
        if as_left_value_subtitle_14 is not None:
            field_dict["AsLeftValueSubtitle14"] = as_left_value_subtitle_14
        if as_left_value_subtitle_15 is not None:
            field_dict["AsLeftValueSubtitle15"] = as_left_value_subtitle_15
        if as_left_value_subtitle_16 is not None:
            field_dict["AsLeftValueSubtitle16"] = as_left_value_subtitle_16
        if as_left_value_subtitle_17 is not None:
            field_dict["AsLeftValueSubtitle17"] = as_left_value_subtitle_17
        if as_left_value_subtitle_18 is not None:
            field_dict["AsLeftValueSubtitle18"] = as_left_value_subtitle_18
        if as_left_value_subtitle_19 is not None:
            field_dict["AsLeftValueSubtitle19"] = as_left_value_subtitle_19
        if as_left_value_subtitle_20 is not None:
            field_dict["AsLeftValueSubtitle20"] = as_left_value_subtitle_20
        if as_left_value_subtitle_21 is not None:
            field_dict["AsLeftValueSubtitle21"] = as_left_value_subtitle_21
        if as_left_value_subtitle_22 is not None:
            field_dict["AsLeftValueSubtitle22"] = as_left_value_subtitle_22
        if as_left_value_subtitle_23 is not None:
            field_dict["AsLeftValueSubtitle23"] = as_left_value_subtitle_23
        if as_left_value_subtitle_24 is not None:
            field_dict["AsLeftValueSubtitle24"] = as_left_value_subtitle_24
        if as_left_value_subtitle_25 is not None:
            field_dict["AsLeftValueSubtitle25"] = as_left_value_subtitle_25
        if as_left_value_subtitle_26 is not None:
            field_dict["AsLeftValueSubtitle26"] = as_left_value_subtitle_26
        if as_left_value_subtitle_27 is not None:
            field_dict["AsLeftValueSubtitle27"] = as_left_value_subtitle_27
        if as_left_value_subtitle_28 is not None:
            field_dict["AsLeftValueSubtitle28"] = as_left_value_subtitle_28
        if as_left_value_subtitle_29 is not None:
            field_dict["AsLeftValueSubtitle29"] = as_left_value_subtitle_29
        if as_left_value_subtitle_30 is not None:
            field_dict["AsLeftValueSubtitle30"] = as_left_value_subtitle_30
        if as_left_value_subtitle_31 is not None:
            field_dict["AsLeftValueSubtitle31"] = as_left_value_subtitle_31
        if as_left_value_subtitle_32 is not None:
            field_dict["AsLeftValueSubtitle32"] = as_left_value_subtitle_32
        if as_left_value_subtitle_33 is not None:
            field_dict["AsLeftValueSubtitle33"] = as_left_value_subtitle_33
        if as_left_value_subtitle_34 is not None:
            field_dict["AsLeftValueSubtitle34"] = as_left_value_subtitle_34
        if as_left_value_subtitle_35 is not None:
            field_dict["AsLeftValueSubtitle35"] = as_left_value_subtitle_35
        if as_left_value_subtitle_36 is not None:
            field_dict["AsLeftValueSubtitle36"] = as_left_value_subtitle_36
        if as_left_value_subtitle_37 is not None:
            field_dict["AsLeftValueSubtitle37"] = as_left_value_subtitle_37
        if as_left_value_subtitle_38 is not None:
            field_dict["AsLeftValueSubtitle38"] = as_left_value_subtitle_38
        if as_left_value_subtitle_39 is not None:
            field_dict["AsLeftValueSubtitle39"] = as_left_value_subtitle_39
        if as_left_value_subtitle_40 is not None:
            field_dict["AsLeftValueSubtitle40"] = as_left_value_subtitle_40
        if as_left_mean is not None:
            field_dict["AsLeftMean"] = as_left_mean
        if as_left_mean_raw is not None:
            field_dict["AsLeftMeanRaw"] = as_left_mean_raw
        if as_left_sd is not None:
            field_dict["AsLeftSd"] = as_left_sd
        if as_left_sd_raw is not None:
            field_dict["AsLeftSdRaw"] = as_left_sd_raw
        if as_left_cv is not None:
            field_dict["AsLeftCv"] = as_left_cv
        if as_left_cv_raw is not None:
            field_dict["AsLeftCvRaw"] = as_left_cv_raw
        if as_left_delta is not None:
            field_dict["AsLeftDelta"] = as_left_delta
        if as_left_range is not None:
            field_dict["AsLeftRange"] = as_left_range
        if as_left_result is not None:
            field_dict["AsLeftResult"] = as_left_result
        if as_left_range_result is not None:
            field_dict["AsLeftRangeResult"] = as_left_range_result
        if as_left_delta_result is not None:
            field_dict["AsLeftDeltaResult"] = as_left_delta_result
        if as_left_min_result is not None:
            field_dict["AsLeftMinResult"] = as_left_min_result
        if as_left_max_result is not None:
            field_dict["AsLeftMaxResult"] = as_left_max_result
        if as_left_tar_result is not None:
            field_dict["AsLeftTarResult"] = as_left_tar_result
        if as_left_tur_result is not None:
            field_dict["AsLeftTurResult"] = as_left_tur_result
        if as_left_error_result is not None:
            field_dict["AsLeftErrorResult"] = as_left_error_result
        if as_left_sd_result is not None:
            field_dict["AsLeftSdResult"] = as_left_sd_result
        if as_left_cv_result is not None:
            field_dict["AsLeftCvResult"] = as_left_cv_result
        if as_left_custom_field_result is not None:
            field_dict["AsLeftCustomFieldResult"] = as_left_custom_field_result
        if as_left_mu is not None:
            field_dict["AsLeftMu"] = as_left_mu
        if as_left_mu_raw is not None:
            field_dict["AsLeftMuRaw"] = as_left_mu_raw
        if as_left_mu_effective_dof is not None:
            field_dict["AsLeftMUEffectiveDOF"] = as_left_mu_effective_dof
        if as_left_mu_coverage_factor is not None:
            field_dict["AsLeftMUCoverageFactor"] = as_left_mu_coverage_factor
        if as_left_cmc is not None:
            field_dict["AsLeftCmc"] = as_left_cmc
        if as_left_cmc_comments is not None:
            field_dict["AsLeftCmcComments"] = as_left_cmc_comments
        if as_left_calculated_uncertainty is not None:
            field_dict["AsLeftCalculatedUncertainty"] = as_left_calculated_uncertainty
        if as_left_lab_mu is not None:
            field_dict["AsLeftLabMu"] = as_left_lab_mu
        if as_left_uncertainty_budget is not None:
            field_dict["AsLeftUncertaintyBudget"] = as_left_uncertainty_budget
        if as_left_mu_extended is not None:
            field_dict["AsLeftMuExtended"] = as_left_mu_extended
        if as_left_channel is not None:
            field_dict["AsLeftChannel"] = as_left_channel
        if as_left_measurement_type is not None:
            field_dict["AsLeftMeasurementType"] = as_left_measurement_type
        if as_left_updated_by is not None:
            field_dict["AsLeftUpdatedBy"] = as_left_updated_by
        if as_left_updated_on is not None:
            field_dict["AsLeftUpdatedOn"] = as_left_updated_on
        if as_left_specification_title is not None:
            field_dict["AsLeftSpecificationTitle"] = as_left_specification_title
        if as_left_specification_subtitle is not None:
            field_dict["AsLeftSpecificationSubtitle"] = as_left_specification_subtitle
        if as_left_specification_group is not None:
            field_dict["AsLeftSpecificationGroup"] = as_left_specification_group
        if as_left_batch_type is not None:
            field_dict["AsLeftBatchType"] = as_left_batch_type
        if as_left_batch_result is not None:
            field_dict["AsLeftBatchResult"] = as_left_batch_result
        if as_left_is_by_channel is not None:
            field_dict["AsLeftIsByChannel"] = as_left_is_by_channel
        if as_left_channel_count is not None:
            field_dict["AsLeftChannelCount"] = as_left_channel_count
        if as_left_commenced_on is not None:
            field_dict["AsLeftCommencedOn"] = as_left_commenced_on
        if as_left_commenced_by is not None:
            field_dict["AsLeftCommencedBy"] = as_left_commenced_by
        if as_left_z_factor is not None:
            field_dict["AsLeftZFactor"] = as_left_z_factor
        if as_left_air_buoyancy is not None:
            field_dict["AsLeftAirBuoyancy"] = as_left_air_buoyancy
        if as_left_evaporation_rate is not None:
            field_dict["AsLeftEvaporationRate"] = as_left_evaporation_rate
        if as_left_ambient_temperature is not None:
            field_dict["AsLeftAmbientTemperature"] = as_left_ambient_temperature
        if as_left_air_humidity is not None:
            field_dict["AsLeftAirHumidity"] = as_left_air_humidity
        if as_left_barometric_pressure is not None:
            field_dict["AsLeftBarometricPressure"] = as_left_barometric_pressure
        if as_left_altitude is not None:
            field_dict["AsLeftAltitude"] = as_left_altitude
        if as_left_wind_speed is not None:
            field_dict["AsLeftWindSpeed"] = as_left_wind_speed
        if as_left_solar_radiation is not None:
            field_dict["AsLeftSolarRadiation"] = as_left_solar_radiation
        if as_left_light_intensity is not None:
            field_dict["AsLeftLightIntensity"] = as_left_light_intensity
        if as_left_noise_level is not None:
            field_dict["AsLeftNoiseLevel"] = as_left_noise_level
        if as_left_ph_level is not None:
            field_dict["AsLeftPhLevel"] = as_left_ph_level
        if as_left_water_conductivity is not None:
            field_dict["AsLeftWaterConductivity"] = as_left_water_conductivity
        if as_left_water_temperature is not None:
            field_dict["AsLeftWaterTemperature"] = as_left_water_temperature
        if as_left_z_factor_uom is not None:
            field_dict["AsLeftZFactorUom"] = as_left_z_factor_uom
        if as_left_air_buoyancy_uom is not None:
            field_dict["AsLeftAirBuoyancyUom"] = as_left_air_buoyancy_uom
        if as_left_evaporation_rate_uom is not None:
            field_dict["AsLeftEvaporationRateUom"] = as_left_evaporation_rate_uom
        if as_left_ambient_temperature_uom is not None:
            field_dict["AsLeftAmbientTemperatureUom"] = as_left_ambient_temperature_uom
        if as_left_air_humidity_uom is not None:
            field_dict["AsLeftAirHumidityUom"] = as_left_air_humidity_uom
        if as_left_barometric_pressure_uom is not None:
            field_dict["AsLeftBarometricPressureUom"] = as_left_barometric_pressure_uom
        if as_left_altitude_uom is not None:
            field_dict["AsLeftAltitudeUom"] = as_left_altitude_uom
        if as_left_wind_speed_uom is not None:
            field_dict["AsLeftWindSpeedUom"] = as_left_wind_speed_uom
        if as_left_solar_radiation_uom is not None:
            field_dict["AsLeftSolarRadiationUom"] = as_left_solar_radiation_uom
        if as_left_light_intensity_uom is not None:
            field_dict["AsLeftLightIntensityUom"] = as_left_light_intensity_uom
        if as_left_noise_level_uom is not None:
            field_dict["AsLeftNoiseLevelUom"] = as_left_noise_level_uom
        if as_left_ph_level_uom is not None:
            field_dict["AsLeftPhLevelUom"] = as_left_ph_level_uom
        if as_left_water_conductivity_uom is not None:
            field_dict["AsLeftWaterConductivityUom"] = as_left_water_conductivity_uom
        if as_left_water_temperature_uom is not None:
            field_dict["AsLeftWaterTemperatureUom"] = as_left_water_temperature_uom
        if as_left_specification_name is not None:
            field_dict["AsLeftSpecificationName"] = as_left_specification_name
        if as_left_parameter_name is not None:
            field_dict["AsLeftParameterName"] = as_left_parameter_name
        if as_left_display_order is not None:
            field_dict["AsLeftDisplayOrder"] = as_left_display_order
        if as_left_unit_of_measure is not None:
            field_dict["AsLeftUnitOfMeasure"] = as_left_unit_of_measure
        if as_left_display_format is not None:
            field_dict["AsLeftDisplayFormat"] = as_left_display_format
        if as_left_precision is not None:
            field_dict["AsLeftPrecision"] = as_left_precision
        if as_left_precision_type is not None:
            field_dict["AsLeftPrecisionType"] = as_left_precision_type
        if as_left_minimum is not None:
            field_dict["AsLeftMinimum"] = as_left_minimum
        if as_left_nominal is not None:
            field_dict["AsLeftNominal"] = as_left_nominal
        if as_left_expected_value is not None:
            field_dict["AsLeftExpectedValue"] = as_left_expected_value
        if as_left_expected_value_raw is not None:
            field_dict["AsLeftExpectedValueRaw"] = as_left_expected_value_raw
        if as_left_test_value is not None:
            field_dict["AsLeftTestValue"] = as_left_test_value
        if as_left_base_value is not None:
            field_dict["AsLeftBaseValue"] = as_left_base_value
        if as_left_maxi_mum is not None:
            field_dict["AsLeftMaxiMum"] = as_left_maxi_mum
        if as_left_resolution is not None:
            field_dict["AsLeftResolution"] = as_left_resolution
        if as_left_resolution_count is not None:
            field_dict["AsLeftResolutionCount"] = as_left_resolution_count
        if as_left_measurement_not_taken_result is not None:
            field_dict["AsLeftMeasurementNotTakenResult"] = as_left_measurement_not_taken_result
        if as_left_hide_from_certificate is not None:
            field_dict["AsLeftHideFromCertificate"] = as_left_hide_from_certificate
        if as_left_measurement_not_taken_reason is not None:
            field_dict["AsLeftMeasurementNotTakenReason"] = as_left_measurement_not_taken_reason
        if as_left_measurement_batch_id is not None:
            field_dict["AsLeftMeasurementBatchId"] = as_left_measurement_batch_id
        if as_left_measurement_id is not None:
            field_dict["AsLeftMeasurementId"] = as_left_measurement_id
        if as_left_standard_id is not None:
            field_dict["AsLeftStandardId"] = as_left_standard_id
        if as_left_tool_id is not None:
            field_dict["AsLeftToolId"] = as_left_tool_id
        if as_left_measurement_condition_id is not None:
            field_dict["AsLeftMeasurementConditionId"] = as_left_measurement_condition_id
        if as_left_measurement_point_id is not None:
            field_dict["AsLeftMeasurementPointId"] = as_left_measurement_point_id
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        barcode = d.pop("Barcode", None)
        display_name = d.pop("DisplayName", None)
        display_part_number = d.pop("DisplayPartNumber", None)
        part_number = d.pop("PartNumber", None)
        vendor_company_id = d.pop("VendorCompanyId", None)
        service_order_number = d.pop("ServiceOrderNumber", None)
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
        service_comments = d.pop("ServiceComments", None)
        order_item_number = d.pop("OrderItemNumber", None)
        service_total = d.pop("ServiceTotal", None)
        repairs_total = d.pop("RepairsTotal", None)
        parts_total = d.pop("PartsTotal", None)
        asset_tag = d.pop("AssetTag", None)
        asset_user = d.pop("AssetUser", None)
        serial_number = d.pop("SerialNumber", None)
        equipment_id = d.pop("EquipmentId", None)
        legacy_identifier = d.pop("LegacyIdentifier", None)
        asset_name = d.pop("AssetName", None)
        asset_description = d.pop("AssetDescription", None)
        product_name = d.pop("ProductName", None)
        product_description = d.pop("ProductDescription", None)
        asset_maker = d.pop("AssetMaker", None)
        asset_tag_change = d.pop("AssetTagChange", None)
        asset_user_change = d.pop("AssetUserChange", None)
        serial_number_change = d.pop("SerialNumberChange", None)

        def _parse_service_date(data: object) -> Optional[datetime.datetime]:
            if data is None:
                return data
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
            if data is None:
                return data
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
        site_name = d.pop("SiteName", None)
        po_number = d.pop("PoNumber", None)

        def _parse_shipped_date(data: object) -> Optional[datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shipped_date_type_0 = isoparse(data)
                return shipped_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        shipped_date = _parse_shipped_date(d.pop("ShippedDate", None))
        tracking_number = d.pop("TrackingNumber", None)
        payment_terms = d.pop("PaymentTerms", None)
        shipping_method = d.pop("ShippingMethod", None)
        location = d.pop("Location", None)
        site_access_notes = d.pop("SiteAccessNotes", None)
        as_left_decimal_places = d.pop("AsLeftDecimalPlaces", None)
        as_left_measurement_set_name = d.pop("AsLeftMeasurementSetName", None)
        as_left_measurement_set_id = d.pop("AsLeftMeasurementSetId", None)
        as_left_adjustment_threshold = d.pop("AsLeftAdjustmentThreshold", None)
        as_left_mean_extended = d.pop("AsLeftMeanExtended", None)
        as_left_sd_extended = d.pop("AsLeftSdExtended", None)
        as_left_range_extended = d.pop("AsLeftRangeExtended", None)
        as_left_delta_extended = d.pop("AsLeftDeltaExtended", None)
        as_left_cv_extended = d.pop("AsLeftCvExtended", None)
        as_left_nominal_extended = d.pop("AsLeftNominalExtended", None)
        as_left_min_max_header = d.pop("AsLeftMinMaxHeader", None)
        as_left_accuracy_class = d.pop("AsLeftAccuracyClass", None)
        as_left_accuracy_class_min = d.pop("AsLeftAccuracyClassMin", None)
        as_left_accuracy_class_max = d.pop("AsLeftAccuracyClassMax", None)
        as_left_minimum_measured_value = d.pop("AsLeftMinimumMeasuredValue", None)
        as_left_maxi_mum_measured_value = d.pop("AsLeftMaxiMumMeasuredValue", None)
        as_left_min_max_value_extended = d.pop("AsLeftMinMaxValueExtended", None)
        as_left_tool_range_name = d.pop("AsLeftToolRangeName", None)
        as_left_tool_range_uncertainty = d.pop("AsLeftToolRangeUncertainty", None)

        def _parse_as_left_primary_tool_last_service_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_left_primary_tool_last_service_date_type_0 = isoparse(data)
                return as_left_primary_tool_last_service_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        as_left_primary_tool_last_service_date = _parse_as_left_primary_tool_last_service_date(
            d.pop("AsLeftPrimaryToolLastServiceDate", None)
        )

        def _parse_as_left_primary_tool_next_service_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_left_primary_tool_next_service_date_type_0 = isoparse(data)
                return as_left_primary_tool_next_service_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        as_left_primary_tool_next_service_date = _parse_as_left_primary_tool_next_service_date(
            d.pop("AsLeftPrimaryToolNextServiceDate", None)
        )
        as_left_primary_tool_calibrated_by = d.pop("AsLeftPrimaryToolCalibratedBy", None)
        as_left_primary_tool_tool_name = d.pop("AsLeftPrimaryToolToolName", None)
        as_left_primary_tool_tool_description = d.pop("AsLeftPrimaryToolToolDescription", None)
        as_left_primary_tool_tool_type_name = d.pop("AsLeftPrimaryToolToolTypeName", None)
        as_left_primary_tool_manufacturer = d.pop("AsLeftPrimaryToolManufacturer", None)
        as_left_primary_tool_manufacturer_part_number = d.pop(
            "AsLeftPrimaryToolManufacturerPartNumber", None
        )
        as_left_primary_tool_serial_number = d.pop("AsLeftPrimaryToolSerialNumber", None)
        as_found_measurement_set_name = d.pop("AsFoundMeasurementSetName", None)
        as_found_measurement_set_id = d.pop("AsFoundMeasurementSetId", None)
        as_found_adjustment_threshold = d.pop("AsFoundAdjustmentThreshold", None)
        as_found_decimal_places = d.pop("AsFoundDecimalPlaces", None)
        as_found_mean_extended = d.pop("AsFoundMeanExtended", None)
        as_found_sd_extended = d.pop("AsFoundSdExtended", None)
        as_found_range_extended = d.pop("AsFoundRangeExtended", None)
        as_found_delta_extended = d.pop("AsFoundDeltaExtended", None)
        as_found_cv_extended = d.pop("AsFoundCvExtended", None)
        as_found_nominal_extended = d.pop("AsFoundNominalExtended", None)
        as_found_min_max_header = d.pop("AsFoundMinMaxHeader", None)
        as_found_accuracy_class = d.pop("AsFoundAccuracyClass", None)
        as_found_accuracy_class_min = d.pop("AsFoundAccuracyClassMin", None)
        as_found_accuracy_class_max = d.pop("AsFoundAccuracyClassMax", None)
        as_found_minimum_measured_value = d.pop("AsFoundMinimumMeasuredValue", None)
        as_found_maxi_mum_measured_value = d.pop("AsFoundMaxiMumMeasuredValue", None)
        as_found_min_max_value_extended = d.pop("AsFoundMinMaxValueExtended", None)
        as_found_tool_range_name = d.pop("AsFoundToolRangeName", None)
        as_found_tool_range_uncertainty = d.pop("AsFoundToolRangeUncertainty", None)

        def _parse_as_found_primary_tool_last_service_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_found_primary_tool_last_service_date_type_0 = isoparse(data)
                return as_found_primary_tool_last_service_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        as_found_primary_tool_last_service_date = _parse_as_found_primary_tool_last_service_date(
            d.pop("AsFoundPrimaryToolLastServiceDate", None)
        )

        def _parse_as_found_primary_tool_next_service_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_found_primary_tool_next_service_date_type_0 = isoparse(data)
                return as_found_primary_tool_next_service_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        as_found_primary_tool_next_service_date = _parse_as_found_primary_tool_next_service_date(
            d.pop("AsFoundPrimaryToolNextServiceDate", None)
        )
        as_found_primary_tool_calibrated_by = d.pop("AsFoundPrimaryToolCalibratedBy", None)
        as_found_primary_tool_tool_name = d.pop("AsFoundPrimaryToolToolName", None)
        as_found_primary_tool_tool_description = d.pop("AsFoundPrimaryToolToolDescription", None)
        as_found_primary_tool_tool_type_name = d.pop("AsFoundPrimaryToolToolTypeName", None)
        as_found_primary_tool_manufacturer = d.pop("AsFoundPrimaryToolManufacturer", None)
        as_found_primary_tool_manufacturer_part_number = d.pop(
            "AsFoundPrimaryToolManufacturerPartNumber", None
        )
        as_found_primary_tool_serial_number = d.pop("AsFoundPrimaryToolSerialNumber", None)

        def _parse_as_left_secondary_tool_last_service_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_left_secondary_tool_last_service_date_type_0 = isoparse(data)
                return as_left_secondary_tool_last_service_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        as_left_secondary_tool_last_service_date = _parse_as_left_secondary_tool_last_service_date(
            d.pop("AsLeftSecondaryToolLastServiceDate", None)
        )

        def _parse_as_left_secondary_tool_next_service_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_left_secondary_tool_next_service_date_type_0 = isoparse(data)
                return as_left_secondary_tool_next_service_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        as_left_secondary_tool_next_service_date = _parse_as_left_secondary_tool_next_service_date(
            d.pop("AsLeftSecondaryToolNextServiceDate", None)
        )
        as_left_secondary_tool_calibrated_by = d.pop("AsLeftSecondaryToolCalibratedBy", None)
        as_left_secondary_tool_tool_name = d.pop("AsLeftSecondaryToolToolName", None)
        as_left_secondary_tool_tool_description = d.pop("AsLeftSecondaryToolToolDescription", None)
        as_left_secondary_tool_tool_type_name = d.pop("AsLeftSecondaryToolToolTypeName", None)
        as_left_secondary_tool_manufacturer = d.pop("AsLeftSecondaryToolManufacturer", None)
        as_left_secondary_tool_manufacturer_part_number = d.pop(
            "AsLeftSecondaryToolManufacturerPartNumber", None
        )
        as_left_secondary_tool_serial_number = d.pop("AsLeftSecondaryToolSerialNumber", None)

        def _parse_as_found_secondary_tool_last_service_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_found_secondary_tool_last_service_date_type_0 = isoparse(data)
                return as_found_secondary_tool_last_service_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        as_found_secondary_tool_last_service_date = (
            _parse_as_found_secondary_tool_last_service_date(
                d.pop("AsFoundSecondaryToolLastServiceDate", None)
            )
        )

        def _parse_as_found_secondary_tool_next_service_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_found_secondary_tool_next_service_date_type_0 = isoparse(data)
                return as_found_secondary_tool_next_service_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        as_found_secondary_tool_next_service_date = (
            _parse_as_found_secondary_tool_next_service_date(
                d.pop("AsFoundSecondaryToolNextServiceDate", None)
            )
        )
        as_found_secondary_tool_calibrated_by = d.pop("AsFoundSecondaryToolCalibratedBy", None)
        as_found_secondary_tool_tool_name = d.pop("AsFoundSecondaryToolToolName", None)
        as_found_secondary_tool_tool_description = d.pop(
            "AsFoundSecondaryToolToolDescription", None
        )
        as_found_secondary_tool_tool_type_name = d.pop("AsFoundSecondaryToolToolTypeName", None)
        as_found_secondary_tool_manufacturer = d.pop("AsFoundSecondaryToolManufacturer", None)
        as_found_secondary_tool_manufacturer_part_number = d.pop(
            "AsFoundSecondaryToolManufacturerPartNumber", None
        )
        as_found_secondary_tool_serial_number = d.pop("AsFoundSecondaryToolSerialNumber", None)
        _as_found_measurement_not_taken_result = d.pop("AsFoundMeasurementNotTakenResult", None)
        as_found_measurement_not_taken_result: Optional[
            ReportDatasetsToMeasurementAllResponseAsFoundMeasurementNotTakenResult
        ]
        if not _as_found_measurement_not_taken_result:
            as_found_measurement_not_taken_result = None
        elif _as_found_measurement_not_taken_result is None:
            as_found_measurement_not_taken_result = None
        else:
            as_found_measurement_not_taken_result = ReportDatasetsToMeasurementAllResponseAsFoundMeasurementNotTakenResult(  # noqa: E501
                _as_found_measurement_not_taken_result
            )
        as_found_hide_from_certificate = d.pop("AsFoundHideFromCertificate", None)
        as_found_measurement_not_taken_reason = d.pop("AsFoundMeasurementNotTakenReason", None)
        as_left_values = d.pop("AsLeftValues", None)
        as_left_is_accredited = d.pop("AsLeftIsAccredited", None)
        as_left_is_range_accredited = d.pop("AsLeftIsRangeAccredited", None)
        as_found_values = d.pop("AsFoundValues", None)
        as_found_is_accredited = d.pop("AsFoundIsAccredited", None)
        as_found_is_range_accredited = d.pop("AsFoundIsRangeAccredited", None)
        as_found_parameter_id = d.pop("AsFoundParameterId", None)
        as_found_sd_header = d.pop("AsFoundSdHeader", None)
        as_found_cv_header = d.pop("AsFoundCvHeader", None)
        _as_found_measurement_local_time = d.pop("AsFoundMeasurementLocalTime", None)
        as_found_measurement_local_time: Optional[datetime.datetime]
        if not _as_found_measurement_local_time:
            as_found_measurement_local_time = None
        else:
            as_found_measurement_local_time = isoparse(_as_found_measurement_local_time)
        as_found_tur = d.pop("AsFoundTur", None)
        as_found_tur_raw = d.pop("AsFoundTurRaw", None)
        as_left_tur = d.pop("AsLeftTur", None)
        as_left_tur_raw = d.pop("AsLeftTurRaw", None)
        as_found_tar = d.pop("AsFoundTar", None)
        as_found_tar_raw = d.pop("AsFoundTarRaw", None)
        as_left_tar = d.pop("AsLeftTar", None)
        as_left_tar_raw = d.pop("AsLeftTarRaw", None)
        as_found_guard_band = d.pop("AsFoundGuardBand", None)
        as_left_guard_band = d.pop("AsLeftGuardBand", None)
        _as_found_guard_band_logic = d.pop("AsFoundGuardBandLogic", None)
        _as_left_guard_band_logic = d.pop("AsLeftGuardBandLogic", None)
        as_found_guard_band_logic: Optional[
            ReportDatasetsToMeasurementAllResponseAsFoundGuardBandLogic
        ]
        if not _as_found_guard_band_logic:
            as_found_guard_band_logic = None
        elif _as_found_guard_band_logic is None:
            as_found_guard_band_logic = None
        else:
            as_found_guard_band_logic = ReportDatasetsToMeasurementAllResponseAsFoundGuardBandLogic(
                _as_found_guard_band_logic
            )
        as_left_guard_band_logic: Optional[
            ReportDatasetsToMeasurementAllResponseAsLeftGuardBandLogic
        ]
        if not _as_left_guard_band_logic:
            as_left_guard_band_logic = None
        elif _as_left_guard_band_logic is None:
            as_left_guard_band_logic = None
        else:
            as_left_guard_band_logic = ReportDatasetsToMeasurementAllResponseAsLeftGuardBandLogic(
                _as_left_guard_band_logic
            )

        as_found_error = d.pop("AsFoundError", None)
        as_found_error_extended = d.pop("AsFoundErrorExtended", None)
        as_left_error = d.pop("AsLeftError", None)
        as_left_error_extended = d.pop("AsLeftErrorExtended", None)
        as_found_percent_of_tolerance = d.pop("AsFoundPercentOfTolerance", None)
        as_found_percent_of_tolerance_extended = d.pop("AsFoundPercentOfToleranceExtended", None)
        as_left_percent_of_tolerance = d.pop("AsLeftPercentOfTolerance", None)
        as_left_percent_of_tolerance_extended = d.pop("AsLeftPercentOfToleranceExtended", None)
        as_found_tolerance_maximum = d.pop("AsFoundToleranceMaximum", None)
        as_found_tolerance_minimum = d.pop("AsFoundToleranceMinimum", None)
        as_found_tolerance_type = d.pop("AsFoundToleranceType", None)
        as_found_tolerance_mode = d.pop("AsFoundToleranceMode", None)
        as_found_tolerance_string = d.pop("AsFoundToleranceString", None)
        as_left_tolerance_maximum = d.pop("AsLeftToleranceMaximum", None)
        as_left_tolerance_minimum = d.pop("AsLeftToleranceMinimum", None)
        as_left_tolerance_type = d.pop("AsLeftToleranceType", None)
        as_left_tolerance_mode = d.pop("AsLeftToleranceMode", None)
        as_left_tolerance_string = d.pop("AsLeftToleranceString", None)
        as_found_max_hysteresis = d.pop("AsFoundMaxHysteresis", None)
        as_found_run = d.pop("AsFoundRun", None)
        as_found_direction = d.pop("AsFoundDirection", None)
        as_found_hysteresis = d.pop("AsFoundHysteresis", None)
        as_left_max_hysteresis = d.pop("AsLeftMaxHysteresis", None)
        as_left_run = d.pop("AsLeftRun", None)
        as_left_direction = d.pop("AsLeftDirection", None)
        as_left_hysteresis = d.pop("AsLeftHysteresis", None)
        _as_found_reading_entry_math = d.pop("AsFoundReadingEntryMath", None)
        as_found_reading_entry_math: Optional[
            ReportDatasetsToMeasurementAllResponseAsFoundReadingEntryMath
        ]
        if not _as_found_reading_entry_math:
            as_found_reading_entry_math = None
        elif _as_found_reading_entry_math is None:
            as_found_reading_entry_math = None
        else:
            # Handle integer to string mapping
            if isinstance(_as_found_reading_entry_math, int):
                as_found_reading_entry_math_map = {
                    0: "Addition",
                    1: "Average",
                    2: "Difference",
                    3: "Division",
                    4: "Maximum",
                    5: "Minimum",
                    6: "Multiplication",
                    7: "ReverseSubtraction",
                    8: "Subtraction",
                }
                _as_found_reading_entry_math = as_found_reading_entry_math_map.get(
                    _as_found_reading_entry_math, _as_found_reading_entry_math
                )
            as_found_reading_entry_math = (
                ReportDatasetsToMeasurementAllResponseAsFoundReadingEntryMath(
                    _as_found_reading_entry_math
                )
            )
        as_found_reading_entry_math_string = d.pop("AsFoundReadingEntryMathString", None)
        as_found_value_1 = d.pop("AsFoundValue1", None)
        as_found_value_2 = d.pop("AsFoundValue2", None)
        as_found_value_3 = d.pop("AsFoundValue3", None)
        as_found_value_4 = d.pop("AsFoundValue4", None)
        as_found_value_5 = d.pop("AsFoundValue5", None)
        as_found_value_6 = d.pop("AsFoundValue6", None)
        as_found_value_7 = d.pop("AsFoundValue7", None)
        as_found_value_8 = d.pop("AsFoundValue8", None)
        as_found_value_9 = d.pop("AsFoundValue9", None)
        as_found_value_10 = d.pop("AsFoundValue10", None)
        as_found_value_11 = d.pop("AsFoundValue11", None)
        as_found_value_12 = d.pop("AsFoundValue12", None)
        as_found_value_13 = d.pop("AsFoundValue13", None)
        as_found_value_14 = d.pop("AsFoundValue14", None)
        as_found_value_15 = d.pop("AsFoundValue15", None)
        as_found_value_16 = d.pop("AsFoundValue16", None)
        as_found_value_17 = d.pop("AsFoundValue17", None)
        as_found_value_18 = d.pop("AsFoundValue18", None)
        as_found_value_19 = d.pop("AsFoundValue19", None)
        as_found_value_20 = d.pop("AsFoundValue20", None)
        as_found_value_21 = d.pop("AsFoundValue21", None)
        as_found_value_22 = d.pop("AsFoundValue22", None)
        as_found_value_23 = d.pop("AsFoundValue23", None)
        as_found_value_24 = d.pop("AsFoundValue24", None)
        as_found_value_25 = d.pop("AsFoundValue25", None)
        as_found_value_26 = d.pop("AsFoundValue26", None)
        as_found_value_27 = d.pop("AsFoundValue27", None)
        as_found_value_28 = d.pop("AsFoundValue28", None)
        as_found_value_29 = d.pop("AsFoundValue29", None)
        as_found_value_30 = d.pop("AsFoundValue30", None)
        as_found_value_31 = d.pop("AsFoundValue31", None)
        as_found_value_32 = d.pop("AsFoundValue32", None)
        as_found_value_33 = d.pop("AsFoundValue33", None)
        as_found_value_34 = d.pop("AsFoundValue34", None)
        as_found_value_35 = d.pop("AsFoundValue35", None)
        as_found_value_36 = d.pop("AsFoundValue36", None)
        as_found_value_37 = d.pop("AsFoundValue37", None)
        as_found_value_38 = d.pop("AsFoundValue38", None)
        as_found_value_39 = d.pop("AsFoundValue39", None)
        as_found_value_40 = d.pop("AsFoundValue40", None)
        as_found_raw_value_1 = d.pop("AsFoundRawValue1", None)
        as_found_raw_value_2 = d.pop("AsFoundRawValue2", None)
        as_found_raw_value_3 = d.pop("AsFoundRawValue3", None)
        as_found_raw_value_4 = d.pop("AsFoundRawValue4", None)
        as_found_raw_value_5 = d.pop("AsFoundRawValue5", None)
        as_found_raw_value_6 = d.pop("AsFoundRawValue6", None)
        as_found_raw_value_7 = d.pop("AsFoundRawValue7", None)
        as_found_raw_value_8 = d.pop("AsFoundRawValue8", None)
        as_found_raw_value_9 = d.pop("AsFoundRawValue9", None)
        as_found_raw_value_10 = d.pop("AsFoundRawValue10", None)
        as_found_raw_value_11 = d.pop("AsFoundRawValue11", None)
        as_found_raw_value_12 = d.pop("AsFoundRawValue12", None)
        as_found_raw_value_13 = d.pop("AsFoundRawValue13", None)
        as_found_raw_value_14 = d.pop("AsFoundRawValue14", None)
        as_found_raw_value_15 = d.pop("AsFoundRawValue15", None)
        as_found_raw_value_16 = d.pop("AsFoundRawValue16", None)
        as_found_raw_value_17 = d.pop("AsFoundRawValue17", None)
        as_found_raw_value_18 = d.pop("AsFoundRawValue18", None)
        as_found_raw_value_19 = d.pop("AsFoundRawValue19", None)
        as_found_raw_value_20 = d.pop("AsFoundRawValue20", None)
        as_found_raw_value_21 = d.pop("AsFoundRawValue21", None)
        as_found_raw_value_22 = d.pop("AsFoundRawValue22", None)
        as_found_raw_value_23 = d.pop("AsFoundRawValue23", None)
        as_found_raw_value_24 = d.pop("AsFoundRawValue24", None)
        as_found_raw_value_25 = d.pop("AsFoundRawValue25", None)
        as_found_raw_value_26 = d.pop("AsFoundRawValue26", None)
        as_found_raw_value_27 = d.pop("AsFoundRawValue27", None)
        as_found_raw_value_28 = d.pop("AsFoundRawValue28", None)
        as_found_raw_value_29 = d.pop("AsFoundRawValue29", None)
        as_found_raw_value_30 = d.pop("AsFoundRawValue30", None)
        as_found_raw_value_31 = d.pop("AsFoundRawValue31", None)
        as_found_raw_value_32 = d.pop("AsFoundRawValue32", None)
        as_found_raw_value_33 = d.pop("AsFoundRawValue33", None)
        as_found_raw_value_34 = d.pop("AsFoundRawValue34", None)
        as_found_raw_value_35 = d.pop("AsFoundRawValue35", None)
        as_found_raw_value_36 = d.pop("AsFoundRawValue36", None)
        as_found_raw_value_37 = d.pop("AsFoundRawValue37", None)
        as_found_raw_value_38 = d.pop("AsFoundRawValue38", None)
        as_found_raw_value_39 = d.pop("AsFoundRawValue39", None)
        as_found_raw_value_40 = d.pop("AsFoundRawValue40", None)
        as_found_value_subtitle_1 = d.pop("AsFoundValueSubtitle1", None)
        as_found_value_subtitle_2 = d.pop("AsFoundValueSubtitle2", None)
        as_found_value_subtitle_3 = d.pop("AsFoundValueSubtitle3", None)
        as_found_value_subtitle_4 = d.pop("AsFoundValueSubtitle4", None)
        as_found_value_subtitle_5 = d.pop("AsFoundValueSubtitle5", None)
        as_found_value_subtitle_6 = d.pop("AsFoundValueSubtitle6", None)
        as_found_value_subtitle_7 = d.pop("AsFoundValueSubtitle7", None)
        as_found_value_subtitle_8 = d.pop("AsFoundValueSubtitle8", None)
        as_found_value_subtitle_9 = d.pop("AsFoundValueSubtitle9", None)
        as_found_value_subtitle_10 = d.pop("AsFoundValueSubtitle10", None)
        as_found_value_subtitle_11 = d.pop("AsFoundValueSubtitle11", None)
        as_found_value_subtitle_12 = d.pop("AsFoundValueSubtitle12", None)
        as_found_value_subtitle_13 = d.pop("AsFoundValueSubtitle13", None)
        as_found_value_subtitle_14 = d.pop("AsFoundValueSubtitle14", None)
        as_found_value_subtitle_15 = d.pop("AsFoundValueSubtitle15", None)
        as_found_value_subtitle_16 = d.pop("AsFoundValueSubtitle16", None)
        as_found_value_subtitle_17 = d.pop("AsFoundValueSubtitle17", None)
        as_found_value_subtitle_18 = d.pop("AsFoundValueSubtitle18", None)
        as_found_value_subtitle_19 = d.pop("AsFoundValueSubtitle19", None)
        as_found_value_subtitle_20 = d.pop("AsFoundValueSubtitle20", None)
        as_found_value_subtitle_21 = d.pop("AsFoundValueSubtitle21", None)
        as_found_value_subtitle_22 = d.pop("AsFoundValueSubtitle22", None)
        as_found_value_subtitle_23 = d.pop("AsFoundValueSubtitle23", None)
        as_found_value_subtitle_24 = d.pop("AsFoundValueSubtitle24", None)
        as_found_value_subtitle_25 = d.pop("AsFoundValueSubtitle25", None)
        as_found_value_subtitle_26 = d.pop("AsFoundValueSubtitle26", None)
        as_found_value_subtitle_27 = d.pop("AsFoundValueSubtitle27", None)
        as_found_value_subtitle_28 = d.pop("AsFoundValueSubtitle28", None)
        as_found_value_subtitle_29 = d.pop("AsFoundValueSubtitle29", None)
        as_found_value_subtitle_30 = d.pop("AsFoundValueSubtitle30", None)
        as_found_value_subtitle_31 = d.pop("AsFoundValueSubtitle31", None)
        as_found_value_subtitle_32 = d.pop("AsFoundValueSubtitle32", None)
        as_found_value_subtitle_33 = d.pop("AsFoundValueSubtitle33", None)
        as_found_value_subtitle_34 = d.pop("AsFoundValueSubtitle34", None)
        as_found_value_subtitle_35 = d.pop("AsFoundValueSubtitle35", None)
        as_found_value_subtitle_36 = d.pop("AsFoundValueSubtitle36", None)
        as_found_value_subtitle_37 = d.pop("AsFoundValueSubtitle37", None)
        as_found_value_subtitle_38 = d.pop("AsFoundValueSubtitle38", None)
        as_found_value_subtitle_39 = d.pop("AsFoundValueSubtitle39", None)
        as_found_value_subtitle_40 = d.pop("AsFoundValueSubtitle40", None)
        as_found_mean = d.pop("AsFoundMean", None)
        as_found_mean_raw = d.pop("AsFoundMeanRaw", None)
        as_found_sd = d.pop("AsFoundSd", None)
        as_found_sd_raw = d.pop("AsFoundSdRaw", None)
        as_found_delta = d.pop("AsFoundDelta", None)
        as_found_range = d.pop("AsFoundRange", None)
        as_found_cv = d.pop("AsFoundCv", None)
        as_found_cv_raw = d.pop("AsFoundCvRaw", None)
        as_found_result = d.pop("AsFoundResult", None)
        as_found_range_result = d.pop("AsFoundRangeResult", None)
        as_found_delta_result = d.pop("AsFoundDeltaResult", None)
        as_found_min_result = d.pop("AsFoundMinResult", None)
        as_found_max_result = d.pop("AsFoundMaxResult", None)
        as_found_tar_result = d.pop("AsFoundTarResult", None)
        as_found_tur_result = d.pop("AsFoundTurResult", None)
        as_found_error_result = d.pop("AsFoundErrorResult", None)
        as_found_sd_result = d.pop("AsFoundSdResult", None)
        as_found_cv_result = d.pop("AsFoundCvResult", None)
        as_found_custom_field_result = d.pop("AsFoundCustomFieldResult", None)
        as_found_mu = d.pop("AsFoundMu", None)
        as_found_mu_raw = d.pop("AsFoundMuRaw", None)
        as_found_mu_effective_dof = d.pop("AsFoundMuEffectiveDOF", None)
        as_found_mu_coverage_factor = d.pop("AsFoundMUCoverageFactor", None)
        as_found_cmc = d.pop("AsFoundCmc", None)
        as_found_cmc_comments = d.pop("AsFoundCmcComments", None)
        as_found_calculated_uncertainty = d.pop("AsFoundCalculatedUncertainty", None)
        as_found_lab_mu = d.pop("AsFoundLabMu", None)
        as_found_uncertainty_budget = d.pop("AsFoundUncertaintyBudget", None)
        as_found_mu_extended = d.pop("AsFoundMuExtended", None)
        as_found_channel = d.pop("AsFoundChannel", None)
        _as_found_measurement_type = d.pop("AsFoundMeasurementType", None)
        as_found_measurement_type: Optional[
            ReportDatasetsToMeasurementAllResponseAsFoundMeasurementType
        ]
        if not _as_found_measurement_type:
            as_found_measurement_type = None
        elif _as_found_measurement_type is None:
            as_found_measurement_type = None
        else:
            # Handle both integer and string values for AsFoundMeasurementType
            if isinstance(_as_found_measurement_type, int):
                # Map integer values to string values
                measurement_type_mapping = {
                    0: "Data",
                    1: "Cumulative",
                }
                string_value = measurement_type_mapping.get(_as_found_measurement_type)
                if string_value:
                    as_found_measurement_type = (
                        ReportDatasetsToMeasurementAllResponseAsFoundMeasurementType(string_value)
                    )
                else:
                    # Unknown integer value, set to None
                    as_found_measurement_type = None
            else:
                # Handle string values normally
                as_found_measurement_type = (
                    ReportDatasetsToMeasurementAllResponseAsFoundMeasurementType(
                        _as_found_measurement_type
                    )
                )
        as_found_updated_by = d.pop("AsFoundUpdatedBy", None)
        _as_found_updated_on = d.pop("AsFoundUpdatedOn", None)
        as_found_updated_on: Optional[datetime.datetime]
        if not _as_found_updated_on:
            as_found_updated_on = None
        elif _as_found_updated_on is None:
            as_found_updated_on = None
        else:
            as_found_updated_on = isoparse(_as_found_updated_on)
        as_left_abbreviated_uom = d.pop("AsLeftAbbreviatedUOM", None)
        as_left_unit_scale_factor = d.pop("AsLeftUnitScaleFactor", None)
        as_found_specification_title = d.pop("AsFoundSpecificationTitle", None)
        as_found_specification_subtitle = d.pop("AsFoundSpecificationSubtitle", None)
        as_found_specification_group = d.pop("AsFoundSpecificationGroup", None)
        as_found_batch_type = d.pop("AsFoundBatchType", None)
        as_found_batch_result = d.pop("AsFoundBatchResult", None)
        as_found_is_by_channel = d.pop("AsFoundIsByChannel", None)
        as_found_channel_count = d.pop("AsFoundChannelCount", None)
        _as_found_commenced_on = d.pop("AsFoundCommencedOn", None)
        as_found_commenced_on: Optional[datetime.datetime]
        if not _as_found_commenced_on:
            as_found_commenced_on = None
        elif _as_found_commenced_on is None:
            as_found_commenced_on = None
        else:
            as_found_commenced_on = isoparse(_as_found_commenced_on)
        as_found_commenced_by = d.pop("AsFoundCommencedBy", None)
        as_found_z_factor = d.pop("AsFoundZFactor", None)
        as_found_air_buoyancy = d.pop("AsFoundAirBuoyancy", None)
        as_found_evaporation_rate = d.pop("AsFoundEvaporationRate", None)
        as_found_ambient_temperature = d.pop("AsFoundAmbientTemperature", None)
        as_found_air_humidity = d.pop("AsFoundAirHumidity", None)
        as_found_barometric_pressure = d.pop("AsFoundBarometricPressure", None)
        as_found_altitude = d.pop("AsFoundAltitude", None)
        as_found_wind_speed = d.pop("AsFoundWindSpeed", None)
        as_found_solar_radiation = d.pop("AsFoundSolarRadiation", None)
        as_found_light_intensity = d.pop("AsFoundLightIntensity", None)
        as_found_noise_level = d.pop("AsFoundNoiseLevel", None)
        as_found_ph_level = d.pop("AsFoundPhLevel", None)
        as_found_water_conductivity = d.pop("AsFoundWaterConductivity", None)
        as_found_water_temperature = d.pop("AsFoundWaterTemperature", None)
        as_found_z_factor_uom = d.pop("AsFoundZFactorUom", None)
        as_found_air_buoyancy_uom = d.pop("AsFoundAirBuoyancyUom", None)
        as_found_evaporation_rate_uom = d.pop("AsFoundEvaporationRateUom", None)
        as_found_ambient_temperature_uom = d.pop("AsFoundAmbientTemperatureUom", None)
        as_found_air_humidity_uom = d.pop("AsFoundAirHumidityUom", None)
        as_found_barometric_pressure_uom = d.pop("AsFoundBarometricPressureUom", None)
        as_found_altitude_uom = d.pop("AsFoundAltitudeUom", None)
        as_found_wind_speed_uom = d.pop("AsFoundWindSpeedUom", None)
        as_found_solar_radiation_uom = d.pop("AsFoundSolarRadiationUom", None)
        as_found_light_intensity_uom = d.pop("AsFoundLightIntensityUom", None)
        as_found_noise_level_uom = d.pop("AsFoundNoiseLevelUom", None)
        as_found_ph_level_uom = d.pop("AsFoundPhLevelUom", None)
        as_found_water_conductivity_uom = d.pop("AsFoundWaterConductivityUom", None)
        as_found_water_temperature_uom = d.pop("AsFoundWaterTemperatureUom", None)
        as_found_abbreviated_uom = d.pop("AsFoundAbbreviatedUOM", None)
        as_found_unit_scale_factor = d.pop("AsFoundUnitScaleFactor", None)
        as_found_specification_name = d.pop("AsFoundSpecificationName", None)
        as_found_parameter_name = d.pop("AsFoundParameterName", None)
        as_found_display_order = d.pop("AsFoundDisplayOrder", None)
        as_found_unit_of_measure = d.pop("AsFoundUnitOfMeasure", None)
        as_found_display_format = d.pop("AsFoundDisplayFormat", None)
        as_found_precision = d.pop("AsFoundPrecision", None)
        _as_found_precision_type = d.pop("AsFoundPrecisionType", None)
        as_found_precision_type: Optional[
            ReportDatasetsToMeasurementAllResponseAsFoundPrecisionType
        ]
        if not _as_found_precision_type:
            as_found_precision_type = None
        elif _as_found_precision_type is None:
            as_found_precision_type = None
        else:
            # Handle integer to string mapping OR string to valid enum mapping
            if isinstance(_as_found_precision_type, int):
                as_found_precision_type_map = {
                    0: "Percentage",
                    1: "Readability",
                    2: "UnitOfMeasure",
                }
                _as_found_precision_type = as_found_precision_type_map.get(
                    _as_found_precision_type, _as_found_precision_type
                )
            elif isinstance(_as_found_precision_type, str):
                # Handle string to valid enum mapping
                string_precision_type_map = {
                    "Standard": "UnitOfMeasure",
                    "Enhanced": "Readability",
                    "HighPrecision": "Percentage",
                }
                _as_found_precision_type = string_precision_type_map.get(
                    _as_found_precision_type, _as_found_precision_type
                )
            as_found_precision_type = ReportDatasetsToMeasurementAllResponseAsFoundPrecisionType(
                _as_found_precision_type
            )
        as_found_minimum = d.pop("AsFoundMinimum", None)
        as_found_nominal = d.pop("AsFoundNominal", None)
        as_found_expected_value = d.pop("AsFoundExpectedValue", None)
        as_found_expected_value_raw = d.pop("AsFoundExpectedValueRaw", None)
        as_found_test_value = d.pop("AsFoundTestValue", None)
        as_found_base_value = d.pop("AsFoundBaseValue", None)
        as_found_maxi_mum = d.pop("AsFoundMaxiMum", None)
        as_found_resolution = d.pop("AsFoundResolution", None)
        as_found_resolution_count = d.pop("AsFoundResolutionCount", None)
        as_found_measurement_batch_id = d.pop("AsFoundMeasurementBatchId", None)
        as_found_measurement_id = d.pop("AsFoundMeasurementId", None)
        as_found_standard_id = d.pop("AsFoundStandardId", None)
        as_found_tool_id = d.pop("AsFoundToolId", None)
        as_found_measurement_condition_id = d.pop("AsFoundMeasurementConditionId", None)
        as_found_measurement_point_id = d.pop("AsFoundMeasurementPointId", None)
        as_left_parameter_id = d.pop("AsLeftParameterId", None)
        as_left_sd_header = d.pop("AsLeftSdHeader", None)
        as_left_cv_header = d.pop("AsLeftCvHeader", None)
        _as_left_measurement_local_time = d.pop("AsLeftMeasurementLocalTime", None)
        as_left_measurement_local_time: Optional[datetime.datetime]
        if not _as_left_measurement_local_time:
            as_left_measurement_local_time = None
        else:
            as_left_measurement_local_time = isoparse(_as_left_measurement_local_time)
        _as_left_reading_entry_math = d.pop("AsLeftReadingEntryMath", None)
        as_left_reading_entry_math: Optional[
            ReportDatasetsToMeasurementAllResponseAsLeftReadingEntryMath
        ]
        if not _as_left_reading_entry_math:
            as_left_reading_entry_math = None
        elif _as_left_reading_entry_math is None:
            as_left_reading_entry_math = None
        else:
            # Handle integer to string mapping
            if isinstance(_as_left_reading_entry_math, int):
                as_left_reading_entry_math_map = {
                    0: "Addition",
                    1: "Average",
                    2: "Difference",
                    3: "Division",
                    4: "Maximum",
                    5: "Minimum",
                    6: "Multiplication",
                    7: "ReverseSubtraction",
                    8: "Subtraction",
                }
                _as_left_reading_entry_math = as_left_reading_entry_math_map.get(
                    _as_left_reading_entry_math, _as_left_reading_entry_math
                )
            as_left_reading_entry_math = (
                ReportDatasetsToMeasurementAllResponseAsLeftReadingEntryMath(
                    _as_left_reading_entry_math
                )
            )
        as_left_reading_entry_math_string = d.pop("AsLeftReadingEntryMathString", None)
        as_left_value_1 = d.pop("AsLeftValue1", None)
        as_left_value_2 = d.pop("AsLeftValue2", None)
        as_left_value_3 = d.pop("AsLeftValue3", None)
        as_left_value_4 = d.pop("AsLeftValue4", None)
        as_left_value_5 = d.pop("AsLeftValue5", None)
        as_left_value_6 = d.pop("AsLeftValue6", None)
        as_left_value_7 = d.pop("AsLeftValue7", None)
        as_left_value_8 = d.pop("AsLeftValue8", None)
        as_left_value_9 = d.pop("AsLeftValue9", None)
        as_left_value_10 = d.pop("AsLeftValue10", None)
        as_left_value_11 = d.pop("AsLeftValue11", None)
        as_left_value_12 = d.pop("AsLeftValue12", None)
        as_left_value_13 = d.pop("AsLeftValue13", None)
        as_left_value_14 = d.pop("AsLeftValue14", None)
        as_left_value_15 = d.pop("AsLeftValue15", None)
        as_left_value_16 = d.pop("AsLeftValue16", None)
        as_left_value_17 = d.pop("AsLeftValue17", None)
        as_left_value_18 = d.pop("AsLeftValue18", None)
        as_left_value_19 = d.pop("AsLeftValue19", None)
        as_left_value_20 = d.pop("AsLeftValue20", None)
        as_left_value_21 = d.pop("AsLeftValue21", None)
        as_left_value_22 = d.pop("AsLeftValue22", None)
        as_left_value_23 = d.pop("AsLeftValue23", None)
        as_left_value_24 = d.pop("AsLeftValue24", None)
        as_left_value_25 = d.pop("AsLeftValue25", None)
        as_left_value_26 = d.pop("AsLeftValue26", None)
        as_left_value_27 = d.pop("AsLeftValue27", None)
        as_left_value_28 = d.pop("AsLeftValue28", None)
        as_left_value_29 = d.pop("AsLeftValue29", None)
        as_left_value_30 = d.pop("AsLeftValue30", None)
        as_left_value_31 = d.pop("AsLeftValue31", None)
        as_left_value_32 = d.pop("AsLeftValue32", None)
        as_left_value_33 = d.pop("AsLeftValue33", None)
        as_left_value_34 = d.pop("AsLeftValue34", None)
        as_left_value_35 = d.pop("AsLeftValue35", None)
        as_left_value_36 = d.pop("AsLeftValue36", None)
        as_left_value_37 = d.pop("AsLeftValue37", None)
        as_left_value_38 = d.pop("AsLeftValue38", None)
        as_left_value_39 = d.pop("AsLeftValue39", None)
        as_left_value_40 = d.pop("AsLeftValue40", None)
        as_left_raw_value_1 = d.pop("AsLeftRawValue1", None)
        as_left_raw_value_2 = d.pop("AsLeftRawValue2", None)
        as_left_raw_value_3 = d.pop("AsLeftRawValue3", None)
        as_left_raw_value_4 = d.pop("AsLeftRawValue4", None)
        as_left_raw_value_5 = d.pop("AsLeftRawValue5", None)
        as_left_raw_value_6 = d.pop("AsLeftRawValue6", None)
        as_left_raw_value_7 = d.pop("AsLeftRawValue7", None)
        as_left_raw_value_8 = d.pop("AsLeftRawValue8", None)
        as_left_raw_value_9 = d.pop("AsLeftRawValue9", None)
        as_left_raw_value_10 = d.pop("AsLeftRawValue10", None)
        as_left_raw_value_11 = d.pop("AsLeftRawValue11", None)
        as_left_raw_value_12 = d.pop("AsLeftRawValue12", None)
        as_left_raw_value_13 = d.pop("AsLeftRawValue13", None)
        as_left_raw_value_14 = d.pop("AsLeftRawValue14", None)
        as_left_raw_value_15 = d.pop("AsLeftRawValue15", None)
        as_left_raw_value_16 = d.pop("AsLeftRawValue16", None)
        as_left_raw_value_17 = d.pop("AsLeftRawValue17", None)
        as_left_raw_value_18 = d.pop("AsLeftRawValue18", None)
        as_left_raw_value_19 = d.pop("AsLeftRawValue19", None)
        as_left_raw_value_20 = d.pop("AsLeftRawValue20", None)
        as_left_raw_value_21 = d.pop("AsLeftRawValue21", None)
        as_left_raw_value_22 = d.pop("AsLeftRawValue22", None)
        as_left_raw_value_23 = d.pop("AsLeftRawValue23", None)
        as_left_raw_value_24 = d.pop("AsLeftRawValue24", None)
        as_left_raw_value_25 = d.pop("AsLeftRawValue25", None)
        as_left_raw_value_26 = d.pop("AsLeftRawValue26", None)
        as_left_raw_value_27 = d.pop("AsLeftRawValue27", None)
        as_left_raw_value_28 = d.pop("AsLeftRawValue28", None)
        as_left_raw_value_29 = d.pop("AsLeftRawValue29", None)
        as_left_raw_value_30 = d.pop("AsLeftRawValue30", None)
        as_left_raw_value_31 = d.pop("AsLeftRawValue31", None)
        as_left_raw_value_32 = d.pop("AsLeftRawValue32", None)
        as_left_raw_value_33 = d.pop("AsLeftRawValue33", None)
        as_left_raw_value_34 = d.pop("AsLeftRawValue34", None)
        as_left_raw_value_35 = d.pop("AsLeftRawValue35", None)
        as_left_raw_value_36 = d.pop("AsLeftRawValue36", None)
        as_left_raw_value_37 = d.pop("AsLeftRawValue37", None)
        as_left_raw_value_38 = d.pop("AsLeftRawValue38", None)
        as_left_raw_value_39 = d.pop("AsLeftRawValue39", None)
        as_left_raw_value_40 = d.pop("AsLeftRawValue40", None)
        as_left_value_subtitle_1 = d.pop("AsLeftValueSubtitle1", None)
        as_left_value_subtitle_2 = d.pop("AsLeftValueSubtitle2", None)
        as_left_value_subtitle_3 = d.pop("AsLeftValueSubtitle3", None)
        as_left_value_subtitle_4 = d.pop("AsLeftValueSubtitle4", None)
        as_left_value_subtitle_5 = d.pop("AsLeftValueSubtitle5", None)
        as_left_value_subtitle_6 = d.pop("AsLeftValueSubtitle6", None)
        as_left_value_subtitle_7 = d.pop("AsLeftValueSubtitle7", None)
        as_left_value_subtitle_8 = d.pop("AsLeftValueSubtitle8", None)
        as_left_value_subtitle_9 = d.pop("AsLeftValueSubtitle9", None)
        as_left_value_subtitle_10 = d.pop("AsLeftValueSubtitle10", None)
        as_left_value_subtitle_11 = d.pop("AsLeftValueSubtitle11", None)
        as_left_value_subtitle_12 = d.pop("AsLeftValueSubtitle12", None)
        as_left_value_subtitle_13 = d.pop("AsLeftValueSubtitle13", None)
        as_left_value_subtitle_14 = d.pop("AsLeftValueSubtitle14", None)
        as_left_value_subtitle_15 = d.pop("AsLeftValueSubtitle15", None)
        as_left_value_subtitle_16 = d.pop("AsLeftValueSubtitle16", None)
        as_left_value_subtitle_17 = d.pop("AsLeftValueSubtitle17", None)
        as_left_value_subtitle_18 = d.pop("AsLeftValueSubtitle18", None)
        as_left_value_subtitle_19 = d.pop("AsLeftValueSubtitle19", None)
        as_left_value_subtitle_20 = d.pop("AsLeftValueSubtitle20", None)
        as_left_value_subtitle_21 = d.pop("AsLeftValueSubtitle21", None)
        as_left_value_subtitle_22 = d.pop("AsLeftValueSubtitle22", None)
        as_left_value_subtitle_23 = d.pop("AsLeftValueSubtitle23", None)
        as_left_value_subtitle_24 = d.pop("AsLeftValueSubtitle24", None)
        as_left_value_subtitle_25 = d.pop("AsLeftValueSubtitle25", None)
        as_left_value_subtitle_26 = d.pop("AsLeftValueSubtitle26", None)
        as_left_value_subtitle_27 = d.pop("AsLeftValueSubtitle27", None)
        as_left_value_subtitle_28 = d.pop("AsLeftValueSubtitle28", None)
        as_left_value_subtitle_29 = d.pop("AsLeftValueSubtitle29", None)
        as_left_value_subtitle_30 = d.pop("AsLeftValueSubtitle30", None)
        as_left_value_subtitle_31 = d.pop("AsLeftValueSubtitle31", None)
        as_left_value_subtitle_32 = d.pop("AsLeftValueSubtitle32", None)
        as_left_value_subtitle_33 = d.pop("AsLeftValueSubtitle33", None)
        as_left_value_subtitle_34 = d.pop("AsLeftValueSubtitle34", None)
        as_left_value_subtitle_35 = d.pop("AsLeftValueSubtitle35", None)
        as_left_value_subtitle_36 = d.pop("AsLeftValueSubtitle36", None)
        as_left_value_subtitle_37 = d.pop("AsLeftValueSubtitle37", None)
        as_left_value_subtitle_38 = d.pop("AsLeftValueSubtitle38", None)
        as_left_value_subtitle_39 = d.pop("AsLeftValueSubtitle39", None)
        as_left_value_subtitle_40 = d.pop("AsLeftValueSubtitle40", None)
        as_left_mean = d.pop("AsLeftMean", None)
        as_left_mean_raw = d.pop("AsLeftMeanRaw", None)
        as_left_sd = d.pop("AsLeftSd", None)
        as_left_sd_raw = d.pop("AsLeftSdRaw", None)
        as_left_cv = d.pop("AsLeftCv", None)
        as_left_cv_raw = d.pop("AsLeftCvRaw", None)
        as_left_delta = d.pop("AsLeftDelta", None)
        as_left_range = d.pop("AsLeftRange", None)

        def _parse_as_left_result(data: object) -> Optional[int]:
            if data is None:
                return data
            return cast(Optional[int], data)

        as_left_result = _parse_as_left_result(d.pop("AsLeftResult", None))
        as_left_range_result = d.pop("AsLeftRangeResult", None)
        as_left_delta_result = d.pop("AsLeftDeltaResult", None)
        as_left_min_result = d.pop("AsLeftMinResult", None)
        as_left_max_result = d.pop("AsLeftMaxResult", None)
        as_left_tar_result = d.pop("AsLeftTarResult", None)
        as_left_tur_result = d.pop("AsLeftTurResult", None)
        as_left_error_result = d.pop("AsLeftErrorResult", None)
        as_left_sd_result = d.pop("AsLeftSdResult", None)
        as_left_cv_result = d.pop("AsLeftCvResult", None)
        as_left_custom_field_result = d.pop("AsLeftCustomFieldResult", None)
        as_left_mu = d.pop("AsLeftMu", None)
        as_left_mu_raw = d.pop("AsLeftMuRaw", None)
        as_left_mu_effective_dof = d.pop("AsLeftMUEffectiveDOF", None)
        as_left_mu_coverage_factor = d.pop("AsLeftMUCoverageFactor", None)
        as_left_cmc = d.pop("AsLeftCmc", None)
        as_left_cmc_comments = d.pop("AsLeftCmcComments", None)
        as_left_calculated_uncertainty = d.pop("AsLeftCalculatedUncertainty", None)
        as_left_lab_mu = d.pop("AsLeftLabMu", None)
        as_left_uncertainty_budget = d.pop("AsLeftUncertaintyBudget", None)
        as_left_mu_extended = d.pop("AsLeftMuExtended", None)
        as_left_channel = d.pop("AsLeftChannel", None)
        _as_left_measurement_type = d.pop("AsLeftMeasurementType", None)
        as_left_measurement_type: Optional[
            ReportDatasetsToMeasurementAllResponseAsLeftMeasurementType
        ]
        if not _as_left_measurement_type:
            as_left_measurement_type = None
        elif _as_left_measurement_type is None:
            as_left_measurement_type = None
        else:
            # Handle both integer and string values for AsLeftMeasurementType
            if isinstance(_as_left_measurement_type, int):
                # Map integer values to string values
                measurement_type_mapping = {
                    0: "Data",
                    1: "Cumulative",
                }
                string_value = measurement_type_mapping.get(_as_left_measurement_type)
                if string_value:
                    as_left_measurement_type = (
                        ReportDatasetsToMeasurementAllResponseAsLeftMeasurementType(string_value)
                    )
                else:
                    # Unknown integer value, set to None
                    as_left_measurement_type = None
            else:
                # Handle string values normally
                as_left_measurement_type = (
                    ReportDatasetsToMeasurementAllResponseAsLeftMeasurementType(
                        _as_left_measurement_type
                    )
                )
        as_left_updated_by = d.pop("AsLeftUpdatedBy", None)
        _as_left_updated_on = d.pop("AsLeftUpdatedOn", None)
        as_left_updated_on: Optional[datetime.datetime]
        if not _as_left_updated_on:
            as_left_updated_on = None
        elif _as_left_updated_on is None:
            as_left_updated_on = None
        else:
            as_left_updated_on = isoparse(_as_left_updated_on)
        as_left_specification_title = d.pop("AsLeftSpecificationTitle", None)
        as_left_specification_subtitle = d.pop("AsLeftSpecificationSubtitle", None)
        as_left_specification_group = d.pop("AsLeftSpecificationGroup", None)
        as_left_batch_type = d.pop("AsLeftBatchType", None)
        as_left_batch_result = d.pop("AsLeftBatchResult", None)
        as_left_is_by_channel = d.pop("AsLeftIsByChannel", None)
        as_left_channel_count = d.pop("AsLeftChannelCount", None)
        _as_left_commenced_on = d.pop("AsLeftCommencedOn", None)
        as_left_commenced_on: Optional[datetime.datetime]
        if not _as_left_commenced_on:
            as_left_commenced_on = None
        elif _as_left_commenced_on is None:
            as_left_commenced_on = None
        else:
            as_left_commenced_on = isoparse(_as_left_commenced_on)
        as_left_commenced_by = d.pop("AsLeftCommencedBy", None)
        as_left_z_factor = d.pop("AsLeftZFactor", None)
        as_left_air_buoyancy = d.pop("AsLeftAirBuoyancy", None)
        as_left_evaporation_rate = d.pop("AsLeftEvaporationRate", None)
        as_left_ambient_temperature = d.pop("AsLeftAmbientTemperature", None)
        as_left_air_humidity = d.pop("AsLeftAirHumidity", None)
        as_left_barometric_pressure = d.pop("AsLeftBarometricPressure", None)
        as_left_altitude = d.pop("AsLeftAltitude", None)
        as_left_wind_speed = d.pop("AsLeftWindSpeed", None)
        as_left_solar_radiation = d.pop("AsLeftSolarRadiation", None)
        as_left_light_intensity = d.pop("AsLeftLightIntensity", None)
        as_left_noise_level = d.pop("AsLeftNoiseLevel", None)
        as_left_ph_level = d.pop("AsLeftPhLevel", None)
        as_left_water_conductivity = d.pop("AsLeftWaterConductivity", None)
        as_left_water_temperature = d.pop("AsLeftWaterTemperature", None)
        as_left_z_factor_uom = d.pop("AsLeftZFactorUom", None)
        as_left_air_buoyancy_uom = d.pop("AsLeftAirBuoyancyUom", None)
        as_left_evaporation_rate_uom = d.pop("AsLeftEvaporationRateUom", None)
        as_left_ambient_temperature_uom = d.pop("AsLeftAmbientTemperatureUom", None)
        as_left_air_humidity_uom = d.pop("AsLeftAirHumidityUom", None)
        as_left_barometric_pressure_uom = d.pop("AsLeftBarometricPressureUom", None)
        as_left_altitude_uom = d.pop("AsLeftAltitudeUom", None)
        as_left_wind_speed_uom = d.pop("AsLeftWindSpeedUom", None)
        as_left_solar_radiation_uom = d.pop("AsLeftSolarRadiationUom", None)
        as_left_light_intensity_uom = d.pop("AsLeftLightIntensityUom", None)
        as_left_noise_level_uom = d.pop("AsLeftNoiseLevelUom", None)
        as_left_ph_level_uom = d.pop("AsLeftPhLevelUom", None)
        as_left_water_conductivity_uom = d.pop("AsLeftWaterConductivityUom", None)
        as_left_water_temperature_uom = d.pop("AsLeftWaterTemperatureUom", None)
        as_left_specification_name = d.pop("AsLeftSpecificationName", None)
        as_left_parameter_name = d.pop("AsLeftParameterName", None)
        as_left_display_order = d.pop("AsLeftDisplayOrder", None)
        as_left_unit_of_measure = d.pop("AsLeftUnitOfMeasure", None)
        as_left_display_format = d.pop("AsLeftDisplayFormat", None)
        as_left_precision = d.pop("AsLeftPrecision", None)
        _as_left_precision_type = d.pop("AsLeftPrecisionType", None)
        as_left_precision_type: Optional[ReportDatasetsToMeasurementAllResponseAsLeftPrecisionType]
        if not _as_left_precision_type:
            as_left_precision_type = None
        elif _as_left_precision_type is None:
            as_left_precision_type = None
        else:
            # Handle integer to string mapping for API responses
            if isinstance(_as_left_precision_type, int):
                as_left_precision_type_map = {
                    0: "Percentage",
                    1: "Readability",
                    2: "UnitOfMeasure",
                }
                _as_left_precision_type = as_left_precision_type_map.get(
                    _as_left_precision_type, _as_left_precision_type
                )
            as_left_precision_type = ReportDatasetsToMeasurementAllResponseAsLeftPrecisionType(
                _as_left_precision_type
            )
        as_left_minimum = d.pop("AsLeftMinimum", None)
        as_left_nominal = d.pop("AsLeftNominal", None)
        as_left_expected_value = d.pop("AsLeftExpectedValue", None)
        as_left_expected_value_raw = d.pop("AsLeftExpectedValueRaw", None)
        as_left_test_value = d.pop("AsLeftTestValue", None)
        as_left_base_value = d.pop("AsLeftBaseValue", None)
        as_left_maxi_mum = d.pop("AsLeftMaxiMum", None)
        as_left_resolution = d.pop("AsLeftResolution", None)
        as_left_resolution_count = d.pop("AsLeftResolutionCount", None)
        _as_left_measurement_not_taken_result = d.pop("AsLeftMeasurementNotTakenResult", None)
        as_left_measurement_not_taken_result: Optional[
            ReportDatasetsToMeasurementAllResponseAsLeftMeasurementNotTakenResult
        ]
        if not _as_left_measurement_not_taken_result:
            as_left_measurement_not_taken_result = None
        elif _as_left_measurement_not_taken_result is None:
            as_left_measurement_not_taken_result = None
        else:
            as_left_measurement_not_taken_result = (
                ReportDatasetsToMeasurementAllResponseAsLeftMeasurementNotTakenResult(  # noqa: E501
                    _as_left_measurement_not_taken_result
                )
            )
        as_left_hide_from_certificate = d.pop("AsLeftHideFromCertificate", None)
        as_left_measurement_not_taken_reason = d.pop("AsLeftMeasurementNotTakenReason", None)
        as_left_measurement_batch_id = d.pop("AsLeftMeasurementBatchId", None)
        as_left_measurement_id = d.pop("AsLeftMeasurementId", None)
        as_left_standard_id = d.pop("AsLeftStandardId", None)
        as_left_tool_id = d.pop("AsLeftToolId", None)
        as_left_measurement_condition_id = d.pop("AsLeftMeasurementConditionId", None)
        as_left_measurement_point_id = d.pop("AsLeftMeasurementPointId", None)
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
        qualer_api_models_report_datasets_to_measurement_all_response.additional_properties = d
        return qualer_api_models_report_datasets_to_measurement_all_response

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
