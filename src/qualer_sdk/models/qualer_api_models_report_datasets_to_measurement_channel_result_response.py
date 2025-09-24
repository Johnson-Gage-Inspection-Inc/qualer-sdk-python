from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.qualer_api_models_report_datasets_to_measurement_channel_result_response_batch_type import (
    ReportDatasetsToMeasurementChannelResultResponseBatchType,
)
from ..models.service_result_status import ServiceResultStatus

T = TypeVar("T", bound="ReportDatasetsToMeasurementChannelResultResponse")


@_attrs_define
class ReportDatasetsToMeasurementChannelResultResponse:
    """
    Attributes:
        service_order_item_id (Optional[int]):
        measurement_point_id (Optional[int]):
        column_index (Optional[int]):
        batch_type (Optional[ReportDatasetsToMeasurementChannelResultResponseBatchType]):
        result (Optional[ServiceResultStatus]):
        mean_result (Optional[bool]):
        range_result (Optional[bool]):
        delta_result (Optional[bool]):
        min_result (Optional[bool]):
        max_result (Optional[bool]):
        tar_result (Optional[bool]):
        tur_result (Optional[bool]):
        error_result (Optional[bool]):
        sd_result (Optional[bool]):
        cv_result (Optional[bool]):
    """

    service_order_item_id: Optional[int] = None
    measurement_point_id: Optional[int] = None
    column_index: Optional[int] = None
    batch_type: Optional[ReportDatasetsToMeasurementChannelResultResponseBatchType] = None
    result: Optional[ServiceResultStatus] = None
    mean_result: Optional[bool] = None
    range_result: Optional[bool] = None
    delta_result: Optional[bool] = None
    min_result: Optional[bool] = None
    max_result: Optional[bool] = None
    tar_result: Optional[bool] = None
    tur_result: Optional[bool] = None
    error_result: Optional[bool] = None
    sd_result: Optional[bool] = None
    cv_result: Optional[bool] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_order_item_id = self.service_order_item_id

        measurement_point_id = self.measurement_point_id

        column_index = self.column_index

        batch_type: Optional[int] = None
        if self.batch_type:
            batch_type = self.batch_type.value

        result: Optional[int] = None
        if self.result:
            result = self.result.value

        mean_result = self.mean_result

        range_result = self.range_result

        delta_result = self.delta_result

        min_result = self.min_result

        max_result = self.max_result

        tar_result = self.tar_result

        tur_result = self.tur_result

        error_result = self.error_result

        sd_result = self.sd_result

        cv_result = self.cv_result

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_item_id is not None:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if measurement_point_id is not None:
            field_dict["MeasurementPointId"] = measurement_point_id
        if column_index is not None:
            field_dict["ColumnIndex"] = column_index
        if batch_type is not None:
            field_dict["BatchType"] = batch_type
        if result is not None:
            field_dict["Result"] = result
        if mean_result is not None:
            field_dict["MeanResult"] = mean_result
        if range_result is not None:
            field_dict["RangeResult"] = range_result
        if delta_result is not None:
            field_dict["DeltaResult"] = delta_result
        if min_result is not None:
            field_dict["MinResult"] = min_result
        if max_result is not None:
            field_dict["MaxResult"] = max_result
        if tar_result is not None:
            field_dict["TarResult"] = tar_result
        if tur_result is not None:
            field_dict["TurResult"] = tur_result
        if error_result is not None:
            field_dict["ErrorResult"] = error_result
        if sd_result is not None:
            field_dict["SdResult"] = sd_result
        if cv_result is not None:
            field_dict["CvResult"] = cv_result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_item_id = d.pop("ServiceOrderItemId", None)

        measurement_point_id = d.pop("MeasurementPointId", None)

        column_index = d.pop("ColumnIndex", None)

        _batch_type = d.pop("BatchType", None)
        batch_type: Optional[ReportDatasetsToMeasurementChannelResultResponseBatchType]
        if not _batch_type:
            batch_type = None
        else:
            batch_type = ReportDatasetsToMeasurementChannelResultResponseBatchType(_batch_type)

        _result = d.pop("Result", None)
        result = ServiceResultStatus(_result)

        mean_result = d.pop("MeanResult", None)

        range_result = d.pop("RangeResult", None)

        delta_result = d.pop("DeltaResult", None)

        min_result = d.pop("MinResult", None)

        max_result = d.pop("MaxResult", None)

        tar_result = d.pop("TarResult", None)

        tur_result = d.pop("TurResult", None)

        error_result = d.pop("ErrorResult", None)

        sd_result = d.pop("SdResult", None)

        cv_result = d.pop("CvResult", None)

        qualer_api_models_report_datasets_to_measurement_channel_result_response = cls(
            service_order_item_id=service_order_item_id,
            measurement_point_id=measurement_point_id,
            column_index=column_index,
            batch_type=batch_type,
            result=result,
            mean_result=mean_result,
            range_result=range_result,
            delta_result=delta_result,
            min_result=min_result,
            max_result=max_result,
            tar_result=tar_result,
            tur_result=tur_result,
            error_result=error_result,
            sd_result=sd_result,
            cv_result=cv_result,
        )

        qualer_api_models_report_datasets_to_measurement_channel_result_response.additional_properties = (
            d
        )
        return qualer_api_models_report_datasets_to_measurement_channel_result_response

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
