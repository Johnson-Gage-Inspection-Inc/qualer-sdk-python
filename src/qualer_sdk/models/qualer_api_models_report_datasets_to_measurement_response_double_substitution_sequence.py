from enum import Enum


class QualerApiModelsReportDatasetsToMeasurementResponseDoubleSubstitutionSequence(str, Enum):
    STANDARDTESTED = "StandardTested"
    TESTEDSTANDARD = "TestedStandard"
    ZEROSTANDARD = "ZeroStandard"

    def __str__(self) -> str:
        return str(self.value)
