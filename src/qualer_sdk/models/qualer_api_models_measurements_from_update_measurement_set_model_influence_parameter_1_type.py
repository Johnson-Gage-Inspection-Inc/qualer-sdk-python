from enum import Enum


class MeasurementsFromUpdateMeasurementSetModelInfluenceParameter1Type(str, Enum):
    CUSTOMFIELD = "CustomField"
    MANUALLYSELECTED = "ManuallySelected"
    MEASUREMENTQUANTITY = "MeasurementQuantity"
    STATICVALUE = "StaticValue"
    TOOLATTRIBUTE = "ToolAttribute"
    UUTATTRIBUTE = "UutAttribute"

    def __str__(self) -> str:
        return str(self.value)
