from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReportDatasetsToToolRangeAttributeResponse")


@_attrs_define
class ReportDatasetsToToolRangeAttributeResponse:
    """
    Attributes:
        measurement_point_id (Optional[int]):
        service_order_item_id (Optional[int]):
        tool_id (Optional[int]):
        range_title (Optional[str]):
        range_subtitle (Optional[str]):
        attribute_name (Optional[str]):
        attribute_value (Optional[str]):
    """

    measurement_point_id: Optional[int] = None
    service_order_item_id: Optional[int] = None
    tool_id: Optional[int] = None
    range_title: Optional[str] = None
    range_subtitle: Optional[str] = None
    attribute_name: Optional[str] = None
    attribute_value: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        measurement_point_id = self.measurement_point_id

        service_order_item_id = self.service_order_item_id

        tool_id = self.tool_id

        range_title = self.range_title

        range_subtitle = self.range_subtitle

        attribute_name = self.attribute_name

        attribute_value = self.attribute_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measurement_point_id is not None:
            field_dict["MeasurementPointId"] = measurement_point_id
        if service_order_item_id is not None:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if tool_id is not None:
            field_dict["ToolId"] = tool_id
        if range_title is not None:
            field_dict["RangeTitle"] = range_title
        if range_subtitle is not None:
            field_dict["RangeSubtitle"] = range_subtitle
        if attribute_name is not None:
            field_dict["AttributeName"] = attribute_name
        if attribute_value is not None:
            field_dict["AttributeValue"] = attribute_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        measurement_point_id = d.pop("MeasurementPointId", None)

        service_order_item_id = d.pop("ServiceOrderItemId", None)

        tool_id = d.pop("ToolId", None)

        range_title = d.pop("RangeTitle", None)

        range_subtitle = d.pop("RangeSubtitle", None)

        attribute_name = d.pop("AttributeName", None)

        attribute_value = d.pop("AttributeValue", None)

        qualer_api_models_report_datasets_to_tool_range_attribute_response = cls(
            measurement_point_id=measurement_point_id,
            service_order_item_id=service_order_item_id,
            tool_id=tool_id,
            range_title=range_title,
            range_subtitle=range_subtitle,
            attribute_name=attribute_name,
            attribute_value=attribute_value,
        )

        qualer_api_models_report_datasets_to_tool_range_attribute_response.additional_properties = d
        return qualer_api_models_report_datasets_to_tool_range_attribute_response

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
