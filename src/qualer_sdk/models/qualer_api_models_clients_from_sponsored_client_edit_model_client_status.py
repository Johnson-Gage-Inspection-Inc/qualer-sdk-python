from enum import Enum


class QualerApiModelsClientsFromSponsoredClientEditModelClientStatus(str, Enum):
    APPROVED = "Approved"
    HIDDEN = "Hidden"
    NOTAPPROVED = "NotApproved"
    PROSPECT = "Prospect"

    def __str__(self) -> str:
        return str(self.value)
