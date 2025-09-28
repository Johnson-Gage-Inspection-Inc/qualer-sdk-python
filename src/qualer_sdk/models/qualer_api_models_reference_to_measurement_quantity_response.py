from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReferenceToMeasurementQuantityResponse")


@_attrs_define
class ReferenceToMeasurementQuantityResponse:
    """
    Attributes:
        measurement_quantity_id (Optional[int]):
        measurement_quantity (Optional[str]):
    """

    measurement_quantity_id: Optional[int] = None
    measurement_quantity: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        measurement_quantity_id = self.measurement_quantity_id
        measurement_quantity = self.measurement_quantity
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measurement_quantity_id is not None:
            field_dict["MeasurementQuantityId"] = measurement_quantity_id
        if measurement_quantity is not None:
            field_dict["MeasurementQuantity"] = measurement_quantity
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        measurement_quantity_id = d.pop("MeasurementQuantityId", None)
        measurement_quantity = d.pop("MeasurementQuantity", None)
        qualer_api_models_reference_to_measurement_quantity_response = cls(
            measurement_quantity_id=measurement_quantity_id,
            measurement_quantity=measurement_quantity,
        )
        qualer_api_models_reference_to_measurement_quantity_response.additional_properties = d
        return qualer_api_models_reference_to_measurement_quantity_response

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
