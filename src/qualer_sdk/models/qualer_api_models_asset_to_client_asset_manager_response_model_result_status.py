from enum import Enum


class QualerApiModelsAssetToClientAssetManagerResponseModelResultStatus(int, Enum):
    NOTAVAILABLE = 0
    FAIL = 1
    PASS = 2
    FAILAMBIGUOUS = 10
    FAILSIGNIFICANT = 11
    PASSAMBIGUOUS = 20
    PASSADJUSTMENT = 21
    DONE = 22
    PENDING = 30
    MISSED = 31

    def __str__(self) -> str:
        return str(self.value)
