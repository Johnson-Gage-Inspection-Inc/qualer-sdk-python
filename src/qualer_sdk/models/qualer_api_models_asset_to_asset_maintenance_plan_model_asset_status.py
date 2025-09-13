from enum import Enum


class AssetToAssetMaintenancePlanModelAssetStatus(str, Enum):
    ACTIVE = "Active"
    FAILED = "Failed"
    INACTIVE = "Inactive"
    NEW = "New"
    RETIRED = "Retired"

    def __str__(self) -> str:
        return str(self.value)
