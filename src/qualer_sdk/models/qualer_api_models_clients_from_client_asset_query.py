from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ClientsFromClientAssetQuery")


@_attrs_define
class ClientsFromClientAssetQuery:
    """
    Attributes:
        equipment_id (Optional[str]):
        serial_number (Optional[str]):
        asset_tag (Optional[str]):
        barcode (Optional[str]):
        legacy_id (Optional[str]):
    """

    equipment_id: Optional[str] = None
    serial_number: Optional[str] = None
    asset_tag: Optional[str] = None
    barcode: Optional[str] = None
    legacy_id: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        equipment_id = self.equipment_id
        serial_number = self.serial_number
        asset_tag = self.asset_tag
        barcode = self.barcode
        legacy_id = self.legacy_id
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if equipment_id is not None:
            field_dict["EquipmentId"] = equipment_id
        if serial_number is not None:
            field_dict["SerialNumber"] = serial_number
        if asset_tag is not None:
            field_dict["AssetTag"] = asset_tag
        if barcode is not None:
            field_dict["Barcode"] = barcode
        if legacy_id is not None:
            field_dict["LegacyId"] = legacy_id
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        equipment_id = d.pop("EquipmentId", None)
        serial_number = d.pop("SerialNumber", None)
        asset_tag = d.pop("AssetTag", None)
        barcode = d.pop("Barcode", None)
        legacy_id = d.pop("LegacyId", None)
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
