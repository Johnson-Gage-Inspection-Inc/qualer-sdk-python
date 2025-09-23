from enum import Enum


class WorkStatus(str, Enum):
    PENDING = "Pending"
    INPROGRESS = "InProgress"
    COMPLETED = "Completed"
    DELAYED = "Delayed"
    WITHDRAWN = "Withdrawn"
    LOCKED = "Locked"
    NEW = "New"
    CLOSED = "Closed"
    WAIT = "Wait"

    def __str__(self) -> str:  # pragma: no cover
        return str(self.value)

    def __int__(self) -> int:
        return self.to_code()

    @classmethod
    def _missing_(cls, value: object) -> "WorkStatus | None":  # type: ignore[override]
        """Allow WorkStatus(value) to accept ints, numeric strings, names, or values.

        This avoids widespread refactors by tolerating mixed-type inputs.
        """
        return cls.from_api_value(value)  # type: ignore[arg-type]

    def to_code(self) -> int:
        return _STR_TO_CODE[self.value]

    @classmethod
    def from_code(cls, code: int | str | None) -> "WorkStatus | None":
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

    @classmethod
    def from_api_value(cls, value: int | str | None) -> "WorkStatus | None":
        if value is None:
            return None
        member = cls.from_code(value)
        if member is not None:
            return member
        s = str(value).strip().lower()
        for m in cls:
            if m.value.lower() == s or m.name.lower() == s:
                return m
        return None


_INT_TO_ENUM: dict[int, WorkStatus] = {
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

_STR_TO_CODE: dict[str, int] = {v.value: k for k, v in _INT_TO_ENUM.items()}
