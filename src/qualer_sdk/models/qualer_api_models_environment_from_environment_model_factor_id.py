import warnings

from qualer_sdk.models.environment_factor import EnvironmentFactor

EnvironmentFromEnvironmentModelFactorId = EnvironmentFactor

warnings.warn(
    "EnvironmentFromEnvironmentModelFactorId is deprecated and will be removed in a future release. Please use EnvironmentFactor instead.",
    DeprecationWarning,
    stacklevel=2,
)
