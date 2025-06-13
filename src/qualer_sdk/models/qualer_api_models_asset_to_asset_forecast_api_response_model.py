import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.qualer_api_models_asset_to_asset_forecast_api_response_model_asset_status import (
    QualerApiModelsAssetToAssetForecastApiResponseModelAssetStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsAssetToAssetForecastApiResponseModel")


@_attrs_define
class QualerApiModelsAssetToAssetForecastApiResponseModel:
    """
    Attributes:
        last_due_date (Union[Unset, datetime.datetime]):
        last_service_date (Union[Unset, datetime.datetime]):
        next_service_date (Union[Unset, datetime.datetime]):
        next_service_task (Union[Unset, str]):
        company_id (Union[Unset, int]):
        asset_id (Union[Unset, int]):
        serial_number (Union[Unset, str]):
        asset_user (Union[Unset, str]):
        asset_tag (Union[Unset, str]):
        equipment_id (Union[Unset, str]):
        asset_status (Union[Unset, QualerApiModelsAssetToAssetForecastApiResponseModelAssetStatus]):
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
        purchase_date (Union[None, Unset, datetime.datetime]):
        purchase_cost (Union[Unset, float]):
        life_span_months (Union[Unset, int]):
        activation_date (Union[None, Unset, datetime.datetime]):
        depreciation_basis (Union[Unset, float]):
        depreciation_method (Union[Unset, int]):
        retirement_date (Union[None, Unset, datetime.datetime]):
        salvage_value (Union[Unset, float]):
        retirment_reason (Union[Unset, str]):
        composite_parent_id (Union[Unset, int]):
        composite_child_count (Union[Unset, int]):
    """

    last_due_date: Union[Unset, datetime.datetime] = UNSET
    last_service_date: Union[Unset, datetime.datetime] = UNSET
    next_service_date: Union[Unset, datetime.datetime] = UNSET
    next_service_task: Union[Unset, str] = UNSET
    company_id: Union[Unset, int] = UNSET
    asset_id: Union[Unset, int] = UNSET
    serial_number: Union[Unset, str] = UNSET
    asset_user: Union[Unset, str] = UNSET
    asset_tag: Union[Unset, str] = UNSET
    equipment_id: Union[Unset, str] = UNSET
    asset_status: Union[
        Unset, QualerApiModelsAssetToAssetForecastApiResponseModelAssetStatus
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
    purchase_date: Union[None, Unset, datetime.datetime] = UNSET
    purchase_cost: Union[Unset, float] = UNSET
    life_span_months: Union[Unset, int] = UNSET
    activation_date: Union[None, Unset, datetime.datetime] = UNSET
    depreciation_basis: Union[Unset, float] = UNSET
    depreciation_method: Union[Unset, int] = UNSET
    retirement_date: Union[None, Unset, datetime.datetime] = UNSET
    salvage_value: Union[Unset, float] = UNSET
    retirment_reason: Union[Unset, str] = UNSET
    composite_parent_id: Union[Unset, int] = UNSET
    composite_child_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_due_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_due_date, Unset):
            last_due_date = self.last_due_date.isoformat()

        last_service_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_service_date, Unset):
            last_service_date = self.last_service_date.isoformat()

        next_service_date: Union[Unset, str] = UNSET
        if not isinstance(self.next_service_date, Unset):
            next_service_date = self.next_service_date.isoformat()

        next_service_task = self.next_service_task

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

        retirment_reason = self.retirment_reason

        composite_parent_id = self.composite_parent_id

        composite_child_count = self.composite_child_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_due_date is not UNSET:
            field_dict["LastDueDate"] = last_due_date
        if last_service_date is not UNSET:
            field_dict["LastServiceDate"] = last_service_date
        if next_service_date is not UNSET:
            field_dict["NextServiceDate"] = next_service_date
        if next_service_task is not UNSET:
            field_dict["NextServiceTask"] = next_service_task
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
        d = dict(src_dict)
        _last_due_date = d.pop("LastDueDate", UNSET)
        last_due_date: Union[Unset, datetime.datetime]
        if isinstance(_last_due_date, Unset):
            last_due_date = UNSET
        else:
            last_due_date = isoparse(_last_due_date)

        _last_service_date = d.pop("LastServiceDate", UNSET)
        last_service_date: Union[Unset, datetime.datetime]
        if isinstance(_last_service_date, Unset):
            last_service_date = UNSET
        else:
            last_service_date = isoparse(_last_service_date)

        _next_service_date = d.pop("NextServiceDate", UNSET)
        next_service_date: Union[Unset, datetime.datetime]
        if isinstance(_next_service_date, Unset):
            next_service_date = UNSET
        else:
            next_service_date = isoparse(_next_service_date)

        next_service_task = d.pop("NextServiceTask", UNSET)

        company_id = d.pop("CompanyId", UNSET)

        asset_id = d.pop("AssetId", UNSET)

        serial_number = d.pop("SerialNumber", UNSET)

        asset_user = d.pop("AssetUser", UNSET)

        asset_tag = d.pop("AssetTag", UNSET)

        equipment_id = d.pop("EquipmentId", UNSET)

        _asset_status = d.pop("AssetStatus", UNSET)
        asset_status: Union[
            Unset, QualerApiModelsAssetToAssetForecastApiResponseModelAssetStatus
        ]
        if isinstance(_asset_status, Unset):
            asset_status = UNSET
        else:
            asset_status = (
                QualerApiModelsAssetToAssetForecastApiResponseModelAssetStatus(
                    _asset_status
                )
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

        retirment_reason = d.pop("RetirmentReason", UNSET)

        composite_parent_id = d.pop("CompositeParentId", UNSET)

        composite_child_count = d.pop("CompositeChildCount", UNSET)

        qualer_api_models_asset_to_asset_forecast_api_response_model = cls(
            last_due_date=last_due_date,
            last_service_date=last_service_date,
            next_service_date=next_service_date,
            next_service_task=next_service_task,
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

        qualer_api_models_asset_to_asset_forecast_api_response_model.additional_properties = (
            d
        )
        return qualer_api_models_asset_to_asset_forecast_api_response_model

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
