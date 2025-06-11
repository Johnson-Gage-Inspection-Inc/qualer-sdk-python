from enum import Enum


class QualerApiModelsReportDatasetsToMeasurementResponseShipmentStatus(str, Enum):
    DELIVERED = "Delivered"
    NOTSHIPPED = "NotShipped"
    ONSITE = "OnSite"
    PARTIALSHIPMENT = "PartialShipment"
    SHIPPED = "Shipped"

    def __str__(self) -> str:
        return str(self.value)
