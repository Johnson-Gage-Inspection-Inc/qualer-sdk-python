from enum import Enum


class QualerApiModelsAssetToAssetManageResponseModelResultStatus(int, Enum):
    NOTAVAILABLE = 0
    FAIL = 1
    PASS = 2
    FAILAMBIGUOUS = 10
    FAILSIGNIFICANT = 11
    PASSAMBIGUOUS = 20
    PASSADJUSTMENT = 21
    DONE = 22
    PENDING = 30
    MISSED = 31

    def __new__(cls, value):
        # Support both integer and string values for backward compatibility
        if isinstance(value, str):
            # Map string values to integers
            string_to_int = {
                "NotAvailable": 0,
                "Fail": 1,
                "Pass": 2,
                "FailAmbiguous": 10,
                "FailSignificant": 11,
                "PassAmbiguous": 20,
                "PassAdjustment": 21,
                "Done": 22,
                "Pending": 30,
                "Missed": 31,
            }
            if value in string_to_int:
                value = string_to_int[value]
            else:
                raise ValueError(f"'{value}' is not a valid {cls.__name__}")
        
        obj = int.__new__(cls, value)
        obj._value_ = value
        return obj

    def __str__(self) -> str:
        return str(self.value)
