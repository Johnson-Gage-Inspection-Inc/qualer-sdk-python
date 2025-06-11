from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsReportDatasetsToToolRangeAttributeResponse")


@_attrs_define
class QualerApiModelsReportDatasetsToToolRangeAttributeResponse:
    """
    Attributes:
        measurement_point_id (Union[Unset, int]):
        service_order_item_id (Union[Unset, int]):
        tool_id (Union[Unset, int]):
        range_title (Union[Unset, str]):
        range_subtitle (Union[Unset, str]):
        attribute_name (Union[Unset, str]):
        attribute_value (Union[Unset, str]):
    """

    measurement_point_id: Union[Unset, int] = UNSET
    service_order_item_id: Union[Unset, int] = UNSET
    tool_id: Union[Unset, int] = UNSET
    range_title: Union[Unset, str] = UNSET
    range_subtitle: Union[Unset, str] = UNSET
    attribute_name: Union[Unset, str] = UNSET
    attribute_value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measurement_point_id = self.measurement_point_id

        service_order_item_id = self.service_order_item_id

        tool_id = self.tool_id

        range_title = self.range_title

        range_subtitle = self.range_subtitle

        attribute_name = self.attribute_name

        attribute_value = self.attribute_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measurement_point_id is not UNSET:
            field_dict["MeasurementPointId"] = measurement_point_id
        if service_order_item_id is not UNSET:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if tool_id is not UNSET:
            field_dict["ToolId"] = tool_id
        if range_title is not UNSET:
            field_dict["RangeTitle"] = range_title
        if range_subtitle is not UNSET:
            field_dict["RangeSubtitle"] = range_subtitle
        if attribute_name is not UNSET:
            field_dict["AttributeName"] = attribute_name
        if attribute_value is not UNSET:
            field_dict["AttributeValue"] = attribute_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        measurement_point_id = d.pop("MeasurementPointId", UNSET)

        service_order_item_id = d.pop("ServiceOrderItemId", UNSET)

        tool_id = d.pop("ToolId", UNSET)

        range_title = d.pop("RangeTitle", UNSET)

        range_subtitle = d.pop("RangeSubtitle", UNSET)

        attribute_name = d.pop("AttributeName", UNSET)

        attribute_value = d.pop("AttributeValue", UNSET)

        qualer_api_models_report_datasets_to_tool_range_attribute_response = cls(
            measurement_point_id=measurement_point_id,
            service_order_item_id=service_order_item_id,
            tool_id=tool_id,
            range_title=range_title,
            range_subtitle=range_subtitle,
            attribute_name=attribute_name,
            attribute_value=attribute_value,
        )

        qualer_api_models_report_datasets_to_tool_range_attribute_response.additional_properties = (
            d
        )
        return qualer_api_models_report_datasets_to_tool_range_attribute_response

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
