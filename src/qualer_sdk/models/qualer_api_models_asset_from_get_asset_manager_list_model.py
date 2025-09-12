from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QualerApiModelsAssetFromGetAssetManagerListModel")


@_attrs_define
class QualerApiModelsAssetFromGetAssetManagerListModel:
    """
    Attributes:
        filter_type (Optional[str]):
        search_string (Optional[str]):
        page (Optional[int]):
        page_size (Optional[int]):
    """

    filter_type: Optional[str] = None
    search_string: Optional[str] = None
    page: Optional[int] = None
    page_size: Optional[int] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filter_type = self.filter_type

        search_string = self.search_string

        page = self.page

        page_size = self.page_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_type is not None:
            field_dict["FilterType"] = filter_type
        if search_string is not None:
            field_dict["SearchString"] = search_string
        if page is not None:
            field_dict["Page"] = page
        if page_size is not None:
            field_dict["PageSize"] = page_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filter_type = d.pop("FilterType", None)

        search_string = d.pop("SearchString", None)

        page = d.pop("Page", None)

        page_size = d.pop("PageSize", None)

        qualer_api_models_asset_from_get_asset_manager_list_model = cls(
            filter_type=filter_type,
            search_string=search_string,
            page=page,
            page_size=page_size,
        )

        qualer_api_models_asset_from_get_asset_manager_list_model.additional_properties = d
        return qualer_api_models_asset_from_get_asset_manager_list_model

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
