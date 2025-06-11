from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsMeasurementsFromDisplayOptions")


@_attrs_define
class QualerApiModelsMeasurementsFromDisplayOptions:
    """
    Attributes:
        err (Union[Unset, bool]):
        mean (Union[Unset, bool]):
        max_ (Union[Unset, bool]):
        min_ (Union[Unset, bool]):
        sd (Union[Unset, bool]):
        cv (Union[Unset, bool]):
        tar (Union[Unset, bool]):
        tur (Union[Unset, bool]):
        mu (Union[Unset, bool]):
        cmc (Union[Unset, bool]):
        tol (Union[Unset, bool]):
        delta (Union[Unset, bool]):
        range_ (Union[Unset, bool]):
    """

    err: Union[Unset, bool] = UNSET
    mean: Union[Unset, bool] = UNSET
    max_: Union[Unset, bool] = UNSET
    min_: Union[Unset, bool] = UNSET
    sd: Union[Unset, bool] = UNSET
    cv: Union[Unset, bool] = UNSET
    tar: Union[Unset, bool] = UNSET
    tur: Union[Unset, bool] = UNSET
    mu: Union[Unset, bool] = UNSET
    cmc: Union[Unset, bool] = UNSET
    tol: Union[Unset, bool] = UNSET
    delta: Union[Unset, bool] = UNSET
    range_: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if err is not UNSET:
            field_dict["Err"] = err
        if mean is not UNSET:
            field_dict["Mean"] = mean
        if max_ is not UNSET:
            field_dict["Max"] = max_
        if min_ is not UNSET:
            field_dict["Min"] = min_
        if sd is not UNSET:
            field_dict["Sd"] = sd
        if cv is not UNSET:
            field_dict["Cv"] = cv
        if tar is not UNSET:
            field_dict["Tar"] = tar
        if tur is not UNSET:
            field_dict["Tur"] = tur
        if mu is not UNSET:
            field_dict["Mu"] = mu
        if cmc is not UNSET:
            field_dict["Cmc"] = cmc
        if tol is not UNSET:
            field_dict["Tol"] = tol
        if delta is not UNSET:
            field_dict["Delta"] = delta
        if range_ is not UNSET:
            field_dict["Range"] = range_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        err = d.pop("Err", UNSET)

        mean = d.pop("Mean", UNSET)

        max_ = d.pop("Max", UNSET)

        min_ = d.pop("Min", UNSET)

        sd = d.pop("Sd", UNSET)

        cv = d.pop("Cv", UNSET)

        tar = d.pop("Tar", UNSET)

        tur = d.pop("Tur", UNSET)

        mu = d.pop("Mu", UNSET)

        cmc = d.pop("Cmc", UNSET)

        tol = d.pop("Tol", UNSET)

        delta = d.pop("Delta", UNSET)

        range_ = d.pop("Range", UNSET)

        qualer_api_models_measurements_from_display_options = cls(
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

        qualer_api_models_measurements_from_display_options.additional_properties = d
        return qualer_api_models_measurements_from_display_options

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
