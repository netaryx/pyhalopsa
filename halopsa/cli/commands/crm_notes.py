"""CRM notes command."""

from .._resource_cmd import make_resource_app

app = make_resource_app(
    name="crm-notes",
    resource_attr="crm_notes",
    list_columns=["id", "client_name", "agent_name", "datetime", "type", "pinned"],
    detail_columns=[
        "id", "client_id", "client_name", "agent_id", "agent_name",
        "note", "datetime", "type", "pinned", "opportunity_id",
    ],
)
