from enum import Enum


class FilterType(str, Enum):
    """Filter types for GetAssetManagerList API endpoint."""

    NONE = "None"
    DUE_FOR_SERVICE = "DueForService"
    RECENTLY_SERVICED = "RecentlyServiced"
    NOT_SERVICED = "NotServiced"
    RECENTLY_PURCHASED = "RecentlyPurchased"
    WARRANTY_EXPIRING = "WarrantyExpiring"
    DUE_FOR_REPLACEMENT = "DueForReplacement"
    OUT_OF_SERVICE = "OutOfService"
    PAST_DUE = "PastDue"
    SERVICE_PENDING = "ServicePending"
    COLLECTED_ASSETS = "CollectedAssets"
    WITHOUT_SCHEDULE = "WithoutSchedule"
    WITHOUT_VENDOR = "WithoutVendor"
    WITHOUT_PRODUCT = "WithoutProduct"
    ADDED = "Added"
    MODIFIED = "Modified"
    DELETED = "Deleted"
    NO_AGREEMENT = "NoAgreement"
    EXPIRED_AGREEMENT = "ExpiredAgreement"
    AGREEMENT_UP_FOR_RENEWAL = "AgreementUpForRenewal"

    def __str__(self) -> str:
        return str(self.value)
