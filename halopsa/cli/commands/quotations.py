"""Quotations command."""

from .._resource_cmd import make_resource_app

app = make_resource_app(
    name="quotations",
    resource_attr="quotations",
    list_columns=["id", "title", "client_name", "status", "total", "date", "expiry_date"],
    detail_columns=[
        "id", "title", "ticket_id", "status", "po_ref", "date", "expiry_date",
        "total", "tax_total_estimate", "note",
        "user_id", "user_name", "site_id", "site_name",
        "client_id", "client_name", "agent_id", "assigned_agent_name",
        "scope", "risk",
    ],
)
