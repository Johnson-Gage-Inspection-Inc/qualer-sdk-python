from enum import Enum


class QualerApiModelsReportDatasetsToMeasurementAllResponseAsFoundGuardBandLogic(
    str, Enum
):
    NCSLZ5403 = "Ncslz5403"
    RDS = "Rds"
    TUR41 = "Tur41"
    UNCERTAINTY = "Uncertainty"

    def __str__(self) -> str:
        return str(self.value)
