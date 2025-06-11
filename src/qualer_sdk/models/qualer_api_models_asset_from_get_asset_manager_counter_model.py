from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsAssetFromGetAssetManagerCounterModel")


@_attrs_define
class QualerApiModelsAssetFromGetAssetManagerCounterModel:
    """
    Attributes:
        search_string (Union[Unset, str]):
    """

    search_string: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        search_string = self.search_string

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if search_string is not UNSET:
            field_dict["SearchString"] = search_string

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        search_string = d.pop("SearchString", UNSET)

        qualer_api_models_asset_from_get_asset_manager_counter_model = cls(
            search_string=search_string,
        )

        qualer_api_models_asset_from_get_asset_manager_counter_model.additional_properties = (
            d
        )
        return qualer_api_models_asset_from_get_asset_manager_counter_model

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
