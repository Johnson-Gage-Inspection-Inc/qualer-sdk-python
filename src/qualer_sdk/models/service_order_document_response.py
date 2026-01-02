from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models import (  # noqa: E501
    ServiceOrderDocumentsToCompanyOrderControlledDocumentResponseDocumentType as DocumentType,  # noqa: E501
)
from ..models.report_type import ReportType

T = TypeVar("T", bound="ServiceOrderDocumentResponse")


@_attrs_define
class ServiceOrderDocumentResponse:
    """
    Unified response model for service order documents, supporting both
    order-level and item-level documents.

    Attributes:
        service_order_id (int): The service order ID.
        guid (UUID): Unique identifier for the document.
            Example: 00000000-0000-0000-0000-000000000000.
        document_name (str): Name of the document.
        file_name (str): File name of the document.
        document_type (DocumentType): Type of the document.
        revision_number (int): Revision number of the document.
        report_type (ReportType): Type of report.
        download_url (str): URL to download the document.
        service_order_item_id (Optional[int]): The service order item ID
            (optional, for item-level documents).
    """

    service_order_id: int
    guid: UUID
    document_name: str
    file_name: str
    document_type: DocumentType
    revision_number: int
    report_type: ReportType
    download_url: str
    service_order_item_id: Optional[int] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_order_id = self.service_order_id
        guid = str(self.guid)
        document_name = self.document_name
        file_name = self.file_name
        document_type = self.document_type.value
        revision_number = self.revision_number
        report_type = self.report_type.value
        download_url = self.download_url
        service_order_item_id = self.service_order_item_id
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        field_dict["ServiceOrderId"] = service_order_id
        field_dict["Guid"] = guid
        field_dict["DocumentName"] = document_name
        field_dict["FileName"] = file_name
        field_dict["DocumentType"] = document_type
        field_dict["RevisionNumber"] = revision_number
        field_dict["ReportType"] = report_type
        field_dict["DownloadUrl"] = download_url
        if service_order_item_id is not None:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_id = d.pop("ServiceOrderId")
        _guid = d.pop("Guid")
        guid = UUID(_guid)
        document_name = d.pop("DocumentName")
        file_name = d.pop("FileName")
        _document_type = d.pop("DocumentType")
        document_type = DocumentType(_document_type)
        revision_number = d.pop("RevisionNumber")
        _report_type = d.pop("ReportType")
        report_type = ReportType(_report_type)
        download_url = d.pop("DownloadUrl")
        service_order_item_id = d.pop("ServiceOrderItemId", None)
        obj = cls(
            service_order_id=service_order_id,
            guid=guid,
            document_name=document_name,
            file_name=file_name,
            document_type=document_type,
            revision_number=revision_number,
            report_type=report_type,
            download_url=download_url,
            service_order_item_id=service_order_item_id,
        )
        obj.additional_properties = d
        return obj

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
