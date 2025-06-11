from enum import Enum


class QualerApiModelsReportDatasetsToMeasurementChannelResultResponseBatchType(
    str, Enum
):
    ASFOUND = "AsFound"
    ASLEFT = "AsLeft"
    UNSET = "Unset"

    def __str__(self) -> str:
        return str(self.value)
