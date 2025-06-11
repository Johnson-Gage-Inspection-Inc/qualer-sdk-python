from enum import Enum


class QualerApiModelsReportDatasetsToServiceOrderItemFieldResponseType(str, Enum):
    BOOLEAN = "Boolean"
    DATE = "Date"
    DATETIME = "DateTime"
    DOUBLE = "Double"
    INT = "Int"
    LIST = "List"
    STRING = "String"
    TEXT = "Text"
    VALUELOOKUP = "ValueLookup"

    def __str__(self) -> str:
        return str(self.value)
