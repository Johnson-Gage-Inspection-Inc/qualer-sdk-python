import datetime
from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="QualerApiModelsVendorsFromVendorCompanySearchModel")


@_attrs_define
class QualerApiModelsVendorsFromVendorCompanySearchModel:
    """
    Attributes:
        account_number_text (Optional[str]):
        company_name (Optional[str]):
        take (Optional[int]):
        modified_after (Optional[datetime.datetime]):
    """

    account_number_text: Optional[str] = None
    company_name: Optional[str] = None
    take: Optional[int] = None
    modified_after: Optional[datetime.datetime] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_number_text = self.account_number_text

        company_name = self.company_name

        take = self.take

        modified_after: Optional[str] = None
        if self.modified_after:
            modified_after = self.modified_after.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_number_text is not None:
            field_dict["AccountNumberText"] = account_number_text
        if company_name is not None:
            field_dict["CompanyName"] = company_name
        if take is not None:
            field_dict["Take"] = take
        if modified_after is not None:
            field_dict["ModifiedAfter"] = modified_after

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_number_text = d.pop("AccountNumberText", None)

        company_name = d.pop("CompanyName", None)

        take = d.pop("Take", None)

        _modified_after = d.pop("ModifiedAfter", None)
        modified_after: Optional[datetime.datetime]
        if not _modified_after:
            modified_after = None
        else:
            modified_after = isoparse(_modified_after)

        qualer_api_models_vendors_from_vendor_company_search_model = cls(
            account_number_text=account_number_text,
            company_name=company_name,
            take=take,
            modified_after=modified_after,
        )

        qualer_api_models_vendors_from_vendor_company_search_model.additional_properties = d
        return qualer_api_models_vendors_from_vendor_company_search_model

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
