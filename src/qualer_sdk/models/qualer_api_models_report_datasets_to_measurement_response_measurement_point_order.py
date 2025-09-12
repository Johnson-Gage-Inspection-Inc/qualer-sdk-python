from enum import Enum


class QualerApiModelsReportDatasetsToMeasurementResponseMeasurementPointOrder(str, Enum):
    ASCENDINGDESCENDING = "AscendingDescending"
    ASENTERED = "AsEntered"
    DESCENDINGASCENDING = "DescendingAscending"
    ZEROASCENDINGDESCENDING = "ZeroAscendingDescending"
    ZERODESCENDINGASCENDING = "ZeroDescendingAscending"

    def __str__(self) -> str:
        return str(self.value)
