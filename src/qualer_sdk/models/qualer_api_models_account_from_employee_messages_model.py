from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsAccountFromEmployeeMessagesModel")


@_attrs_define
class QualerApiModelsAccountFromEmployeeMessagesModel:
    """
    Attributes:
        period (Union[Unset, int]):
        site_id (Union[Unset, int]):
    """

    period: Union[Unset, int] = UNSET
    site_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        period = self.period

        site_id = self.site_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if period is not UNSET:
            field_dict["Period"] = period
        if site_id is not UNSET:
            field_dict["SiteId"] = site_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        period = d.pop("Period", UNSET)

        site_id = d.pop("SiteId", UNSET)

        qualer_api_models_account_from_employee_messages_model = cls(
            period=period,
            site_id=site_id,
        )

        qualer_api_models_account_from_employee_messages_model.additional_properties = d
        return qualer_api_models_account_from_employee_messages_model

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
