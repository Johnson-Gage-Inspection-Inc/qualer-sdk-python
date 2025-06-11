from enum import Enum


class QualerApiModelsReportDatasetsToMeasurementResponseToleranceUnit(str, Enum):
    PERCENTAGE = "Percentage"
    PPM = "Ppm"
    UNITOFMEASURE = "UnitOfMeasure"

    def __str__(self) -> str:
        return str(self.value)
