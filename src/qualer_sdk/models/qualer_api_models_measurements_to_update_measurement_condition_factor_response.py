from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MeasurementsToUpdateMeasurementConditionFactorResponse")


@_attrs_define
class MeasurementsToUpdateMeasurementConditionFactorResponse:
    """
    Attributes:
        measurement_condition_factor_id (Optional[int]):
        factor_id (Optional[str]):
        factor_name (Optional[str]):
        factor_value (Optional[float]):
        factor_uom (Optional[str]):
    """

    measurement_condition_factor_id: Optional[int] = None
    factor_id: Optional[str] = None
    factor_name: Optional[str] = None
    factor_value: Optional[float] = None
    factor_uom: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        measurement_condition_factor_id = self.measurement_condition_factor_id
        factor_id = self.factor_id
        factor_name = self.factor_name
        factor_value = self.factor_value
        factor_uom = self.factor_uom
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measurement_condition_factor_id is not None:
            field_dict["MeasurementConditionFactorId"] = measurement_condition_factor_id
        if factor_id is not None:
            field_dict["FactorId"] = factor_id
        if factor_name is not None:
            field_dict["FactorName"] = factor_name
        if factor_value is not None:
            field_dict["FactorValue"] = factor_value
        if factor_uom is not None:
            field_dict["FactorUom"] = factor_uom
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        measurement_condition_factor_id = d.pop("MeasurementConditionFactorId", None)
        factor_id = d.pop("FactorId", None)
        factor_name = d.pop("FactorName", None)
        factor_value = d.pop("FactorValue", None)
        factor_uom = d.pop("FactorUom", None)
        qualer_api_models_measurements_to_update_measurement_condition_factor_response = cls(
            measurement_condition_factor_id=measurement_condition_factor_id,
            factor_id=factor_id,
            factor_name=factor_name,
            factor_value=factor_value,
            factor_uom=factor_uom,
        )
        qualer_api_models_measurements_to_update_measurement_condition_factor_response.additional_properties = (
            d
        )
        return qualer_api_models_measurements_to_update_measurement_condition_factor_response

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
