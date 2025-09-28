from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EmployeesFromEmployeeLocationModel")


@_attrs_define
class EmployeesFromEmployeeLocationModel:
    """
    Attributes:
        latitude (Optional[float]):
        longitude (Optional[float]):
        accuracy (Optional[float]):
        altitude (Optional[float]):
        altitude_accuracy (Optional[float]):
        heading (Optional[float]):
        speed (Optional[float]):
        timestamp (Optional[int]):
    """

    latitude: Optional[float] = None
    longitude: Optional[float] = None
    accuracy: Optional[float] = None
    altitude: Optional[float] = None
    altitude_accuracy: Optional[float] = None
    heading: Optional[float] = None
    speed: Optional[float] = None
    timestamp: Optional[int] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        latitude = self.latitude
        longitude = self.longitude
        accuracy = self.accuracy
        altitude = self.altitude
        altitude_accuracy = self.altitude_accuracy
        heading = self.heading
        speed = self.speed
        timestamp = self.timestamp
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latitude is not None:
            field_dict["Latitude"] = latitude
        if longitude is not None:
            field_dict["Longitude"] = longitude
        if accuracy is not None:
            field_dict["Accuracy"] = accuracy
        if altitude is not None:
            field_dict["Altitude"] = altitude
        if altitude_accuracy is not None:
            field_dict["AltitudeAccuracy"] = altitude_accuracy
        if heading is not None:
            field_dict["Heading"] = heading
        if speed is not None:
            field_dict["Speed"] = speed
        if timestamp is not None:
            field_dict["Timestamp"] = timestamp
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        latitude = d.pop("Latitude", None)
        longitude = d.pop("Longitude", None)
        accuracy = d.pop("Accuracy", None)
        altitude = d.pop("Altitude", None)
        altitude_accuracy = d.pop("AltitudeAccuracy", None)
        heading = d.pop("Heading", None)
        speed = d.pop("Speed", None)
        timestamp = d.pop("Timestamp", None)
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
        qualer_api_models_employees_from_employee_location_model.additional_properties = d
        return qualer_api_models_employees_from_employee_location_model

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
