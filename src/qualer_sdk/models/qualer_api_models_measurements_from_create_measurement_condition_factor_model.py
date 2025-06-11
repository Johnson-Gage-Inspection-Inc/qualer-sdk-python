import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="QualerApiModelsMeasurementsFromCreateMeasurementConditionFactorModel"
)


@_attrs_define
class QualerApiModelsMeasurementsFromCreateMeasurementConditionFactorModel:
    """
    Attributes:
        factor_id (Union[Unset, str]):
        factor_name (Union[Unset, str]):
        factor_value (Union[Unset, float]):
        factor_uom (Union[Unset, str]):
        last_modified_on_utc (Union[Unset, datetime.datetime]):
    """

    factor_id: Union[Unset, str] = UNSET
    factor_name: Union[Unset, str] = UNSET
    factor_value: Union[Unset, float] = UNSET
    factor_uom: Union[Unset, str] = UNSET
    last_modified_on_utc: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        factor_id = self.factor_id

        factor_name = self.factor_name

        factor_value = self.factor_value

        factor_uom = self.factor_uom

        last_modified_on_utc: Union[Unset, str] = UNSET
        if not isinstance(self.last_modified_on_utc, Unset):
            last_modified_on_utc = self.last_modified_on_utc.isoformat()

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

        _last_modified_on_utc = d.pop("LastModifiedOnUtc", UNSET)
        last_modified_on_utc: Union[Unset, datetime.datetime]
        if isinstance(_last_modified_on_utc, Unset):
            last_modified_on_utc = UNSET
        else:
            last_modified_on_utc = isoparse(_last_modified_on_utc)

        qualer_api_models_measurements_from_create_measurement_condition_factor_model = cls(
            factor_id=factor_id,
            factor_name=factor_name,
            factor_value=factor_value,
            factor_uom=factor_uom,
            last_modified_on_utc=last_modified_on_utc,
        )

        qualer_api_models_measurements_from_create_measurement_condition_factor_model.additional_properties = (
            d
        )
        return qualer_api_models_measurements_from_create_measurement_condition_factor_model

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
