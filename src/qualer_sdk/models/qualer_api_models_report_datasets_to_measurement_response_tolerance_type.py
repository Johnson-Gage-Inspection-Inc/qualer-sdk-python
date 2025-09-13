from enum import Enum


class ReportDatasetsToMeasurementResponseToleranceType(str, Enum):
    FUNCTION = "Function"
    OFFSET = "Offset"
    PERCENTAGE = "Percentage"
    PERCENTAGEPLUS = "PercentagePlus"
    PPM = "Ppm"
    PPMPLUS = "PpmPlus"
    RANGE = "Range"

    def __str__(self) -> str:
        return str(self.value)
