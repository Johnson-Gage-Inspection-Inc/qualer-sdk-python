from enum import Enum


class AssetToAssetResponseModelAssetStatus(str, Enum):
    ACTIVE = "Active"
    FAILED = "Failed"
    INACTIVE = "Inactive"
    NEW = "New"
    RETIRED = "Retired"

    def __str__(self) -> str:
        return str(self.value)
