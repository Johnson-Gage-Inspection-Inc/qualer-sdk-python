from collections.abc import Mapping
from typing import Any, Dict, List, Optional, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QualerApiModelsReportDatasetsToExternalDataReportResponse")


@_attrs_define
class QualerApiModelsReportDatasetsToExternalDataReportResponse:
    """
    Attributes:
        measurement_set_id (Optional[int]):
        service_order_item_id (Optional[int]):
        row (Optional[int]):
        a (Optional[str]):
        b (Optional[str]):
        c (Optional[str]):
        d (Optional[str]):
        e (Optional[str]):
        f (Optional[str]):
        g (Optional[str]):
        h (Optional[str]):
        i (Optional[str]):
        j (Optional[str]):
        k (Optional[str]):
        l (Optional[str]):
        m (Optional[str]):
        n (Optional[str]):
        o (Optional[str]):
        p (Optional[str]):
        q (Optional[str]):
        r (Optional[str]):
        s (Optional[str]):
        t (Optional[str]):
        u (Optional[str]):
        v (Optional[str]):
        w (Optional[str]):
        x (Optional[str]):
        y (Optional[str]):
        z (Optional[str]):
    """

    measurement_set_id: Optional[int] = None
    service_order_item_id: Optional[int] = None
    row: Optional[int] = None
    a: Optional[str] = None
    b: Optional[str] = None
    c: Optional[str] = None
    d: Optional[str] = None
    e: Optional[str] = None
    f: Optional[str] = None
    g: Optional[str] = None
    h: Optional[str] = None
    i: Optional[str] = None
    j: Optional[str] = None
    k: Optional[str] = None
    l: Optional[str] = None  # noqa: E741
    m: Optional[str] = None
    n: Optional[str] = None
    o: Optional[str] = None
    p: Optional[str] = None
    q: Optional[str] = None
    r: Optional[str] = None
    s: Optional[str] = None
    t: Optional[str] = None
    u: Optional[str] = None
    v: Optional[str] = None
    w: Optional[str] = None
    x: Optional[str] = None
    y: Optional[str] = None
    z: Optional[str] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if self.measurement_set_id is not None:
            field_dict["MeasurementSetId"] = self.measurement_set_id
        if self.service_order_item_id is not None:
            field_dict["ServiceOrderItemId"] = self.service_order_item_id
        if self.row is not None:
            field_dict["Row"] = self.row

        # Map single-letter fields dynamically to avoid E741 on variable names
        for letter in "abcdefghijklmnopqrstuvwxyz":
            value = getattr(self, letter)
            if value is not None:
                field_dict[letter.upper()] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        data = dict(src_dict)

        kwargs: Dict[str, Any] = {}
        kwargs["measurement_set_id"] = data.pop("MeasurementSetId", None)
        kwargs["service_order_item_id"] = data.pop("ServiceOrderItemId", None)
        kwargs["row"] = data.pop("Row", None)

        # Extract A..Z into a..z
        for letter in "abcdefghijklmnopqrstuvwxyz":
            kwargs[letter] = data.pop(letter.upper(), None)

        obj = cls(**kwargs)
        obj.additional_properties = data
        return obj

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
