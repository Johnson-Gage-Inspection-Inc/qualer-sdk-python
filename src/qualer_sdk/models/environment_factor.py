from enum import Enum


class EnvironmentFactor(str, Enum):
    AIRBUOYANCY = "AirBuoyancy"
    AIRHUMIDITY = "AirHumidity"
    ALTITUDE = "Altitude"
    AMBIENTTEMPERATURE = "AmbientTemperature"
    BAROMETRICPRESSURE = "BarometricPressure"
    EVAPORATIONRATE = "EvaporationRate"
    LIGHTINTENSITY = "LightIntensity"
    NOISELEVEL = "NoiseLevel"
    PHLEVEL = "PhLevel"
    SOLARRADIATION = "SolarRadiation"
    WATERCONDUCTIVITY = "WaterConductivity"
    WATERTEMPERATURE = "WaterTemperature"
    WINDSPEED = "WindSpeed"
    ZFACTOR = "ZFactor"

    def __str__(self) -> str:
        return str(self.value)
