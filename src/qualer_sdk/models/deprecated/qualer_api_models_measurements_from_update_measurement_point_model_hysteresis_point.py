import warnings

from qualer_sdk.models.hysteresis_point import HysteresisPoint

MeasurementsFromUpdateMeasurementPointModelHysteresisPoint = HysteresisPoint

warnings.warn(
    "MeasurementsFromUpdateMeasurementPointModelHysteresisPoint is deprecated and will be removed in a future release. Please use HysteresisPoint instead.",
    DeprecationWarning,
    stacklevel=2,
)
