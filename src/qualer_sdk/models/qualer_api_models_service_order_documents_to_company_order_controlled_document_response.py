from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.qualer_api_models_service_order_documents_to_company_order_controlled_document_response_document_type import (
    QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponseDocumentType,
)
from ..models.qualer_api_models_service_order_documents_to_company_order_controlled_document_response_report_type import (
    QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponseReportType,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponse",
)


@_attrs_define
class QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponse:
    """
    Attributes:
        service_order_id (Union[Unset, int]):
        guid (Union[Unset, UUID]):  Example: 00000000-0000-0000-0000-000000000000.
        document_name (Union[Unset, str]):
        file_name (Union[Unset, str]):
        document_type (Union[Unset,
            QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponseDocumentType]):
        revision_number (Union[Unset, int]):
        report_type (Union[Unset,
            QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponseReportType]):
        download_url (Union[Unset, str]):
    """

    service_order_id: Union[Unset, int] = UNSET
    guid: Union[Unset, UUID] = UNSET
    document_name: Union[Unset, str] = UNSET
    file_name: Union[Unset, str] = UNSET
    document_type: Union[
        Unset,
        QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponseDocumentType,
    ] = UNSET
    revision_number: Union[Unset, int] = UNSET
    report_type: Union[
        Unset,
        QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponseReportType,
    ] = UNSET
    download_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_order_id = self.service_order_id

        guid: Union[Unset, str] = UNSET
        if not isinstance(self.guid, Unset):
            guid = str(self.guid)

        document_name = self.document_name

        file_name = self.file_name

        document_type: Union[Unset, int] = UNSET
        if not isinstance(self.document_type, Unset):
            document_type = self.document_type.value

        revision_number = self.revision_number

        report_type: Union[Unset, int] = UNSET
        if not isinstance(self.report_type, Unset):
            report_type = self.report_type.value

        download_url = self.download_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_id is not UNSET:
            field_dict["ServiceOrderId"] = service_order_id
        if guid is not UNSET:
            field_dict["Guid"] = guid
        if document_name is not UNSET:
            field_dict["DocumentName"] = document_name
        if file_name is not UNSET:
            field_dict["FileName"] = file_name
        if document_type is not UNSET:
            field_dict["DocumentType"] = document_type
        if revision_number is not UNSET:
            field_dict["RevisionNumber"] = revision_number
        if report_type is not UNSET:
            field_dict["ReportType"] = report_type
        if download_url is not UNSET:
            field_dict["DownloadUrl"] = download_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_id = d.pop("ServiceOrderId", UNSET)

        _guid = d.pop("Guid", UNSET)
        guid: Union[Unset, UUID]
        if isinstance(_guid, Unset):
            guid = UNSET
        else:
            guid = UUID(_guid)

        document_name = d.pop("DocumentName", UNSET)

        file_name = d.pop("FileName", UNSET)

        _document_type = d.pop("DocumentType", UNSET)
        document_type: Union[
            Unset,
            QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponseDocumentType,
        ]
        if isinstance(_document_type, Unset):
            document_type = UNSET
        else:
            document_type = QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponseDocumentType(
                _document_type
            )

        revision_number = d.pop("RevisionNumber", UNSET)

        _report_type = d.pop("ReportType", UNSET)
        report_type: Union[
            Unset,
            QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponseReportType,
        ]
        if isinstance(_report_type, Unset):
            report_type = UNSET
        else:
            report_type = QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponseReportType(
                _report_type
            )

        download_url = d.pop("DownloadUrl", UNSET)

        qualer_api_models_service_order_documents_to_company_order_controlled_document_response = cls(
            service_order_id=service_order_id,
            guid=guid,
            document_name=document_name,
            file_name=file_name,
            document_type=document_type,
            revision_number=revision_number,
            report_type=report_type,
            download_url=download_url,
        )

        qualer_api_models_service_order_documents_to_company_order_controlled_document_response.additional_properties = (
            d
        )
        return qualer_api_models_service_order_documents_to_company_order_controlled_document_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
