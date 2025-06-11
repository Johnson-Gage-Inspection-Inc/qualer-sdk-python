from enum import Enum


class QualerApiModelsReportDatasetsToMeasurementResponseMeasurementNotTakenResult(
    str, Enum
):
    FAIL = "Fail"
    LIMITED = "Limited"
    PASS = "Pass"

    def __str__(self) -> str:
        return str(self.value)
