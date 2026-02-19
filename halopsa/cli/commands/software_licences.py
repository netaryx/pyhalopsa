"""Software licences command."""

from .._resource_cmd import make_resource_app

app = make_resource_app(
    name="software-licences",
    resource_attr="software_licences",
    list_columns=["id", "name", "client_name", "count", "consumedcount", "start_date", "end_date"],
    detail_columns=[
        "id", "type", "name", "count", "consumedcount",
        "client_id", "client_name", "site_id", "site_name",
        "purchase_price", "recurring_price",
        "supplier_id", "supplier_name", "key", "notes",
        "start_date", "end_date", "inactive",
    ],
)
