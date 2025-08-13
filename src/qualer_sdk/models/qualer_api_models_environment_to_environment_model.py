from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.qualer_api_models_environment_to_environment_model_factor_id import (
    QualerApiModelsEnvironmentToEnvironmentModelFactorId,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsEnvironmentToEnvironmentModel")


@_attrs_define
class QualerApiModelsEnvironmentToEnvironmentModel:
    """
    Attributes:
        room_name (Union[None, Unset, str]):
        factor_id (Union[None, Unset, QualerApiModelsEnvironmentToEnvironmentModelFactorId]):
        station_id (Union[None, Unset, int]):
        factor_name (Union[None, Unset, str]):
        factor_value (Union[None, Unset, float]):
        valid_range_min (Union[None, Unset, float]):
        valid_range_max (Union[None, Unset, float]):
        unit_of_measure (Union[None, Unset, str]):
    """

    room_name: Union[None, Unset, str] = UNSET
    factor_id: Union[
        None, Unset, QualerApiModelsEnvironmentToEnvironmentModelFactorId
    ] = UNSET
    station_id: Union[None, Unset, int] = UNSET
    factor_name: Union[None, Unset, str] = UNSET
    factor_value: Union[None, Unset, float] = UNSET
    valid_range_min: Union[None, Unset, float] = UNSET
    valid_range_max: Union[None, Unset, float] = UNSET
    unit_of_measure: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        room_name = self.room_name

        factor_id: Union[None, Unset, str] = UNSET
        if self.factor_id and not isinstance(self.factor_id, Unset):
            factor_id = self.factor_id.value

        station_id = self.station_id

        factor_name = self.factor_name

        factor_value = self.factor_value

        valid_range_min = self.valid_range_min

        valid_range_max = self.valid_range_max

        unit_of_measure = self.unit_of_measure

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if room_name is not UNSET:
            field_dict["RoomName"] = room_name
        if factor_id is not UNSET:
            field_dict["FactorId"] = factor_id
        if station_id is not UNSET:
            field_dict["StationId"] = station_id
        if factor_name is not UNSET:
            field_dict["FactorName"] = factor_name
        if factor_value is not UNSET:
            field_dict["FactorValue"] = factor_value
        if valid_range_min is not UNSET:
            field_dict["ValidRangeMin"] = valid_range_min
        if valid_range_max is not UNSET:
            field_dict["ValidRangeMax"] = valid_range_max
        if unit_of_measure is not UNSET:
            field_dict["UnitOfMeasure"] = unit_of_measure

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        room_name = d.pop("RoomName", UNSET)

        _factor_id = d.pop("FactorId", UNSET)
        factor_id: Union[
            None, Unset, QualerApiModelsEnvironmentToEnvironmentModelFactorId
        ]
        if isinstance(_factor_id, Unset):
            factor_id = UNSET
        else:
            factor_id = QualerApiModelsEnvironmentToEnvironmentModelFactorId(_factor_id)

        station_id = d.pop("StationId", UNSET)

        factor_name = d.pop("FactorName", UNSET)

        factor_value = d.pop("FactorValue", UNSET)

        valid_range_min = d.pop("ValidRangeMin", UNSET)

        valid_range_max = d.pop("ValidRangeMax", UNSET)

        unit_of_measure = d.pop("UnitOfMeasure", UNSET)

        qualer_api_models_environment_to_environment_model = cls(
            room_name=room_name,
            factor_id=factor_id,
            station_id=station_id,
            factor_name=factor_name,
            factor_value=factor_value,
            valid_range_min=valid_range_min,
            valid_range_max=valid_range_max,
            unit_of_measure=unit_of_measure,
        )

        qualer_api_models_environment_to_environment_model.additional_properties = d
        return qualer_api_models_environment_to_environment_model

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
