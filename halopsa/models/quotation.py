"""Quotation model."""

from __future__ import annotations

from typing import Any

from ._base import HaloModel
from ._common import CustomField


class Quotation(HaloModel):
    id: int | None = None
    use: str | None = None
    table: str | None = None
    title: str | None = None
    ticket_id: int | None = None
    status: int | None = None
    po_ref: str | None = None
    date: str | None = None
    expiry_date: str | None = None
    total: float | None = None
    carriage_desc: str | None = None
    carriage_price: float | None = None
    tax_total_estimate: float | None = None
    auth_by: str | None = None
    note: str | None = None
    user_id: int | None = None
    user_name: str | None = None
    site_id: int | None = None
    site_name: str | None = None
    client_id: int | None = None
    client_name: str | None = None
    scope: str | None = None
    risk: str | None = None
    agent_id: int | None = None
    assigned_agent_name: str | None = None
    customfields: list[CustomField] | None = None
    lines: list[Any] | None = None
