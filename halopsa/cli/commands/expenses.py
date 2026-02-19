"""Expenses command (no delete)."""

from .._resource_cmd import make_resource_app

app = make_resource_app(
    name="expenses",
    resource_attr="expenses",
    list_columns=["id", "description", "amount", "client_name", "agent_id", "date_added", "type_name"],
    detail_columns=[
        "id", "agent_id", "fault_id", "actionnumber", "description", "amount",
        "date_added", "date_reimbursed", "date_invoiced",
        "invoiceable", "type_name", "client_name", "client_id", "site_id",
    ],
    no_delete=True,
)
