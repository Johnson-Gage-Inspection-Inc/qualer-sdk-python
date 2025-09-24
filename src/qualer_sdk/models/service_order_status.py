from __future__ import annotations

from enum import Enum
from typing import Dict

from .api_enum import ApiEnum


class ServiceOrderStatus(ApiEnum, str, Enum):
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

    def __str__(self) -> str:  # pragma: no cover - mirrors Enum behavior
        return str(self.value)

    @classmethod
    def _get_int_to_enum_mapping(cls) -> Dict[int, "ServiceOrderStatus"]:
        """Return the mapping from integer codes to enum members."""
        return _INT_TO_STR


# Central mapping for observed integer codes -> API string values
_INT_TO_STR: dict[int, ServiceOrderStatus] = {
    7: ServiceOrderStatus.NEW,  # Inferred based on enum order; not yet observed
    8: ServiceOrderStatus.DRAFT,  # Inferred based on enum order; not yet observed
    9: ServiceOrderStatus.WAITINGFORAPPROVAL,
    10: ServiceOrderStatus.SUBMITTED,  # Inferred based on enum order; not yet observed
    11: ServiceOrderStatus.PROCESSING,
    12: ServiceOrderStatus.QUALITYCONTROL,
    13: ServiceOrderStatus.CANCELLED,
    14: ServiceOrderStatus.WAITINGFORCLIENTSIGNOFF,  # Inferred; not observed
    15: ServiceOrderStatus.COMPLETED,
    16: ServiceOrderStatus.DENIED,
    17: ServiceOrderStatus.DELAYED,
    18: ServiceOrderStatus.SCHEDULING,
    19: ServiceOrderStatus.CLOSED,
    20: ServiceOrderStatus.WAITINGFORVENDORSIGNOFF,
    21: ServiceOrderStatus.DELAYEDAPPROVAL,  # Inferred based on enum order; not yet observed
    22: ServiceOrderStatus.READY,  # Inferred based on enum order; not yet observed
}
