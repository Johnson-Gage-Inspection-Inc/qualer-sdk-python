from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsClientsFromClientAssetQuery")


@_attrs_define
class QualerApiModelsClientsFromClientAssetQuery:
    """
    Attributes:
        equipment_id (Union[None, Unset, str]):
        serial_number (Union[None, Unset, str]):
        asset_tag (Union[None, Unset, str]):
        barcode (Union[None, Unset, str]):
        legacy_id (Union[None, Unset, str]):
    """

    equipment_id: Union[None, Unset, str] = UNSET
    serial_number: Union[None, Unset, str] = UNSET
    asset_tag: Union[None, Unset, str] = UNSET
    barcode: Union[None, Unset, str] = UNSET
    legacy_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        equipment_id = self.equipment_id

        serial_number = self.serial_number

        asset_tag = self.asset_tag

        barcode = self.barcode

        legacy_id = self.legacy_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if equipment_id is not UNSET:
            field_dict["EquipmentId"] = equipment_id
        if serial_number is not UNSET:
            field_dict["SerialNumber"] = serial_number
        if asset_tag is not UNSET:
            field_dict["AssetTag"] = asset_tag
        if barcode is not UNSET:
            field_dict["Barcode"] = barcode
        if legacy_id is not UNSET:
            field_dict["LegacyId"] = legacy_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        equipment_id = d.pop("EquipmentId", UNSET)

        serial_number = d.pop("SerialNumber", UNSET)

        asset_tag = d.pop("AssetTag", UNSET)

        barcode = d.pop("Barcode", UNSET)

        legacy_id = d.pop("LegacyId", UNSET)

        qualer_api_models_clients_from_client_asset_query = cls(
            equipment_id=equipment_id,
            serial_number=serial_number,
            asset_tag=asset_tag,
            barcode=barcode,
            legacy_id=legacy_id,
        )

        qualer_api_models_clients_from_client_asset_query.additional_properties = d
        return qualer_api_models_clients_from_client_asset_query

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
