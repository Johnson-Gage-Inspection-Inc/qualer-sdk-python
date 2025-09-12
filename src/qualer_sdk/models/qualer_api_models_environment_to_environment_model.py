from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.qualer_api_models_environment_to_environment_model_factor_id import (
    QualerApiModelsEnvironmentToEnvironmentModelFactorId,
)

T = TypeVar("T", bound="QualerApiModelsEnvironmentToEnvironmentModel")


@_attrs_define
class QualerApiModelsEnvironmentToEnvironmentModel:
    """
    Attributes:
        room_name (Optional[str]):
        factor_id (Optional[QualerApiModelsEnvironmentToEnvironmentModelFactorId]):
        station_id (Optional[int]):
        factor_name (Optional[str]):
        factor_value (Optional[float]):
        valid_range_min (Optional[float]):
        valid_range_max (Optional[float]):
        unit_of_measure (Optional[str]):
    """

    room_name: Optional[str] = None
    factor_id: Optional[QualerApiModelsEnvironmentToEnvironmentModelFactorId] = None
    station_id: Optional[int] = None
    factor_name: Optional[str] = None
    factor_value: Optional[float] = None
    valid_range_min: Optional[float] = None
    valid_range_max: Optional[float] = None
    unit_of_measure: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        room_name = self.room_name

        factor_id: Optional[str] = None
        if self.factor_id:
            factor_id = self.factor_id.value

        station_id = self.station_id

        factor_name = self.factor_name

        factor_value = self.factor_value

        valid_range_min = self.valid_range_min

        valid_range_max = self.valid_range_max

        unit_of_measure = self.unit_of_measure

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if room_name is not None:
            field_dict["RoomName"] = room_name
        if factor_id is not None:
            field_dict["FactorId"] = factor_id
        if station_id is not None:
            field_dict["StationId"] = station_id
        if factor_name is not None:
            field_dict["FactorName"] = factor_name
        if factor_value is not None:
            field_dict["FactorValue"] = factor_value
        if valid_range_min is not None:
            field_dict["ValidRangeMin"] = valid_range_min
        if valid_range_max is not None:
            field_dict["ValidRangeMax"] = valid_range_max
        if unit_of_measure is not None:
            field_dict["UnitOfMeasure"] = unit_of_measure

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        room_name = d.pop("RoomName", None)

        _factor_id = d.pop("FactorId", None)
        factor_id: Optional[QualerApiModelsEnvironmentToEnvironmentModelFactorId]
        if not _factor_id:
            factor_id = None
        else:
            factor_id = QualerApiModelsEnvironmentToEnvironmentModelFactorId(_factor_id)

        station_id = d.pop("StationId", None)

        factor_name = d.pop("FactorName", None)

        factor_value = d.pop("FactorValue", None)

        valid_range_min = d.pop("ValidRangeMin", None)

        valid_range_max = d.pop("ValidRangeMax", None)

        unit_of_measure = d.pop("UnitOfMeasure", None)

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
