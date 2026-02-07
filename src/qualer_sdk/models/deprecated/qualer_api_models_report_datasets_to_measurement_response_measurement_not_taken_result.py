import warnings

from qualer_sdk.models.measurement_not_taken_result import MeasurementNotTakenResult

ReportDatasetsToMeasurementResponseMeasurementNotTakenResult = MeasurementNotTakenResult

warnings.warn(
    "ReportDatasetsToMeasurementResponseMeasurementNotTakenResult is deprecated and will be removed in a future release. Please use MeasurementNotTakenResult instead.",
    DeprecationWarning,
    stacklevel=2,
)
