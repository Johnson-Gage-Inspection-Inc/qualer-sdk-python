import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualer_api_models_asset_to_asset_maintenance_plan_response_assigned_employee import (
        QualerApiModelsAssetToAssetMaintenancePlanResponseAssignedEmployee,
    )


T = TypeVar("T", bound="QualerApiModelsAssetToAssetMaintenancePlanResponse")


@_attrs_define
class QualerApiModelsAssetToAssetMaintenancePlanResponse:
    """
    Attributes:
        maintenance_plan_id (Union[None, Unset, int]):
        maintenance_plan_name (Union[None, Unset, str]):
        task_notes (Union[None, Unset, str]):
        last_service_task (Union[None, Unset, str]):
        last_service_date (Union[None, Unset, datetime.datetime]):
        next_service_task (Union[None, Unset, str]):
        next_service_date (Union[None, Unset, datetime.datetime]):
        certificate_due_date (Union[None, Unset, datetime.datetime]):
        owner_first_name (Union[None, Unset, str]):
        owner_last_name (Union[None, Unset, str]):
        owner_alias (Union[None, Unset, str]):
        owner_department_name (Union[None, Unset, str]):
        technician_first_name (Union[None, Unset, str]):
        technician_last_name (Union[None, Unset, str]):
        technician_alias (Union[None, Unset, str]):
        technician_department_name (Union[None, Unset, str]):
        assigned_employees (Union[None, Unset, list['QualerApiModelsAssetToAssetMaintenancePlanResponseAssignedEmployee']]):
    """

    maintenance_plan_id: Union[None, Unset, int] = UNSET
    maintenance_plan_name: Union[None, Unset, str] = UNSET
    task_notes: Union[None, Unset, str] = UNSET
    last_service_task: Union[None, Unset, str] = UNSET
    last_service_date: Union[None, Unset, datetime.datetime] = UNSET
    next_service_task: Union[None, Unset, str] = UNSET
    next_service_date: Union[None, Unset, datetime.datetime] = UNSET
    certificate_due_date: Union[None, Unset, datetime.datetime] = UNSET
    owner_first_name: Union[None, Unset, str] = UNSET
    owner_last_name: Union[None, Unset, str] = UNSET
    owner_alias: Union[None, Unset, str] = UNSET
    owner_department_name: Union[None, Unset, str] = UNSET
    technician_first_name: Union[None, Unset, str] = UNSET
    technician_last_name: Union[None, Unset, str] = UNSET
    technician_alias: Union[None, Unset, str] = UNSET
    technician_department_name: Union[None, Unset, str] = UNSET
    assigned_employees: Union[
        None,
        Unset,
        list["QualerApiModelsAssetToAssetMaintenancePlanResponseAssignedEmployee"],
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        maintenance_plan_id = self.maintenance_plan_id

        maintenance_plan_name = self.maintenance_plan_name

        task_notes = self.task_notes

        last_service_task = self.last_service_task

        last_service_date: Union[None, Unset, str]
        if isinstance(self.last_service_date, Unset):
            last_service_date = UNSET
        elif isinstance(self.last_service_date, datetime.datetime):
            last_service_date = self.last_service_date.isoformat()
        else:
            last_service_date = self.last_service_date

        next_service_task = self.next_service_task

        next_service_date: Union[None, Unset, str]
        if isinstance(self.next_service_date, Unset):
            next_service_date = UNSET
        elif isinstance(self.next_service_date, datetime.datetime):
            next_service_date = self.next_service_date.isoformat()
        else:
            next_service_date = self.next_service_date

        certificate_due_date: Union[None, Unset, str]
        if isinstance(self.certificate_due_date, Unset):
            certificate_due_date = UNSET
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

        assigned_employees: Union[None, Unset, list[dict[str, Any]]] = UNSET
        if self.assigned_employees and not isinstance(self.assigned_employees, Unset):
            assigned_employees = []
            for assigned_employees_item_data in self.assigned_employees:
                assigned_employees_item = assigned_employees_item_data.to_dict()
                assigned_employees.append(assigned_employees_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if maintenance_plan_id is not UNSET:
            field_dict["MaintenancePlanId"] = maintenance_plan_id
        if maintenance_plan_name is not UNSET:
            field_dict["MaintenancePlanName"] = maintenance_plan_name
        if task_notes is not UNSET:
            field_dict["TaskNotes"] = task_notes
        if last_service_task is not UNSET:
            field_dict["LastServiceTask"] = last_service_task
        if last_service_date is not UNSET:
            field_dict["LastServiceDate"] = last_service_date
        if next_service_task is not UNSET:
            field_dict["NextServiceTask"] = next_service_task
        if next_service_date is not UNSET:
            field_dict["NextServiceDate"] = next_service_date
        if certificate_due_date is not UNSET:
            field_dict["CertificateDueDate"] = certificate_due_date
        if owner_first_name is not UNSET:
            field_dict["OwnerFirstName"] = owner_first_name
        if owner_last_name is not UNSET:
            field_dict["OwnerLastName"] = owner_last_name
        if owner_alias is not UNSET:
            field_dict["OwnerAlias"] = owner_alias
        if owner_department_name is not UNSET:
            field_dict["OwnerDepartmentName"] = owner_department_name
        if technician_first_name is not UNSET:
            field_dict["TechnicianFirstName"] = technician_first_name
        if technician_last_name is not UNSET:
            field_dict["TechnicianLastName"] = technician_last_name
        if technician_alias is not UNSET:
            field_dict["TechnicianAlias"] = technician_alias
        if technician_department_name is not UNSET:
            field_dict["TechnicianDepartmentName"] = technician_department_name
        if assigned_employees is not UNSET:
            field_dict["AssignedEmployees"] = assigned_employees

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_asset_to_asset_maintenance_plan_response_assigned_employee import (
            QualerApiModelsAssetToAssetMaintenancePlanResponseAssignedEmployee,
        )

        d = dict(src_dict)
        maintenance_plan_id = d.pop("MaintenancePlanId", UNSET)

        maintenance_plan_name = d.pop("MaintenancePlanName", UNSET)

        task_notes = d.pop("TaskNotes", UNSET)

        last_service_task = d.pop("LastServiceTask", UNSET)

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

        next_service_task = d.pop("NextServiceTask", UNSET)

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

        def _parse_certificate_due_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                certificate_due_date_type_0 = isoparse(data)

                return certificate_due_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        certificate_due_date = _parse_certificate_due_date(
            d.pop("CertificateDueDate", UNSET)
        )

        owner_first_name = d.pop("OwnerFirstName", UNSET)

        owner_last_name = d.pop("OwnerLastName", UNSET)

        owner_alias = d.pop("OwnerAlias", UNSET)

        owner_department_name = d.pop("OwnerDepartmentName", UNSET)

        technician_first_name = d.pop("TechnicianFirstName", UNSET)

        technician_last_name = d.pop("TechnicianLastName", UNSET)

        technician_alias = d.pop("TechnicianAlias", UNSET)

        technician_department_name = d.pop("TechnicianDepartmentName", UNSET)

        assigned_employees = []
        _assigned_employees = d.pop("AssignedEmployees", UNSET)
        for assigned_employees_item_data in _assigned_employees or []:
            assigned_employees_item = QualerApiModelsAssetToAssetMaintenancePlanResponseAssignedEmployee.from_dict(
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

        qualer_api_models_asset_to_asset_maintenance_plan_response.additional_properties = (
            d
        )
        return qualer_api_models_asset_to_asset_maintenance_plan_response

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
