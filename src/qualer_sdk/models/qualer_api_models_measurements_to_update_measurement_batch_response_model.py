from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualer_api_models_measurements_to_update_measurement_set_response_model import (
        QualerApiModelsMeasurementsToUpdateMeasurementSetResponseModel,
    )


T = TypeVar(
    "T", bound="QualerApiModelsMeasurementsToUpdateMeasurementBatchResponseModel"
)


@_attrs_define
class QualerApiModelsMeasurementsToUpdateMeasurementBatchResponseModel:
    """
    Attributes:
        batch_id (Union[Unset, int]):
        batch_type (Union[Unset, str]):
        measurement_sets (Union[Unset, list['QualerApiModelsMeasurementsToUpdateMeasurementSetResponseModel']]):
    """

    batch_id: Union[Unset, int] = UNSET
    batch_type: Union[Unset, str] = UNSET
    measurement_sets: Union[
        Unset, list["QualerApiModelsMeasurementsToUpdateMeasurementSetResponseModel"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        batch_id = self.batch_id

        batch_type = self.batch_type

        measurement_sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.measurement_sets, Unset):
            measurement_sets = []
            for measurement_sets_item_data in self.measurement_sets:
                measurement_sets_item = measurement_sets_item_data.to_dict()
                measurement_sets.append(measurement_sets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if batch_id is not UNSET:
            field_dict["BatchId"] = batch_id
        if batch_type is not UNSET:
            field_dict["BatchType"] = batch_type
        if measurement_sets is not UNSET:
            field_dict["MeasurementSets"] = measurement_sets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_measurements_to_update_measurement_set_response_model import (
            QualerApiModelsMeasurementsToUpdateMeasurementSetResponseModel,
        )

        d = dict(src_dict)
        batch_id = d.pop("BatchId", UNSET)

        batch_type = d.pop("BatchType", UNSET)

        measurement_sets = []
        _measurement_sets = d.pop("MeasurementSets", UNSET)
        for measurement_sets_item_data in _measurement_sets or []:
            measurement_sets_item = QualerApiModelsMeasurementsToUpdateMeasurementSetResponseModel.from_dict(
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
