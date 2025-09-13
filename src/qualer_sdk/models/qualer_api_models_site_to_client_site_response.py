import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.qualer_api_models_common_from_attribute_model import (
        CommonFromAttributeModel,
    )
    from ..models.qualer_api_models_site_to_client_site_response_billing_address_type_0 import (
        SiteToClientSiteResponseBillingAddressType0,
    )
    from ..models.qualer_api_models_site_to_client_site_response_shipping_address_type_0 import (
        SiteToClientSiteResponseShippingAddressType0,
    )


T = TypeVar("T", bound="SiteToClientSiteResponse")


@_attrs_define
class SiteToClientSiteResponse:
    """
    Attributes:
        site_id (Optional[int]):
        site_name (Optional[str]):
        site_code (Optional[str]):
        shipping_address (Union['SiteToClientSiteResponseShippingAddressType0', None]):
        shipping_inherited (Optional[bool]):
        billing_address (Union['SiteToClientSiteResponseBillingAddressType0', None]):
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
        updated_on_utc (Optional[datetime.datetime]):
        attributes (Optional[List['CommonFromAttributeModel']]):
    """

    site_id: Optional[int] = None
    site_name: Optional[str] = None
    site_code: Optional[str] = None
    shipping_address: Optional["SiteToClientSiteResponseShippingAddressType0"] = None
    shipping_inherited: Optional[bool] = None
    billing_address: Optional["SiteToClientSiteResponseBillingAddressType0"] = None
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
    updated_on_utc: Optional[datetime.datetime] = None
    attributes: Optional[List["CommonFromAttributeModel"]] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.qualer_api_models_site_to_client_site_response_billing_address_type_0 import (
            SiteToClientSiteResponseBillingAddressType0,
        )
        from ..models.qualer_api_models_site_to_client_site_response_shipping_address_type_0 import (
            SiteToClientSiteResponseShippingAddressType0,
        )

        site_id = self.site_id

        site_name = self.site_name

        site_code = self.site_code

        shipping_address: Optional[Dict[str, Any]]
        if not self.shipping_address:
            shipping_address = None
        elif isinstance(
            self.shipping_address,
            SiteToClientSiteResponseShippingAddressType0,
        ):
            shipping_address = self.shipping_address.to_dict()
        else:
            shipping_address = self.shipping_address

        shipping_inherited = self.shipping_inherited

        billing_address: Optional[Dict[str, Any]]
        if not self.billing_address:
            billing_address = None
        elif isinstance(
            self.billing_address,
            SiteToClientSiteResponseBillingAddressType0,
        ):
            billing_address = self.billing_address.to_dict()
        else:
            billing_address = self.billing_address

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

        updated_on_utc: Optional[str] = None
        if self.updated_on_utc:
            updated_on_utc = self.updated_on_utc.isoformat()

        attributes: Optional[List[Dict[str, Any]]] = None
        if self.attributes:
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()
                attributes.append(attributes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_id is not None:
            field_dict["SiteId"] = site_id
        if site_name is not None:
            field_dict["SiteName"] = site_name
        if site_code is not None:
            field_dict["SiteCode"] = site_code
        if shipping_address is not None:
            field_dict["ShippingAddress"] = shipping_address
        if shipping_inherited is not None:
            field_dict["ShippingInherited"] = shipping_inherited
        if billing_address is not None:
            field_dict["BillingAddress"] = billing_address
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
        if updated_on_utc is not None:
            field_dict["UpdatedOnUtc"] = updated_on_utc
        if attributes is not None:
            field_dict["Attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_common_from_attribute_model import (
            CommonFromAttributeModel,
        )
        from ..models.qualer_api_models_site_to_client_site_response_billing_address_type_0 import (
            SiteToClientSiteResponseBillingAddressType0,
        )
        from ..models.qualer_api_models_site_to_client_site_response_shipping_address_type_0 import (
            SiteToClientSiteResponseShippingAddressType0,
        )

        d = dict(src_dict)
        site_id = d.pop("SiteId", None)

        site_name = d.pop("SiteName", None)

        site_code = d.pop("SiteCode", None)

        def _parse_shipping_address(
            data: object,
        ) -> Optional["SiteToClientSiteResponseShippingAddressType0"]:
            if not data:
                return None
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                shipping_address_type_0 = SiteToClientSiteResponseShippingAddressType0.from_dict(
                    data
                )

                return shipping_address_type_0
            except Exception:
                pass
            return cast(
                Union[
                    "SiteToClientSiteResponseShippingAddressType0",
                    None,
                    None,
                ],
                data,
            )

        shipping_address = _parse_shipping_address(d.pop("ShippingAddress", None))

        shipping_inherited = d.pop("ShippingInherited", None)

        def _parse_billing_address(
            data: object,
        ) -> Optional["SiteToClientSiteResponseBillingAddressType0"]:
            if not data:
                return None
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                billing_address_type_0 = SiteToClientSiteResponseBillingAddressType0.from_dict(data)

                return billing_address_type_0
            except Exception:
                pass
            return cast(
                Union[
                    "SiteToClientSiteResponseBillingAddressType0",
                    None,
                    None,
                ],
                data,
            )

        billing_address = _parse_billing_address(d.pop("BillingAddress", None))

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

        _updated_on_utc = d.pop("UpdatedOnUtc", None)
        updated_on_utc: Optional[datetime.datetime]
        if not _updated_on_utc:
            updated_on_utc = None
        else:
            updated_on_utc = isoparse(_updated_on_utc)

        attributes = []
        _attributes = d.pop("Attributes", None)
        for attributes_item_data in _attributes or []:
            attributes_item = CommonFromAttributeModel.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        qualer_api_models_site_to_client_site_response = cls(
            site_id=site_id,
            site_name=site_name,
            site_code=site_code,
            shipping_address=shipping_address,
            shipping_inherited=shipping_inherited,
            billing_address=billing_address,
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
            updated_on_utc=updated_on_utc,
            attributes=attributes,
        )

        qualer_api_models_site_to_client_site_response.additional_properties = d
        return qualer_api_models_site_to_client_site_response

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
