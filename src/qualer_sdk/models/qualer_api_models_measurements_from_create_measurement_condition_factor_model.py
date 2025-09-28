import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="MeasurementsFromCreateMeasurementConditionFactorModel")


@_attrs_define
class MeasurementsFromCreateMeasurementConditionFactorModel:
    """
    Attributes:
        factor_id (Optional[str]):
        factor_name (Optional[str]):
        factor_value (Optional[float]):
        factor_uom (Optional[str]):
        last_modified_on_utc (Optional[datetime.datetime]):
    """

    factor_id: Optional[str] = None
    factor_name: Optional[str] = None
    factor_value: Optional[float] = None
    factor_uom: Optional[str] = None
    last_modified_on_utc: Optional[datetime.datetime] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        factor_id = self.factor_id
        factor_name = self.factor_name
        factor_value = self.factor_value
        factor_uom = self.factor_uom
        last_modified_on_utc = self.last_modified_on_utc.isoformat() if self.last_modified_on_utc else None
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if factor_id is not None:
            field_dict["FactorId"] = factor_id
        if factor_name is not None:
            field_dict["FactorName"] = factor_name
        if factor_value is not None:
            field_dict["FactorValue"] = factor_value
        if factor_uom is not None:
            field_dict["FactorUom"] = factor_uom
        if last_modified_on_utc is not None:
            field_dict["LastModifiedOnUtc"] = last_modified_on_utc
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        factor_id = d.pop("FactorId", None)
        factor_name = d.pop("FactorName", None)
        factor_value = d.pop("FactorValue", None)
        factor_uom = d.pop("FactorUom", None)
        def _parse_last_modified_on_utc(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_modified_on_utc_type_0 = isoparse(data)
                return last_modified_on_utc_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)
        last_modified_on_utc = _parse_last_modified_on_utc(d.pop("LastModifiedOnUtc", None))
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
