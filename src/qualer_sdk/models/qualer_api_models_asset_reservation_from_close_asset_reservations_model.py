from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsAssetReservationFromCloseAssetReservationsModel")


@_attrs_define
class QualerApiModelsAssetReservationFromCloseAssetReservationsModel:
    """
    Attributes:
        asset_id (Union[Unset, int]):
        area_id (Union[Unset, int]):
        product_id (Union[Unset, int]):
        serial_number (Union[Unset, str]):
        asset_tag (Union[Unset, str]):
        reservation_id (Union[Unset, int]):
    """

    asset_id: Union[Unset, int] = UNSET
    area_id: Union[Unset, int] = UNSET
    product_id: Union[Unset, int] = UNSET
    serial_number: Union[Unset, str] = UNSET
    asset_tag: Union[Unset, str] = UNSET
    reservation_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        area_id = self.area_id

        product_id = self.product_id

        serial_number = self.serial_number

        asset_tag = self.asset_tag

        reservation_id = self.reservation_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["AssetId"] = asset_id
        if area_id is not UNSET:
            field_dict["AreaId"] = area_id
        if product_id is not UNSET:
            field_dict["ProductId"] = product_id
        if serial_number is not UNSET:
            field_dict["SerialNumber"] = serial_number
        if asset_tag is not UNSET:
            field_dict["AssetTag"] = asset_tag
        if reservation_id is not UNSET:
            field_dict["ReservationId"] = reservation_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = d.pop("AssetId", UNSET)

        area_id = d.pop("AreaId", UNSET)

        product_id = d.pop("ProductId", UNSET)

        serial_number = d.pop("SerialNumber", UNSET)

        asset_tag = d.pop("AssetTag", UNSET)

        reservation_id = d.pop("ReservationId", UNSET)

        qualer_api_models_asset_reservation_from_close_asset_reservations_model = cls(
            asset_id=asset_id,
            area_id=area_id,
            product_id=product_id,
            serial_number=serial_number,
            asset_tag=asset_tag,
            reservation_id=reservation_id,
        )

        qualer_api_models_asset_reservation_from_close_asset_reservations_model.additional_properties = (
            d
        )
        return qualer_api_models_asset_reservation_from_close_asset_reservations_model

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
