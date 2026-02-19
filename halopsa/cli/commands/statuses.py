"""Statuses command."""

from .._resource_cmd import make_resource_app

app = make_resource_app(
    name="statuses",
    resource_attr="statuses",
    list_columns=["id", "name", "type", "colour", "treatasopen", "treatasclose", "treatasonhold"],
    detail_columns=[
        "id", "name", "type", "colour", "treatasopen", "treatasclose",
        "treatasonhold", "sequence", "note",
    ],
)
