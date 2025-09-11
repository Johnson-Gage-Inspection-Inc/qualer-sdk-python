from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QualerApiModelsServiceOrdersFromCreateOrderModel")


@_attrs_define
class QualerApiModelsServiceOrdersFromCreateOrderModel:
    """
    Attributes:
        client_company_id (Optional[int]):
        vendor_site_id (Optional[int]):
        asset_ids (Optional[List[int]]):
        schedule_segment_ids (Optional[List[int]]):
        service_level_ids (Optional[List[int]]):
        use_due_segments (Optional[bool]):
        order_notes (Optional[str]):
    """

    client_company_id: Optional[int] = None
    vendor_site_id: Optional[int] = None
    asset_ids: Optional[List[int]] = None
    schedule_segment_ids: Optional[List[int]] = None
    service_level_ids: Optional[List[int]] = None
    use_due_segments: Optional[bool] = None
    order_notes: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_company_id = self.client_company_id

        vendor_site_id = self.vendor_site_id

        asset_ids: Optional[List[int]] = None
        if self.asset_ids:
            asset_ids = self.asset_ids

        schedule_segment_ids: Optional[List[int]] = None
        if self.schedule_segment_ids and not isinstance(self.schedule_segment_ids, None):
            schedule_segment_ids = self.schedule_segment_ids

        service_level_ids: Optional[List[int]] = None
        if self.service_level_ids:
            service_level_ids = self.service_level_ids

        use_due_segments = self.use_due_segments

        order_notes = self.order_notes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_company_id is not None:
            field_dict["ClientCompanyId"] = client_company_id
        if vendor_site_id is not None:
            field_dict["VendorSiteId"] = vendor_site_id
        if asset_ids is not None:
            field_dict["AssetIds"] = asset_ids
        if schedule_segment_ids is not None:
            field_dict["ScheduleSegmentIds"] = schedule_segment_ids
        if service_level_ids is not None:
            field_dict["ServiceLevelIds"] = service_level_ids
        if use_due_segments is not None:
            field_dict["UseDueSegments"] = use_due_segments
        if order_notes is not None:
            field_dict["OrderNotes"] = order_notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_company_id = d.pop("ClientCompanyId", None)

        vendor_site_id = d.pop("VendorSiteId", None)

        asset_ids = cast(List[int], d.pop("AssetIds", None))

        schedule_segment_ids = cast(List[int], d.pop("ScheduleSegmentIds", None))

        service_level_ids = cast(List[int], d.pop("ServiceLevelIds", None))

        use_due_segments = d.pop("UseDueSegments", None)

        order_notes = d.pop("OrderNotes", None)

        qualer_api_models_service_orders_from_create_order_model = cls(
            client_company_id=client_company_id,
            vendor_site_id=vendor_site_id,
            asset_ids=asset_ids,
            schedule_segment_ids=schedule_segment_ids,
            service_level_ids=service_level_ids,
            use_due_segments=use_due_segments,
            order_notes=order_notes,
        )

        qualer_api_models_service_orders_from_create_order_model.additional_properties = d
        return qualer_api_models_service_orders_from_create_order_model

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
