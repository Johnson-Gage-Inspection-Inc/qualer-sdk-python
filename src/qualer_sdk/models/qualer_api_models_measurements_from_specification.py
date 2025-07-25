from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsMeasurementsFromSpecification")


@_attrs_define
class QualerApiModelsMeasurementsFromSpecification:
    """
    Attributes:
        title (Union[Unset, str]):
        subtitle (Union[Unset, str]):
        group (Union[Unset, str]):
    """

    title: Union[Unset, str] = UNSET
    subtitle: Union[Unset, str] = UNSET
    group: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        subtitle = self.subtitle

        group = self.group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["Title"] = title
        if subtitle is not UNSET:
            field_dict["Subtitle"] = subtitle
        if group is not UNSET:
            field_dict["Group"] = group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("Title", UNSET)

        subtitle = d.pop("Subtitle", UNSET)

        group = d.pop("Group", UNSET)

        qualer_api_models_measurements_from_specification = cls(
            title=title,
            subtitle=subtitle,
            group=group,
        )

        qualer_api_models_measurements_from_specification.additional_properties = d
        return qualer_api_models_measurements_from_specification

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
