"""Appointments command."""

from .._resource_cmd import make_resource_app

app = make_resource_app(
    name="appointments",
    resource_attr="appointments",
    list_columns=["id", "subject", "start", "end", "agent_id", "ticket_id", "status"],
    detail_columns=[
        "id", "subject", "description", "start", "end", "allday", "location",
        "ticket_id", "agent_id", "appointment_type_id", "status",
        "note", "complete_date", "client_id", "site_id", "user_id",
    ],
)
