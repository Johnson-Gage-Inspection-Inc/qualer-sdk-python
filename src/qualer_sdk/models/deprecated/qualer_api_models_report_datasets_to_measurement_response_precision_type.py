import warnings

from qualer_sdk.models.measurement_precision_type import MeasurementPrecisionType

ReportDatasetsToMeasurementResponsePrecisionType = MeasurementPrecisionType

warnings.warn(
    "ReportDatasetsToMeasurementResponsePrecisionType is deprecated and will be removed in a future release. Please use MeasurementPrecisionType instead.",
    DeprecationWarning,
    stacklevel=2,
)
