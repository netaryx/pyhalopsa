"""Contracts command."""

from .._resource_cmd import make_resource_app

app = make_resource_app(
    name="contracts",
    resource_attr="contracts",
    list_columns=["id", "ref", "client_name", "start_date", "end_date", "contract_status", "billingperiod"],
    detail_columns=[
        "id", "ref", "refextra", "client_id", "client_name",
        "site_id", "site_name", "start_date", "end_date",
        "started", "expired", "billingperiod", "billingdescription",
        "subtype", "status", "sla_id", "next_invoice_date",
        "periodchargeamount", "note", "contract_status",
    ],
)
