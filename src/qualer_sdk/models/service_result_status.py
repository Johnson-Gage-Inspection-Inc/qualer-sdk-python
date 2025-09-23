from __future__ import annotations

from enum import IntEnum


class ServiceResultStatus(IntEnum):
    """Service result outcome codes.

    This IntEnum intentionally mirrors Qualer API integer codes so that when
    serialized to JSON, values are emitted as integers. Some endpoints may
    return strings for these values, so a tolerant parser is provided via
    `from_api_value`.
    """

    DONE = 0
    FAIL = 1
    FAILAMBIGUOUS = 10
    FAILSIGNIFICANT = 11
    MISSED = 2
    NOTAVAILABLE = 20
    PASS = 21
    PASSADJUSTMENT = 22
    PASSAMBIGUOUS = 30
    PENDING = 31

    def __str__(self) -> str:  # pragma: no cover - mirrors Enum behavior
        # Keep numeric string form to match IntEnum behavior elsewhere
        return str(self.value)

    @classmethod
    def from_api_value(cls, value: int | str | None) -> ServiceResultStatus | None:
        """Best-effort parser for API values.

        Accepts either:
        - an integer code (e.g. 21),
        - a string name (e.g. "Pass"),
        - a numeric string (e.g. "21").

        Returns None for unknown/unsupported values.
        """
        if value is None:
            return None

        # Fast path: already an int code
        if isinstance(value, int):
            return _INT_TO_ENUM.get(value)

        # Strings: try numeric first
        s = str(value).strip()
        if s.isdigit():
            try:
                code = int(s)
            except ValueError:  # pragma: no cover - guarded by isdigit
                return None
            return _INT_TO_ENUM.get(code)

        # Case-insensitive match against canonical names
        lowered = s.lower()
        for member in cls:
            if member.name.lower() == lowered:
                return member

        # Also allow equality against expected API string values which match names
        for member in cls:
            if str(member.name).lower() == lowered:
                return member

        return None


# Central mapping for integer codes -> Enum members (authoritative)
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
