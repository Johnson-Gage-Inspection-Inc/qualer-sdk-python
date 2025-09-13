from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.qualer_core_shared_models_service_order_metadata_service_order_metadata_exhibits import (
        QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits,
    )


T = TypeVar("T", bound="ServiceOrdersFromServiceOrderMetadataCreateModel")


@_attrs_define
class ServiceOrdersFromServiceOrderMetadataCreateModel:
    """
    Attributes:
        metadata (Optional[str]):
        exhibits (Optional[QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits]):
    """

    metadata: Optional[str] = None
    exhibits: Union[
        None,
        None,
        "QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits",
    ] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metadata = self.metadata

        exhibits: Optional[Dict[str, Any]] = None
        if self.exhibits:
            exhibits = self.exhibits.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metadata is not None:
            field_dict["Metadata"] = metadata
        if exhibits is not None:
            field_dict["Exhibits"] = exhibits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_core_shared_models_service_order_metadata_service_order_metadata_exhibits import (
            QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits,
        )

        d = dict(src_dict)
        metadata = d.pop("Metadata", None)

        _exhibits = d.pop("Exhibits", None)
        exhibits: Union[
            None,
            None,
            QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits,
        ]
        if not _exhibits:
            exhibits = None
        else:
            exhibits = (
                QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits.from_dict(
                    _exhibits
                )
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
