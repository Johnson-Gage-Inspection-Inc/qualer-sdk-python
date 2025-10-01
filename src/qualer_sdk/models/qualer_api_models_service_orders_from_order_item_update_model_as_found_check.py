import warnings

from qualer_sdk.models.service_order_check_result import ServiceOrderCheckResult

ServiceOrdersFromOrderItemUpdateModelAsFoundCheck = ServiceOrderCheckResult

warnings.warn(
    "ServiceOrdersFromOrderItemUpdateModelAsFoundCheck is deprecated and will be removed in a future release. Please use ServiceOrderCheckResult instead.",
    DeprecationWarning,
    stacklevel=2,
)
