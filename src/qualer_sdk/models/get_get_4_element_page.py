import warnings

from qualer_sdk.models.element_page import ElementPage

GetGet4ElementPage = ElementPage

warnings.warn(
    "GetGet4ElementPage is deprecated and will be removed in a future release. Please use ElementPage instead.",
    DeprecationWarning,
    stacklevel=2,
)
