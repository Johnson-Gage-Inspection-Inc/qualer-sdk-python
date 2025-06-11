from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualer_api_models_measurements_from_create_measurement_point_model import (
        QualerApiModelsMeasurementsFromCreateMeasurementPointModel,
    )
    from ..models.qualer_api_models_measurements_from_custom_fields import (
        QualerApiModelsMeasurementsFromCustomFields,
    )
    from ..models.qualer_api_models_measurements_from_display_options import (
        QualerApiModelsMeasurementsFromDisplayOptions,
    )


T = TypeVar("T", bound="QualerApiModelsMeasurementsFromCreateMeasurementSetModel")


@_attrs_define
class QualerApiModelsMeasurementsFromCreateMeasurementSetModel:
    """
    Attributes:
        measurement_name (Union[Unset, str]):
        is_accredited (Union[Unset, bool]):
        measurement_quantity_id (Union[Unset, int]):
        default_unit_of_measure_id (Union[Unset, int]):
        decimal_places (Union[Unset, int]):
        significant_figures (Union[Unset, int]):
        display_options (Union[Unset, QualerApiModelsMeasurementsFromDisplayOptions]):
        custom_fields (Union[Unset, QualerApiModelsMeasurementsFromCustomFields]):
        measurement_points (Union[Unset, list['QualerApiModelsMeasurementsFromCreateMeasurementPointModel']]):
    """

    measurement_name: Union[Unset, str] = UNSET
    is_accredited: Union[Unset, bool] = UNSET
    measurement_quantity_id: Union[Unset, int] = UNSET
    default_unit_of_measure_id: Union[Unset, int] = UNSET
    decimal_places: Union[Unset, int] = UNSET
    significant_figures: Union[Unset, int] = UNSET
    display_options: Union[Unset, "QualerApiModelsMeasurementsFromDisplayOptions"] = (
        UNSET
    )
    custom_fields: Union[Unset, "QualerApiModelsMeasurementsFromCustomFields"] = UNSET
    measurement_points: Union[
        Unset, list["QualerApiModelsMeasurementsFromCreateMeasurementPointModel"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measurement_name = self.measurement_name

        is_accredited = self.is_accredited

        measurement_quantity_id = self.measurement_quantity_id

        default_unit_of_measure_id = self.default_unit_of_measure_id

        decimal_places = self.decimal_places

        significant_figures = self.significant_figures

        display_options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.display_options, Unset):
            display_options = self.display_options.to_dict()

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        measurement_points: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.measurement_points, Unset):
            measurement_points = []
            for measurement_points_item_data in self.measurement_points:
                measurement_points_item = measurement_points_item_data.to_dict()
                measurement_points.append(measurement_points_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measurement_name is not UNSET:
            field_dict["MeasurementName"] = measurement_name
        if is_accredited is not UNSET:
            field_dict["IsAccredited"] = is_accredited
        if measurement_quantity_id is not UNSET:
            field_dict["MeasurementQuantityId"] = measurement_quantity_id
        if default_unit_of_measure_id is not UNSET:
            field_dict["DefaultUnitOfMeasureId"] = default_unit_of_measure_id
        if decimal_places is not UNSET:
            field_dict["DecimalPlaces"] = decimal_places
        if significant_figures is not UNSET:
            field_dict["SignificantFigures"] = significant_figures
        if display_options is not UNSET:
            field_dict["DisplayOptions"] = display_options
        if custom_fields is not UNSET:
            field_dict["CustomFields"] = custom_fields
        if measurement_points is not UNSET:
            field_dict["MeasurementPoints"] = measurement_points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_measurements_from_create_measurement_point_model import (
            QualerApiModelsMeasurementsFromCreateMeasurementPointModel,
        )
        from ..models.qualer_api_models_measurements_from_custom_fields import (
            QualerApiModelsMeasurementsFromCustomFields,
        )
        from ..models.qualer_api_models_measurements_from_display_options import (
            QualerApiModelsMeasurementsFromDisplayOptions,
        )

        d = dict(src_dict)
        measurement_name = d.pop("MeasurementName", UNSET)

        is_accredited = d.pop("IsAccredited", UNSET)

        measurement_quantity_id = d.pop("MeasurementQuantityId", UNSET)

        default_unit_of_measure_id = d.pop("DefaultUnitOfMeasureId", UNSET)

        decimal_places = d.pop("DecimalPlaces", UNSET)

        significant_figures = d.pop("SignificantFigures", UNSET)

        _display_options = d.pop("DisplayOptions", UNSET)
        display_options: Union[Unset, QualerApiModelsMeasurementsFromDisplayOptions]
        if isinstance(_display_options, Unset):
            display_options = UNSET
        else:
            display_options = QualerApiModelsMeasurementsFromDisplayOptions.from_dict(
                _display_options
            )

        _custom_fields = d.pop("CustomFields", UNSET)
        custom_fields: Union[Unset, QualerApiModelsMeasurementsFromCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = QualerApiModelsMeasurementsFromCustomFields.from_dict(
                _custom_fields
            )

        measurement_points = []
        _measurement_points = d.pop("MeasurementPoints", UNSET)
        for measurement_points_item_data in _measurement_points or []:
            measurement_points_item = (
                QualerApiModelsMeasurementsFromCreateMeasurementPointModel.from_dict(
                    measurement_points_item_data
                )
            )

            measurement_points.append(measurement_points_item)

        qualer_api_models_measurements_from_create_measurement_set_model = cls(
            measurement_name=measurement_name,
            is_accredited=is_accredited,
            measurement_quantity_id=measurement_quantity_id,
            default_unit_of_measure_id=default_unit_of_measure_id,
            decimal_places=decimal_places,
            significant_figures=significant_figures,
            display_options=display_options,
            custom_fields=custom_fields,
            measurement_points=measurement_points,
        )

        qualer_api_models_measurements_from_create_measurement_set_model.additional_properties = (
            d
        )
        return qualer_api_models_measurements_from_create_measurement_set_model

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
