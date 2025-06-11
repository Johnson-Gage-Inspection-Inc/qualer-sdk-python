import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.qualer_api_models_asset_to_asset_maintenance_plan_model_asset_status import (
    QualerApiModelsAssetToAssetMaintenancePlanModelAssetStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualer_api_models_asset_to_asset_maintenance_plan_response import (
        QualerApiModelsAssetToAssetMaintenancePlanResponse,
    )


T = TypeVar("T", bound="QualerApiModelsAssetToAssetMaintenancePlanModel")


@_attrs_define
class QualerApiModelsAssetToAssetMaintenancePlanModel:
    """
    Attributes:
        maintenance_plans (Union[Unset, list['QualerApiModelsAssetToAssetMaintenancePlanResponse']]):
        company_id (Union[Unset, int]):
        asset_id (Union[Unset, int]):
        serial_number (Union[Unset, str]):
        asset_user (Union[Unset, str]):
        asset_tag (Union[Unset, str]):
        equipment_id (Union[Unset, str]):
        asset_status (Union[Unset, QualerApiModelsAssetToAssetMaintenancePlanModelAssetStatus]):
        asset_name (Union[Unset, str]):
        asset_description (Union[Unset, str]):
        asset_maker (Union[Unset, str]):
        location (Union[Unset, str]):
        room_number (Union[Unset, str]):
        barcode (Union[Unset, str]):
        legacy_identifier (Union[Unset, str]):
        root_category_name (Union[Unset, str]):
        category_name (Union[Unset, str]):
        class_ (Union[Unset, str]):
        custodian_email (Union[Unset, str]):
        custodian_first_name (Union[Unset, str]):
        custodian_last_name (Union[Unset, str]):
        custodian_name (Union[Unset, str]):
        department (Union[Unset, str]):
        station (Union[Unset, str]):
        notes (Union[Unset, str]):
        document_number (Union[Unset, str]):
        document_section (Union[Unset, str]):
        cumulative_service_cost (Union[Unset, float]):
        product_id (Union[Unset, int]):
        manufacturer_part_number (Union[Unset, str]):
        product_name (Union[Unset, str]):
        product_description (Union[Unset, str]):
        product_manufacturer (Union[Unset, str]):
        site_name (Union[Unset, str]):
        site_id (Union[Unset, int]):
        condition (Union[Unset, str]):
        criticality (Union[Unset, str]):
        pool (Union[Unset, str]):
        purchase_date (Union[Unset, datetime.datetime]):
        purchase_cost (Union[Unset, float]):
        life_span_months (Union[Unset, int]):
        activation_date (Union[Unset, datetime.datetime]):
        depreciation_basis (Union[Unset, float]):
        depreciation_method (Union[Unset, int]):
        retirement_date (Union[Unset, datetime.datetime]):
        salvage_value (Union[Unset, float]):
        retirment_reason (Union[Unset, str]):
        composite_parent_id (Union[Unset, int]):
        composite_child_count (Union[Unset, int]):
    """

    maintenance_plans: Union[
        Unset, list["QualerApiModelsAssetToAssetMaintenancePlanResponse"]
    ] = UNSET
    company_id: Union[Unset, int] = UNSET
    asset_id: Union[Unset, int] = UNSET
    serial_number: Union[Unset, str] = UNSET
    asset_user: Union[Unset, str] = UNSET
    asset_tag: Union[Unset, str] = UNSET
    equipment_id: Union[Unset, str] = UNSET
    asset_status: Union[
        Unset, QualerApiModelsAssetToAssetMaintenancePlanModelAssetStatus
    ] = UNSET
    asset_name: Union[Unset, str] = UNSET
    asset_description: Union[Unset, str] = UNSET
    asset_maker: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    room_number: Union[Unset, str] = UNSET
    barcode: Union[Unset, str] = UNSET
    legacy_identifier: Union[Unset, str] = UNSET
    root_category_name: Union[Unset, str] = UNSET
    category_name: Union[Unset, str] = UNSET
    class_: Union[Unset, str] = UNSET
    custodian_email: Union[Unset, str] = UNSET
    custodian_first_name: Union[Unset, str] = UNSET
    custodian_last_name: Union[Unset, str] = UNSET
    custodian_name: Union[Unset, str] = UNSET
    department: Union[Unset, str] = UNSET
    station: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    document_number: Union[Unset, str] = UNSET
    document_section: Union[Unset, str] = UNSET
    cumulative_service_cost: Union[Unset, float] = UNSET
    product_id: Union[Unset, int] = UNSET
    manufacturer_part_number: Union[Unset, str] = UNSET
    product_name: Union[Unset, str] = UNSET
    product_description: Union[Unset, str] = UNSET
    product_manufacturer: Union[Unset, str] = UNSET
    site_name: Union[Unset, str] = UNSET
    site_id: Union[Unset, int] = UNSET
    condition: Union[Unset, str] = UNSET
    criticality: Union[Unset, str] = UNSET
    pool: Union[Unset, str] = UNSET
    purchase_date: Union[Unset, datetime.datetime] = UNSET
    purchase_cost: Union[Unset, float] = UNSET
    life_span_months: Union[Unset, int] = UNSET
    activation_date: Union[Unset, datetime.datetime] = UNSET
    depreciation_basis: Union[Unset, float] = UNSET
    depreciation_method: Union[Unset, int] = UNSET
    retirement_date: Union[Unset, datetime.datetime] = UNSET
    salvage_value: Union[Unset, float] = UNSET
    retirment_reason: Union[Unset, str] = UNSET
    composite_parent_id: Union[Unset, int] = UNSET
    composite_child_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        maintenance_plans: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.maintenance_plans, Unset):
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

        asset_status: Union[Unset, str] = UNSET
        if not isinstance(self.asset_status, Unset):
            asset_status = self.asset_status.value

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

        purchase_date: Union[Unset, str] = UNSET
        if not isinstance(self.purchase_date, Unset):
            purchase_date = self.purchase_date.isoformat()

        purchase_cost = self.purchase_cost

        life_span_months = self.life_span_months

        activation_date: Union[Unset, str] = UNSET
        if not isinstance(self.activation_date, Unset):
            activation_date = self.activation_date.isoformat()

        depreciation_basis = self.depreciation_basis

        depreciation_method = self.depreciation_method

        retirement_date: Union[Unset, str] = UNSET
        if not isinstance(self.retirement_date, Unset):
            retirement_date = self.retirement_date.isoformat()

        salvage_value = self.salvage_value

        retirment_reason = self.retirment_reason

        composite_parent_id = self.composite_parent_id

        composite_child_count = self.composite_child_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if maintenance_plans is not UNSET:
            field_dict["MaintenancePlans"] = maintenance_plans
        if company_id is not UNSET:
            field_dict["CompanyId"] = company_id
        if asset_id is not UNSET:
            field_dict["AssetId"] = asset_id
        if serial_number is not UNSET:
            field_dict["SerialNumber"] = serial_number
        if asset_user is not UNSET:
            field_dict["AssetUser"] = asset_user
        if asset_tag is not UNSET:
            field_dict["AssetTag"] = asset_tag
        if equipment_id is not UNSET:
            field_dict["EquipmentId"] = equipment_id
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
        if room_number is not UNSET:
            field_dict["RoomNumber"] = room_number
        if barcode is not UNSET:
            field_dict["Barcode"] = barcode
        if legacy_identifier is not UNSET:
            field_dict["LegacyIdentifier"] = legacy_identifier
        if root_category_name is not UNSET:
            field_dict["RootCategoryName"] = root_category_name
        if category_name is not UNSET:
            field_dict["CategoryName"] = category_name
        if class_ is not UNSET:
            field_dict["Class"] = class_
        if custodian_email is not UNSET:
            field_dict["CustodianEmail"] = custodian_email
        if custodian_first_name is not UNSET:
            field_dict["CustodianFirstName"] = custodian_first_name
        if custodian_last_name is not UNSET:
            field_dict["CustodianLastName"] = custodian_last_name
        if custodian_name is not UNSET:
            field_dict["CustodianName"] = custodian_name
        if department is not UNSET:
            field_dict["Department"] = department
        if station is not UNSET:
            field_dict["Station"] = station
        if notes is not UNSET:
            field_dict["Notes"] = notes
        if document_number is not UNSET:
            field_dict["DocumentNumber"] = document_number
        if document_section is not UNSET:
            field_dict["DocumentSection"] = document_section
        if cumulative_service_cost is not UNSET:
            field_dict["CumulativeServiceCost"] = cumulative_service_cost
        if product_id is not UNSET:
            field_dict["ProductId"] = product_id
        if manufacturer_part_number is not UNSET:
            field_dict["ManufacturerPartNumber"] = manufacturer_part_number
        if product_name is not UNSET:
            field_dict["ProductName"] = product_name
        if product_description is not UNSET:
            field_dict["ProductDescription"] = product_description
        if product_manufacturer is not UNSET:
            field_dict["ProductManufacturer"] = product_manufacturer
        if site_name is not UNSET:
            field_dict["SiteName"] = site_name
        if site_id is not UNSET:
            field_dict["SiteId"] = site_id
        if condition is not UNSET:
            field_dict["Condition"] = condition
        if criticality is not UNSET:
            field_dict["Criticality"] = criticality
        if pool is not UNSET:
            field_dict["Pool"] = pool
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
        if retirment_reason is not UNSET:
            field_dict["RetirmentReason"] = retirment_reason
        if composite_parent_id is not UNSET:
            field_dict["CompositeParentId"] = composite_parent_id
        if composite_child_count is not UNSET:
            field_dict["CompositeChildCount"] = composite_child_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_asset_to_asset_maintenance_plan_response import (
            QualerApiModelsAssetToAssetMaintenancePlanResponse,
        )

        d = dict(src_dict)
        maintenance_plans = []
        _maintenance_plans = d.pop("MaintenancePlans", UNSET)
        for maintenance_plans_item_data in _maintenance_plans or []:
            maintenance_plans_item = (
                QualerApiModelsAssetToAssetMaintenancePlanResponse.from_dict(
                    maintenance_plans_item_data
                )
            )

            maintenance_plans.append(maintenance_plans_item)

        company_id = d.pop("CompanyId", UNSET)

        asset_id = d.pop("AssetId", UNSET)

        serial_number = d.pop("SerialNumber", UNSET)

        asset_user = d.pop("AssetUser", UNSET)

        asset_tag = d.pop("AssetTag", UNSET)

        equipment_id = d.pop("EquipmentId", UNSET)

        _asset_status = d.pop("AssetStatus", UNSET)
        asset_status: Union[
            Unset, QualerApiModelsAssetToAssetMaintenancePlanModelAssetStatus
        ]
        if isinstance(_asset_status, Unset):
            asset_status = UNSET
        else:
            asset_status = QualerApiModelsAssetToAssetMaintenancePlanModelAssetStatus(
                _asset_status
            )

        asset_name = d.pop("AssetName", UNSET)

        asset_description = d.pop("AssetDescription", UNSET)

        asset_maker = d.pop("AssetMaker", UNSET)

        location = d.pop("Location", UNSET)

        room_number = d.pop("RoomNumber", UNSET)

        barcode = d.pop("Barcode", UNSET)

        legacy_identifier = d.pop("LegacyIdentifier", UNSET)

        root_category_name = d.pop("RootCategoryName", UNSET)

        category_name = d.pop("CategoryName", UNSET)

        class_ = d.pop("Class", UNSET)

        custodian_email = d.pop("CustodianEmail", UNSET)

        custodian_first_name = d.pop("CustodianFirstName", UNSET)

        custodian_last_name = d.pop("CustodianLastName", UNSET)

        custodian_name = d.pop("CustodianName", UNSET)

        department = d.pop("Department", UNSET)

        station = d.pop("Station", UNSET)

        notes = d.pop("Notes", UNSET)

        document_number = d.pop("DocumentNumber", UNSET)

        document_section = d.pop("DocumentSection", UNSET)

        cumulative_service_cost = d.pop("CumulativeServiceCost", UNSET)

        product_id = d.pop("ProductId", UNSET)

        manufacturer_part_number = d.pop("ManufacturerPartNumber", UNSET)

        product_name = d.pop("ProductName", UNSET)

        product_description = d.pop("ProductDescription", UNSET)

        product_manufacturer = d.pop("ProductManufacturer", UNSET)

        site_name = d.pop("SiteName", UNSET)

        site_id = d.pop("SiteId", UNSET)

        condition = d.pop("Condition", UNSET)

        criticality = d.pop("Criticality", UNSET)

        pool = d.pop("Pool", UNSET)

        _purchase_date = d.pop("PurchaseDate", UNSET)
        purchase_date: Union[Unset, datetime.datetime]
        if isinstance(_purchase_date, Unset):
            purchase_date = UNSET
        else:
            purchase_date = isoparse(_purchase_date)

        purchase_cost = d.pop("PurchaseCost", UNSET)

        life_span_months = d.pop("LifeSpanMonths", UNSET)

        _activation_date = d.pop("ActivationDate", UNSET)
        activation_date: Union[Unset, datetime.datetime]
        if isinstance(_activation_date, Unset):
            activation_date = UNSET
        else:
            activation_date = isoparse(_activation_date)

        depreciation_basis = d.pop("DepreciationBasis", UNSET)

        depreciation_method = d.pop("DepreciationMethod", UNSET)

        _retirement_date = d.pop("RetirementDate", UNSET)
        retirement_date: Union[Unset, datetime.datetime]
        if isinstance(_retirement_date, Unset):
            retirement_date = UNSET
        else:
            retirement_date = isoparse(_retirement_date)

        salvage_value = d.pop("SalvageValue", UNSET)

        retirment_reason = d.pop("RetirmentReason", UNSET)

        composite_parent_id = d.pop("CompositeParentId", UNSET)

        composite_child_count = d.pop("CompositeChildCount", UNSET)

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

        qualer_api_models_asset_to_asset_maintenance_plan_model.additional_properties = (
            d
        )
        return qualer_api_models_asset_to_asset_maintenance_plan_model

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
