from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.qualer_api_models_address_address_model import AddressAddressModel


T = TypeVar("T", bound="SiteFromSiteCreateModel")


@_attrs_define
class SiteFromSiteCreateModel:
    """
    Attributes:
        site_name (Optional[str]):
        site_code (Optional[str]):
        shipping_inherited (Optional[bool]):
        default_account_representative_employee_id (Optional[int]):
        billing_inherited (Optional[bool]):
        federal_number (Optional[str]):
        state_number (Optional[str]):
        culture_name (Optional[str]):
        is_science_facility (Optional[bool]):
        is_service_center (Optional[bool]):
        is_inventory_storage (Optional[bool]):
        is_production (Optional[bool]):
        time_zone_id (Optional[str]):
        time_zone_offset_minutes (Optional[int]):
        company_name (Optional[str]):
        billing_address (Optional[AddressAddressModel]):
        shipping_address (Optional[AddressAddressModel]):
    """

    site_name: Optional[str] = None
    site_code: Optional[str] = None
    shipping_inherited: Optional[bool] = None
    default_account_representative_employee_id: Optional[int] = None
    billing_inherited: Optional[bool] = None
    federal_number: Optional[str] = None
    state_number: Optional[str] = None
    culture_name: Optional[str] = None
    is_science_facility: Optional[bool] = None
    is_service_center: Optional[bool] = None
    is_inventory_storage: Optional[bool] = None
    is_production: Optional[bool] = None
    time_zone_id: Optional[str] = None
    time_zone_offset_minutes: Optional[int] = None
    company_name: Optional[str] = None
    billing_address: Optional["AddressAddressModel"] = None
    shipping_address: Optional["AddressAddressModel"] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        site_name = self.site_name

        site_code = self.site_code

        shipping_inherited = self.shipping_inherited

        default_account_representative_employee_id = self.default_account_representative_employee_id

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

        billing_address: Optional[Dict[str, Any]] = None
        if self.billing_address:
            billing_address = self.billing_address.to_dict()

        shipping_address: Optional[Dict[str, Any]] = None
        if self.shipping_address:
            shipping_address = self.shipping_address.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_name is not None:
            field_dict["SiteName"] = site_name
        if site_code is not None:
            field_dict["SiteCode"] = site_code
        if shipping_inherited is not None:
            field_dict["ShippingInherited"] = shipping_inherited
        if default_account_representative_employee_id is not None:
            field_dict["DefaultAccountRepresentativeEmployeeId"] = (
                default_account_representative_employee_id
            )
        if billing_inherited is not None:
            field_dict["BillingInherited"] = billing_inherited
        if federal_number is not None:
            field_dict["FederalNumber"] = federal_number
        if state_number is not None:
            field_dict["StateNumber"] = state_number
        if culture_name is not None:
            field_dict["CultureName"] = culture_name
        if is_science_facility is not None:
            field_dict["IsScienceFacility"] = is_science_facility
        if is_service_center is not None:
            field_dict["IsServiceCenter"] = is_service_center
        if is_inventory_storage is not None:
            field_dict["IsInventoryStorage"] = is_inventory_storage
        if is_production is not None:
            field_dict["IsProduction"] = is_production
        if time_zone_id is not None:
            field_dict["TimeZoneId"] = time_zone_id
        if time_zone_offset_minutes is not None:
            field_dict["TimeZoneOffsetMinutes"] = time_zone_offset_minutes
        if company_name is not None:
            field_dict["CompanyName"] = company_name
        if billing_address is not None:
            field_dict["BillingAddress"] = billing_address
        if shipping_address is not None:
            field_dict["ShippingAddress"] = shipping_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_address_address_model import (
            AddressAddressModel,
        )

        d = dict(src_dict)
        site_name = d.pop("SiteName", None)

        site_code = d.pop("SiteCode", None)

        shipping_inherited = d.pop("ShippingInherited", None)

        default_account_representative_employee_id = d.pop(
            "DefaultAccountRepresentativeEmployeeId", None
        )

        billing_inherited = d.pop("BillingInherited", None)

        federal_number = d.pop("FederalNumber", None)

        state_number = d.pop("StateNumber", None)

        culture_name = d.pop("CultureName", None)

        is_science_facility = d.pop("IsScienceFacility", None)

        is_service_center = d.pop("IsServiceCenter", None)

        is_inventory_storage = d.pop("IsInventoryStorage", None)

        is_production = d.pop("IsProduction", None)

        time_zone_id = d.pop("TimeZoneId", None)

        time_zone_offset_minutes = d.pop("TimeZoneOffsetMinutes", None)

        company_name = d.pop("CompanyName", None)

        _billing_address = d.pop("BillingAddress", None)
        billing_address: Optional[AddressAddressModel]
        if not _billing_address:
            billing_address = None
        else:
            billing_address = AddressAddressModel.from_dict(_billing_address)

        _shipping_address = d.pop("ShippingAddress", None)
        shipping_address: Optional[AddressAddressModel]
        if not _shipping_address:
            shipping_address = None
        else:
            shipping_address = AddressAddressModel.from_dict(_shipping_address)

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
