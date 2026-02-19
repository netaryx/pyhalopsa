"""Top levels command."""

from .._resource_cmd import make_resource_app

app = make_resource_app(
    name="top-levels",
    resource_attr="top_levels",
    list_columns=["id", "name", "inactive", "sequence", "colour"],
    detail_columns=[
        "id", "name", "inactive", "sequence", "colour", "note",
    ],
)
