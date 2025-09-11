from collections.abc import Mapping
from typing import Any, Dict, List, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QualerApiModelsClientsToClientCompanyResponseModelShippingAddressType0")


@_attrs_define
class QualerApiModelsClientsToClientCompanyResponseModelShippingAddressType0:
    """ """

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        qualer_api_models_clients_to_client_company_response_model_shipping_address_type_0 = cls()

        qualer_api_models_clients_to_client_company_response_model_shipping_address_type_0.additional_properties = (
            d
        )
        return qualer_api_models_clients_to_client_company_response_model_shipping_address_type_0

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
