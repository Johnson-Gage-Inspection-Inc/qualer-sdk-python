from enum import Enum


class QualerApiModelsServiceOrderItemPartsToOrderItemPartResponseModelServiceOrderChargeType(
    str, Enum
):
    CHARGE = "Charge"
    LABOR = "Labor"
    PART = "Part"

    def __str__(self) -> str:
        return str(self.value)
