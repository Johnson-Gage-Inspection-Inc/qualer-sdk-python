import warnings

from qualer_sdk.models.measurement_precision_type import MeasurementPrecisionType

ReportDatasetsToMeasurementAllResponseAsFoundPrecisionType = MeasurementPrecisionType

warnings.warn(
    "ReportDatasetsToMeasurementAllResponseAsFoundPrecisionType is deprecated and will be removed in a future release. Please use MeasurementPrecisionType instead.",
    DeprecationWarning,
    stacklevel=2,
)
