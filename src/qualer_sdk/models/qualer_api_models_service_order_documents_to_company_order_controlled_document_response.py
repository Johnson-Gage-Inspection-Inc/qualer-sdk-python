from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.qualer_api_models_service_order_documents_to_company_order_controlled_document_response_document_type import (
    ServiceOrderDocumentsToCompanyOrderControlledDocumentResponseDocumentType,
)
from ..models.report_type import ReportType

T = TypeVar(
    "T",
    bound="ServiceOrderDocumentsToCompanyOrderControlledDocumentResponse",
)


@_attrs_define
class ServiceOrderDocumentsToCompanyOrderControlledDocumentResponse:
    """
    Attributes:
        service_order_id (Optional[int]):
        guid (Optional[UUID]):  Example: 00000000-0000-0000-0000-000000000000.
        document_name (Optional[str]):
        file_name (Optional[str]):
        document_type (Optional[ServiceOrderDocumentsToCompanyOrderControlledDocumentResponseDocumentType]):
        revision_number (Optional[int]):
        report_type (Optional[ReportType]):
        download_url (Optional[str]):
    """

    service_order_id: Optional[int] = None
    guid: Optional[UUID] = None
    document_name: Optional[str] = None
    file_name: Optional[str] = None
    document_type: Optional[
        ServiceOrderDocumentsToCompanyOrderControlledDocumentResponseDocumentType
    ] = None
    revision_number: Optional[int] = None
    report_type: Optional[ReportType] = None
    download_url: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_order_id = self.service_order_id

        guid: Optional[str] = None
        if self.guid:
            guid = str(self.guid)

        document_name = self.document_name

        file_name = self.file_name

        document_type: Optional[int] = None
        if self.document_type:
            document_type = self.document_type.value

        revision_number = self.revision_number

        report_type: Optional[int] = None
        if self.report_type:
            report_type = self.report_type.value

        download_url = self.download_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_id is not None:
            field_dict["ServiceOrderId"] = service_order_id
        if guid is not None:
            field_dict["Guid"] = guid
        if document_name is not None:
            field_dict["DocumentName"] = document_name
        if file_name is not None:
            field_dict["FileName"] = file_name
        if document_type is not None:
            field_dict["DocumentType"] = document_type
        if revision_number is not None:
            field_dict["RevisionNumber"] = revision_number
        if report_type is not None:
            field_dict["ReportType"] = report_type
        if download_url is not None:
            field_dict["DownloadUrl"] = download_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_id = d.pop("ServiceOrderId", None)

        _guid = d.pop("Guid", None)
        guid: Optional[UUID]
        if not _guid:
            guid = None
        else:
            guid = UUID(_guid)

        document_name = d.pop("DocumentName", None)

        file_name = d.pop("FileName", None)

        _document_type = d.pop("DocumentType", None)
        document_type: Optional[
            ServiceOrderDocumentsToCompanyOrderControlledDocumentResponseDocumentType
        ]
        if not _document_type:
            document_type = None
        else:
            document_type = (
                ServiceOrderDocumentsToCompanyOrderControlledDocumentResponseDocumentType(
                    _document_type
                )
            )

        revision_number = d.pop("RevisionNumber", None)

        _report_type = d.pop("ReportType", None)
        report_type: Optional[ReportType]
        if not _report_type:
            report_type = None
        else:
            report_type = ReportType(_report_type)

        download_url = d.pop("DownloadUrl", None)

        qualer_api_models_service_order_documents_to_company_order_controlled_document_response = (
            cls(
                service_order_id=service_order_id,
                guid=guid,
                document_name=document_name,
                file_name=file_name,
                document_type=document_type,
                revision_number=revision_number,
                report_type=report_type,
                download_url=download_url,
            )
        )

        qualer_api_models_service_order_documents_to_company_order_controlled_document_response.additional_properties = (
            d
        )
        return (
            qualer_api_models_service_order_documents_to_company_order_controlled_document_response
        )

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
