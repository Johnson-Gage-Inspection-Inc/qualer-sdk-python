import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsReportDatasetsToCompanyCertificationResponse")


@_attrs_define
class QualerApiModelsReportDatasetsToCompanyCertificationResponse:
    """
    Attributes:
        logo (Union[Unset, str]):
        initial_date (Union[Unset, datetime.datetime]):
        certification_date (Union[Unset, datetime.datetime]):
        expiration_date (Union[Unset, datetime.datetime]):
        certification_name (Union[Unset, str]):
        certificate_number (Union[Unset, str]):
        certification_authority (Union[Unset, str]):
        certification_standard (Union[Unset, str]):
    """

    logo: Union[Unset, str] = UNSET
    initial_date: Union[Unset, datetime.datetime] = UNSET
    certification_date: Union[Unset, datetime.datetime] = UNSET
    expiration_date: Union[Unset, datetime.datetime] = UNSET
    certification_name: Union[Unset, str] = UNSET
    certificate_number: Union[Unset, str] = UNSET
    certification_authority: Union[Unset, str] = UNSET
    certification_standard: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logo = self.logo

        initial_date: Union[Unset, str] = UNSET
        if not isinstance(self.initial_date, Unset):
            initial_date = self.initial_date.isoformat()

        certification_date: Union[Unset, str] = UNSET
        if not isinstance(self.certification_date, Unset):
            certification_date = self.certification_date.isoformat()

        expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        certification_name = self.certification_name

        certificate_number = self.certificate_number

        certification_authority = self.certification_authority

        certification_standard = self.certification_standard

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logo is not UNSET:
            field_dict["Logo"] = logo
        if initial_date is not UNSET:
            field_dict["InitialDate"] = initial_date
        if certification_date is not UNSET:
            field_dict["CertificationDate"] = certification_date
        if expiration_date is not UNSET:
            field_dict["ExpirationDate"] = expiration_date
        if certification_name is not UNSET:
            field_dict["CertificationName"] = certification_name
        if certificate_number is not UNSET:
            field_dict["CertificateNumber"] = certificate_number
        if certification_authority is not UNSET:
            field_dict["CertificationAuthority"] = certification_authority
        if certification_standard is not UNSET:
            field_dict["CertificationStandard"] = certification_standard

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        logo = d.pop("Logo", UNSET)

        _initial_date = d.pop("InitialDate", UNSET)
        initial_date: Union[Unset, datetime.datetime]
        if isinstance(_initial_date, Unset):
            initial_date = UNSET
        else:
            initial_date = isoparse(_initial_date)

        _certification_date = d.pop("CertificationDate", UNSET)
        certification_date: Union[Unset, datetime.datetime]
        if isinstance(_certification_date, Unset):
            certification_date = UNSET
        else:
            certification_date = isoparse(_certification_date)

        _expiration_date = d.pop("ExpirationDate", UNSET)
        expiration_date: Union[Unset, datetime.datetime]
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date)

        certification_name = d.pop("CertificationName", UNSET)

        certificate_number = d.pop("CertificateNumber", UNSET)

        certification_authority = d.pop("CertificationAuthority", UNSET)

        certification_standard = d.pop("CertificationStandard", UNSET)

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
