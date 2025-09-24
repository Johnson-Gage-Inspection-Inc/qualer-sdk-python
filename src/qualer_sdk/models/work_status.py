# src/qualer_sdk/models/work_status.py
from __future__ import annotations

from .api_enum import ApiEnum


class WorkStatus(ApiEnum):
    PENDING = "Pending"
    INPROGRESS = "InProgress"
    COMPLETED = "Completed"
    DELAYED = "Delayed"
    WITHDRAWN = "Withdrawn"
    LOCKED = "Locked"
    NEW = "New"
    CLOSED = "Closed"
    WAIT = "Wait"
