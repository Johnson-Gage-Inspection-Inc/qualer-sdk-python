from enum import Enum


class QualerApiModelsServiceOrdersFromOrderItemUpdateModelAsLeftResult(str, Enum):
    DONE = "Done"
    FAIL = "Fail"
    FAILAMBIGUOUS = "FailAmbiguous"
    FAILSIGNIFICANT = "FailSignificant"
    NOTAVAILABLE = "NotAvailable"
    PASS = "Pass"
    PASSADJUSTMENT = "PassAdjustment"
    PASSAMBIGUOUS = "PassAmbiguous"

    def __str__(self) -> str:
        return str(self.value)
