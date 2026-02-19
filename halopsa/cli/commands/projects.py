"""Projects command."""

from .._resource_cmd import make_resource_app

app = make_resource_app(
    name="projects",
    resource_attr="projects",
    list_columns=["id", "summary", "client_name", "agent_name", "status_name", "projectcompletionpercentage"],
    detail_columns=[
        "id", "summary", "details", "status_id", "status_name",
        "client_id", "client_name", "agent_id", "agent_name",
        "team_id", "team", "priority_id",
        "projecttimepercentage", "projectcompletionpercentage",
        "projectearlieststart", "projectlatestend",
        "budget", "budgettype", "dateoccurred", "dateclosed",
    ],
)
