from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsAssetServiceRecordsFromAssetServiceRecordModel")


@_attrs_define
class QualerApiModelsAssetServiceRecordsFromAssetServiceRecordModel:
    """
    Attributes:
        asset_service_record_id (Union[Unset, int]):
    """

    asset_service_record_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_service_record_id = self.asset_service_record_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_service_record_id is not UNSET:
            field_dict["AssetServiceRecordId"] = asset_service_record_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_service_record_id = d.pop("AssetServiceRecordId", UNSET)

        qualer_api_models_asset_service_records_from_asset_service_record_model = cls(
            asset_service_record_id=asset_service_record_id,
        )

        qualer_api_models_asset_service_records_from_asset_service_record_model.additional_properties = (
            d
        )
        return qualer_api_models_asset_service_records_from_asset_service_record_model

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
