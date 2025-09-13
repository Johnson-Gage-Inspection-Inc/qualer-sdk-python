from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AssetToAssetsCountResponseModel")


@_attrs_define
class AssetToAssetsCountResponseModel:
    """
    Attributes:
        assets_all (Optional[int]):
        assets_collected (Optional[int]):
        assets_recently_serviced (Optional[int]):
        assets_due (Optional[int]):
        assets_past_due (Optional[int]):
        assets_service_pending (Optional[int]):
        assets_recently_purchased (Optional[int]):
        assets_warranty_expires (Optional[int]):
        assets_due_for_replacement (Optional[int]):
        assets_out_of_service (Optional[int]):
        assets_not_serviced (Optional[int]):
        assets_without_schedule (Optional[int]):
        assets_without_vendor (Optional[int]):
        assets_without_product (Optional[int]):
        assets_added (Optional[int]):
        assets_updated (Optional[int]):
        assets_deleted (Optional[int]):
        assets_no_agreement (Optional[int]):
        assets_expired_agreement (Optional[int]):
        assets_expiring_soon_agreement (Optional[int]):
    """

    assets_all: Optional[int] = None
    assets_collected: Optional[int] = None
    assets_recently_serviced: Optional[int] = None
    assets_due: Optional[int] = None
    assets_past_due: Optional[int] = None
    assets_service_pending: Optional[int] = None
    assets_recently_purchased: Optional[int] = None
    assets_warranty_expires: Optional[int] = None
    assets_due_for_replacement: Optional[int] = None
    assets_out_of_service: Optional[int] = None
    assets_not_serviced: Optional[int] = None
    assets_without_schedule: Optional[int] = None
    assets_without_vendor: Optional[int] = None
    assets_without_product: Optional[int] = None
    assets_added: Optional[int] = None
    assets_updated: Optional[int] = None
    assets_deleted: Optional[int] = None
    assets_no_agreement: Optional[int] = None
    assets_expired_agreement: Optional[int] = None
    assets_expiring_soon_agreement: Optional[int] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        assets_all = self.assets_all

        assets_collected = self.assets_collected

        assets_recently_serviced = self.assets_recently_serviced

        assets_due = self.assets_due

        assets_past_due = self.assets_past_due

        assets_service_pending = self.assets_service_pending

        assets_recently_purchased = self.assets_recently_purchased

        assets_warranty_expires = self.assets_warranty_expires

        assets_due_for_replacement = self.assets_due_for_replacement

        assets_out_of_service = self.assets_out_of_service

        assets_not_serviced = self.assets_not_serviced

        assets_without_schedule = self.assets_without_schedule

        assets_without_vendor = self.assets_without_vendor

        assets_without_product = self.assets_without_product

        assets_added = self.assets_added

        assets_updated = self.assets_updated

        assets_deleted = self.assets_deleted

        assets_no_agreement = self.assets_no_agreement

        assets_expired_agreement = self.assets_expired_agreement

        assets_expiring_soon_agreement = self.assets_expiring_soon_agreement

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assets_all is not None:
            field_dict["AssetsAll"] = assets_all
        if assets_collected is not None:
            field_dict["AssetsCollected"] = assets_collected
        if assets_recently_serviced is not None:
            field_dict["AssetsRecentlyServiced"] = assets_recently_serviced
        if assets_due is not None:
            field_dict["AssetsDue"] = assets_due
        if assets_past_due is not None:
            field_dict["AssetsPastDue"] = assets_past_due
        if assets_service_pending is not None:
            field_dict["AssetsServicePending"] = assets_service_pending
        if assets_recently_purchased is not None:
            field_dict["AssetsRecentlyPurchased"] = assets_recently_purchased
        if assets_warranty_expires is not None:
            field_dict["AssetsWarrantyExpires"] = assets_warranty_expires
        if assets_due_for_replacement is not None:
            field_dict["AssetsDueForReplacement"] = assets_due_for_replacement
        if assets_out_of_service is not None:
            field_dict["AssetsOutOfService"] = assets_out_of_service
        if assets_not_serviced is not None:
            field_dict["AssetsNotServiced"] = assets_not_serviced
        if assets_without_schedule is not None:
            field_dict["AssetsWithoutSchedule"] = assets_without_schedule
        if assets_without_vendor is not None:
            field_dict["AssetsWithoutVendor"] = assets_without_vendor
        if assets_without_product is not None:
            field_dict["AssetsWithoutProduct"] = assets_without_product
        if assets_added is not None:
            field_dict["AssetsAdded"] = assets_added
        if assets_updated is not None:
            field_dict["AssetsUpdated"] = assets_updated
        if assets_deleted is not None:
            field_dict["AssetsDeleted"] = assets_deleted
        if assets_no_agreement is not None:
            field_dict["AssetsNoAgreement"] = assets_no_agreement
        if assets_expired_agreement is not None:
            field_dict["AssetsExpiredAgreement"] = assets_expired_agreement
        if assets_expiring_soon_agreement is not None:
            field_dict["AssetsExpiringSoonAgreement"] = assets_expiring_soon_agreement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assets_all = d.pop("AssetsAll", None)

        assets_collected = d.pop("AssetsCollected", None)

        assets_recently_serviced = d.pop("AssetsRecentlyServiced", None)

        assets_due = d.pop("AssetsDue", None)

        assets_past_due = d.pop("AssetsPastDue", None)

        assets_service_pending = d.pop("AssetsServicePending", None)

        assets_recently_purchased = d.pop("AssetsRecentlyPurchased", None)

        assets_warranty_expires = d.pop("AssetsWarrantyExpires", None)

        assets_due_for_replacement = d.pop("AssetsDueForReplacement", None)

        assets_out_of_service = d.pop("AssetsOutOfService", None)

        assets_not_serviced = d.pop("AssetsNotServiced", None)

        assets_without_schedule = d.pop("AssetsWithoutSchedule", None)

        assets_without_vendor = d.pop("AssetsWithoutVendor", None)

        assets_without_product = d.pop("AssetsWithoutProduct", None)

        assets_added = d.pop("AssetsAdded", None)

        assets_updated = d.pop("AssetsUpdated", None)

        assets_deleted = d.pop("AssetsDeleted", None)

        assets_no_agreement = d.pop("AssetsNoAgreement", None)

        assets_expired_agreement = d.pop("AssetsExpiredAgreement", None)

        assets_expiring_soon_agreement = d.pop("AssetsExpiringSoonAgreement", None)

        qualer_api_models_asset_to_assets_count_response_model = cls(
            assets_all=assets_all,
            assets_collected=assets_collected,
            assets_recently_serviced=assets_recently_serviced,
            assets_due=assets_due,
            assets_past_due=assets_past_due,
            assets_service_pending=assets_service_pending,
            assets_recently_purchased=assets_recently_purchased,
            assets_warranty_expires=assets_warranty_expires,
            assets_due_for_replacement=assets_due_for_replacement,
            assets_out_of_service=assets_out_of_service,
            assets_not_serviced=assets_not_serviced,
            assets_without_schedule=assets_without_schedule,
            assets_without_vendor=assets_without_vendor,
            assets_without_product=assets_without_product,
            assets_added=assets_added,
            assets_updated=assets_updated,
            assets_deleted=assets_deleted,
            assets_no_agreement=assets_no_agreement,
            assets_expired_agreement=assets_expired_agreement,
            assets_expiring_soon_agreement=assets_expiring_soon_agreement,
        )

        qualer_api_models_asset_to_assets_count_response_model.additional_properties = d
        return qualer_api_models_asset_to_assets_count_response_model

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
