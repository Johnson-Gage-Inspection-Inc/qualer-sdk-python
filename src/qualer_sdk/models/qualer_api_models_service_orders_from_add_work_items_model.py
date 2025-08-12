from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsServiceOrdersFromAddWorkItemsModel")


@_attrs_define
class QualerApiModelsServiceOrdersFromAddWorkItemsModel:
    """
    Attributes:
        asset_ids (Union[None, Unset, list[int]]):
        schedule_segment_ids (Union[None, Unset, list[int]]):
    """

    asset_ids: Union[None, Unset, list[int]] = UNSET
    schedule_segment_ids: Union[None, Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_ids: Union[None, Unset, list[int]] = UNSET
        if self.asset_ids and not isinstance(self.asset_ids, Unset):
            asset_ids = self.asset_ids

        schedule_segment_ids: Union[None, Unset, list[int]] = UNSET
        if self.schedule_segment_ids and not isinstance(
            self.schedule_segment_ids, Unset
        ):
            schedule_segment_ids = self.schedule_segment_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_ids is not UNSET:
            field_dict["AssetIds"] = asset_ids
        if schedule_segment_ids is not UNSET:
            field_dict["ScheduleSegmentIds"] = schedule_segment_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_ids = cast(list[int], d.pop("AssetIds", UNSET))

        schedule_segment_ids = cast(list[int], d.pop("ScheduleSegmentIds", UNSET))

        qualer_api_models_service_orders_from_add_work_items_model = cls(
            asset_ids=asset_ids,
            schedule_segment_ids=schedule_segment_ids,
        )

        qualer_api_models_service_orders_from_add_work_items_model.additional_properties = (
            d
        )
        return qualer_api_models_service_orders_from_add_work_items_model

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
