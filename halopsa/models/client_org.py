"""Client / Organisation (Area) models."""

from __future__ import annotations

from ._base import HaloModel
from ._common import CustomField


class ClientOrgList(HaloModel):
    """Abbreviated client returned by list endpoints."""

    id: int | None = None
    name: str | None = None
    toplevel_id: int | None = None
    toplevel_name: str | None = None
    inactive: bool | None = None
    colour: str | None = None
    main_site_id: int | None = None
    sla_id: int | None = None
    website: str | None = None
    phone_number: str | None = None
    email_address: str | None = None
    ticket_count: int | None = None
    contract_count: int | None = None


class ClientOrg(HaloModel):
    """Full client / organisation detail."""

    id: int | None = None
    name: str | None = None
    toplevel_id: int | None = None
    toplevel_name: str | None = None
    inactive: bool | None = None
    colour: str | None = None
    messagegroup_id: int | None = None
    main_site_id: int | None = None
    sla_id: int | None = None
    client_to_invoice: int | None = None
    ticket_invoices_to_site: bool | None = None
    override_org_name: str | None = None
    override_org_email: str | None = None
    override_org_phone: str | None = None
    override_org_website: str | None = None
    item_tax_code: str | None = None
    service_tax_code: str | None = None
    notes: str | None = None
    website: str | None = None
    phone_number: str | None = None
    email_address: str | None = None
    accounts_id: str | None = None
    currency_code: str | None = None
    contract_count: int | None = None
    ticket_count: int | None = None
    customfields: list[CustomField] | None = None
