from enum import Enum


class QualerApiModelsReportDatasetsToMeasurementAllResponseAsLeftPrecisionType(
    str, Enum
):
    PERCENTAGE = "Percentage"
    READABILITY = "Readability"
    UNITOFMEASURE = "UnitOfMeasure"

    def __str__(self) -> str:
        return str(self.value)
