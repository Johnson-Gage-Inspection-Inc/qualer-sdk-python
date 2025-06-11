from enum import Enum


class QualerApiModelsServiceOrdersFromOrderItemUpdateModelAsFoundCheck(str, Enum):
    FAIL = "Fail"
    NOTSERVICED = "NotServiced"
    PASS = "Pass"

    def __str__(self) -> str:
        return str(self.value)
