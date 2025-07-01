from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.qualer_api_models_report_datasets_to_measurement_channel_result_response_batch_type import (
    QualerApiModelsReportDatasetsToMeasurementChannelResultResponseBatchType,
)
from ..models.qualer_api_models_report_datasets_to_measurement_channel_result_response_result import (
    QualerApiModelsReportDatasetsToMeasurementChannelResultResponseResult,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="QualerApiModelsReportDatasetsToMeasurementChannelResultResponse"
)


@_attrs_define
class QualerApiModelsReportDatasetsToMeasurementChannelResultResponse:
    """
    Attributes:
        service_order_item_id (Union[Unset, int]):
        measurement_point_id (Union[Unset, int]):
        column_index (Union[Unset, int]):
        batch_type (Union[Unset, QualerApiModelsReportDatasetsToMeasurementChannelResultResponseBatchType]):
        result (Union[Unset, QualerApiModelsReportDatasetsToMeasurementChannelResultResponseResult]):
        mean_result (Union[Unset, bool]):
        range_result (Union[Unset, bool]):
        delta_result (Union[Unset, bool]):
        min_result (Union[Unset, bool]):
        max_result (Union[Unset, bool]):
        tar_result (Union[Unset, bool]):
        tur_result (Union[Unset, bool]):
        error_result (Union[Unset, bool]):
        sd_result (Union[Unset, bool]):
        cv_result (Union[Unset, bool]):
    """

    service_order_item_id: Union[Unset, int] = UNSET
    measurement_point_id: Union[Unset, int] = UNSET
    column_index: Union[Unset, int] = UNSET
    batch_type: Union[
        Unset, QualerApiModelsReportDatasetsToMeasurementChannelResultResponseBatchType
    ] = UNSET
    result: Union[
        Unset, QualerApiModelsReportDatasetsToMeasurementChannelResultResponseResult
    ] = UNSET
    mean_result: Union[Unset, bool] = UNSET
    range_result: Union[Unset, bool] = UNSET
    delta_result: Union[Unset, bool] = UNSET
    min_result: Union[Unset, bool] = UNSET
    max_result: Union[Unset, bool] = UNSET
    tar_result: Union[Unset, bool] = UNSET
    tur_result: Union[Unset, bool] = UNSET
    error_result: Union[Unset, bool] = UNSET
    sd_result: Union[Unset, bool] = UNSET
    cv_result: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_order_item_id = self.service_order_item_id

        measurement_point_id = self.measurement_point_id

        column_index = self.column_index

        batch_type: Union[Unset, int] = UNSET
        if not isinstance(self.batch_type, Unset):
            batch_type = self.batch_type.value

        result: Union[Unset, str] = UNSET
        if not isinstance(self.result, Unset):
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_item_id is not UNSET:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if measurement_point_id is not UNSET:
            field_dict["MeasurementPointId"] = measurement_point_id
        if column_index is not UNSET:
            field_dict["ColumnIndex"] = column_index
        if batch_type is not UNSET:
            field_dict["BatchType"] = batch_type
        if result is not UNSET:
            field_dict["Result"] = result
        if mean_result is not UNSET:
            field_dict["MeanResult"] = mean_result
        if range_result is not UNSET:
            field_dict["RangeResult"] = range_result
        if delta_result is not UNSET:
            field_dict["DeltaResult"] = delta_result
        if min_result is not UNSET:
            field_dict["MinResult"] = min_result
        if max_result is not UNSET:
            field_dict["MaxResult"] = max_result
        if tar_result is not UNSET:
            field_dict["TarResult"] = tar_result
        if tur_result is not UNSET:
            field_dict["TurResult"] = tur_result
        if error_result is not UNSET:
            field_dict["ErrorResult"] = error_result
        if sd_result is not UNSET:
            field_dict["SdResult"] = sd_result
        if cv_result is not UNSET:
            field_dict["CvResult"] = cv_result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_item_id = d.pop("ServiceOrderItemId", UNSET)

        measurement_point_id = d.pop("MeasurementPointId", UNSET)

        column_index = d.pop("ColumnIndex", UNSET)

        _batch_type = d.pop("BatchType", UNSET)
        batch_type: Union[
            Unset,
            QualerApiModelsReportDatasetsToMeasurementChannelResultResponseBatchType,
        ]
        if isinstance(_batch_type, Unset):
            batch_type = UNSET
        else:
            batch_type = QualerApiModelsReportDatasetsToMeasurementChannelResultResponseBatchType(
                _batch_type
            )

        _result = d.pop("Result", UNSET)
        result: Union[
            Unset, QualerApiModelsReportDatasetsToMeasurementChannelResultResponseResult
        ]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = (
                QualerApiModelsReportDatasetsToMeasurementChannelResultResponseResult(
                    _result
                )
            )

        mean_result = d.pop("MeanResult", UNSET)

        range_result = d.pop("RangeResult", UNSET)

        delta_result = d.pop("DeltaResult", UNSET)

        min_result = d.pop("MinResult", UNSET)

        max_result = d.pop("MaxResult", UNSET)

        tar_result = d.pop("TarResult", UNSET)

        tur_result = d.pop("TurResult", UNSET)

        error_result = d.pop("ErrorResult", UNSET)

        sd_result = d.pop("SdResult", UNSET)

        cv_result = d.pop("CvResult", UNSET)

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
