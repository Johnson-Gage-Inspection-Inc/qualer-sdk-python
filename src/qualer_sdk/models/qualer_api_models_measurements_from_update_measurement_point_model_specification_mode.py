from enum import Enum


class QualerApiModelsMeasurementsFromUpdateMeasurementPointModelSpecificationMode(
    str, Enum
):
    POINT = "Point"
    RANGE = "Range"

    def __str__(self) -> str:
        return str(self.value)
