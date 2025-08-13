from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsAssetServiceRecordsFromAsrDocumentDownloadModel")


@_attrs_define
class QualerApiModelsAssetServiceRecordsFromAsrDocumentDownloadModel:
    """
    Attributes:
        asset_service_record_id (Union[None, Unset, int]):
        file_name (Union[None, Unset, str]):
    """

    asset_service_record_id: Union[None, Unset, int] = UNSET
    file_name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_service_record_id = self.asset_service_record_id

        file_name = self.file_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_service_record_id is not UNSET:
            field_dict["AssetServiceRecordId"] = asset_service_record_id
        if file_name is not UNSET:
            field_dict["FileName"] = file_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_service_record_id = d.pop("AssetServiceRecordId", UNSET)

        file_name = d.pop("FileName", UNSET)

        qualer_api_models_asset_service_records_from_asr_document_download_model = cls(
            asset_service_record_id=asset_service_record_id,
            file_name=file_name,
        )

        qualer_api_models_asset_service_records_from_asr_document_download_model.additional_properties = (
            d
        )
        return qualer_api_models_asset_service_records_from_asr_document_download_model

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
