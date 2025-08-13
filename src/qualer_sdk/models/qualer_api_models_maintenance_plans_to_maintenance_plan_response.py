from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualer_api_models_maintenance_plans_to_maintenance_task_response import (
        QualerApiModelsMaintenancePlansToMaintenanceTaskResponse,
    )


T = TypeVar("T", bound="QualerApiModelsMaintenancePlansToMaintenancePlanResponse")


@_attrs_define
class QualerApiModelsMaintenancePlansToMaintenancePlanResponse:
    """
    Attributes:
        maintenance_plan_id (Union[None, Unset, int]):
        maintenance_plan_name (Union[None, Unset, str]):
        is_template (Union[None, Unset, bool]):
        company_name (Union[None, Unset, str]):
        maintenance_tasks (Union[None, Unset, list['QualerApiModelsMaintenancePlansToMaintenanceTaskResponse']]):
    """

    maintenance_plan_id: Union[None, Unset, int] = UNSET
    maintenance_plan_name: Union[None, Unset, str] = UNSET
    is_template: Union[None, Unset, bool] = UNSET
    company_name: Union[None, Unset, str] = UNSET
    maintenance_tasks: Union[None, Unset, list["QualerApiModelsMaintenancePlansToMaintenanceTaskResponse"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        maintenance_plan_id = self.maintenance_plan_id

        maintenance_plan_name = self.maintenance_plan_name

        is_template = self.is_template

        company_name = self.company_name

        maintenance_tasks: Union[None, Unset, list[dict[str, Any]]] = UNSET
        if self.maintenance_tasks and not isinstance(self.maintenance_tasks, Unset):
            maintenance_tasks = []
            for maintenance_tasks_item_data in self.maintenance_tasks:
                maintenance_tasks_item = maintenance_tasks_item_data.to_dict()
                maintenance_tasks.append(maintenance_tasks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if maintenance_plan_id is not UNSET:
            field_dict["MaintenancePlanId"] = maintenance_plan_id
        if maintenance_plan_name is not UNSET:
            field_dict["MaintenancePlanName"] = maintenance_plan_name
        if is_template is not UNSET:
            field_dict["IsTemplate"] = is_template
        if company_name is not UNSET:
            field_dict["CompanyName"] = company_name
        if maintenance_tasks is not UNSET:
            field_dict["MaintenanceTasks"] = maintenance_tasks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_maintenance_plans_to_maintenance_task_response import (
            QualerApiModelsMaintenancePlansToMaintenanceTaskResponse,
        )

        d = dict(src_dict)
        maintenance_plan_id = d.pop("MaintenancePlanId", UNSET)

        maintenance_plan_name = d.pop("MaintenancePlanName", UNSET)

        is_template = d.pop("IsTemplate", UNSET)

        company_name = d.pop("CompanyName", UNSET)

        maintenance_tasks = []
        _maintenance_tasks = d.pop("MaintenanceTasks", UNSET)
        for maintenance_tasks_item_data in _maintenance_tasks or []:
            maintenance_tasks_item = (
                QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.from_dict(
                    maintenance_tasks_item_data
                )
            )

            maintenance_tasks.append(maintenance_tasks_item)

        qualer_api_models_maintenance_plans_to_maintenance_plan_response = cls(
            maintenance_plan_id=maintenance_plan_id,
            maintenance_plan_name=maintenance_plan_name,
            is_template=is_template,
            company_name=company_name,
            maintenance_tasks=maintenance_tasks,
        )

        qualer_api_models_maintenance_plans_to_maintenance_plan_response.additional_properties = (
            d
        )
        return qualer_api_models_maintenance_plans_to_maintenance_plan_response

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
