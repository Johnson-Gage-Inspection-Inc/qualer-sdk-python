from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.qualer_core_shared_models_service_order_metadata_service_order_metadata_exhibits import (
        QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits,
    )


T = TypeVar("T", bound="ServiceOrdersFromServiceOrderMetadataUpdateModel")


@_attrs_define
class ServiceOrdersFromServiceOrderMetadataUpdateModel:
    """
    Attributes:
        service_order_metadata_id (Optional[int]):
        metadata (Optional[str]):
        exhibits (Optional[QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits]):
    """

    service_order_metadata_id: Optional[int] = None
    metadata: Optional[str] = None
    exhibits: Optional["QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits"] = (
        None
    )
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_order_metadata_id = self.service_order_metadata_id
        metadata = self.metadata
        exhibits: Optional[Dict[str, Any]] = None
        if self.exhibits:
            exhibits = self.exhibits.to_dict()
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_order_metadata_id is not None:
            field_dict["ServiceOrderMetadataId"] = service_order_metadata_id
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
        service_order_metadata_id = d.pop("ServiceOrderMetadataId", None)
        metadata = d.pop("Metadata", None)
        _exhibits = d.pop("Exhibits", None)
        exhibits: Optional[QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits]
        if not _exhibits:
            exhibits = None
        else:
            exhibits = (
                QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits.from_dict(
                    _exhibits
                )
            )
        qualer_api_models_service_orders_from_service_order_metadata_update_model = cls(
            service_order_metadata_id=service_order_metadata_id,
            metadata=metadata,
            exhibits=exhibits,
        )
        qualer_api_models_service_orders_from_service_order_metadata_update_model.additional_properties = (
            d
        )
        return qualer_api_models_service_orders_from_service_order_metadata_update_model

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
