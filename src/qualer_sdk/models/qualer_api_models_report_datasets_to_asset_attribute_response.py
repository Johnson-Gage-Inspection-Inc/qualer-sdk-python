from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReportDatasetsToAssetAttributeResponse")


@_attrs_define
class ReportDatasetsToAssetAttributeResponse:
    """
    Attributes:
        asset_id (int):
        attribute_name (Optional[str]):
        attribute_value (Optional[str]):
        is_service (Optional[bool]):
    """

    asset_id: int
    attribute_name: Optional[str] = None
    attribute_value: Optional[str] = None
    is_service: Optional[bool] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asset_id = self.asset_id
        attribute_name = self.attribute_name
        attribute_value = self.attribute_value
        is_service = self.is_service
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not None:
            field_dict["AssetId"] = asset_id
        if attribute_name is not None:
            field_dict["AttributeName"] = attribute_name
        if attribute_value is not None:
            field_dict["AttributeValue"] = attribute_value
        if is_service is not None:
            field_dict["IsService"] = is_service
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = d.pop("AssetId", None)
        attribute_name = d.pop("AttributeName", None)
        attribute_value = d.pop("AttributeValue", None)
        is_service = d.pop("IsService", None)
        qualer_api_models_report_datasets_to_asset_attribute_response = cls(
            asset_id=asset_id,
            attribute_name=attribute_name,
            attribute_value=attribute_value,
            is_service=is_service,
        )
        qualer_api_models_report_datasets_to_asset_attribute_response.additional_properties = d
        return qualer_api_models_report_datasets_to_asset_attribute_response

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
