import warnings

from qualer_sdk.models.service_order_status import ServiceOrderStatus

ServiceOrdersToProviderServiceOrderResponseModelOrderStatus = ServiceOrderStatus

warnings.warn(
    "ServiceOrdersToProviderServiceOrderResponseModelOrderStatus is deprecated and will be removed in a future release. "
    "Please use ServiceOrderStatus instead.",
    DeprecationWarning,
    stacklevel=2,
)
