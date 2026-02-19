"""Suppliers command."""

from .._resource_cmd import make_resource_app

app = make_resource_app(
    name="suppliers",
    resource_attr="suppliers",
    list_columns=["id", "name", "contact_name", "email_address", "phone_number", "inactive"],
    detail_columns=[
        "id", "name", "toplevel_id", "toplevel_name", "contact_name",
        "email_address", "support_email_address", "ordering_email_address",
        "phone_number", "inactive", "notes", "address", "portal_url",
    ],
)
