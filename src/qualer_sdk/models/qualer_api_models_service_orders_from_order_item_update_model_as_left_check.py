import warnings

from qualer_sdk.models.service_order_check_result import ServiceOrderCheckResult

ServiceOrdersFromOrderItemUpdateModelAsLeftCheck = ServiceOrderCheckResult

warnings.warn(
    "ServiceOrdersFromOrderItemUpdateModelAsLeftCheck is deprecated and will be removed in a future release. Please use ServiceOrderCheckResult instead.",
    DeprecationWarning,
    stacklevel=2,
)
