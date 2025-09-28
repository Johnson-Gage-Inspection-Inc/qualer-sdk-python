from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.qualer_api_models_measurements_to_update_measurement_set_response_model import (
        MeasurementsToUpdateMeasurementSetResponseModel,
    )


T = TypeVar("T", bound="MeasurementsToUpdateMeasurementBatchResponseModel")


@_attrs_define
class MeasurementsToUpdateMeasurementBatchResponseModel:
    """
    Attributes:
        batch_id (Optional[int]):
        batch_type (Optional[str]):
        measurement_sets (Optional[List['MeasurementsToUpdateMeasurementSetResponseModel']]):
    """

    batch_id: Optional[int] = None
    batch_type: Optional[str] = None
    measurement_sets: Union[
        None,
        None,
        List["MeasurementsToUpdateMeasurementSetResponseModel"],
    ] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        batch_id = self.batch_id
        batch_type = self.batch_type
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
        if measurement_sets is not None:
            field_dict["MeasurementSets"] = measurement_sets
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_measurements_to_update_measurement_set_response_model import (
            MeasurementsToUpdateMeasurementSetResponseModel,
        )
        d = dict(src_dict)
        batch_id = d.pop("BatchId", None)
        batch_type = d.pop("BatchType", None)
        measurement_sets = []
        _measurement_sets = d.pop("MeasurementSets", None)
        for measurement_sets_item_data in _measurement_sets or []:
            measurement_sets_item = MeasurementsToUpdateMeasurementSetResponseModel.from_dict(
                measurement_sets_item_data
            )
            measurement_sets.append(measurement_sets_item)
        qualer_api_models_measurements_to_update_measurement_batch_response_model = cls(
            batch_id=batch_id,
            batch_type=batch_type,
            measurement_sets=measurement_sets,
        )
        qualer_api_models_measurements_to_update_measurement_batch_response_model.additional_properties = (
            d
        )
        return qualer_api_models_measurements_to_update_measurement_batch_response_model

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
