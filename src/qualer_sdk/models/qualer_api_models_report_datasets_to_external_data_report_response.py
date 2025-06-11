from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualerApiModelsReportDatasetsToExternalDataReportResponse")


@_attrs_define
class QualerApiModelsReportDatasetsToExternalDataReportResponse:
    """
    Attributes:
        measurement_set_id (Union[Unset, int]):
        service_order_item_id (Union[Unset, int]):
        row (Union[Unset, int]):
        a (Union[Unset, str]):
        b (Union[Unset, str]):
        c (Union[Unset, str]):
        d (Union[Unset, str]):
        e (Union[Unset, str]):
        f (Union[Unset, str]):
        g (Union[Unset, str]):
        h (Union[Unset, str]):
        i (Union[Unset, str]):
        j (Union[Unset, str]):
        k (Union[Unset, str]):
        l (Union[Unset, str]):
        m (Union[Unset, str]):
        n (Union[Unset, str]):
        o (Union[Unset, str]):
        p (Union[Unset, str]):
        q (Union[Unset, str]):
        r (Union[Unset, str]):
        s (Union[Unset, str]):
        t (Union[Unset, str]):
        u (Union[Unset, str]):
        v (Union[Unset, str]):
        w (Union[Unset, str]):
        x (Union[Unset, str]):
        y (Union[Unset, str]):
        z (Union[Unset, str]):
    """

    measurement_set_id: Union[Unset, int] = UNSET
    service_order_item_id: Union[Unset, int] = UNSET
    row: Union[Unset, int] = UNSET
    a: Union[Unset, str] = UNSET
    b: Union[Unset, str] = UNSET
    c: Union[Unset, str] = UNSET
    d: Union[Unset, str] = UNSET
    e: Union[Unset, str] = UNSET
    f: Union[Unset, str] = UNSET
    g: Union[Unset, str] = UNSET
    h: Union[Unset, str] = UNSET
    i: Union[Unset, str] = UNSET
    j: Union[Unset, str] = UNSET
    k: Union[Unset, str] = UNSET
    l: Union[Unset, str] = UNSET
    m: Union[Unset, str] = UNSET
    n: Union[Unset, str] = UNSET
    o: Union[Unset, str] = UNSET
    p: Union[Unset, str] = UNSET
    q: Union[Unset, str] = UNSET
    r: Union[Unset, str] = UNSET
    s: Union[Unset, str] = UNSET
    t: Union[Unset, str] = UNSET
    u: Union[Unset, str] = UNSET
    v: Union[Unset, str] = UNSET
    w: Union[Unset, str] = UNSET
    x: Union[Unset, str] = UNSET
    y: Union[Unset, str] = UNSET
    z: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measurement_set_id = self.measurement_set_id

        service_order_item_id = self.service_order_item_id

        row = self.row

        a = self.a

        b = self.b

        c = self.c

        d = self.d

        e = self.e

        f = self.f

        g = self.g

        h = self.h

        i = self.i

        j = self.j

        k = self.k

        l = self.l

        m = self.m

        n = self.n

        o = self.o

        p = self.p

        q = self.q

        r = self.r

        s = self.s

        t = self.t

        u = self.u

        v = self.v

        w = self.w

        x = self.x

        y = self.y

        z = self.z

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measurement_set_id is not UNSET:
            field_dict["MeasurementSetId"] = measurement_set_id
        if service_order_item_id is not UNSET:
            field_dict["ServiceOrderItemId"] = service_order_item_id
        if row is not UNSET:
            field_dict["Row"] = row
        if a is not UNSET:
            field_dict["A"] = a
        if b is not UNSET:
            field_dict["B"] = b
        if c is not UNSET:
            field_dict["C"] = c
        if d is not UNSET:
            field_dict["D"] = d
        if e is not UNSET:
            field_dict["E"] = e
        if f is not UNSET:
            field_dict["F"] = f
        if g is not UNSET:
            field_dict["G"] = g
        if h is not UNSET:
            field_dict["H"] = h
        if i is not UNSET:
            field_dict["I"] = i
        if j is not UNSET:
            field_dict["J"] = j
        if k is not UNSET:
            field_dict["K"] = k
        if l is not UNSET:
            field_dict["L"] = l
        if m is not UNSET:
            field_dict["M"] = m
        if n is not UNSET:
            field_dict["N"] = n
        if o is not UNSET:
            field_dict["O"] = o
        if p is not UNSET:
            field_dict["P"] = p
        if q is not UNSET:
            field_dict["Q"] = q
        if r is not UNSET:
            field_dict["R"] = r
        if s is not UNSET:
            field_dict["S"] = s
        if t is not UNSET:
            field_dict["T"] = t
        if u is not UNSET:
            field_dict["U"] = u
        if v is not UNSET:
            field_dict["V"] = v
        if w is not UNSET:
            field_dict["W"] = w
        if x is not UNSET:
            field_dict["X"] = x
        if y is not UNSET:
            field_dict["Y"] = y
        if z is not UNSET:
            field_dict["Z"] = z

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        measurement_set_id = d.pop("MeasurementSetId", UNSET)

        service_order_item_id = d.pop("ServiceOrderItemId", UNSET)

        row = d.pop("Row", UNSET)

        a = d.pop("A", UNSET)

        b = d.pop("B", UNSET)

        c = d.pop("C", UNSET)

        d = d.pop("D", UNSET)

        e = d.pop("E", UNSET)

        f = d.pop("F", UNSET)

        g = d.pop("G", UNSET)

        h = d.pop("H", UNSET)

        i = d.pop("I", UNSET)

        j = d.pop("J", UNSET)

        k = d.pop("K", UNSET)

        l = d.pop("L", UNSET)

        m = d.pop("M", UNSET)

        n = d.pop("N", UNSET)

        o = d.pop("O", UNSET)

        p = d.pop("P", UNSET)

        q = d.pop("Q", UNSET)

        r = d.pop("R", UNSET)

        s = d.pop("S", UNSET)

        t = d.pop("T", UNSET)

        u = d.pop("U", UNSET)

        v = d.pop("V", UNSET)

        w = d.pop("W", UNSET)

        x = d.pop("X", UNSET)

        y = d.pop("Y", UNSET)

        z = d.pop("Z", UNSET)

        qualer_api_models_report_datasets_to_external_data_report_response = cls(
            measurement_set_id=measurement_set_id,
            service_order_item_id=service_order_item_id,
            row=row,
            a=a,
            b=b,
            c=c,
            d=d,
            e=e,
            f=f,
            g=g,
            h=h,
            i=i,
            j=j,
            k=k,
            l=l,
            m=m,
            n=n,
            o=o,
            p=p,
            q=q,
            r=r,
            s=s,
            t=t,
            u=u,
            v=v,
            w=w,
            x=x,
            y=y,
            z=z,
        )

        qualer_api_models_report_datasets_to_external_data_report_response.additional_properties = (
            d
        )
        return qualer_api_models_report_datasets_to_external_data_report_response

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
