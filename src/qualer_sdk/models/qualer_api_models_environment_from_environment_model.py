from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.environment_factor import EnvironmentFactor as EnvironmentFromEnvironmentModelFactorId

T = TypeVar("T", bound="EnvironmentFromEnvironmentModel")


@_attrs_define
class EnvironmentFromEnvironmentModel:
    """
    Attributes:
        station_id (Optional[int]):
        factor_id (Optional[EnvironmentFromEnvironmentModelFactorId]):
        factor_name (Optional[str]):
        factor_value (Optional[float]):
        unit_of_measure (Optional[str]):
    """

    station_id: Optional[int] = None
    factor_id: Optional[EnvironmentFromEnvironmentModelFactorId] = None
    factor_name: Optional[str] = None
    factor_value: Optional[float] = None
    unit_of_measure: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        station_id = self.station_id
        factor_id = self.factor_id.value if self.factor_id else None
        factor_name = self.factor_name
        factor_value = self.factor_value
        unit_of_measure = self.unit_of_measure
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if station_id is not None:
            field_dict["StationId"] = station_id
        if factor_id is not None:
            field_dict["FactorId"] = factor_id
        if factor_name is not None:
            field_dict["FactorName"] = factor_name
        if factor_value is not None:
            field_dict["FactorValue"] = factor_value
        if unit_of_measure is not None:
            field_dict["UnitOfMeasure"] = unit_of_measure
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        station_id = d.pop("StationId", None)
        _factor_id = d.pop("FactorId", None)
        factor_id: Optional[EnvironmentFromEnvironmentModelFactorId]
        if not _factor_id:
            factor_id = None
        else:
            factor_id = EnvironmentFromEnvironmentModelFactorId(_factor_id)
        factor_name = d.pop("FactorName", None)
        factor_value = d.pop("FactorValue", None)
        unit_of_measure = d.pop("UnitOfMeasure", None)
        qualer_api_models_environment_from_environment_model = cls(
            station_id=station_id,
            factor_id=factor_id,
            factor_name=factor_name,
            factor_value=factor_value,
            unit_of_measure=unit_of_measure,
        )
        qualer_api_models_environment_from_environment_model.additional_properties = d
        return qualer_api_models_environment_from_environment_model

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
