from enum import Enum


class QualerApiModelsAssetToAssetManageResponseModelResultStatus(str, Enum):
    DONE = "Done"
    FAIL = "Fail"
    FAILAMBIGUOUS = "FailAmbiguous"
    FAILSIGNIFICANT = "FailSignificant"
    MISSED = "Missed"
    NOTAVAILABLE = "NotAvailable"
    PASS = "Pass"
    PASSADJUSTMENT = "PassAdjustment"
    PASSAMBIGUOUS = "PassAmbiguous"
    PENDING = "Pending"

    def __str__(self) -> str:
        return str(self.value)
