from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsReportDatasetsToOrderItemImageResponse")


@_attrs_define
class QualerApiModelsReportDatasetsToOrderItemImageResponse:
    """
    Attributes:
        service_order_item_id (Union[Unset, int]):
        image (Union[Unset, str]):
        image_url (Union[Unset, str]):
    """

    service_order_item_id: Union[Unset, int] = UNSET
    image: Union[Unset, str] = UNSET
    image_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_order_item_id = self.service_order_item_id

        image = self.image

        image_url = self.image_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_item_id is not UNSET:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if image is not UNSET:
            field_dict["Image"] = image
        if image_url is not UNSET:
            field_dict["ImageUrl"] = image_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_order_item_id = d.pop("ServiceOrderItemId", UNSET)

        image = d.pop("Image", UNSET)

        image_url = d.pop("ImageUrl", UNSET)

        qualer_api_models_report_datasets_to_order_item_image_response = cls(
            service_order_item_id=service_order_item_id,
            image=image,
            image_url=image_url,
        )

        qualer_api_models_report_datasets_to_order_item_image_response.additional_properties = (
            d
        )
        return qualer_api_models_report_datasets_to_order_item_image_response

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
