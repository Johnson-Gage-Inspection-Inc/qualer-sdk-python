from enum import Enum


class QualerApiModelsServiceOrdersFromOrderItemUpdateModelResultStatus(int, Enum):
    NOTAVAILABLE = 0
    FAIL = 1
    PASS = 2
    FAILAMBIGUOUS = 10
    FAILSIGNIFICANT = 11
    PASSAMBIGUOUS = 20
    PASSADJUSTMENT = 21
    DONE = 22

    def __str__(self) -> str:
        return str(self.value)
