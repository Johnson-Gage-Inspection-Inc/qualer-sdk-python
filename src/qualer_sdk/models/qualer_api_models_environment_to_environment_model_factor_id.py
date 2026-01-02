import warnings

from qualer_sdk.models.environment_factor import EnvironmentFactor

EnvironmentToEnvironmentModelFactorId = EnvironmentFactor

warnings.warn(
    "EnvironmentToEnvironmentModelFactorId is deprecated and will be removed in a future release. Please use EnvironmentFactor instead.",
    DeprecationWarning,
    stacklevel=2,
)
