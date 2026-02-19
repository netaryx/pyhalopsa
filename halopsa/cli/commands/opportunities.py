"""Opportunities command."""

from .._resource_cmd import make_resource_app

app = make_resource_app(
    name="opportunities",
    resource_attr="opportunities",
    list_columns=["id", "summary", "client_name", "agent_name", "status_name", "opportunityvalue", "probability"],
    detail_columns=[
        "id", "summary", "details", "status_id", "status_name",
        "client_id", "client_name", "agent_id", "agent_name",
        "opportunityvalue", "probability", "weighted_value",
        "pipeline_id", "pipeline_stage_id", "expected_close_date",
        "dateoccurred", "dateclosed",
    ],
)
