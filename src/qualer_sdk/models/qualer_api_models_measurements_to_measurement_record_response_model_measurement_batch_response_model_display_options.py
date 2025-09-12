from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T",
    bound="QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelDisplayOptions",
)


@_attrs_define
class QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelDisplayOptions:
    """
    Attributes:
        err (Optional[bool]):
        mean (Optional[bool]):
        max_ (Optional[bool]):
        min_ (Optional[bool]):
        sd (Optional[bool]):
        cv (Optional[bool]):
        tar (Optional[bool]):
        tur (Optional[bool]):
        mu (Optional[bool]):
        cmc (Optional[bool]):
        tol (Optional[bool]):
        delta (Optional[bool]):
        range_ (Optional[bool]):
    """

    err: Optional[bool] = None
    mean: Optional[bool] = None
    max_: Optional[bool] = None
    min_: Optional[bool] = None
    sd: Optional[bool] = None
    cv: Optional[bool] = None
    tar: Optional[bool] = None
    tur: Optional[bool] = None
    mu: Optional[bool] = None
    cmc: Optional[bool] = None
    tol: Optional[bool] = None
    delta: Optional[bool] = None
    range_: Optional[bool] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        err = self.err

        mean = self.mean

        max_ = self.max_

        min_ = self.min_

        sd = self.sd

        cv = self.cv

        tar = self.tar

        tur = self.tur

        mu = self.mu

        cmc = self.cmc

        tol = self.tol

        delta = self.delta

        range_ = self.range_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if err is not None:
            field_dict["Err"] = err
        if mean is not None:
            field_dict["Mean"] = mean
        if max_ is not None:
            field_dict["Max"] = max_
        if min_ is not None:
            field_dict["Min"] = min_
        if sd is not None:
            field_dict["Sd"] = sd
        if cv is not None:
            field_dict["Cv"] = cv
        if tar is not None:
            field_dict["Tar"] = tar
        if tur is not None:
            field_dict["Tur"] = tur
        if mu is not None:
            field_dict["Mu"] = mu
        if cmc is not None:
            field_dict["Cmc"] = cmc
        if tol is not None:
            field_dict["Tol"] = tol
        if delta is not None:
            field_dict["Delta"] = delta
        if range_ is not None:
            field_dict["Range"] = range_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        err = d.pop("Err", None)

        mean = d.pop("Mean", None)

        max_ = d.pop("Max", None)

        min_ = d.pop("Min", None)

        sd = d.pop("Sd", None)

        cv = d.pop("Cv", None)

        tar = d.pop("Tar", None)

        tur = d.pop("Tur", None)

        mu = d.pop("Mu", None)

        cmc = d.pop("Cmc", None)

        tol = d.pop("Tol", None)

        delta = d.pop("Delta", None)

        range_ = d.pop("Range", None)

        qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_display_options = cls(
            err=err,
            mean=mean,
            max_=max_,
            min_=min_,
            sd=sd,
            cv=cv,
            tar=tar,
            tur=tur,
            mu=mu,
            cmc=cmc,
            tol=tol,
            delta=delta,
            range_=range_,
        )

        qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_display_options.additional_properties = (
            d
        )
        return qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_display_options

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
