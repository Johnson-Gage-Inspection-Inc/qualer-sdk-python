import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.qualer_api_models_clients_from_asset_model_asset_status import (
    QualerApiModelsClientsFromAssetModelAssetStatus,
)

T = TypeVar("T", bound="QualerApiModelsClientsFromAssetModel")


@_attrs_define
class QualerApiModelsClientsFromAssetModel:
    """
    Attributes:
        site_id (Optional[int]):
        product_id (Optional[int]):
        manufacturer (Optional[str]):
        manufacturer_part_number (Optional[str]):
        category_id (Optional[int]):
        serial_number (Optional[str]):
        asset_tag (Optional[str]):
        asset_user (Optional[str]):
        asset_status (Optional[QualerApiModelsClientsFromAssetModelAssetStatus]):
        asset_name (Optional[str]):
        asset_description (Optional[str]):
        asset_maker (Optional[str]):
        location (Optional[str]):
        retirement_reason (Optional[str]):
        barcode (Optional[str]):
        legacy_identifier (Optional[str]):
        condition (Optional[str]):
        criticality (Optional[str]):
        purchase_date (Optional[datetime.datetime]):
        purchase_cost (Optional[float]):
        life_span_months (Optional[int]):
        activation_date (Optional[datetime.datetime]):
        depreciation_basis (Optional[float]):
        depreciation_method (Optional[int]):
        retirement_date (Optional[datetime.datetime]):
        salvage_value (Optional[float]):
    """

    site_id: Optional[int] = None
    product_id: Optional[int] = None
    manufacturer: Optional[str] = None
    manufacturer_part_number: Optional[str] = None
    category_id: Optional[int] = None
    serial_number: Optional[str] = None
    asset_tag: Optional[str] = None
    asset_user: Optional[str] = None
    asset_status: Optional[QualerApiModelsClientsFromAssetModelAssetStatus] = None
    asset_name: Optional[str] = None
    asset_description: Optional[str] = None
    asset_maker: Optional[str] = None
    location: Optional[str] = None
    retirement_reason: Optional[str] = None
    barcode: Optional[str] = None
    legacy_identifier: Optional[str] = None
    condition: Optional[str] = None
    criticality: Optional[str] = None
    purchase_date: Optional[datetime.datetime] = None
    purchase_cost: Optional[float] = None
    life_span_months: Optional[int] = None
    activation_date: Optional[datetime.datetime] = None
    depreciation_basis: Optional[float] = None
    depreciation_method: Optional[int] = None
    retirement_date: Optional[datetime.datetime] = None
    salvage_value: Optional[float] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        # Simple value copies
        site_id = self.site_id
        product_id = self.product_id
        manufacturer = self.manufacturer
        manufacturer_part_number = self.manufacturer_part_number
        category_id = self.category_id
        serial_number = self.serial_number
        asset_tag = self.asset_tag
        asset_user = self.asset_user

        # Enum and optional string fields
        asset_status: Optional[str] = (
            self.asset_status.value if self.asset_status is not None else None
        )
        asset_name = self.asset_name
        asset_description = self.asset_description
        asset_maker = self.asset_maker
        location = self.location
        retirement_reason = self.retirement_reason
        barcode = self.barcode
        legacy_identifier = self.legacy_identifier
        condition = self.condition
        criticality = self.criticality

        # Datetime fields to ISO8601 strings
        purchase_date: Optional[str]
        if self.purchase_date is None:
            purchase_date = None
        elif isinstance(self.purchase_date, datetime.datetime):
            purchase_date = self.purchase_date.isoformat()
        else:
            purchase_date = self.purchase_date

        purchase_cost = self.purchase_cost
        life_span_months = self.life_span_months

        activation_date: Optional[str]
        if self.activation_date is None:
            activation_date = None
        elif isinstance(self.activation_date, datetime.datetime):
            activation_date = self.activation_date.isoformat()
        else:
            activation_date = self.activation_date

        depreciation_basis = self.depreciation_basis
        depreciation_method = self.depreciation_method

        retirement_date: Optional[str]
        if self.retirement_date is None:
            retirement_date = None
        elif isinstance(self.retirement_date, datetime.datetime):
            retirement_date = self.retirement_date.isoformat()
        else:
            retirement_date = self.retirement_date

        salvage_value = self.salvage_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_id is not None:
            field_dict["SiteId"] = site_id
        if product_id is not None:
            field_dict["ProductId"] = product_id
        if manufacturer is not None:
            field_dict["Manufacturer"] = manufacturer
        if manufacturer_part_number is not None:
            field_dict["ManufacturerPartNumber"] = manufacturer_part_number
        if category_id is not None:
            field_dict["CategoryId"] = category_id
        if serial_number is not None:
            field_dict["SerialNumber"] = serial_number
        if asset_tag is not None:
            field_dict["AssetTag"] = asset_tag
        if asset_user is not None:
            field_dict["AssetUser"] = asset_user
        if asset_status is not None:
            field_dict["AssetStatus"] = asset_status
        if asset_name is not None:
            field_dict["AssetName"] = asset_name
        if asset_description is not None:
            field_dict["AssetDescription"] = asset_description
        if asset_maker is not None:
            field_dict["AssetMaker"] = asset_maker
        if location is not None:
            field_dict["Location"] = location
        if retirement_reason is not None:
            field_dict["RetirementReason"] = retirement_reason
        if barcode is not None:
            field_dict["Barcode"] = barcode
        if legacy_identifier is not None:
            field_dict["LegacyIdentifier"] = legacy_identifier
        if condition is not None:
            field_dict["Condition"] = condition
        if criticality is not None:
            field_dict["Criticality"] = criticality
        if purchase_date is not None:
            field_dict["PurchaseDate"] = purchase_date
        if purchase_cost is not None:
            field_dict["PurchaseCost"] = purchase_cost
        if life_span_months is not None:
            field_dict["LifeSpanMonths"] = life_span_months
        if activation_date is not None:
            field_dict["ActivationDate"] = activation_date
        if depreciation_basis is not None:
            field_dict["DepreciationBasis"] = depreciation_basis
        if depreciation_method is not None:
            field_dict["DepreciationMethod"] = depreciation_method
        if retirement_date is not None:
            field_dict["RetirementDate"] = retirement_date
        if salvage_value is not None:
            field_dict["SalvageValue"] = salvage_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        site_id = d.pop("SiteId", None)
        product_id = d.pop("ProductId", None)
        manufacturer = d.pop("Manufacturer", None)
        manufacturer_part_number = d.pop("ManufacturerPartNumber", None)
        category_id = d.pop("CategoryId", None)
        serial_number = d.pop("SerialNumber", None)
        asset_tag = d.pop("AssetTag", None)
        asset_user = d.pop("AssetUser", None)

        _asset_status = d.pop("AssetStatus", None)
        asset_status: Optional[QualerApiModelsClientsFromAssetModelAssetStatus]
        if _asset_status is None:
            asset_status = None
        else:
            asset_status = QualerApiModelsClientsFromAssetModelAssetStatus(_asset_status)

        asset_name = d.pop("AssetName", None)
        asset_description = d.pop("AssetDescription", None)
        asset_maker = d.pop("AssetMaker", None)
        location = d.pop("Location", None)
        retirement_reason = d.pop("RetirementReason", None)
        barcode = d.pop("Barcode", None)
        legacy_identifier = d.pop("LegacyIdentifier", None)
        condition = d.pop("Condition", None)
        criticality = d.pop("Criticality", None)

        def _parse_purchase_date(data: object) -> Optional[datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                purchase_date_type_0 = isoparse(data)
                return purchase_date_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        purchase_date = _parse_purchase_date(d.pop("PurchaseDate", None))
        purchase_cost = d.pop("PurchaseCost", None)
        life_span_months = d.pop("LifeSpanMonths", None)

        def _parse_activation_date(data: object) -> Optional[datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                activation_date_type_0 = isoparse(data)
                return activation_date_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        activation_date = _parse_activation_date(d.pop("ActivationDate", None))
        depreciation_basis = d.pop("DepreciationBasis", None)
        depreciation_method = d.pop("DepreciationMethod", None)

        def _parse_retirement_date(data: object) -> Optional[datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                retirement_date_type_0 = isoparse(data)
                return retirement_date_type_0
            except:  # noqa: E722
                pass
            return cast(Optional[datetime.datetime], data)

        retirement_date = _parse_retirement_date(d.pop("RetirementDate", None))
        salvage_value = d.pop("SalvageValue", None)

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
