from enum import Enum


class AssetFilterType(str, Enum):
    """Filter types for GetAssetManagerList API endpoint."""

    CLIENT_UNSET = "ClientUnset"
    CLIENT_ASSETS_COLLECTED = "ClientAssetsCollected"
    CLIENT_PAST_DUE = "ClientPastDue"
    CLIENT_DUE_FOR_SERVICE = "ClientDueForService"
    CLIENT_OUT_OF_SERVICE = "ClientOutOfService"
    CLIENT_WITHOUT_SCHEDULE = "ClientWithoutSchedule"

    def __str__(self) -> str:
        return str(self.value)
