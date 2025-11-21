from enum import Enum


class ToolRole(str, Enum):
    REFERENCE_STANDARD = "Reference Standard"
    ENVIRONMENTAL_SENSOR = "Environmental Sensor"
    CONTROLLED_ENVIRONMENT = "Controlled Environment"
    SCIENTIFIC_INSTRUMENT = "Scientific Instrument"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value):
        """Handle integer to string mapping for API responses."""
        if isinstance(value, int):
            _int_to_str_map = {
                0: "Reference Standard",
                1: "Environmental Sensor",
                2: "Controlled Environment",
                3: "Scientific Instrument",
            }
            if value in _int_to_str_map:
                return cls(_int_to_str_map[value])
        return super()._missing_(value)
