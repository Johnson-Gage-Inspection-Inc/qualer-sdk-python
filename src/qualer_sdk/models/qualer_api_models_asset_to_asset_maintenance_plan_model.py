import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.asset_status import AssetStatus as AssetToAssetMaintenancePlanModelAssetStatus

if TYPE_CHECKING:
    from ..models.qualer_api_models_asset_to_asset_maintenance_plan_response import (
        AssetToAssetMaintenancePlanResponse,
    )


T = TypeVar("T", bound="AssetToAssetMaintenancePlanModel")


@_attrs_define
class AssetToAssetMaintenancePlanModel:
    """
    Attributes:
        maintenance_plans (Optional[List['AssetToAssetMaintenancePlanResponse']]):
        company_id (Optional[int]):
        asset_id (Optional[int]):
        serial_number (Optional[str]):
        asset_user (Optional[str]):
        asset_tag (Optional[str]):
        equipment_id (Optional[str]):
        asset_status (Optional[AssetToAssetMaintenancePlanModelAssetStatus]):
        asset_name (Optional[str]):
        asset_description (Optional[str]):
        asset_maker (Optional[str]):
        location (Optional[str]):
        room_number (Optional[str]):
        barcode (Optional[str]):
        legacy_identifier (Optional[str]):
        root_category_name (Optional[str]):
        category_name (Optional[str]):
        class_ (Optional[str]):
        custodian_email (Optional[str]):
        custodian_first_name (Optional[str]):
        custodian_last_name (Optional[str]):
        custodian_name (Optional[str]):
        department (Optional[str]):
        station (Optional[str]):
        notes (Optional[str]):
        document_number (Optional[str]):
        document_section (Optional[str]):
        cumulative_service_cost (Optional[float]):
        product_id (Optional[int]):
        manufacturer_part_number (Optional[str]):
        product_name (Optional[str]):
        product_description (Optional[str]):
        product_manufacturer (Optional[str]):
        site_name (Optional[str]):
        site_id (Optional[int]):
        condition (Optional[str]):
        criticality (Optional[str]):
        pool (Optional[str]):
        purchase_date (Optional[datetime.datetime]):
        purchase_cost (Optional[float]):
        life_span_months (Optional[int]):
        activation_date (Optional[datetime.datetime]):
        depreciation_basis (Optional[float]):
        depreciation_method (Optional[int]):
        retirement_date (Optional[datetime.datetime]):
        salvage_value (Optional[float]):
        retirment_reason (Optional[str]):
        composite_parent_id (Optional[int]):
        composite_child_count (Optional[int]):
    """

    maintenance_plans: Optional[List["AssetToAssetMaintenancePlanResponse"]] = None
    company_id: Optional[int] = None
    asset_id: Optional[int] = None
    serial_number: Optional[str] = None
    asset_user: Optional[str] = None
    asset_tag: Optional[str] = None
    equipment_id: Optional[str] = None
    asset_status: Optional["AssetToAssetMaintenancePlanModelAssetStatus"] = None
    asset_name: Optional[str] = None
    asset_description: Optional[str] = None
    asset_maker: Optional[str] = None
    location: Optional[str] = None
    room_number: Optional[str] = None
    barcode: Optional[str] = None
    legacy_identifier: Optional[str] = None
    root_category_name: Optional[str] = None
    category_name: Optional[str] = None
    class_: Optional[str] = None
    custodian_email: Optional[str] = None
    custodian_first_name: Optional[str] = None
    custodian_last_name: Optional[str] = None
    custodian_name: Optional[str] = None
    department: Optional[str] = None
    station: Optional[str] = None
    notes: Optional[str] = None
    document_number: Optional[str] = None
    document_section: Optional[str] = None
    cumulative_service_cost: Optional[float] = None
    product_id: Optional[int] = None
    manufacturer_part_number: Optional[str] = None
    product_name: Optional[str] = None
    product_description: Optional[str] = None
    product_manufacturer: Optional[str] = None
    site_name: Optional[str] = None
    site_id: Optional[int] = None
    condition: Optional[str] = None
    criticality: Optional[str] = None
    pool: Optional[str] = None
    purchase_date: Optional[datetime.datetime] = None
    purchase_cost: Optional[float] = None
    life_span_months: Optional[int] = None
    activation_date: Optional[datetime.datetime] = None
    depreciation_basis: Optional[float] = None
    depreciation_method: Optional[int] = None
    retirement_date: Optional[datetime.datetime] = None
    salvage_value: Optional[float] = None
    retirment_reason: Optional[str] = None
    composite_parent_id: Optional[int] = None
    composite_child_count: Optional[int] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        maintenance_plans: Optional[List[Dict[str, Any]]] = None
        if self.maintenance_plans:
            maintenance_plans = []
            for maintenance_plans_item_data in self.maintenance_plans:
                maintenance_plans_item = maintenance_plans_item_data.to_dict()
                maintenance_plans.append(maintenance_plans_item)
        company_id = self.company_id
        asset_id = self.asset_id
        serial_number = self.serial_number
        asset_user = self.asset_user
        asset_tag = self.asset_tag
        equipment_id = self.equipment_id
        asset_status = self.asset_status.value if self.asset_status else None
        asset_name = self.asset_name
        asset_description = self.asset_description
        asset_maker = self.asset_maker
        location = self.location
        room_number = self.room_number
        barcode = self.barcode
        legacy_identifier = self.legacy_identifier
        root_category_name = self.root_category_name
        category_name = self.category_name
        class_ = self.class_
        custodian_email = self.custodian_email
        custodian_first_name = self.custodian_first_name
        custodian_last_name = self.custodian_last_name
        custodian_name = self.custodian_name
        department = self.department
        station = self.station
        notes = self.notes
        document_number = self.document_number
        document_section = self.document_section
        cumulative_service_cost = self.cumulative_service_cost
        product_id = self.product_id
        manufacturer_part_number = self.manufacturer_part_number
        product_name = self.product_name
        product_description = self.product_description
        product_manufacturer = self.product_manufacturer
        site_name = self.site_name
        site_id = self.site_id
        condition = self.condition
        criticality = self.criticality
        pool = self.pool
        purchase_date = self.purchase_date.isoformat() if self.purchase_date else None
        purchase_cost = self.purchase_cost
        life_span_months = self.life_span_months
        activation_date = self.activation_date.isoformat() if self.activation_date else None
        depreciation_basis = self.depreciation_basis
        depreciation_method = self.depreciation_method
        retirement_date = self.retirement_date.isoformat() if self.retirement_date else None
        salvage_value = self.salvage_value
        retirment_reason = self.retirment_reason
        composite_parent_id = self.composite_parent_id
        composite_child_count = self.composite_child_count
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if maintenance_plans is not None:
            field_dict["MaintenancePlans"] = maintenance_plans
        if company_id is not None:
            field_dict["CompanyId"] = company_id
        if asset_id is not None:
            field_dict["AssetId"] = asset_id
        if serial_number is not None:
            field_dict["SerialNumber"] = serial_number
        if asset_user is not None:
            field_dict["AssetUser"] = asset_user
        if asset_tag is not None:
            field_dict["AssetTag"] = asset_tag
        if equipment_id is not None:
            field_dict["EquipmentId"] = equipment_id
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
        if room_number is not None:
            field_dict["RoomNumber"] = room_number
        if barcode is not None:
            field_dict["Barcode"] = barcode
        if legacy_identifier is not None:
            field_dict["LegacyIdentifier"] = legacy_identifier
        if root_category_name is not None:
            field_dict["RootCategoryName"] = root_category_name
        if category_name is not None:
            field_dict["CategoryName"] = category_name
        if class_ is not None:
            field_dict["Class"] = class_
        if custodian_email is not None:
            field_dict["CustodianEmail"] = custodian_email
        if custodian_first_name is not None:
            field_dict["CustodianFirstName"] = custodian_first_name
        if custodian_last_name is not None:
            field_dict["CustodianLastName"] = custodian_last_name
        if custodian_name is not None:
            field_dict["CustodianName"] = custodian_name
        if department is not None:
            field_dict["Department"] = department
        if station is not None:
            field_dict["Station"] = station
        if notes is not None:
            field_dict["Notes"] = notes
        if document_number is not None:
            field_dict["DocumentNumber"] = document_number
        if document_section is not None:
            field_dict["DocumentSection"] = document_section
        if cumulative_service_cost is not None:
            field_dict["CumulativeServiceCost"] = cumulative_service_cost
        if product_id is not None:
            field_dict["ProductId"] = product_id
        if manufacturer_part_number is not None:
            field_dict["ManufacturerPartNumber"] = manufacturer_part_number
        if product_name is not None:
            field_dict["ProductName"] = product_name
        if product_description is not None:
            field_dict["ProductDescription"] = product_description
        if product_manufacturer is not None:
            field_dict["ProductManufacturer"] = product_manufacturer
        if site_name is not None:
            field_dict["SiteName"] = site_name
        if site_id is not None:
            field_dict["SiteId"] = site_id
        if condition is not None:
            field_dict["Condition"] = condition
        if criticality is not None:
            field_dict["Criticality"] = criticality
        if pool is not None:
            field_dict["Pool"] = pool
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
        if retirment_reason is not None:
            field_dict["RetirmentReason"] = retirment_reason
        if composite_parent_id is not None:
            field_dict["CompositeParentId"] = composite_parent_id
        if composite_child_count is not None:
            field_dict["CompositeChildCount"] = composite_child_count
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_asset_to_asset_maintenance_plan_response import (
            AssetToAssetMaintenancePlanResponse,
        )
        d = dict(src_dict)
        maintenance_plans = []
        _maintenance_plans = d.pop("MaintenancePlans", None)
        for maintenance_plans_item_data in _maintenance_plans or []:
            maintenance_plans_item = AssetToAssetMaintenancePlanResponse.from_dict(
                maintenance_plans_item_data
            )
            maintenance_plans.append(maintenance_plans_item)
        company_id = d.pop("CompanyId", None)
        asset_id = d.pop("AssetId", None)
        serial_number = d.pop("SerialNumber", None)
        asset_user = d.pop("AssetUser", None)
        asset_tag = d.pop("AssetTag", None)
        equipment_id = d.pop("EquipmentId", None)
        _asset_status = d.pop("AssetStatus", None)
        asset_status: Optional[AssetToAssetMaintenancePlanModelAssetStatus]
        if not _asset_status:
            asset_status = None
        else:
            asset_status = AssetToAssetMaintenancePlanModelAssetStatus(_asset_status)
        asset_name = d.pop("AssetName", None)
        asset_description = d.pop("AssetDescription", None)
        asset_maker = d.pop("AssetMaker", None)
        location = d.pop("Location", None)
        room_number = d.pop("RoomNumber", None)
        barcode = d.pop("Barcode", None)
        legacy_identifier = d.pop("LegacyIdentifier", None)
        root_category_name = d.pop("RootCategoryName", None)
        category_name = d.pop("CategoryName", None)
        class_ = d.pop("Class", None)
        custodian_email = d.pop("CustodianEmail", None)
        custodian_first_name = d.pop("CustodianFirstName", None)
        custodian_last_name = d.pop("CustodianLastName", None)
        custodian_name = d.pop("CustodianName", None)
        department = d.pop("Department", None)
        station = d.pop("Station", None)
        notes = d.pop("Notes", None)
        document_number = d.pop("DocumentNumber", None)
        document_section = d.pop("DocumentSection", None)
        cumulative_service_cost = d.pop("CumulativeServiceCost", None)
        product_id = d.pop("ProductId", None)
        manufacturer_part_number = d.pop("ManufacturerPartNumber", None)
        product_name = d.pop("ProductName", None)
        product_description = d.pop("ProductDescription", None)
        product_manufacturer = d.pop("ProductManufacturer", None)
        site_name = d.pop("SiteName", None)
        site_id = d.pop("SiteId", None)
        condition = d.pop("Condition", None)
        criticality = d.pop("Criticality", None)
        pool = d.pop("Pool", None)
        def _parse_purchase_date(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                purchase_date_type_0 = isoparse(data)
                return purchase_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)
        purchase_date = _parse_purchase_date(d.pop("PurchaseDate", None))
        purchase_cost = d.pop("PurchaseCost", None)
        life_span_months = d.pop("LifeSpanMonths", None)
        def _parse_activation_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                activation_date_type_0 = isoparse(data)
                return activation_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)
        activation_date = _parse_activation_date(d.pop("ActivationDate", None))
        depreciation_basis = d.pop("DepreciationBasis", None)
        depreciation_method = d.pop("DepreciationMethod", None)
        def _parse_retirement_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                retirement_date_type_0 = isoparse(data)
                return retirement_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)
        retirement_date = _parse_retirement_date(d.pop("RetirementDate", None))
        salvage_value = d.pop("SalvageValue", None)
        retirment_reason = d.pop("RetirmentReason", None)
        composite_parent_id = d.pop("CompositeParentId", None)
        composite_child_count = d.pop("CompositeChildCount", None)
        qualer_api_models_asset_to_asset_maintenance_plan_model = cls(
            maintenance_plans=maintenance_plans,
            company_id=company_id,
            asset_id=asset_id,
            serial_number=serial_number,
            asset_user=asset_user,
            asset_tag=asset_tag,
            equipment_id=equipment_id,
            asset_status=asset_status,
            asset_name=asset_name,
            asset_description=asset_description,
            asset_maker=asset_maker,
            location=location,
            room_number=room_number,
            barcode=barcode,
            legacy_identifier=legacy_identifier,
            root_category_name=root_category_name,
            category_name=category_name,
            class_=class_,
            custodian_email=custodian_email,
            custodian_first_name=custodian_first_name,
            custodian_last_name=custodian_last_name,
            custodian_name=custodian_name,
            department=department,
            station=station,
            notes=notes,
            document_number=document_number,
            document_section=document_section,
            cumulative_service_cost=cumulative_service_cost,
            product_id=product_id,
            manufacturer_part_number=manufacturer_part_number,
            product_name=product_name,
            product_description=product_description,
            product_manufacturer=product_manufacturer,
            site_name=site_name,
            site_id=site_id,
            condition=condition,
            criticality=criticality,
            pool=pool,
            purchase_date=purchase_date,
            purchase_cost=purchase_cost,
            life_span_months=life_span_months,
            activation_date=activation_date,
            depreciation_basis=depreciation_basis,
            depreciation_method=depreciation_method,
            retirement_date=retirement_date,
            salvage_value=salvage_value,
            retirment_reason=retirment_reason,
            composite_parent_id=composite_parent_id,
            composite_child_count=composite_child_count,
        )
        qualer_api_models_asset_to_asset_maintenance_plan_model.additional_properties = d
        return qualer_api_models_asset_to_asset_maintenance_plan_model

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
