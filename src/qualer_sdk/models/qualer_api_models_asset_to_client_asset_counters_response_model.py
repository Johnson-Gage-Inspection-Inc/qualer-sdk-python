from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsAssetToClientAssetCountersResponseModel")


@_attrs_define
class QualerApiModelsAssetToClientAssetCountersResponseModel:
    """
    Attributes:
        client_assets_collected (Union[Unset, int]):
        client_unset (Union[Unset, int]):
        client_due_for_service (Union[Unset, int]):
        client_past_due (Union[Unset, int]):
        client_out_of_service (Union[Unset, int]):
        client_without_schedule (Union[Unset, int]):
    """

    client_assets_collected: Union[Unset, int] = UNSET
    client_unset: Union[Unset, int] = UNSET
    client_due_for_service: Union[Unset, int] = UNSET
    client_past_due: Union[Unset, int] = UNSET
    client_out_of_service: Union[Unset, int] = UNSET
    client_without_schedule: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_assets_collected = self.client_assets_collected

        client_unset = self.client_unset

        client_due_for_service = self.client_due_for_service

        client_past_due = self.client_past_due

        client_out_of_service = self.client_out_of_service

        client_without_schedule = self.client_without_schedule

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_assets_collected is not UNSET:
            field_dict["ClientAssetsCollected"] = client_assets_collected
        if client_unset is not UNSET:
            field_dict["ClientUnset"] = client_unset
        if client_due_for_service is not UNSET:
            field_dict["ClientDueForService"] = client_due_for_service
        if client_past_due is not UNSET:
            field_dict["ClientPastDue"] = client_past_due
        if client_out_of_service is not UNSET:
            field_dict["ClientOutOfService"] = client_out_of_service
        if client_without_schedule is not UNSET:
            field_dict["ClientWithoutSchedule"] = client_without_schedule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_assets_collected = d.pop("ClientAssetsCollected", UNSET)

        client_unset = d.pop("ClientUnset", UNSET)

        client_due_for_service = d.pop("ClientDueForService", UNSET)

        client_past_due = d.pop("ClientPastDue", UNSET)

        client_out_of_service = d.pop("ClientOutOfService", UNSET)

        client_without_schedule = d.pop("ClientWithoutSchedule", UNSET)

        qualer_api_models_asset_to_client_asset_counters_response_model = cls(
            client_assets_collected=client_assets_collected,
            client_unset=client_unset,
            client_due_for_service=client_due_for_service,
            client_past_due=client_past_due,
            client_out_of_service=client_out_of_service,
            client_without_schedule=client_without_schedule,
        )

        qualer_api_models_asset_to_client_asset_counters_response_model.additional_properties = (
            d
        )
        return qualer_api_models_asset_to_client_asset_counters_response_model

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
