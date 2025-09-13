from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.qualer_api_models_measurements_from_update_measurement_batch_model import (
        MeasurementsFromUpdateMeasurementBatchModel,
    )


T = TypeVar("T", bound="MeasurementsFromUpdateMeasurementFormModel")


@_attrs_define
class MeasurementsFromUpdateMeasurementFormModel:
    """
    Attributes:
        measurement_batches (Optional[List['MeasurementsFromUpdateMeasurementBatchModel']]):
    """

    measurement_batches: Union[None, List["MeasurementsFromUpdateMeasurementBatchModel"]] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        measurement_batches: Optional[List[Dict[str, Any]]] = None
        if self.measurement_batches:
            measurement_batches = []
            for measurement_batches_item_data in self.measurement_batches:
                measurement_batches_item = measurement_batches_item_data.to_dict()
                measurement_batches.append(measurement_batches_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measurement_batches is not None:
            field_dict["MeasurementBatches"] = measurement_batches

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_measurements_from_update_measurement_batch_model import (
            MeasurementsFromUpdateMeasurementBatchModel,
        )

        d = dict(src_dict)
        measurement_batches = []
        _measurement_batches = d.pop("MeasurementBatches", None)
        for measurement_batches_item_data in _measurement_batches or []:
            measurement_batches_item = MeasurementsFromUpdateMeasurementBatchModel.from_dict(
                measurement_batches_item_data
            )

            measurement_batches.append(measurement_batches_item)

        qualer_api_models_measurements_from_update_measurement_form_model = cls(
            measurement_batches=measurement_batches,
        )

        qualer_api_models_measurements_from_update_measurement_form_model.additional_properties = d
        return qualer_api_models_measurements_from_update_measurement_form_model

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
