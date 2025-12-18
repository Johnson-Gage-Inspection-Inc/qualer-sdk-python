from __future__ import annotations

from enum import Enum


class RecordType(str, Enum):
    WAITING_FOR_AGREEMENT = "WaitingForAgreement"
    EQUIPMENT = "Equipment"
    SYSTEM = "System"
    AGREEMENT = "Agreement"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def from_api_value(cls, value: int | str | None) -> RecordType | None:
        """Best-effort parser for API values.
        Accepts either a string enum value (e.g. "Equipment") or an integer code
        (e.g. 1) seen in some API responses. Returns None for unknown values.
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
_INT_TO_STR: dict[int, RecordType] = {
    0: RecordType.WAITING_FOR_AGREEMENT,
    1: RecordType.EQUIPMENT,
    2: RecordType.SYSTEM,
    3: RecordType.AGREEMENT,
}
