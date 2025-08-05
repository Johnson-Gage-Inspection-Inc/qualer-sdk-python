from enum import Enum


class QualerApiModelsReportDatasetsToServiceOrderResponseProcessDateOption(str, Enum):
    ASSOONASPOSSIBLE = "AsSoonAsPossible"
    BEFOREDATE = "BeforeDate"
    ONDATETIME = "OnDateTime"
    URGENT = "Urgent"
    WITHINRANGE = "WithinRange"

    def __str__(self) -> str:
        return str(self.value)
