"""Ticket types command."""

from .._resource_cmd import make_resource_app

app = make_resource_app(
    name="ticket-types",
    resource_attr="ticket_types",
    list_columns=["id", "name", "prefix", "inactive", "colour"],
    detail_columns=[
        "id", "name", "prefix", "autoincrement", "inactive", "colour",
        "sequence", "default_team_id", "default_agent_id",
        "default_sla_id", "default_priority_id",
        "showinusercatalog", "showintechcatalog",
    ],
)
