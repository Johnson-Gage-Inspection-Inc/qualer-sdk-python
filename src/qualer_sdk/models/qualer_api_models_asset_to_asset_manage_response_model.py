import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.qualer_api_models_asset_to_asset_manage_response_model_as_found_result import (
    QualerApiModelsAssetToAssetManageResponseModelAsFoundResult,
)
from ..models.qualer_api_models_asset_to_asset_manage_response_model_as_left_result import (
    QualerApiModelsAssetToAssetManageResponseModelAsLeftResult,
)
from ..models.qualer_api_models_asset_to_asset_manage_response_model_due_status import (
    QualerApiModelsAssetToAssetManageResponseModelDueStatus,
)
from ..models.qualer_api_models_asset_to_asset_manage_response_model_record_type import (
    QualerApiModelsAssetToAssetManageResponseModelRecordType,
)
from ..models.qualer_api_models_asset_to_asset_manage_response_model_result_status import (
    QualerApiModelsAssetToAssetManageResponseModelResultStatus,
)
from ..models.qualer_api_models_asset_to_asset_manage_response_model_service_order_status import (
    QualerApiModelsAssetToAssetManageResponseModelServiceOrderStatus,
)
from ..models.qualer_api_models_asset_to_asset_manage_response_model_tool_role import (
    QualerApiModelsAssetToAssetManageResponseModelToolRole,
)
from ..models.qualer_api_models_asset_to_asset_manage_response_model_work_status import (
    QualerApiModelsAssetToAssetManageResponseModelWorkStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsAssetToAssetManageResponseModel")


@_attrs_define
class QualerApiModelsAssetToAssetManageResponseModel:
    """
    Attributes:
        asset_id (Union[Unset, int]):
        asset_name (Union[Unset, str]):
        asset_description (Union[Unset, str]):
        asset_maker (Union[Unset, str]):
        record_type (Union[Unset, QualerApiModelsAssetToAssetManageResponseModelRecordType]):
        parent_asset_id (Union[Unset, int]):
        children_count (Union[Unset, int]):
        site_id (Union[Unset, int]):
        serial_number (Union[Unset, str]):
        asset_tag (Union[Unset, str]):
        asset_user (Union[Unset, str]):
        equipment_id (Union[Unset, str]):
        legacy_identifier (Union[Unset, str]):
        criticality (Union[Unset, str]):
        condition (Union[Unset, str]):
        asset_class (Union[Unset, str]):
        activation_date (Union[None, Unset, datetime.datetime]):
        retirment_date (Union[None, Unset, datetime.datetime]):
        client_vendor_id (Union[Unset, int]):
        company_name (Union[Unset, str]):
        site_name (Union[Unset, str]):
        asset_has_image (Union[Unset, bool]):
        has_image (Union[Unset, bool]):
        parent_has_image (Union[Unset, bool]):
        pool_id (Union[Unset, int]):
        pool (Union[Unset, str]):
        product_id (Union[Unset, int]):
        parent_product_id (Union[Unset, int]):
        product_name (Union[Unset, str]):
        parent_product_name (Union[Unset, str]):
        category_id (Union[Unset, int]):
        root_category_id (Union[Unset, int]):
        category_name (Union[Unset, str]):
        root_category_name (Union[Unset, str]):
        manufacturer_id (Union[Unset, int]):
        manufacturer (Union[Unset, str]):
        display_part_number (Union[Unset, str]):
        display_name (Union[Unset, str]):
        manufacturer_part_number (Union[Unset, str]):
        asset_room (Union[Unset, str]):
        location (Union[Unset, str]):
        station (Union[Unset, str]):
        tool_role (Union[Unset, QualerApiModelsAssetToAssetManageResponseModelToolRole]):
        tool_id (Union[Unset, int]):
        department_id (Union[Unset, int]):
        department_name (Union[Unset, str]):
        custodian_name (Union[Unset, str]):
        warranty (Union[Unset, str]):
        warranty_end (Union[None, Unset, datetime.datetime]):
        is_warranty_expired (Union[Unset, bool]):
        depreciation_method (Union[Unset, int]):
        depreciation_basis (Union[Unset, float]):
        salvage_value (Union[Unset, float]):
        total_service_cost (Union[Unset, float]):
        life_span_months (Union[Unset, int]):
        due_for_replacement_date (Union[None, Unset, datetime.datetime]):
        depreciation_proc (Union[Unset, float]):
        purchase_date (Union[None, Unset, datetime.datetime]):
        purchase_cost (Union[Unset, float]):
        time_in_service (Union[Unset, int]):
        retirement_reason (Union[Unset, str]):
        residual_cost (Union[Unset, float]):
        employee_id (Union[Unset, int]):
        asset_service_record_id (Union[Unset, int]):
        result_status (Union[Unset, QualerApiModelsAssetToAssetManageResponseModelResultStatus]):
        as_found_result (Union[Unset, QualerApiModelsAssetToAssetManageResponseModelAsFoundResult]):
        as_left_result (Union[Unset, QualerApiModelsAssetToAssetManageResponseModelAsLeftResult]):
        last_service_date (Union[None, Unset, datetime.datetime]):
        last_service (Union[None, Unset, str]):
        next_service_date (Union[None, Unset, datetime.datetime]):
        next_service (Union[Unset, str]):
        service_schedule_segment_id (Union[Unset, int]):
        service_schedule_id (Union[Unset, int]):
        service_schedule (Union[Unset, str]):
        service_order_id (Union[Unset, int]):
        service_order_status (Union[Unset, QualerApiModelsAssetToAssetManageResponseModelServiceOrderStatus]):
        custom_order_number (Union[Unset, str]):
        service_order_item_id (Union[Unset, int]):
        vendor (Union[Unset, str]):
        technician (Union[Unset, str]):
        certificate_number (Union[Unset, str]):
        due_trigger_date (Union[None, Unset, datetime.datetime]):
        past_due_trigger_date (Union[None, Unset, datetime.datetime]):
        due_status (Union[Unset, QualerApiModelsAssetToAssetManageResponseModelDueStatus]):
        work_status (Union[Unset, QualerApiModelsAssetToAssetManageResponseModelWorkStatus]):
    """

    asset_id: Union[Unset, int] = UNSET
    asset_name: Union[Unset, str] = UNSET
    asset_description: Union[Unset, str] = UNSET
    asset_maker: Union[Unset, str] = UNSET
    record_type: Union[
        None, Unset, QualerApiModelsAssetToAssetManageResponseModelRecordType
    ] = UNSET
    parent_asset_id: Union[Unset, int] = UNSET
    children_count: Union[Unset, int] = UNSET
    site_id: Union[Unset, int] = UNSET
    serial_number: Union[Unset, str] = UNSET
    asset_tag: Union[Unset, str] = UNSET
    asset_user: Union[Unset, str] = UNSET
    equipment_id: Union[Unset, str] = UNSET
    legacy_identifier: Union[Unset, str] = UNSET
    criticality: Union[Unset, str] = UNSET
    condition: Union[Unset, str] = UNSET
    asset_class: Union[Unset, str] = UNSET
    activation_date: Union[None, Unset, datetime.datetime] = UNSET
    retirment_date: Union[None, Unset, datetime.datetime] = UNSET
    client_vendor_id: Union[Unset, int] = UNSET
    company_name: Union[Unset, str] = UNSET
    site_name: Union[Unset, str] = UNSET
    asset_has_image: Union[Unset, bool] = UNSET
    has_image: Union[Unset, bool] = UNSET
    parent_has_image: Union[Unset, bool] = UNSET
    pool_id: Union[Unset, int] = UNSET
    pool: Union[Unset, str] = UNSET
    product_id: Union[Unset, int] = UNSET
    parent_product_id: Union[Unset, int] = UNSET
    product_name: Union[Unset, str] = UNSET
    parent_product_name: Union[Unset, str] = UNSET
    category_id: Union[Unset, int] = UNSET
    root_category_id: Union[Unset, int] = UNSET
    category_name: Union[Unset, str] = UNSET
    root_category_name: Union[Unset, str] = UNSET
    manufacturer_id: Union[Unset, int] = UNSET
    manufacturer: Union[Unset, str] = UNSET
    display_part_number: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    manufacturer_part_number: Union[Unset, str] = UNSET
    asset_room: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    station: Union[Unset, str] = UNSET
    tool_role: Union[
        None, Unset, QualerApiModelsAssetToAssetManageResponseModelToolRole
    ] = UNSET
    tool_id: Union[Unset, int] = UNSET
    department_id: Union[Unset, int] = UNSET
    department_name: Union[Unset, str] = UNSET
    custodian_name: Union[Unset, str] = UNSET
    warranty: Union[Unset, str] = UNSET
    warranty_end: Union[None, Unset, datetime.datetime] = UNSET
    is_warranty_expired: Union[Unset, bool] = UNSET
    depreciation_method: Union[Unset, int] = UNSET
    depreciation_basis: Union[Unset, float] = UNSET
    salvage_value: Union[Unset, float] = UNSET
    total_service_cost: Union[Unset, float] = UNSET
    life_span_months: Union[Unset, int] = UNSET
    due_for_replacement_date: Union[None, Unset, datetime.datetime] = UNSET
    depreciation_proc: Union[Unset, float] = UNSET
    purchase_date: Union[None, Unset, datetime.datetime] = UNSET
    purchase_cost: Union[Unset, float] = UNSET
    time_in_service: Union[Unset, int] = UNSET
    retirement_reason: Union[Unset, str] = UNSET
    residual_cost: Union[Unset, float] = UNSET
    employee_id: Union[Unset, int] = UNSET
    asset_service_record_id: Union[Unset, int] = UNSET
    result_status: Union[
        None, Unset, QualerApiModelsAssetToAssetManageResponseModelResultStatus
    ] = UNSET
    as_found_result: Union[
        None, Unset, QualerApiModelsAssetToAssetManageResponseModelAsFoundResult
    ] = UNSET
    as_left_result: Union[
        None, Unset, QualerApiModelsAssetToAssetManageResponseModelAsLeftResult
    ] = UNSET
    last_service_date: Union[None, Unset, datetime.datetime] = UNSET
    last_service: Union[None, Unset, str] = UNSET
    next_service_date: Union[None, Unset, datetime.datetime] = UNSET
    next_service: Union[Unset, str] = UNSET
    service_schedule_segment_id: Union[Unset, int] = UNSET
    service_schedule_id: Union[Unset, int] = UNSET
    service_schedule: Union[Unset, str] = UNSET
    service_order_id: Union[Unset, int] = UNSET
    service_order_status: Union[
        None, Unset, QualerApiModelsAssetToAssetManageResponseModelServiceOrderStatus
    ] = UNSET
    custom_order_number: Union[Unset, str] = UNSET
    service_order_item_id: Union[Unset, int] = UNSET
    vendor: Union[Unset, str] = UNSET
    technician: Union[Unset, str] = UNSET
    certificate_number: Union[Unset, str] = UNSET
    due_trigger_date: Union[None, Unset, datetime.datetime] = UNSET
    past_due_trigger_date: Union[None, Unset, datetime.datetime] = UNSET
    due_status: Union[
        None, Unset, QualerApiModelsAssetToAssetManageResponseModelDueStatus
    ] = UNSET
    work_status: Union[
        None, Unset, QualerApiModelsAssetToAssetManageResponseModelWorkStatus
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        asset_name = self.asset_name

        asset_description = self.asset_description

        asset_maker = self.asset_maker

        record_type: Union[None, Unset, int] = UNSET
        if not isinstance(self.record_type, Unset):
            record_type = self.record_type.value

        parent_asset_id = self.parent_asset_id

        children_count = self.children_count

        site_id = self.site_id

        serial_number = self.serial_number

        asset_tag = self.asset_tag

        asset_user = self.asset_user

        equipment_id = self.equipment_id

        legacy_identifier = self.legacy_identifier

        criticality = self.criticality

        condition = self.condition

        asset_class = self.asset_class

        activation_date: Union[None, Unset, str]
        if isinstance(self.activation_date, Unset):
            activation_date = UNSET
        elif isinstance(self.activation_date, datetime.datetime):
            activation_date = self.activation_date.isoformat()
        else:
            activation_date = self.activation_date

        retirment_date: Union[None, Unset, str]
        if isinstance(self.retirment_date, Unset):
            retirment_date = UNSET
        elif isinstance(self.retirment_date, datetime.datetime):
            retirment_date = self.retirment_date.isoformat()
        else:
            retirment_date = self.retirment_date

        client_vendor_id = self.client_vendor_id

        company_name = self.company_name

        site_name = self.site_name

        asset_has_image = self.asset_has_image

        has_image = self.has_image

        parent_has_image = self.parent_has_image

        pool_id = self.pool_id

        pool = self.pool

        product_id = self.product_id

        parent_product_id = self.parent_product_id

        product_name = self.product_name

        parent_product_name = self.parent_product_name

        category_id = self.category_id

        root_category_id = self.root_category_id

        category_name = self.category_name

        root_category_name = self.root_category_name

        manufacturer_id = self.manufacturer_id

        manufacturer = self.manufacturer

        display_part_number = self.display_part_number

        display_name = self.display_name

        manufacturer_part_number = self.manufacturer_part_number

        asset_room = self.asset_room

        location = self.location

        station = self.station

        tool_role: Union[None, Unset, int] = UNSET
        if not isinstance(self.tool_role, Unset):
            tool_role = self.tool_role.value

        tool_id = self.tool_id

        department_id = self.department_id

        department_name = self.department_name

        custodian_name = self.custodian_name

        warranty = self.warranty

        warranty_end: Union[None, Unset, str]
        if isinstance(self.warranty_end, Unset):
            warranty_end = UNSET
        elif isinstance(self.warranty_end, datetime.datetime):
            warranty_end = self.warranty_end.isoformat()
        else:
            warranty_end = self.warranty_end

        is_warranty_expired = self.is_warranty_expired

        depreciation_method = self.depreciation_method

        depreciation_basis = self.depreciation_basis

        salvage_value = self.salvage_value

        total_service_cost = self.total_service_cost

        life_span_months = self.life_span_months

        due_for_replacement_date: Union[None, Unset, str]
        if isinstance(self.due_for_replacement_date, Unset):
            due_for_replacement_date = UNSET
        elif isinstance(self.due_for_replacement_date, datetime.datetime):
            due_for_replacement_date = self.due_for_replacement_date.isoformat()
        else:
            due_for_replacement_date = self.due_for_replacement_date

        depreciation_proc = self.depreciation_proc

        purchase_date: Union[None, Unset, str]
        if isinstance(self.purchase_date, Unset):
            purchase_date = UNSET
        elif isinstance(self.purchase_date, datetime.datetime):
            purchase_date = self.purchase_date.isoformat()
        else:
            purchase_date = self.purchase_date

        purchase_cost = self.purchase_cost

        time_in_service = self.time_in_service

        retirement_reason = self.retirement_reason

        residual_cost = self.residual_cost

        employee_id = self.employee_id

        asset_service_record_id = self.asset_service_record_id

        result_status: Union[None, Unset, str] = UNSET
        if not isinstance(self.result_status, Unset):
            result_status = self.result_status.value

        as_found_result: Union[None, Unset, str] = UNSET
        if not isinstance(self.as_found_result, Unset):
            as_found_result = self.as_found_result.value

        as_left_result: Union[None, Unset, str] = UNSET
        if not isinstance(self.as_left_result, Unset):
            as_left_result = self.as_left_result.value

        last_service_date: Union[None, Unset, str]
        if isinstance(self.last_service_date, Unset):
            last_service_date = UNSET
        elif isinstance(self.last_service_date, datetime.datetime):
            last_service_date = self.last_service_date.isoformat()
        else:
            last_service_date = self.last_service_date

        last_service: Union[None, Unset, str]
        if isinstance(self.last_service, Unset):
            last_service = UNSET
        else:
            last_service = self.last_service

        next_service_date: Union[None, Unset, str]
        if isinstance(self.next_service_date, Unset):
            next_service_date = UNSET
        elif isinstance(self.next_service_date, datetime.datetime):
            next_service_date = self.next_service_date.isoformat()
        else:
            next_service_date = self.next_service_date

        next_service = self.next_service

        service_schedule_segment_id = self.service_schedule_segment_id

        service_schedule_id = self.service_schedule_id

        service_schedule = self.service_schedule

        service_order_id = self.service_order_id

        service_order_status: Union[None, Unset, str] = UNSET
        if not isinstance(self.service_order_status, Unset):
            service_order_status = self.service_order_status.value

        custom_order_number = self.custom_order_number

        service_order_item_id = self.service_order_item_id

        vendor = self.vendor

        technician = self.technician

        certificate_number = self.certificate_number

        due_trigger_date: Union[None, Unset, str]
        if isinstance(self.due_trigger_date, Unset):
            due_trigger_date = UNSET
        elif isinstance(self.due_trigger_date, datetime.datetime):
            due_trigger_date = self.due_trigger_date.isoformat()
        else:
            due_trigger_date = self.due_trigger_date

        past_due_trigger_date: Union[None, Unset, str]
        if isinstance(self.past_due_trigger_date, Unset):
            past_due_trigger_date = UNSET
        elif isinstance(self.past_due_trigger_date, datetime.datetime):
            past_due_trigger_date = self.past_due_trigger_date.isoformat()
        else:
            past_due_trigger_date = self.past_due_trigger_date

        due_status: Union[None, Unset, int] = UNSET
        if not isinstance(self.due_status, Unset):
            due_status = self.due_status.value

        work_status: Union[None, Unset, str] = UNSET
        if not isinstance(self.work_status, Unset):
            work_status = self.work_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["AssetId"] = asset_id
        if asset_name is not UNSET:
            field_dict["AssetName"] = asset_name
        if asset_description is not UNSET:
            field_dict["AssetDescription"] = asset_description
        if asset_maker is not UNSET:
            field_dict["AssetMaker"] = asset_maker
        if record_type is not UNSET:
            field_dict["RecordType"] = record_type
        if parent_asset_id is not UNSET:
            field_dict["ParentAssetId"] = parent_asset_id
        if children_count is not UNSET:
            field_dict["ChildrenCount"] = children_count
        if site_id is not UNSET:
            field_dict["SiteId"] = site_id
        if serial_number is not UNSET:
            field_dict["SerialNumber"] = serial_number
        if asset_tag is not UNSET:
            field_dict["AssetTag"] = asset_tag
        if asset_user is not UNSET:
            field_dict["AssetUser"] = asset_user
        if equipment_id is not UNSET:
            field_dict["EquipmentId"] = equipment_id
        if legacy_identifier is not UNSET:
            field_dict["LegacyIdentifier"] = legacy_identifier
        if criticality is not UNSET:
            field_dict["Criticality"] = criticality
        if condition is not UNSET:
            field_dict["Condition"] = condition
        if asset_class is not UNSET:
            field_dict["AssetClass"] = asset_class
        if activation_date is not UNSET:
            field_dict["ActivationDate"] = activation_date
        if retirment_date is not UNSET:
            field_dict["RetirmentDate"] = retirment_date
        if client_vendor_id is not UNSET:
            field_dict["ClientVendorId"] = client_vendor_id
        if company_name is not UNSET:
            field_dict["CompanyName"] = company_name
        if site_name is not UNSET:
            field_dict["SiteName"] = site_name
        if asset_has_image is not UNSET:
            field_dict["AssetHasImage"] = asset_has_image
        if has_image is not UNSET:
            field_dict["HasImage"] = has_image
        if parent_has_image is not UNSET:
            field_dict["ParentHasImage"] = parent_has_image
        if pool_id is not UNSET:
            field_dict["PoolId"] = pool_id
        if pool is not UNSET:
            field_dict["Pool"] = pool
        if product_id is not UNSET:
            field_dict["ProductId"] = product_id
        if parent_product_id is not UNSET:
            field_dict["ParentProductId"] = parent_product_id
        if product_name is not UNSET:
            field_dict["ProductName"] = product_name
        if parent_product_name is not UNSET:
            field_dict["ParentProductName"] = parent_product_name
        if category_id is not UNSET:
            field_dict["CategoryId"] = category_id
        if root_category_id is not UNSET:
            field_dict["RootCategoryId"] = root_category_id
        if category_name is not UNSET:
            field_dict["CategoryName"] = category_name
        if root_category_name is not UNSET:
            field_dict["RootCategoryName"] = root_category_name
        if manufacturer_id is not UNSET:
            field_dict["ManufacturerId"] = manufacturer_id
        if manufacturer is not UNSET:
            field_dict["Manufacturer"] = manufacturer
        if display_part_number is not UNSET:
            field_dict["DisplayPartNumber"] = display_part_number
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if manufacturer_part_number is not UNSET:
            field_dict["ManufacturerPartNumber"] = manufacturer_part_number
        if asset_room is not UNSET:
            field_dict["AssetRoom"] = asset_room
        if location is not UNSET:
            field_dict["Location"] = location
        if station is not UNSET:
            field_dict["Station"] = station
        if tool_role is not UNSET:
            field_dict["ToolRole"] = tool_role
        if tool_id is not UNSET:
            field_dict["ToolId"] = tool_id
        if department_id is not UNSET:
            field_dict["DepartmentId"] = department_id
        if department_name is not UNSET:
            field_dict["DepartmentName"] = department_name
        if custodian_name is not UNSET:
            field_dict["CustodianName"] = custodian_name
        if warranty is not UNSET:
            field_dict["Warranty"] = warranty
        if warranty_end is not UNSET:
            field_dict["WarrantyEnd"] = warranty_end
        if is_warranty_expired is not UNSET:
            field_dict["IsWarrantyExpired"] = is_warranty_expired
        if depreciation_method is not UNSET:
            field_dict["DepreciationMethod"] = depreciation_method
        if depreciation_basis is not UNSET:
            field_dict["DepreciationBasis"] = depreciation_basis
        if salvage_value is not UNSET:
            field_dict["SalvageValue"] = salvage_value
        if total_service_cost is not UNSET:
            field_dict["TotalServiceCost"] = total_service_cost
        if life_span_months is not UNSET:
            field_dict["LifeSpanMonths"] = life_span_months
        if due_for_replacement_date is not UNSET:
            field_dict["DueForReplacementDate"] = due_for_replacement_date
        if depreciation_proc is not UNSET:
            field_dict["DepreciationProc"] = depreciation_proc
        if purchase_date is not UNSET:
            field_dict["PurchaseDate"] = purchase_date
        if purchase_cost is not UNSET:
            field_dict["PurchaseCost"] = purchase_cost
        if time_in_service is not UNSET:
            field_dict["TimeInService"] = time_in_service
        if retirement_reason is not UNSET:
            field_dict["RetirementReason"] = retirement_reason
        if residual_cost is not UNSET:
            field_dict["ResidualCost"] = residual_cost
        if employee_id is not UNSET:
            field_dict["EmployeeId"] = employee_id
        if asset_service_record_id is not UNSET:
            field_dict["AssetServiceRecordId"] = asset_service_record_id
        if result_status is not UNSET:
            field_dict["ResultStatus"] = result_status
        if as_found_result is not UNSET:
            field_dict["AsFoundResult"] = as_found_result
        if as_left_result is not UNSET:
            field_dict["AsLeftResult"] = as_left_result
        if last_service_date is not UNSET:
            field_dict["LastServiceDate"] = last_service_date
        if last_service is not UNSET:
            field_dict["LastService"] = last_service
        if next_service_date is not UNSET:
            field_dict["NextServiceDate"] = next_service_date
        if next_service is not UNSET:
            field_dict["NextService"] = next_service
        if service_schedule_segment_id is not UNSET:
            field_dict["ServiceScheduleSegmentId"] = service_schedule_segment_id
        if service_schedule_id is not UNSET:
            field_dict["ServiceScheduleId"] = service_schedule_id
        if service_schedule is not UNSET:
            field_dict["ServiceSchedule"] = service_schedule
        if service_order_id is not UNSET:
            field_dict["ServiceOrderId"] = service_order_id
        if service_order_status is not UNSET:
            field_dict["ServiceOrderStatus"] = service_order_status
        if custom_order_number is not UNSET:
            field_dict["CustomOrderNumber"] = custom_order_number
        if service_order_item_id is not UNSET:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if vendor is not UNSET:
            field_dict["Vendor"] = vendor
        if technician is not UNSET:
            field_dict["Technician"] = technician
        if certificate_number is not UNSET:
            field_dict["CertificateNumber"] = certificate_number
        if due_trigger_date is not UNSET:
            field_dict["DueTriggerDate"] = due_trigger_date
        if past_due_trigger_date is not UNSET:
            field_dict["PastDueTriggerDate"] = past_due_trigger_date
        if due_status is not UNSET:
            field_dict["DueStatus"] = due_status
        if work_status is not UNSET:
            field_dict["WorkStatus"] = work_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = d.pop("AssetId", UNSET)

        asset_name = d.pop("AssetName", UNSET)

        asset_description = d.pop("AssetDescription", UNSET)

        asset_maker = d.pop("AssetMaker", UNSET)

        _record_type = d.pop("RecordType", UNSET)
        record_type: Union[
            Unset, QualerApiModelsAssetToAssetManageResponseModelRecordType
        ]
        if isinstance(_record_type, Unset):
            record_type = UNSET
        elif _record_type is None:
            record_type = None
        else:
            record_type = QualerApiModelsAssetToAssetManageResponseModelRecordType(
                _record_type
            )

        parent_asset_id = d.pop("ParentAssetId", UNSET)

        children_count = d.pop("ChildrenCount", UNSET)

        site_id = d.pop("SiteId", UNSET)

        serial_number = d.pop("SerialNumber", UNSET)

        asset_tag = d.pop("AssetTag", UNSET)

        asset_user = d.pop("AssetUser", UNSET)

        equipment_id = d.pop("EquipmentId", UNSET)

        legacy_identifier = d.pop("LegacyIdentifier", UNSET)

        criticality = d.pop("Criticality", UNSET)

        condition = d.pop("Condition", UNSET)

        asset_class = d.pop("AssetClass", UNSET)

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

        def _parse_retirment_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                retirment_date_type_0 = isoparse(data)

                return retirment_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        retirment_date = _parse_retirment_date(d.pop("RetirmentDate", UNSET))

        client_vendor_id = d.pop("ClientVendorId", UNSET)

        company_name = d.pop("CompanyName", UNSET)

        site_name = d.pop("SiteName", UNSET)

        asset_has_image = d.pop("AssetHasImage", UNSET)

        has_image = d.pop("HasImage", UNSET)

        parent_has_image = d.pop("ParentHasImage", UNSET)

        pool_id = d.pop("PoolId", UNSET)

        pool = d.pop("Pool", UNSET)

        product_id = d.pop("ProductId", UNSET)

        parent_product_id = d.pop("ParentProductId", UNSET)

        product_name = d.pop("ProductName", UNSET)

        parent_product_name = d.pop("ParentProductName", UNSET)

        category_id = d.pop("CategoryId", UNSET)

        root_category_id = d.pop("RootCategoryId", UNSET)

        category_name = d.pop("CategoryName", UNSET)

        root_category_name = d.pop("RootCategoryName", UNSET)

        manufacturer_id = d.pop("ManufacturerId", UNSET)

        manufacturer = d.pop("Manufacturer", UNSET)

        display_part_number = d.pop("DisplayPartNumber", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        manufacturer_part_number = d.pop("ManufacturerPartNumber", UNSET)

        asset_room = d.pop("AssetRoom", UNSET)

        location = d.pop("Location", UNSET)

        station = d.pop("Station", UNSET)

        _tool_role = d.pop("ToolRole", UNSET)
        tool_role: Union[Unset, QualerApiModelsAssetToAssetManageResponseModelToolRole]
        if isinstance(_tool_role, Unset):
            tool_role = UNSET
        elif _tool_role is None:
            tool_role = None
        else:
            tool_role = QualerApiModelsAssetToAssetManageResponseModelToolRole(
                _tool_role
            )

        tool_id = d.pop("ToolId", UNSET)

        department_id = d.pop("DepartmentId", UNSET)

        department_name = d.pop("DepartmentName", UNSET)

        custodian_name = d.pop("CustodianName", UNSET)

        warranty = d.pop("Warranty", UNSET)

        def _parse_warranty_end(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                warranty_end_type_0 = isoparse(data)

                return warranty_end_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        warranty_end = _parse_warranty_end(d.pop("WarrantyEnd", UNSET))

        is_warranty_expired = d.pop("IsWarrantyExpired", UNSET)

        depreciation_method = d.pop("DepreciationMethod", UNSET)

        depreciation_basis = d.pop("DepreciationBasis", UNSET)

        salvage_value = d.pop("SalvageValue", UNSET)

        total_service_cost = d.pop("TotalServiceCost", UNSET)

        life_span_months = d.pop("LifeSpanMonths", UNSET)

        def _parse_due_for_replacement_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_for_replacement_date_type_0 = isoparse(data)

                return due_for_replacement_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        due_for_replacement_date = _parse_due_for_replacement_date(
            d.pop("DueForReplacementDate", UNSET)
        )

        depreciation_proc = d.pop("DepreciationProc", UNSET)

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

        time_in_service = d.pop("TimeInService", UNSET)

        retirement_reason = d.pop("RetirementReason", UNSET)

        residual_cost = d.pop("ResidualCost", UNSET)

        employee_id = d.pop("EmployeeId", UNSET)

        asset_service_record_id = d.pop("AssetServiceRecordId", UNSET)

        _result_status = d.pop("ResultStatus", UNSET)
        result_status: Union[
            Unset, QualerApiModelsAssetToAssetManageResponseModelResultStatus
        ]
        if isinstance(_result_status, Unset):
            result_status = UNSET
        elif _result_status is None:
            result_status = None
        else:
            result_status = QualerApiModelsAssetToAssetManageResponseModelResultStatus(
                _result_status
            )

        _as_found_result = d.pop("AsFoundResult", UNSET)
        as_found_result: Union[
            Unset, QualerApiModelsAssetToAssetManageResponseModelAsFoundResult
        ]
        if isinstance(_as_found_result, Unset):
            as_found_result = UNSET
        elif _as_found_result is None:
            as_found_result = None
        else:
            as_found_result = (
                QualerApiModelsAssetToAssetManageResponseModelAsFoundResult(
                    _as_found_result
                )
            )

        _as_left_result = d.pop("AsLeftResult", UNSET)
        as_left_result: Union[
            Unset, QualerApiModelsAssetToAssetManageResponseModelAsLeftResult
        ]
        if isinstance(_as_left_result, Unset):
            as_left_result = UNSET
        elif _as_left_result is None:
            as_left_result = None
        else:
            as_left_result = QualerApiModelsAssetToAssetManageResponseModelAsLeftResult(
                _as_left_result
            )

        def _parse_last_service_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_service_date_type_0 = isoparse(data)

                return last_service_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_service_date = _parse_last_service_date(d.pop("LastServiceDate", UNSET))

        def _parse_last_service(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_service = _parse_last_service(d.pop("LastService", UNSET))

        def _parse_next_service_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_service_date_type_0 = isoparse(data)

                return next_service_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        next_service_date = _parse_next_service_date(d.pop("NextServiceDate", UNSET))

        next_service = d.pop("NextService", UNSET)

        service_schedule_segment_id = d.pop("ServiceScheduleSegmentId", UNSET)

        service_schedule_id = d.pop("ServiceScheduleId", UNSET)

        service_schedule = d.pop("ServiceSchedule", UNSET)

        service_order_id = d.pop("ServiceOrderId", UNSET)

        _service_order_status = d.pop("ServiceOrderStatus", UNSET)
        service_order_status: Union[
            Unset, QualerApiModelsAssetToAssetManageResponseModelServiceOrderStatus
        ]
        if isinstance(_service_order_status, Unset):
            service_order_status = UNSET
        elif _service_order_status is None:
            service_order_status = None
        else:
            service_order_status = (
                QualerApiModelsAssetToAssetManageResponseModelServiceOrderStatus(
                    _service_order_status
                )
            )

        custom_order_number = d.pop("CustomOrderNumber", UNSET)

        service_order_item_id = d.pop("ServiceOrderItemId", UNSET)

        vendor = d.pop("Vendor", UNSET)

        technician = d.pop("Technician", UNSET)

        certificate_number = d.pop("CertificateNumber", UNSET)

        def _parse_due_trigger_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_trigger_date_type_0 = isoparse(data)

                return due_trigger_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        due_trigger_date = _parse_due_trigger_date(d.pop("DueTriggerDate", UNSET))

        def _parse_past_due_trigger_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                past_due_trigger_date_type_0 = isoparse(data)

                return past_due_trigger_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        past_due_trigger_date = _parse_past_due_trigger_date(
            d.pop("PastDueTriggerDate", UNSET)
        )

        _due_status = d.pop("DueStatus", UNSET)
        due_status: Union[
            Unset, QualerApiModelsAssetToAssetManageResponseModelDueStatus
        ]
        if isinstance(_due_status, Unset):
            due_status = UNSET
        elif _due_status is None:
            due_status = None
        else:
            due_status = QualerApiModelsAssetToAssetManageResponseModelDueStatus(
                _due_status
            )

        _work_status = d.pop("WorkStatus", UNSET)
        work_status: Union[
            Unset, QualerApiModelsAssetToAssetManageResponseModelWorkStatus
        ]
        if isinstance(_work_status, Unset):
            work_status = UNSET
        elif _work_status is None:
            work_status = None
        else:
            work_status = QualerApiModelsAssetToAssetManageResponseModelWorkStatus(
                _work_status
            )

        qualer_api_models_asset_to_asset_manage_response_model = cls(
            asset_id=asset_id,
            asset_name=asset_name,
            asset_description=asset_description,
            asset_maker=asset_maker,
            record_type=record_type,
            parent_asset_id=parent_asset_id,
            children_count=children_count,
            site_id=site_id,
            serial_number=serial_number,
            asset_tag=asset_tag,
            asset_user=asset_user,
            equipment_id=equipment_id,
            legacy_identifier=legacy_identifier,
            criticality=criticality,
            condition=condition,
            asset_class=asset_class,
            activation_date=activation_date,
            retirment_date=retirment_date,
            client_vendor_id=client_vendor_id,
            company_name=company_name,
            site_name=site_name,
            asset_has_image=asset_has_image,
            has_image=has_image,
            parent_has_image=parent_has_image,
            pool_id=pool_id,
            pool=pool,
            product_id=product_id,
            parent_product_id=parent_product_id,
            product_name=product_name,
            parent_product_name=parent_product_name,
            category_id=category_id,
            root_category_id=root_category_id,
            category_name=category_name,
            root_category_name=root_category_name,
            manufacturer_id=manufacturer_id,
            manufacturer=manufacturer,
            display_part_number=display_part_number,
            display_name=display_name,
            manufacturer_part_number=manufacturer_part_number,
            asset_room=asset_room,
            location=location,
            station=station,
            tool_role=tool_role,
            tool_id=tool_id,
            department_id=department_id,
            department_name=department_name,
            custodian_name=custodian_name,
            warranty=warranty,
            warranty_end=warranty_end,
            is_warranty_expired=is_warranty_expired,
            depreciation_method=depreciation_method,
            depreciation_basis=depreciation_basis,
            salvage_value=salvage_value,
            total_service_cost=total_service_cost,
            life_span_months=life_span_months,
            due_for_replacement_date=due_for_replacement_date,
            depreciation_proc=depreciation_proc,
            purchase_date=purchase_date,
            purchase_cost=purchase_cost,
            time_in_service=time_in_service,
            retirement_reason=retirement_reason,
            residual_cost=residual_cost,
            employee_id=employee_id,
            asset_service_record_id=asset_service_record_id,
            result_status=result_status,
            as_found_result=as_found_result,
            as_left_result=as_left_result,
            last_service_date=last_service_date,
            last_service=last_service,
            next_service_date=next_service_date,
            next_service=next_service,
            service_schedule_segment_id=service_schedule_segment_id,
            service_schedule_id=service_schedule_id,
            service_schedule=service_schedule,
            service_order_id=service_order_id,
            service_order_status=service_order_status,
            custom_order_number=custom_order_number,
            service_order_item_id=service_order_item_id,
            vendor=vendor,
            technician=technician,
            certificate_number=certificate_number,
            due_trigger_date=due_trigger_date,
            past_due_trigger_date=past_due_trigger_date,
            due_status=due_status,
            work_status=work_status,
        )

        qualer_api_models_asset_to_asset_manage_response_model.additional_properties = d
        return qualer_api_models_asset_to_asset_manage_response_model

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
