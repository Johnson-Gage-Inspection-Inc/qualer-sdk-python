import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualer_api_models_common_from_attribute_model import (
        QualerApiModelsCommonFromAttributeModel,
    )
    from ..models.qualer_api_models_site_to_client_site_response_billing_address_type_0 import (
        QualerApiModelsSiteToClientSiteResponseBillingAddressType0,
    )
    from ..models.qualer_api_models_site_to_client_site_response_shipping_address_type_0 import (
        QualerApiModelsSiteToClientSiteResponseShippingAddressType0,
    )


T = TypeVar("T", bound="QualerApiModelsSiteToClientSiteResponse")


@_attrs_define
class QualerApiModelsSiteToClientSiteResponse:
    """
    Attributes:
        site_id (Union[Unset, int]):
        site_name (Union[Unset, str]):
        site_code (Union[Unset, str]):
        shipping_address (Union['QualerApiModelsSiteToClientSiteResponseShippingAddressType0', None, Unset]):
        shipping_inherited (Union[Unset, bool]):
        billing_address (Union['QualerApiModelsSiteToClientSiteResponseBillingAddressType0', None, Unset]):
        default_account_representative_employee_id (Union[Unset, int]):
        billing_inherited (Union[Unset, bool]):
        federal_number (Union[Unset, str]):
        state_number (Union[Unset, str]):
        culture_name (Union[Unset, str]):
        is_science_facility (Union[Unset, bool]):
        is_service_center (Union[Unset, bool]):
        is_inventory_storage (Union[Unset, bool]):
        is_production (Union[Unset, bool]):
        time_zone_id (Union[Unset, str]):
        time_zone_offset_minutes (Union[Unset, int]):
        updated_on_utc (Union[Unset, datetime.datetime]):
        attributes (Union[Unset, list['QualerApiModelsCommonFromAttributeModel']]):
    """

    site_id: Union[Unset, int] = UNSET
    site_name: Union[Unset, str] = UNSET
    site_code: Union[Unset, str] = UNSET
    shipping_address: Union[
        "QualerApiModelsSiteToClientSiteResponseShippingAddressType0", None, Unset
    ] = UNSET
    shipping_inherited: Union[Unset, bool] = UNSET
    billing_address: Union[
        "QualerApiModelsSiteToClientSiteResponseBillingAddressType0", None, Unset
    ] = UNSET
    default_account_representative_employee_id: Union[Unset, int] = UNSET
    billing_inherited: Union[Unset, bool] = UNSET
    federal_number: Union[Unset, str] = UNSET
    state_number: Union[Unset, str] = UNSET
    culture_name: Union[Unset, str] = UNSET
    is_science_facility: Union[Unset, bool] = UNSET
    is_service_center: Union[Unset, bool] = UNSET
    is_inventory_storage: Union[Unset, bool] = UNSET
    is_production: Union[Unset, bool] = UNSET
    time_zone_id: Union[Unset, str] = UNSET
    time_zone_offset_minutes: Union[Unset, int] = UNSET
    updated_on_utc: Union[Unset, datetime.datetime] = UNSET
    attributes: Union[Unset, list["QualerApiModelsCommonFromAttributeModel"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.qualer_api_models_site_to_client_site_response_billing_address_type_0 import (
            QualerApiModelsSiteToClientSiteResponseBillingAddressType0,
        )
        from ..models.qualer_api_models_site_to_client_site_response_shipping_address_type_0 import (
            QualerApiModelsSiteToClientSiteResponseShippingAddressType0,
        )

        site_id = self.site_id

        site_name = self.site_name

        site_code = self.site_code

        shipping_address: Union[None, Unset, dict[str, Any]]
        if isinstance(self.shipping_address, Unset):
            shipping_address = UNSET
        elif isinstance(
            self.shipping_address,
            QualerApiModelsSiteToClientSiteResponseShippingAddressType0,
        ):
            shipping_address = self.shipping_address.to_dict()
        else:
            shipping_address = self.shipping_address

        shipping_inherited = self.shipping_inherited

        billing_address: Union[None, Unset, dict[str, Any]]
        if isinstance(self.billing_address, Unset):
            billing_address = UNSET
        elif isinstance(
            self.billing_address,
            QualerApiModelsSiteToClientSiteResponseBillingAddressType0,
        ):
            billing_address = self.billing_address.to_dict()
        else:
            billing_address = self.billing_address

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

        updated_on_utc: Union[Unset, str] = UNSET
        if not isinstance(self.updated_on_utc, Unset):
            updated_on_utc = self.updated_on_utc.isoformat()

        attributes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()
                attributes.append(attributes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_id is not UNSET:
            field_dict["SiteId"] = site_id
        if site_name is not UNSET:
            field_dict["SiteName"] = site_name
        if site_code is not UNSET:
            field_dict["SiteCode"] = site_code
        if shipping_address is not UNSET:
            field_dict["ShippingAddress"] = shipping_address
        if shipping_inherited is not UNSET:
            field_dict["ShippingInherited"] = shipping_inherited
        if billing_address is not UNSET:
            field_dict["BillingAddress"] = billing_address
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
        if updated_on_utc is not UNSET:
            field_dict["UpdatedOnUtc"] = updated_on_utc
        if attributes is not UNSET:
            field_dict["Attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_common_from_attribute_model import (
            QualerApiModelsCommonFromAttributeModel,
        )
        from ..models.qualer_api_models_site_to_client_site_response_billing_address_type_0 import (
            QualerApiModelsSiteToClientSiteResponseBillingAddressType0,
        )
        from ..models.qualer_api_models_site_to_client_site_response_shipping_address_type_0 import (
            QualerApiModelsSiteToClientSiteResponseShippingAddressType0,
        )

        d = dict(src_dict)
        site_id = d.pop("SiteId", UNSET)

        site_name = d.pop("SiteName", UNSET)

        site_code = d.pop("SiteCode", UNSET)

        def _parse_shipping_address(
            data: object,
        ) -> Union[
            "QualerApiModelsSiteToClientSiteResponseShippingAddressType0", None, Unset
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                shipping_address_type_0 = QualerApiModelsSiteToClientSiteResponseShippingAddressType0.from_dict(
                    data
                )

                return shipping_address_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    "QualerApiModelsSiteToClientSiteResponseShippingAddressType0",
                    None,
                    Unset,
                ],
                data,
            )

        shipping_address = _parse_shipping_address(d.pop("ShippingAddress", UNSET))

        shipping_inherited = d.pop("ShippingInherited", UNSET)

        def _parse_billing_address(
            data: object,
        ) -> Union[
            "QualerApiModelsSiteToClientSiteResponseBillingAddressType0", None, Unset
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                billing_address_type_0 = QualerApiModelsSiteToClientSiteResponseBillingAddressType0.from_dict(
                    data
                )

                return billing_address_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    "QualerApiModelsSiteToClientSiteResponseBillingAddressType0",
                    None,
                    Unset,
                ],
                data,
            )

        billing_address = _parse_billing_address(d.pop("BillingAddress", UNSET))

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

        _updated_on_utc = d.pop("UpdatedOnUtc", UNSET)
        updated_on_utc: Union[Unset, datetime.datetime]
        if isinstance(_updated_on_utc, Unset):
            updated_on_utc = UNSET
        else:
            updated_on_utc = isoparse(_updated_on_utc)

        attributes = []
        _attributes = d.pop("Attributes", UNSET)
        for attributes_item_data in _attributes or []:
            attributes_item = QualerApiModelsCommonFromAttributeModel.from_dict(
                attributes_item_data
            )

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
