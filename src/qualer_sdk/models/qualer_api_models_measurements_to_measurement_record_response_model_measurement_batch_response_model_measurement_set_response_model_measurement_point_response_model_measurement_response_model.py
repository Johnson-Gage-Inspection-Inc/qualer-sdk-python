import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar(
    "T",
    bound="QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModelMeasurementResponseModel",
)


@_attrs_define
class QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModelMeasurementResponseModel:
    """
    Attributes:
        values (Optional[str]):
        mean (Optional[float]):
        sd (Optional[float]):
        range_ (Optional[float]):
        delta (Optional[float]):
        cv (Optional[float]):
        cmc (Optional[float]):
        mu (Optional[float]):
        tur (Optional[float]):
        tar (Optional[float]):
        max_value (Optional[float]):
        min_value (Optional[float]):
        error (Optional[float]):
        result (Optional[str]):
        updated_on (Optional[datetime.datetime]):
        updated_by (Optional[str]):
    """

    values: Optional[str] = None
    mean: Optional[float] = None
    sd: Optional[float] = None
    range_: Optional[float] = None
    delta: Optional[float] = None
    cv: Optional[float] = None
    cmc: Optional[float] = None
    mu: Optional[float] = None
    tur: Optional[float] = None
    tar: Optional[float] = None
    max_value: Optional[float] = None
    min_value: Optional[float] = None
    error: Optional[float] = None
    result: Optional[str] = None
    updated_on: Optional[datetime.datetime] = None
    updated_by: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        updated_on: Optional[str] = None
        if self.updated_on:
            updated_on = self.updated_on.isoformat()

        updated_by = self.updated_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if values is not None:
            field_dict["Values"] = values
        if mean is not None:
            field_dict["Mean"] = mean
        if sd is not None:
            field_dict["SD"] = sd
        if range_ is not None:
            field_dict["Range"] = range_
        if delta is not None:
            field_dict["Delta"] = delta
        if cv is not None:
            field_dict["CV"] = cv
        if cmc is not None:
            field_dict["CMC"] = cmc
        if mu is not None:
            field_dict["MU"] = mu
        if tur is not None:
            field_dict["TUR"] = tur
        if tar is not None:
            field_dict["TAR"] = tar
        if max_value is not None:
            field_dict["MaxValue"] = max_value
        if min_value is not None:
            field_dict["MinValue"] = min_value
        if error is not None:
            field_dict["Error"] = error
        if result is not None:
            field_dict["Result"] = result
        if updated_on is not None:
            field_dict["UpdatedOn"] = updated_on
        if updated_by is not None:
            field_dict["UpdatedBy"] = updated_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        values = d.pop("Values", None)

        mean = d.pop("Mean", None)

        sd = d.pop("SD", None)

        range_ = d.pop("Range", None)

        delta = d.pop("Delta", None)

        cv = d.pop("CV", None)

        cmc = d.pop("CMC", None)

        mu = d.pop("MU", None)

        tur = d.pop("TUR", None)

        tar = d.pop("TAR", None)

        max_value = d.pop("MaxValue", None)

        min_value = d.pop("MinValue", None)

        error = d.pop("Error", None)

        result = d.pop("Result", None)

        _updated_on = d.pop("UpdatedOn", None)
        updated_on: Optional[datetime.datetime]
        if not _updated_on:
            updated_on = None
        else:
            updated_on = isoparse(_updated_on)

        updated_by = d.pop("UpdatedBy", None)

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
