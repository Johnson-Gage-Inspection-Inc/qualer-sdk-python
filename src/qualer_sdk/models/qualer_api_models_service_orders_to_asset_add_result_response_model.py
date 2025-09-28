from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServiceOrdersToAssetAddResultResponseModel")


@_attrs_define
class ServiceOrdersToAssetAddResultResponseModel:
    """
    Attributes:
        asset_count (Optional[int]):
        already_added_asset_serials (Optional[List[str]]):
    """

    asset_count: Optional[int] = None
    already_added_asset_serials: Optional[List[str]] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asset_count = self.asset_count
        already_added_asset_serials: Optional[List[str]] = None
        if self.already_added_asset_serials:
            already_added_asset_serials = self.already_added_asset_serials
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_count is not None:
            field_dict["AssetCount"] = asset_count
        if already_added_asset_serials is not None:
            field_dict["AlreadyAddedAssetSerials"] = already_added_asset_serials
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_count = d.pop("AssetCount", None)
        already_added_asset_serials = cast(List[str], d.pop("AlreadyAddedAssetSerials", None))
        qualer_api_models_service_orders_to_asset_add_result_response_model = cls(
            asset_count=asset_count,
            already_added_asset_serials=already_added_asset_serials,
        )
        qualer_api_models_service_orders_to_asset_add_result_response_model.additional_properties = (
            d
        )
        return qualer_api_models_service_orders_to_asset_add_result_response_model

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
