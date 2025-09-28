from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AccountFromLoginResponseModel")


@_attrs_define
class AccountFromLoginResponseModel:
    """
    Attributes:
        token (Optional[UUID]):  Example: 00000000-0000-0000-0000-000000000000.
    """

    token: Optional[UUID] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token: Optional[str] = None
        if self.token:
            token = str(self.token)
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not None:
            field_dict["Token"] = token
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _token = d.pop("Token", None)
        token: Optional[UUID]
        if not _token:
            token = None
        else:
            token = UUID(_token)
        qualer_api_models_account_from_login_response_model = cls(
            token=token,
        )
        qualer_api_models_account_from_login_response_model.additional_properties = d
        return qualer_api_models_account_from_login_response_model

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
