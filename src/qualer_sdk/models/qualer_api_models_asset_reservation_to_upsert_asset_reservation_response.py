from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AssetReservationToUpsertAssetReservationResponse")


@_attrs_define
class AssetReservationToUpsertAssetReservationResponse:
    """
    Attributes:
        asset_reservation_id (Optional[int]):
    """

    asset_reservation_id: Optional[int] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asset_reservation_id = self.asset_reservation_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_reservation_id is not None:
            field_dict["AssetReservationId"] = asset_reservation_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_reservation_id = d.pop("AssetReservationId", None)

        qualer_api_models_asset_reservation_to_upsert_asset_reservation_response = cls(
            asset_reservation_id=asset_reservation_id,
        )

        qualer_api_models_asset_reservation_to_upsert_asset_reservation_response.additional_properties = (
            d
        )
        return qualer_api_models_asset_reservation_to_upsert_asset_reservation_response

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
