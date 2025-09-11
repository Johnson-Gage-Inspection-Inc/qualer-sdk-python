from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QualerWebMvcAreasApiModelsCompanyFromAddDepartmentModel")


@_attrs_define
class QualerWebMvcAreasApiModelsCompanyFromAddDepartmentModel:
    """
    Attributes:
        name (Optional[str]):
        description (Optional[str]):
    """

    name: Optional[str] = None
    description: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not None:
            field_dict["Name"] = name
        if description is not None:
            field_dict["Description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("Name", None)

        description = d.pop("Description", None)

        qualer_web_mvc_areas_api_models_company_from_add_department_model = cls(
            name=name,
            description=description,
        )

        qualer_web_mvc_areas_api_models_company_from_add_department_model.additional_properties = d
        return qualer_web_mvc_areas_api_models_company_from_add_department_model

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
