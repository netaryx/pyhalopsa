"""SoftwareLicence model."""

from __future__ import annotations

from ._base import HaloModel


class SoftwareLicence(HaloModel):
    id: int | None = None
    type: int | None = None
    name: str | None = None
    count: int | None = None
    consumedcount: int | None = None
    client_id: int | None = None
    site_id: int | None = None
    client_name: str | None = None
    site_name: str | None = None
    purchase_price: float | None = None
    recurring_price: float | None = None
    supplier_id: int | None = None
    supplier_name: str | None = None
    key: str | None = None
    notes: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    inactive: bool | None = None
