from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.qualer_api_models_report_datasets_to_measurement_field_response_batch_type import (
    QualerApiModelsReportDatasetsToMeasurementFieldResponseBatchType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsReportDatasetsToMeasurementFieldResponse")


@_attrs_define
class QualerApiModelsReportDatasetsToMeasurementFieldResponse:
    """
    Attributes:
        field_id (Union[Unset, str]):
        name (Union[Unset, str]):
        value (Union[Unset, str]):
        measurement_name (Union[Unset, str]):
        measurement_set_id (Union[Unset, int]):
        specification_name (Union[Unset, str]):
        measurement_point_id (Union[Unset, int]):
        batch_type (Union[Unset, QualerApiModelsReportDatasetsToMeasurementFieldResponseBatchType]):
        service_order_item_id (Union[Unset, int]):
        service_order_id (Union[Unset, int]):
        batch_field_id (Union[Unset, str]):
        point_field_id (Union[Unset, str]):
    """

    field_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    measurement_name: Union[Unset, str] = UNSET
    measurement_set_id: Union[Unset, int] = UNSET
    specification_name: Union[Unset, str] = UNSET
    measurement_point_id: Union[Unset, int] = UNSET
    batch_type: Union[
        Unset, QualerApiModelsReportDatasetsToMeasurementFieldResponseBatchType
    ] = UNSET
    service_order_item_id: Union[Unset, int] = UNSET
    service_order_id: Union[Unset, int] = UNSET
    batch_field_id: Union[Unset, str] = UNSET
    point_field_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        name = self.name

        value = self.value

        measurement_name = self.measurement_name

        measurement_set_id = self.measurement_set_id

        specification_name = self.specification_name

        measurement_point_id = self.measurement_point_id

        batch_type: Union[Unset, str] = UNSET
        if not isinstance(self.batch_type, Unset):
            batch_type = self.batch_type.value

        service_order_item_id = self.service_order_item_id

        service_order_id = self.service_order_id

        batch_field_id = self.batch_field_id

        point_field_id = self.point_field_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_id is not UNSET:
            field_dict["FieldId"] = field_id
        if name is not UNSET:
            field_dict["Name"] = name
        if value is not UNSET:
            field_dict["Value"] = value
        if measurement_name is not UNSET:
            field_dict["MeasurementName"] = measurement_name
        if measurement_set_id is not UNSET:
            field_dict["MeasurementSetId"] = measurement_set_id
        if specification_name is not UNSET:
            field_dict["SpecificationName"] = specification_name
        if measurement_point_id is not UNSET:
            field_dict["MeasurementPointId"] = measurement_point_id
        if batch_type is not UNSET:
            field_dict["BatchType"] = batch_type
        if service_order_item_id is not UNSET:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if service_order_id is not UNSET:
            field_dict["ServiceOrderId"] = service_order_id
        if batch_field_id is not UNSET:
            field_dict["BatchFieldId"] = batch_field_id
        if point_field_id is not UNSET:
            field_dict["PointFieldId"] = point_field_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_id = d.pop("FieldId", UNSET)

        name = d.pop("Name", UNSET)

        value = d.pop("Value", UNSET)

        measurement_name = d.pop("MeasurementName", UNSET)

        measurement_set_id = d.pop("MeasurementSetId", UNSET)

        specification_name = d.pop("SpecificationName", UNSET)

        measurement_point_id = d.pop("MeasurementPointId", UNSET)

        _batch_type = d.pop("BatchType", UNSET)
        batch_type: Union[
            Unset, QualerApiModelsReportDatasetsToMeasurementFieldResponseBatchType
        ]
        if isinstance(_batch_type, Unset):
            batch_type = UNSET
        else:
            batch_type = (
                QualerApiModelsReportDatasetsToMeasurementFieldResponseBatchType(
                    _batch_type
                )
            )

        service_order_item_id = d.pop("ServiceOrderItemId", UNSET)

        service_order_id = d.pop("ServiceOrderId", UNSET)

        batch_field_id = d.pop("BatchFieldId", UNSET)

        point_field_id = d.pop("PointFieldId", UNSET)

        qualer_api_models_report_datasets_to_measurement_field_response = cls(
            field_id=field_id,
            name=name,
            value=value,
            measurement_name=measurement_name,
            measurement_set_id=measurement_set_id,
            specification_name=specification_name,
            measurement_point_id=measurement_point_id,
            batch_type=batch_type,
            service_order_item_id=service_order_item_id,
            service_order_id=service_order_id,
            batch_field_id=batch_field_id,
            point_field_id=point_field_id,
        )

        qualer_api_models_report_datasets_to_measurement_field_response.additional_properties = (
            d
        )
        return qualer_api_models_report_datasets_to_measurement_field_response

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
