from enum import Enum


class ServiceOrdersFromOrderItemUpdateModelAsLeftCheck(str, Enum):
    FAIL = "Fail"
    NOTSERVICED = "NotServiced"
    PASS = "Pass"

    def __str__(self) -> str:
        return str(self.value)
