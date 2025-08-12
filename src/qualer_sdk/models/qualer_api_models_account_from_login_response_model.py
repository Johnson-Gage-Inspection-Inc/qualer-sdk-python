from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsAccountFromLoginResponseModel")


@_attrs_define
class QualerApiModelsAccountFromLoginResponseModel:
    """
    Attributes:
        token (Union[None, Unset, UUID]):  Example: 00000000-0000-0000-0000-000000000000.
    """

    token: Union[None, Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token: Union[None, Unset, str] = UNSET
        if self.token and not isinstance(self.token, Unset):
            token = str(self.token)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["Token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _token = d.pop("Token", UNSET)
        token: Union[None, Unset, UUID]
        if isinstance(_token, Unset):
            token = UNSET
        else:
            token = UUID(_token)

        qualer_api_models_account_from_login_response_model = cls(
            token=token,
        )

        qualer_api_models_account_from_login_response_model.additional_properties = d
        return qualer_api_models_account_from_login_response_model

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
