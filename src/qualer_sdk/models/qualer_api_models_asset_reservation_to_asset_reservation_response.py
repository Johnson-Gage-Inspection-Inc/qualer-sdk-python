import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="AssetReservationToAssetReservationResponse")


@_attrs_define
class AssetReservationToAssetReservationResponse:
    """
    Attributes:
        original_begin_date (Optional[datetime.datetime]):
        original_end_date (Optional[datetime.datetime]):
        begin_date (Optional[datetime.datetime]):
        end_date (Optional[datetime.datetime]):
        reserved_on (Optional[datetime.datetime]):
        reserved_on_utc (Optional[datetime.datetime]):
        comments (Optional[str]):
        product_id (Optional[int]):
        asset_id (Optional[int]):
        service_order_id (Optional[int]):
        reserved_by_id (Optional[int]):
        reserved_by_name (Optional[str]):
    """

    original_begin_date: Optional[datetime.datetime] = None
    original_end_date: Optional[datetime.datetime] = None
    begin_date: Optional[datetime.datetime] = None
    end_date: Optional[datetime.datetime] = None
    reserved_on: Optional[datetime.datetime] = None
    reserved_on_utc: Optional[datetime.datetime] = None
    comments: Optional[str] = None
    product_id: Optional[int] = None
    asset_id: Optional[int] = None
    service_order_id: Optional[int] = None
    reserved_by_id: Optional[int] = None
    reserved_by_name: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        original_begin_date: Optional[str] = None
        if self.original_begin_date:
            original_begin_date = self.original_begin_date.isoformat()
        original_end_date: Optional[str] = None
        if self.original_end_date:
            original_end_date = self.original_end_date.isoformat()
        begin_date: Optional[str] = None
        if self.begin_date:
            begin_date = self.begin_date.isoformat()
        end_date: Optional[str] = None
        if self.end_date:
            end_date = self.end_date.isoformat()
        reserved_on: Optional[str] = None
        if self.reserved_on:
            reserved_on = self.reserved_on.isoformat()
        reserved_on_utc: Optional[str] = None
        if self.reserved_on_utc:
            reserved_on_utc = self.reserved_on_utc.isoformat()
        comments = self.comments
        product_id = self.product_id
        asset_id = self.asset_id
        service_order_id = self.service_order_id
        reserved_by_id = self.reserved_by_id
        reserved_by_name = self.reserved_by_name
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if original_begin_date is not None:
            field_dict["OriginalBeginDate"] = original_begin_date
        if original_end_date is not None:
            field_dict["OriginalEndDate"] = original_end_date
        if begin_date is not None:
            field_dict["BeginDate"] = begin_date
        if end_date is not None:
            field_dict["EndDate"] = end_date
        if reserved_on is not None:
            field_dict["ReservedOn"] = reserved_on
        if reserved_on_utc is not None:
            field_dict["ReservedOnUtc"] = reserved_on_utc
        if comments is not None:
            field_dict["Comments"] = comments
        if product_id is not None:
            field_dict["ProductId"] = product_id
        if asset_id is not None:
            field_dict["AssetId"] = asset_id
        if service_order_id is not None:
            field_dict["ServiceOrderId"] = service_order_id
        if reserved_by_id is not None:
            field_dict["ReservedById"] = reserved_by_id
        if reserved_by_name is not None:
            field_dict["ReservedByName"] = reserved_by_name
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _original_begin_date = d.pop("OriginalBeginDate", None)
        original_begin_date: Optional[datetime.datetime]
        if not _original_begin_date:
            original_begin_date = None
        else:
            original_begin_date = isoparse(_original_begin_date)
        _original_end_date = d.pop("OriginalEndDate", None)
        original_end_date: Optional[datetime.datetime]
        if not _original_end_date:
            original_end_date = None
        else:
            original_end_date = isoparse(_original_end_date)
        _begin_date = d.pop("BeginDate", None)
        begin_date: Optional[datetime.datetime]
        if not _begin_date:
            begin_date = None
        else:
            begin_date = isoparse(_begin_date)
        _end_date = d.pop("EndDate", None)
        end_date: Optional[datetime.datetime]
        if not _end_date:
            end_date = None
        else:
            end_date = isoparse(_end_date)
        _reserved_on = d.pop("ReservedOn", None)
        reserved_on: Optional[datetime.datetime]
        if not _reserved_on:
            reserved_on = None
        else:
            reserved_on = isoparse(_reserved_on)
        _reserved_on_utc = d.pop("ReservedOnUtc", None)
        reserved_on_utc: Optional[datetime.datetime]
        if not _reserved_on_utc:
            reserved_on_utc = None
        else:
            reserved_on_utc = isoparse(_reserved_on_utc)
        comments = d.pop("Comments", None)
        product_id = d.pop("ProductId", None)
        asset_id = d.pop("AssetId", None)
        service_order_id = d.pop("ServiceOrderId", None)
        reserved_by_id = d.pop("ReservedById", None)
        reserved_by_name = d.pop("ReservedByName", None)
        qualer_api_models_asset_reservation_to_asset_reservation_response = cls(
            original_begin_date=original_begin_date,
            original_end_date=original_end_date,
            begin_date=begin_date,
            end_date=end_date,
            reserved_on=reserved_on,
            reserved_on_utc=reserved_on_utc,
            comments=comments,
            product_id=product_id,
            asset_id=asset_id,
            service_order_id=service_order_id,
            reserved_by_id=reserved_by_id,
            reserved_by_name=reserved_by_name,
        )
        qualer_api_models_asset_reservation_to_asset_reservation_response.additional_properties = d
        return qualer_api_models_asset_reservation_to_asset_reservation_response

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
