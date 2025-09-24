from __future__ import annotations

from enum import Enum
from typing import Any, Mapping, TypeVar

E = TypeVar("E", bound="ApiEnum")


class ApiEnum(str, Enum):
    """
    - If a subclass sets INT_CODES (int -> member), we use it.
    - Otherwise we fall back to the declaration order: 0..n map to list(cls)[0..n].
    """

    def __str__(self) -> str:
        return self.value

    def __int__(self) -> int:
        cls = type(self)
        int_codes: Mapping[int, ApiEnum] | None = getattr(cls, "INT_CODES", None)
        if int_codes:
            reverse: dict[ApiEnum, int] = {v: k for k, v in int_codes.items()}
            if self in reverse:
                return reverse[self]
            raise ValueError(f"No int alias defined for {cls.__name__}.{self.name}")

        # ordinal fallback
        members = list(cls)
        try:
            return members.index(self)
        except ValueError:
            raise ValueError(f"{self} is not a member of {cls.__name__}")

    def to_api(self) -> str:
        return self.value

    @classmethod
    def _missing_(cls: type[E], value: Any) -> E | None:
        # ints -> explicit mapping or ordinal fallback
        if isinstance(value, int):
            int_codes: Mapping[int, ApiEnum] | None = getattr(cls, "INT_CODES", None)
            if int_codes:
                mapped = int_codes.get(value)
                if mapped is not None and isinstance(mapped, cls):
                    return mapped  # type: ignore[return-value]
                return None
            members = list(cls)
            if 0 <= value < len(members):
                return members[value]  # type: ignore[return-value]
            return None

        # strings: digit-string → int path; else case-insensitive value; else enum NAME
        if isinstance(value, str):
            s = value.strip()
            if s.isdigit():
                return cls._missing_(int(s))
            lv = s.lower()
            for m in cls:
                if m.value.lower() == lv:
                    return m  # type: ignore[return-value]
            try:
                return cls[s.upper()]  # type: ignore[return-value]
            except Exception:
                return None

        return None

    @classmethod
    def parse(cls: type[E], value: Any) -> E | None:
        try:
            return cls(value)  # type: ignore[call-arg]
        except ValueError:
            return None


# Provide the default *after* class creation to avoid creating a member.
ApiEnum.INT_CODES = {}  # type: ignore[attr-defined]
