from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_custom_fields_create_measurement_field_response_model import (
        MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFieldsCreateMeasurementFieldResponseModel,
    )


T = TypeVar(
    "T",
    bound="MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields",
)


@_attrs_define
class MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields:
    """
    Attributes:
        description (Optional[str]):
        result (Optional[str]):
        items (Optional[List['MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseMod
            elCustomFieldsCreateMeasurementFieldResponseModel']]):
    """

    description: Optional[str] = None
    result: Optional[str] = None
    items: Optional[
        List[
            "MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFieldsCreateMeasurementFieldResponseModel"
        ]
    ] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        result = self.result

        items: Optional[List[Dict[str, Any]]] = None
        if self.items:
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not None:
            field_dict["Description"] = description
        if result is not None:
            field_dict["Result"] = result
        if items is not None:
            field_dict["Items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_custom_fields_create_measurement_field_response_model import (
            MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFieldsCreateMeasurementFieldResponseModel,
        )

        d = dict(src_dict)
        description = d.pop("Description", None)

        result = d.pop("Result", None)

        items = []
        _items = d.pop("Items", None)
        for items_item_data in _items or []:
            items_item = MeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFieldsCreateMeasurementFieldResponseModel.from_dict(
                items_item_data
            )

            items.append(items_item)

        qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_custom_fields = cls(
            description=description,
            result=result,
            items=items,
        )

        qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_custom_fields.additional_properties = (
            d
        )
        return qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_custom_fields

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
