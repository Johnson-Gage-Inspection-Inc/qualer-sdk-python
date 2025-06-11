import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModelMeasurementResponseModel",
)


@_attrs_define
class QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModelMeasurementResponseModel:
    """
    Attributes:
        values (Union[Unset, str]):
        mean (Union[Unset, float]):
        sd (Union[Unset, float]):
        range_ (Union[Unset, float]):
        delta (Union[Unset, float]):
        cv (Union[Unset, float]):
        cmc (Union[Unset, float]):
        mu (Union[Unset, float]):
        tur (Union[Unset, float]):
        tar (Union[Unset, float]):
        max_value (Union[Unset, float]):
        min_value (Union[Unset, float]):
        error (Union[Unset, float]):
        result (Union[Unset, str]):
        updated_on (Union[Unset, datetime.datetime]):
        updated_by (Union[Unset, str]):
    """

    values: Union[Unset, str] = UNSET
    mean: Union[Unset, float] = UNSET
    sd: Union[Unset, float] = UNSET
    range_: Union[Unset, float] = UNSET
    delta: Union[Unset, float] = UNSET
    cv: Union[Unset, float] = UNSET
    cmc: Union[Unset, float] = UNSET
    mu: Union[Unset, float] = UNSET
    tur: Union[Unset, float] = UNSET
    tar: Union[Unset, float] = UNSET
    max_value: Union[Unset, float] = UNSET
    min_value: Union[Unset, float] = UNSET
    error: Union[Unset, float] = UNSET
    result: Union[Unset, str] = UNSET
    updated_on: Union[Unset, datetime.datetime] = UNSET
    updated_by: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        values = self.values

        mean = self.mean

        sd = self.sd

        range_ = self.range_

        delta = self.delta

        cv = self.cv

        cmc = self.cmc

        mu = self.mu

        tur = self.tur

        tar = self.tar

        max_value = self.max_value

        min_value = self.min_value

        error = self.error

        result = self.result

        updated_on: Union[Unset, str] = UNSET
        if not isinstance(self.updated_on, Unset):
            updated_on = self.updated_on.isoformat()

        updated_by = self.updated_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if values is not UNSET:
            field_dict["Values"] = values
        if mean is not UNSET:
            field_dict["Mean"] = mean
        if sd is not UNSET:
            field_dict["SD"] = sd
        if range_ is not UNSET:
            field_dict["Range"] = range_
        if delta is not UNSET:
            field_dict["Delta"] = delta
        if cv is not UNSET:
            field_dict["CV"] = cv
        if cmc is not UNSET:
            field_dict["CMC"] = cmc
        if mu is not UNSET:
            field_dict["MU"] = mu
        if tur is not UNSET:
            field_dict["TUR"] = tur
        if tar is not UNSET:
            field_dict["TAR"] = tar
        if max_value is not UNSET:
            field_dict["MaxValue"] = max_value
        if min_value is not UNSET:
            field_dict["MinValue"] = min_value
        if error is not UNSET:
            field_dict["Error"] = error
        if result is not UNSET:
            field_dict["Result"] = result
        if updated_on is not UNSET:
            field_dict["UpdatedOn"] = updated_on
        if updated_by is not UNSET:
            field_dict["UpdatedBy"] = updated_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        values = d.pop("Values", UNSET)

        mean = d.pop("Mean", UNSET)

        sd = d.pop("SD", UNSET)

        range_ = d.pop("Range", UNSET)

        delta = d.pop("Delta", UNSET)

        cv = d.pop("CV", UNSET)

        cmc = d.pop("CMC", UNSET)

        mu = d.pop("MU", UNSET)

        tur = d.pop("TUR", UNSET)

        tar = d.pop("TAR", UNSET)

        max_value = d.pop("MaxValue", UNSET)

        min_value = d.pop("MinValue", UNSET)

        error = d.pop("Error", UNSET)

        result = d.pop("Result", UNSET)

        _updated_on = d.pop("UpdatedOn", UNSET)
        updated_on: Union[Unset, datetime.datetime]
        if isinstance(_updated_on, Unset):
            updated_on = UNSET
        else:
            updated_on = isoparse(_updated_on)

        updated_by = d.pop("UpdatedBy", UNSET)

        qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_measurement_set_response_model_measurement_point_response_model_measurement_response_model = cls(
            values=values,
            mean=mean,
            sd=sd,
            range_=range_,
            delta=delta,
            cv=cv,
            cmc=cmc,
            mu=mu,
            tur=tur,
            tar=tar,
            max_value=max_value,
            min_value=min_value,
            error=error,
            result=result,
            updated_on=updated_on,
            updated_by=updated_by,
        )

        qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_measurement_set_response_model_measurement_point_response_model_measurement_response_model.additional_properties = (
            d
        )
        return qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_measurement_set_response_model_measurement_point_response_model_measurement_response_model

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
