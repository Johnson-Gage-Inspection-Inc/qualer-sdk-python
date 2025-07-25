from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsAccountToLogoutModel")


@_attrs_define
class QualerApiModelsAccountToLogoutModel:
    """
    Attributes:
        logout_action (Union[Unset, str]):
    """

    logout_action: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logout_action = self.logout_action

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logout_action is not UNSET:
            field_dict["LogoutAction"] = logout_action

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        logout_action = d.pop("LogoutAction", UNSET)

        qualer_api_models_account_to_logout_model = cls(
            logout_action=logout_action,
        )

        qualer_api_models_account_to_logout_model.additional_properties = d
        return qualer_api_models_account_to_logout_model

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
