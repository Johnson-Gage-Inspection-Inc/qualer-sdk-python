from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.qualer_api_models_report_datasets_to_measurement_field_response_batch_type import (
    ReportDatasetsToMeasurementFieldResponseBatchType,
)

T = TypeVar("T", bound="ReportDatasetsToMeasurementFieldResponse")


@_attrs_define
class ReportDatasetsToMeasurementFieldResponse:
    """
    Attributes:
        field_id (Optional[str]):
        name (Optional[str]):
        value (Optional[str]):
        measurement_name (Optional[str]):
        measurement_set_id (Optional[int]):
        specification_name (Optional[str]):
        measurement_point_id (Optional[int]):
        batch_type (Optional[ReportDatasetsToMeasurementFieldResponseBatchType]):
        service_order_item_id (Optional[int]):
        service_order_id (Optional[int]):
        batch_field_id (Optional[str]):
        point_field_id (Optional[str]):
    """

    field_id: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    measurement_name: Optional[str] = None
    measurement_set_id: Optional[int] = None
    specification_name: Optional[str] = None
    measurement_point_id: Optional[int] = None
    batch_type: Optional["ReportDatasetsToMeasurementFieldResponseBatchType"] = None
    service_order_item_id: Optional[int] = None
    service_order_id: Optional[int] = None
    batch_field_id: Optional[str] = None
    point_field_id: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_id = self.field_id
        name = self.name
        value = self.value
        measurement_name = self.measurement_name
        measurement_set_id = self.measurement_set_id
        specification_name = self.specification_name
        measurement_point_id = self.measurement_point_id
        batch_type = self.batch_type.value if self.batch_type else None
        service_order_item_id = self.service_order_item_id
        service_order_id = self.service_order_id
        batch_field_id = self.batch_field_id
        point_field_id = self.point_field_id
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_id is not None:
            field_dict["FieldId"] = field_id
        if name is not None:
            field_dict["Name"] = name
        if value is not None:
            field_dict["Value"] = value
        if measurement_name is not None:
            field_dict["MeasurementName"] = measurement_name
        if measurement_set_id is not None:
            field_dict["MeasurementSetId"] = measurement_set_id
        if specification_name is not None:
            field_dict["SpecificationName"] = specification_name
        if measurement_point_id is not None:
            field_dict["MeasurementPointId"] = measurement_point_id
        if batch_type is not None:
            field_dict["BatchType"] = batch_type
        if service_order_item_id is not None:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if service_order_id is not None:
            field_dict["ServiceOrderId"] = service_order_id
        if batch_field_id is not None:
            field_dict["BatchFieldId"] = batch_field_id
        if point_field_id is not None:
            field_dict["PointFieldId"] = point_field_id
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_id = d.pop("FieldId", None)
        name = d.pop("Name", None)
        value = d.pop("Value", None)
        measurement_name = d.pop("MeasurementName", None)
        measurement_set_id = d.pop("MeasurementSetId", None)
        specification_name = d.pop("SpecificationName", None)
        measurement_point_id = d.pop("MeasurementPointId", None)
        _batch_type = d.pop("BatchType", None)
        batch_type: Optional[ReportDatasetsToMeasurementFieldResponseBatchType]
        if not _batch_type:
            batch_type = None
        else:
            batch_type = ReportDatasetsToMeasurementFieldResponseBatchType(_batch_type)
        service_order_item_id = d.pop("ServiceOrderItemId", None)
        service_order_id = d.pop("ServiceOrderId", None)
        batch_field_id = d.pop("BatchFieldId", None)
        point_field_id = d.pop("PointFieldId", None)
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
        qualer_api_models_report_datasets_to_measurement_field_response.additional_properties = d
        return qualer_api_models_report_datasets_to_measurement_field_response

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
