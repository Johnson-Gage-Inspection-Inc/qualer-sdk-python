from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel")


@_attrs_define
class QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel:
    """
    Attributes:
        service_option_id (Optional[int]):
        service_option (Optional[str]):
        service_option_code (Optional[str]):
        option_type (Optional[str]):
        description (Optional[str]):
        service_task_id (Optional[int]):
        service_code (Optional[str]):
        document_number (Optional[str]):
        document_section (Optional[str]):
        capability_id (Optional[int]):
        service_type_id (Optional[int]):
        service_task_price_id (Optional[int]):
        service_pricing_id (Optional[int]):
        price (Optional[float]):
        is_hourly (Optional[bool]):
        issue (Optional[str]):
        log_error (Optional[str]):
    """

    service_option_id: Optional[int] = None
    service_option: Optional[str] = None
    service_option_code: Optional[str] = None
    option_type: Optional[str] = None
    description: Optional[str] = None
    service_task_id: Optional[int] = None
    service_code: Optional[str] = None
    document_number: Optional[str] = None
    document_section: Optional[str] = None
    capability_id: Optional[int] = None
    service_type_id: Optional[int] = None
    service_task_price_id: Optional[int] = None
    service_pricing_id: Optional[int] = None
    price: Optional[float] = None
    is_hourly: Optional[bool] = None
    issue: Optional[str] = None
    log_error: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_option_id is not None:
            field_dict["ServiceOptionId"] = service_option_id
        if service_option is not None:
            field_dict["ServiceOption"] = service_option
        if service_option_code is not None:
            field_dict["ServiceOptionCode"] = service_option_code
        if option_type is not None:
            field_dict["OptionType"] = option_type
        if description is not None:
            field_dict["Description"] = description
        if service_task_id is not None:
            field_dict["ServiceTaskId"] = service_task_id
        if service_code is not None:
            field_dict["ServiceCode"] = service_code
        if document_number is not None:
            field_dict["DocumentNumber"] = document_number
        if document_section is not None:
            field_dict["DocumentSection"] = document_section
        if capability_id is not None:
            field_dict["CapabilityId"] = capability_id
        if service_type_id is not None:
            field_dict["ServiceTypeId"] = service_type_id
        if service_task_price_id is not None:
            field_dict["ServiceTaskPriceId"] = service_task_price_id
        if service_pricing_id is not None:
            field_dict["ServicePricingId"] = service_pricing_id
        if price is not None:
            field_dict["Price"] = price
        if is_hourly is not None:
            field_dict["IsHourly"] = is_hourly
        if issue is not None:
            field_dict["Issue"] = issue
        if log_error is not None:
            field_dict["LogError"] = log_error
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_option_id = d.pop("ServiceOptionId", None)
        service_option = d.pop("ServiceOption", None)
        service_option_code = d.pop("ServiceOptionCode", None)
        option_type = d.pop("OptionType", None)
        description = d.pop("Description", None)
        service_task_id = d.pop("ServiceTaskId", None)
        service_code = d.pop("ServiceCode", None)
        document_number = d.pop("DocumentNumber", None)
        document_section = d.pop("DocumentSection", None)
        capability_id = d.pop("CapabilityId", None)
        service_type_id = d.pop("ServiceTypeId", None)
        service_task_price_id = d.pop("ServiceTaskPriceId", None)
        service_pricing_id = d.pop("ServicePricingId", None)
        price = d.pop("Price", None)
        is_hourly = d.pop("IsHourly", None)
        issue = d.pop("Issue", None)
        log_error = d.pop("LogError", None)
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
