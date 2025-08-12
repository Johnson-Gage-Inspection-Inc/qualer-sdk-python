from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsReferenceToUnitOfMeasureResponse")


@_attrs_define
class QualerApiModelsReferenceToUnitOfMeasureResponse:
    """
    Attributes:
        measurement_quantity_id (Union[None, Unset, int]):
        measurement_quantity (Union[None, Unset, str]):
        unit_of_measure_id (Union[None, Unset, int]):
        unit_of_measure (Union[None, Unset, str]):
    """

    measurement_quantity_id: Union[None, Unset, int] = UNSET
    measurement_quantity: Union[None, Unset, str] = UNSET
    unit_of_measure_id: Union[None, Unset, int] = UNSET
    unit_of_measure: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measurement_quantity_id = self.measurement_quantity_id

        measurement_quantity = self.measurement_quantity

        unit_of_measure_id = self.unit_of_measure_id

        unit_of_measure = self.unit_of_measure

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measurement_quantity_id is not UNSET:
            field_dict["MeasurementQuantityId"] = measurement_quantity_id
        if measurement_quantity is not UNSET:
            field_dict["MeasurementQuantity"] = measurement_quantity
        if unit_of_measure_id is not UNSET:
            field_dict["UnitOfMeasureId"] = unit_of_measure_id
        if unit_of_measure is not UNSET:
            field_dict["UnitOfMeasure"] = unit_of_measure

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        measurement_quantity_id = d.pop("MeasurementQuantityId", UNSET)

        measurement_quantity = d.pop("MeasurementQuantity", UNSET)

        unit_of_measure_id = d.pop("UnitOfMeasureId", UNSET)

        unit_of_measure = d.pop("UnitOfMeasure", UNSET)

        qualer_api_models_reference_to_unit_of_measure_response = cls(
            measurement_quantity_id=measurement_quantity_id,
            measurement_quantity=measurement_quantity,
            unit_of_measure_id=unit_of_measure_id,
            unit_of_measure=unit_of_measure,
        )

        qualer_api_models_reference_to_unit_of_measure_response.additional_properties = (
            d
        )
        return qualer_api_models_reference_to_unit_of_measure_response

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
