import warnings

from qualer_sdk.models.measurement_not_taken_result import MeasurementNotTakenResult

ReportDatasetsToMeasurementAllResponseAsFoundMeasurementNotTakenResult = MeasurementNotTakenResult

warnings.warn(
    "ReportDatasetsToMeasurementAllResponseAsFoundMeasurementNotTakenResult is deprecated and will be removed in a future release. Please use MeasurementNotTakenResult instead.",
    DeprecationWarning,
    stacklevel=2,
)
