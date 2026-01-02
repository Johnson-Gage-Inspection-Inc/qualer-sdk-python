import warnings

from qualer_sdk.models.measurement_not_taken_result import MeasurementNotTakenResult

ReportDatasetsToMeasurementAllResponseAsLeftMeasurementNotTakenResult = MeasurementNotTakenResult

warnings.warn(
    "ReportDatasetsToMeasurementAllResponseAsLeftMeasurementNotTakenResult is deprecated and will be removed in a future release. Please use MeasurementNotTakenResult instead.",
    DeprecationWarning,
    stacklevel=2,
)
