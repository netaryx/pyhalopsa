"""Expense model."""

from __future__ import annotations

from typing import Any

from ._base import HaloModel
from ._common import CustomField


class Expense(HaloModel):
    id: int | None = None
    agent_id: int | None = None
    fault_id: int | None = None
    actionnumber: int | None = None
    description: str | None = None
    amount: float | None = None
    lookup_id: int | None = None
    date_added: str | None = None
    date_reimbursed: str | None = None
    date_invoiced: str | None = None
    invoiceable: bool | None = None
    ihid: int | None = None
    type_name: str | None = None
    client_name: str | None = None
    client_id: int | None = None
    client_to_invoice_to_id: int | None = None
    site_id: int | None = None
    reviewed: bool | None = None
    reviewed_agent_id: int | None = None
    can_review: bool | None = None
    customfields: list[CustomField] | None = None
