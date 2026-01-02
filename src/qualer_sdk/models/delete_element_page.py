import warnings

from qualer_sdk.models.element_page import ElementPage

DeleteElementPage = ElementPage

warnings.warn(
    "DeleteElementPage is deprecated and will be removed in a future release. Please use ElementPage instead.",
    DeprecationWarning,
    stacklevel=2,
)
