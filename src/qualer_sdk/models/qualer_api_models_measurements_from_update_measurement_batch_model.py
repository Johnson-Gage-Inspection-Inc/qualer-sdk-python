from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.qualer_api_models_measurements_from_update_measurement_set_model import (
        MeasurementsFromUpdateMeasurementSetModel,
    )


T = TypeVar("T", bound="MeasurementsFromUpdateMeasurementBatchModel")


@_attrs_define
class MeasurementsFromUpdateMeasurementBatchModel:
    """
    Attributes:
        batch_id (Optional[int]):
        batch_type (Optional[str]):
        save_and_delete_empty (Optional[bool]):
        measurement_sets (Optional[List['MeasurementsFromUpdateMeasurementSetModel']]):
    """

    batch_id: Optional[int] = None
    batch_type: Optional[str] = None
    save_and_delete_empty: Optional[bool] = None
    measurement_sets: Optional[List["MeasurementsFromUpdateMeasurementSetModel"]] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        batch_id = self.batch_id

        batch_type = self.batch_type

        save_and_delete_empty = self.save_and_delete_empty

        measurement_sets: Optional[List[Dict[str, Any]]] = None
        if self.measurement_sets:
            measurement_sets = []
            for measurement_sets_item_data in self.measurement_sets:
                measurement_sets_item = measurement_sets_item_data.to_dict()
                measurement_sets.append(measurement_sets_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if batch_id is not None:
            field_dict["BatchId"] = batch_id
        if batch_type is not None:
            field_dict["BatchType"] = batch_type
        if save_and_delete_empty is not None:
            field_dict["SaveAndDeleteEmpty"] = save_and_delete_empty
        if measurement_sets is not None:
            field_dict["MeasurementSets"] = measurement_sets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_measurements_from_update_measurement_set_model import (
            MeasurementsFromUpdateMeasurementSetModel,
        )

        d = dict(src_dict)
        batch_id = d.pop("BatchId", None)

        batch_type = d.pop("BatchType", None)

        save_and_delete_empty = d.pop("SaveAndDeleteEmpty", None)

        measurement_sets = []
        _measurement_sets = d.pop("MeasurementSets", None)
        for measurement_sets_item_data in _measurement_sets or []:
            measurement_sets_item = MeasurementsFromUpdateMeasurementSetModel.from_dict(
                measurement_sets_item_data
            )

            measurement_sets.append(measurement_sets_item)

        qualer_api_models_measurements_from_update_measurement_batch_model = cls(
            batch_id=batch_id,
            batch_type=batch_type,
            save_and_delete_empty=save_and_delete_empty,
            measurement_sets=measurement_sets,
        )

        qualer_api_models_measurements_from_update_measurement_batch_model.additional_properties = d
        return qualer_api_models_measurements_from_update_measurement_batch_model

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
