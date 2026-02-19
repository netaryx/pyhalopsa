"""Sites command."""

from .._resource_cmd import make_resource_app

app = make_resource_app(
    name="sites",
    resource_attr="sites",
    list_columns=["id", "name", "client_name", "phonenumber", "inactive", "main_site"],
    detail_columns=[
        "id", "name", "display_name", "summary", "client_id", "client_name",
        "phonenumber", "address", "colour", "inactive", "notes", "sla_id", "main_site",
    ],
)
