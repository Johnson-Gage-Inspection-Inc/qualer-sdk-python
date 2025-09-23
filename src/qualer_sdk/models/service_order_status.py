from __future__ import annotations

from enum import Enum


class ServiceOrderStatus(str, Enum):
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

    # Central mapping for observed integer codes -> API string values
    def __str__(self) -> str:  # pragma: no cover - mirrors Enum behavior
        return str(self.value)

    @classmethod
    def from_api_value(cls, value: int | str | None) -> ServiceOrderStatus | None:
        """Best-effort parser for API values.

        Accepts either a string enum value (e.g. "Processing") or an integer code
        (e.g. 11) seen in some API responses. Returns None for unknown values.
        """
        if value is None:
            return None

        if isinstance(value, int):
            mapped = _INT_TO_STR.get(value)
            return mapped if isinstance(mapped, cls) else None

        # Strings: accept exact match; try case-insensitive as a fallback.
        try:
            return cls(value)
        except ValueError:
            # Case-insensitive fallback
            normalized = str(value).strip().lower()
            for member in cls:
                if member.value.lower() == normalized:
                    return member
            return None


# Central mapping for observed integer codes -> API string values
_INT_TO_STR: dict[int, ServiceOrderStatus] = {
    7: ServiceOrderStatus.NEW,  # This is a guess; not yet observed
    8: ServiceOrderStatus.DRAFT,  # This is a guess; not yet observed
    9: ServiceOrderStatus.WAITINGFORAPPROVAL,
    10: ServiceOrderStatus.SUBMITTED,  # Not observed, but inferred from the order
    11: ServiceOrderStatus.PROCESSING,
    12: ServiceOrderStatus.QUALITYCONTROL,
    13: ServiceOrderStatus.CANCELLED,
    14: ServiceOrderStatus.WAITINGFORCLIENTSIGNOFF,  # Not observed, but inferred from the order
    15: ServiceOrderStatus.COMPLETED,
    16: ServiceOrderStatus.DENIED,
    17: ServiceOrderStatus.DELAYED,
    18: ServiceOrderStatus.SCHEDULING,
    19: ServiceOrderStatus.CLOSED,
    20: ServiceOrderStatus.WAITINGFORVENDORSIGNOFF,
    21: ServiceOrderStatus.DELAYEDAPPROVAL,  # This is a guess; not yet observed
    22: ServiceOrderStatus.READY,  # This is a guess; not yet observed
}
