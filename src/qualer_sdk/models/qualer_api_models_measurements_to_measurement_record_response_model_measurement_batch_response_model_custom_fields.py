from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_custom_fields_create_measurement_field_response_model import (
        QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFieldsCreateMeasurementFieldResponseModel,
    )


T = TypeVar(
    "T",
    bound="QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields",
)


@_attrs_define
class QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields:
    """
    Attributes:
        description (Union[Unset, str]):
        result (Union[Unset, str]):
        items (Union[Unset, list['QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseMod
            elCustomFieldsCreateMeasurementFieldResponseModel']]):
    """

    description: Union[Unset, str] = UNSET
    result: Union[Unset, str] = UNSET
    items: Union[
        Unset,
        list[
            "QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFieldsCreateMeasurementFieldResponseModel"
        ],
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        result = self.result

        items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["Description"] = description
        if result is not UNSET:
            field_dict["Result"] = result
        if items is not UNSET:
            field_dict["Items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_custom_fields_create_measurement_field_response_model import (
            QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFieldsCreateMeasurementFieldResponseModel,
        )

        d = dict(src_dict)
        description = d.pop("Description", UNSET)

        result = d.pop("Result", UNSET)

        items = []
        _items = d.pop("Items", UNSET)
        for items_item_data in _items or []:
            items_item = QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFieldsCreateMeasurementFieldResponseModel.from_dict(
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
