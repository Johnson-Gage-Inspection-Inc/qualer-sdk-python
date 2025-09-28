from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ClientsFromClientEmployeeModel")


@_attrs_define
class ClientsFromClientEmployeeModel:
    """
    Attributes:
        employee_id (Optional[int]):
    """

    employee_id: Optional[int] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        employee_id = self.employee_id
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if employee_id is not None:
            field_dict["EmployeeId"] = employee_id
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        employee_id = d.pop("EmployeeId", None)
        qualer_api_models_clients_from_client_employee_model = cls(
            employee_id=employee_id,
        )
        qualer_api_models_clients_from_client_employee_model.additional_properties = d
        return qualer_api_models_clients_from_client_employee_model

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
