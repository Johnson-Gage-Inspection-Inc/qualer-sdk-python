from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.qualer_api_models_report_datasets_to_measurement_channel_uniformity_response_batch_type import (
    QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponseBatchType,
)
from ..models.qualer_api_models_report_datasets_to_measurement_channel_uniformity_response_result import (
    QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponseResult,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponse"
)


@_attrs_define
class QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponse:
    """
    Attributes:
        service_order_item_id (Union[Unset, int]):
        measurement_point_id (Union[Unset, int]):
        batch_type (Union[Unset, QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponseBatchType]):
        column_index (Union[Unset, int]):
        mean (Union[Unset, str]):
        mean_result (Union[Unset, bool]):
        sd (Union[Unset, str]):
        sd_result (Union[Unset, bool]):
        cv (Union[Unset, str]):
        cv_result (Union[Unset, bool]):
        range_ (Union[Unset, str]):
        range_result (Union[Unset, bool]):
        delta (Union[Unset, str]):
        delta_result (Union[Unset, bool]):
        result (Union[Unset, QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponseResult]):
    """

    service_order_item_id: Union[Unset, int] = UNSET
    measurement_point_id: Union[Unset, int] = UNSET
    batch_type: Union[
        Unset,
        QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponseBatchType,
    ] = UNSET
    column_index: Union[Unset, int] = UNSET
    mean: Union[Unset, str] = UNSET
    mean_result: Union[Unset, bool] = UNSET
    sd: Union[Unset, str] = UNSET
    sd_result: Union[Unset, bool] = UNSET
    cv: Union[Unset, str] = UNSET
    cv_result: Union[Unset, bool] = UNSET
    range_: Union[Unset, str] = UNSET
    range_result: Union[Unset, bool] = UNSET
    delta: Union[Unset, str] = UNSET
    delta_result: Union[Unset, bool] = UNSET
    result: Union[
        Unset, QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponseResult
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_order_item_id = self.service_order_item_id

        measurement_point_id = self.measurement_point_id

        batch_type: Union[Unset, str] = UNSET
        if not isinstance(self.batch_type, Unset):
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

        result: Union[Unset, str] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_item_id is not UNSET:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if measurement_point_id is not UNSET:
            field_dict["MeasurementPointId"] = measurement_point_id
        if batch_type is not UNSET:
            field_dict["BatchType"] = batch_type
        if column_index is not UNSET:
            field_dict["ColumnIndex"] = column_index
        if mean is not UNSET:
            field_dict["Mean"] = mean
        if mean_result is not UNSET:
            field_dict["MeanResult"] = mean_result
        if sd is not UNSET:
            field_dict["SD"] = sd
        if sd_result is not UNSET:
            field_dict["SDResult"] = sd_result
        if cv is not UNSET:
            field_dict["CV"] = cv
        if cv_result is not UNSET:
            field_dict["CVResult"] = cv_result
        if range_ is not UNSET:
            field_dict["Range"] = range_
        if range_result is not UNSET:
            field_dict["RangeResult"] = range_result
        if delta is not UNSET:
            field_dict["Delta"] = delta
        if delta_result is not UNSET:
            field_dict["DeltaResult"] = delta_result
        if result is not UNSET:
            field_dict["Result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_item_id = d.pop("ServiceOrderItemId", UNSET)

        measurement_point_id = d.pop("MeasurementPointId", UNSET)

        _batch_type = d.pop("BatchType", UNSET)
        batch_type: Union[
            Unset,
            QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponseBatchType,
        ]
        if isinstance(_batch_type, Unset):
            batch_type = UNSET
        else:
            batch_type = QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponseBatchType(
                _batch_type
            )

        column_index = d.pop("ColumnIndex", UNSET)

        mean = d.pop("Mean", UNSET)

        mean_result = d.pop("MeanResult", UNSET)

        sd = d.pop("SD", UNSET)

        sd_result = d.pop("SDResult", UNSET)

        cv = d.pop("CV", UNSET)

        cv_result = d.pop("CVResult", UNSET)

        range_ = d.pop("Range", UNSET)

        range_result = d.pop("RangeResult", UNSET)

        delta = d.pop("Delta", UNSET)

        delta_result = d.pop("DeltaResult", UNSET)

        _result = d.pop("Result", UNSET)
        result: Union[
            Unset,
            QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponseResult,
        ]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponseResult(
                _result
            )

        qualer_api_models_report_datasets_to_measurement_channel_uniformity_response = (
            cls(
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
        )

        qualer_api_models_report_datasets_to_measurement_channel_uniformity_response.additional_properties = (
            d
        )
        return (
            qualer_api_models_report_datasets_to_measurement_channel_uniformity_response
        )

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
