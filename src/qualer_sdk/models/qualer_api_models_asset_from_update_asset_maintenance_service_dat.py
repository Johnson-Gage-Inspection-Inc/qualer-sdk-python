import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat")


@_attrs_define
class QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat:
    """
    Attributes:
        reset_service_date (Optional[datetime.datetime]):
        reset_service_task (Optional[str]):
    """

    reset_service_date: Optional[datetime.datetime] = None
    reset_service_task: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reset_service_date: Optional[str] = None
        if self.reset_service_date:
            reset_service_date = self.reset_service_date.isoformat()

        reset_service_task = self.reset_service_task

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reset_service_date is not None:
            field_dict["ResetServiceDate"] = reset_service_date
        if reset_service_task is not None:
            field_dict["ResetServiceTask"] = reset_service_task

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _reset_service_date = d.pop("ResetServiceDate", None)
        reset_service_date: Optional[datetime.datetime]
        if not _reset_service_date:
            reset_service_date = None
        else:
            reset_service_date = isoparse(_reset_service_date)

        reset_service_task = d.pop("ResetServiceTask", None)

        qualer_api_models_asset_from_update_asset_maintenance_service_dat = cls(
            reset_service_date=reset_service_date,
            reset_service_task=reset_service_task,
        )

        qualer_api_models_asset_from_update_asset_maintenance_service_dat.additional_properties = d
        return qualer_api_models_asset_from_update_asset_maintenance_service_dat

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
