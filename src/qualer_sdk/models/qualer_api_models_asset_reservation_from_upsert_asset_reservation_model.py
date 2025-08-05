import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsAssetReservationFromUpsertAssetReservationModel")


@_attrs_define
class QualerApiModelsAssetReservationFromUpsertAssetReservationModel:
    """
    Attributes:
        asset_id (Union[Unset, int]):
        product_id (Union[Unset, int]):
        reservation_id (Union[Unset, int]):
        service_order_id (Union[Unset, int]):
        begin_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        reserved_by (Union[Unset, int]):
        reserved_by_name (Union[Unset, str]):
        comments (Union[Unset, str]):
    """

    asset_id: Union[Unset, int] = UNSET
    product_id: Union[Unset, int] = UNSET
    reservation_id: Union[Unset, int] = UNSET
    service_order_id: Union[Unset, int] = UNSET
    begin_date: Union[Unset, datetime.datetime] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    reserved_by: Union[Unset, int] = UNSET
    reserved_by_name: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        product_id = self.product_id

        reservation_id = self.reservation_id

        service_order_id = self.service_order_id

        begin_date: Union[Unset, str] = UNSET
        if not isinstance(self.begin_date, Unset):
            begin_date = self.begin_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        reserved_by = self.reserved_by

        reserved_by_name = self.reserved_by_name

        comments = self.comments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["AssetId"] = asset_id
        if product_id is not UNSET:
            field_dict["ProductId"] = product_id
        if reservation_id is not UNSET:
            field_dict["ReservationId"] = reservation_id
        if service_order_id is not UNSET:
            field_dict["ServiceOrderId"] = service_order_id
        if begin_date is not UNSET:
            field_dict["BeginDate"] = begin_date
        if end_date is not UNSET:
            field_dict["EndDate"] = end_date
        if reserved_by is not UNSET:
            field_dict["ReservedBy"] = reserved_by
        if reserved_by_name is not UNSET:
            field_dict["ReservedByName"] = reserved_by_name
        if comments is not UNSET:
            field_dict["Comments"] = comments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = d.pop("AssetId", UNSET)

        product_id = d.pop("ProductId", UNSET)

        reservation_id = d.pop("ReservationId", UNSET)

        service_order_id = d.pop("ServiceOrderId", UNSET)

        _begin_date = d.pop("BeginDate", UNSET)
        begin_date: Union[Unset, datetime.datetime]
        if isinstance(_begin_date, Unset):
            begin_date = UNSET
        else:
            begin_date = isoparse(_begin_date)

        _end_date = d.pop("EndDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        reserved_by = d.pop("ReservedBy", UNSET)

        reserved_by_name = d.pop("ReservedByName", UNSET)

        comments = d.pop("Comments", UNSET)

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
