from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_custom_fields import (
        MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields,
    )
    from ..models.qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_display_options import (
        MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelDisplayOptions,
    )
    from ..models.qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_measurement_set_response_model_measurement_point_response_model import (
        MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModel,
    )


T = TypeVar(
    "T",
    bound="MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel",
)


@_attrs_define
class MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel:
    """
    Attributes:
        measurement_name (Optional[str]):
        is_accredited (Optional[bool]):
        measurement_quantity_id (Optional[int]):
        default_unit_of_measure_id (Optional[int]):
        decimal_places (Optional[int]):
        significant_figures (Optional[int]):
        display_options (Optional[MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelDisplayOptions]):
        custom_fields (Optional[MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields]):
        measurement_points (Optional[List['MeasurementsToMeasurementRecordResponseModelMeasurementBat
            chResponseModelMeasurementSetResponseModelMeasurementPointResponseModel']]):
    """

    measurement_name: Optional[str] = None
    is_accredited: Optional[bool] = None
    measurement_quantity_id: Optional[int] = None
    default_unit_of_measure_id: Optional[int] = None
    decimal_places: Optional[int] = None
    significant_figures: Optional[int] = None
    display_options: Optional[
        "MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelDisplayOptions"
    ] = None
    custom_fields: Optional[
        "MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields"
    ] = None
    measurement_points: Optional[
        List[
            "MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModel"
        ]
    ] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        measurement_name = self.measurement_name
        is_accredited = self.is_accredited
        measurement_quantity_id = self.measurement_quantity_id
        default_unit_of_measure_id = self.default_unit_of_measure_id
        decimal_places = self.decimal_places
        significant_figures = self.significant_figures
        display_options: Optional[Dict[str, Any]] = None
        if self.display_options:
            display_options = self.display_options.to_dict()
        custom_fields: Optional[Dict[str, Any]] = None
        if self.custom_fields:
            custom_fields = self.custom_fields.to_dict()
        measurement_points: Optional[List[Dict[str, Any]]] = None
        if self.measurement_points:
            measurement_points = []
            for measurement_points_item_data in self.measurement_points:
                measurement_points_item = measurement_points_item_data.to_dict()
                measurement_points.append(measurement_points_item)
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measurement_name is not None:
            field_dict["MeasurementName"] = measurement_name
        if is_accredited is not None:
            field_dict["IsAccredited"] = is_accredited
        if measurement_quantity_id is not None:
            field_dict["MeasurementQuantityId"] = measurement_quantity_id
        if default_unit_of_measure_id is not None:
            field_dict["DefaultUnitOfMeasureId"] = default_unit_of_measure_id
        if decimal_places is not None:
            field_dict["DecimalPlaces"] = decimal_places
        if significant_figures is not None:
            field_dict["SignificantFigures"] = significant_figures
        if display_options is not None:
            field_dict["DisplayOptions"] = display_options
        if custom_fields is not None:
            field_dict["CustomFields"] = custom_fields
        if measurement_points is not None:
            field_dict["MeasurementPoints"] = measurement_points
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_custom_fields import (
            MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields,
        )
        from ..models.qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_display_options import (
            MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelDisplayOptions,
        )
        from ..models.qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_measurement_set_response_model_measurement_point_response_model import (
            MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModel,
        )
        d = dict(src_dict)
        measurement_name = d.pop("MeasurementName", None)
        is_accredited = d.pop("IsAccredited", None)
        measurement_quantity_id = d.pop("MeasurementQuantityId", None)
        default_unit_of_measure_id = d.pop("DefaultUnitOfMeasureId", None)
        decimal_places = d.pop("DecimalPlaces", None)
        significant_figures = d.pop("SignificantFigures", None)
        _display_options = d.pop("DisplayOptions", None)
        display_options: Optional[
            MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelDisplayOptions
        ]
        if not _display_options:
            display_options = None
        else:
            display_options = MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelDisplayOptions.from_dict(
                _display_options
            )
        _custom_fields = d.pop("CustomFields", None)
        custom_fields: Optional[
            MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields
        ]
        if not _custom_fields:
            custom_fields = None
        else:
            custom_fields = MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields.from_dict(
                _custom_fields
            )
        measurement_points = []
        _measurement_points = d.pop("MeasurementPoints", None)
        for measurement_points_item_data in _measurement_points or []:
            measurement_points_item = MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModel.from_dict(
                measurement_points_item_data
            )
            measurement_points.append(measurement_points_item)
        qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_measurement_set_response_model = cls(
            measurement_name=measurement_name,
            is_accredited=is_accredited,
            measurement_quantity_id=measurement_quantity_id,
            default_unit_of_measure_id=default_unit_of_measure_id,
            decimal_places=decimal_places,
            significant_figures=significant_figures,
            display_options=display_options,
            custom_fields=custom_fields,
            measurement_points=measurement_points,
        )
        qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_measurement_set_response_model.additional_properties = (
            d
        )
        return qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_measurement_set_response_model

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
