from enum import Enum


class ServiceOrdersFromChangeServiceOrderStatusModelServiceOrderStatus(str, Enum):
    CANCELLED = "Cancelled"
    CLOSED = "Closed"
    COMPLETED = "Completed"
    DELAYED = "Delayed"
    DELAYEDAPPROVAL = "DelayedApproval"
    DENIED = "Denied"
    DRAFT = "Draft"
    NEW = "New"
    PROCESSING = "Processing"
    QUALITYCONTROL = "QualityControl"
    READY = "Ready"
    SCHEDULING = "Scheduling"
    SUBMITTED = "Submitted"
    WAITINGFORAPPROVAL = "WaitingForApproval"
    WAITINGFORCLIENTSIGNOFF = "WaitingForClientSignOff"
    WAITINGFORVENDORSIGNOFF = "WaitingForVendorSignOff"

    def __str__(self) -> str:
        return str(self.value)
