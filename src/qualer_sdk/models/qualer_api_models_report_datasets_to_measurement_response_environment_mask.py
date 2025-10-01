import warnings

from qualer_sdk.models.environment_factor import EnvironmentFactor

ReportDatasetsToMeasurementResponseEnvironmentMask = EnvironmentFactor

warnings.warn(
    "ReportDatasetsToMeasurementResponseEnvironmentMask is deprecated and will be removed in a future release. Please use EnvironmentFactor instead.",
    DeprecationWarning,
    stacklevel=2,
)
