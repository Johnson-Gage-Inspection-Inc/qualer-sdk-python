import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsClientsFromClientCompanySearchModel")


@_attrs_define
class QualerApiModelsClientsFromClientCompanySearchModel:
    """
    Attributes:
        legacy_id (Union[Unset, str]):
        account_number_text (Union[Unset, str]):
        company_name (Union[Unset, str]):
        take (Union[Unset, int]):
        modified_after (Union[Unset, datetime.datetime]):
    """

    legacy_id: Union[Unset, str] = UNSET
    account_number_text: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    take: Union[Unset, int] = UNSET
    modified_after: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        legacy_id = self.legacy_id

        account_number_text = self.account_number_text

        company_name = self.company_name

        take = self.take

        modified_after: Union[Unset, str] = UNSET
        if not isinstance(self.modified_after, Unset):
            modified_after = self.modified_after.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if legacy_id is not UNSET:
            field_dict["LegacyId"] = legacy_id
        if account_number_text is not UNSET:
            field_dict["AccountNumberText"] = account_number_text
        if company_name is not UNSET:
            field_dict["CompanyName"] = company_name
        if take is not UNSET:
            field_dict["Take"] = take
        if modified_after is not UNSET:
            field_dict["ModifiedAfter"] = modified_after

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        legacy_id = d.pop("LegacyId", UNSET)

        account_number_text = d.pop("AccountNumberText", UNSET)

        company_name = d.pop("CompanyName", UNSET)

        take = d.pop("Take", UNSET)

        _modified_after = d.pop("ModifiedAfter", UNSET)
        modified_after: Union[Unset, datetime.datetime]
        if isinstance(_modified_after, Unset):
            modified_after = UNSET
        else:
            modified_after = isoparse(_modified_after)

        qualer_api_models_clients_from_client_company_search_model = cls(
            legacy_id=legacy_id,
            account_number_text=account_number_text,
            company_name=company_name,
            take=take,
            modified_after=modified_after,
        )

        qualer_api_models_clients_from_client_company_search_model.additional_properties = (
            d
        )
        return qualer_api_models_clients_from_client_company_search_model

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
