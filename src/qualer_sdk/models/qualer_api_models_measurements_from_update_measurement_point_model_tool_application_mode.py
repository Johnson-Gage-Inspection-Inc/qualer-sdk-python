from enum import Enum


class QualerApiModelsMeasurementsFromUpdateMeasurementPointModelToolApplicationMode(
    str, Enum
):
    COMBINE = "Combine"
    POINT = "Point"
    RANGE = "Range"

    def __str__(self) -> str:
        return str(self.value)
