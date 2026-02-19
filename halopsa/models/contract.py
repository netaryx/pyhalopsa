"""Contract models."""

from __future__ import annotations

from datetime import datetime as dt

from ._base import HaloModel
from ._common import CustomField


class ContractList(HaloModel):
    """Abbreviated contract returned by list endpoints."""

    id: int | None = None
    client_id: int | None = None
    client_name: str | None = None
    ref: str | None = None
    start_date: dt | None = None
    end_date: dt | None = None
    started: bool | None = None
    expired: bool | None = None
    billingperiod: str | None = None
    subtype: str | None = None
    status: str | None = None
    site_id: int | None = None
    site_name: str | None = None
    contract_status: str | None = None


class Contract(HaloModel):
    """Full contract detail returned by single-get endpoints."""

    id: int | None = None
    client_id: int | None = None
    client_name: str | None = None
    ref: str | None = None
    refextra: str | None = None
    start_date: dt | None = None
    end_date: dt | None = None
    started: bool | None = None
    expired: bool | None = None
    billingperiod: str | None = None
    billingdescription: str | None = None
    subtype: str | None = None
    status: str | None = None
    site_id: int | None = None
    site_name: str | None = None
    user_id: int | None = None
    user_name: str | None = None
    sla_id: int | None = None
    next_invoice_date: dt | None = None
    periodchargeamount: float | None = None
    note: str | None = None
    contract_status: str | None = None
    customfields: list[CustomField] | None = None
