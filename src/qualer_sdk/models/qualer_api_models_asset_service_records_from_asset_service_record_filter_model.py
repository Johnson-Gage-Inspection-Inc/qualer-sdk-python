import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="AssetServiceRecordsFromAssetServiceRecordFilterModel")


@_attrs_define
class AssetServiceRecordsFromAssetServiceRecordFilterModel:
    """
    Attributes:
        asset_id (int):
        serial_number (Optional[str]):
        from_ (Optional[datetime.datetime]):
        to (Optional[datetime.datetime]):
    """

    asset_id: int
    serial_number: Optional[str] = None
    from_: Optional[datetime.datetime] = None
    to: Optional[datetime.datetime] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asset_id = self.asset_id
        serial_number = self.serial_number
        from_: Optional[str] = None
        if self.from_:
            from_ = self.from_.isoformat()
        to: Optional[str] = None
        if self.to:
            to = self.to.isoformat()
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not None:
            field_dict["AssetId"] = asset_id
        if serial_number is not None:
            field_dict["SerialNumber"] = serial_number
        if from_ is not None:
            field_dict["From"] = from_
        if to is not None:
            field_dict["To"] = to
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = d.pop("AssetId", None)
        serial_number = d.pop("SerialNumber", None)
        _from_ = d.pop("From", None)
        from_: Optional[datetime.datetime]
        if not _from_:
            from_ = None
        else:
            from_ = isoparse(_from_)
        _to = d.pop("To", None)
        to: Optional[datetime.datetime]
        if not _to:
            to = None
        else:
            to = isoparse(_to)
        qualer_api_models_asset_service_records_from_asset_service_record_filter_model = cls(
            asset_id=asset_id,
            serial_number=serial_number,
            from_=from_,
            to=to,
        )
        qualer_api_models_asset_service_records_from_asset_service_record_filter_model.additional_properties = (
            d
        )
        return qualer_api_models_asset_service_records_from_asset_service_record_filter_model

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
