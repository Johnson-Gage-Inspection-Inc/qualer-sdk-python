from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReportDatasetsToMeasurementChartResponse")


@_attrs_define
class ReportDatasetsToMeasurementChartResponse:
    """
    Attributes:
        service_order_item_id (Optional[int]):
        measurement_set_id (Optional[int]):
        chart_type (Optional[int]):
        chart_image (Optional[str]):
        nominal (Optional[str]):
        title (Optional[str]):
        unit_of_measure (Optional[str]):
        abbreviated_uom (Optional[str]):
    """

    service_order_item_id: Optional[int] = None
    measurement_set_id: Optional[int] = None
    chart_type: Optional[int] = None
    chart_image: Optional[str] = None
    nominal: Optional[str] = None
    title: Optional[str] = None
    unit_of_measure: Optional[str] = None
    abbreviated_uom: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_order_item_id = self.service_order_item_id
        measurement_set_id = self.measurement_set_id
        chart_type = self.chart_type
        chart_image = self.chart_image
        nominal = self.nominal
        title = self.title
        unit_of_measure = self.unit_of_measure
        abbreviated_uom = self.abbreviated_uom
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_item_id is not None:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if measurement_set_id is not None:
            field_dict["MeasurementSetId"] = measurement_set_id
        if chart_type is not None:
            field_dict["ChartType"] = chart_type
        if chart_image is not None:
            field_dict["ChartImage"] = chart_image
        if nominal is not None:
            field_dict["Nominal"] = nominal
        if title is not None:
            field_dict["Title"] = title
        if unit_of_measure is not None:
            field_dict["UnitOfMeasure"] = unit_of_measure
        if abbreviated_uom is not None:
            field_dict["AbbreviatedUOM"] = abbreviated_uom
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_item_id = d.pop("ServiceOrderItemId", None)
        measurement_set_id = d.pop("MeasurementSetId", None)
        chart_type = d.pop("ChartType", None)
        chart_image = d.pop("ChartImage", None)
        nominal = d.pop("Nominal", None)
        title = d.pop("Title", None)
        unit_of_measure = d.pop("UnitOfMeasure", None)
        abbreviated_uom = d.pop("AbbreviatedUOM", None)
        qualer_api_models_report_datasets_to_measurement_chart_response = cls(
            service_order_item_id=service_order_item_id,
            measurement_set_id=measurement_set_id,
            chart_type=chart_type,
            chart_image=chart_image,
            nominal=nominal,
            title=title,
            unit_of_measure=unit_of_measure,
            abbreviated_uom=abbreviated_uom,
        )
        qualer_api_models_report_datasets_to_measurement_chart_response.additional_properties = d
        return qualer_api_models_report_datasets_to_measurement_chart_response

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
