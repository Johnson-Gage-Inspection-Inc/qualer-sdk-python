from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServiceOptionsToServiceOptionResponseModel")


@_attrs_define
class ServiceOptionsToServiceOptionResponseModel:
    """
    Attributes:
        name (Optional[str]):
        price (Optional[float]):
        service_charge (Optional[float]):
        time_spent (Optional[float]):
        is_hourly (Optional[bool]):
        document_number (Optional[str]):
        document_section (Optional[str]):
        service_code (Optional[str]):
    """

    name: Optional[str] = None
    price: Optional[float] = None
    service_charge: Optional[float] = None
    time_spent: Optional[float] = None
    is_hourly: Optional[bool] = None
    document_number: Optional[str] = None
    document_section: Optional[str] = None
    service_code: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        price = self.price
        service_charge = self.service_charge
        time_spent = self.time_spent
        is_hourly = self.is_hourly
        document_number = self.document_number
        document_section = self.document_section
        service_code = self.service_code
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not None:
            field_dict["Name"] = name
        if price is not None:
            field_dict["Price"] = price
        if service_charge is not None:
            field_dict["ServiceCharge"] = service_charge
        if time_spent is not None:
            field_dict["TimeSpent"] = time_spent
        if is_hourly is not None:
            field_dict["IsHourly"] = is_hourly
        if document_number is not None:
            field_dict["DocumentNumber"] = document_number
        if document_section is not None:
            field_dict["DocumentSection"] = document_section
        if service_code is not None:
            field_dict["ServiceCode"] = service_code
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("Name", None)
        price = d.pop("Price", None)
        service_charge = d.pop("ServiceCharge", None)
        time_spent = d.pop("TimeSpent", None)
        is_hourly = d.pop("IsHourly", None)
        document_number = d.pop("DocumentNumber", None)
        document_section = d.pop("DocumentSection", None)
        service_code = d.pop("ServiceCode", None)
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
        qualer_api_models_service_options_to_service_option_response_model.additional_properties = d
        return qualer_api_models_service_options_to_service_option_response_model

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
