from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerWebMvcAreasApiModelsAccountToLoginModel")


@_attrs_define
class QualerWebMvcAreasApiModelsAccountToLoginModel:
    """
    Attributes:
        user_name (str):
        password (str):
        clear_previous_tokens (Union[Unset, bool]):
    """

    user_name: str
    password: str
    clear_previous_tokens: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_name = self.user_name

        password = self.password

        clear_previous_tokens = self.clear_previous_tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "UserName": user_name,
                "Password": password,
            }
        )
        if clear_previous_tokens is not UNSET:
            field_dict["ClearPreviousTokens"] = clear_previous_tokens

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_name = d.pop("UserName")

        password = d.pop("Password")

        clear_previous_tokens = d.pop("ClearPreviousTokens", UNSET)

        qualer_web_mvc_areas_api_models_account_to_login_model = cls(
            user_name=user_name,
            password=password,
            clear_previous_tokens=clear_previous_tokens,
        )

        qualer_web_mvc_areas_api_models_account_to_login_model.additional_properties = d
        return qualer_web_mvc_areas_api_models_account_to_login_model

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
