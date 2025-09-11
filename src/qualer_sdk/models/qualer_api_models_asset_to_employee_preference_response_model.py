from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QualerApiModelsAssetToEmployeePreferenceResponseModel")


@_attrs_define
class QualerApiModelsAssetToEmployeePreferenceResponseModel:
    """
    Attributes:
        element_type (Optional[str]):
        element_page (Optional[str]):
        element_id (Optional[str]):
        preference (Optional[List[str]]):
        is_pinned (Optional[bool]):
    """

    element_type: Optional[str] = None
    element_page: Optional[str] = None
    element_id: Optional[str] = None
    preference: Optional[List[str]] = None
    is_pinned: Optional[bool] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        element_type = self.element_type

        element_page = self.element_page

        element_id = self.element_id

        preference: Optional[List[str]] = None
        if self.preference:
            preference = self.preference

        is_pinned = self.is_pinned

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if element_type is not None:
            field_dict["ElementType"] = element_type
        if element_page is not None:
            field_dict["ElementPage"] = element_page
        if element_id is not None:
            field_dict["ElementId"] = element_id
        if preference is not None:
            field_dict["Preference"] = preference
        if is_pinned is not None:
            field_dict["IsPinned"] = is_pinned

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        element_type = d.pop("ElementType", None)

        element_page = d.pop("ElementPage", None)

        element_id = d.pop("ElementId", None)

        preference = cast(List[str], d.pop("Preference", None))

        is_pinned = d.pop("IsPinned", None)

        qualer_api_models_asset_to_employee_preference_response_model = cls(
            element_type=element_type,
            element_page=element_page,
            element_id=element_id,
            preference=preference,
            is_pinned=is_pinned,
        )

        qualer_api_models_asset_to_employee_preference_response_model.additional_properties = d
        return qualer_api_models_asset_to_employee_preference_response_model

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
