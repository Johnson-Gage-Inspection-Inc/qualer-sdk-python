import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModelMeasurementConditionFactorResponseModel",
)


@_attrs_define
class QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModelMeasurementConditionFactorResponseModel:
    """
    Attributes:
        factor_id (Union[None, Unset, str]):
        factor_name (Union[None, Unset, str]):
        factor_value (Union[None, Unset, float]):
        factor_uom (Union[None, Unset, str]):
        last_modified_on_utc (Union[None, Unset, datetime.datetime]):
    """

    factor_id: Union[None, Unset, str] = UNSET
    factor_name: Union[None, Unset, str] = UNSET
    factor_value: Union[None, Unset, float] = UNSET
    factor_uom: Union[None, Unset, str] = UNSET
    last_modified_on_utc: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        factor_id = self.factor_id

        factor_name = self.factor_name

        factor_value = self.factor_value

        factor_uom = self.factor_uom

        last_modified_on_utc: Union[None, Unset, str]
        if isinstance(self.last_modified_on_utc, Unset):
            last_modified_on_utc = UNSET
        elif isinstance(self.last_modified_on_utc, datetime.datetime):
            last_modified_on_utc = self.last_modified_on_utc.isoformat()
        else:
            last_modified_on_utc = self.last_modified_on_utc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if factor_id is not UNSET:
            field_dict["FactorId"] = factor_id
        if factor_name is not UNSET:
            field_dict["FactorName"] = factor_name
        if factor_value is not UNSET:
            field_dict["FactorValue"] = factor_value
        if factor_uom is not UNSET:
            field_dict["FactorUom"] = factor_uom
        if last_modified_on_utc is not UNSET:
            field_dict["LastModifiedOnUtc"] = last_modified_on_utc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        factor_id = d.pop("FactorId", UNSET)

        factor_name = d.pop("FactorName", UNSET)

        factor_value = d.pop("FactorValue", UNSET)

        factor_uom = d.pop("FactorUom", UNSET)

        def _parse_last_modified_on_utc(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_modified_on_utc_type_0 = isoparse(data)

                return last_modified_on_utc_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_modified_on_utc = _parse_last_modified_on_utc(
            d.pop("LastModifiedOnUtc", UNSET)
        )

        qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_measurement_set_response_model_measurement_point_response_model_measurement_condition_factor_response_model = cls(
            factor_id=factor_id,
            factor_name=factor_name,
            factor_value=factor_value,
            factor_uom=factor_uom,
            last_modified_on_utc=last_modified_on_utc,
        )

        qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_measurement_set_response_model_measurement_point_response_model_measurement_condition_factor_response_model.additional_properties = (
            d
        )
        return qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_measurement_set_response_model_measurement_point_response_model_measurement_condition_factor_response_model

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
