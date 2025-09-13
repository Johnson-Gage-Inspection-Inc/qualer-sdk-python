from enum import Enum


class ReportDatasetsToMeasurementResponseReadingEntryLogic(str, Enum):
    DOUBLESUBSTITUTION = "DoubleSubstitution"
    MEASUREDVALUECONVERSION = "MeasuredValueConversion"
    MEASUREDVALUECONVERSIONDISPLAY = "MeasuredValueConversionDisplay"
    SINGLEVALUE = "SingleValue"
    TWOVALUES = "TwoValues"
    TWOVALUESANDRESULT = "TwoValuesAndResult"

    def __str__(self) -> str:
        return str(self.value)
