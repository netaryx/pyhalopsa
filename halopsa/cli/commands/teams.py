"""Teams command."""

from .._resource_cmd import make_resource_app

app = make_resource_app(
    name="teams",
    resource_attr="teams",
    list_columns=["id", "name", "department_name", "ticket_count", "inactive"],
    detail_columns=[
        "id", "name", "department_id", "department_name", "ticket_count",
        "sequence", "description", "inactive", "colour",
    ],
)
