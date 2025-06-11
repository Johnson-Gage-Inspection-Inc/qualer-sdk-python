from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsServiceOptionsToServiceOptionResponseModel")


@_attrs_define
class QualerApiModelsServiceOptionsToServiceOptionResponseModel:
    """
    Attributes:
        name (Union[Unset, str]):
        price (Union[Unset, float]):
        service_charge (Union[Unset, float]):
        time_spent (Union[Unset, float]):
        is_hourly (Union[Unset, bool]):
        document_number (Union[Unset, str]):
        document_section (Union[Unset, str]):
        service_code (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    price: Union[Unset, float] = UNSET
    service_charge: Union[Unset, float] = UNSET
    time_spent: Union[Unset, float] = UNSET
    is_hourly: Union[Unset, bool] = UNSET
    document_number: Union[Unset, str] = UNSET
    document_section: Union[Unset, str] = UNSET
    service_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        price = self.price

        service_charge = self.service_charge

        time_spent = self.time_spent

        is_hourly = self.is_hourly

        document_number = self.document_number

        document_section = self.document_section

        service_code = self.service_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if price is not UNSET:
            field_dict["Price"] = price
        if service_charge is not UNSET:
            field_dict["ServiceCharge"] = service_charge
        if time_spent is not UNSET:
            field_dict["TimeSpent"] = time_spent
        if is_hourly is not UNSET:
            field_dict["IsHourly"] = is_hourly
        if document_number is not UNSET:
            field_dict["DocumentNumber"] = document_number
        if document_section is not UNSET:
            field_dict["DocumentSection"] = document_section
        if service_code is not UNSET:
            field_dict["ServiceCode"] = service_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("Name", UNSET)

        price = d.pop("Price", UNSET)

        service_charge = d.pop("ServiceCharge", UNSET)

        time_spent = d.pop("TimeSpent", UNSET)

        is_hourly = d.pop("IsHourly", UNSET)

        document_number = d.pop("DocumentNumber", UNSET)

        document_section = d.pop("DocumentSection", UNSET)

        service_code = d.pop("ServiceCode", UNSET)

        qualer_api_models_service_options_to_service_option_response_model = cls(
            name=name,
            price=price,
            service_charge=service_charge,
            time_spent=time_spent,
            is_hourly=is_hourly,
            document_number=document_number,
            document_section=document_section,
            service_code=service_code,
        )

        qualer_api_models_service_options_to_service_option_response_model.additional_properties = (
            d
        )
        return qualer_api_models_service_options_to_service_option_response_model

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
