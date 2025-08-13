from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsEmployeesFromEmployeeLocationModel")


@_attrs_define
class QualerApiModelsEmployeesFromEmployeeLocationModel:
    """
    Attributes:
        latitude (Union[None, Unset, float]):
        longitude (Union[None, Unset, float]):
        accuracy (Union[None, Unset, float]):
        altitude (Union[None, Unset, float]):
        altitude_accuracy (Union[None, Unset, float]):
        heading (Union[None, Unset, float]):
        speed (Union[None, Unset, float]):
        timestamp (Union[None, Unset, int]):
    """

    latitude: Union[None, Unset, float] = UNSET
    longitude: Union[None, Unset, float] = UNSET
    accuracy: Union[None, Unset, float] = UNSET
    altitude: Union[None, Unset, float] = UNSET
    altitude_accuracy: Union[None, Unset, float] = UNSET
    heading: Union[None, Unset, float] = UNSET
    speed: Union[None, Unset, float] = UNSET
    timestamp: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latitude = self.latitude

        longitude = self.longitude

        accuracy = self.accuracy

        altitude = self.altitude

        altitude_accuracy = self.altitude_accuracy

        heading = self.heading

        speed = self.speed

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if accuracy is not UNSET:
            field_dict["Accuracy"] = accuracy
        if altitude is not UNSET:
            field_dict["Altitude"] = altitude
        if altitude_accuracy is not UNSET:
            field_dict["AltitudeAccuracy"] = altitude_accuracy
        if heading is not UNSET:
            field_dict["Heading"] = heading
        if speed is not UNSET:
            field_dict["Speed"] = speed
        if timestamp is not UNSET:
            field_dict["Timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        latitude = d.pop("Latitude", UNSET)

        longitude = d.pop("Longitude", UNSET)

        accuracy = d.pop("Accuracy", UNSET)

        altitude = d.pop("Altitude", UNSET)

        altitude_accuracy = d.pop("AltitudeAccuracy", UNSET)

        heading = d.pop("Heading", UNSET)

        speed = d.pop("Speed", UNSET)

        timestamp = d.pop("Timestamp", UNSET)

        qualer_api_models_employees_from_employee_location_model = cls(
            latitude=latitude,
            longitude=longitude,
            accuracy=accuracy,
            altitude=altitude,
            altitude_accuracy=altitude_accuracy,
            heading=heading,
            speed=speed,
            timestamp=timestamp,
        )

        qualer_api_models_employees_from_employee_location_model.additional_properties = (
            d
        )
        return qualer_api_models_employees_from_employee_location_model

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
