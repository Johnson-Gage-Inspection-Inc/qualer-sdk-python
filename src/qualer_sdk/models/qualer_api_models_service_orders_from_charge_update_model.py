from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualer_api_models_service_orders_from_charge_update_model_price_model import (
        QualerApiModelsServiceOrdersFromChargeUpdateModelPriceModel,
    )


T = TypeVar("T", bound="QualerApiModelsServiceOrdersFromChargeUpdateModel")


@_attrs_define
class QualerApiModelsServiceOrdersFromChargeUpdateModel:
    """
    Attributes:
        charges (Union[Unset, list['QualerApiModelsServiceOrdersFromChargeUpdateModelPriceModel']]):
    """

    charges: Union[
        Unset, list["QualerApiModelsServiceOrdersFromChargeUpdateModelPriceModel"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charges: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.charges, Unset):
            charges = []
            for charges_item_data in self.charges:
                charges_item = charges_item_data.to_dict()
                charges.append(charges_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if charges is not UNSET:
            field_dict["Charges"] = charges

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualer_api_models_service_orders_from_charge_update_model_price_model import (
            QualerApiModelsServiceOrdersFromChargeUpdateModelPriceModel,
        )

        d = dict(src_dict)
        charges = []
        _charges = d.pop("Charges", UNSET)
        for charges_item_data in _charges or []:
            charges_item = (
                QualerApiModelsServiceOrdersFromChargeUpdateModelPriceModel.from_dict(
                    charges_item_data
                )
            )

            charges.append(charges_item)

        qualer_api_models_service_orders_from_charge_update_model = cls(
            charges=charges,
        )

        qualer_api_models_service_orders_from_charge_update_model.additional_properties = (
            d
        )
        return qualer_api_models_service_orders_from_charge_update_model

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
