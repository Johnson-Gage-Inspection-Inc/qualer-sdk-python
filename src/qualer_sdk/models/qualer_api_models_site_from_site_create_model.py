from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualer_api_models_address_address_model import (
        QualerApiModelsAddressAddressModel,
    )


T = TypeVar("T", bound="QualerApiModelsSiteFromSiteCreateModel")


@_attrs_define
class QualerApiModelsSiteFromSiteCreateModel:
    """
    Attributes:
        site_name (Union[None, Unset, str]):
        site_code (Union[None, Unset, str]):
        shipping_inherited (Union[None, Unset, bool]):
        default_account_representative_employee_id (Union[None, Unset, int]):
        billing_inherited (Union[None, Unset, bool]):
        federal_number (Union[None, Unset, str]):
        state_number (Union[None, Unset, str]):
        culture_name (Union[None, Unset, str]):
        is_science_facility (Union[None, Unset, bool]):
        is_service_center (Union[None, Unset, bool]):
        is_inventory_storage (Union[None, Unset, bool]):
        is_production (Union[None, Unset, bool]):
        time_zone_id (Union[None, Unset, str]):
        time_zone_offset_minutes (Union[None, Unset, int]):
        company_name (Union[None, Unset, str]):
        billing_address (Union[None, Unset, QualerApiModelsAddressAddressModel]):
        shipping_address (Union[None, Unset, QualerApiModelsAddressAddressModel]):
    """

    site_name: Union[None, Unset, str] = UNSET
    site_code: Union[None, Unset, str] = UNSET
    shipping_inherited: Union[None, Unset, bool] = UNSET
    default_account_representative_employee_id: Union[None, Unset, int] = UNSET
    billing_inherited: Union[None, Unset, bool] = UNSET
    federal_number: Union[None, Unset, str] = UNSET
    state_number: Union[None, Unset, str] = UNSET
    culture_name: Union[None, Unset, str] = UNSET
    is_science_facility: Union[None, Unset, bool] = UNSET
    is_service_center: Union[None, Unset, bool] = UNSET
    is_inventory_storage: Union[None, Unset, bool] = UNSET
    is_production: Union[None, Unset, bool] = UNSET
    time_zone_id: Union[None, Unset, str] = UNSET
    time_zone_offset_minutes: Union[None, Unset, int] = UNSET
    company_name: Union[None, Unset, str] = UNSET
    billing_address: Union[None, Unset, "QualerApiModelsAddressAddressModel"] = UNSET
    shipping_address: Union[None, Unset, "QualerApiModelsAddressAddressModel"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_name = self.site_name

        site_code = self.site_code

        shipping_inherited = self.shipping_inherited

        default_account_representative_employee_id = (
            self.default_account_representative_employee_id
        )

        billing_inherited = self.billing_inherited

        federal_number = self.federal_number

        state_number = self.state_number

        culture_name = self.culture_name

        is_science_facility = self.is_science_facility

        is_service_center = self.is_service_center

        is_inventory_storage = self.is_inventory_storage

        is_production = self.is_production

        time_zone_id = self.time_zone_id

        time_zone_offset_minutes = self.time_zone_offset_minutes

        company_name = self.company_name

        billing_address: Union[None, Unset, dict[str, Any]] = UNSET
        if self.billing_address and not isinstance(self.billing_address, Unset):
            billing_address = self.billing_address.to_dict()

        shipping_address: Union[None, Unset, dict[str, Any]] = UNSET
        if self.shipping_address and not isinstance(self.shipping_address, Unset):
            shipping_address = self.shipping_address.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_name is not UNSET:
            field_dict["SiteName"] = site_name
        if site_code is not UNSET:
            field_dict["SiteCode"] = site_code
        if shipping_inherited is not UNSET:
            field_dict["ShippingInherited"] = shipping_inherited
        if default_account_representative_employee_id is not UNSET:
            field_dict["DefaultAccountRepresentativeEmployeeId"] = (
                default_account_representative_employee_id
            )
        if billing_inherited is not UNSET:
            field_dict["BillingInherited"] = billing_inherited
        if federal_number is not UNSET:
            field_dict["FederalNumber"] = federal_number
        if state_number is not UNSET:
            field_dict["StateNumber"] = state_number
        if culture_name is not UNSET:
            field_dict["CultureName"] = culture_name
        if is_science_facility is not UNSET:
            field_dict["IsScienceFacility"] = is_science_facility
        if is_service_center is not UNSET:
            field_dict["IsServiceCenter"] = is_service_center
        if is_inventory_storage is not UNSET:
            field_dict["IsInventoryStorage"] = is_inventory_storage
        if is_production is not UNSET:
            field_dict["IsProduction"] = is_production
        if time_zone_id is not UNSET:
            field_dict["TimeZoneId"] = time_zone_id
        if time_zone_offset_minutes is not UNSET:
            field_dict["TimeZoneOffsetMinutes"] = time_zone_offset_minutes
        if company_name is not UNSET:
            field_dict["CompanyName"] = company_name
        if billing_address is not UNSET:
            field_dict["BillingAddress"] = billing_address
        if shipping_address is not UNSET:
            field_dict["ShippingAddress"] = shipping_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_address_address_model import (
            QualerApiModelsAddressAddressModel,
        )

        d = dict(src_dict)
        site_name = d.pop("SiteName", UNSET)

        site_code = d.pop("SiteCode", UNSET)

        shipping_inherited = d.pop("ShippingInherited", UNSET)

        default_account_representative_employee_id = d.pop(
            "DefaultAccountRepresentativeEmployeeId", UNSET
        )

        billing_inherited = d.pop("BillingInherited", UNSET)

        federal_number = d.pop("FederalNumber", UNSET)

        state_number = d.pop("StateNumber", UNSET)

        culture_name = d.pop("CultureName", UNSET)

        is_science_facility = d.pop("IsScienceFacility", UNSET)

        is_service_center = d.pop("IsServiceCenter", UNSET)

        is_inventory_storage = d.pop("IsInventoryStorage", UNSET)

        is_production = d.pop("IsProduction", UNSET)

        time_zone_id = d.pop("TimeZoneId", UNSET)

        time_zone_offset_minutes = d.pop("TimeZoneOffsetMinutes", UNSET)

        company_name = d.pop("CompanyName", UNSET)

        _billing_address = d.pop("BillingAddress", UNSET)
        billing_address: Union[None, Unset, QualerApiModelsAddressAddressModel]
        if isinstance(_billing_address, Unset):
            billing_address = UNSET
        else:
            billing_address = QualerApiModelsAddressAddressModel.from_dict(
                _billing_address
            )

        _shipping_address = d.pop("ShippingAddress", UNSET)
        shipping_address: Union[None, Unset, QualerApiModelsAddressAddressModel]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = QualerApiModelsAddressAddressModel.from_dict(
                _shipping_address
            )

        qualer_api_models_site_from_site_create_model = cls(
            site_name=site_name,
            site_code=site_code,
            shipping_inherited=shipping_inherited,
            default_account_representative_employee_id=default_account_representative_employee_id,
            billing_inherited=billing_inherited,
            federal_number=federal_number,
            state_number=state_number,
            culture_name=culture_name,
            is_science_facility=is_science_facility,
            is_service_center=is_service_center,
            is_inventory_storage=is_inventory_storage,
            is_production=is_production,
            time_zone_id=time_zone_id,
            time_zone_offset_minutes=time_zone_offset_minutes,
            company_name=company_name,
            billing_address=billing_address,
            shipping_address=shipping_address,
        )

        qualer_api_models_site_from_site_create_model.additional_properties = d
        return qualer_api_models_site_from_site_create_model

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
