"""Timesheets command (no delete)."""

from .._resource_cmd import make_resource_app

app = make_resource_app(
    name="timesheets",
    resource_attr="timesheets",
    list_columns=["id", "agent_name", "date", "actual_hours", "target_hours", "percentage"],
    detail_columns=[
        "id", "agent_id", "agent_name", "date", "start_time", "end_time",
        "target_hours", "actual_hours", "break_hours", "unlogged_hours",
        "work_hours", "percentage", "chargeable_hours",
    ],
    no_delete=True,
)
