from enum import Enum


class ReportDatasetsToMeasurementResponseHysteresisPoint(str, Enum):
    FIRST = "First"
    NONE = "None"
    SECOND = "Second"
    ZERO = "Zero"

    def __str__(self) -> str:
        return str(self.value)
