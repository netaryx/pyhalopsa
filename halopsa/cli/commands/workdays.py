"""Workdays command."""

from .._resource_cmd import make_resource_app

app = make_resource_app(
    name="workdays",
    resource_attr="workdays",
    list_columns=["id", "name", "timezone", "start", "end"],
    detail_columns=[
        "id", "name", "summary", "timezone", "start", "end",
        "incmonday", "inctuesday", "incwednesday", "incthursday",
        "incfriday", "incsaturday", "incsunday",
    ],
)
