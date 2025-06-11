from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsReportDatasetsToAssetAttributeResponse")


@_attrs_define
class QualerApiModelsReportDatasetsToAssetAttributeResponse:
    """
    Attributes:
        asset_id (Union[Unset, int]):
        attribute_name (Union[Unset, str]):
        attribute_value (Union[Unset, str]):
        is_service (Union[Unset, bool]):
    """

    asset_id: Union[Unset, int] = UNSET
    attribute_name: Union[Unset, str] = UNSET
    attribute_value: Union[Unset, str] = UNSET
    is_service: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        attribute_name = self.attribute_name

        attribute_value = self.attribute_value

        is_service = self.is_service

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["AssetId"] = asset_id
        if attribute_name is not UNSET:
            field_dict["AttributeName"] = attribute_name
        if attribute_value is not UNSET:
            field_dict["AttributeValue"] = attribute_value
        if is_service is not UNSET:
            field_dict["IsService"] = is_service

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = d.pop("AssetId", UNSET)

        attribute_name = d.pop("AttributeName", UNSET)

        attribute_value = d.pop("AttributeValue", UNSET)

        is_service = d.pop("IsService", UNSET)

        qualer_api_models_report_datasets_to_asset_attribute_response = cls(
            asset_id=asset_id,
            attribute_name=attribute_name,
            attribute_value=attribute_value,
            is_service=is_service,
        )

        qualer_api_models_report_datasets_to_asset_attribute_response.additional_properties = (
            d
        )
        return qualer_api_models_report_datasets_to_asset_attribute_response

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
