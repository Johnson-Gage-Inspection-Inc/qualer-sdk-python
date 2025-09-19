from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.qualer_api_models_measurements_from_create_measurement_set_model import (
        MeasurementsFromCreateMeasurementSetModel,
    )
    from ..models.qualer_api_models_measurements_from_specification import (
        MeasurementsFromSpecification,
    )


T = TypeVar("T", bound="MeasurementsFromCreateMeasurementFormModel")


@_attrs_define
class MeasurementsFromCreateMeasurementFormModel:
    """
    Attributes:
        batch_type (Optional[str]):
        batch_result (Optional[str]):
        specification (Optional[MeasurementsFromSpecification]):
        measurement_sets (Optional[List['MeasurementsFromCreateMeasurementSetModel']]):
    """

    batch_type: Optional[str] = None
    batch_result: Optional[str] = None
    specification: Optional["MeasurementsFromSpecification"] = None
    measurement_sets: Optional[List["MeasurementsFromCreateMeasurementSetModel"]] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        batch_type = self.batch_type
        batch_result = self.batch_result

        specification: Optional[Dict[str, Any]] = None
        if self.specification is not None:
            specification = self.specification.to_dict()

        measurement_sets: Optional[List[Dict[str, Any]]] = None
        if self.measurement_sets is not None:
            measurement_sets = []
            for measurement_sets_item_data in self.measurement_sets:
                measurement_sets_item = measurement_sets_item_data.to_dict()
                measurement_sets.append(measurement_sets_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if batch_type is not None:
            field_dict["BatchType"] = batch_type
        if batch_result is not None:
            field_dict["BatchResult"] = batch_result
        if specification is not None:
            field_dict["Specification"] = specification
        if measurement_sets is not None:
            field_dict["MeasurementSets"] = measurement_sets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_measurements_from_create_measurement_set_model import (
            MeasurementsFromCreateMeasurementSetModel,
        )
        from ..models.qualer_api_models_measurements_from_specification import (
            MeasurementsFromSpecification,
        )

        d = dict(src_dict)
        batch_type = d.pop("BatchType", None)
        batch_result = d.pop("BatchResult", None)

        _specification = d.pop("Specification", None)
        specification: Optional[MeasurementsFromSpecification]
        if _specification is None:
            specification = None
        else:
            specification = MeasurementsFromSpecification.from_dict(_specification)

        measurement_sets: List[MeasurementsFromCreateMeasurementSetModel] = []
        _measurement_sets = d.pop("MeasurementSets", None)
        for measurement_sets_item_data in _measurement_sets or []:
            measurement_sets_item = MeasurementsFromCreateMeasurementSetModel.from_dict(
                measurement_sets_item_data
            )
            measurement_sets.append(measurement_sets_item)

        qualer_api_models_measurements_from_create_measurement_form_model = cls(
            batch_type=batch_type,
            batch_result=batch_result,
            specification=specification,
            measurement_sets=measurement_sets,
        )

        qualer_api_models_measurements_from_create_measurement_form_model.additional_properties = d
        return qualer_api_models_measurements_from_create_measurement_form_model

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
