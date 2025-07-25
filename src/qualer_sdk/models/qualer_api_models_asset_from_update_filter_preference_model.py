import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsAssetFromUpdateFilterPreferenceModel")


@_attrs_define
class QualerApiModelsAssetFromUpdateFilterPreferenceModel:
    """
    Attributes:
        filter_type (Union[Unset, str]):
        within_days (Union[Unset, int]):
        use_date_range (Union[Unset, bool]):
        start_date (Union[None, Unset, datetime.datetime]):
        end_date (Union[None, Unset, datetime.datetime]):
    """

    filter_type: Union[Unset, str] = UNSET
    within_days: Union[Unset, int] = UNSET
    use_date_range: Union[Unset, bool] = UNSET
    start_date: Union[None, Unset, datetime.datetime] = UNSET
    end_date: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_type = self.filter_type

        within_days = self.within_days

        use_date_range = self.use_date_range

        start_date: Union[None, Unset, str]
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.datetime):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_type is not UNSET:
            field_dict["FilterType"] = filter_type
        if within_days is not UNSET:
            field_dict["WithinDays"] = within_days
        if use_date_range is not UNSET:
            field_dict["UseDateRange"] = use_date_range
        if start_date is not UNSET:
            field_dict["StartDate"] = start_date
        if end_date is not UNSET:
            field_dict["EndDate"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filter_type = d.pop("FilterType", UNSET)

        within_days = d.pop("WithinDays", UNSET)

        use_date_range = d.pop("UseDateRange", UNSET)

        def _parse_start_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data)

                return start_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        start_date = _parse_start_date(d.pop("StartDate", UNSET))

        def _parse_end_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data)

                return end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        end_date = _parse_end_date(d.pop("EndDate", UNSET))

        qualer_api_models_asset_from_update_filter_preference_model = cls(
            filter_type=filter_type,
            within_days=within_days,
            use_date_range=use_date_range,
            start_date=start_date,
            end_date=end_date,
        )

        qualer_api_models_asset_from_update_filter_preference_model.additional_properties = (
            d
        )
        return qualer_api_models_asset_from_update_filter_preference_model

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
