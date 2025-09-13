import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="AssetReservationFromUpsertAssetReservationModel")


@_attrs_define
class AssetReservationFromUpsertAssetReservationModel:
    """
    Attributes:
        asset_id (Optional[int]):
        product_id (Optional[int]):
        reservation_id (Optional[int]):
        service_order_id (Optional[int]):
        begin_date (Optional[datetime.datetime]):
        end_date (Optional[datetime.datetime]):
        reserved_by (Optional[int]):
        reserved_by_name (Optional[str]):
        comments (Optional[str]):
    """

    asset_id: Optional[int] = None
    product_id: Optional[int] = None
    reservation_id: Optional[int] = None
    service_order_id: Optional[int] = None
    begin_date: Optional[datetime.datetime] = None
    end_date: Optional[datetime.datetime] = None
    reserved_by: Optional[int] = None
    reserved_by_name: Optional[str] = None
    comments: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asset_id = self.asset_id

        product_id = self.product_id

        reservation_id = self.reservation_id

        service_order_id = self.service_order_id

        begin_date: Optional[str] = None
        if self.begin_date:
            begin_date = self.begin_date.isoformat()

        end_date: Optional[str] = None
        if self.end_date:
            end_date = self.end_date.isoformat()

        reserved_by = self.reserved_by

        reserved_by_name = self.reserved_by_name

        comments = self.comments

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not None:
            field_dict["AssetId"] = asset_id
        if product_id is not None:
            field_dict["ProductId"] = product_id
        if reservation_id is not None:
            field_dict["ReservationId"] = reservation_id
        if service_order_id is not None:
            field_dict["ServiceOrderId"] = service_order_id
        if begin_date is not None:
            field_dict["BeginDate"] = begin_date
        if end_date is not None:
            field_dict["EndDate"] = end_date
        if reserved_by is not None:
            field_dict["ReservedBy"] = reserved_by
        if reserved_by_name is not None:
            field_dict["ReservedByName"] = reserved_by_name
        if comments is not None:
            field_dict["Comments"] = comments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = d.pop("AssetId", None)

        product_id = d.pop("ProductId", None)

        reservation_id = d.pop("ReservationId", None)

        service_order_id = d.pop("ServiceOrderId", None)

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

        reserved_by = d.pop("ReservedBy", None)

        reserved_by_name = d.pop("ReservedByName", None)

        comments = d.pop("Comments", None)

        qualer_api_models_asset_reservation_from_upsert_asset_reservation_model = cls(
            asset_id=asset_id,
            product_id=product_id,
            reservation_id=reservation_id,
            service_order_id=service_order_id,
            begin_date=begin_date,
            end_date=end_date,
            reserved_by=reserved_by,
            reserved_by_name=reserved_by_name,
            comments=comments,
        )

        qualer_api_models_asset_reservation_from_upsert_asset_reservation_model.additional_properties = (
            d
        )
        return qualer_api_models_asset_reservation_from_upsert_asset_reservation_model

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
