from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsAssetFromUpdateRoomModel")


@_attrs_define
class QualerApiModelsAssetFromUpdateRoomModel:
    """
    Attributes:
        room (Union[Unset, str]):
        tracking_id (Union[Unset, str]):
    """

    room: Union[Unset, str] = UNSET
    tracking_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        room = self.room

        tracking_id = self.tracking_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if room is not UNSET:
            field_dict["Room"] = room
        if tracking_id is not UNSET:
            field_dict["TrackingId"] = tracking_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        room = d.pop("Room", UNSET)

        tracking_id = d.pop("TrackingId", UNSET)

        qualer_api_models_asset_from_update_room_model = cls(
            room=room,
            tracking_id=tracking_id,
        )

        qualer_api_models_asset_from_update_room_model.additional_properties = d
        return qualer_api_models_asset_from_update_room_model

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
