import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="AssetToEmployeeFilterPreferenceResponseModel")


@_attrs_define
class AssetToEmployeeFilterPreferenceResponseModel:
    """
    Attributes:
        filter_type (Optional[str]):
        within_days (Optional[int]):
        use_date_range (Optional[bool]):
        start_date (Optional[datetime.datetime]):
        end_date (Optional[datetime.datetime]):
    """

    filter_type: Optional[str] = None
    within_days: Optional[int] = None
    use_date_range: Optional[bool] = None
    start_date: Optional[datetime.datetime] = None
    end_date: Optional[datetime.datetime] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filter_type = self.filter_type
        within_days = self.within_days
        use_date_range = self.use_date_range
        start_date = self.start_date.isoformat() if self.start_date else None
        end_date = self.end_date.isoformat() if self.end_date else None
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_type is not None:
            field_dict["FilterType"] = filter_type
        if within_days is not None:
            field_dict["WithinDays"] = within_days
        if use_date_range is not None:
            field_dict["UseDateRange"] = use_date_range
        if start_date is not None:
            field_dict["StartDate"] = start_date
        if end_date is not None:
            field_dict["EndDate"] = end_date
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filter_type = d.pop("FilterType", None)
        within_days = d.pop("WithinDays", None)
        use_date_range = d.pop("UseDateRange", None)
        def _parse_start_date(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data)
                return start_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)
        start_date = _parse_start_date(d.pop("StartDate", None))
        def _parse_end_date(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data)
                return end_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)
        end_date = _parse_end_date(d.pop("EndDate", None))
        qualer_api_models_asset_to_employee_filter_preference_response_model = cls(
            filter_type=filter_type,
            within_days=within_days,
            use_date_range=use_date_range,
            start_date=start_date,
            end_date=end_date,
        )
        qualer_api_models_asset_to_employee_filter_preference_response_model.additional_properties = (
            d
        )
        return qualer_api_models_asset_to_employee_filter_preference_response_model

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
