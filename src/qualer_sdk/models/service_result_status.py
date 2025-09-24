from __future__ import annotations

from enum import Enum
from typing import Dict

from .api_enum import ApiEnum


class ServiceResultStatus(ApiEnum, str, Enum):
    """Service result outcome values (string-first).

    SDK standardizes on string values for readability. Some API endpoints
    (e.g., set_work_item) require integer codes; use to_code() at those edges.
    """

    DONE = "Done"
    FAIL = "Fail"
    FAILAMBIGUOUS = "FailAmbiguous"
    FAILSIGNIFICANT = "FailSignificant"
    MISSED = "Missed"
    NOTAVAILABLE = "NotAvailable"
    PASS = "Pass"
    PASSADJUSTMENT = "PassAdjustment"
    PASSAMBIGUOUS = "PassAmbiguous"
    PENDING = "Pending"

    def __str__(self) -> str:  # pragma: no cover - mirrors Enum behavior
        return str(self.value)

    def to_code(self) -> int:
        """Return the API integer code for this status."""
        return _STR_TO_CODE[self.value]

    @classmethod
    def _get_int_to_enum_mapping(cls) -> Dict[int, "ServiceResultStatus"]:
        """Return the mapping from integer codes to enum members."""
        return _INT_TO_ENUM

    @classmethod
    def from_code(cls, code: int | str | None) -> ServiceResultStatus | None:
        """Parse from an API integer code or numeric string."""
        if code is None:
            return None
        if isinstance(code, int):
            return _INT_TO_ENUM.get(code)
        s = str(code).strip()
        if s.isdigit():
            try:
                return _INT_TO_ENUM.get(int(s))
            except ValueError:  # pragma: no cover
                return None
        return None


# Centralized mappings between API integer codes and string values
_INT_TO_ENUM: dict[int, ServiceResultStatus] = {
    0: ServiceResultStatus.DONE,
    1: ServiceResultStatus.FAIL,
    2: ServiceResultStatus.MISSED,
    10: ServiceResultStatus.FAILAMBIGUOUS,
    11: ServiceResultStatus.FAILSIGNIFICANT,
    20: ServiceResultStatus.NOTAVAILABLE,
    21: ServiceResultStatus.PASS,
    22: ServiceResultStatus.PASSADJUSTMENT,
    30: ServiceResultStatus.PASSAMBIGUOUS,
    31: ServiceResultStatus.PENDING,
}

_STR_TO_CODE: dict[str, int] = {v.value: k for k, v in _INT_TO_ENUM.items()}
