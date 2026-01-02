import warnings

from qualer_sdk.models.measurement_type import MeasurementType

ReportDatasetsToMeasurementAllResponseAsLeftMeasurementType = MeasurementType

warnings.warn(
    "ReportDatasetsToMeasurementAllResponseAsLeftMeasurementType is deprecated and will be removed in a future release. Please use MeasurementType instead.",
    DeprecationWarning,
    stacklevel=2,
)
