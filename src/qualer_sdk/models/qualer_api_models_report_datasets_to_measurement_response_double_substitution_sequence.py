from enum import Enum


class ReportDatasetsToMeasurementResponseDoubleSubstitutionSequence(str, Enum):
    STANDARDTESTED = "StandardTested"
    TESTEDSTANDARD = "TestedStandard"
    ZEROSTANDARD = "ZeroStandard"

    def __str__(self) -> str:
        return str(self.value)
