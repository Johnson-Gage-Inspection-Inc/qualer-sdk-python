from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsServiceOrdersFromAppendTrackingNumberModel")


@_attrs_define
class QualerApiModelsServiceOrdersFromAppendTrackingNumberModel:
    """
    Attributes:
        tracking_number (Union[None, Unset, str]):
    """

    tracking_number: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tracking_number = self.tracking_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tracking_number is not UNSET:
            field_dict["TrackingNumber"] = tracking_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tracking_number = d.pop("TrackingNumber", UNSET)

        qualer_api_models_service_orders_from_append_tracking_number_model = cls(
            tracking_number=tracking_number,
        )

        qualer_api_models_service_orders_from_append_tracking_number_model.additional_properties = (
            d
        )
        return qualer_api_models_service_orders_from_append_tracking_number_model

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
