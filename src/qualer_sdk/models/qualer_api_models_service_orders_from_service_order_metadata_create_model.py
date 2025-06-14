from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualer_core_shared_models_service_order_metadata_service_order_metadata_exhibits import (
        QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits,
    )


T = TypeVar(
    "T", bound="QualerApiModelsServiceOrdersFromServiceOrderMetadataCreateModel"
)


@_attrs_define
class QualerApiModelsServiceOrdersFromServiceOrderMetadataCreateModel:
    """
    Attributes:
        metadata (Union[Unset, str]):
        exhibits (Union[Unset, QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits]):
    """

    metadata: Union[Unset, str] = UNSET
    exhibits: Union[
        Unset, "QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits"
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata = self.metadata

        exhibits: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.exhibits, Unset):
            exhibits = self.exhibits.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metadata is not UNSET:
            field_dict["Metadata"] = metadata
        if exhibits is not UNSET:
            field_dict["Exhibits"] = exhibits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_core_shared_models_service_order_metadata_service_order_metadata_exhibits import (
            QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits,
        )

        d = dict(src_dict)
        metadata = d.pop("Metadata", UNSET)

        _exhibits = d.pop("Exhibits", UNSET)
        exhibits: Union[
            Unset,
            QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits,
        ]
        if isinstance(_exhibits, Unset):
            exhibits = UNSET
        else:
            exhibits = QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits.from_dict(
                _exhibits
            )

        qualer_api_models_service_orders_from_service_order_metadata_create_model = cls(
            metadata=metadata,
            exhibits=exhibits,
        )

        qualer_api_models_service_orders_from_service_order_metadata_create_model.additional_properties = (
            d
        )
        return qualer_api_models_service_orders_from_service_order_metadata_create_model

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
