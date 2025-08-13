import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="QualerApiModelsAssetServiceRecordsFromAssetServiceRecordFilterModel"
)


@_attrs_define
class QualerApiModelsAssetServiceRecordsFromAssetServiceRecordFilterModel:
    """
    Attributes:
        asset_id (Union[None, Unset, int]):
        serial_number (Union[None, Unset, str]):
        from_ (Union[None, Unset, datetime.datetime]):
        to (Union[None, Unset, datetime.datetime]):
    """

    asset_id: Union[None, Unset, int] = UNSET
    serial_number: Union[None, Unset, str] = UNSET
    from_: Union[None, Unset, datetime.datetime] = UNSET
    to: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        serial_number = self.serial_number

        from_: Union[None, Unset, str] = UNSET
        if self.from_ and not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        to: Union[None, Unset, str] = UNSET
        if self.to and not isinstance(self.to, Unset):
            to = self.to.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["AssetId"] = asset_id
        if serial_number is not UNSET:
            field_dict["SerialNumber"] = serial_number
        if from_ is not UNSET:
            field_dict["From"] = from_
        if to is not UNSET:
            field_dict["To"] = to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = d.pop("AssetId", UNSET)

        serial_number = d.pop("SerialNumber", UNSET)

        _from_ = d.pop("From", UNSET)
        from_: Union[None, Unset, datetime.datetime]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = isoparse(_from_)

        _to = d.pop("To", UNSET)
        to: Union[None, Unset, datetime.datetime]
        if isinstance(_to, Unset):
            to = UNSET
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
