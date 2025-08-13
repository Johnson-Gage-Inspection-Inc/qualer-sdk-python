from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="QualerApiModelsMeasurementsFromUpdateMeasurementConditionFactorModel"
)


@_attrs_define
class QualerApiModelsMeasurementsFromUpdateMeasurementConditionFactorModel:
    """
    Attributes:
        measurement_condition_factor_id (Union[None, Unset, int]):
        factor_id (Union[None, Unset, str]):
        factor_name (Union[None, Unset, str]):
        factor_value (Union[None, Unset, float]):
        factor_uom (Union[None, Unset, str]):
    """

    measurement_condition_factor_id: Union[None, Unset, int] = UNSET
    factor_id: Union[None, Unset, str] = UNSET
    factor_name: Union[None, Unset, str] = UNSET
    factor_value: Union[None, Unset, float] = UNSET
    factor_uom: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measurement_condition_factor_id = self.measurement_condition_factor_id

        factor_id = self.factor_id

        factor_name = self.factor_name

        factor_value = self.factor_value

        factor_uom = self.factor_uom

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measurement_condition_factor_id is not UNSET:
            field_dict["MeasurementConditionFactorId"] = measurement_condition_factor_id
        if factor_id is not UNSET:
            field_dict["FactorId"] = factor_id
        if factor_name is not UNSET:
            field_dict["FactorName"] = factor_name
        if factor_value is not UNSET:
            field_dict["FactorValue"] = factor_value
        if factor_uom is not UNSET:
            field_dict["FactorUom"] = factor_uom

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        measurement_condition_factor_id = d.pop("MeasurementConditionFactorId", UNSET)

        factor_id = d.pop("FactorId", UNSET)

        factor_name = d.pop("FactorName", UNSET)

        factor_value = d.pop("FactorValue", UNSET)

        factor_uom = d.pop("FactorUom", UNSET)

        qualer_api_models_measurements_from_update_measurement_condition_factor_model = cls(
            measurement_condition_factor_id=measurement_condition_factor_id,
            factor_id=factor_id,
            factor_name=factor_name,
            factor_value=factor_value,
            factor_uom=factor_uom,
        )

        qualer_api_models_measurements_from_update_measurement_condition_factor_model.additional_properties = (
            d
        )
        return qualer_api_models_measurements_from_update_measurement_condition_factor_model

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
