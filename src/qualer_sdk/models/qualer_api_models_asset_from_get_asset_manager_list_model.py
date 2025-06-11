from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsAssetFromGetAssetManagerListModel")


@_attrs_define
class QualerApiModelsAssetFromGetAssetManagerListModel:
    """
    Attributes:
        filter_type (Union[Unset, str]):
        search_string (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
    """

    filter_type: Union[Unset, str] = UNSET
    search_string: Union[Unset, str] = UNSET
    page: Union[Unset, int] = UNSET
    page_size: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_type = self.filter_type

        search_string = self.search_string

        page = self.page

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_type is not UNSET:
            field_dict["FilterType"] = filter_type
        if search_string is not UNSET:
            field_dict["SearchString"] = search_string
        if page is not UNSET:
            field_dict["Page"] = page
        if page_size is not UNSET:
            field_dict["PageSize"] = page_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filter_type = d.pop("FilterType", UNSET)

        search_string = d.pop("SearchString", UNSET)

        page = d.pop("Page", UNSET)

        page_size = d.pop("PageSize", UNSET)

        qualer_api_models_asset_from_get_asset_manager_list_model = cls(
            filter_type=filter_type,
            search_string=search_string,
            page=page,
            page_size=page_size,
        )

        qualer_api_models_asset_from_get_asset_manager_list_model.additional_properties = (
            d
        )
        return qualer_api_models_asset_from_get_asset_manager_list_model

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
