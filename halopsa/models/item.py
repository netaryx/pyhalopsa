"""Item (product / stock) models."""

from __future__ import annotations

from ._base import HaloModel
from ._common import CustomField


class Item(HaloModel):
    """Full item detail returned by single-get endpoints."""

    id: int | None = None
    use: str | None = None
    name: str | None = None
    status: str | None = None
    assetgroup_id: int | None = None
    assetgroup_name: str | None = None
    note: str | None = None
    supplier_part_code: str | None = None
    description: str | None = None
    purchase_description: str | None = None
    quantity_in_stock: float | None = None
    quantity_reserved: float | None = None
    quantity_on_order: float | None = None
    baseprice: float | None = None
    supplier_id: int | None = None
    supplier_name: str | None = None
    manufacturer_id: int | None = None
    manufacturer_name: str | None = None
    internalreference: str | None = None
    externalreference: str | None = None
    type: str | None = None
    customfields: list[CustomField] | None = None
    nominal_code_id: int | None = None
    tax_code_id: int | None = None
