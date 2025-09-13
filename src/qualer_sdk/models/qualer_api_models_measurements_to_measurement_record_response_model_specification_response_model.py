from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T",
    bound="MeasurementsToMeasurementRecordResponseModelSpecificationResponseModel",
)


@_attrs_define
class MeasurementsToMeasurementRecordResponseModelSpecificationResponseModel:
    """
    Attributes:
        title (Optional[str]):
        subtitle (Optional[str]):
        group (Optional[str]):
    """

    title: Optional[str] = None
    subtitle: Optional[str] = None
    group: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title

        subtitle = self.subtitle

        group = self.group

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not None:
            field_dict["Title"] = title
        if subtitle is not None:
            field_dict["Subtitle"] = subtitle
        if group is not None:
            field_dict["Group"] = group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("Title", None)

        subtitle = d.pop("Subtitle", None)

        group = d.pop("Group", None)

        qualer_api_models_measurements_to_measurement_record_response_model_specification_response_model = cls(
            title=title,
            subtitle=subtitle,
            group=group,
        )

        qualer_api_models_measurements_to_measurement_record_response_model_specification_response_model.additional_properties = (
            d
        )
        return qualer_api_models_measurements_to_measurement_record_response_model_specification_response_model

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
