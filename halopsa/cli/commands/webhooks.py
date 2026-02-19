"""Webhooks command."""

from .._resource_cmd import make_resource_app

app = make_resource_app(
    name="webhooks",
    resource_attr="webhooks",
    list_columns=["id", "name", "type", "url", "method", "active", "last_status"],
    detail_columns=[
        "id", "name", "type", "url", "content_type", "authentication_type",
        "method", "active", "last_status",
    ],
)
