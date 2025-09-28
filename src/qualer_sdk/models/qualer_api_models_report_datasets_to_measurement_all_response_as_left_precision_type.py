import warnings

from qualer_sdk.models.measurement_precision_type import MeasurementPrecisionType

ReportDatasetsToMeasurementAllResponseAsLeftPrecisionType = MeasurementPrecisionType

warnings.warn(
    "ReportDatasetsToMeasurementAllResponseAsLeftPrecisionType is deprecated and will be removed in a future release. Please use MeasurementPrecisionType instead.",
    DeprecationWarning,
    stacklevel=2,
)
