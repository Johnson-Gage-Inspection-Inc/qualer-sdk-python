from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel"
)


@_attrs_define
class QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel:
    """
    Attributes:
        service_option_id (Union[Unset, int]):
        service_option (Union[Unset, str]):
        service_option_code (Union[Unset, str]):
        option_type (Union[Unset, str]):
        description (Union[Unset, str]):
        service_task_id (Union[Unset, int]):
        service_code (Union[Unset, str]):
        document_number (Union[Unset, str]):
        document_section (Union[Unset, str]):
        capability_id (Union[Unset, int]):
        service_type_id (Union[Unset, int]):
        service_task_price_id (Union[Unset, int]):
        service_pricing_id (Union[Unset, int]):
        price (Union[Unset, float]):
        is_hourly (Union[Unset, bool]):
        issue (Union[Unset, str]):
        log_error (Union[Unset, str]):
    """

    service_option_id: Union[Unset, int] = UNSET
    service_option: Union[Unset, str] = UNSET
    service_option_code: Union[Unset, str] = UNSET
    option_type: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    service_task_id: Union[Unset, int] = UNSET
    service_code: Union[Unset, str] = UNSET
    document_number: Union[Unset, str] = UNSET
    document_section: Union[Unset, str] = UNSET
    capability_id: Union[Unset, int] = UNSET
    service_type_id: Union[Unset, int] = UNSET
    service_task_price_id: Union[Unset, int] = UNSET
    service_pricing_id: Union[Unset, int] = UNSET
    price: Union[Unset, float] = UNSET
    is_hourly: Union[Unset, bool] = UNSET
    issue: Union[Unset, str] = UNSET
    log_error: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_option_id = self.service_option_id

        service_option = self.service_option

        service_option_code = self.service_option_code

        option_type = self.option_type

        description = self.description

        service_task_id = self.service_task_id

        service_code = self.service_code

        document_number = self.document_number

        document_section = self.document_section

        capability_id = self.capability_id

        service_type_id = self.service_type_id

        service_task_price_id = self.service_task_price_id

        service_pricing_id = self.service_pricing_id

        price = self.price

        is_hourly = self.is_hourly

        issue = self.issue

        log_error = self.log_error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_option_id is not UNSET:
            field_dict["ServiceOptionId"] = service_option_id
        if service_option is not UNSET:
            field_dict["ServiceOption"] = service_option
        if service_option_code is not UNSET:
            field_dict["ServiceOptionCode"] = service_option_code
        if option_type is not UNSET:
            field_dict["OptionType"] = option_type
        if description is not UNSET:
            field_dict["Description"] = description
        if service_task_id is not UNSET:
            field_dict["ServiceTaskId"] = service_task_id
        if service_code is not UNSET:
            field_dict["ServiceCode"] = service_code
        if document_number is not UNSET:
            field_dict["DocumentNumber"] = document_number
        if document_section is not UNSET:
            field_dict["DocumentSection"] = document_section
        if capability_id is not UNSET:
            field_dict["CapabilityId"] = capability_id
        if service_type_id is not UNSET:
            field_dict["ServiceTypeId"] = service_type_id
        if service_task_price_id is not UNSET:
            field_dict["ServiceTaskPriceId"] = service_task_price_id
        if service_pricing_id is not UNSET:
            field_dict["ServicePricingId"] = service_pricing_id
        if price is not UNSET:
            field_dict["Price"] = price
        if is_hourly is not UNSET:
            field_dict["IsHourly"] = is_hourly
        if issue is not UNSET:
            field_dict["Issue"] = issue
        if log_error is not UNSET:
            field_dict["LogError"] = log_error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_option_id = d.pop("ServiceOptionId", UNSET)

        service_option = d.pop("ServiceOption", UNSET)

        service_option_code = d.pop("ServiceOptionCode", UNSET)

        option_type = d.pop("OptionType", UNSET)

        description = d.pop("Description", UNSET)

        service_task_id = d.pop("ServiceTaskId", UNSET)

        service_code = d.pop("ServiceCode", UNSET)

        document_number = d.pop("DocumentNumber", UNSET)

        document_section = d.pop("DocumentSection", UNSET)

        capability_id = d.pop("CapabilityId", UNSET)

        service_type_id = d.pop("ServiceTypeId", UNSET)

        service_task_price_id = d.pop("ServiceTaskPriceId", UNSET)

        service_pricing_id = d.pop("ServicePricingId", UNSET)

        price = d.pop("Price", UNSET)

        is_hourly = d.pop("IsHourly", UNSET)

        issue = d.pop("Issue", UNSET)

        log_error = d.pop("LogError", UNSET)

        qualer_web_mvc_areas_api_models_service_prices_from_service_price_bulk_edit_model = cls(
            service_option_id=service_option_id,
            service_option=service_option,
            service_option_code=service_option_code,
            option_type=option_type,
            description=description,
            service_task_id=service_task_id,
            service_code=service_code,
            document_number=document_number,
            document_section=document_section,
            capability_id=capability_id,
            service_type_id=service_type_id,
            service_task_price_id=service_task_price_id,
            service_pricing_id=service_pricing_id,
            price=price,
            is_hourly=is_hourly,
            issue=issue,
            log_error=log_error,
        )

        qualer_web_mvc_areas_api_models_service_prices_from_service_price_bulk_edit_model.additional_properties = (
            d
        )
        return qualer_web_mvc_areas_api_models_service_prices_from_service_price_bulk_edit_model

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
