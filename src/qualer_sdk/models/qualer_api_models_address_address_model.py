from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AddressAddressModel")


@_attrs_define
class AddressAddressModel:
    """
    Attributes:
        first_name (Optional[str]):
        last_name (Optional[str]):
        email (Optional[str]):
        company (Optional[str]):
        city (Optional[str]):
        address_1 (Optional[str]):
        address_2 (Optional[str]):
        zip_postal_code (Optional[str]):
        phone_number (Optional[str]):
        fax_number (Optional[str]):
        attention_1 (Optional[str]):
        attention_2 (Optional[str]):
        country (Optional[str]):
        state_province (Optional[str]):
        state_province_abbreviation (Optional[str]):
    """

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    company: Optional[str] = None
    city: Optional[str] = None
    address_1: Optional[str] = None
    address_2: Optional[str] = None
    zip_postal_code: Optional[str] = None
    phone_number: Optional[str] = None
    fax_number: Optional[str] = None
    attention_1: Optional[str] = None
    attention_2: Optional[str] = None
    country: Optional[str] = None
    state_province: Optional[str] = None
    state_province_abbreviation: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not None:
            field_dict["FirstName"] = first_name
        if last_name is not None:
            field_dict["LastName"] = last_name
        if email is not None:
            field_dict["Email"] = email
        if company is not None:
            field_dict["Company"] = company
        if city is not None:
            field_dict["City"] = city
        if address_1 is not None:
            field_dict["Address1"] = address_1
        if address_2 is not None:
            field_dict["Address2"] = address_2
        if zip_postal_code is not None:
            field_dict["ZipPostalCode"] = zip_postal_code
        if phone_number is not None:
            field_dict["PhoneNumber"] = phone_number
        if fax_number is not None:
            field_dict["FaxNumber"] = fax_number
        if attention_1 is not None:
            field_dict["Attention1"] = attention_1
        if attention_2 is not None:
            field_dict["Attention2"] = attention_2
        if country is not None:
            field_dict["Country"] = country
        if state_province is not None:
            field_dict["StateProvince"] = state_province
        if state_province_abbreviation is not None:
            field_dict["StateProvinceAbbreviation"] = state_province_abbreviation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        first_name = d.pop("FirstName", None)

        last_name = d.pop("LastName", None)

        email = d.pop("Email", None)

        company = d.pop("Company", None)

        city = d.pop("City", None)

        address_1 = d.pop("Address1", None)

        address_2 = d.pop("Address2", None)

        zip_postal_code = d.pop("ZipPostalCode", None)

        phone_number = d.pop("PhoneNumber", None)

        fax_number = d.pop("FaxNumber", None)

        attention_1 = d.pop("Attention1", None)

        attention_2 = d.pop("Attention2", None)

        country = d.pop("Country", None)

        state_province = d.pop("StateProvince", None)

        state_province_abbreviation = d.pop("StateProvinceAbbreviation", None)

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
