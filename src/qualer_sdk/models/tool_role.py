from enum import IntEnum


class ToolRole(IntEnum):
    REFERENCE_STANDARD = 0
    ENVIRONMENTAL_SENSOR = 1
    CONTROLLED_ENVIRONMENT = 2
    SCIENTIFIC_INSTRUMENT = 3

    def __str__(self) -> str:
        return str(self.value)
