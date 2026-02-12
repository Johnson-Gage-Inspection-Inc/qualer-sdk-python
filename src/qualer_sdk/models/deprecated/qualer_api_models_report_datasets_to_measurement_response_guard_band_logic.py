import warnings

from qualer_sdk.models.guard_band_logic import GuardBandLogic

ReportDatasetsToMeasurementResponseGuardBandLogic = GuardBandLogic

warnings.warn(
    "ReportDatasetsToMeasurementResponseGuardBandLogic is deprecated and will be removed in a future release. Please use GuardBandLogic instead.",
    DeprecationWarning,
    stacklevel=2,
)
