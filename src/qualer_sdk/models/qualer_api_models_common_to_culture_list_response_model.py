from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsCommonToCultureListResponseModel")


@_attrs_define
class QualerApiModelsCommonToCultureListResponseModel:
    """
    Attributes:
        culture_list (Union[Unset, list[str]]):
    """

    culture_list: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        culture_list: Union[Unset, list[str]] = UNSET
        if self.culture_list and not isinstance(self.culture_list, Unset):
            culture_list = self.culture_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if culture_list is not UNSET:
            field_dict["CultureList"] = culture_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        culture_list = cast(list[str], d.pop("CultureList", UNSET))

        qualer_api_models_common_to_culture_list_response_model = cls(
            culture_list=culture_list,
        )

        qualer_api_models_common_to_culture_list_response_model.additional_properties = (
            d
        )
        return qualer_api_models_common_to_culture_list_response_model

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
