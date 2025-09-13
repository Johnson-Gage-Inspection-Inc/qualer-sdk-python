import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="MeasurementsFromUpdateMeasurementModel")


@_attrs_define
class MeasurementsFromUpdateMeasurementModel:
    """
    Attributes:
        measurement_id (Optional[int]):
        values (Optional[str]):
        channel (Optional[int]):
        updated_by (Optional[str]):
        updated_on (Optional[datetime.datetime]):
    """

    measurement_id: Optional[int] = None
    values: Optional[str] = None
    channel: Optional[int] = None
    updated_by: Optional[str] = None
    updated_on: Optional[datetime.datetime] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        measurement_id = self.measurement_id

        values = self.values

        channel = self.channel

        updated_by = self.updated_by

        updated_on: Optional[str] = None
        if self.updated_on:
            updated_on = self.updated_on.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measurement_id is not None:
            field_dict["MeasurementId"] = measurement_id
        if values is not None:
            field_dict["Values"] = values
        if channel is not None:
            field_dict["Channel"] = channel
        if updated_by is not None:
            field_dict["UpdatedBy"] = updated_by
        if updated_on is not None:
            field_dict["UpdatedOn"] = updated_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        measurement_id = d.pop("MeasurementId", None)

        values = d.pop("Values", None)

        channel = d.pop("Channel", None)

        updated_by = d.pop("UpdatedBy", None)

        _updated_on = d.pop("UpdatedOn", None)
        updated_on: Optional[datetime.datetime]
        if not _updated_on:
            updated_on = None
        else:
            updated_on = isoparse(_updated_on)

        qualer_api_models_measurements_from_update_measurement_model = cls(
            measurement_id=measurement_id,
            values=values,
            channel=channel,
            updated_by=updated_by,
            updated_on=updated_on,
        )

        qualer_api_models_measurements_from_update_measurement_model.additional_properties = d
        return qualer_api_models_measurements_from_update_measurement_model

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
