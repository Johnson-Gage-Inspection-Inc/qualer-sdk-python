from __future__ import annotations

from enum import Enum
from typing import Dict

from .api_enum import ApiEnum


class WorkStatus(ApiEnum, str, Enum):
    """Work status values for order items.

    SDK standardizes on string values for readability. Integer codes
    are mapped from API responses and can be accessed via to_code().
    """

    PENDING = "Pending"
    INPROGRESS = "InProgress"
    COMPLETED = "Completed"
    DELAYED = "Delayed"
    WITHDRAWN = "Withdrawn"
    LOCKED = "Locked"
    NEW = "New"
    CLOSED = "Closed"
    WAIT = "Wait"

    def __str__(self) -> str:
        return str(self.value)

    def to_code(self) -> int:
        """Return the API integer code for this status."""
        return _STR_TO_CODE[self.value]

    @classmethod
    def _get_int_to_enum_mapping(cls) -> Dict[int, "WorkStatus"]:
        """Return the mapping from integer codes to enum members."""
        return _INT_TO_ENUM


# Centralized mappings between API integer codes and string values
_INT_TO_ENUM: Dict[int, WorkStatus] = {
    0: WorkStatus.PENDING,
    1: WorkStatus.INPROGRESS,
    2: WorkStatus.COMPLETED,
    3: WorkStatus.DELAYED,
    4: WorkStatus.WITHDRAWN,
    5: WorkStatus.LOCKED,
    6: WorkStatus.NEW,
    7: WorkStatus.CLOSED,
    8: WorkStatus.WAIT,
}

_STR_TO_CODE: Dict[str, int] = {v.value: k for k, v in _INT_TO_ENUM.items()}
