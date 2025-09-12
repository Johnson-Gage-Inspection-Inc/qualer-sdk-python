import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.qualer_api_models_asset_to_client_asset_manager_response_model_due_status import (
    QualerApiModelsAssetToClientAssetManagerResponseModelDueStatus,
)
from ..models.qualer_api_models_asset_to_client_asset_manager_response_model_record_type import (
    QualerApiModelsAssetToClientAssetManagerResponseModelRecordType,
)
from ..models.qualer_api_models_asset_to_client_asset_manager_response_model_service_order_status import (
    QualerApiModelsAssetToClientAssetManagerResponseModelServiceOrderStatus,
)
from ..models.qualer_api_models_asset_to_client_asset_manager_response_model_tool_role import (
    QualerApiModelsAssetToClientAssetManagerResponseModelToolRole,
)
from ..models.service_result_status import ServiceResultStatus
from ..models.work_status import WorkStatus

T = TypeVar("T", bound="QualerApiModelsAssetToClientAssetManagerResponseModel")


@_attrs_define
class QualerApiModelsAssetToClientAssetManagerResponseModel:
    """
    Attributes:
        asset_id (Optional[int]):
        asset_name (Optional[str]):
        asset_description (Optional[str]):
        asset_maker (Optional[str]):
        record_type (Optional[QualerApiModelsAssetToClientAssetManagerResponseModelRecordType]):
        parent_asset_id (Optional[int]):
        children_count (Optional[int]):
        site_id (Optional[int]):
        serial_number (Optional[str]):
        asset_tag (Optional[str]):
        asset_user (Optional[str]):
        equipment_id (Optional[str]):
        legacy_identifier (Optional[str]):
        criticality (Optional[str]):
        condition (Optional[str]):
        asset_class (Optional[str]):
        activation_date (Optional[datetime.datetime]):
        retirment_date (Optional[datetime.datetime]):
        client_vendor_id (Optional[int]):
        company_name (Optional[str]):
        site_name (Optional[str]):
        asset_has_image (Optional[bool]):
        has_image (Optional[bool]):
        parent_has_image (Optional[bool]):
        pool_id (Optional[int]):
        pool (Optional[str]):
        product_id (Optional[int]):
        parent_product_id (Optional[int]):
        product_name (Optional[str]):
        parent_product_name (Optional[str]):
        category_id (Optional[int]):
        root_category_id (Optional[int]):
        category_name (Optional[str]):
        root_category_name (Optional[str]):
        manufacturer_id (Optional[int]):
        manufacturer (Optional[str]):
        display_part_number (Optional[str]):
        display_name (Optional[str]):
        manufacturer_part_number (Optional[str]):
        asset_room (Optional[str]):
        location (Optional[str]):
        station (Optional[str]):
        tool_role (Optional[QualerApiModelsAssetToClientAssetManagerResponseModelToolRole]):
        tool_id (Optional[int]):
        department_id (Optional[int]):
        department_name (Optional[str]):
        custodian_name (Optional[str]):
        warranty (Optional[str]):
        warranty_end (Optional[datetime.datetime]):
        is_warranty_expired (Optional[bool]):
        depreciation_method (Optional[int]):
        depreciation_basis (Optional[float]):
        salvage_value (Optional[float]):
        total_service_cost (Optional[float]):
        life_span_months (Optional[int]):
        due_for_replacement_date (Optional[datetime.datetime]):
        depreciation_proc (Optional[float]):
        purchase_date (Optional[datetime.datetime]):
        purchase_cost (Optional[float]):
        time_in_service (Optional[int]):
        retirement_reason (Optional[str]):
        residual_cost (Optional[float]):
        employee_id (Optional[int]):
        asset_collection_id (Optional[int]):
        asset_service_record_id (Optional[int]):
        result_status (Optional[ServiceResultStatus]):
        as_found_result (Optional[ServiceResultStatus]):
        as_left_result (Optional[ServiceResultStatus]):
        last_service_date (Optional[datetime.datetime]):
        last_service (Optional[str]):
        next_service_date (Optional[datetime.datetime]):
        next_service (Optional[str]):
        service_schedule_segment_id (Optional[int]):
        service_schedule_id (Optional[int]):
        service_schedule (Optional[str]):
        in_service (Optional[bool]):
        in_last_service (Optional[bool]):
        service_order_id (Optional[int]):
        service_order_status (Optional[QualerApiModelsAssetToClientAssetManagerResponseModelServiceOrderStatus]):
        custom_order_number (Optional[str]):
        service_order_item_id (Optional[int]):
        vendor (Optional[str]):
        technician (Optional[str]):
        certificate_number (Optional[str]):
        due_trigger_date (Optional[datetime.datetime]):
        past_due_trigger_date (Optional[datetime.datetime]):
        due_status (Optional[QualerApiModelsAssetToClientAssetManagerResponseModelDueStatus]):
        work_status (Optional[WorkStatus]):
        service_tag (Optional[str]):
        service_site_name (Optional[str]):
        service_site_id (Optional[int]):
        standard_title (Optional[str]):
        schedules (Optional[str]):
    """

    asset_id: Optional[int] = None
    asset_name: Optional[str] = None
    asset_description: Optional[str] = None
    asset_maker: Optional[str] = None
    record_type: Optional["QualerApiModelsAssetToClientAssetManagerResponseModelRecordType"] = None
    parent_asset_id: Optional[int] = None
    children_count: Optional[int] = None
    site_id: Optional[int] = None
    serial_number: Optional[str] = None
    asset_tag: Optional[str] = None
    asset_user: Optional[str] = None
    equipment_id: Optional[str] = None
    legacy_identifier: Optional[str] = None
    criticality: Optional[str] = None
    condition: Optional[str] = None
    asset_class: Optional[str] = None
    activation_date: Optional[datetime.datetime] = None
    retirment_date: Optional[datetime.datetime] = None
    client_vendor_id: Optional[int] = None
    company_name: Optional[str] = None
    site_name: Optional[str] = None
    asset_has_image: Optional[bool] = None
    has_image: Optional[bool] = None
    parent_has_image: Optional[bool] = None
    pool_id: Optional[int] = None
    pool: Optional[str] = None
    product_id: Optional[int] = None
    parent_product_id: Optional[int] = None
    product_name: Optional[str] = None
    parent_product_name: Optional[str] = None
    category_id: Optional[int] = None
    root_category_id: Optional[int] = None
    category_name: Optional[str] = None
    root_category_name: Optional[str] = None
    manufacturer_id: Optional[int] = None
    manufacturer: Optional[str] = None
    display_part_number: Optional[str] = None
    display_name: Optional[str] = None
    manufacturer_part_number: Optional[str] = None
    asset_room: Optional[str] = None
    location: Optional[str] = None
    station: Optional[str] = None
    tool_role: Optional["QualerApiModelsAssetToClientAssetManagerResponseModelToolRole"] = None
    tool_id: Optional[int] = None
    department_id: Optional[int] = None
    department_name: Optional[str] = None
    custodian_name: Optional[str] = None
    warranty: Optional[str] = None
    warranty_end: Optional[datetime.datetime] = None
    is_warranty_expired: Optional[bool] = None
    depreciation_method: Optional[int] = None
    depreciation_basis: Optional[float] = None
    salvage_value: Optional[float] = None
    total_service_cost: Optional[float] = None
    life_span_months: Optional[int] = None
    due_for_replacement_date: Optional[datetime.datetime] = None
    depreciation_proc: Optional[float] = None
    purchase_date: Optional[datetime.datetime] = None
    purchase_cost: Optional[float] = None
    time_in_service: Optional[int] = None
    retirement_reason: Optional[str] = None
    residual_cost: Optional[float] = None
    employee_id: Optional[int] = None
    asset_collection_id: Optional[int] = None
    asset_service_record_id: Optional[int] = None
    result_status: Optional[ServiceResultStatus] = None
    as_found_result: Optional[ServiceResultStatus] = None
    as_left_result: Optional[ServiceResultStatus] = None
    last_service_date: Optional[datetime.datetime] = None
    last_service: Optional[str] = None
    next_service_date: Optional[datetime.datetime] = None
    next_service: Optional[str] = None
    service_schedule_segment_id: Optional[int] = None
    service_schedule_id: Optional[int] = None
    service_schedule: Optional[str] = None
    in_service: Optional[bool] = None
    in_last_service: Optional[bool] = None
    service_order_id: Optional[int] = None
    service_order_status: Union[
        None,
        None,
        QualerApiModelsAssetToClientAssetManagerResponseModelServiceOrderStatus,
    ] = None
    custom_order_number: Optional[str] = None
    service_order_item_id: Optional[int] = None
    vendor: Optional[str] = None
    technician: Optional[str] = None
    certificate_number: Optional[str] = None
    due_trigger_date: Optional[datetime.datetime] = None
    past_due_trigger_date: Optional[datetime.datetime] = None
    due_status: Optional["QualerApiModelsAssetToClientAssetManagerResponseModelDueStatus"] = None
    work_status: Optional[WorkStatus] = None
    service_tag: Optional[str] = None
    service_site_name: Optional[str] = None
    service_site_id: Optional[int] = None
    standard_title: Optional[str] = None
    schedules: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asset_id = self.asset_id

        asset_name = self.asset_name

        asset_description = self.asset_description

        asset_maker = self.asset_maker

        record_type: Optional[int] = None
        if self.record_type:
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

        activation_date: Optional[str]
        if not self.activation_date:
            activation_date = None
        elif isinstance(self.activation_date, datetime.datetime):
            activation_date = self.activation_date.isoformat()
        else:
            activation_date = self.activation_date

        retirment_date: Optional[str]
        if not self.retirment_date:
            retirment_date = None
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

        tool_role: Optional[int] = None
        if self.tool_role:
            tool_role = self.tool_role.value

        tool_id = self.tool_id

        department_id = self.department_id

        department_name = self.department_name

        custodian_name = self.custodian_name

        warranty = self.warranty

        warranty_end: Optional[str]
        if not self.warranty_end:
            warranty_end = None
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

        due_for_replacement_date: Optional[str]
        if not self.due_for_replacement_date:
            due_for_replacement_date = None
        elif isinstance(self.due_for_replacement_date, datetime.datetime):
            due_for_replacement_date = self.due_for_replacement_date.isoformat()
        else:
            due_for_replacement_date = self.due_for_replacement_date

        depreciation_proc = self.depreciation_proc

        purchase_date: Optional[str]
        if not self.purchase_date:
            purchase_date = None
        elif isinstance(self.purchase_date, datetime.datetime):
            purchase_date = self.purchase_date.isoformat()
        else:
            purchase_date = self.purchase_date

        purchase_cost = self.purchase_cost

        time_in_service = self.time_in_service

        retirement_reason = self.retirement_reason

        residual_cost = self.residual_cost

        employee_id = self.employee_id

        asset_collection_id = self.asset_collection_id

        asset_service_record_id = self.asset_service_record_id

        result_status: Optional[int] = None
        if self.result_status:
            result_status = self.result_status.value

        as_found_result: Optional[int] = None
        if self.as_found_result:
            as_found_result = self.as_found_result.value

        as_left_result: Optional[int] = None
        if self.as_left_result:
            as_left_result = self.as_left_result.value

        last_service_date: Optional[str]
        if not self.last_service_date:
            last_service_date = None
        elif isinstance(self.last_service_date, datetime.datetime):
            last_service_date = self.last_service_date.isoformat()
        else:
            last_service_date = self.last_service_date

        last_service: Optional[str]
        if not self.last_service:
            last_service = None
        else:
            last_service = self.last_service

        next_service_date: Optional[str]
        if not self.next_service_date:
            next_service_date = None
        elif isinstance(self.next_service_date, datetime.datetime):
            next_service_date = self.next_service_date.isoformat()
        else:
            next_service_date = self.next_service_date

        next_service = self.next_service

        service_schedule_segment_id = self.service_schedule_segment_id

        service_schedule_id = self.service_schedule_id

        service_schedule = self.service_schedule

        in_service = self.in_service

        in_last_service = self.in_last_service

        service_order_id = self.service_order_id

        service_order_status: Optional[str] = None
        if self.service_order_status and not isinstance(self.service_order_status, None):
            service_order_status = self.service_order_status.value

        custom_order_number = self.custom_order_number

        service_order_item_id = self.service_order_item_id

        vendor = self.vendor

        technician = self.technician

        certificate_number = self.certificate_number

        due_trigger_date: Optional[str]
        if not self.due_trigger_date:
            due_trigger_date = None
        elif isinstance(self.due_trigger_date, datetime.datetime):
            due_trigger_date = self.due_trigger_date.isoformat()
        else:
            due_trigger_date = self.due_trigger_date

        past_due_trigger_date: Optional[str]
        if not self.past_due_trigger_date:
            past_due_trigger_date = None
        elif isinstance(self.past_due_trigger_date, datetime.datetime):
            past_due_trigger_date = self.past_due_trigger_date.isoformat()
        else:
            past_due_trigger_date = self.past_due_trigger_date

        due_status: Optional[int] = None
        if self.due_status:
            due_status = self.due_status.value

        work_status: Optional[int] = None
        if self.work_status:
            work_status = self.work_status.value

        service_tag = self.service_tag

        service_site_name = self.service_site_name

        service_site_id = self.service_site_id

        standard_title = self.standard_title

        schedules = self.schedules

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not None:
            field_dict["AssetId"] = asset_id
        if asset_name is not None:
            field_dict["AssetName"] = asset_name
        if asset_description is not None:
            field_dict["AssetDescription"] = asset_description
        if asset_maker is not None:
            field_dict["AssetMaker"] = asset_maker
        if record_type is not None:
            field_dict["RecordType"] = record_type
        if parent_asset_id is not None:
            field_dict["ParentAssetId"] = parent_asset_id
        if children_count is not None:
            field_dict["ChildrenCount"] = children_count
        if site_id is not None:
            field_dict["SiteId"] = site_id
        if serial_number is not None:
            field_dict["SerialNumber"] = serial_number
        if asset_tag is not None:
            field_dict["AssetTag"] = asset_tag
        if asset_user is not None:
            field_dict["AssetUser"] = asset_user
        if equipment_id is not None:
            field_dict["EquipmentId"] = equipment_id
        if legacy_identifier is not None:
            field_dict["LegacyIdentifier"] = legacy_identifier
        if criticality is not None:
            field_dict["Criticality"] = criticality
        if condition is not None:
            field_dict["Condition"] = condition
        if asset_class is not None:
            field_dict["AssetClass"] = asset_class
        if activation_date is not None:
            field_dict["ActivationDate"] = activation_date
        if retirment_date is not None:
            field_dict["RetirmentDate"] = retirment_date
        if client_vendor_id is not None:
            field_dict["ClientVendorId"] = client_vendor_id
        if company_name is not None:
            field_dict["CompanyName"] = company_name
        if site_name is not None:
            field_dict["SiteName"] = site_name
        if asset_has_image is not None:
            field_dict["AssetHasImage"] = asset_has_image
        if has_image is not None:
            field_dict["HasImage"] = has_image
        if parent_has_image is not None:
            field_dict["ParentHasImage"] = parent_has_image
        if pool_id is not None:
            field_dict["PoolId"] = pool_id
        if pool is not None:
            field_dict["Pool"] = pool
        if product_id is not None:
            field_dict["ProductId"] = product_id
        if parent_product_id is not None:
            field_dict["ParentProductId"] = parent_product_id
        if product_name is not None:
            field_dict["ProductName"] = product_name
        if parent_product_name is not None:
            field_dict["ParentProductName"] = parent_product_name
        if category_id is not None:
            field_dict["CategoryId"] = category_id
        if root_category_id is not None:
            field_dict["RootCategoryId"] = root_category_id
        if category_name is not None:
            field_dict["CategoryName"] = category_name
        if root_category_name is not None:
            field_dict["RootCategoryName"] = root_category_name
        if manufacturer_id is not None:
            field_dict["ManufacturerId"] = manufacturer_id
        if manufacturer is not None:
            field_dict["Manufacturer"] = manufacturer
        if display_part_number is not None:
            field_dict["DisplayPartNumber"] = display_part_number
        if display_name is not None:
            field_dict["DisplayName"] = display_name
        if manufacturer_part_number is not None:
            field_dict["ManufacturerPartNumber"] = manufacturer_part_number
        if asset_room is not None:
            field_dict["AssetRoom"] = asset_room
        if location is not None:
            field_dict["Location"] = location
        if station is not None:
            field_dict["Station"] = station
        if tool_role is not None:
            field_dict["ToolRole"] = tool_role
        if tool_id is not None:
            field_dict["ToolId"] = tool_id
        if department_id is not None:
            field_dict["DepartmentId"] = department_id
        if department_name is not None:
            field_dict["DepartmentName"] = department_name
        if custodian_name is not None:
            field_dict["CustodianName"] = custodian_name
        if warranty is not None:
            field_dict["Warranty"] = warranty
        if warranty_end is not None:
            field_dict["WarrantyEnd"] = warranty_end
        if is_warranty_expired is not None:
            field_dict["IsWarrantyExpired"] = is_warranty_expired
        if depreciation_method is not None:
            field_dict["DepreciationMethod"] = depreciation_method
        if depreciation_basis is not None:
            field_dict["DepreciationBasis"] = depreciation_basis
        if salvage_value is not None:
            field_dict["SalvageValue"] = salvage_value
        if total_service_cost is not None:
            field_dict["TotalServiceCost"] = total_service_cost
        if life_span_months is not None:
            field_dict["LifeSpanMonths"] = life_span_months
        if due_for_replacement_date is not None:
            field_dict["DueForReplacementDate"] = due_for_replacement_date
        if depreciation_proc is not None:
            field_dict["DepreciationProc"] = depreciation_proc
        if purchase_date is not None:
            field_dict["PurchaseDate"] = purchase_date
        if purchase_cost is not None:
            field_dict["PurchaseCost"] = purchase_cost
        if time_in_service is not None:
            field_dict["TimeInService"] = time_in_service
        if retirement_reason is not None:
            field_dict["RetirementReason"] = retirement_reason
        if residual_cost is not None:
            field_dict["ResidualCost"] = residual_cost
        if employee_id is not None:
            field_dict["EmployeeId"] = employee_id
        if asset_collection_id is not None:
            field_dict["AssetCollectionId"] = asset_collection_id
        if asset_service_record_id is not None:
            field_dict["AssetServiceRecordId"] = asset_service_record_id
        if result_status is not None:
            field_dict["ResultStatus"] = result_status
        if as_found_result is not None:
            field_dict["AsFoundResult"] = as_found_result
        if as_left_result is not None:
            field_dict["AsLeftResult"] = as_left_result
        if last_service_date is not None:
            field_dict["LastServiceDate"] = last_service_date
        if last_service is not None:
            field_dict["LastService"] = last_service
        if next_service_date is not None:
            field_dict["NextServiceDate"] = next_service_date
        if next_service is not None:
            field_dict["NextService"] = next_service
        if service_schedule_segment_id is not None:
            field_dict["ServiceScheduleSegmentId"] = service_schedule_segment_id
        if service_schedule_id is not None:
            field_dict["ServiceScheduleId"] = service_schedule_id
        if service_schedule is not None:
            field_dict["ServiceSchedule"] = service_schedule
        if in_service is not None:
            field_dict["InService"] = in_service
        if in_last_service is not None:
            field_dict["InLastService"] = in_last_service
        if service_order_id is not None:
            field_dict["ServiceOrderId"] = service_order_id
        if service_order_status is not None:
            field_dict["ServiceOrderStatus"] = service_order_status
        if custom_order_number is not None:
            field_dict["CustomOrderNumber"] = custom_order_number
        if service_order_item_id is not None:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if vendor is not None:
            field_dict["Vendor"] = vendor
        if technician is not None:
            field_dict["Technician"] = technician
        if certificate_number is not None:
            field_dict["CertificateNumber"] = certificate_number
        if due_trigger_date is not None:
            field_dict["DueTriggerDate"] = due_trigger_date
        if past_due_trigger_date is not None:
            field_dict["PastDueTriggerDate"] = past_due_trigger_date
        if due_status is not None:
            field_dict["DueStatus"] = due_status
        if work_status is not None:
            field_dict["WorkStatus"] = work_status
        if service_tag is not None:
            field_dict["ServiceTag"] = service_tag
        if service_site_name is not None:
            field_dict["ServiceSiteName"] = service_site_name
        if service_site_id is not None:
            field_dict["ServiceSiteId"] = service_site_id
        if standard_title is not None:
            field_dict["StandardTitle"] = standard_title
        if schedules is not None:
            field_dict["Schedules"] = schedules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = d.pop("AssetId", None)

        asset_name = d.pop("AssetName", None)

        asset_description = d.pop("AssetDescription", None)

        asset_maker = d.pop("AssetMaker", None)

        _record_type = d.pop("RecordType", None)
        record_type: Optional[QualerApiModelsAssetToClientAssetManagerResponseModelRecordType]
        if not _record_type:
            record_type = None
        elif _record_type is None:
            record_type = None
        else:
            record_type = QualerApiModelsAssetToClientAssetManagerResponseModelRecordType(
                _record_type
            )

        parent_asset_id = d.pop("ParentAssetId", None)

        children_count = d.pop("ChildrenCount", None)

        site_id = d.pop("SiteId", None)

        serial_number = d.pop("SerialNumber", None)

        asset_tag = d.pop("AssetTag", None)

        asset_user = d.pop("AssetUser", None)

        equipment_id = d.pop("EquipmentId", None)

        legacy_identifier = d.pop("LegacyIdentifier", None)

        criticality = d.pop("Criticality", None)

        condition = d.pop("Condition", None)

        asset_class = d.pop("AssetClass", None)

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

        def _parse_retirment_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                retirment_date_type_0 = isoparse(data)

                return retirment_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        retirment_date = _parse_retirment_date(d.pop("RetirmentDate", None))

        client_vendor_id = d.pop("ClientVendorId", None)

        company_name = d.pop("CompanyName", None)

        site_name = d.pop("SiteName", None)

        asset_has_image = d.pop("AssetHasImage", None)

        has_image = d.pop("HasImage", None)

        parent_has_image = d.pop("ParentHasImage", None)

        pool_id = d.pop("PoolId", None)

        pool = d.pop("Pool", None)

        product_id = d.pop("ProductId", None)

        parent_product_id = d.pop("ParentProductId", None)

        product_name = d.pop("ProductName", None)

        parent_product_name = d.pop("ParentProductName", None)

        category_id = d.pop("CategoryId", None)

        root_category_id = d.pop("RootCategoryId", None)

        category_name = d.pop("CategoryName", None)

        root_category_name = d.pop("RootCategoryName", None)

        manufacturer_id = d.pop("ManufacturerId", None)

        manufacturer = d.pop("Manufacturer", None)

        display_part_number = d.pop("DisplayPartNumber", None)

        display_name = d.pop("DisplayName", None)

        manufacturer_part_number = d.pop("ManufacturerPartNumber", None)

        asset_room = d.pop("AssetRoom", None)

        location = d.pop("Location", None)

        station = d.pop("Station", None)

        _tool_role = d.pop("ToolRole", None)
        tool_role: Optional[QualerApiModelsAssetToClientAssetManagerResponseModelToolRole]
        if not _tool_role:
            tool_role = None
        elif _tool_role is None:
            tool_role = None
        else:
            tool_role = QualerApiModelsAssetToClientAssetManagerResponseModelToolRole(_tool_role)

        tool_id = d.pop("ToolId", None)

        department_id = d.pop("DepartmentId", None)

        department_name = d.pop("DepartmentName", None)

        custodian_name = d.pop("CustodianName", None)

        warranty = d.pop("Warranty", None)

        def _parse_warranty_end(data: object) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                warranty_end_type_0 = isoparse(data)

                return warranty_end_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        warranty_end = _parse_warranty_end(d.pop("WarrantyEnd", None))

        is_warranty_expired = d.pop("IsWarrantyExpired", None)

        depreciation_method = d.pop("DepreciationMethod", None)

        depreciation_basis = d.pop("DepreciationBasis", None)

        salvage_value = d.pop("SalvageValue", None)

        total_service_cost = d.pop("TotalServiceCost", None)

        life_span_months = d.pop("LifeSpanMonths", None)

        def _parse_due_for_replacement_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_for_replacement_date_type_0 = isoparse(data)

                return due_for_replacement_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        due_for_replacement_date = _parse_due_for_replacement_date(
            d.pop("DueForReplacementDate", None)
        )

        depreciation_proc = d.pop("DepreciationProc", None)

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

        time_in_service = d.pop("TimeInService", None)

        retirement_reason = d.pop("RetirementReason", None)

        residual_cost = d.pop("ResidualCost", None)

        employee_id = d.pop("EmployeeId", None)

        asset_collection_id = d.pop("AssetCollectionId", None)

        asset_service_record_id = d.pop("AssetServiceRecordId", None)

        _result_status = d.pop("ResultStatus", None)
        result_status: Optional[ServiceResultStatus]
        if not _result_status:
            result_status = None
        elif _result_status is None:
            result_status = None
        else:
            result_status = ServiceResultStatus(_result_status)

        _as_found_result = d.pop("AsFoundResult", None)
        as_found_result: Optional[ServiceResultStatus]
        if not _as_found_result:
            as_found_result = None
        elif _as_found_result is None:
            as_found_result = None
        else:
            as_found_result = ServiceResultStatus(_as_found_result)

        _as_left_result = d.pop("AsLeftResult", None)
        as_left_result: Optional[ServiceResultStatus]
        if not _as_left_result:
            as_left_result = None
        elif _as_left_result is None:
            as_left_result = None
        else:
            as_left_result = ServiceResultStatus(_as_left_result)

        def _parse_last_service_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_service_date_type_0 = isoparse(data)

                return last_service_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        last_service_date = _parse_last_service_date(d.pop("LastServiceDate", None))

        def _parse_last_service(data: object) -> Optional[str]:
            if not data:
                return None
            return cast(Optional[str], data)

        last_service = _parse_last_service(d.pop("LastService", None))

        def _parse_next_service_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_service_date_type_0 = isoparse(data)

                return next_service_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        next_service_date = _parse_next_service_date(d.pop("NextServiceDate", None))

        next_service = d.pop("NextService", None)

        service_schedule_segment_id = d.pop("ServiceScheduleSegmentId", None)

        service_schedule_id = d.pop("ServiceScheduleId", None)

        service_schedule = d.pop("ServiceSchedule", None)

        in_service = d.pop("InService", None)

        in_last_service = d.pop("InLastService", None)

        service_order_id = d.pop("ServiceOrderId", None)

        _service_order_status = d.pop("ServiceOrderStatus", None)
        service_order_status: Union[
            None,
            None,
            QualerApiModelsAssetToClientAssetManagerResponseModelServiceOrderStatus,
        ]
        if not _service_order_status:
            service_order_status = None
        elif _service_order_status is None:
            service_order_status = None
        else:
            service_order_status = (
                QualerApiModelsAssetToClientAssetManagerResponseModelServiceOrderStatus(
                    _service_order_status
                )
            )

        custom_order_number = d.pop("CustomOrderNumber", None)

        service_order_item_id = d.pop("ServiceOrderItemId", None)

        vendor = d.pop("Vendor", None)

        technician = d.pop("Technician", None)

        certificate_number = d.pop("CertificateNumber", None)

        def _parse_due_trigger_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_trigger_date_type_0 = isoparse(data)

                return due_trigger_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        due_trigger_date = _parse_due_trigger_date(d.pop("DueTriggerDate", None))

        def _parse_past_due_trigger_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                past_due_trigger_date_type_0 = isoparse(data)

                return past_due_trigger_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        past_due_trigger_date = _parse_past_due_trigger_date(d.pop("PastDueTriggerDate", None))

        _due_status = d.pop("DueStatus", None)
        due_status: Optional[QualerApiModelsAssetToClientAssetManagerResponseModelDueStatus]
        if not _due_status:
            due_status = None
        elif _due_status is None:
            due_status = None
        else:
            due_status = QualerApiModelsAssetToClientAssetManagerResponseModelDueStatus(_due_status)

        _work_status = d.pop("WorkStatus", None)
        work_status: Optional[WorkStatus]
        if not _work_status:
            work_status = None
        elif _work_status is None:
            work_status = None
        else:
            work_status = WorkStatus(_work_status)

        service_tag = d.pop("ServiceTag", None)

        service_site_name = d.pop("ServiceSiteName", None)

        service_site_id = d.pop("ServiceSiteId", None)

        standard_title = d.pop("StandardTitle", None)

        schedules = d.pop("Schedules", None)

        qualer_api_models_asset_to_client_asset_manager_response_model = cls(
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
            asset_collection_id=asset_collection_id,
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
            in_service=in_service,
            in_last_service=in_last_service,
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
            service_tag=service_tag,
            service_site_name=service_site_name,
            service_site_id=service_site_id,
            standard_title=standard_title,
            schedules=schedules,
        )

        qualer_api_models_asset_to_client_asset_manager_response_model.additional_properties = d
        return qualer_api_models_asset_to_client_asset_manager_response_model

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
