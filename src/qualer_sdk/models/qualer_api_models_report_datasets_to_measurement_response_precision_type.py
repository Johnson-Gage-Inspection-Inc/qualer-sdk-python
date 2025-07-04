from enum import Enum


class QualerApiModelsReportDatasetsToMeasurementResponsePrecisionType(str, Enum):
    PERCENTAGE = "Percentage"
    READABILITY = "Readability"
    UNITOFMEASURE = "UnitOfMeasure"

    def __str__(self) -> str:
        return str(self.value)
