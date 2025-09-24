# src/qualer_sdk/models/service_order_status.py
from __future__ import annotations

from .api_enum import ApiEnum


class ServiceOrderStatus(ApiEnum):
    NEW = "New"
    DRAFT = "Draft"
    WAITINGFORAPPROVAL = "WaitingForApproval"
    SUBMITTED = "Submitted"
    PROCESSING = "Processing"
    QUALITYCONTROL = "QualityControl"
    CANCELLED = "Cancelled"
    WAITINGFORCLIENTSIGNOFF = "WaitingForClientSignOff"
    COMPLETED = "Completed"
    DENIED = "Denied"
    DELAYED = "Delayed"
    SCHEDULING = "Scheduling"
    CLOSED = "Closed"
    WAITINGFORVENDORSIGNOFF = "WaitingForVendorSignOff"
    DELAYEDAPPROVAL = "DelayedApproval"
    READY = "Ready"


# If/when we know their integer codes, wire them here once (runtime assign).

ServiceOrderStatus.INT_CODES = {  # type: ignore[attr-defined]
    7: ServiceOrderStatus.NEW,  # Inferred based on enum order; not yet observed
    8: ServiceOrderStatus.DRAFT,  # Inferred based on enum order; not yet observed
    9: ServiceOrderStatus.WAITINGFORAPPROVAL,
    10: ServiceOrderStatus.SUBMITTED,  # Inferred based on enum order; not yet observed
    11: ServiceOrderStatus.PROCESSING,
    12: ServiceOrderStatus.QUALITYCONTROL,
    13: ServiceOrderStatus.CANCELLED,
    14: ServiceOrderStatus.WAITINGFORCLIENTSIGNOFF,  # Inferred based on enum order; not yet observed
    15: ServiceOrderStatus.COMPLETED,
    16: ServiceOrderStatus.DENIED,
    17: ServiceOrderStatus.DELAYED,
    18: ServiceOrderStatus.SCHEDULING,
    19: ServiceOrderStatus.CLOSED,
    20: ServiceOrderStatus.WAITINGFORVENDORSIGNOFF,
    21: ServiceOrderStatus.DELAYEDAPPROVAL,  # Inferred based on enum order; not yet observed
    22: ServiceOrderStatus.READY,  # Inferred based on enum order; not yet observed
}
