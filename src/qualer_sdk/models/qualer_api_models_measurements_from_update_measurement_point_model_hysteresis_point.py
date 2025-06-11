from enum import Enum


class QualerApiModelsMeasurementsFromUpdateMeasurementPointModelHysteresisPoint(
    str, Enum
):
    FIRST = "First"
    NONE = "None"
    SECOND = "Second"
    ZERO = "Zero"

    def __str__(self) -> str:
        return str(self.value)
