from enum import Enum


class MeasurementType(str, Enum):
    CUMULATIVE = "Cumulative"
    DATA = "Data"

    def __str__(self) -> str:
        return str(self.value)
