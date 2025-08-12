from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualer_api_models_measurements_from_create_measurement_set_model import (
        QualerApiModelsMeasurementsFromCreateMeasurementSetModel,
    )
    from ..models.qualer_api_models_measurements_from_specification import (
        QualerApiModelsMeasurementsFromSpecification,
    )


T = TypeVar("T", bound="QualerApiModelsMeasurementsFromCreateMeasurementFormModel")


@_attrs_define
class QualerApiModelsMeasurementsFromCreateMeasurementFormModel:
    """
    Attributes:
        batch_type (Union[Unset, str]):
        batch_result (Union[Unset, str]):
        specification (Union[Unset, QualerApiModelsMeasurementsFromSpecification]):
        measurement_sets (Union[Unset, list['QualerApiModelsMeasurementsFromCreateMeasurementSetModel']]):
    """

    batch_type: Union[Unset, str] = UNSET
    batch_result: Union[Unset, str] = UNSET
    specification: Union[Unset, "QualerApiModelsMeasurementsFromSpecification"] = UNSET
    measurement_sets: Union[
        Unset, list["QualerApiModelsMeasurementsFromCreateMeasurementSetModel"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        batch_type = self.batch_type

        batch_result = self.batch_result

        specification: Union[Unset, dict[str, Any]] = UNSET
        if self.specification and not isinstance(self.specification, Unset):
            specification = self.specification.to_dict()

        measurement_sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if self.measurement_sets and not isinstance(self.measurement_sets, Unset):
            measurement_sets = []
            for measurement_sets_item_data in self.measurement_sets:
                measurement_sets_item = measurement_sets_item_data.to_dict()
                measurement_sets.append(measurement_sets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if batch_type is not UNSET:
            field_dict["BatchType"] = batch_type
        if batch_result is not UNSET:
            field_dict["BatchResult"] = batch_result
        if specification is not UNSET:
            field_dict["Specification"] = specification
        if measurement_sets is not UNSET:
            field_dict["MeasurementSets"] = measurement_sets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_measurements_from_create_measurement_set_model import (
            QualerApiModelsMeasurementsFromCreateMeasurementSetModel,
        )
        from ..models.qualer_api_models_measurements_from_specification import (
            QualerApiModelsMeasurementsFromSpecification,
        )

        d = dict(src_dict)
        batch_type = d.pop("BatchType", UNSET)

        batch_result = d.pop("BatchResult", UNSET)

        _specification = d.pop("Specification", UNSET)
        specification: Union[Unset, QualerApiModelsMeasurementsFromSpecification]
        if isinstance(_specification, Unset):
            specification = UNSET
        else:
            specification = QualerApiModelsMeasurementsFromSpecification.from_dict(
                _specification
            )

        measurement_sets = []
        _measurement_sets = d.pop("MeasurementSets", UNSET)
        for measurement_sets_item_data in _measurement_sets or []:
            measurement_sets_item = (
                QualerApiModelsMeasurementsFromCreateMeasurementSetModel.from_dict(
                    measurement_sets_item_data
                )
            )

            measurement_sets.append(measurement_sets_item)

        qualer_api_models_measurements_from_create_measurement_form_model = cls(
            batch_type=batch_type,
            batch_result=batch_result,
            specification=specification,
            measurement_sets=measurement_sets,
        )

        qualer_api_models_measurements_from_create_measurement_form_model.additional_properties = (
            d
        )
        return qualer_api_models_measurements_from_create_measurement_form_model

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
