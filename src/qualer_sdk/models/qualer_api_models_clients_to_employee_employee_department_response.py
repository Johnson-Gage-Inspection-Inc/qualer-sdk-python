from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ClientsToEmployeeEmployeeDepartmentResponse")


@_attrs_define
class ClientsToEmployeeEmployeeDepartmentResponse:
    """
    Attributes:
        id (Optional[int]):
        name (Optional[str]):
        position (Optional[str]):
    """

    id: Optional[int] = None
    name: Optional[str] = None
    position: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        position = self.position

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not None:
            field_dict["Id"] = id
        if name is not None:
            field_dict["Name"] = name
        if position is not None:
            field_dict["Position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("Id", None)

        name = d.pop("Name", None)

        position = d.pop("Position", None)

        qualer_api_models_clients_to_employee_employee_department_response = cls(
            id=id,
            name=name,
            position=position,
        )

        qualer_api_models_clients_to_employee_employee_department_response.additional_properties = d
        return qualer_api_models_clients_to_employee_employee_department_response

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
