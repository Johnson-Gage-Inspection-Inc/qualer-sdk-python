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
        measurement_set_id (Union[None, Unset, int]):
        service_order_item_id (Union[None, Unset, int]):
        row (Union[None, Unset, int]):
        a (Union[None, Unset, str]):
        b (Union[None, Unset, str]):
        c (Union[None, Unset, str]):
        d (Union[None, Unset, str]):
        e (Union[None, Unset, str]):
        f (Union[None, Unset, str]):
        g (Union[None, Unset, str]):
        h (Union[None, Unset, str]):
        i (Union[None, Unset, str]):
        j (Union[None, Unset, str]):
        k (Union[None, Unset, str]):
        l (Union[None, Unset, str]):
        m (Union[None, Unset, str]):
        n (Union[None, Unset, str]):
        o (Union[None, Unset, str]):
        p (Union[None, Unset, str]):
        q (Union[None, Unset, str]):
        r (Union[None, Unset, str]):
        s (Union[None, Unset, str]):
        t (Union[None, Unset, str]):
        u (Union[None, Unset, str]):
        v (Union[None, Unset, str]):
        w (Union[None, Unset, str]):
        x (Union[None, Unset, str]):
        y (Union[None, Unset, str]):
        z (Union[None, Unset, str]):
    """

    measurement_set_id: Union[None, Unset, int] = UNSET
    service_order_item_id: Union[None, Unset, int] = UNSET
    row: Union[None, Unset, int] = UNSET
    a: Union[None, Unset, str] = UNSET
    b: Union[None, Unset, str] = UNSET
    c: Union[None, Unset, str] = UNSET
    d: Union[None, Unset, str] = UNSET
    e: Union[None, Unset, str] = UNSET
    f: Union[None, Unset, str] = UNSET
    g: Union[None, Unset, str] = UNSET
    h: Union[None, Unset, str] = UNSET
    i: Union[None, Unset, str] = UNSET
    j: Union[None, Unset, str] = UNSET
    k: Union[None, Unset, str] = UNSET
    l: Union[None, Unset, str] = UNSET
    m: Union[None, Unset, str] = UNSET
    n: Union[None, Unset, str] = UNSET
    o: Union[None, Unset, str] = UNSET
    p: Union[None, Unset, str] = UNSET
    q: Union[None, Unset, str] = UNSET
    r: Union[None, Unset, str] = UNSET
    s: Union[None, Unset, str] = UNSET
    t: Union[None, Unset, str] = UNSET
    u: Union[None, Unset, str] = UNSET
    v: Union[None, Unset, str] = UNSET
    w: Union[None, Unset, str] = UNSET
    x: Union[None, Unset, str] = UNSET
    y: Union[None, Unset, str] = UNSET
    z: Union[None, Unset, str] = UNSET
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
