import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsAssetReservationToAssetReservationResponse")


@_attrs_define
class QualerApiModelsAssetReservationToAssetReservationResponse:
    """
    Attributes:
        original_begin_date (Union[None, Unset, datetime.datetime]):
        original_end_date (Union[None, Unset, datetime.datetime]):
        begin_date (Union[None, Unset, datetime.datetime]):
        end_date (Union[None, Unset, datetime.datetime]):
        reserved_on (Union[Unset, datetime.datetime]):
        reserved_on_utc (Union[Unset, datetime.datetime]):
        comments (Union[Unset, str]):
        product_id (Union[Unset, int]):
        asset_id (Union[Unset, int]):
        service_order_id (Union[Unset, int]):
        reserved_by_id (Union[Unset, int]):
        reserved_by_name (Union[Unset, str]):
    """

    original_begin_date: Union[None, Unset, datetime.datetime] = UNSET
    original_end_date: Union[None, Unset, datetime.datetime] = UNSET
    begin_date: Union[None, Unset, datetime.datetime] = UNSET
    end_date: Union[None, Unset, datetime.datetime] = UNSET
    reserved_on: Union[Unset, datetime.datetime] = UNSET
    reserved_on_utc: Union[Unset, datetime.datetime] = UNSET
    comments: Union[Unset, str] = UNSET
    product_id: Union[Unset, int] = UNSET
    asset_id: Union[Unset, int] = UNSET
    service_order_id: Union[Unset, int] = UNSET
    reserved_by_id: Union[Unset, int] = UNSET
    reserved_by_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        original_begin_date: Union[None, Unset, str]
        if isinstance(self.original_begin_date, Unset):
            original_begin_date = UNSET
        elif isinstance(self.original_begin_date, datetime.datetime):
            original_begin_date = self.original_begin_date.isoformat()
        else:
            original_begin_date = self.original_begin_date

        original_end_date: Union[None, Unset, str]
        if isinstance(self.original_end_date, Unset):
            original_end_date = UNSET
        elif isinstance(self.original_end_date, datetime.datetime):
            original_end_date = self.original_end_date.isoformat()
        else:
            original_end_date = self.original_end_date

        begin_date: Union[None, Unset, str]
        if isinstance(self.begin_date, Unset):
            begin_date = UNSET
        elif isinstance(self.begin_date, datetime.datetime):
            begin_date = self.begin_date.isoformat()
        else:
            begin_date = self.begin_date

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        reserved_on: Union[Unset, str] = UNSET
        if not isinstance(self.reserved_on, Unset):
            reserved_on = self.reserved_on.isoformat()

        reserved_on_utc: Union[Unset, str] = UNSET
        if not isinstance(self.reserved_on_utc, Unset):
            reserved_on_utc = self.reserved_on_utc.isoformat()

        comments = self.comments

        product_id = self.product_id

        asset_id = self.asset_id

        service_order_id = self.service_order_id

        reserved_by_id = self.reserved_by_id

        reserved_by_name = self.reserved_by_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if original_begin_date is not UNSET:
            field_dict["OriginalBeginDate"] = original_begin_date
        if original_end_date is not UNSET:
            field_dict["OriginalEndDate"] = original_end_date
        if begin_date is not UNSET:
            field_dict["BeginDate"] = begin_date
        if end_date is not UNSET:
            field_dict["EndDate"] = end_date
        if reserved_on is not UNSET:
            field_dict["ReservedOn"] = reserved_on
        if reserved_on_utc is not UNSET:
            field_dict["ReservedOnUtc"] = reserved_on_utc
        if comments is not UNSET:
            field_dict["Comments"] = comments
        if product_id is not UNSET:
            field_dict["ProductId"] = product_id
        if asset_id is not UNSET:
            field_dict["AssetId"] = asset_id
        if service_order_id is not UNSET:
            field_dict["ServiceOrderId"] = service_order_id
        if reserved_by_id is not UNSET:
            field_dict["ReservedById"] = reserved_by_id
        if reserved_by_name is not UNSET:
            field_dict["ReservedByName"] = reserved_by_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_original_begin_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                original_begin_date_type_0 = isoparse(data)

                return original_begin_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        original_begin_date = _parse_original_begin_date(
            d.pop("OriginalBeginDate", UNSET)
        )

        def _parse_original_end_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                original_end_date_type_0 = isoparse(data)

                return original_end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        original_end_date = _parse_original_end_date(d.pop("OriginalEndDate", UNSET))

        def _parse_begin_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                begin_date_type_0 = isoparse(data)

                return begin_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        begin_date = _parse_begin_date(d.pop("BeginDate", UNSET))

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

        _reserved_on = d.pop("ReservedOn", UNSET)
        reserved_on: Union[Unset, datetime.datetime]
        if isinstance(_reserved_on, Unset):
            reserved_on = UNSET
        else:
            if _reserved_on is None:

                reserved_on = None

            else:

                reserved_on = isoparse(_reserved_on)

        _reserved_on_utc = d.pop("ReservedOnUtc", UNSET)
        reserved_on_utc: Union[Unset, datetime.datetime]
        if isinstance(_reserved_on_utc, Unset):
            reserved_on_utc = UNSET
        else:
            if _reserved_on_utc is None:

                reserved_on_utc = None

            else:

                reserved_on_utc = isoparse(_reserved_on_utc)

        comments = d.pop("Comments", UNSET)

        product_id = d.pop("ProductId", UNSET)

        asset_id = d.pop("AssetId", UNSET)

        service_order_id = d.pop("ServiceOrderId", UNSET)

        reserved_by_id = d.pop("ReservedById", UNSET)

        reserved_by_name = d.pop("ReservedByName", UNSET)

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

        qualer_api_models_asset_reservation_to_asset_reservation_response.additional_properties = (
            d
        )
        return qualer_api_models_asset_reservation_to_asset_reservation_response

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
