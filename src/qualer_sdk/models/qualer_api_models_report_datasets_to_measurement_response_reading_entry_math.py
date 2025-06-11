from enum import Enum


class QualerApiModelsReportDatasetsToMeasurementResponseReadingEntryMath(str, Enum):
    ADDITION = "Addition"
    AVERAGE = "Average"
    DIFFERENCE = "Difference"
    DIVISION = "Division"
    MAXIMUM = "Maximum"
    MINIMUM = "Minimum"
    MULTIPLICATION = "Multiplication"
    REVERSESUBTRACTION = "ReverseSubtraction"
    SUBTRACTION = "Subtraction"

    def __str__(self) -> str:
        return str(self.value)
