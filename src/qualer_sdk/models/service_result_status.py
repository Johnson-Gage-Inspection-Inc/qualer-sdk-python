# src/qualer_sdk/models/service_result_status.py
from __future__ import annotations

from .api_enum import ApiEnum


class ServiceResultStatus(ApiEnum):

    DONE = "Done"
    FAIL = "Fail"
    FAILAMBIGUOUS = "FailAmbiguous"
    FAILSIGNIFICANT = "FailSignificant"
    MISSED = "Missed"
    NOTAVAILABLE = "NotAvailable"
    PASS = "Pass"
    PASSADJUSTMENT = "PassAdjustment"
    PASSAMBIGUOUS = "PassAmbiguous"
    PENDING = "Pending"


# ApiEnum will use this mapping for __int__ and tolerant construction
ServiceResultStatus.INT_CODES = {  # type: ignore[attr-defined]
    0: ServiceResultStatus.DONE,
    1: ServiceResultStatus.FAIL,
    2: ServiceResultStatus.MISSED,
    10: ServiceResultStatus.FAILAMBIGUOUS,
    11: ServiceResultStatus.FAILSIGNIFICANT,
    20: ServiceResultStatus.NOTAVAILABLE,
    21: ServiceResultStatus.PASS,
    22: ServiceResultStatus.PASSADJUSTMENT,
    30: ServiceResultStatus.PASSAMBIGUOUS,
    31: ServiceResultStatus.PENDING,
}
