import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsMeasurementsToUpdateMeasurementResponseModel")


@_attrs_define
class QualerApiModelsMeasurementsToUpdateMeasurementResponseModel:
    """
    Attributes:
        measurement_id (Union[Unset, int]):
        values (Union[Unset, str]):
        channel (Union[Unset, int]):
        updated_by (Union[Unset, str]):
        updated_on (Union[Unset, datetime.datetime]):
    """

    measurement_id: Union[Unset, int] = UNSET
    values: Union[Unset, str] = UNSET
    channel: Union[Unset, int] = UNSET
    updated_by: Union[Unset, str] = UNSET
    updated_on: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measurement_id = self.measurement_id

        values = self.values

        channel = self.channel

        updated_by = self.updated_by

        updated_on: Union[Unset, str] = UNSET
        if not isinstance(self.updated_on, Unset):
            updated_on = self.updated_on.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measurement_id is not UNSET:
            field_dict["MeasurementId"] = measurement_id
        if values is not UNSET:
            field_dict["Values"] = values
        if channel is not UNSET:
            field_dict["Channel"] = channel
        if updated_by is not UNSET:
            field_dict["UpdatedBy"] = updated_by
        if updated_on is not UNSET:
            field_dict["UpdatedOn"] = updated_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        measurement_id = d.pop("MeasurementId", UNSET)

        values = d.pop("Values", UNSET)

        channel = d.pop("Channel", UNSET)

        updated_by = d.pop("UpdatedBy", UNSET)

        _updated_on = d.pop("UpdatedOn", UNSET)
        updated_on: Union[Unset, datetime.datetime]
        if isinstance(_updated_on, Unset):
            updated_on = UNSET
        else:
            updated_on = isoparse(_updated_on)

        qualer_api_models_measurements_to_update_measurement_response_model = cls(
            measurement_id=measurement_id,
            values=values,
            channel=channel,
            updated_by=updated_by,
            updated_on=updated_on,
        )

        qualer_api_models_measurements_to_update_measurement_response_model.additional_properties = (
            d
        )
        return qualer_api_models_measurements_to_update_measurement_response_model

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
