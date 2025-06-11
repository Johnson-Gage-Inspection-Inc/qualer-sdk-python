from enum import Enum


class QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModelSpecificationMode(
    str, Enum
):
    POINT = "Point"
    RANGE = "Range"

    def __str__(self) -> str:
        return str(self.value)
