from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsAssetToEmployeePreferenceResponseModel")


@_attrs_define
class QualerApiModelsAssetToEmployeePreferenceResponseModel:
    """
    Attributes:
        element_type (Union[None, Unset, str]):
        element_page (Union[None, Unset, str]):
        element_id (Union[None, Unset, str]):
        preference (Union[None, Unset, list[str]]):
        is_pinned (Union[None, Unset, bool]):
    """

    element_type: Union[None, Unset, str] = UNSET
    element_page: Union[None, Unset, str] = UNSET
    element_id: Union[None, Unset, str] = UNSET
    preference: Union[None, Unset, list[str]] = UNSET
    is_pinned: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        element_type = self.element_type

        element_page = self.element_page

        element_id = self.element_id

        preference: Union[None, Unset, list[str]] = UNSET
        if self.preference and not isinstance(self.preference, Unset):
            preference = self.preference

        is_pinned = self.is_pinned

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if element_type is not UNSET:
            field_dict["ElementType"] = element_type
        if element_page is not UNSET:
            field_dict["ElementPage"] = element_page
        if element_id is not UNSET:
            field_dict["ElementId"] = element_id
        if preference is not UNSET:
            field_dict["Preference"] = preference
        if is_pinned is not UNSET:
            field_dict["IsPinned"] = is_pinned

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        element_type = d.pop("ElementType", UNSET)

        element_page = d.pop("ElementPage", UNSET)

        element_id = d.pop("ElementId", UNSET)

        preference = cast(list[str], d.pop("Preference", UNSET))

        is_pinned = d.pop("IsPinned", UNSET)

        qualer_api_models_asset_to_employee_preference_response_model = cls(
            element_type=element_type,
            element_page=element_page,
            element_id=element_id,
            preference=preference,
            is_pinned=is_pinned,
        )

        qualer_api_models_asset_to_employee_preference_response_model.additional_properties = (
            d
        )
        return qualer_api_models_asset_to_employee_preference_response_model

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
