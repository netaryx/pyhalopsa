"""Asset (Device / inventory item) models."""

from __future__ import annotations

from datetime import datetime as dt

from ._base import HaloModel
from ._common import CustomField


class AssetList(HaloModel):
    """Abbreviated asset returned by list endpoints."""

    id: int | None = None
    inventory_number: str | None = None
    key_field: str | None = None
    key_field2: str | None = None
    key_field3: str | None = None
    client_id: int | None = None
    client_name: str | None = None
    site_id: int | None = None
    site_name: str | None = None
    username: str | None = None
    assettype_id: int | None = None
    assettype_name: str | None = None
    status: str | None = None
    devicename: str | None = None
    serialnumber: str | None = None


class Asset(HaloModel):
    """Full asset / device detail."""

    id: int | None = None
    inventory_number: str | None = None
    key_field: str | None = None
    key_field2: str | None = None
    key_field3: str | None = None
    client_id: int | None = None
    client_name: str | None = None
    site_id: int | None = None
    site_name: str | None = None
    username: str | None = None
    assettype_id: int | None = None
    assettype_name: str | None = None
    colour: str | None = None
    icon: str | None = None
    warranty_end: dt | None = None
    status: str | None = None
    contract_id: int | None = None
    supplier_id: int | None = None
    supplier_name: str | None = None
    purchase_price: float | None = None
    purchase_date: dt | None = None
    notes: str | None = None
    serialnumber: str | None = None
    assettag: str | None = None
    devicename: str | None = None
    customfields: list[CustomField] | None = None
