from enum import Enum


class QualerApiModelsAssetToClientAssetManagerResponseModelRecordType(str, Enum):
    AGREEMENT = "Agreement"
    EQUIPMENT = "Equipment"
    SYSTEM = "System"
    WAITINGFORAGREEMENT = "WaitingForAgreement"

    def __str__(self) -> str:
        return str(self.value)
