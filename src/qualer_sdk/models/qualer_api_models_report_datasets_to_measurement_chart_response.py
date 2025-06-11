from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsReportDatasetsToMeasurementChartResponse")


@_attrs_define
class QualerApiModelsReportDatasetsToMeasurementChartResponse:
    """
    Attributes:
        service_order_item_id (Union[Unset, int]):
        measurement_set_id (Union[Unset, int]):
        chart_type (Union[Unset, int]):
        chart_image (Union[Unset, str]):
        nominal (Union[Unset, str]):
        title (Union[Unset, str]):
        unit_of_measure (Union[Unset, str]):
        abbreviated_uom (Union[Unset, str]):
    """

    service_order_item_id: Union[Unset, int] = UNSET
    measurement_set_id: Union[Unset, int] = UNSET
    chart_type: Union[Unset, int] = UNSET
    chart_image: Union[Unset, str] = UNSET
    nominal: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    unit_of_measure: Union[Unset, str] = UNSET
    abbreviated_uom: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_order_item_id = self.service_order_item_id

        measurement_set_id = self.measurement_set_id

        chart_type = self.chart_type

        chart_image = self.chart_image

        nominal = self.nominal

        title = self.title

        unit_of_measure = self.unit_of_measure

        abbreviated_uom = self.abbreviated_uom

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_item_id is not UNSET:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if measurement_set_id is not UNSET:
            field_dict["MeasurementSetId"] = measurement_set_id
        if chart_type is not UNSET:
            field_dict["ChartType"] = chart_type
        if chart_image is not UNSET:
            field_dict["ChartImage"] = chart_image
        if nominal is not UNSET:
            field_dict["Nominal"] = nominal
        if title is not UNSET:
            field_dict["Title"] = title
        if unit_of_measure is not UNSET:
            field_dict["UnitOfMeasure"] = unit_of_measure
        if abbreviated_uom is not UNSET:
            field_dict["AbbreviatedUOM"] = abbreviated_uom

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_item_id = d.pop("ServiceOrderItemId", UNSET)

        measurement_set_id = d.pop("MeasurementSetId", UNSET)

        chart_type = d.pop("ChartType", UNSET)

        chart_image = d.pop("ChartImage", UNSET)

        nominal = d.pop("Nominal", UNSET)

        title = d.pop("Title", UNSET)

        unit_of_measure = d.pop("UnitOfMeasure", UNSET)

        abbreviated_uom = d.pop("AbbreviatedUOM", UNSET)

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

        qualer_api_models_report_datasets_to_measurement_chart_response.additional_properties = (
            d
        )
        return qualer_api_models_report_datasets_to_measurement_chart_response

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
