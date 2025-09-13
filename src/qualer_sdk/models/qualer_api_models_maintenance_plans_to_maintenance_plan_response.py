from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.qualer_api_models_maintenance_plans_to_maintenance_task_response import (
        MaintenancePlansToMaintenanceTaskResponse,
    )


T = TypeVar("T", bound="MaintenancePlansToMaintenancePlanResponse")


@_attrs_define
class MaintenancePlansToMaintenancePlanResponse:
    """
    Attributes:
        maintenance_plan_id (Optional[int]):
        maintenance_plan_name (Optional[str]):
        is_template (Optional[bool]):
        company_name (Optional[str]):
        maintenance_tasks (Optional[List['MaintenancePlansToMaintenanceTaskResponse']]):
    """

    maintenance_plan_id: Optional[int] = None
    maintenance_plan_name: Optional[str] = None
    is_template: Optional[bool] = None
    company_name: Optional[str] = None
    maintenance_tasks: Union[None, List["MaintenancePlansToMaintenanceTaskResponse"]] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        maintenance_plan_id = self.maintenance_plan_id

        maintenance_plan_name = self.maintenance_plan_name

        is_template = self.is_template

        company_name = self.company_name

        maintenance_tasks: Optional[List[Dict[str, Any]]] = None
        if self.maintenance_tasks:
            maintenance_tasks = []
            for maintenance_tasks_item_data in self.maintenance_tasks:
                maintenance_tasks_item = maintenance_tasks_item_data.to_dict()
                maintenance_tasks.append(maintenance_tasks_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if maintenance_plan_id is not None:
            field_dict["MaintenancePlanId"] = maintenance_plan_id
        if maintenance_plan_name is not None:
            field_dict["MaintenancePlanName"] = maintenance_plan_name
        if is_template is not None:
            field_dict["IsTemplate"] = is_template
        if company_name is not None:
            field_dict["CompanyName"] = company_name
        if maintenance_tasks is not None:
            field_dict["MaintenanceTasks"] = maintenance_tasks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_maintenance_plans_to_maintenance_task_response import (
            MaintenancePlansToMaintenanceTaskResponse,
        )

        d = dict(src_dict)
        maintenance_plan_id = d.pop("MaintenancePlanId", None)

        maintenance_plan_name = d.pop("MaintenancePlanName", None)

        is_template = d.pop("IsTemplate", None)

        company_name = d.pop("CompanyName", None)

        maintenance_tasks = []
        _maintenance_tasks = d.pop("MaintenanceTasks", None)
        for maintenance_tasks_item_data in _maintenance_tasks or []:
            maintenance_tasks_item = MaintenancePlansToMaintenanceTaskResponse.from_dict(
                maintenance_tasks_item_data
            )

            maintenance_tasks.append(maintenance_tasks_item)

        qualer_api_models_maintenance_plans_to_maintenance_plan_response = cls(
            maintenance_plan_id=maintenance_plan_id,
            maintenance_plan_name=maintenance_plan_name,
            is_template=is_template,
            company_name=company_name,
            maintenance_tasks=maintenance_tasks,
        )

        qualer_api_models_maintenance_plans_to_maintenance_plan_response.additional_properties = d
        return qualer_api_models_maintenance_plans_to_maintenance_plan_response

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
