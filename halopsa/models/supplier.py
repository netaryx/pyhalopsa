"""Supplier models."""

from __future__ import annotations

from datetime import datetime as dt

from ._base import HaloModel
from ._common import CustomField


class SupplierList(HaloModel):
    """Abbreviated supplier returned by list endpoints."""

    id: int | None = None
    name: str | None = None
    toplevel_id: int | None = None
    toplevel_name: str | None = None
    contact_name: str | None = None
    email_address: str | None = None
    phone_number: str | None = None
    inactive: bool | None = None


class Supplier(HaloModel):
    """Full supplier detail returned by single-get endpoints."""

    id: int | None = None
    name: str | None = None
    toplevel_id: int | None = None
    toplevel_name: str | None = None
    contact_name: str | None = None
    email_address: str | None = None
    support_email_address: str | None = None
    ordering_email_address: str | None = None
    phone_number: str | None = None
    inactive: bool | None = None
    default_contract_id: int | None = None
    customfields: list[CustomField] | None = None
    contract_count: int | None = None
    datecreated: dt | None = None
    notes: str | None = None
    address: str | None = None
    accounts_id: str | None = None
    portal_url: str | None = None
