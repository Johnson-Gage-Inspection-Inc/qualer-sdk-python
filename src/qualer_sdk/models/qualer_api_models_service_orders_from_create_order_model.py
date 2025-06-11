from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsServiceOrdersFromCreateOrderModel")


@_attrs_define
class QualerApiModelsServiceOrdersFromCreateOrderModel:
    """
    Attributes:
        client_company_id (Union[Unset, int]):
        vendor_site_id (Union[Unset, int]):
        asset_ids (Union[Unset, list[int]]):
        schedule_segment_ids (Union[Unset, list[int]]):
        service_level_ids (Union[Unset, list[int]]):
        use_due_segments (Union[Unset, bool]):
        order_notes (Union[Unset, str]):
    """

    client_company_id: Union[Unset, int] = UNSET
    vendor_site_id: Union[Unset, int] = UNSET
    asset_ids: Union[Unset, list[int]] = UNSET
    schedule_segment_ids: Union[Unset, list[int]] = UNSET
    service_level_ids: Union[Unset, list[int]] = UNSET
    use_due_segments: Union[Unset, bool] = UNSET
    order_notes: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_company_id = self.client_company_id

        vendor_site_id = self.vendor_site_id

        asset_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.asset_ids, Unset):
            asset_ids = self.asset_ids

        schedule_segment_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.schedule_segment_ids, Unset):
            schedule_segment_ids = self.schedule_segment_ids

        service_level_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.service_level_ids, Unset):
            service_level_ids = self.service_level_ids

        use_due_segments = self.use_due_segments

        order_notes = self.order_notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_company_id is not UNSET:
            field_dict["ClientCompanyId"] = client_company_id
        if vendor_site_id is not UNSET:
            field_dict["VendorSiteId"] = vendor_site_id
        if asset_ids is not UNSET:
            field_dict["AssetIds"] = asset_ids
        if schedule_segment_ids is not UNSET:
            field_dict["ScheduleSegmentIds"] = schedule_segment_ids
        if service_level_ids is not UNSET:
            field_dict["ServiceLevelIds"] = service_level_ids
        if use_due_segments is not UNSET:
            field_dict["UseDueSegments"] = use_due_segments
        if order_notes is not UNSET:
            field_dict["OrderNotes"] = order_notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_company_id = d.pop("ClientCompanyId", UNSET)

        vendor_site_id = d.pop("VendorSiteId", UNSET)

        asset_ids = cast(list[int], d.pop("AssetIds", UNSET))

        schedule_segment_ids = cast(list[int], d.pop("ScheduleSegmentIds", UNSET))

        service_level_ids = cast(list[int], d.pop("ServiceLevelIds", UNSET))

        use_due_segments = d.pop("UseDueSegments", UNSET)

        order_notes = d.pop("OrderNotes", UNSET)

        qualer_api_models_service_orders_from_create_order_model = cls(
            client_company_id=client_company_id,
            vendor_site_id=vendor_site_id,
            asset_ids=asset_ids,
            schedule_segment_ids=schedule_segment_ids,
            service_level_ids=service_level_ids,
            use_due_segments=use_due_segments,
            order_notes=order_notes,
        )

        qualer_api_models_service_orders_from_create_order_model.additional_properties = (
            d
        )
        return qualer_api_models_service_orders_from_create_order_model

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
