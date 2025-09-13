import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ReportDatasetsToCompanyCertificationResponse")


@_attrs_define
class ReportDatasetsToCompanyCertificationResponse:
    """
    Attributes:
        logo (Optional[str]):
        initial_date (Optional[datetime.datetime]):
        certification_date (Optional[datetime.datetime]):
        expiration_date (Optional[datetime.datetime]):
        certification_name (Optional[str]):
        certificate_number (Optional[str]):
        certification_authority (Optional[str]):
        certification_standard (Optional[str]):
    """

    logo: Optional[str] = None
    initial_date: Optional[datetime.datetime] = None
    certification_date: Optional[datetime.datetime] = None
    expiration_date: Optional[datetime.datetime] = None
    certification_name: Optional[str] = None
    certificate_number: Optional[str] = None
    certification_authority: Optional[str] = None
    certification_standard: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        logo = self.logo

        initial_date: Optional[str] = None
        if self.initial_date:
            initial_date = self.initial_date.isoformat()

        certification_date: Optional[str] = None
        if self.certification_date:
            certification_date = self.certification_date.isoformat()

        expiration_date: Optional[str] = None
        if self.expiration_date:
            expiration_date = self.expiration_date.isoformat()

        certification_name = self.certification_name

        certificate_number = self.certificate_number

        certification_authority = self.certification_authority

        certification_standard = self.certification_standard

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logo is not None:
            field_dict["Logo"] = logo
        if initial_date is not None:
            field_dict["InitialDate"] = initial_date
        if certification_date is not None:
            field_dict["CertificationDate"] = certification_date
        if expiration_date is not None:
            field_dict["ExpirationDate"] = expiration_date
        if certification_name is not None:
            field_dict["CertificationName"] = certification_name
        if certificate_number is not None:
            field_dict["CertificateNumber"] = certificate_number
        if certification_authority is not None:
            field_dict["CertificationAuthority"] = certification_authority
        if certification_standard is not None:
            field_dict["CertificationStandard"] = certification_standard

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        logo = d.pop("Logo", None)

        _initial_date = d.pop("InitialDate", None)
        initial_date: Optional[datetime.datetime]
        if not _initial_date:
            initial_date = None
        else:
            initial_date = isoparse(_initial_date)

        _certification_date = d.pop("CertificationDate", None)
        certification_date: Optional[datetime.datetime]
        if not _certification_date:
            certification_date = None
        else:
            certification_date = isoparse(_certification_date)

        _expiration_date = d.pop("ExpirationDate", None)
        expiration_date: Optional[datetime.datetime]
        if not _expiration_date:
            expiration_date = None
        else:
            expiration_date = isoparse(_expiration_date)

        certification_name = d.pop("CertificationName", None)

        certificate_number = d.pop("CertificateNumber", None)

        certification_authority = d.pop("CertificationAuthority", None)

        certification_standard = d.pop("CertificationStandard", None)

        qualer_api_models_report_datasets_to_company_certification_response = cls(
            logo=logo,
            initial_date=initial_date,
            certification_date=certification_date,
            expiration_date=expiration_date,
            certification_name=certification_name,
            certificate_number=certificate_number,
            certification_authority=certification_authority,
            certification_standard=certification_standard,
        )

        qualer_api_models_report_datasets_to_company_certification_response.additional_properties = (
            d
        )
        return qualer_api_models_report_datasets_to_company_certification_response

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
