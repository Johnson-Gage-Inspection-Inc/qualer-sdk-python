import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.qualer_api_models_clients_from_asset_model_asset_status import (
    QualerApiModelsClientsFromAssetModelAssetStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsClientsFromAssetModel")


@_attrs_define
class QualerApiModelsClientsFromAssetModel:
    """
    Attributes:
        site_id (Union[None, Unset, int]):
        product_id (Union[None, Unset, int]):
        manufacturer (Union[None, Unset, str]):
        manufacturer_part_number (Union[None, Unset, str]):
        category_id (Union[None, Unset, int]):
        serial_number (Union[None, Unset, str]):
        asset_tag (Union[None, Unset, str]):
        asset_user (Union[None, Unset, str]):
        asset_status (Union[None, Unset, QualerApiModelsClientsFromAssetModelAssetStatus]):
        asset_name (Union[None, Unset, str]):
        asset_description (Union[None, Unset, str]):
        asset_maker (Union[None, Unset, str]):
        location (Union[None, Unset, str]):
        retirement_reason (Union[None, Unset, str]):
        barcode (Union[None, Unset, str]):
        legacy_identifier (Union[None, Unset, str]):
        condition (Union[None, Unset, str]):
        criticality (Union[None, Unset, str]):
        purchase_date (Union[None, Unset, datetime.datetime]):
        purchase_cost (Union[None, Unset, float]):
        life_span_months (Union[None, Unset, int]):
        activation_date (Union[None, Unset, datetime.datetime]):
        depreciation_basis (Union[None, Unset, float]):
        depreciation_method (Union[None, Unset, int]):
        retirement_date (Union[None, Unset, datetime.datetime]):
        salvage_value (Union[None, Unset, float]):
    """

    site_id: Union[None, Unset, int] = UNSET
    product_id: Union[None, Unset, int] = UNSET
    manufacturer: Union[None, Unset, str] = UNSET
    manufacturer_part_number: Union[None, Unset, str] = UNSET
    category_id: Union[None, Unset, int] = UNSET
    serial_number: Union[None, Unset, str] = UNSET
    asset_tag: Union[None, Unset, str] = UNSET
    asset_user: Union[None, Unset, str] = UNSET
    asset_status: Union[
        None, Unset, QualerApiModelsClientsFromAssetModelAssetStatus
    ] = UNSET
    asset_name: Union[None, Unset, str] = UNSET
    asset_description: Union[None, Unset, str] = UNSET
    asset_maker: Union[None, Unset, str] = UNSET
    location: Union[None, Unset, str] = UNSET
    retirement_reason: Union[None, Unset, str] = UNSET
    barcode: Union[None, Unset, str] = UNSET
    legacy_identifier: Union[None, Unset, str] = UNSET
    condition: Union[None, Unset, str] = UNSET
    criticality: Union[None, Unset, str] = UNSET
    purchase_date: Union[None, Unset, datetime.datetime] = UNSET
    purchase_cost: Union[None, Unset, float] = UNSET
    life_span_months: Union[None, Unset, int] = UNSET
    activation_date: Union[None, Unset, datetime.datetime] = UNSET
    depreciation_basis: Union[None, Unset, float] = UNSET
    depreciation_method: Union[None, Unset, int] = UNSET
    retirement_date: Union[None, Unset, datetime.datetime] = UNSET
    salvage_value: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        product_id = self.product_id

        manufacturer = self.manufacturer

        manufacturer_part_number = self.manufacturer_part_number

        category_id = self.category_id

        serial_number = self.serial_number

        asset_tag = self.asset_tag

        asset_user = self.asset_user

        asset_status: Union[None, Unset, str] = UNSET
        if self.asset_status and not isinstance(self.asset_status, Unset):
            asset_status = self.asset_status.value

        asset_name = self.asset_name

        asset_description = self.asset_description

        asset_maker = self.asset_maker

        location = self.location

        retirement_reason = self.retirement_reason

        barcode = self.barcode

        legacy_identifier = self.legacy_identifier

        condition = self.condition

        criticality = self.criticality

        purchase_date: Union[None, Unset, str]
        if isinstance(self.purchase_date, Unset):
            purchase_date = UNSET
        elif isinstance(self.purchase_date, datetime.datetime):
            purchase_date = self.purchase_date.isoformat()
        else:
            purchase_date = self.purchase_date

        purchase_cost = self.purchase_cost

        life_span_months = self.life_span_months

        activation_date: Union[None, Unset, str]
        if isinstance(self.activation_date, Unset):
            activation_date = UNSET
        elif isinstance(self.activation_date, datetime.datetime):
            activation_date = self.activation_date.isoformat()
        else:
            activation_date = self.activation_date

        depreciation_basis = self.depreciation_basis

        depreciation_method = self.depreciation_method

        retirement_date: Union[None, Unset, str]
        if isinstance(self.retirement_date, Unset):
            retirement_date = UNSET
        elif isinstance(self.retirement_date, datetime.datetime):
            retirement_date = self.retirement_date.isoformat()
        else:
            retirement_date = self.retirement_date

        salvage_value = self.salvage_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_id is not UNSET:
            field_dict["SiteId"] = site_id
        if product_id is not UNSET:
            field_dict["ProductId"] = product_id
        if manufacturer is not UNSET:
            field_dict["Manufacturer"] = manufacturer
        if manufacturer_part_number is not UNSET:
            field_dict["ManufacturerPartNumber"] = manufacturer_part_number
        if category_id is not UNSET:
            field_dict["CategoryId"] = category_id
        if serial_number is not UNSET:
            field_dict["SerialNumber"] = serial_number
        if asset_tag is not UNSET:
            field_dict["AssetTag"] = asset_tag
        if asset_user is not UNSET:
            field_dict["AssetUser"] = asset_user
        if asset_status is not UNSET:
            field_dict["AssetStatus"] = asset_status
        if asset_name is not UNSET:
            field_dict["AssetName"] = asset_name
        if asset_description is not UNSET:
            field_dict["AssetDescription"] = asset_description
        if asset_maker is not UNSET:
            field_dict["AssetMaker"] = asset_maker
        if location is not UNSET:
            field_dict["Location"] = location
        if retirement_reason is not UNSET:
            field_dict["RetirementReason"] = retirement_reason
        if barcode is not UNSET:
            field_dict["Barcode"] = barcode
        if legacy_identifier is not UNSET:
            field_dict["LegacyIdentifier"] = legacy_identifier
        if condition is not UNSET:
            field_dict["Condition"] = condition
        if criticality is not UNSET:
            field_dict["Criticality"] = criticality
        if purchase_date is not UNSET:
            field_dict["PurchaseDate"] = purchase_date
        if purchase_cost is not UNSET:
            field_dict["PurchaseCost"] = purchase_cost
        if life_span_months is not UNSET:
            field_dict["LifeSpanMonths"] = life_span_months
        if activation_date is not UNSET:
            field_dict["ActivationDate"] = activation_date
        if depreciation_basis is not UNSET:
            field_dict["DepreciationBasis"] = depreciation_basis
        if depreciation_method is not UNSET:
            field_dict["DepreciationMethod"] = depreciation_method
        if retirement_date is not UNSET:
            field_dict["RetirementDate"] = retirement_date
        if salvage_value is not UNSET:
            field_dict["SalvageValue"] = salvage_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        site_id = d.pop("SiteId", UNSET)

        product_id = d.pop("ProductId", UNSET)

        manufacturer = d.pop("Manufacturer", UNSET)

        manufacturer_part_number = d.pop("ManufacturerPartNumber", UNSET)

        category_id = d.pop("CategoryId", UNSET)

        serial_number = d.pop("SerialNumber", UNSET)

        asset_tag = d.pop("AssetTag", UNSET)

        asset_user = d.pop("AssetUser", UNSET)

        _asset_status = d.pop("AssetStatus", UNSET)
        asset_status: Union[
            None, Unset, QualerApiModelsClientsFromAssetModelAssetStatus
        ]
        if isinstance(_asset_status, Unset):
            asset_status = UNSET
        else:
            asset_status = QualerApiModelsClientsFromAssetModelAssetStatus(
                _asset_status
            )

        asset_name = d.pop("AssetName", UNSET)

        asset_description = d.pop("AssetDescription", UNSET)

        asset_maker = d.pop("AssetMaker", UNSET)

        location = d.pop("Location", UNSET)

        retirement_reason = d.pop("RetirementReason", UNSET)

        barcode = d.pop("Barcode", UNSET)

        legacy_identifier = d.pop("LegacyIdentifier", UNSET)

        condition = d.pop("Condition", UNSET)

        criticality = d.pop("Criticality", UNSET)

        def _parse_purchase_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                purchase_date_type_0 = isoparse(data)

                return purchase_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        purchase_date = _parse_purchase_date(d.pop("PurchaseDate", UNSET))

        purchase_cost = d.pop("PurchaseCost", UNSET)

        life_span_months = d.pop("LifeSpanMonths", UNSET)

        def _parse_activation_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                activation_date_type_0 = isoparse(data)

                return activation_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        activation_date = _parse_activation_date(d.pop("ActivationDate", UNSET))

        depreciation_basis = d.pop("DepreciationBasis", UNSET)

        depreciation_method = d.pop("DepreciationMethod", UNSET)

        def _parse_retirement_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                retirement_date_type_0 = isoparse(data)

                return retirement_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        retirement_date = _parse_retirement_date(d.pop("RetirementDate", UNSET))

        salvage_value = d.pop("SalvageValue", UNSET)

        qualer_api_models_clients_from_asset_model = cls(
            site_id=site_id,
            product_id=product_id,
            manufacturer=manufacturer,
            manufacturer_part_number=manufacturer_part_number,
            category_id=category_id,
            serial_number=serial_number,
            asset_tag=asset_tag,
            asset_user=asset_user,
            asset_status=asset_status,
            asset_name=asset_name,
            asset_description=asset_description,
            asset_maker=asset_maker,
            location=location,
            retirement_reason=retirement_reason,
            barcode=barcode,
            legacy_identifier=legacy_identifier,
            condition=condition,
            criticality=criticality,
            purchase_date=purchase_date,
            purchase_cost=purchase_cost,
            life_span_months=life_span_months,
            activation_date=activation_date,
            depreciation_basis=depreciation_basis,
            depreciation_method=depreciation_method,
            retirement_date=retirement_date,
            salvage_value=salvage_value,
        )

        qualer_api_models_clients_from_asset_model.additional_properties = d
        return qualer_api_models_clients_from_asset_model

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
