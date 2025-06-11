from enum import Enum


class QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModelToleranceMode(
    str, Enum
):
    ASYMMETRIC = "Asymmetric"
    RANGE = "Range"
    SYMMETRIC = "Symmetric"

    def __str__(self) -> str:
        return str(self.value)
