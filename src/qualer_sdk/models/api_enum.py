from __future__ import annotations

from typing import Any, Dict, Optional, Type, TypeVar


T = TypeVar("T", bound="ApiEnum")


class ApiEnum:
    """Base mixin for API enums that need to handle mixed integer/string inputs.

    Provides common functionality for tolerant parsing from API responses that
    may contain integers, strings, or None values. Concrete enum classes should
    inherit from both this mixin and an appropriate Enum base class.
    """

    @classmethod
    def _get_int_to_enum_mapping(cls) -> Dict[int, Any]:
        """Return the mapping from integer codes to enum members.

        Must be implemented by concrete enum classes to define their
        specific integer-to-enum mappings.
        """
        raise NotImplementedError("Subclasses must implement _get_int_to_enum_mapping")

    @classmethod
    def from_api_value(cls: Type[T], value: int | str | None) -> Optional[T]:
        """Best-effort parser for API values.

        Accepts integers (API codes), strings (enum values or names), or None.
        Returns None for unknown/invalid values instead of raising exceptions.

        Args:
            value: The value to parse - can be int, str, or None

        Returns:
            The corresponding enum member, or None for unknown/invalid values
        """
        if value is None:
            return None

        # Try integer mapping first
        if isinstance(value, int):
            mapping = cls._get_int_to_enum_mapping()
            member = mapping.get(value)
            if isinstance(member, cls):
                return member
            return None

        # Handle string values
        if isinstance(value, str):
            value_str = str(value).strip()

            # If the class has a from_code method, try numeric string parsing first
            if hasattr(cls, "from_code") and value_str.isdigit():
                try:
                    numeric_result = cls.from_code(int(value_str))
                    if numeric_result is not None:
                        return numeric_result
                except (ValueError, TypeError):
                    pass

            # Try case-insensitive value matching
            value_lower = value_str.lower()
            for member in cls:  # type: ignore
                if hasattr(member, "value") and member.value.lower() == value_lower:
                    return member

            # Try case-insensitive name matching
            for member in cls:  # type: ignore
                if hasattr(member, "name") and member.name.lower() == value_lower:
                    return member

        return None

    @classmethod
    def _missing_(cls, value: Any):
        """Handle missing enum values by delegating to from_api_value.

        This allows direct enum construction like MyEnum(value) to work
        with mixed types without needing to refactor call sites.
        """
        return cls.from_api_value(value)
