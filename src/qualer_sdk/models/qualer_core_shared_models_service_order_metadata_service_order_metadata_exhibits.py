from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualer_core_shared_models_service_order_metadata_service_order_metadata_exhibits_key_value import (
        QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibitsKeyValue,
    )


T = TypeVar(
    "T", bound="QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits"
)


@_attrs_define
class QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits:
    """
    Attributes:
        title (Union[None, Unset, str]):
        subtitle (Union[None, Unset, str]):
        exhibits (Union[None, Unset, list['QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibitsKeyValue']]):
    """

    title: Union[None, Unset, str] = UNSET
    subtitle: Union[None, Unset, str] = UNSET
    exhibits: Union[None, Unset,
        list[
            "QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibitsKeyValue"
        ],
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        subtitle = self.subtitle

        exhibits: Union[None, Unset, list[dict[str, Any]]] = UNSET
        if self.exhibits and not isinstance(self.exhibits, Unset):
            exhibits = []
            for exhibits_item_data in self.exhibits:
                exhibits_item = exhibits_item_data.to_dict()
                exhibits.append(exhibits_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["Title"] = title
        if subtitle is not UNSET:
            field_dict["Subtitle"] = subtitle
        if exhibits is not UNSET:
            field_dict["Exhibits"] = exhibits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_core_shared_models_service_order_metadata_service_order_metadata_exhibits_key_value import (
            QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibitsKeyValue,
        )

        d = dict(src_dict)
        title = d.pop("Title", UNSET)

        subtitle = d.pop("Subtitle", UNSET)

        exhibits = []
        _exhibits = d.pop("Exhibits", UNSET)
        for exhibits_item_data in _exhibits or []:
            exhibits_item = QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibitsKeyValue.from_dict(
                exhibits_item_data
            )

            exhibits.append(exhibits_item)

        qualer_core_shared_models_service_order_metadata_service_order_metadata_exhibits = cls(
            title=title,
            subtitle=subtitle,
            exhibits=exhibits,
        )

        qualer_core_shared_models_service_order_metadata_service_order_metadata_exhibits.additional_properties = (
            d
        )
        return qualer_core_shared_models_service_order_metadata_service_order_metadata_exhibits

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
