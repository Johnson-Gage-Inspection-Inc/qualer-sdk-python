from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsAssetToAssetsCountResponseModel")


@_attrs_define
class QualerApiModelsAssetToAssetsCountResponseModel:
    """
    Attributes:
        assets_all (Union[Unset, int]):
        assets_collected (Union[Unset, int]):
        assets_recently_serviced (Union[Unset, int]):
        assets_due (Union[Unset, int]):
        assets_past_due (Union[Unset, int]):
        assets_service_pending (Union[Unset, int]):
        assets_recently_purchased (Union[Unset, int]):
        assets_warranty_expires (Union[Unset, int]):
        assets_due_for_replacement (Union[Unset, int]):
        assets_out_of_service (Union[Unset, int]):
        assets_not_serviced (Union[Unset, int]):
        assets_without_schedule (Union[Unset, int]):
        assets_without_vendor (Union[Unset, int]):
        assets_without_product (Union[Unset, int]):
        assets_added (Union[Unset, int]):
        assets_updated (Union[Unset, int]):
        assets_deleted (Union[Unset, int]):
        assets_no_agreement (Union[Unset, int]):
        assets_expired_agreement (Union[Unset, int]):
        assets_expiring_soon_agreement (Union[Unset, int]):
    """

    assets_all: Union[Unset, int] = UNSET
    assets_collected: Union[Unset, int] = UNSET
    assets_recently_serviced: Union[Unset, int] = UNSET
    assets_due: Union[Unset, int] = UNSET
    assets_past_due: Union[Unset, int] = UNSET
    assets_service_pending: Union[Unset, int] = UNSET
    assets_recently_purchased: Union[Unset, int] = UNSET
    assets_warranty_expires: Union[Unset, int] = UNSET
    assets_due_for_replacement: Union[Unset, int] = UNSET
    assets_out_of_service: Union[Unset, int] = UNSET
    assets_not_serviced: Union[Unset, int] = UNSET
    assets_without_schedule: Union[Unset, int] = UNSET
    assets_without_vendor: Union[Unset, int] = UNSET
    assets_without_product: Union[Unset, int] = UNSET
    assets_added: Union[Unset, int] = UNSET
    assets_updated: Union[Unset, int] = UNSET
    assets_deleted: Union[Unset, int] = UNSET
    assets_no_agreement: Union[Unset, int] = UNSET
    assets_expired_agreement: Union[Unset, int] = UNSET
    assets_expiring_soon_agreement: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assets_all is not UNSET:
            field_dict["AssetsAll"] = assets_all
        if assets_collected is not UNSET:
            field_dict["AssetsCollected"] = assets_collected
        if assets_recently_serviced is not UNSET:
            field_dict["AssetsRecentlyServiced"] = assets_recently_serviced
        if assets_due is not UNSET:
            field_dict["AssetsDue"] = assets_due
        if assets_past_due is not UNSET:
            field_dict["AssetsPastDue"] = assets_past_due
        if assets_service_pending is not UNSET:
            field_dict["AssetsServicePending"] = assets_service_pending
        if assets_recently_purchased is not UNSET:
            field_dict["AssetsRecentlyPurchased"] = assets_recently_purchased
        if assets_warranty_expires is not UNSET:
            field_dict["AssetsWarrantyExpires"] = assets_warranty_expires
        if assets_due_for_replacement is not UNSET:
            field_dict["AssetsDueForReplacement"] = assets_due_for_replacement
        if assets_out_of_service is not UNSET:
            field_dict["AssetsOutOfService"] = assets_out_of_service
        if assets_not_serviced is not UNSET:
            field_dict["AssetsNotServiced"] = assets_not_serviced
        if assets_without_schedule is not UNSET:
            field_dict["AssetsWithoutSchedule"] = assets_without_schedule
        if assets_without_vendor is not UNSET:
            field_dict["AssetsWithoutVendor"] = assets_without_vendor
        if assets_without_product is not UNSET:
            field_dict["AssetsWithoutProduct"] = assets_without_product
        if assets_added is not UNSET:
            field_dict["AssetsAdded"] = assets_added
        if assets_updated is not UNSET:
            field_dict["AssetsUpdated"] = assets_updated
        if assets_deleted is not UNSET:
            field_dict["AssetsDeleted"] = assets_deleted
        if assets_no_agreement is not UNSET:
            field_dict["AssetsNoAgreement"] = assets_no_agreement
        if assets_expired_agreement is not UNSET:
            field_dict["AssetsExpiredAgreement"] = assets_expired_agreement
        if assets_expiring_soon_agreement is not UNSET:
            field_dict["AssetsExpiringSoonAgreement"] = assets_expiring_soon_agreement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assets_all = d.pop("AssetsAll", UNSET)

        assets_collected = d.pop("AssetsCollected", UNSET)

        assets_recently_serviced = d.pop("AssetsRecentlyServiced", UNSET)

        assets_due = d.pop("AssetsDue", UNSET)

        assets_past_due = d.pop("AssetsPastDue", UNSET)

        assets_service_pending = d.pop("AssetsServicePending", UNSET)

        assets_recently_purchased = d.pop("AssetsRecentlyPurchased", UNSET)

        assets_warranty_expires = d.pop("AssetsWarrantyExpires", UNSET)

        assets_due_for_replacement = d.pop("AssetsDueForReplacement", UNSET)

        assets_out_of_service = d.pop("AssetsOutOfService", UNSET)

        assets_not_serviced = d.pop("AssetsNotServiced", UNSET)

        assets_without_schedule = d.pop("AssetsWithoutSchedule", UNSET)

        assets_without_vendor = d.pop("AssetsWithoutVendor", UNSET)

        assets_without_product = d.pop("AssetsWithoutProduct", UNSET)

        assets_added = d.pop("AssetsAdded", UNSET)

        assets_updated = d.pop("AssetsUpdated", UNSET)

        assets_deleted = d.pop("AssetsDeleted", UNSET)

        assets_no_agreement = d.pop("AssetsNoAgreement", UNSET)

        assets_expired_agreement = d.pop("AssetsExpiredAgreement", UNSET)

        assets_expiring_soon_agreement = d.pop("AssetsExpiringSoonAgreement", UNSET)

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
