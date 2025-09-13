from enum import Enum


class ReportDatasetsToMeasurementResponseMeasurementNotTakenResult(str, Enum):
    FAIL = "Fail"
    LIMITED = "Limited"
    PASS = "Pass"

    def __str__(self) -> str:
        return str(self.value)
