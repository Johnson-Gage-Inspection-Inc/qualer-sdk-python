from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EmployeesFromEmployeeDepartmentModel")


@_attrs_define
class EmployeesFromEmployeeDepartmentModel:
    """
    Attributes:
        department_id (Optional[int]):
        position (Optional[str]):
    """

    department_id: Optional[int] = None
    position: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        department_id = self.department_id

        position = self.position

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if department_id is not None:
            field_dict["DepartmentId"] = department_id
        if position is not None:
            field_dict["Position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        department_id = d.pop("DepartmentId", None)

        position = d.pop("Position", None)

        qualer_api_models_employees_from_employee_department_model = cls(
            department_id=department_id,
            position=position,
        )

        qualer_api_models_employees_from_employee_department_model.additional_properties = d
        return qualer_api_models_employees_from_employee_department_model

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
