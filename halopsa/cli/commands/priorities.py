"""Priorities command."""

from .._resource_cmd import make_resource_app

app = make_resource_app(
    name="priorities",
    resource_attr="priorities",
    list_columns=["id", "name", "colour", "sequence", "severity", "ishidden"],
    detail_columns=[
        "id", "name", "colour", "sequence", "ishidden", "severity", "noaliases",
    ],
)
