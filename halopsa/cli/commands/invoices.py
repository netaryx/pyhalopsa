"""Invoices command."""

from .._resource_cmd import make_resource_app

app = make_resource_app(
    name="invoices",
    resource_attr="invoices",
    list_columns=["id", "invoicenumber", "client_name", "invoice_date", "total", "payment_status"],
    detail_columns=[
        "id", "invoicenumber", "client_id", "client_name", "name",
        "invoice_date", "schedule_date", "dateposted", "posted",
        "total", "subtotal", "tax_total", "payment_status",
        "note", "contract_id", "currency_code",
    ],
)
