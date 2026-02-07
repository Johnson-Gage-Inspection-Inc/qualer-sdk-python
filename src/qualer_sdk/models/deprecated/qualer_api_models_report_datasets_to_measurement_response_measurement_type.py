import warnings

from qualer_sdk.models.measurement_type import MeasurementType

ReportDatasetsToMeasurementResponseMeasurementType = MeasurementType

warnings.warn(
    "ReportDatasetsToMeasurementResponseMeasurementType is deprecated and will be removed in a future release. Please use MeasurementType instead.",
    DeprecationWarning,
    stacklevel=2,
)
