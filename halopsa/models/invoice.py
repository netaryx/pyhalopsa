"""Invoice (InvoiceHeader) model."""

from __future__ import annotations

from datetime import datetime as dt

from ._base import HaloModel
from ._common import CustomField


class Invoice(HaloModel):
    """Full invoice detail."""

    id: int | None = None
    use: str | None = None
    client_id: int | None = None
    client_name: str | None = None
    invoicenumber: str | None = None
    posted: bool | None = None
    name: str | None = None
    address1: str | None = None
    address2: str | None = None
    address3: str | None = None
    address4: str | None = None
    address5: str | None = None
    contactname: str | None = None
    invoice_date: dt | None = None
    schedule_date: dt | None = None
    dateposted: dt | None = None
    total: float | None = None
    subtotal: float | None = None
    tax_total: float | None = None
    payment_status: str | None = None
    note: str | None = None
    contract_id: int | None = None
    currency_code: str | None = None
    customfields: list[CustomField] | None = None
