from enum import Enum


class QualerApiModelsReportDatasetsToMeasurementResponseSpecificationMode(str, Enum):
    POINT = "Point"
    RANGE = "Range"

    def __str__(self) -> str:
        return str(self.value)
