from enum import Enum


class ElementPage(str, Enum):
    ASSETMANAGER = "AssetManager"
    CLIENTAGREEMENTS = "ClientAgreements"
    CLIENTASSETMANAGER = "ClientAssetManager"
    CLIENTS = "Clients"
    DOCUMENTMANAGER = "DocumentManager"
    GLOBALASSETMANAGER = "GlobalAssetManager"
    INVENTORYMANAGER = "InventoryManager"
    INVOICESMANAGER = "InvoicesManager"
    PRODUCTMANAGER = "ProductManager"
    PRODUCTSPECIFICATIONS = "ProductSpecifications"
    SERVICEORDERITEMS = "ServiceOrderItems"
    SERVICEREQUESTS = "ServiceRequests"
    SERVICESCHEDULES = "ServiceSchedules"
    TAXONOMY = "Taxonomy"
    VENDORAGREEMENTS = "VendorAgreements"
    VENDORS = "Vendors"
    WORKCALENDAR = "WorkCalendar"
    WORKORDERS = "WorkOrders"

    def __str__(self) -> str:
        return str(self.value)
