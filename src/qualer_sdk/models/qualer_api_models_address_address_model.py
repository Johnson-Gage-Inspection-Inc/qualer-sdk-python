from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsAddressAddressModel")


@_attrs_define
class QualerApiModelsAddressAddressModel:
    """
    Attributes:
        first_name (Union[None, Unset, str]):
        last_name (Union[None, Unset, str]):
        email (Union[None, Unset, str]):
        company (Union[None, Unset, str]):
        city (Union[None, Unset, str]):
        address_1 (Union[None, Unset, str]):
        address_2 (Union[None, Unset, str]):
        zip_postal_code (Union[None, Unset, str]):
        phone_number (Union[None, Unset, str]):
        fax_number (Union[None, Unset, str]):
        attention_1 (Union[None, Unset, str]):
        attention_2 (Union[None, Unset, str]):
        country (Union[None, Unset, str]):
        state_province (Union[None, Unset, str]):
        state_province_abbreviation (Union[None, Unset, str]):
    """

    first_name: Union[None, Unset, str] = UNSET
    last_name: Union[None, Unset, str] = UNSET
    email: Union[None, Unset, str] = UNSET
    company: Union[None, Unset, str] = UNSET
    city: Union[None, Unset, str] = UNSET
    address_1: Union[None, Unset, str] = UNSET
    address_2: Union[None, Unset, str] = UNSET
    zip_postal_code: Union[None, Unset, str] = UNSET
    phone_number: Union[None, Unset, str] = UNSET
    fax_number: Union[None, Unset, str] = UNSET
    attention_1: Union[None, Unset, str] = UNSET
    attention_2: Union[None, Unset, str] = UNSET
    country: Union[None, Unset, str] = UNSET
    state_province: Union[None, Unset, str] = UNSET
    state_province_abbreviation: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        email = self.email

        company = self.company

        city = self.city

        address_1 = self.address_1

        address_2 = self.address_2

        zip_postal_code = self.zip_postal_code

        phone_number = self.phone_number

        fax_number = self.fax_number

        attention_1 = self.attention_1

        attention_2 = self.attention_2

        country = self.country

        state_province = self.state_province

        state_province_abbreviation = self.state_province_abbreviation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["FirstName"] = first_name
        if last_name is not UNSET:
            field_dict["LastName"] = last_name
        if email is not UNSET:
            field_dict["Email"] = email
        if company is not UNSET:
            field_dict["Company"] = company
        if city is not UNSET:
            field_dict["City"] = city
        if address_1 is not UNSET:
            field_dict["Address1"] = address_1
        if address_2 is not UNSET:
            field_dict["Address2"] = address_2
        if zip_postal_code is not UNSET:
            field_dict["ZipPostalCode"] = zip_postal_code
        if phone_number is not UNSET:
            field_dict["PhoneNumber"] = phone_number
        if fax_number is not UNSET:
            field_dict["FaxNumber"] = fax_number
        if attention_1 is not UNSET:
            field_dict["Attention1"] = attention_1
        if attention_2 is not UNSET:
            field_dict["Attention2"] = attention_2
        if country is not UNSET:
            field_dict["Country"] = country
        if state_province is not UNSET:
            field_dict["StateProvince"] = state_province
        if state_province_abbreviation is not UNSET:
            field_dict["StateProvinceAbbreviation"] = state_province_abbreviation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        first_name = d.pop("FirstName", UNSET)

        last_name = d.pop("LastName", UNSET)

        email = d.pop("Email", UNSET)

        company = d.pop("Company", UNSET)

        city = d.pop("City", UNSET)

        address_1 = d.pop("Address1", UNSET)

        address_2 = d.pop("Address2", UNSET)

        zip_postal_code = d.pop("ZipPostalCode", UNSET)

        phone_number = d.pop("PhoneNumber", UNSET)

        fax_number = d.pop("FaxNumber", UNSET)

        attention_1 = d.pop("Attention1", UNSET)

        attention_2 = d.pop("Attention2", UNSET)

        country = d.pop("Country", UNSET)

        state_province = d.pop("StateProvince", UNSET)

        state_province_abbreviation = d.pop("StateProvinceAbbreviation", UNSET)

        qualer_api_models_address_address_model = cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
            company=company,
            city=city,
            address_1=address_1,
            address_2=address_2,
            zip_postal_code=zip_postal_code,
            phone_number=phone_number,
            fax_number=fax_number,
            attention_1=attention_1,
            attention_2=attention_2,
            country=country,
            state_province=state_province,
            state_province_abbreviation=state_province_abbreviation,
        )

        qualer_api_models_address_address_model.additional_properties = d
        return qualer_api_models_address_address_model

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
