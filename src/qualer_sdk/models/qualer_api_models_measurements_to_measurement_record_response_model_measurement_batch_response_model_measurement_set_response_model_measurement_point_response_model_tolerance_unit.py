from enum import Enum


class QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModelToleranceUnit(
    str, Enum
):
    PERCENTAGE = "Percentage"
    PPM = "Ppm"
    UNITOFMEASURE = "UnitOfMeasure"

    def __str__(self) -> str:
        return str(self.value)
