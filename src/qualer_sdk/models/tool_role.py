from enum import Enum


class ToolRole(str, Enum):
    REFERENCE_STANDARD = "Reference Standard"
    ENVIRONMENTAL_SENSOR = "Environmental Sensor"
    CONTROLLED_ENVIRONMENT = "Controlled Environment"
    SCIENTIFIC_INSTRUMENT = "Scientific Instrument"

    def __str__(self) -> str:
        return str(self.value)
