from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsAssetPoolsToAssetPoolModel")


@_attrs_define
class QualerApiModelsAssetPoolsToAssetPoolModel:
    """
    Attributes:
        asset_pool_id (Union[None, Unset, int]):
        asset_pool_name (Union[None, Unset, str]):
    """

    asset_pool_id: Union[None, Unset, int] = UNSET
    asset_pool_name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_pool_id = self.asset_pool_id

        asset_pool_name = self.asset_pool_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_pool_id is not UNSET:
            field_dict["AssetPoolId"] = asset_pool_id
        if asset_pool_name is not UNSET:
            field_dict["AssetPoolName"] = asset_pool_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_pool_id = d.pop("AssetPoolId", UNSET)

        asset_pool_name = d.pop("AssetPoolName", UNSET)

        qualer_api_models_asset_pools_to_asset_pool_model = cls(
            asset_pool_id=asset_pool_id,
            asset_pool_name=asset_pool_name,
        )

        qualer_api_models_asset_pools_to_asset_pool_model.additional_properties = d
        return qualer_api_models_asset_pools_to_asset_pool_model

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
