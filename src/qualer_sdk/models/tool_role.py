from __future__ import annotations

from enum import Enum


class ToolRole(str, Enum):
    REFERENCE_STANDARD = "Reference Standard"
    ENVIRONMENTAL_SENSOR = "Environmental Sensor"
    CONTROLLED_ENVIRONMENT = "Controlled Environment"
    SCIENTIFIC_INSTRUMENT = "Scientific Instrument"

    def __str__(self) -> str:  # pragma: no cover - mirrors Enum behavior
        return str(self.value)

    @classmethod
    def from_api_value(cls, value: int | str | None) -> ToolRole | None:
        """Best-effort parser for API values.
        Accepts either a string enum value (e.g. "Environmental Sensor") or an integer code
        (e.g. 1) seen in API responses. Returns None for unknown values.
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
_INT_TO_STR: dict[int, ToolRole] = {
    0: ToolRole.REFERENCE_STANDARD,
    1: ToolRole.ENVIRONMENTAL_SENSOR,
    2: ToolRole.CONTROLLED_ENVIRONMENT,
    3: ToolRole.SCIENTIFIC_INSTRUMENT,
}
