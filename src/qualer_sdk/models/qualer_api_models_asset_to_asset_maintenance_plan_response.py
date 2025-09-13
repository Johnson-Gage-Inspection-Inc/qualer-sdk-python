import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.qualer_api_models_asset_to_asset_maintenance_plan_response_assigned_employee import (
        AssetToAssetMaintenancePlanResponseAssignedEmployee,
    )


T = TypeVar("T", bound="AssetToAssetMaintenancePlanResponse")


@_attrs_define
class AssetToAssetMaintenancePlanResponse:
    """
    Attributes:
        maintenance_plan_id (Optional[int]):
        maintenance_plan_name (Optional[str]):
        task_notes (Optional[str]):
        last_service_task (Optional[str]):
        last_service_date (Optional[datetime.datetime]):
        next_service_task (Optional[str]):
        next_service_date (Optional[datetime.datetime]):
        certificate_due_date (Optional[datetime.datetime]):
        owner_first_name (Optional[str]):
        owner_last_name (Optional[str]):
        owner_alias (Optional[str]):
        owner_department_name (Optional[str]):
        technician_first_name (Optional[str]):
        technician_last_name (Optional[str]):
        technician_alias (Optional[str]):
        technician_department_name (Optional[str]):
        assigned_employees (Optional[List['AssetToAssetMaintenancePlanResponseAssignedEmployee']]):
    """

    maintenance_plan_id: Optional[int] = None
    maintenance_plan_name: Optional[str] = None
    task_notes: Optional[str] = None
    last_service_task: Optional[str] = None
    last_service_date: Optional[datetime.datetime] = None
    next_service_task: Optional[str] = None
    next_service_date: Optional[datetime.datetime] = None
    certificate_due_date: Optional[datetime.datetime] = None
    owner_first_name: Optional[str] = None
    owner_last_name: Optional[str] = None
    owner_alias: Optional[str] = None
    owner_department_name: Optional[str] = None
    technician_first_name: Optional[str] = None
    technician_last_name: Optional[str] = None
    technician_alias: Optional[str] = None
    technician_department_name: Optional[str] = None
    assigned_employees: Union[
        None,
        None,
        List["AssetToAssetMaintenancePlanResponseAssignedEmployee"],
    ] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        maintenance_plan_id = self.maintenance_plan_id

        maintenance_plan_name = self.maintenance_plan_name

        task_notes = self.task_notes

        last_service_task = self.last_service_task

        last_service_date: Optional[str]
        if not self.last_service_date:
            last_service_date = None
        elif isinstance(self.last_service_date, datetime.datetime):
            last_service_date = self.last_service_date.isoformat()
        else:
            last_service_date = self.last_service_date

        next_service_task = self.next_service_task

        next_service_date: Optional[str]
        if not self.next_service_date:
            next_service_date = None
        elif isinstance(self.next_service_date, datetime.datetime):
            next_service_date = self.next_service_date.isoformat()
        else:
            next_service_date = self.next_service_date

        certificate_due_date: Optional[str]
        if not self.certificate_due_date:
            certificate_due_date = None
        elif isinstance(self.certificate_due_date, datetime.datetime):
            certificate_due_date = self.certificate_due_date.isoformat()
        else:
            certificate_due_date = self.certificate_due_date

        owner_first_name = self.owner_first_name

        owner_last_name = self.owner_last_name

        owner_alias = self.owner_alias

        owner_department_name = self.owner_department_name

        technician_first_name = self.technician_first_name

        technician_last_name = self.technician_last_name

        technician_alias = self.technician_alias

        technician_department_name = self.technician_department_name

        assigned_employees: Optional[List[Dict[str, Any]]] = None
        if self.assigned_employees:
            assigned_employees = []
            for assigned_employees_item_data in self.assigned_employees:
                assigned_employees_item = assigned_employees_item_data.to_dict()
                assigned_employees.append(assigned_employees_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if maintenance_plan_id is not None:
            field_dict["MaintenancePlanId"] = maintenance_plan_id
        if maintenance_plan_name is not None:
            field_dict["MaintenancePlanName"] = maintenance_plan_name
        if task_notes is not None:
            field_dict["TaskNotes"] = task_notes
        if last_service_task is not None:
            field_dict["LastServiceTask"] = last_service_task
        if last_service_date is not None:
            field_dict["LastServiceDate"] = last_service_date
        if next_service_task is not None:
            field_dict["NextServiceTask"] = next_service_task
        if next_service_date is not None:
            field_dict["NextServiceDate"] = next_service_date
        if certificate_due_date is not None:
            field_dict["CertificateDueDate"] = certificate_due_date
        if owner_first_name is not None:
            field_dict["OwnerFirstName"] = owner_first_name
        if owner_last_name is not None:
            field_dict["OwnerLastName"] = owner_last_name
        if owner_alias is not None:
            field_dict["OwnerAlias"] = owner_alias
        if owner_department_name is not None:
            field_dict["OwnerDepartmentName"] = owner_department_name
        if technician_first_name is not None:
            field_dict["TechnicianFirstName"] = technician_first_name
        if technician_last_name is not None:
            field_dict["TechnicianLastName"] = technician_last_name
        if technician_alias is not None:
            field_dict["TechnicianAlias"] = technician_alias
        if technician_department_name is not None:
            field_dict["TechnicianDepartmentName"] = technician_department_name
        if assigned_employees is not None:
            field_dict["AssignedEmployees"] = assigned_employees

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_asset_to_asset_maintenance_plan_response_assigned_employee import (
            AssetToAssetMaintenancePlanResponseAssignedEmployee,
        )

        d = dict(src_dict)
        maintenance_plan_id = d.pop("MaintenancePlanId", None)

        maintenance_plan_name = d.pop("MaintenancePlanName", None)

        task_notes = d.pop("TaskNotes", None)

        last_service_task = d.pop("LastServiceTask", None)

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

        next_service_task = d.pop("NextServiceTask", None)

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

        def _parse_certificate_due_date(
            data: object,
        ) -> Optional[datetime.datetime]:
            if not data:
                return None
            try:
                if not isinstance(data, str):
                    raise TypeError()
                certificate_due_date_type_0 = isoparse(data)

                return certificate_due_date_type_0
            except Exception:
                pass
            return cast(Optional[datetime.datetime], data)

        certificate_due_date = _parse_certificate_due_date(d.pop("CertificateDueDate", None))

        owner_first_name = d.pop("OwnerFirstName", None)

        owner_last_name = d.pop("OwnerLastName", None)

        owner_alias = d.pop("OwnerAlias", None)

        owner_department_name = d.pop("OwnerDepartmentName", None)

        technician_first_name = d.pop("TechnicianFirstName", None)

        technician_last_name = d.pop("TechnicianLastName", None)

        technician_alias = d.pop("TechnicianAlias", None)

        technician_department_name = d.pop("TechnicianDepartmentName", None)

        assigned_employees = []
        _assigned_employees = d.pop("AssignedEmployees", None)
        for assigned_employees_item_data in _assigned_employees or []:
            assigned_employees_item = AssetToAssetMaintenancePlanResponseAssignedEmployee.from_dict(
                assigned_employees_item_data
            )

            assigned_employees.append(assigned_employees_item)

        qualer_api_models_asset_to_asset_maintenance_plan_response = cls(
            maintenance_plan_id=maintenance_plan_id,
            maintenance_plan_name=maintenance_plan_name,
            task_notes=task_notes,
            last_service_task=last_service_task,
            last_service_date=last_service_date,
            next_service_task=next_service_task,
            next_service_date=next_service_date,
            certificate_due_date=certificate_due_date,
            owner_first_name=owner_first_name,
            owner_last_name=owner_last_name,
            owner_alias=owner_alias,
            owner_department_name=owner_department_name,
            technician_first_name=technician_first_name,
            technician_last_name=technician_last_name,
            technician_alias=technician_alias,
            technician_department_name=technician_department_name,
            assigned_employees=assigned_employees,
        )

        qualer_api_models_asset_to_asset_maintenance_plan_response.additional_properties = d
        return qualer_api_models_asset_to_asset_maintenance_plan_response

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
