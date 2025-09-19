from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.qualer_api_models_report_datasets_to_measurement_channel_uniformity_response_batch_type import (
    ReportDatasetsToMeasurementChannelUniformityResponseBatchType,
)
from ..models.service_result_status import ServiceResultStatus

T = TypeVar("T", bound="ReportDatasetsToMeasurementChannelUniformityResponse")


@_attrs_define
class ReportDatasetsToMeasurementChannelUniformityResponse:
    """
    Attributes:
        service_order_item_id (Optional[int]):
        measurement_point_id (Optional[int]):
        batch_type (Optional[ReportDatasetsToMeasurementChannelUniformityResponseBatchType]):
        column_index (Optional[int]):
        mean (Optional[str]):
        mean_result (Optional[bool]):
        sd (Optional[str]):
        sd_result (Optional[bool]):
        cv (Optional[str]):
        cv_result (Optional[bool]):
        range_ (Optional[str]):
        range_result (Optional[bool]):
        delta (Optional[str]):
        delta_result (Optional[bool]):
        result (Optional[ServiceResultStatus]):
    """

    service_order_item_id: Optional[int] = None
    measurement_point_id: Optional[int] = None
    batch_type: Optional[ReportDatasetsToMeasurementChannelUniformityResponseBatchType] = None
    column_index: Optional[int] = None
    mean: Optional[str] = None
    mean_result: Optional[bool] = None
    sd: Optional[str] = None
    sd_result: Optional[bool] = None
    cv: Optional[str] = None
    cv_result: Optional[bool] = None
    range_: Optional[str] = None
    range_result: Optional[bool] = None
    delta: Optional[str] = None
    delta_result: Optional[bool] = None
    result: Optional[ServiceResultStatus] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_order_item_id = self.service_order_item_id

        measurement_point_id = self.measurement_point_id

        batch_type: Optional[int] = None
        if self.batch_type:
            batch_type = self.batch_type.value

        column_index = self.column_index

        mean = self.mean

        mean_result = self.mean_result

        sd = self.sd

        sd_result = self.sd_result

        cv = self.cv

        cv_result = self.cv_result

        range_ = self.range_

        range_result = self.range_result

        delta = self.delta

        delta_result = self.delta_result

        result: Optional[int] = None
        if self.result:
            result = self.result.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_item_id is not None:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if measurement_point_id is not None:
            field_dict["MeasurementPointId"] = measurement_point_id
        if batch_type is not None:
            field_dict["BatchType"] = batch_type
        if column_index is not None:
            field_dict["ColumnIndex"] = column_index
        if mean is not None:
            field_dict["Mean"] = mean
        if mean_result is not None:
            field_dict["MeanResult"] = mean_result
        if sd is not None:
            field_dict["SD"] = sd
        if sd_result is not None:
            field_dict["SDResult"] = sd_result
        if cv is not None:
            field_dict["CV"] = cv
        if cv_result is not None:
            field_dict["CVResult"] = cv_result
        if range_ is not None:
            field_dict["Range"] = range_
        if range_result is not None:
            field_dict["RangeResult"] = range_result
        if delta is not None:
            field_dict["Delta"] = delta
        if delta_result is not None:
            field_dict["DeltaResult"] = delta_result
        if result is not None:
            field_dict["Result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_item_id = d.pop("ServiceOrderItemId", None)

        measurement_point_id = d.pop("MeasurementPointId", None)

        _batch_type = d.pop("BatchType", None)
        batch_type: Optional[ReportDatasetsToMeasurementChannelUniformityResponseBatchType]
        if not _batch_type:
            batch_type = None
        else:
            batch_type = ReportDatasetsToMeasurementChannelUniformityResponseBatchType(_batch_type)

        column_index = d.pop("ColumnIndex", None)

        mean = d.pop("Mean", None)

        mean_result = d.pop("MeanResult", None)

        sd = d.pop("SD", None)

        sd_result = d.pop("SDResult", None)

        cv = d.pop("CV", None)

        cv_result = d.pop("CVResult", None)

        range_ = d.pop("Range", None)

        range_result = d.pop("RangeResult", None)

        delta = d.pop("Delta", None)

        delta_result = d.pop("DeltaResult", None)

        _result = d.pop("Result", None)
        result: Optional[ServiceResultStatus]
        if not _result:
            result = None
        elif _result is None:
            result = None
        else:
            result = ServiceResultStatus(_result)

        qualer_api_models_report_datasets_to_measurement_channel_uniformity_response = cls(
            service_order_item_id=service_order_item_id,
            measurement_point_id=measurement_point_id,
            batch_type=batch_type,
            column_index=column_index,
            mean=mean,
            mean_result=mean_result,
            sd=sd,
            sd_result=sd_result,
            cv=cv,
            cv_result=cv_result,
            range_=range_,
            range_result=range_result,
            delta=delta,
            delta_result=delta_result,
            result=result,
        )

        qualer_api_models_report_datasets_to_measurement_channel_uniformity_response.additional_properties = (
            d
        )
        return qualer_api_models_report_datasets_to_measurement_channel_uniformity_response

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
