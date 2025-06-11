from enum import Enum


class QualerApiModelsReportDatasetsToMeasurementChannelResultResponseResult(str, Enum):
    DONE = "Done"
    FAIL = "Fail"
    FAILAMBIGUOUS = "FailAmbiguous"
    FAILSIGNIFICANT = "FailSignificant"
    NOTSERVICED = "NotServiced"
    PASS = "Pass"
    PASSADJUSTMENT = "PassAdjustment"
    PASSAMBIGUOUS = "PassAmbiguous"
    PENDING = "Pending"

    def __str__(self) -> str:
        return str(self.value)
