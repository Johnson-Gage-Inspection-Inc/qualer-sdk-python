from enum import Enum


class ReportDatasetsToMeasurementResponseMeasurementType(str, Enum):
    CUMULATIVE = "Cumulative"
    DATA = "Data"

    def __str__(self) -> str:
        return str(self.value)
